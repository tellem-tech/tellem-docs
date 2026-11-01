---
name: verification-before-completion
description: Verify changed documentation, skills, and site behavior before reporting completion or readiness to commit.
---

# Verify before reporting completion

Choose checks that prove the claim, run them against the final changes, and inspect their complete output and exit codes. Report failures and limits alongside passing checks.

For this repository:

1. Run `python -m unittest discover -s tests -v` for skill metadata, aliases, page metadata, and browser event behavior.
2. Run `python -m mkdocs build --strict` for both languages and site links.
3. Review changed pages for equivalent meaning, interface labels, anchors, media, and navigation. A successful build cannot verify factual accuracy or image contents.
4. Inspect the diff and working-tree status. Preserve unrelated changes and confirm that secrets, personal data, local files, and build output stay out of the change.

Verify uncertain product claims against the interface or source. Inspect rendered output when presentation changes; use a focused check for a narrow change. Re-run affected checks after fixing a failure or changing tested content.

State the command and observed result. Distinguish static inspection, a built site, browser checks, and real product interaction; one does not prove the others. A subagent's report is a lead to inspect, not evidence by itself. Do not publish or push unless the user requests it.
