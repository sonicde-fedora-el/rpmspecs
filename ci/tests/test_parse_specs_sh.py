#!/usr/bin/env python3
"""Tests for ci/parse-specs.sh propagating ci/specs.py failures."""

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SCRIPT = REPO / "ci" / "parse-specs.sh"
HELPER = REPO / "ci" / "specs.py"


def make_repo(root):
    ci = Path(root) / "ci"
    ci.mkdir()
    shutil.copy(SCRIPT, ci / "parse-specs.sh")
    shutil.copy(HELPER, ci / "specs.py")
    (Path(root) / "a-pkg").mkdir()
    (Path(root) / "a-pkg" / "a-pkg.spec").write_text("Name: a-pkg\n")
    (Path(root) / "build-order.txt").write_text("a-pkg\n")
    return ci / "retired-kde-specs.json"


class ParseSpecsShTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.retired_file = make_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self):
        return subprocess.run(
            ["bash", str(self.root / "ci" / "parse-specs.sh")],
            capture_output=True, text=True, cwd=self.root)

    def test_missing_retired_path_fails(self):
        self.retired_file.write_text(json.dumps(["ghost/ghost.spec"]))
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("kan ikke liste aktive specs", r.stderr)

    def test_stem_mismatch_fails(self):
        self.retired_file.write_text("[]")
        (self.root / "a-pkg" / "wrong.spec").write_text("Name: wrong\n")
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("kan ikke liste aktive specs", r.stderr)


if __name__ == "__main__":
    unittest.main()
