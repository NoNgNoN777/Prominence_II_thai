# Full warning triage

Ran mtt.all_translations and check_item on all 6,537 final items, plus item_name_regex without the report's 300-warning truncation. Snapshot before this overlay: errors0, warnings1648 = left-in-English1530 + original-consumer-format64 + item-name54.

All54 name-warning pairs were read. 38 are corrected in review-final-lang-fixes.json. 16 are false positives/context-dependent generic phrases intentionally kept Thai: elevator block (actual Elevator already English), any material, Fluid Container, Missing Item, the end (end of track), Nuclear Fuel (generic mode), Magnet upgrade (upgrade descriptor), shopping list2 (UI concept), nuclear reactor6 in New Age (generic multi-block concept erroneously matched another mod's item), crafting pattern (generic AE2 recipe concept). Name scanning is global across mods so these matches do not prove named-item references.

Checked every English-only target for length/prose characteristics: no retained English string longer than45 chars. Inspected350 English-only labels outside obvious tag/fluid/item/block-name keys. Most are searchable machine GUI names, resource tags, units, named bogey styles, mod/person/painting names or formula fragments. Added5 non-name UI translations (Infinity, Charging x2, Mirror, example e.g.). Technical units, IDs and machine names intentionally remain English. English-only warning count alone is not translation incompleteness.

64 %d/original bare-percent warnings preserve original placeholders/consumer behavior; they require in-game checks and should not be 'fixed' by changing placeholders without confirming the caller.

The correction overlay includes43 items, contains no English-prose filler and should be merged after review-resolved-fixes.json. Re-run mtt validate after merge. Root handles final packaging and game QA separately.
