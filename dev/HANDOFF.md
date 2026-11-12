# PoE2 Minion Army Infernalist — Chat Handoff (v2.13, 2026-11-12)

## What this project is
A Path of Exile 2 **patch 0.5.5** Witch → Infernalist minion-army build for a player who
prioritises **army size + personal survivability** over raw DPS. Deliverables: a 2-page
double-sided laminated cheatsheet (Letter, 0.25" margins) and an importable PoB code.

## Current deliverables (v2.13) — SEE THE v2.13 SECTION AT THE END: the repository layout replaced the zip packages
The gear .xlsx is no longer packaged (user has no Excel) — the gear PDF is the only gear file. Source: `source/gear_targets_source_v1_12.html`.
v2.3 changes: "While levelling" gear note (guide ③ and gear PDF v1.2); ⑤ header says "finished Lv 100 tree". PoB code unchanged (v2.2). Front column split 53/44, back 40/57.

| File | What it is |
|---|---|
| `PoE2_MinionArmy_COMPLETE_GUIDE_v2_12.pdf` | Cheatsheet. Front: ① Ascendancy ② Gems ③ Gear ④ Rotation. Back: ⑤ Stat priority ⑥ Levelling ⑦ Tree (25 phases) |
| `PoB_code_v2_4_FULL.txt` | Final tree + 4 levelling checkpoint specs, full gem loadout, Notes tab |
| `PoE2_MinionArmy_GEAR_TARGETS_v1_12.pdf` | Slot × stat gear targets. v1.1: Str rows rated YOUR EHP (Str = Life); Int/Dex notes match the support budget |
| `source/guide_source_v2_12_front.html`, `..._back.html`, `fit_v2_12.py`, `gear_targets_source_v1_12.html` | Editable pages; the fit script scales each page independently to fill exactly 1 Letter page and merges |

Versioning rule (user request): version + date in banner, back-page banner, footer **and filename**.

## The build — verified in PoB 0.23.1 (gearless, level 100)
- Life 1,646 · ES 1,576 · Spirit 165 · EHP 1,352 · Str 142 / Dex 7 / Int 72
- Reserved 145 of 165 → **20 spare** (Discipline cost unknown; Reaver/Raging Spirits need 30)
- 123 passive points, 8 ascendancy points, 3 jewel sockets

### Ascendancy (path is forced — 1 point per node)
Root → Minion Life → **Loyal Hellhound** (2) · Root → +3% Life → **Altered Flesh** (4) → +3% Life →
**Beidat's Will** (6) · Altered Flesh → +3% Life → **Beidat's Hand** (8).
Altered Flesh gates both Beidat nodes. v2.0's card wrongly showed Will before Altered Flesh.

### Gems (endgame)
| Skill | Spirit | Supports |
|---|---|---|
| Spectre → **Zealous Excavator**, skill 1 Orb Explosion | 49 | Concentrated Area, Feeding Frenzy I, Bleed III, **Muster**, Heft — 24,794 DPS |
| Skeletal Brute | 39 | Feeding Frenzy I, Bleed III, Brutality III, Heavy Swing, Muster |
| Skeletal Frost Mage | 32 | Rakiata's Flow (the 1 Lineage gem), Feeding Frenzy I, Cold Attunement, Elemental Focus, Rapid Casting II |
| Skeletal Sniper | 25 | Feeding Frenzy I, Brutality III, Bleed III, Heft, Muster |
| Skeletal Warrior | 0 | Feeding Frenzy I, Hulking Minions, **Brutality III, Heavy Swing, Bleed III** (last 3 = 2.26×) |
| Detonate Dead | 0 | **Brutality III, Bleed III, Heft** (1.80×) |
| Pain Offering / Vulnerability / Unearth | 0 | bare (their best supports need Int/Dex the budget lacks) |
| Despair, Discipline | — | in PoB but disabled |
| Hellhound | — | socket Loyalty in game (PoB drops supports on the ascendancy-granted skill) |

Support attribute budget (each support costs 5 of its attribute, copies count):
Str 14 supports (70/142) · Int 14 incl. Loyalty (70/72) · Dex 1 (5/7).
**Uul-Netol's Embrace is Lineage** — illegal alongside Rakiata's Flow (and measured 1.00× in PoB anyway).

### Spectre measurements (full v2.2 build, same 5 supports unless noted)
| Spectre | Area | Best skill | DPS | Spirit |
|---|---|---|---|---|
| Zealous Excavator | The Excavation (Act 4), Digsite map | 1 Orb Explosion (skill 2 = 5,372; 3 = 15,074) | 20,362 → **24,794** with Muster | 49 (base 60) |
| Nymph Wasp | Arastas (Act 4) | 3 Laser | 13,268 | 48 (base 59) |
| Vaal Guard (mortar) | Utzaal / Library of Kamasa (Act 3) | 2 Grenade | 9,676 | 41 (base 50) |
Excavator support search: all ~490 non-Lineage supports tried in each slot within the attribute
budget. Only improvement: Controlled Destruction → Muster (1.218×). Caveat: PoB can't tell how often
the monster actually uses Orb Explosion — check in game.

## Major findings this session
1. **20 of 27 attribute nodes had no attribute chosen** in the v2.0 PoB code → PoB counted them as 0.
   Strength gives Life, which feeds Beidat's Will (Spirit) and Hand (ES). All-Str vs blank:
   +216 Life, +207 ES, +8 Spirit, **+21% EHP**. Each Str attribute node ≈ +1.2% EHP, +1 Spirit.
2. **v2.0's tree table did not match the PoB code**: "Raw Destruction" and "Power of the Dead" don't
   exist in 0.5 data; Living Death was described wrongly; 4 notables listed weren't in the code and
   4 in the code weren't listed. v2.1+ table is generated from the code itself.
3. **New 25-phase allocation order** (same 123-node set). Ingenuity moved to point 36 so Int covers
   supports while levelling; 4 attribute nodes go Int at points 11–35, re-picked as Str after
   Pure Energy (~pt 97). The first 12 points are forced (only route out of the Witch start: spell/ele).
4. **Single-node swap search** (~3,800 swaps, all-Str baseline): no measurable improvement.
   Eldritch Will loses to the 2 ES nodes it replaces. Profane Commander is a trade: +8 Spirit for −8% EHP.
   Blind spots: minion survival, recoup, reservation efficiency, movement, command damage.
5. **Possible better tree not yet searched:** the full tree has shorter attribute-chain routes into
   the minion cluster. Worthless when attributes counted as 0; now worth Str. Needs a full re-optimisation.

## Gearless checkpoints (PoB code v2.2, auto level)
| Lv | Pts | Life | ES | Spirit | EHP |
|---|---|---|---|---|---|
| 22 | 25 | 435 | 0 | 100 | 320 |
| 43 | 50 | 730 | 0 | 100 | 536 |
| 60 | 75 | 1,023 | 157 | 140 | 621 |
| 77 | 100 | 1,293 | 1,078 | 151 | 871 |
| 100 | 123 | 1,646 | 1,576 | 165 | 1,352 |

## Headless PoB — how to reproduce
- `git clone --depth 1 --branch v0.23.1 https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2`
  — at this tag **every .lua file compiles under stock LuaJIT** (no dialect conversion needed;
  the v2.0 handoff's conversion note does not apply to this tag).
- `apt-get install luajit libluajit-5.1-dev`; build lua-utf8 from `github.com/starwing/luautf8` (tag 0.1.6):
  `gcc -O2 -shared -fPIC -I/usr/include/luajit-2.1 lutf8lib.c -o lua-utf8.so`
- Runner (from `src/`): set `package.cpath` to the .so, `package.path` to `../runtime/lua/?.lua`,
  `dofile("HeadlessWrapper.lua")`, `loadBuildFromXML(xml)`, read `build.calcsTab.mainOutput`.
- Add skill groups with `build.skillsTab:PasteSocketGroup("Label: X\nSkill 20/0 1\nSupport 1/0 1")`;
  save with `build:SaveDB("x")`.

### Traps (all hit this session — avoid)
1. **Spectre name lookup is random**: `PasteSocketGroup` picks the first monster with that display
   name via `pairs()`, so "Vaal Guard" resolves to different monsters per process (DPS and Spirit
   both change). Always set `skillMinion`/`skillMinionCalcs` to the exact id **and**
   `skillMinionSkill`/`...Calcs` explicitly, and add the id to `build.spectreList`.
2. **Attribute overrides need a rebuild**: after `spec:SwitchAttributeNode(id, 1=Str/2=Dex/3=Int)` call
   `spec:BuildAllDependsAndPaths()` or nothing changes.
3. **Auto-level lags a frame**: after `treeTab:SetActiveSpec(i)` run `OnFrame` 2–3 times before reading.
4. **The wrapper clears `arg`**: capture `local A1,A2=...` before `dofile`.
5. **Background jobs die when a tool call returns** unless started with `setsid nohup ... < /dev/null &`.
   Commands over 300 s are killed — run long searches in the background and poll.
6. Never `pkill -f <word>` where the word is in your own command line — it kills the shell.

## Open items
- Discipline's Spirit cost (missing from PoB data) — check in game.
- Full tree re-optimisation with attribute nodes valued as Str (see finding 5).
- How often the Excavator uses Orb Explosion in real fights.
- All numbers are gearless; rankings hold, absolute values shift with gear.
- QR code removed in v2.1 (old maxroll link couldn't be verified). Re-add if the user supplies a
  pobb.in link for the v2.2 code.
- A file `an.py` appeared in the previous working folder that this chat did not create; it was not run.

## v2.4 research (2026-10-15) — all measured in the full v2.2/v2.4 build
### Spectre survey: all 619 PoB spectres × every usable skill, same 5 supports as the Excavator
- Only monsters with a spawn location count. Top raw numbers (Firebreather, Krell, Riptide, Quadrilla bosses) have none.
- Skills named ...OnDeath are fake DPS (fire when the spectre dies).
- Best overall / best AoE: **Zealous Excavator** 24,794 (49 sp, move speed 11, tag very_slow_movement; median spectre speed 32).
- Best Interlude: **Nymph Wasp** (Ashen Forest; also Arastas Act 4), skill 3 laser, 16,231, 48 sp, speed 25. Mapping alternative.
- Best non-AoE: Sun Clan Scavenger spear throw 15,244 at 69 sp (Bone Pits Act 2, Qimah Interlude, Mesa/Savannah maps) — worse per Spirit.
- Vaal Guard grenade 11,691 at 41 sp in this build.
- AoE classification uses skill-ID conventions (GS/GA/GT/MMS/EDS + names like Explosion/Slam/Laser) because PoB doesn't set Area on monster GS/GA skills.
- Not each spectre's own best supports — the Wasp's laser may prefer a different set.

### Skeletons (effective Spirit after 22% reservation efficiency; DPS per Spirit)
Brute 6,934 / 39 = 178 · Sniper 4,440 / 25 = 178 · Frost Mage 4,940 / 32 = 154 (with Muster) · Reaver 3,362 / 25 = 134 ·
Arsonist 3,750 / 32 = 117 · Storm Mage 2,419 / 32 = 76 · Cleric 0 DPS (heals), 16 sp · Warrior 3,322 (free).
New-skeleton numbers use their best non-Lineage, non-Dex supports (would need the replaced minion's Int slots).
Base Spirit (gem lvl 20): Brute 48, Frost/Storm Mage 39, Arsonist 39, Reaver 30, Sniper 30, Warrior 20, Cleric 20.
The v2.0–2.3 card's "Reaver 30 sp / Arsonist 39 sp" were base costs.

### Supports
- Frost Mage: Rapid Casting II → Muster 1.265× (both Int). Brute: no swap >1%. Excavator: only bigger swaps need a 2nd Lineage or more Int.
- Hound (PoB wipes supports on ascendancy-granted groups — measured as a normal group with gem SkillGemAscendancySummonInfernalHound):
  bare 3,049; Loyalty adds no DPS; + Heavy Swing, Brutality II, Heft, Bleed III (Str) = 5,970 (1.96×). Best Int option Muster 1.42× (Int full).
- Kalguuran: Eternal March = active spell, spends Runic Ward to revive minions (4 s cd). Build has no Ward source.
  Vorana's Siege, Esh's Prowess = Lineage. No Kalguuran support was a usable upgrade.
- Str supports now 18 of 28 incl. Hound. Int 14 of 14. Dex 1 of 1.
- Sniper and Warrior support searches did not finish (Warrior's set was measured earlier: 2.26×).

### New harness traps
7. `skillMinionSkill` indexes PoB's filtered list of usable minion skills, not the monster's raw skillList; out-of-range resets to 1 silently.
8. `SpiritReserved` diff by disabling a group returned 0 in these runs — take Spirit from gem data (spiritReservationFlat at [20]) ÷ 1.22.
9. Pasting a gem with DISABLED disables the gem, not the group.

## v2.5 — Jewels (PoB Data/ModJewel.lua; measured via Config custom modifiers on the full v2.4 build)
Bases: strjewel = Ruby, dexjewel = Emerald, intjewel = Sapphire; *_radius_jewel = Time-Lost (tiny 1–3% rolls).
Mods with zero weight on normal jewels: flat resistances, minion revive speed, ES recharge rate, minion accuracy.
Per max roll (army = Excavator + Brute + Frost Mage + Sniper + Warrior = 44,430; DD 16,502; EHP 1,352):
Minion dmg 15% (Sapphire P) +3.09% army · Minion atk/cast 4% (Sapphire S) +2.32% · Minion crit dmg 25% (S) +1.86% ·
Minion crit chance 20% (S) +1.39% · Spell dmg 15% (Sapphire P) DD +7.57% · ES 20% (Sapphire P) +3.10% EHP (+57 ES).
Minion Life/phys DR (Ruby), minion res (Sapphire): 0 in PoB — it doesn't model minion survival. Minion AoE: 0.
Corpse-consumed damage: 0 (condition off in config). Cold penetration: 0 (player mod, doesn't reach minions).
Gear PDF v1.5: 2 pages (user laminates back to back). Dropped 29 UTILITY rows (Rarity, max Mana, Mana regen, +Dex, +Int, Presence area); kept Movement Speed and +all Attributes. Blocks split 5/5 (Sceptre–Boots | Gloves–Jewels), each page fitted independently (0.85× / 0.97×) by source/fit_gear_v1_12.py; both pages ~96% full. The .xlsx is not packaged.
Open: a full minion priority list was requested — needs a 3rd guide page or trimming (user not yet asked).

## v2.6 — Sceptre socketables (PoB Data/ModRunes.lua)
A sceptre takes both the "caster" and the "sceptre" entries (Item.lua GetSocketedAugmentTypes). Measured via custom mods, full build:
Rabbit Idol 15% Spirit: 165 → 190 gearless (+25) · Primate Idol "Allies in your Presence deal 40% increased Damage": army +8.23% ·
Rune of Vitality +80 Life: EHP +6.95%, Spirit +4 · Ancient Rune of the Horde 8% minion atk/cast: +4.51% · Owl Idol 10% ally cast speed: +3.88% ·
Bear Idol 12–18 ally attack phys: +2.41% · Snake Idol 10% ally attack speed: +1.79% · Wolf Idol: +1.49% · Cat Idol: +0.98% · Perfect Robust Rune +15 Str: EHP +2.72%, +2 Spirit.
0 in PoB (not modelled): Xipocado's Soul Core (Command dmg), Ox Idol (ally ele res), Fox Idol (Presence area), Stag Idol lightning, Bonded lines.
Idol drop sources unknown — PoB lists them but not where they drop.
Guide front split now 52/45 (0.93×). Gear sheet split 4/6 blocks (Sceptre–Helmet | Boots–Jewels).

## v2.7 — Accuracy audit (all on PoB code v2.4, gearless Lv 100; army = Excavator+Brute+Frost Mage+Sniper+Warrior 44,430, DD 16,502, total 60,932)
Stat priority (custom mods): +1 minion level total 1.102× (army 1.140×) · minions 40% dmg 1.060× · minions 8–12 attack phys 1.012× ·
+100 ES EHP 1.305× · +30% ele res 1.180× · +100 Str 1.172× +9 Spirit · +30% chaos 1.125× · +100 Life 1.087× +5 Spirit ·
40% ES 1.061× · +30 Str 1.051× +3 Spirit · +30 Dex / +30 Int / minion 40% Life: 0.
Group contributions: Pain Offering on = army +35.9% · Vulnerability on = army +7.0% (DD +4.7%) · DD = 37.1% of army · Discipline: +328 ES, EHP 1.178×, PoB reserves 0 (no cost data).
Gem attributes verified in PoB data: Int — Concentrated Area, Feeding Frenzy I, Muster, Cold Attunement, Elemental Focus, Hulking Minions, Loyalty, Sacrificial Offering, Rapid Casting II, Cold Penetration.
Str — Bleed III, Heft, Brutality II/III, Heavy Swing. Dex — Rakiata's Flow (Lineage), Culling Strike II, Poison II, Lightning Penetration. Doedre's Undoing = Int + LINEAGE.
Budget recount: Str 18, Int 14, Dex 1 — matches the card.
Not re-verifiable on the endgame build (kept, levelling context): Feeding Frenzy I 1.45×/1.41×/1.39× socket-order numbers, levelling spectre DPS table.
Kept on purpose: "+216 Life, +207 ES, +8 Spirit, +21% EHP" in ⑦ (all-Str vs blank attribute nodes — a different baseline).

## v2.8 — Utility-skill supports (2026-10-29). Container was reset before this session; rebuilt from the v2.7 zip
(sources are now edited directly; the old gen.py generator is gone). Front column split 57/40 (0.897×), back 0.813×.
Method: only supports PoB's calcLib.canGrantedEffectSupportActiveSkill allows; each measured alone.
- Pain Offering (metric: army + DD total): Sacrificial Offering 1.060×, Danse Macabre 1.060×, Minion Mastery 1.007× (all Int); Uhtred's Exodus 1.018× (Lineage). No Str support helps.
- Vulnerability: 57 compatible supports, none changes PoB's numbers. Listed by function: Prolonged Duration II (Str); Heightened Curse, Ritualistic Curse, Focused Curse (Int).
- Unearth (Bone Construct + spell DPS, base 1,643): Muster 1.330× (Int), Considered Casting 1.307× (Int), Feeding Frenzy I/II 1.236× (Int),
  Brutality III 1.207× (Str), Heft 1.178× (Str), Bleed III 1.157× (Str), Heavy Swing 1.147× (Str), Culling Strike II 1.053× (Dex). Lineage: Uhtred's 1.436×, Uul-Netol's 1.372×.
- Skeletal Cleric (metric: Cleric's own EHP 4,864; PoB can't value healing): Meat Shield II 1.672× (Str), Meat Shield I 1.541×, Elemental Army 1.360× (Int),
  Hulking Minions 1.195× (Int), Minion Mastery 1.091× (Int), Infernal Legion II/III 1.063× (Str). Meat Shield is fine here: the Cleric deals no damage.
- Str budget with every Str pick: 18 + Unearth 4 + Cleric 2 + Vuln 1 = 25 of 28 (125 of 142 Str).
- The PoB code (v2.4) does not yet include these utility supports.

## 1.0 PREP (researched 2026-10-29 — decision: apply everything below in the 1.0 rebuild, NOT to 0.5.5)
Timeline: 1.0 launches Dec 11 2026 (PST). Full patch notes ~1 week before (~Dec 4). PoB 1.0 data likely at/after launch.
Plan: (1) draft guide v3.0 from patch notes (mark "from notes" vs "carried from 0.5.5"); (2) verified pass once PoB has 1.0 data.
The user wants a levelling guide they can follow blindly — verified numbers only in the final version.

Revealed at ExileCon (Nov 6 2026) — sources: maxroll "Everything New in PoE2 1.0", Output Lag, SenseOS, Sportskeeda:
- Infernalist rework: Demon Magus (demon companion that casts spells you socket into it); Infernal Hounds come in threes,
  commandable to charge and explode; new Covenant skills (Covenant of Ghorr drains Life to spawn Bloatflies).
  UNKNOWN: whether Beidat's Will / Beidat's Hand / Altered Flesh survive — check first in patch notes.
- Passive tree rebuilt: hundreds of new stats; 18 highway jewel sockets → ~60 inside notable clusters;
  Critical Hit Chance removed from the regular tree. Our 123-point tree + 25-phase order must be rebuilt.
- Support gems redesigned: adapt to the skill they support (spell/attack); Cold/Fire/Lightning Penetration merged
  into Elemental Penetration; Brutality now adds damage as extra Physical (used in most of our setups); many buffed.
- Witch gets new skills. Acts 5–6 (24 areas, 18 bosses) → new spectre candidates; spawn areas will change.
  One unconfirmed report says Interludes stop being campaign chapters.
- Atlas tree cut to ~70 nodes. Jewel crafting changes (5-mod jewels reportedly removed).

METHOD FIX FOR 1.0 — multiple copies of a minion:
PoB gem `count` = number of copies; Spirit is charged per copy, DPS shown is per minion.
Verified on v2.4 code: Excavator count 1/2/3 → reserved 145 / +49 / +49 each, 24,794 DPS per copy.
DPS per Spirit (0.5.5): Excavator 506 · Brute 178 · Sniper 178 · Frost Mage 154 · Reaver 134 · Arsonist 117 · Storm Mage 76.
Copies share one gem → no extra support-attribute cost. Our v2.x guide ran one of each type — likely far from optimal
(community builds stack Vaal Guards / Reavers / laser spectres). In 1.0: optimise copies of the best minion first,
then add types only for buffs PoB can't count (Brute Intimidate +10%, Frost Mage Command shields, Cleric healing)
and for practical reasons (Excavator very slow — move speed 11 vs median 32).

## SCOPE CHANGE (2026-10-29): class and ascendancy are OPEN for 1.0
The user will play whichever class + ascendancy makes the most efficient "many minions" army in 1.0 — not necessarily
Witch or Infernalist. Step 1 of the 1.0 rebuild = compare candidates on measured numbers, then build the levelling guide for the winner.
Comparison criteria (in priority order): (1) army size — total Spirit and Spirit sources unique to the ascendancy;
(2) survivability of player and minions; (3) army damage with copies of the best minion; (4) levelling smoothness
(how early the engine comes online); (5) gear dependence / no uniques required.
Note: in PoE2 every class can use every skill gem — class decides tree start + ascendancy only.
Candidates seen in ExileCon coverage: Infernalist (Demon Magus, 3 Hounds, Covenants; Beidat's Will = Spirit engine if kept);
Lich (0.5: Necromantic Conduit boosts minion damage); Blood Mage (new Dominate curse raises slain enemies as minions);
Knight (Duelist — one gear-able Squire: strong single companion, not an army); Acolyte of Chayula (Keeper of the Flame clone).
Also re-check the other 0.5 ascendancies in the 1.0 patch notes for minion or Spirit nodes.

## Interactive checklist guide (2026-10-29)
Published artifact: https://claude.ai/artifact/6GUVnDPmArTxy19MSkx2m1 (capabilities db + user).
Same content as the v2.8 PDF, rendered from source/checklist_data_v2_9.json (extracted from the v2.8 HTML with BeautifulSoup) into source/checklist_template_v2_9.html.
96 checkboxes: 4 ascendancy nodes, 62 gems and supports (chip colour = attribute: Str/Int/Dex/Lineage; skill/spirit/aura gems),
5 levelling spectres, 25 tree phases. Gear / rotation / stat priority are collapsible reference panels.
Ticks save to localStorage (key poe2-minion-checklist-v1) and, when signed in, to db doc data/users/<id>/checklist
{checks, updatedAt}; newer updatedAt wins; writes debounced 0.9 s, one at a time.
To update: regenerate data.json from new guide sources, rebuild from tpl.html, and publish to the same URL (keeps users' ticks if keys are unchanged).
Keys: asc:<node>, gem<row>:<name>, gem<row>:skill:<name>, lev:<act>, tree:<phase>.

## VERSIONING RULE (user request, 2026-10-29)
Bump the package version on EVERY delivery, even notes-only or packaging-only changes. Re-stamp every file that carries
the version (guide banners + footers, checklist header + <title>, gear sheet companion line), rename files and the zip folder,
and add a "What changed" entry to README. Gear sheet keeps its own series (v1.x) but bumps in step. PoB code keeps its own
number and only bumps when the build itself changes.
One zip holds everything: guide PDF, checklist HTML, gear PDF, PoB code, README, handoff, source/.
v2.9 (2026-10-29): packaging release — checklist page added, 1.0 notes, re-stamped. The v2.8→v2.9 banner text was already
present in the sources before this session's edit ran (origin unknown); output verified correct.

## v2.10 (2026-10-29) — checklist moved to Google Sheets
User has Claude account issues and does NOT want the interactive checklist hosted on Claude. The Claude-hosted page
(artifact 6GUVnDPmArTxy19MSkx2m1) is deprecated — the user may delete it; never re-publish it. Do not package HTML checklists.
Checklist = PoE2_MinionArmy_CHECKLIST_v2_10.xlsx, opened in Google Sheets (syncs phone <-> PC via Google account).
Built by source/build_checklist_v2_10.py from source/checklist_data_v2_10.json (same data as the guide).
Tabs: Start (progress via COUNTIF + setup steps + colour key), Ascendancy, Gems (62 rows, attribute-coloured), Spectres, Tree (25), Gear, Notes.
Tick cells are plain FALSE booleans; the user converts them once with Insert -> Checkbox (Google doesn't import xlsx checkboxes).
TRAP: LibreOffice recalc (xlsx skill recalc.py) rewrites FALSE cells as =FALSE() formulas, which Sheets shows as locked
checkboxes — run recalc on a COPY to verify (0 errors; totals 4/62/5/25 = 96) and ship the un-recalculated file.
Fixed: fit_v2_x.py's second open('front.html') was never renamed — fit script now reads the versioned source on both lines.

## v2.11 (2026-10-29) — checklist on GitHub Pages + Gist sync (replaces Google Sheets)
Why: Sheets updates meant re-upload + convert + re-insert checkboxes, and lost ticks. GitHub: user uploads one index.html; ticks persist.
Deliverable: UPLOAD_TO_GITHUB/index.html (built from source/checklist_template_v2_12.html + checklist_data_v2_12.json, __DATA__ placeholder).
User's site: https://<username>.github.io/minion-guide/ (repo "minion-guide", public, Pages from main / root). Username not yet known.
Sync: classic token with ONLY "gist" scope, pasted via the page's "Sync" dialog, stored in localStorage (poe2-gh-token).
The page finds its gist by filename poe2-minion-checklist.json (GET /gists, up to 5 pages) or creates a secret one (POST /gists);
id cached in localStorage (poe2-gh-gist). Content {checks, updatedAt, app, version}. Newer updatedAt wins. Saves debounced 1.2 s (PATCH),
one request at a time; pulls on visibilitychange and when back online; 401 → clear "token rejected" message.
Tested in jsdom against a mock GitHub API (source/checklist_sync_test_v2_12.js): bad token, create-once, second device finds the same
gist, A→B ticks, B untick → A on refocus. NOT tested against real GitHub (no token here) — first real run may need a fix.
KEEP CHECKBOX KEYS STABLE across updates (asc:<node>, gem<row>:<name>, gem<row>:skill:<name>, lev:<act>, tree:<phase>) or ticks won't carry over.
Note for the 1.0 rebuild: gem row indices are part of the keys, so a reordered gem table resets those ticks (fine for a new character).
Google Sheets checklist (v2.10) and the Claude-hosted page are both retired. Never re-publish to Claude.

## v2.12 (2026-11-12) — live on GitHub + repo README
GitHub username: countinbiskitsyo. Repository: MinionGuide (public). Live site: https://countinbiskitsyo.github.io/MinionGuide/
(user's other project, for style reference: countinbiskitsyo/MirrorFilter). Pages deployed and confirmed green by the user.
UPLOAD_TO_GITHUB now holds index.html + README.md (MirrorFilter-style: title, tagline, "Use it here" link, features, sync, updating, disclaimer).
About box: user to tick "Use your GitHub Pages website" (gear next to About). Token setup not yet done as of this version.
Dates: version dates now follow the real date (v2.12 = 2026-11-12).

## v2.13 (2026-11-12) — RESTRUCTURE: the GitHub repository is now the single home of everything
Repo: https://github.com/countinbiskitsyo/MinionGuide (public). Live: https://countinbiskitsyo.github.io/MinionGuide/
START OF EVERY SESSION: `git clone https://github.com/countinbiskitsyo/MinionGuide` (github.com is reachable from bash),
read dev/HANDOFF.md, rebuild with `python3 dev/source/build_index.py`. The user no longer needs to upload zips to Claude.
Layout (STABLE names — never put version numbers in file names; uploads overwrite by name and old names would pile up):
  index.html                         the guide + checklist (built — don't hand-edit; edit the template/data and rebuild)
  README.md                          repo front page
  dev/HANDOFF.md                     this file
  dev/GITHUB_SETUP.md                user's setup/update steps (token, phone, updating)
  dev/PoB_code.txt                   PoB code (v2.4 build) — embedded into index.html by the build
  dev/source/checklist_template.html page template; version lives in <title> and the hero '.ver' line
  dev/source/checklist_data.json     guide content (from the v2.8 guide HTML; same keys → ticks persist)
  dev/source/gear_targets_fragment.html  gear targets (legend, levelling note, 10 slot blocks) shown in the "Targets" panel
  dev/source/build_index.py          template + data + gear fragment + PoB code → ../../index.html
  dev/source/sync_test.js            jsdom test vs a mock GitHub API (JSDOM=path node dev/source/sync_test.js)
  dev/source/print/                  guide_front/back.html, gear_targets.html, fit_guide.py, fit_gear.py → PDFs ON REQUEST ONLY
                                     (run from that folder; needs weasyprint + pypdf; outputs MinionGuide_print_*.pdf; stamp the
                                     version in the sources first). PDFs are NOT stored in the repo or rebuilt every version.
DELIVERY RULE: give the user ONE zip containing a folder that mirrors the repo root with ONLY the changed files.
User drags the folder's contents into Add file → Upload files → Commit. Bump the version (template + this file) every delivery.
Page v2.13: wide layout (max 1560 px; ≥1150 px = 2-column grid: Ascendancy+Spectres, Gems full, Tree full, then reference panels
half-width, Gear targets full); new panels "Path of Building code" (Copy button, clipboard + select fallback) and "Gear targets".
Checkbox keys unchanged from v2.12 (verified: identical 96 keys). Token/sync setup: not yet done by the user as of v2.13.
Retired: README.txt, versioned zips with PDFs, UPLOAD_TO_GITHUB folder, Google Sheets, Claude-hosted page.

## v2.14 (2026-11-12) — calmer colours, full width
User kept font option A (Cinzel + Crimson Pro) after seeing 4 samples (B Barlow, C Cinzel+Source Sans 3, D Alegreya SC+Sans).
User found the colours "too bold and overwhelming". Changes (CSS block at the end of checklist_template.html's <style>):
- Muted palettes (light + dark). Chips: 1px neutral border, neutral text, small coloured diamond = attribute; ticked = 18% tint + ✓.
- Nav pills, section titles, Spirit badges and the tick circles toned down.
- Width: .wrap max 2400 px. Grid: ≥1150 px 2 columns (dense), ≥1800 px 3 columns.
  Order: Ascendancy, Spectres, PoB code (top row) → Gems (full; groups in an auto-fill grid, min 520 px each) →
  Tree (full; 2 text columns ≥1500 px) → Gear, Rotation, Stat → Gear targets (full).
- The user does NOT use the page on a phone — optimise for a ~2560 px desktop.
Checkbox keys unchanged (96, identical). WeasyPrint cannot preview CSS grid faithfully — don't use it to judge the layout.

## v2.15 (2026-11-12) — page overhaul: numbered collapsible sections, gem cards, uniform grid
Template rewritten (dev/source/checklist_template.html); build reads dev/source/gems.json (structured gem loadout:
key, name, kind skill|spirit|aura, spirit, sub, sup [[name, attr, multiplier?, "or"?]], alt {key,name,kind,text}, note).
Gem checkbox keys unchanged — verified identical set of 96 keys. NEVER change keys.
Sections (display order = numbering): ① Gems (full) · ② Ascendancy · ③ Spectres · ④ Path of Building (thirds) ·
⑤ Passive tree (full, 2 text columns ≥1500 px) · ⑥ Gear targets (full; MERGED the old "Gear — what can roll where" table
into it: its Exclusive + Buy-order notes on top, then the 10 slot blocks in a grid) · ⑦ Rotation · ⑧ Stat priority (halves).
Layout: 6-column grid ≥1150 px (thirds = span 2 at ≥1800, span 3 below; PoB spans full at 1150–1800); boxes stretch to equal row height.
Every section collapsible (header button, chevron); state saved in localStorage 'mg-sections-v1' (default: ⑥⑦⑧ collapsed).
Nav: numbered pills + Expand all / Collapse all / Hide collected / Sync. Clicking a nav pill opens a collapsed section.
Each section has its own muted colour (--c1..--c8). Skill gems = bold Cinzel chips with a 2 px border in the gem colour;
supports = quiet chips with the multiplier inside; commentary on its own faint line under each gem card.
The duplicate "PoB code has 5 tree checkpoints" note was removed from Spectres (now in ④).
NOTE: the print PDFs (dev/source/print) still use the old cheatsheet numbering (① Ascendancy … ⑦ Tree) — fine for print,
but renumber if the user wants them to match the page.

## v2.16 (2026-11-12) — PoB moved to a top-bar panel; 7 sections
PoB section removed; top bar "PoB code" button toggles #pobPanel (instructions + Copy button + code), state in localStorage 'mg-pob-open'.
Sections now: ① Gems (full) · ② Ascendancy · ③ Spectres (halves) · ④ Passive tree (full) · ⑤ Gear targets (full) · ⑥ Rotation · ⑦ Stat priority (halves).
All note groups use grid auto-fit (min 380 px) so they stretch across the full section width. README.md rewritten to match.
User feedback so far: likes the look; font A (Cinzel + Crimson Pro) confirmed; wants uniform, full-width, calm colours; desktop only.
