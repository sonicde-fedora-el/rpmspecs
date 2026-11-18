#!/usr/bin/env python3
"""Unit tests for normalize-hidpi-layout.py (stdlib only)."""

import importlib.util
import os
import shutil
import stat
import tempfile
import unittest
from pathlib import Path


HELPER_PATH = Path(__file__).resolve().with_name("normalize-hidpi-layout.py")


def load_helper():
    spec = importlib.util.spec_from_file_location(
        "normalize_hidpi_layout", HELPER_PATH
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


helper = load_helper()


def snapshot(root):
    result = {}
    for directory, subdirs, files in os.walk(root, followlinks=False):
        for name in subdirs + files:
            path = Path(directory) / name
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                value = ("link", os.readlink(path))
            elif stat.S_ISDIR(mode):
                value = ("dir", stat.S_IMODE(mode))
            else:
                value = ("file", stat.S_IMODE(mode), path.read_bytes())
            result[path.relative_to(root)] = value
    return result


class NormalizeHiDpiLayoutTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.icons = Path(self.tmp.name)

    def add_tree(self, theme, category, size, content=b"<svg>icon</svg>",
                 leaf_link=None):
        base = self.icons / theme / category / size
        base.mkdir(parents=True)
        (base / "icon.svg").write_bytes(content)
        if leaf_link:
            (base / leaf_link).symlink_to("icon.svg")
        return base

    def duplicate(self, base, variant):
        copy = base.with_name(variant)
        shutil.copytree(base, copy, symlinks=True)
        return copy

    def test_helper_loads_without_running_cli(self):
        self.assertTrue(callable(helper.normalize))
        self.assertNotEqual(helper.__name__, "__main__")

    def test_duplicate_variants_become_relative_symlinks(self):
        base = self.add_tree("breeze", "actions", "16", leaf_link="alias.svg")
        dup2x = self.duplicate(base, "16@2x")
        dup3x = self.duplicate(base, "16@3x")
        dark = self.add_tree("breeze-dark", "status", "22",
                             content=b"<svg>dark</svg>")
        dark_dup = self.duplicate(dark, "22@3x")

        helper.normalize(self.icons)

        for variant, target in ((dup2x, "16"), (dup3x, "16"),
                                (dark_dup, "22")):
            self.assertTrue(variant.is_symlink())
            self.assertEqual(os.readlink(variant), target)
            # Contents remain reachable through the new symlink.
            self.assertEqual((variant / "icon.svg").read_bytes(),
                             (variant.with_name(target) / "icon.svg")
                             .read_bytes())
        self.assertEqual(os.readlink(dup2x / "alias.svg"), "icon.svg")
        # Real backing directories are untouched.
        self.assertTrue(base.is_dir() and not base.is_symlink())
        self.assertTrue(dark.is_dir() and not dark.is_symlink())

        after_first = snapshot(self.icons)
        helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), after_first)

    def test_later_bad_candidate_blocks_all_replacements(self):
        good_base = self.add_tree("breeze", "actions", "16")
        good_dup = self.duplicate(good_base, "16@2x")
        bad_base = self.add_tree("breeze", "emblems", "22")
        bad_dup = self.duplicate(bad_base, "22@2x")
        (bad_dup / "icon.svg").write_bytes(b"<svg>distinct</svg>")

        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        # The earlier valid candidate must not have been replaced.
        self.assertTrue(good_dup.is_dir() and not good_dup.is_symlink())
        self.assertEqual(snapshot(self.icons), before)

    def test_extra_or_missing_relative_file_raises(self):
        base = self.add_tree("breeze", "apps", "32")
        dup = self.duplicate(base, "32@2x")

        (dup / "extra.svg").write_bytes(b"<svg>extra</svg>")
        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

        (dup / "extra.svg").unlink()
        (dup / "icon.svg").unlink()
        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

    def test_missing_backing_target_raises_without_change(self):
        orphan = self.icons / "breeze" / "mimetypes" / "64@2x"
        orphan.mkdir(parents=True)
        (orphan / "doc.svg").write_bytes(b"<svg>doc</svg>")

        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

    def test_no_variant_directories_is_noop(self):
        self.add_tree("breeze", "actions", "16")
        before = snapshot(self.icons)
        helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

    def test_file_permission_mismatch_raises(self):
        base = self.add_tree("breeze", "devices", "16")
        dup = self.duplicate(base, "16@2x")
        (dup / "icon.svg").chmod(0o600)

        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

    def test_directory_permission_mismatch_raises(self):
        base = self.add_tree("breeze", "devices", "16")
        dup = self.duplicate(base, "16@2x")
        dup.chmod(0o700)

        before = snapshot(self.icons)
        with self.assertRaises(ValueError):
            helper.normalize(self.icons)
        self.assertEqual(snapshot(self.icons), before)

    def test_existing_symlink_variant_left_intact(self):
        base = self.add_tree("breeze", "actions", "16")
        linked = base.with_name("16@2x")
        linked.symlink_to("16", target_is_directory=True)
        other = self.add_tree("breeze", "emblems", "22")
        other_dup = self.duplicate(other, "22@2x")

        helper.normalize(self.icons)

        self.assertTrue(linked.is_symlink())
        self.assertEqual(os.readlink(linked), "16")
        self.assertTrue(other_dup.is_symlink())
        self.assertEqual(os.readlink(other_dup), "22")


if __name__ == "__main__":
    unittest.main()
