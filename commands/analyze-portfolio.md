---
description: End-to-end portfolio review with multi-format intake and gated recommendations
argument-hint: [portfolio file, paste, or screenshot — optional; will ask if not provided]
---

# /analyze-portfolio

Full portfolio review through the aggressive-growth / higher-risk-tolerance lens.

## Workflow

### Step 0 — Intake (always first)

Detect the input format:

| Format | Action |
|---|---|
| .xlsx / .csv attachment | Run `python skills/equity-research/scripts/parse_portfolio.py <path>` |
| Image / screenshot | Read with vision, extract rows |
| .pdf (broker statement) | Invoke the `pdf` skill to extract tables, then normalize |
| Typed / pasted text | Parse inline |
| Nothing provided | Ask the user to share in any of the formats above |

**Always confirm the parsed portfolio back as a table** before running any analysis. Ask: "Does this look right?"

Normalize to: `{ ticker, shares, avg_cost?, cost_basis_date?, account?, notes? }`

### Step 1 — Per-position research

- For positions ≥5% of book OR top 10 by weight: run the full 7-phase deep dive
- For the tail: run a fast version — `get_ticker_info` + `get_analyst_data(recommendations+price_targets)` + 6-month chart

Parallelize aggressively — pull all `get_tickers_info` and `download([all_tickers])` data in batch calls, not per-position loops.

### Step 2 — Portfolio-level metrics

Run `skills/equity-research/scripts/portfolio_metrics.py` with the parsed portfolio to produce:
- Weights, sector/geo/mcap breakdown
- Weighted beta
- Correlation matrix
- Simulated drawdowns at -15%, -25%, -40% market
- Factor exposure vs. aggressive-growth benchmark

### Step 3 — Critical review

See `skills/equity-research/references/portfolio-construction.md` for the review checklist. Identify:
- Broken theses
- Dead weight
- Concentration risks AND concentration opportunities (aggressive lens)
- Gaps that cost upside

### Step 4 — Recommendations

Structured action list:
- **REDUCE / REMOVE** — per position with reason + quantified risk if kept
- **KEEP** — per position with restated thesis
- **ADD** — specific tickers/ETFs with sizing, role, thesis
- **CONDITIONAL TRIGGERS** — every action gated on price, technical, fundamental, or macro condition
- **TIMELINE** — immediate / 2–4 weeks / pending catalyst
- **HEDGES** — if concentration warrants it

Every aggressive suggestion carries a risk callout. See `skills/equity-research/references/risk-frameworks.md`.

## Deliverable

Default: .docx report saved to `/outputs/` using `skills/equity-research/references/report-templates/portfolio-review.md`. Include a chat summary of the top 3 actions with clear triggers.

If the user asks for an artifact ("let me check this weekly"), build an HTML artifact they can re-open.

## Mandatory disclaimer in every output.
