#!/usr/bin/env python3
"""Preserve EL10's HiDPI icon symlinks without discarding distinct artwork."""

import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import stat


def tree_signature(root):
    entries = {}
    for directory, subdirs, files in os.walk(root, followlinks=False):
        for name in subdirs + files:
            path = Path(directory) / name
            mode = path.lstat().st_mode
            kind = stat.S_IFMT(mode)
            if stat.S_ISLNK(mode):
                content = os.readlink(path)
            elif stat.S_ISREG(mode):
                with path.open("rb") as stream:
                    content = hashlib.file_digest(stream, "sha256").hexdigest()
            elif stat.S_ISDIR(mode):
                content = None
            else:
                raise ValueError(f"Unsupported icon entry: {path}")
            entries[path.relative_to(root)] = (kind, stat.S_IMODE(mode), content)
    return entries


def normalize(icons_root):
    replacements = []
    for theme in ("breeze", "breeze-dark"):
        for variant in sorted((icons_root / theme).glob("*/*@*x")):
            match = re.fullmatch(r"([0-9]+)@[23]x", variant.name)
            if not match or variant.is_symlink():
                continue
            target = variant.with_name(match.group(1))
            if not variant.is_dir() or not target.is_dir() or target.is_symlink():
                raise ValueError(f"Missing real backing directory for {variant}")
            if stat.S_IMODE(variant.stat().st_mode) != stat.S_IMODE(target.stat().st_mode):
                raise ValueError(f"Directory permissions differ: {variant}")
            if tree_signature(variant) != tree_signature(target):
                raise ValueError(f"Distinct HiDPI artwork must not be discarded: {variant}")
            replacements.append((variant, target.name))
    # Validate every tree first, so an unexpected future source fails untouched.
    for variant, target in replacements:
        shutil.rmtree(variant)
        variant.symlink_to(target, target_is_directory=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("icons_root", type=Path)
    args = parser.parse_args()
    if not args.icons_root.is_dir() or args.icons_root.is_symlink():
        parser.error("icons_root must be a real buildroot directory")
    normalize(args.icons_root)


if __name__ == "__main__":
    main()
