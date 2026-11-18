#!/usr/bin/env python3
"""Shared enumeration of the active spec files in this repository.

Retired KDE specs listed in ci/retired-kde-specs.json stay on disk as
reference but are excluded from the active build selection.  Every helper
that enumerates specs (parse check, build-order generator, build plan)
must go through here so the exclusion set can never drift.

Usage:
    import specs
    for path in specs.active(REPO): ...
"""

import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RETIRED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "retired-kde-specs.json")


def retired(repo=REPO):
    """Return the retired spec paths (relative, e.g. 'pkg/pkg.spec')."""
    with open(RETIRED_FILE) as fh:
        entries = json.load(fh)
    if not isinstance(entries, list) or not all(
            isinstance(e, str) for e in entries):
        raise ValueError(f"{RETIRED_FILE} must be a JSON array of strings")
    for rel in entries:
        full = os.path.join(repo, rel)
        if not os.path.isfile(full):
            raise FileNotFoundError(f"retired spec missing: {rel}")
    return sorted(entries)


def all_specs(repo=REPO):
    """Every */*.spec in the repo as sorted relative paths."""
    out = []
    for entry in sorted(os.listdir(repo)):
        sub = os.path.join(repo, entry)
        if not os.path.isdir(sub):
            continue
        for name in sorted(os.listdir(sub)):
            if name.endswith(".spec"):
                out.append(f"{entry}/{name}")
    return out


def active(repo=REPO, check_layout=True):
    """Active spec paths (all specs minus retired), sorted relative paths.

    With check_layout, each active spec must sit in a directory named
    after its basename (pkg/pkg.spec) - mismatches raise ValueError.
    """
    ret = set(retired(repo))
    act = []
    for rel in all_specs(repo):
        if rel in ret:
            continue
        if check_layout:
            stem = os.path.basename(rel)[:-5]
            parent = os.path.basename(os.path.dirname(rel))
            if stem != parent:
                raise ValueError(
                    f"spec {rel} does not sit in directory '{stem}'")
        act.append(rel)
    return act


if __name__ == "__main__":
    for rel in active():
        print(rel)
