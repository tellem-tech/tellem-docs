# [Tellem](https://tellem.tech) documentation

Public documentation for store owners and customers: [Russian](https://docs.tellem.tech/) · [English](https://docs.tellem.tech/en/).

See [AGENTS.md](AGENTS.md) for writing, translation, and public repository guidelines.

## Structure

- [mkdocs.yml](mkdocs.yml) — MkDocs and Material settings, languages, navigation, and redirects.
- [docs/](docs/) — Russian pages (`page.md`) and English translations (`page.en.md`); `docs/media/` contains shared images and GIFs.
- [docs/legal/](docs/legal/) — current legal documents and their translations. Legacy `/legal/en/` URLs redirect to the corresponding `/en/legal/` pages.
- [requirements.txt](requirements.txt) — site dependencies.

Russian pages keep their existing URLs; English pages are served under `/en/`. The language switcher opens the corresponding page. Update both translations together, using unsuffixed `.md` paths in internal links so the site keeps readers in their chosen language.

## Agent environment

[AGENTS.md](AGENTS.md) routes editing to [stop-slop](.agents/skills/stop-slop/SKILL.md) and completion checks to [verification-before-completion](.agents/skills/verification-before-completion/SKILL.md). [CLAUDE.md](CLAUDE.md) imports the same rules; `.claude/skills/` contains relative aliases to the canonical `.agents/skills/` directories. No global installation is required.

Keep the [upstream sources and license notices](.agents/skills/SOURCES.md) with the skills. For a new skill, add its Claude alias and AGENTS.md entry. The tests below check metadata, local references, licenses, and aliases.

## Local development

Use the Python version from [CI](.github/workflows/mkdocs-deploy.yml) in an activated virtual environment. Browser event tests also require Node.js with the built-in test runner.

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

Use [Content Workshop](https://github.com/tellem-tech/tellem-workshop) to capture the real interface and prepare screenshots, GIFs, and short videos. Its README covers setup and use; team access is required.

To rebuild the home-page wordmark, pass the workshop checkout and an ignored output directory:

```sh
node scripts/render-wordmark.mjs --workshop ../tellem-workshop --output site/wordmark-rebuild
```

Update both language pages with matching actions and captions. Identify shared Russian UI in English instructions. Name translated media `name.en.gif` or `name.en.png`: the localization plugin publishes it under `/en/media/` without the `.en` suffix. Check the built URLs and contents. Shared home-page CSS loads from `/css/home.css` in both languages, so its relative logo URLs resolve under `/media/`.

## Publication

The [deployment workflow](.github/workflows/mkdocs-deploy.yml) runs on pushes to `master` or manually through **Run workflow** in GitHub Actions. After a successful strict build, it deploys both languages to GitHub Pages.

Pushing to `master` also publishes legal documents. Make sure all changes are ready for public access before pushing.
