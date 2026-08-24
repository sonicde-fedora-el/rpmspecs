#!/usr/bin/env python3
"""Recompute build-order.txt tiers from the BuildRequires of every spec.

The tiers generated from the SonicDE builder dependency graph only describe
source-level dependencies; RPM build dependencies are wider (devel subpackages,
cmake config files, pkgconfig files).  This derives the tiers from the specs
themselves so a tier only needs packages from earlier tiers.
"""
import glob
import os
import re
import subprocess
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

specs = sorted(glob.glob(os.path.join(REPO, "*", "*.spec")))
specs = [s for s in specs if os.path.basename(s)[:-5] == os.path.basename(os.path.dirname(s))]

provides = {}   # capability -> package dir name
brs = defaultdict(set)


def parse(spec):
    pkg = os.path.basename(spec)[:-5]
    out = subprocess.run(["rpmspec", "-P", spec], capture_output=True, text=True).stdout
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
        elif s.startswith("%") and re.match(r"%(prep|build|install|conf|check|changelog|description|post|pre)", s):
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
    return pkg


pkgs = [parse(s) for s in specs]

edges = defaultdict(set)
for pkg in pkgs:
    for cap in brs[pkg]:
        owner = provides.get(cap)
        if owner and owner != pkg:
            edges[pkg].add(owner)

# longest-path tier assignment, ignoring back edges of cycles
tier = {}
state = {}


def depth(pkg, stack=()):
    if pkg in tier:
        return tier[pkg]
    if pkg in stack:
        return 0
    d = 0
    for dep in edges[pkg]:
        d = max(d, depth(dep, stack + (pkg,)) + 1)
    tier[pkg] = d
    return d


sys.setrecursionlimit(10000)
for pkg in pkgs:
    depth(pkg)

cycles = []
for pkg in pkgs:
    for dep in edges[pkg]:
        if tier[dep] >= tier[pkg]:
            cycles.append((pkg, dep))

groups = defaultdict(list)
for pkg in pkgs:
    groups[tier[pkg]].append(pkg)

lines = [
    "# Build order for the SonicDE packages, derived from the BuildRequires of",
    "# every spec in this repository (see ci/generate-build-order.py).",
    "#",
    "# Packages inside one tier are independent and can be built in parallel;",
    "# the tiers themselves must be built in order.",
    "",
]
for i, t in enumerate(sorted(groups), start=1):
    lines.append(f"[tier{i}]")
    lines += sorted(groups[t])
    lines.append("")

open(os.path.join(REPO, "build-order.txt"), "w").write("\n".join(lines).rstrip() + "\n")
print("tiers:", len(groups), "packages:", len(pkgs))
if cycles:
    print("dependency cycles (built with the earlier tier's package from the repo):")
    for a, b in sorted(set(cycles)):
        print(f"  {a} <- {b}")
