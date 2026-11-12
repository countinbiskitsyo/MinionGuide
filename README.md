# MinionGuide

**An interactive guide and checklist for a Path of Exile 2 minion army build — Witch → Infernalist.**

Tick off every skill gem, support gem, ascendancy point, spectre and passive-tree phase as you get them. Your progress is remembered between visits.

▶️ **Use it here: [https://countinbiskitsyo.github.io/MinionGuide/](https://countinbiskitsyo.github.io/MinionGuide/)**

---

## What's in the guide

The page has seven numbered sections. Each one can be collapsed, and the page remembers which ones you left open.

1. **Gem loadout** — every skill gem with its five supports, as tick-off chips. Diamond colour shows the gem type (red Str, blue Int, gold Lineage); measured gains sit inside each chip.
2. **Ascendancy** — the four Infernalist nodes in the order the path allows.
3. **Spectres by act** — the best spectre to bind in each act and where to find it.
4. **Passive tree** — all 123 points in 25 phases, allocated top to bottom.
5. **Gear targets** — every useful stat per slot: prefix or suffix, best roll and priority, plus jewels and sceptre sockets.
6. **Rotation & troubleshooting** — what to press when mapping and bossing.
7. **Stat priority & checkpoints** — measured stat values and the expected Life / ES / Spirit at each tree checkpoint.

**Hover over any gem or support** to see what it does in game and why it's in that slot (with the measured gain). Ticking a support also ticks its skill gem.

The top bar also has:

- **PoB code** — opens the Path of Building code with a one-click Copy button (final tree, 4 levelling checkpoints, full gem loadout).
- **Expand all / Collapse all**, **Hide collected**, and **Sync**.

## Syncing (optional)

Ticks are saved in your browser automatically. **Sync** also backs them up to your own GitHub account, so they survive clearing your browser and work on other devices: tap **Sync** and paste a GitHub token that has only the `gist` permission. Your ticks are kept in a secret Gist on your account; the token stays in your browser and never goes into this repository.

## Updating

Each update is a small zip holding only the files that changed, laid out like this repository. Unzip it, drag the contents of the folder inside into **Add file → Upload files**, then **Commit changes**. About a minute later the site shows the new version, and your ticks carry over.

## Printable versions

Printable PDFs (a 2-page cheatsheet and a 2-page gear sheet, made for double-sided lamination) are produced on request from the files in `dev/source/print/`.

## About the numbers

Every recommendation is measured in Path of Building (PoE2) 0.23.1 for patch 0.5.5 (still current for 0.5.5f — its patches since then changed nothing for this build), on a gearless level-100 character. A full rebuild is planned for Path of Exile 2 1.0 (December 11, 2026).

## Repository layout

- `index.html` — the guide (this is the website)
- `README.md` — this page
- `dev/` — build files, the Path of Building code and project notes

---

*Fan-made guide. Not affiliated with or endorsed by Grinding Gear Games.*
