"""Check that the versioned skill set works without global skill installations."""

import hashlib
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
ALIASES = ROOT / ".claude" / "skills"


class AgentEnvironmentTest(unittest.TestCase):
    def setUp(self):
        self.skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        self.assertTrue(self.skills, "The project skill set is empty")

    def test_skill_metadata_and_resources(self):
        for skill in self.skills:
            with self.subTest(skill=skill.name):
                self.assertFalse(skill.is_symlink(), "Canonical skills must be real directories")
                entrypoint = skill / "SKILL.md"
                parts = entrypoint.read_text(encoding="utf-8").split("---", 2)
                self.assertEqual(parts[0], "", "SKILL.md must start with YAML frontmatter")
                self.assertEqual(len(parts), 3, "Missing frontmatter closing delimiter")
                metadata = yaml.safe_load(parts[1])
                self.assertEqual(metadata["name"], skill.name)
                self.assertRegex(skill.name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertLessEqual(len(skill.name), 64)
                self.assertIsInstance(metadata["description"], str)
                self.assertTrue(metadata["description"].strip())
                self.assertLessEqual(len(metadata["description"]), 1024)
                self.assertTrue((skill / "LICENSE").is_file(), "Keep the vendored license")
                for source in skill.rglob("*.md"):
                    targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8"))
                    for target in targets:
                        url = urlsplit(target)
                        if url.scheme or url.netloc or not url.path:
                            continue
                        resource = (source.parent / unquote(url.path)).resolve()
                        self.assertTrue(resource.is_relative_to(ROOT), f"External resource: {source}: {target}")
                        self.assertTrue(resource.exists(), f"Missing resource: {source}: {target}")

    def test_claude_aliases_resolve_to_canonical_skills(self):
        self.assertEqual({path.name for path in ALIASES.iterdir()}, {path.name for path in self.skills})
        for skill in self.skills:
            with self.subTest(skill=skill.name):
                alias = ALIASES / skill.name
                self.assertTrue(alias.is_symlink(), "Claude aliases must not duplicate skill files")
                self.assertFalse(alias.readlink().is_absolute(), "Aliases must work after cloning")
                self.assertEqual(alias.resolve(strict=True), skill.resolve(strict=True))

    def test_shared_rules_route_to_local_skills(self):
        rules = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("@AGENTS.md", (ROOT / "CLAUDE.md").read_text(encoding="utf-8"))
        for skill in self.skills:
            with self.subTest(skill=skill.name):
                self.assertIn(f".agents/skills/{skill.name}/SKILL.md", rules)
                self.assertIn(skill.name, (SKILLS / "SOURCES.md").read_text(encoding="utf-8"))

    def test_shared_block_matches_its_hash(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8").replace("\r\n", "\n")
        match = re.search(
            r"^<!-- tellem-shared:begin source=\S+ sha256=([0-9a-f]{64}) -->\n(.*?)^<!-- tellem-shared:end -->$",
            text,
            re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(match, "AGENTS.md has no shared block")
        inner = "\n".join(match.group(2).strip("\n").split("\n"))  # same trim as the sync script
        self.assertEqual(hashlib.sha256(inner.encode()).hexdigest(), match.group(1), "Shared block was edited by hand")


if __name__ == "__main__":
    unittest.main()
