# MinionGuide

**An interactive checklist guide for a Path of Exile 2 minion army build — Witch → Infernalist.**

Tick off every skill gem, support gem, ascendancy point, spectre and passive-tree phase as you get them. Your ticks sync between your phone and PC.

▶️ **Use it here: [https://countinbiskitsyo.github.io/MinionGuide/](https://countinbiskitsyo.github.io/MinionGuide/)**

---

## What it does

- **Gem loadout checklist** — every skill gem and support, colour-coded like in-game gems: red Str, blue Int, green Dex, gold Lineage.
- **Ascendancy order** — all four Infernalist nodes in the order the path allows.
- **Spectres by act** — the best spectre to bind in each act, with where to find it.
- **Passive tree in 25 phases** — all 123 points, allocated top to bottom while levelling.
- **Progress bars** for every section, plus a "Hide collected" button that leaves only what you still need.
- **Gear targets for every slot** — every useful stat, prefix or suffix, best roll and priority, plus jewels and sceptre sockets.
- **Copy PoB code** — one tap copies the Path of Building code (final tree, 4 levelling checkpoints, full gem loadout).
- **Reference panels** for rotation, troubleshooting and stat priority.

## How syncing works

Ticks are saved on the device instantly. To sync between devices, tap **Sync** on the page and paste a GitHub token that has only the `gist` permission. The page stores your ticks in a secret Gist on your own GitHub account, and every device using that token sees the same ticks.

- The token is stored only in your browser — it never goes into this repository.
- No signal? Ticks stay on the device and sync next time.
- To stop syncing on a device: **Sync → Remove token from this device**.

## Updating

Each update is a small zip holding only the files that changed, laid out like this repository. Unzip it, drag its contents into **Add file → Upload files**, then **Commit changes**. About a minute later every device shows the new version, and your ticks carry over.

## Printable versions

The page is the guide. Printable PDFs (a 2-page cheatsheet and a 2-page gear sheet, made for double-sided lamination) are produced on request from the files in `dev/source/print/`.

## Repository layout

- `index.html` — the guide and checklist (this is the website)
- `README.md` — this page
- `dev/` — build files, the Path of Building code and project notes

## About the numbers

Every recommendation is measured in Path of Building (PoE2) 0.23.1 for patch 0.5.5, on a gearless level-100 character. A full rebuild is planned for Path of Exile 2 1.0 (December 11, 2026).

---

*Fan-made guide. Not affiliated with or endorsed by Grinding Gear Games.*
