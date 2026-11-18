#!/usr/bin/env python3
"""Tests for ci/check-upstream-lock.py using temporary spec fixtures."""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent.parent / "check-upstream-lock.py"
spec = importlib.util.spec_from_file_location("check_upstream_lock", MODULE_PATH)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def write_lock(tmpdir, records):
    lock = Path(tmpdir) / "lock.json"
    lock.write_text(json.dumps({
        "captured_at": "2026-01-01T00:00:00+00:00",
        "selection": "test",
        "packages": records,
        "errors": [],
    }))
    return str(lock)


SPEC_OK = """\
# Generated comment.
%define debug_package %{nil}
#Name:    plasma-thing
Name:           sonic-thing
Summary:        thing
Version:        6.8.2
Release:        1%{?dist}
Source0:        https://example.invalid/%{version}.tar.gz

%description
desc

%package devel
Version:        99.99.99
Summary:        devel subpackage

%files
"""

SPEC_SUBPACKAGE_FIRST = """\
Name:           sonic-thing
Version:        6.8.2
Release:        1%{?dist}

%package qt6
Version:        0.0.1
"""


class CheckUpstreamLockTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write_spec(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def record(self, spec_rel="sonic-thing/sonic-thing.spec", package="sonic-thing",
               tag="6.8.2"):
        return {
            "spec": spec_rel, "package": package, "current_version": "0",
            "source_repository": "https://example.invalid",
            "resolved_refs_url": "", "tag": tag, "commit": "0" * 40,
            "previous_tag_exists": True,
        }

    def run_check(self, records):
        lock = write_lock(self.root, records)
        out = []
        rc = checker.check(lock, self.root, report=out.append)
        return rc, "\n".join(out)

    def test_ok_top_level_ignores_subpackage_and_comments(self):
        self.write_spec("sonic-thing/sonic-thing.spec", SPEC_OK)
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 0, out)
        self.assertIn("1 ok, 0 failed", out)

    def test_subpackage_version_not_used(self):
        self.write_spec("sonic-thing/sonic-thing.spec", SPEC_SUBPACKAGE_FIRST)
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 0, out)

    def test_missing_spec_fails(self):
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 1)
        self.assertIn("spec missing", out)

    def test_version_mismatch_fails(self):
        self.write_spec("sonic-thing/sonic-thing.spec",
                        SPEC_OK.replace("6.8.2", "6.7.4", 1))
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 1)
        self.assertIn("!= locked tag '6.8.2'", out)

    def test_name_mismatch_fails(self):
        self.write_spec("sonic-thing/sonic-thing.spec",
                        SPEC_OK.replace("sonic-thing", "other-name", 1))
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 1)
        self.assertIn("top-level Name", out)

    def test_resolvable_macro_version_ok(self):
        spec_text = (
            "%global sonicde_frameworks_version 6.31.0\n"
            "Name:           sonic-thing\n"
            "Version:        %{sonicde_frameworks_version}\n"
            "Release:        1%{?dist}\n\n%description\nx\n"
        )
        self.write_spec("sonic-thing/sonic-thing.spec", spec_text)
        rc, out = self.run_check([self.record(tag="6.31.0")])
        self.assertEqual(rc, 0, out)

    def test_lock_errors_entry_fails(self):
        self.write_spec("sonic-thing/sonic-thing.spec", SPEC_OK)
        lock = Path(self.root) / "lock.json"
        lock.write_text(json.dumps({
            "packages": [self.record()],
            "errors": [{"source": "x", "error": "boom"}],
        }))
        out = []
        rc = checker.check(str(lock), self.root, report=out.append)
        self.assertEqual(rc, 1)
        self.assertIn("fetch errors", "\n".join(out))

    def test_empty_packages_fails(self):
        lock = Path(self.root) / "lock.json"
        lock.write_text(json.dumps({"packages": [], "errors": []}))
        out = []
        rc = checker.check(str(lock), self.root, report=out.append)
        self.assertEqual(rc, 1)
        self.assertIn("no packages", "\n".join(out))

    def test_duplicate_package_fails(self):
        self.write_spec("sonic-thing/sonic-thing.spec", SPEC_OK)
        rec = self.record()
        dup = dict(rec)
        dup["spec"] = "other-dir/other-dir.spec"
        self.write_spec("other-dir/other-dir.spec", SPEC_OK)
        rc, out = self.run_check([rec, dup])
        self.assertEqual(rc, 1)
        self.assertIn("duplicate package entry 'sonic-thing'", out)

    def test_duplicate_spec_fails(self):
        self.write_spec("sonic-thing/sonic-thing.spec", SPEC_OK)
        dup = dict(self.record())
        dup["package"] = "other-package"
        rc, out = self.run_check([self.record(), dup])
        self.assertEqual(rc, 1)
        self.assertIn("duplicate spec entry", out)

    def test_macro_cycle_fails_clean(self):
        spec_text = (
            "%global a %{b}\n"
            "%global b %{a}\n"
            "Name:           sonic-thing\n"
            "Version:        %{a}\n"
            "Release:        1%{?dist}\n\n%description\nx\n"
        )
        self.write_spec("sonic-thing/sonic-thing.spec", spec_text)
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 1)
        self.assertIn("macro expansion too deep", out)

    def test_unresolved_macro_version_fails_clear(self):
        spec_text = (
            "Name:           sonic-thing\n"
            "Version:        %{undefined_macro}\n"
            "Release:        1%{?dist}\n\n%description\nx\n"
        )
        self.write_spec("sonic-thing/sonic-thing.spec", spec_text)
        rc, out = self.run_check([self.record()])
        self.assertEqual(rc, 1)
        self.assertIn("unresolved macro %{undefined_macro}", out)


if __name__ == "__main__":
    unittest.main()
