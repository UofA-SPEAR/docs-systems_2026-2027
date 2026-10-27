# Systems Documentation

## Wiki

Pages in `docs/wiki/` are published to this repo's Wiki tab automatically on every push to `main`.

### One-time setup (each person who pushes)

```bash
git remote add wiki https://github.com/UofA-SPEAR/docs-systems_2026-2027.wiki.git
git config core.hooksPath .githooks
```

### Editing the wiki

1. Add or edit `.md` files in `docs/wiki/`. Each file is one page; `Home.md` is the landing page.
2. Link new pages in `docs/wiki/_Sidebar.md`.
3. Commit and push to `main`. The Wiki tab updates on its own.

Only `docs/wiki/` is published. Do not edit pages on the GitHub website; the next push overwrites them.
