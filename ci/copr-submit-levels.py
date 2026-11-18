#!/usr/bin/env python3
"""Submit SRPMs to COPR in dependency levels (gated tiers).

Production build driver for this specs repo: builds every package on COPR in
dependency order so each build only sees real errors — a tier is submitted
only after the previous tier succeeded AND the COPR chroot repositories have
been regenerated, so in-project BuildRequires always resolve from the repo.

Pipeline on any clone of this repo (prod):
    1. python3 ci/generate-build-order.py   # tiers fra specs' BuildRequires
    2. rpmbuild -bs for hver spec i en container af mål-distroen
       (.el10-SRPM'er i EL10-container, .fcNN i Fedora-container —
       %if 0%{?fedora} evalueres ved SRPM-generering). Se også
       .devin/automation i RytterOS-repoet for den kørende instans.
    3. dette script, én gang pr. chroot-sæt, hver med sin egen --state-fil:
       python3 ci/copr-submit-levels.py \
           --project @SonicDE/SonicDE-dev \
           --srpm-dir /path/to/SRPMS \
           --chroots rhel+epel-10-x86_64 rhel+epel-10-aarch64 ... \
           --state copr-state-el.json

Kræver copr-cli med login (~/.config/copr).  --repo peger på specs-repoet
med build-order.txt (default: repo'et dette script ligger i).

Options:
    --keep-going   fortsæt til næste tier trods fejl (drain-tilstand; pakker
                   der fejler resubmitteres først ved næste manuelle kørsel)
    --retry N      ekstra resubmits pr. fejlet build i samme tier (1)
    --no-reconcile spring monitor-reconcile over ved start
    --tiers a b    kun disse tiers
    --dry-run      vis hvad der ville blive submittet

State i --state (JSON) gør scriptet resume-sikkert: pakker der allerede
er bygget på COPR markeres done og resubmitteres aldrig.
"""
import argparse
import gzip
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# Defaults resolve relative to THIS specs repo so the script is portable:
# copy ci/ with the repo and only --project/--srpm-dir/--state/--chroots
# need to be supplied per build track.
REPO = Path(__file__).resolve().parent.parent
SRPMS = None
STATE = None
PROJECT = "@SonicDE/SonicDE-dev"
RESULTS = ("https://download.copr.fedorainfracloud.org/results/"
           "{project}/{chroot}")


def apply_env(args):
    global SRPMS, STATE, REPO, PROJECT
    if args.srpm_dir:
        SRPMS = Path(args.srpm_dir)
    if args.state:
        STATE = Path(args.state)
    if args.repo:
        REPO = Path(args.repo)
    if args.project:
        PROJECT = args.project


TERMINAL = {"succeeded", "failed", "canceled", "skipped"}
PASS_CHROOT = {"succeeded", "skipped"}
LOG_URL = ("https://download.copr.fedorainfracloud.org/results/"
           "{project}/{chroot}/{build}-{pkg}/builder-live.log.gz")


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def load_tiers():
    order_file = REPO / "build-order.txt"
    tiers = {}
    order = []
    cur = None
    for line in order_file.read_text().splitlines():
        m = re.match(r"^\[(tier\d+)\]", line)
        if m:
            cur = m.group(1)
            tiers[cur] = []
            order.append(cur)
            continue
        line = line.strip()
        if cur and line and not line.startswith("#") and not line.startswith("["):
            tiers[cur].append(line)
    return order, tiers


def spec_name(pkg):
    """Dir name -> spec Name (robust against dir/spec mismatches)."""
    spec = REPO / pkg / f"{pkg}.spec"
    if spec.exists():
        for line in spec.read_text(errors="replace").splitlines():
            m = re.match(r"^Name:\s*(\S+)", line)
            if m and "%{" not in m.group(1):
                return m.group(1).strip()
    return pkg


_exclude_arches = None


def exclude_arches():
    """ark -> [pkgs] fra REPO/ci/exclude-arches.json (ExclusiveArch-pakker).

    COPR faerdigkoerer en chroot for en udelukket ark og melder den "failed"
    (builderen opdager exclusionen forst ved spec-parse) — derfor skal
    orkestreatoren selv springe chrootet over ved submit og ignorere det ved
    gating, ellers blokerer en korrekt exclusion tieren for evigt.
    """
    global _exclude_arches
    if _exclude_arches is None:
        f = REPO / "ci" / "exclude-arches.json"
        try:
            _exclude_arches = {k: v for k, v in
                               json.loads(f.read_text()).items()
                               if not k.startswith("_")}
        except (OSError, json.JSONDecodeError):
            _exclude_arches = {}
    return _exclude_arches


def chroot_arch(chroot):
    """'rhel+epel-10-x86_64_v2' -> 'x86_64_v2'."""
    return chroot.rsplit("-", 1)[-1]


def pkg_chroots(pkg, chroots):
    """Track-chroots minus pakkens ekskluderede ark'er/chroots.

    Noglerne i exclude-arches.json er enten et ark-navn (matcher alle
    chroots med den ark, fx 'ppc64le') eller et fuldt chroot-navn
    (matcher kun det chroot, fx 'epel-10-ppc64le' naar en pakke kan
    bygges til ark'en paa Fedora men ikke paa el10 hvor provideren
    mangler)."""
    ex = exclude_arches()
    return [c for c in chroots
            if pkg not in ex.get(chroot_arch(c), [])
            and pkg not in ex.get(c, [])]


_srpm_index = None


def srpm_index():
    """Map spec Name -> newest SRPM (exact NAME match from RPM header)."""
    global _srpm_index
    if _srpm_index is not None:
        return _srpm_index
    idx = {}
    for p in SRPMS.glob("*.src.rpm"):
        q = run(["rpm", "-qp", "--queryformat",
                 "%{NAME}|%{EPOCHNUM}|%{VERSION}|%{RELEASE}", str(p)])
        if q.returncode != 0:
            continue
        parts = q.stdout.split("|")
        if len(parts) != 4:
            continue
        name, epoch, ver, rel = parts[0], int(parts[1]), parts[2], parts[3]
        key = (epoch, rpmver(ver),
               rpmver(re.sub(r'\.(fc|el|al|rhel)\d+.*$', '', rel)),
               p.stat().st_mtime)
        if name not in idx or key > idx[name][0]:
            idx[name] = (key, p)
    _srpm_index = {n: p for n, (k, p) in idx.items()}
    return _srpm_index


def newest_srpm(name):
    return srpm_index().get(name)


def rpmver(s):
    # crude rpm-ish version key: split numeric/alpha runs
    parts = re.split(r"([0-9]+)", s)
    return tuple(int(p) if p.isdigit() else p for p in parts)


def copr(*args):
    return run(["copr-cli", *args])


def submit(srpm, chroots):
    # uden --chroots bygges på projektets default-chroots
    cmd = ["build", PROJECT, str(srpm), "--nowait"]
    for c in chroots or []:
        cmd += ["-r", c]
    r = copr(*cmd)
    m = re.search(r"Created builds: (\d+)", r.stdout)
    if m:
        return int(m.group(1)), None
    return None, (r.stdout + r.stderr).strip()


def status(build_id):
    r = copr("status", str(build_id))
    return r.stdout.strip()


def chroot_states(build_id):
    """{chroot: {"state": s, "ended_on": ts}} via api_3; {} on failure."""
    out = {}
    try:
        url = (f"https://copr.fedorainfracloud.org/api_3/build/{build_id}")
        d = json.loads(urllib.request.urlopen(url, timeout=30).read())
        for ch in d.get("chroots", []):
            cu = (f"https://copr.fedorainfracloud.org/api_3/build-chroot/"
                  f"{build_id}/{ch}")
            cd = json.loads(urllib.request.urlopen(cu, timeout=30).read())
            out[ch] = {"state": cd.get("state", "?"),
                       "ended_on": cd.get("ended_on")}
    except Exception:
        pass
    return out


def monitor_latest(project):
    """pkg -> {chroot: state, build_id} for the LATEST build of each package."""
    r = copr("monitor", project)
    try:
        entries = json.loads(r.stdout)
    except json.JSONDecodeError:
        return {}
    latest = {}
    for e in entries:
        p = latest.setdefault(e["name"], {"build_id": e["build_id"], "chroots": {}})
        if e["build_id"] > p["build_id"]:
            p["build_id"] = e["build_id"]
            p["chroots"] = {}
        if e["build_id"] == p["build_id"]:
            p["chroots"][e["chroot"]] = e["state"]
    return latest


def _repomd_root(chroot):
    url = (RESULTS.format(project=PROJECT, chroot=chroot)
           + f"/repodata/repomd.xml?nocache={time.time_ns()}")
    req = urllib.request.Request(url, headers={
        "Cache-Control": "no-cache", "Pragma": "no-cache"})
    try:
        data = urllib.request.urlopen(req, timeout=30).read()
        return ET.fromstring(data)
    except Exception:
        return None


def repomd_revision(chroot):
    root = _repomd_root(chroot)
    if root is None:
        return None
    ns = {"r": "http://linux.duke.edu/metadata/repo"}
    rev = root.findtext("r:revision", namespaces=ns)
    if rev:
        return int(rev)
    for d in root.findall("r:data", ns):
        ts = d.findtext("r:timestamp", namespaces=ns)
        if ts:
            return int(ts)
    return None


def primary_href(chroot):
    """Content-hash af primary.xml — ændrer sig ved hver repo-regen.
    Pulp-backend'en bumper ikke længere repomd <revision>, så
    href-skift er det pålidelige regen-signal."""
    root = _repomd_root(chroot)
    if root is None:
        return None
    ns = {"r": "http://linux.duke.edu/metadata/repo"}
    for d in root.findall("r:data", ns):
        if d.get("type") == "primary":
            loc = d.find("r:location", ns)
            if loc is not None:
                return loc.get("href")
    return None


def primary_content(chroot, href):
    url = RESULTS.format(project=PROJECT, chroot=chroot) + "/" + href
    req = urllib.request.Request(url, headers={
        "Cache-Control": "no-cache", "Pragma": "no-cache"})
    try:
        return gzip.decompress(urllib.request.urlopen(req, timeout=60).read())
    except Exception:
        return None


def wait_repo_per_chroot(chroot_end, baselines=None, expect_vrs=None,
                         timeout=1800, poll=30):
    """Vent til hver chroots repodata er regenereret efter chroot'ets eget
    sidste build-sluttidspunkt. En regen efter build-end inkluderer alt
    færdigt indhold, så pass-kriterierne er: revision >= end, ELLER
    primary-href ændret siden build-end (baselines), ELLER at tier'ens
    versionsstrenge allerede findes i primary.xml (dækker regen der nåede
    at fuldføre før baseline-snapshot)."""
    baselines = baselines or {}
    expect_vrs = expect_vrs or []
    pending = dict(chroot_end)
    checked = {}   # ch -> href hvis indhold allerede crawlet
    waited = 0
    while pending and waited < timeout:
        done_now = set()
        for ch, since in pending.items():
            rev = repomd_revision(ch)
            if rev and rev >= since:
                done_now.add(ch)
                continue
            href = primary_href(ch)
            base = baselines.get(ch)
            if href and base and href != base:
                done_now.add(ch)
                continue
            if href and expect_vrs and checked.get(ch) != href:
                checked[ch] = href
                body = primary_content(ch, href)
                if body and any(v.encode() in body for v in expect_vrs):
                    done_now.add(ch)
        for ch in done_now:
            del pending[ch]
        if not pending:
            return True
        time.sleep(poll)
        waited += poll
        print(f"  repo-vent: {sorted(pending)} ({waited}s)", flush=True)
    return not pending


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chroots", nargs="+", default=None,
                    help="chroots at bygge for (default: projektets egne)")
    ap.add_argument("--tiers", nargs="+", default=None)
    ap.add_argument("--poll", type=int, default=120)
    ap.add_argument("--max-wait", type=int, default=60 * 60 * 10)
    ap.add_argument("--repo-wait", type=int, default=1800,
                    help="max sek vent på COPR repo-regenerering pr. tier")
    ap.add_argument("--retry", type=int, default=1,
                    help="ekstra resubmits pr. fejlet build i samme tier")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--srpm-dir", required=True)
    ap.add_argument("--repo", default=None,
                    help="specs-repo med build-order.txt "
                         "(default: repo'et dette script ligger i)")
    ap.add_argument("--project", default=PROJECT)
    ap.add_argument("--state", required=True)
    ap.add_argument("--keep-going", action="store_true",
                    help="fortsæt til næste tier trods fejl (drain-tilstand)")
    ap.add_argument("--burst", action="store_true",
                    help="submit ALLE ikke-færdige pakker med det samme "
                         "(alle tiers på én gang) — til genbygningsbølger "
                         "hvor afhængighederne allerede ligger i repo'et. "
                         "Vente-loop'en markerer stadig done/failed "
                         "pr. pakke; --keep-going fjerner stop-ved-fejl.")
    ap.add_argument("--no-reconcile", action="store_true",
                    help="spring monitor-reconcile over ved start")
    a = ap.parse_args()
    apply_env(a)

    order, tiers = load_tiers()
    state = {"builds": {}, "done_pkgs": [], "failed": {}}
    if STATE.exists():
        state = json.loads(STATE.read_text())
        state.setdefault("failed", {})
    done = set(state["done_pkgs"])

    # Reconcile: mark every package whose latest COPR build succeeded on all
    # requested chroots as done — covers builds from older states/runs.
    if not a.no_reconcile:
        latest = monitor_latest(PROJECT)
        got = 0
        for tier in order:
            for pkg in tiers[tier]:
                if pkg in done:
                    continue
                name = spec_name(pkg)
                ent = latest.get(name) or latest.get(pkg)
                if not ent:
                    continue
                chs = ent["chroots"]
                want = pkg_chroots(pkg, a.chroots) or list(chs)
                # "skipped" counts as pass: COPR skips chroots excluded by the
                # SRPM's ExclusiveArch (e.g. qtwebengine on ppc64le).
                if all(chs.get(c) in PASS_CHROOT for c in want):
                    done.add(pkg)
                    state["builds"].setdefault(pkg, {"id": ent["build_id"]})
                    got += 1
        if got:
            print(f"reconcile: {got} pakker allerede bygget på COPR", flush=True)
            state["done_pkgs"] = sorted(done)
            STATE.write_text(json.dumps(state, indent=1))

    if a.burst:
        # Genbygningsbølge: alle BuildRequires resolves mod repo'ets
        # nuværende indhold, så tier-rækkefølgen er unødvendig. Submit
        # alt med det samme; den normale loop nedenfor samler dem op i
        # `pending` og markerer done/failed efterhånden som builds lander.
        burst_n = 0
        for tier in order:
            if a.tiers and tier not in a.tiers:
                continue
            for pkg in tiers[tier]:
                if pkg in done:
                    continue
                name = spec_name(pkg)
                ent = state["builds"].get(pkg)
                if ent and status(ent["id"]) not in TERMINAL:
                    continue          # allerede i luften
                srpm = newest_srpm(name)
                if not srpm:
                    print(f"burst {pkg}: INGEN SRPM for {name}", flush=True)
                    state["failed"][pkg] = "ingen-srpm"
                    continue
                pchroots = pkg_chroots(pkg, a.chroots)
                if not pchroots:
                    done.add(pkg)     # ekskluderet fra alle spor-chroots
                    continue
                print(f"burst {pkg} <- {srpm.name}", flush=True)
                if a.dry_run:
                    continue
                bid, err = submit(srpm, pchroots)
                if bid:
                    state["builds"][pkg] = {"id": bid, "srpm": srpm.name,
                                            "tier": tier, "chroots": pchroots}
                    burst_n += 1
                else:
                    print(f"  FEJL ved burst-submit {pkg}: {err}", flush=True)
                    state["failed"][pkg] = f"submit: {err[:200]}"
                time.sleep(2)  # skån API'et
                STATE.write_text(json.dumps(state, indent=1))
        state["done_pkgs"] = sorted(done)
        STATE.write_text(json.dumps(state, indent=1))
        print(f"BURST: {burst_n} pakker submittet på én gang", flush=True)

    for tier in order:
        if a.tiers and tier not in a.tiers:
            continue
        pkgs = tiers[tier]
        attempts = {}          # pkg -> submissions this pass
        pending = []
        t_submit = time.time()
        for pkg in pkgs:
            if pkg in done:
                continue
            name = spec_name(pkg)
            srpm = newest_srpm(name)
            if not srpm:
                print(f"[{tier}] {pkg}: INGEN SRPM for {name}", flush=True)
                state["failed"][pkg] = "ingen-srpm"
                continue
            ent = state["builds"].get(pkg)
            if ent:
                st = status(ent["id"])
                if st == "succeeded":
                    done.add(pkg)
                    state["done_pkgs"] = sorted(done)
                    continue
                if st in TERMINAL:
                    # failed/canceled pga. udelukket ark taeller som done
                    chs0 = chroot_states(ent["id"])
                    allowed0 = pkg_chroots(pkg, a.chroots or list(chs0))
                    if (chs0 and all(i["state"] in PASS_CHROOT
                                     for c, i in chs0.items()
                                     if c in allowed0)):
                        done.add(pkg)
                        state["done_pkgs"] = sorted(done)
                        continue
                else:
                    pending.append(pkg)      # løbende build, afvent
                    continue
            pchroots = pkg_chroots(pkg, a.chroots)
            if not pchroots:
                # Pakken er ekskluderet fra ALLE dette spors chroots (fx
                # distro-leverede qt6-*/kf6-* paa Fedora): ingen submit —
                # copr build uden -r ville ramme default-chroots.
                print(f"[{tier}] {pkg}: ekskluderet fra alle chroots, "
                      "springer over", flush=True)
                done.add(pkg)
                state["done_pkgs"] = sorted(done)
                continue
            print(f"[{tier}] submit {pkg} <- {srpm.name}", flush=True)
            if a.dry_run:
                continue
            bid, err = submit(srpm, pchroots)
            attempts[pkg] = attempts.get(pkg, 0) + 1
            if bid:
                state["builds"][pkg] = {"id": bid, "srpm": srpm.name,
                                        "tier": tier, "chroots": pchroots}
                pending.append(pkg)
            else:
                print(f"  FEJL ved submit {pkg}: {err}", flush=True)
                state["failed"][pkg] = f"submit: {err[:200]}"
            STATE.write_text(json.dumps(state, indent=1))
            time.sleep(2)  # skån API'et
        STATE.write_text(json.dumps(state, indent=1))
        if a.dry_run:
            continue

        # vent på tier (med --retry gen-submits af fejlede)
        waited = 0
        last_end = t_submit
        # hvert chroots repo regenereres efter chroot'ets eget ended_on —
        # track per-chroot sluttidspunkt så repo-vent ikke hænger på
        # tidligt-færdige chroots
        chroot_end = {}
        chroot_base = {}
        had_completion = False
        while pending and waited < a.max_wait:
            time.sleep(a.poll)
            waited += a.poll
            still = []
            for pkg in pending:
                st = status(state["builds"][pkg]["id"])
                if st in TERMINAL:
                    had_completion = True
                    chs = chroot_states(state["builds"][pkg]["id"])
                    now = time.time()
                    for c, info in chs.items():
                        end = info.get("ended_on") or now
                        if end > chroot_end.get(c, 0):
                            chroot_end[c] = end
                            # pre-regen snapshot: enhver href-ændring
                            # herefter beviser regen med dette build
                            h = primary_href(c)
                            if h:
                                chroot_base[c] = h
                    if chs:
                        last_end = max(chroot_end.values())
                    else:
                        last_end = max(last_end, now)
                    print(f"[{tier}] {pkg}: {st}", flush=True)
                    # En build med "failed" paa en af pakken ekskluderede
                    # ark'er er stadig en succes naar alle tilladte chroots
                    # er i PASS_CHROOT — COPR melder exclusion som failure.
                    allowed = pkg_chroots(pkg, a.chroots or list(chs))
                    ok = (st == "succeeded" or
                          (chs and all(i["state"] in PASS_CHROOT
                                       for c, i in chs.items()
                                       if c in allowed)))
                    if ok:
                        done.add(pkg)
                        state["failed"].pop(pkg, None)
                    else:
                        state["failed"][pkg] = st
                        if chs:
                            bad = {c: i["state"] for c, i in chs.items()
                                   if i["state"] not in PASS_CHROOT
                                   and c in allowed}
                            print(f"  chroots: {bad}", flush=True)
                        # retry direkte mens resten af tier'en bygger
                        if attempts.get(pkg, 1) <= a.retry and not a.dry_run:
                            srpm = newest_srpm(spec_name(pkg))
                            bid, err = submit(srpm, allowed)
                            if bid:
                                attempts[pkg] = attempts.get(pkg, 0) + 1
                                state["builds"][pkg] = {
                                    "id": bid, "srpm": srpm.name,
                                    "tier": tier, "chroots": allowed}
                                still.append(pkg)
                                print(f"  retry {pkg} (forsøg "
                                      f"{attempts[pkg]}): build {bid}",
                                      flush=True)
                            else:
                                print(f"  retry-submit fejlede: {err}", flush=True)
                else:
                    still.append(pkg)
            pending = still
            STATE.write_text(json.dumps(state, indent=1))
            print(f"[{tier}] venter: {len(pending)} tilbage ({waited}s)",
                  flush=True)

        state["done_pkgs"] = sorted(done)
        STATE.write_text(json.dumps(state, indent=1))
        fails = [p for p in pkgs if p not in done]
        if fails:
            print(f"[{tier}] uafsluttede: {fails}", flush=True)
            if not a.keep_going:
                print("STOPPER — ret fejlene og kør scriptet igen "
                      "(genoptager automatisk).", flush=True)
                for p in fails:
                    ent = state["builds"].get(p, {})
                    bid = ent.get("id", "?")
                    for c in (a.chroots or ent.get("chroots") or []):
                        print(f"  {p}: {LOG_URL.format(project=PROJECT, chroot=c, build=bid, pkg=spec_name(p))}",
                              flush=True)
                sys.exit(2)

        # vent til hver chroots repo er regenereret efter DETS sidste build
        # i tier'en — uafhængige per-chroot-regens. expect_vrs = versions-
        # tokens fra tier'ens SRPM'er bruges til indholds-check af primary.xml
        expect_vrs = []
        for p in pkgs:
            s = state["builds"].get(p, {}).get("srpm", "")
            m = re.match(r".*-([0-9][^-]*)-([0-9]+)", s)
            if m:
                expect_vrs.append(f"-{m.group(1)}-{m.group(2)}.")
        if (not a.dry_run and not a.burst and had_completion and chroot_end
                and not wait_repo_per_chroot(chroot_end, chroot_base,
                                             expect_vrs,
                                             timeout=a.repo_wait)):
            print(f"[{tier}] ADVARSEL: repo ikke regenereret inden "
                  f"{a.repo_wait}s — fortsætter alligevel", flush=True)

    print("FÆRDIG — alle valgte tiers submittet og gennemført.", flush=True)


if __name__ == "__main__":
    main()
