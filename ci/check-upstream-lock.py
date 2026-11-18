#!/usr/bin/env python3
"""Offline verification of ci/upstream-lock.json against the spec tree.

For every record in the lock file, checks that:
  * the spec file exists,
  * the FIRST active (non-commented) top-level Name matches the record's
    package,
  * the FIRST active top-level Version matches the locked tag.

Subpackage Name/Version lines and content inside script sections
(%install heredocs, pkgconfig templates, etc.) are never consulted - only
the top-level preamble (everything before the first %package /
%description / %prep section) is examined.

Version values may reference %global macros defined in the same preamble;
they are resolved from the spec itself. An unresolvable macro version is
a hard failure, never a skip.

Usage: check-upstream-lock.py [lock.json] [spec-root]
Exits non-zero on any missing spec or mismatch.
"""

import json
import re
import sys
from pathlib import Path

# Section directives that end the top-level preamble.
SECTION_RE = re.compile(
    r"^%\s*(package|description|prep|build|install|check|clean|files|changelog"
    r"|pre|post|preun|postun|pretrans|posttrans|trigger|verifyscript)\b",
    re.IGNORECASE,
)
TAG_RE = re.compile(r"^\s*(Name|Version|Release)\s*:\s*(.*\S)\s*$")
GLOBAL_RE = re.compile(r"^\s*%global\s+(\w+)\s+(.*\S)\s*$")
DEFINE_RE = re.compile(r"^\s*%define\s+(\w+)\s+(.*\S)\s*$")
MACRO_RE = re.compile(r"%\{(\w+)\}")


def active_lines(spec_path):
    """Yield (lineno, text) of non-comment lines in the top-level preamble."""
    with open(spec_path, encoding="utf-8", errors="replace") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if line.lstrip().startswith("#"):
                continue
            if SECTION_RE.match(line):
                break
            yield lineno, line


def preamble(spec_path):
    """Return (first Name, first Version, first Release, globals dict)."""
    name = version = release = None
    globals_ = {}
    for _lineno, line in active_lines(spec_path):
        m = GLOBAL_RE.match(line) or DEFINE_RE.match(line)
        if m:
            globals_[m.group(1)] = m.group(2)
            continue
        m = TAG_RE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if key == "Name" and name is None:
            name = val
        elif key == "Version" and version is None:
            version = val
        elif key == "Release" and release is None:
            release = val
    return name, version, release, globals_


def resolve(value, globals_, _depth=0):
    """Expand %{macro} refs from globals; returns value or raises."""
    if _depth > 10:
        raise ValueError(f"macro expansion too deep in '{value}'")
    def repl(m):
        macro = m.group(1)
        if macro not in globals_:
            raise KeyError(macro)
        return resolve(globals_[macro], globals_, _depth + 1)
    return MACRO_RE.sub(repl, value)


def check(lock_path, spec_root, report=print):
    lock = json.loads(Path(lock_path).read_text())
    failures = []
    lock_errors = lock.get("errors")
    if lock_errors:
        failures.append(f"lock file records {len(lock_errors)} fetch errors; "
                        f"metadata is incomplete")
    packages = lock.get("packages")
    if not packages:
        failures.append("lock file has no packages")
        packages = []
    seen_pkgs, seen_specs = set(), set()
    for rec in packages:
        pkg, spec_rel = rec.get("package"), rec.get("spec")
        if pkg in seen_pkgs:
            failures.append(f"duplicate package entry '{pkg}'")
        if spec_rel in seen_specs:
            failures.append(f"duplicate spec entry '{spec_rel}'")
        seen_pkgs.add(pkg)
        seen_specs.add(spec_rel)
    ok = 0
    for rec in packages:
        pkg = rec["package"]
        tag = rec["tag"]
        spec_rel = rec["spec"]
        spec_path = Path(spec_root) / spec_rel
        if not spec_path.is_file():
            failures.append(f"{pkg}: spec missing: {spec_rel}")
            continue
        name, version, _release, globals_ = preamble(spec_path)
        if name != pkg:
            failures.append(
                f"{pkg}: top-level Name is '{name}', expected '{pkg}' ({spec_rel})"
            )
            continue
        if version is None:
            failures.append(f"{pkg}: no top-level Version line ({spec_rel})")
            continue
        try:
            resolved = resolve(version, globals_)
        except ValueError as exc:
            failures.append(f"{pkg}: {exc} ({spec_rel})")
            continue
        except KeyError as exc:
            failures.append(
                f"{pkg}: unresolved macro %{{{exc.args[0]}}} in Version "
                f"'{version}' ({spec_rel})"
            )
            continue
        if "%" in resolved:
            failures.append(
                f"{pkg}: Version '{version}' still contains macros after "
                f"expansion ({spec_rel})"
            )
            continue
        if resolved != tag:
            failures.append(
                f"{pkg}: top-level Version '{resolved}' != locked tag '{tag}' "
                f"({spec_rel})"
            )
            continue
        ok += 1
    report(f"checked {ok + len(failures)} lock records: {ok} ok, "
           f"{len(failures)} failed")
    for f in failures:
        report(f"FAIL {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    lock_arg = sys.argv[1] if len(sys.argv) > 1 else "ci/upstream-lock.json"
    root_arg = sys.argv[2] if len(sys.argv) > 2 else "."
    sys.exit(check(lock_arg, root_arg))
