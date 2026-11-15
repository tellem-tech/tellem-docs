"""Check Russian/English page pairs, nav translations, media references and media budgets."""

import re
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MEDIA = DOCS / "media"
GIF_BUDGET = 2.5 * 1024 * 1024
PNG_BUDGET = 300 * 1024

# The one anchor pattern: `{#id}` and `{ #id }` both count. test_pinned_urls imports it.
ANCHOR = re.compile(r"\{\s*#([\w-]+)\s*\}")
PLANS = "superpowers"
HEADING = re.compile(r"^#{1,6}\s", re.MULTILINE)
IMAGE = re.compile(r"!\[[^\]]*\]\(")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")
ADMONITION = re.compile(r"^\s*(?:!!!|\?\?\?\+?)\s", re.MULTILINE)
CYRILLIC = re.compile(r"[А-Яа-яЁё]")
TEXT_SUFFIXES = {".md", ".css", ".js", ".html", ".yml"}


def doc_files(base, pattern):
    """Files under `base` matching `pattern`, without the ignored local plans in `<base>/superpowers/`."""
    return sorted(p for p in base.rglob(pattern) if PLANS not in p.relative_to(base).parts[:1])


def ru_pages(docs=DOCS):
    return [p for p in doc_files(docs, "*.md") if not p.name.endswith(".en.md")]


def anchor_mismatches(docs=DOCS):
    mismatched = []
    for ru in ru_pages(docs):
        ids = set(ANCHOR.findall(ru.read_text(encoding="utf-8")))
        en_ids = set(ANCHOR.findall(en_pair(ru).read_text(encoding="utf-8")))
        if ids != en_ids:
            mismatched.append(f"{ru.relative_to(docs)}: {sorted(ids ^ en_ids)}")
    return mismatched


def en_pair(page):
    return page.with_name(page.stem + ".en.md")


def without_fences(text):
    return re.sub(r"^```.*?^```", "", text, flags=re.MULTILINE | re.DOTALL)


def internal_links(text):
    targets = LINK.findall(without_fences(text))
    return [t for t in targets if not re.match(r"[a-z][a-z0-9+.-]*:|#", t)]


def structure(page):
    text = page.read_text(encoding="utf-8")
    body = without_fences(text)
    return {
        "headings": len(HEADING.findall(body)),
        "images": len(IMAGE.findall(body)),
        "internal links": len(internal_links(text)),
        "admonitions": len(ADMONITION.findall(body)),
    }


def nav_labels(node):
    if isinstance(node, list):
        for item in node:
            yield from nav_labels(item)
    elif isinstance(node, dict):
        for label, value in node.items():
            yield label
            yield from nav_labels(value)


def mkdocs_config():
    # mkdocs.yml uses !!python/name tags in extensions; load only what the tests read.
    class Loader(yaml.SafeLoader):
        pass

    loader = Loader
    loader.add_multi_constructor("tag:yaml.org,2002:python/", lambda *_: None)
    loader.add_multi_constructor("!", lambda *_: None)
    return yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=loader)


class PagePairTest(unittest.TestCase):
    def test_every_page_has_its_pair(self):
        pages = set(doc_files(DOCS, "*.md"))
        missing = []
        for page in sorted(pages):
            name = page.name.removesuffix(".en.md") + ".md" if page.name.endswith(".en.md") else page.stem + ".en.md"
            counterpart = page.with_name(name)
            if counterpart not in pages:
                missing.append(str(counterpart.relative_to(ROOT)))
        self.assertEqual([], missing, "Missing translation counterparts")

    def test_pairs_share_anchor_ids(self):
        self.assertEqual([], anchor_mismatches())

    def test_pairs_share_structure(self):
        mismatched = []
        for ru in ru_pages():
            ru_s, en_s = structure(ru), structure(en_pair(ru))
            diff = {k: (ru_s[k], en_s[k]) for k in ru_s if ru_s[k] != en_s[k]}
            if diff:
                mismatched.append(f"{ru.relative_to(ROOT)}: {diff}")
        self.assertEqual([], mismatched)


class AnchorProbeTest(unittest.TestCase):
    def test_spaced_anchor_on_one_side_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "a.md").write_text("## Title { #x }\n", encoding="utf-8")
            (docs / "a.en.md").write_text("## Title\n", encoding="utf-8")
            self.assertEqual(["a.md: ['x']"], anchor_mismatches(docs))
            (docs / "a.en.md").write_text("## Title {#x}\n", encoding="utf-8")
            self.assertEqual([], anchor_mismatches(docs))

    def test_plans_are_not_scanned(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "superpowers").mkdir()
            (docs / "superpowers" / "plan.md").write_text("no pair\n", encoding="utf-8")
            self.assertEqual([], ru_pages(docs))


class NavTranslationTest(unittest.TestCase):
    def test_nav_labels_are_translated(self):
        config = mkdocs_config()
        labels = {label for label in nav_labels(config["nav"]) if CYRILLIC.search(label)}
        i18n = next(p["i18n"] for p in config["plugins"] if isinstance(p, dict) and "i18n" in p)
        en = next(lang for lang in i18n["languages"] if lang["locale"] == "en")
        translated = set(en["nav_translations"])
        self.assertEqual([], sorted(labels - translated), "Nav labels without a translation")
        self.assertEqual([], sorted(translated - labels), "Translations for labels not in nav")


class MediaTest(unittest.TestCase):
    @staticmethod
    def media_files():
        return sorted(p for p in MEDIA.rglob("*") if p.is_file())

    def test_media_is_referenced(self):
        sources = [ROOT / "mkdocs.yml"] + [
            p for base in (DOCS, ROOT / "overrides") for p in doc_files(base, "*")
            if p.is_file() and p.suffix in TEXT_SUFFIXES
        ]
        corpus = "\n".join(p.read_text(encoding="utf-8") for p in sources)
        orphans = [
            str(f.relative_to(ROOT)) for f in self.media_files()
            if f"media/{f.relative_to(MEDIA).as_posix()}" not in corpus
        ]
        self.assertEqual([], orphans, "Media files that nothing references")

    def test_media_within_budget(self):
        budgets = {".gif": GIF_BUDGET, ".png": PNG_BUDGET}
        over = [
            f"{f.relative_to(ROOT)}: {f.stat().st_size} bytes"
            for f in self.media_files()
            if f.suffix in budgets and f.stat().st_size > budgets[f.suffix]
        ]
        self.assertEqual([], over, "Media files over budget")


if __name__ == "__main__":
    unittest.main()
