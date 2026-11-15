"""Check navigation-safe browser code and contextual documentation feedback."""

import subprocess
import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qs, urlsplit

from jinja2 import DictLoader, Environment
import yaml

from test_pages import doc_files


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.targets = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.targets.append(dict(attrs)["href"])


class SiteBehaviorTest(unittest.TestCase):
    def test_page_metadata_is_valid_yaml(self):
        for source in doc_files(ROOT / "docs", "*.md"):
            text = source.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            with self.subTest(source=source.relative_to(ROOT)):
                metadata = yaml.safe_load(text.split("---", 2)[1])
                self.assertIsInstance(metadata, dict)
                if "description" in metadata:
                    self.assertIsInstance(metadata["description"], str)

    def test_browser_event_lifecycle(self):
        subprocess.run(
            ["node", "--test", str(ROOT / "tests/test_site_javascript.mjs")],
            cwd=ROOT,
            check=True,
        )

    def test_feedback_preserves_language_and_page_context(self):
        env = Environment(autoescape=True, loader=DictLoader({
            "main.html": (ROOT / "overrides/main.html").read_text(encoding="utf-8"),
            "base.html": "{% block content %}Guide content{% endblock %}",
        }))
        for language, src_uri, canonical in [
            ("ru", "modules/crm/orders.md", "https://docs.tellem.tech/modules/crm/orders/"),
            ("en", "modules/crm/orders.en.md", "https://docs.tellem.tech/en/modules/crm/orders/"),
        ]:
            with self.subTest(language=language):
                page = SimpleNamespace(file=SimpleNamespace(src_uri=src_uri),
                                       title="Orders & delivery + returns", canonical_url=canonical)
                config = SimpleNamespace(theme=SimpleNamespace(language=language))
                html = env.get_template("main.html").render(page=page, config=config)
                link, = Links(html).targets
                target = urlsplit(link)
                query = parse_qs(target.query)
                self.assertEqual(target.netloc, "github.com")
                self.assertEqual(target.path, "/tellem-tech/tellem-docs/issues/new")
                self.assertIn(canonical, query["body"][0])
                self.assertIn(page.title, query["title"][0])
                self.assertIn("Report an error" if language == "en" else "Сообщить об ошибке", html)

        for src_uri in ["index.md", "index.en.md", "legal/offer/index.md", "legal/offer/index.en.md"]:
            with self.subTest(src_uri=src_uri):
                page.file.src_uri = src_uri
                html = env.get_template("main.html").render(page=page, config=config)
                self.assertEqual(Links(html).targets, [])


if __name__ == "__main__":
    unittest.main()
