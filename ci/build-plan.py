#!/usr/bin/env python3
"""Compute which packages to build.

Three modes:
  ci/build-plan.py                          # full rebuild (all packages)
  ci/build-plan.py <base> <head>            # incremental: diff base..head
  ci/build-plan.py --missing                # build packages not in Forgejo repo

Outputs JSON: {"tiers": [...], "changed": [...], "total": N}
"""
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER_FILE = os.path.join(REPO, "build-order.txt")


def parse_build_order():
    tiers = []
    current_tier = None
    current_pkgs = []
    with open(ORDER_FILE) as f:
        for line in f:
            line = line.strip()
            m = re.match(r"^\[tier(\d+)\]$", line)
            if m:
                if current_tier is not None:
                    tiers.append((current_tier, current_pkgs))
                current_tier = int(m.group(1))
                current_pkgs = []
            elif line and not line.startswith("#"):
                current_pkgs.append(line)
    if current_tier is not None:
        tiers.append((current_tier, current_pkgs))
    return tiers


def build_dependency_graph():
    specs = sorted(glob.glob(os.path.join(REPO, "*", "*.spec")))
    specs = [s for s in specs
             if os.path.basename(s)[:-5] == os.path.basename(os.path.dirname(s))]

    provides = {}
    brs = defaultdict(set)

    for spec in specs:
        pkg = os.path.basename(spec)[:-5]
        out = subprocess.run(
            ["rpmspec", "-P", spec], capture_output=True, text=True
        ).stdout
        if not out:
            out = open(spec, errors="replace").read()
        names = {pkg}
        in_files = False
        for line in out.splitlines():
            s = line.strip()
            m = re.match(r"%package\s+(?:-n\s+(\S+)|(\S+))", s)
            if m:
                names.add(m.group(1) or f"{pkg}-{m.group(2)}")
                continue
            if s.startswith("%files"):
                in_files = True
            elif s.startswith("%") and re.match(
                r"%(prep|build|install|conf|check|changelog|description|post|pre)", s
            ):
                in_files = s.startswith("%files")
            m = re.match(r"(Provides|BuildRequires)\s*:\s*(.+)", s)
            if m:
                for dep in re.split(r"\s+(?=[A-Za-z_%(/])", m.group(2).strip()):
                    cap = dep.split()[0].replace("%{?_isa}", "").strip()
                    if not cap or cap.startswith(("%", "(")):
                        continue
                    if m.group(1) == "Provides":
                        names.add(cap)
                    else:
                        brs[pkg].add(cap)
            if in_files:
                for cm in re.findall(r"/cmake/([A-Za-z0-9_.+-]+)/?", s):
                    names.add(f"cmake({cm})")
                for pc in re.findall(r"/([A-Za-z0-9_.+-]+)\.pc\b", s):
                    names.add(f"pkgconfig({pc})")
        for n in names:
            provides.setdefault(n, pkg)

    forward = defaultdict(set)
    for pkg, caps in brs.items():
        for cap in caps:
            owner = provides.get(cap)
            if owner and owner != pkg:
                forward[pkg].add(owner)

    return forward


def compute_affected(changed_pkgs, forward_graph):
    reverse = defaultdict(set)
    for pkg, deps in forward_graph.items():
        for dep in deps:
            reverse[dep].add(pkg)

    affected = set(changed_pkgs)
    queue = list(changed_pkgs)
    while queue:
        pkg = queue.pop(0)
        for dependent in reverse.get(pkg, ()):
            if dependent not in affected:
                affected.add(dependent)
                queue.append(dependent)
    return affected


def get_spec_version(pkg):
    """Return (version, release) for a package from its spec."""
    spec = os.path.join(REPO, pkg, f"{pkg}.spec")
    out = subprocess.run(
        ["rpmspec", "-q", "--srpm",
         "--queryformat", "%{VERSION} %{RELEASE}", spec],
        capture_output=True, text=True
    ).stdout.strip()
    if " " in out:
        return out.split(" ", 1)
    return None, None


def query_forgejo_packages():
    """Query the Forgejo RPM registry for existing packages.

    Returns a dict: {package_name: {(version, release)}} for all subpackages.
    """
    forgejo_url = os.environ.get("FORGEJO_URL", "")
    owner = os.environ.get("FORGEJO_OWNER", "")
    if not forgejo_url or not owner:
        return {}

    packages = {}
    page = 1
    while True:
        url = f"{forgejo_url}/api/packages/{owner}/rpm?page={page}&limit=50"
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
        except Exception:
            break
        if not data:
            break
        for entry in data:
            name = entry.get("name", "")
            if not name:
                continue
            # Strip arch suffix and subpackage qualifiers to map back to source pkg
            ver = entry.get("version", "")
            rel = ""
            # Forgejo RPM packages store version-release in the version field
            if "-" in ver:
                ver, rel = ver.rsplit("-", 1)
            packages.setdefault(name, set()).add((ver, rel))
        page += 1
    return packages


def compute_missing(all_pkgs, tiers, forgejo_packages):
    """Find packages whose spec version is not in the Forgejo registry."""
    if not forgejo_packages:
        return set(all_pkgs)

    missing = set()
    for pkg in all_pkgs:
        ver, rel = get_spec_version(pkg)
        if ver is None:
            continue
        # Check if the main package or any subpackage with this version exists
        found = False
        for name, versions in forgejo_packages.items():
            # Match either the exact package name or a subpackage (pkg-foo)
            if name == pkg or name.startswith(f"{pkg}-"):
                for (fv, fr) in versions:
                    if fv == ver:
                        found = True
                        break
            if found:
                break
        if not found:
            missing.add(pkg)
    return missing


def main():
    tiers = parse_build_order()
    all_pkgs = [pkg for _, pkgs in tiers for pkg in pkgs]

    # Determine mode
    if len(sys.argv) >= 3 and sys.argv[1] != "--missing":
        # Incremental: diff base..head
        base, head = sys.argv[1], sys.argv[2]
        changed_files = subprocess.run(
            ["git", "diff", "--name-only", base, head],
            capture_output=True, text=True, cwd=REPO,
        ).stdout.split()
        changed_pkgs = {
            os.path.basename(f).replace(".spec", "")
            for f in changed_files if f.endswith(".spec")
        }
        for f in changed_files:
            if "/" in f and not f.endswith(".spec"):
                pkg = f.split("/")[0]
                if pkg in all_pkgs:
                    changed_pkgs.add(pkg)
    elif len(sys.argv) >= 2 and sys.argv[1] == "--missing":
        # Missing mode: build packages not in Forgejo registry
        forgejo_pkgs = query_forgejo_packages()
        changed_pkgs = compute_missing(all_pkgs, tiers, forgejo_pkgs)
    else:
        # Full rebuild
        changed_pkgs = set(all_pkgs)

    if not changed_pkgs:
        print(json.dumps({"tiers": [], "changed": [], "total": 0}))
        return

    forward = build_dependency_graph()
    affected = compute_affected(changed_pkgs, forward)

    plan = []
    for tier_num, pkgs in tiers:
        tier_affected = [p for p in pkgs if p in affected]
        if tier_affected:
            plan.append({"tier": tier_num, "packages": sorted(tier_affected)})

    result = {
        "tiers": plan,
        "changed": sorted(changed_pkgs),
        "total": sum(len(t["packages"]) for t in plan),
    }
    print(json.dumps(result))


if __name__ == "__main__":
    main()
