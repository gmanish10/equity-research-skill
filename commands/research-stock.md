---
description: Deep 7-phase research workup on a single stock with multi-horizon ratings
argument-hint: TICKER [depth: quick|deep (default: deep)]
---

# /research-stock

Run the full 7-phase framework on `$ARGUMENTS` and produce an equity research report with short/mid/long-term ratings.

## Workflow

1. **Parse** the ticker from `$ARGUMENTS`. If invalid or ambiguous, call `lookup($ARGUMENTS)` and confirm with the user.

2. **Run Batch 1, 2, 3 in parallel** (see skills/equity-research/SKILL.md for the exact calls). Do not serialize these.

3. **Execute the 7 phases** in order, using the reference files for each:
   - Phase 1 — Business model & supply chain → `skills/equity-research/references/supply-chain-research.md`
   - Phase 2 — Sector context → `skills/equity-research/references/sector-analysis.md`
   - Phase 3 — Fundamentals → `skills/equity-research/references/fundamentals.md`
   - Phase 4 — Technicals → `skills/equity-research/references/technicals.md` + `skills/equity-research/scripts/technicals.py`
   - Phase 5 — Options → `skills/equity-research/references/options.md` + `skills/equity-research/scripts/options_analytics.py`
   - Phase 6 — News, ownership, sentiment → `skills/equity-research/references/social-sentiment.md`
   - Phase 7 — Verdict with mandatory short/mid/long rating blocks

4. **Produce the deliverable:**
   - If depth is `deep` (default): build a .docx report using `skills/equity-research/references/report-templates/equity-research-report.md` and `skills/equity-research/scripts/report_builder.py`. Save to `/outputs/`.
   - If depth is `quick`: respond in chat — just the 7-phase summary and the three horizon rating blocks.

5. **Every rating carries a `WHAT KILLS THIS TRADE` line.** Non-negotiable.

6. **Include the mandatory disclaimer** in any document output and at the end of chat responses that include ratings.

## Quality bar

- Numbers, not adjectives. "Revenue grew 23% to $45.2B," not "revenue grew nicely."
- Compute ratios yourself from the MCP data — don't rely on pre-computed ones.
- When data is stale (e.g., Q4 not yet reported), say so.
- If you don't know, say you don't know.
