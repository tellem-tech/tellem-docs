"""Check that every URL pinned in tests/pinned-urls.txt still resolves to a page, an anchor or a redirect."""

import re
import tempfile
import unittest
from pathlib import Path

from test_pages import DOCS, ROOT, mkdocs_config

MANIFEST = ROOT / "tests" / "pinned-urls.txt"
EXPLICIT_ANCHOR = re.compile(r"\{\s*#([\w-]+)\s*\}")


def manifest_entries(path):
    lines = (line.strip() for line in path.read_text(encoding="utf-8").splitlines())
    return [line for line in lines if line and not line.startswith("#")]


def page_candidates(site_path):
    """Source files that publish a site path: `/en/` paths come from `.en.md` pages."""
    english = site_path == "/en/" or site_path.startswith("/en/")
    rel = site_path.removeprefix("/en").strip("/") if english else site_path.strip("/")
    suffix = ".en.md" if english else ".md"
    return [Path(rel) / f"index{suffix}"] + ([Path(f"{rel}{suffix}")] if rel else [])


def redirect_keys(site_path):
    rel = site_path.strip("/")
    return {f"{rel}.md", f"{rel}/index.md"} if rel else set()


def problem(entry, docs, redirects):
    """Why a manifest line no longer resolves, or None when it does."""
    site_path, _, anchor = entry.partition("#")
    if not site_path.startswith("/") or not site_path.endswith("/"):
        return "not normalized: expected /<path>/ with an optional #anchor"
    # An anchor is pinned on both language versions of a Russian page.
    sites = [site_path, "/en" + site_path] if anchor and not site_path.startswith("/en/") else [site_path]
    for site in sites:
        found = [c for c in page_candidates(site) if (docs / c).is_file()]
        if not found and site == site_path:
            break
        if not found:
            return f"no English page for {site_path}"
        if anchor and anchor not in EXPLICIT_ANCHOR.findall((docs / found[0]).read_text(encoding="utf-8")):
            return f"no explicit {{#{anchor}}} on {found[0].as_posix()}"
    else:
        return None
    if redirect_keys(site_path) & set(redirects):
        return "anchor on a redirected path" if anchor else None
    return "no page and no redirect"


class PinnedUrlsTest(unittest.TestCase):
    def test_every_pinned_url_resolves(self):
        redirects = next(p for p in mkdocs_config()["plugins"] if isinstance(p, dict) and "redirects" in p)
        redirect_maps = redirects["redirects"]["redirect_maps"]
        entries = manifest_entries(MANIFEST)
        self.assertEqual(len(entries), len(set(entries)), "duplicate manifest lines")
        failures = [f"{e}: {why}" for e in entries if (why := problem(e, DOCS, redirect_maps))]
        self.assertEqual([], failures)


class ProblemProbeTest(unittest.TestCase):
    """The check fails when a pinned page, anchor or redirect is gone."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.docs = Path(self.tmp.name)
        (self.docs / "a").mkdir()
        (self.docs / "a" / "b.md").write_text("## Title { #part }\n", encoding="utf-8")
        (self.docs / "a" / "b.en.md").write_text("## Title {#part}\n## Two {#two}\n", encoding="utf-8")
        (self.docs / "a" / "c.md").write_text("## Title {#part}\n", encoding="utf-8")
        (self.docs / "a" / "c.en.md").write_text("## Title\n", encoding="utf-8")
        (self.docs / "legal" / "doc").mkdir(parents=True)
        (self.docs / "legal" / "doc" / "index.en.md").write_text("text\n", encoding="utf-8")

    def test_existing_pages_and_anchors_pass(self):
        for entry in ("/a/b/", "/a/b/#part", "/en/a/b/", "/en/a/b/#part", "/en/legal/doc/"):
            self.assertIsNone(problem(entry, self.docs, {}), entry)

    def test_removed_page_fails(self):
        self.assertIsNotNone(problem("/a/gone/", self.docs, {}))
        self.assertIsNotNone(problem("/legal/doc/", self.docs, {}))

    def test_anchor_missing_from_the_english_page_fails(self):
        self.assertIsNotNone(problem("/a/c/#part", self.docs, {}))

    def test_removed_anchor_fails(self):
        self.assertIsNotNone(problem("/a/b/#gone", self.docs, {}))

    def test_redirect_resolves_until_it_is_removed(self):
        redirects = {"legal/en/doc/index.md": "x", "old.md": "y"}
        self.assertIsNone(problem("/legal/en/doc/", self.docs, redirects))
        self.assertIsNone(problem("/old/", self.docs, redirects))
        self.assertIsNotNone(problem("/legal/en/doc/", self.docs, {}))

    def test_anchor_on_a_redirected_path_fails(self):
        self.assertEqual("anchor on a redirected path", problem("/old/#x", self.docs, {"old.md": "y"}))
        self.assertEqual("no page and no redirect", problem("/old/#x", self.docs, {}))

    def test_unnormalized_line_fails(self):
        self.assertIsNotNone(problem("a/b/", self.docs, {}))
        self.assertIsNotNone(problem("/a/b", self.docs, {}))
        self.assertIsNotNone(problem("/a/b#part", self.docs, {}))


if __name__ == "__main__":
    unittest.main()
