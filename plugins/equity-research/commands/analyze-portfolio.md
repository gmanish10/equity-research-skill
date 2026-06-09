---
description: End-to-end portfolio review with multi-format intake and gated recommendations
argument-hint: [portfolio file, paste, or screenshot — optional; will ask if not provided]
---

# /analyze-portfolio

Full portfolio review through the aggressive-growth / higher-risk-tolerance lens.

## Workflow

### Step 0 — Intake (always first)

| Format | Action |
|---|---|
| .xlsx / .csv | `python skills/equity-research/scripts/parse_portfolio.py <path>` |
| Image | Read with vision, extract rows |
| .pdf (broker) | Invoke `pdf` skill, then normalize |
| Typed / pasted | Parse inline |
| Nothing | Ask user to share |

Normalize to `{ ticker, shares, avg_cost?, cost_basis_date?, account?, notes? }`.

**Always confirm the parsed portfolio as a table** before analysis. Ask: "Does this look right?"

### Step 1 — Per-position deep dive via subagents (see SKILL.md for full rules)

**Every position gets the full 7-phase deep dive. No shallow tier, no top-holdings shortcut.** Each holding is researched to the same depth as a standalone `/research-stock` call. Subagents make this affordable.

1. **Base pass (main thread, 2 batch calls):** `get_tickers_info([all])` + `download([all, SPY, sectors], 1y, 1wk)` → `scripts/portfolio_metrics.py`. Consume only the summary — do NOT inline raw OHLCV. This is the cross-position view (correlation, weighted beta, weights) that individual subagents can't see; compute it first.
2. **Per-position pass — one Task subagent per holding:** dispatch in parallel batches. Each subagent runs the **full 7-phase framework** on its ticker, obeys the token rules internally, and returns **only its 3-horizon verdict block**. Pass into each: ticker, shares/avg_cost, its **% weight**, the **lens**, any portfolio-level flag it trips, and a compact **"rest of the book"** line (other holdings + weights + sectors, plus this name's top correlation pairs) so its verdict is portfolio-aware, not blind to siblings. The main thread keeps only the verdicts + base-pass metrics — never the intermediate MCP payloads. These verdicts are **provisional** — reconcile them in Step 3.5.

**Flags are now for prioritization, not gating** — every position is deep-dived regardless. They decide which names lead the summary and get the hardest scrutiny: broken thesis (price down >20% from avg cost, or 6m return >15% below sector), rich valuation (fwd P/E > 1.5× 5y median), weakening momentum (< 50-DMA + RSI < 45 + 3m negative), net analyst downgrades in last 90d, insider selling > $10M, fresh catalyst in last 30d, any position >10% of book, or explicit user callout.

Note: the cost-basis flags only fire when intake carries `avg_cost`. Without it, lean on the sector-relative and momentum flags, and say which flags couldn't be evaluated.

**Scale guardrail:** for books **>20 positions**, confirm before firing (N full deep dives is real time/token cost) and run subagents in batches. Never serialize per-ticker loops. Output defaults to the full 3-horizon verdict per position; offer the compact 5-line rendering (SKILL.md → "Compact verdict") for very large books if the full block ×N would be unreadable.

### Step 2 — Portfolio-level metrics

Run `skills/equity-research/scripts/portfolio_metrics.py` against the base-pass `download()` output. Consume only the summary — never hand raw OHLCV to the model. Produces:
- Weights, sector/geo/mcap breakdown
- Weighted beta
- Correlation matrix (from 1y weekly)
- Simulated drawdowns at -15% / -25% / -40%
- Factor exposure vs. aggressive-growth benchmark

### Step 3 — Critical review

See `skills/equity-research/references/portfolio-construction.md`. Identify:
- Broken theses
- Dead weight
- Concentration risks AND concentration opportunities
- Gaps costing upside

### Step 3.5 — Reconciliation (mandatory)

The N per-position verdicts are provisional and were formed in isolation. Reconcile them into one coherent book before recommending anything (see SKILL.md → Step 3.5):
- **Summed sizing must close** — all "Add" targets + holds ≤ 100% / available cash, and no name/sector breaches the lens cap once adds land. Targets yield if they don't.
- **Correlation clusters** — two correlated "Add"s are one bet sized twice; keep the higher-conviction expression, trim/hold the other.
- **Redundancy** — collapse duplicate exposures (same theme/driver, or an ETF that already holds a single-name position).
- **Factor/beta coherence** — check the reconciled set against base-pass weighted beta and factor tilts; rein in drift past the lens tolerance.

Where a reconciled action differs from a standalone verdict, say so and why.

### Step 4 — Recommendations

Recommendations follow from the **reconciled** action set (Step 3.5), not the raw verdicts. Every line must clear the **Recommendation quality bar** in SKILL.md (falsifiable, quantified downside, sized, time-boxed, opportunity-cost aware, conviction-tagged). **Gate the action set in plan mode** — present it for approval before committing it to the `.docx`.

Structured action list:
- **REDUCE / REMOVE** — per position, reason + quantified risk if kept
- **KEEP** — per position, restated thesis
- **ADD** — tickers/ETFs with sizing, role, thesis. To fill a gap the book can't cover from existing holdings, **generate new candidates via a live screen** (SKILL.md → Section 5, "Idea generation") — `screen_stocks` + sector/industry data → shortlist → subagent mini deep-dive. Never pull new names from memory. Prefer ETF equivalents over mutual funds for new money.
- **CONDITIONAL TRIGGERS** — every action gated on price / technical / fundamental / macro
- **TIMELINE** — immediate / 2–4 weeks / pending catalyst
- **HEDGES** — if concentration warrants

Every aggressive suggestion carries a risk callout. See `skills/equity-research/references/risk-frameworks.md`.

## Deliverable

Default: `.docx` in `/outputs/` using `skills/equity-research/references/report-templates/portfolio-review.md`. Chat summary of top 3 actions with triggers.

If user asks for an artifact ("let me check this weekly"), build an HTML artifact.

## Mandatory disclaimer in every output.
