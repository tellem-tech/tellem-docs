# [Tellem](https://tellem.tech) documentation

Public documentation for store owners and customers: [Russian](https://docs.tellem.tech/) · [English](https://docs.tellem.tech/en/).

See [AGENTS.md](AGENTS.md) for writing, translation, and public repository guidelines. [CLAUDE.md](CLAUDE.md) imports the same instructions for Claude. Keep these repository instructions in English; maintain user documentation in both Russian and English.

## Structure

- [mkdocs.yml](mkdocs.yml) — MkDocs and Material settings, languages, navigation, and redirects.
- [docs/](docs/) — Russian pages (`page.md`) and English translations (`page.en.md`); `docs/media/` contains shared images and GIFs.
- [docs/legal/](docs/legal/) — current legal documents and their translations. Legacy `/legal/en/` URLs redirect to the corresponding `/en/legal/` pages.
- [requirements.txt](requirements.txt) — site dependencies and allowed versions.

Russian pages keep their existing URLs; English pages are served under `/en/`. The language switcher opens the corresponding page. Update both translations together, using unsuffixed `.md` paths in internal links so the site keeps readers in their chosen language.

## Agent environment

[Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/skills/), and [OpenCode](https://opencode.ai/docs/skills/) share [AGENTS.md](AGENTS.md) and the versioned skills in [.agents/skills/](.agents/skills/). No global skill installation or environment synchronization is required.

Start a new agent session after pulling changes to these instructions or skills.

- `stop-slop` supports concise editing without changing the documented meaning.
- `verification-before-completion` requires evidence before reporting that work is ready.

[CLAUDE.md](CLAUDE.md) imports the shared rules; `.claude/skills/` contains relative aliases to the canonical skill directories. Codex and OpenCode use `.agents/skills` directly. Agents must follow the skill routing in AGENTS.md even when automatic discovery is unavailable.

Keep the [upstream revisions and license notices](.agents/skills/SOURCES.md) with the skills. After adding or updating a skill, update its Claude alias and run the checks below. CI checks skill metadata, local references, licenses, and alias targets; it cannot prove that a model followed prose instructions.

## Local development

Use Python 3.12, matching CI, and an activated virtual environment. Browser event tests also require Node.js 18 or newer.

```sh
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open the local address printed in the terminal. Use `/en/` for the English version.

Validate both languages before submitting changes:

```sh
python -m unittest discover -s tests -v
python -m mkdocs build --strict
```

Check external links and the text's accuracy against the interface separately. Some shared screenshots show the Russian interface.

CI also checks that every page has a translation. Link preview cards are enabled in CI and disabled in local builds by default.

## Product screenshots and GIFs

Tellem team members can use [Content Workshop](https://github.com/tellem-tech/tellem-workshop) to create product screenshots, GIFs and short videos for documentation and Telegram. A coding agent captures the real interface and prepares the material; you can edit its text in a local browser. The workshop repository requires team access. Its README covers setup and use.

For `scripts/render-wordmark.mjs`, pass the current workshop checkout with `--workshop`. Use `--workshop ../tellem-content-workshop` while local directories keep their old names, then `--workshop ../tellem-workshop` after the directory rename.

Update both language pages together, with matching actions and captions. Keep screenshots truthful; identify shared Russian UI in the English instructions. An English GIF can use `.en.gif` with translated explanations and the same recording. Check the built image URLs and contents: the localization plugin publishes `home-screen-editor.en.gif` as `/en/media/crm/home-screen-editor.gif`, while the Russian file uses `/media/crm/home-screen-editor.gif`. Shared home-page CSS loads from `/css/home.css` in both languages, so its relative logo URLs resolve under `/media/`.

## Publication

The [deployment workflow](.github/workflows/mkdocs-deploy.yml) runs on pushes to `master` or manually through **Run workflow** in GitHub Actions. After a successful strict build, it deploys both languages to GitHub Pages.

Pushing to `master` also publishes legal documents. Make sure all changes are ready for public access before pushing.
