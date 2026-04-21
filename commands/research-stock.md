---
description: Deep 7-phase research workup on a single stock with multi-horizon ratings
argument-hint: TICKER [depth: quick|deep (default: deep)]
---

# /research-stock

Run the 7-phase framework on `$ARGUMENTS` and produce multi-horizon ratings.

## Workflow

1. **Parse** the ticker from `$ARGUMENTS`. If ambiguous, call `lookup($ARGUMENTS)` and confirm.

2. **Obey the token-conservation rules in `skills/equity-research/SKILL.md`.** Default to smaller fetches: 6mo/1d for price history, 1wk interval for 1y correlation downloads, 30-day filter on `upgrades_downgrades`, nearest-monthly only for options.

3. **Run Batch 1, 2, 3 in parallel** (see SKILL.md). Do not serialize.

4. **Execute the 7 phases** (reference files cited in SKILL.md table).

5. **Produce the deliverable:**
   - `deep` (default): build `.docx` via `skills/equity-research/scripts/report_builder.py` using `skills/equity-research/references/report-templates/equity-research-report.md`. Save to `/outputs/`.
   - `quick`: chat response — 7-phase summary + three horizon rating blocks, no docx.

6. **Every rating carries `WHAT KILLS THIS TRADE`.** Non-negotiable.

7. **Mandatory disclaimer** in any document output and at the end of chat responses with ratings.

## Quality bar

- Numbers, not adjectives.
- Compute ratios yourself from MCP data.
- When data is stale, say so.
- When you don't know, say you don't know.
