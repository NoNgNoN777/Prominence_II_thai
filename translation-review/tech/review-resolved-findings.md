# Independent translation review

Reviewed all 2,717 resolved entries with source metadata and structural scanning; native mod-th_th accounts for 2,009 Create entries. Read approximately 900 longer Create prose/Ponder/tooltip/advancement pairs, plus representative shorter UI labels and non-native memory entries. This is a source-level review, not in-game verification.

Findings:
- Native Create Thai translates many searchable machine/item names, conflicting with project style. Restored exact official name pairs only when the corresponding English name occurs in that exact source sentence. Added spacing between Thai and English.
- Corrected semantic errors: at least 10 versus more than 10; fully retracted Hose Pulley incorrectly described as fully extended; transient low redstone pulses; Gantry rotation confused with redstone; longest fitting curve confused with narrowest curve; Sticker state toggle confused with removing signal; output threshold/steam-engine capacity phrasing; bogeys confused with entire carriages; missing empty-station condition and opposite-facing signal condition.
- Corrected typo/awkward fragments and malformed Clipboard underscore markup in reviewed entries.
- agent-create.json (1,687) and agent-ae-space.json (879): scanned every entry for placeholders/newlines and sampled approximately 40 longer prose entries. No structural errors found; one motor name correction added.
- review-resolved-fixes.json is a correction overlay only. Existing files/source/batches remain untouched. Check this overlay through mtt before build; root merges it last.
- Existing Thai emphasis may regroup words compared with English. Even pairing and render checks are appropriate; exact underscore-count identity is not required for meaning. No in-game layout claim.
