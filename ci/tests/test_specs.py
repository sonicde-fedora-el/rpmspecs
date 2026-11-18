#!/usr/bin/env python3
"""Tests for ci/specs.py shared spec enumeration."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parent.parent / "specs.py"
_spec = importlib.util.spec_from_file_location("specs", MODULE_PATH)
specs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(specs)


def make_repo(root):
    for pkg in ("a-pkg", "b-pkg", "old-pkg"):
        d = Path(root) / pkg
        d.mkdir()
        (d / f"{pkg}.spec").write_text(f"Name: {pkg}\n")
    ci = Path(root) / "ci"
    ci.mkdir()
    (ci / "retired-kde-specs.json").write_text(
        json.dumps(["old-pkg/old-pkg.spec"]))
    return ci / "retired-kde-specs.json"


class SpecsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        self.retired_file = make_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def _retired_patch(self):
        return mock.patch.object(
            specs, "RETIRED_FILE", str(self.retired_file))

    def test_active_excludes_retired_sorted(self):
        with self._retired_patch():
            self.assertEqual(
                specs.active(self.root),
                ["a-pkg/a-pkg.spec", "b-pkg/b-pkg.spec"])

    def test_retired_missing_path_fails(self):
        entries = json.loads(self.retired_file.read_text())
        entries.append("ghost/ghost.spec")
        self.retired_file.write_text(json.dumps(entries))
        with self._retired_patch():
            with self.assertRaises(FileNotFoundError):
                specs.retired(self.root)

    def test_stem_parent_mismatch_fails(self):
        (Path(self.root) / "a-pkg" / "wrong-name.spec").write_text("Name: x\n")
        with self._retired_patch():
            with self.assertRaises(ValueError):
                specs.active(self.root)

    def test_retired_not_a_list_fails(self):
        self.retired_file.write_text(json.dumps({"a": 1}))
        with self._retired_patch():
            with self.assertRaises(ValueError):
                specs.retired(self.root)


class SpecsRealRepoTest(unittest.TestCase):
    """Sanity checks against the real repository layout."""

    def test_real_repo_retired_entries_exist_and_are_excluded(self):
        repo = Path(__file__).resolve().parent.parent.parent
        ret = specs.retired(str(repo))
        self.assertTrue(ret)
        act = specs.active(str(repo))
        for r in ret:
            self.assertNotIn(r, act)
        self.assertIn("plasma-discover/plasma-discover.spec", act)


if __name__ == "__main__":
    unittest.main()
