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

### Step 1 — Per-position research (tiered; obey SKILL.md token-conservation rules)

- **Tier 1** — top 5 by weight OR any position ≥5%: full 7-phase deep dive
- **Tier 2** — positions 6–10: `get_ticker_info` + `get_analyst_data(recommendations+price_targets)` + 6mo weekly chart
- **Tier 3** — tail: single `get_tickers_info` batch call; no per-ticker fetches

Parallelize: pull `get_tickers_info` and `download([all_tickers], 1y, 1wk)` in batch calls, not per-position loops.

### Step 2 — Portfolio-level metrics

Run `skills/equity-research/scripts/portfolio_metrics.py`:
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

### Step 4 — Recommendations

Structured action list:
- **REDUCE / REMOVE** — per position, reason + quantified risk if kept
- **KEEP** — per position, restated thesis
- **ADD** — tickers/ETFs with sizing, role, thesis
- **CONDITIONAL TRIGGERS** — every action gated on price / technical / fundamental / macro
- **TIMELINE** — immediate / 2–4 weeks / pending catalyst
- **HEDGES** — if concentration warrants

Every aggressive suggestion carries a risk callout. See `skills/equity-research/references/risk-frameworks.md`.

## Deliverable

Default: `.docx` in `/outputs/` using `skills/equity-research/references/report-templates/portfolio-review.md`. Chat summary of top 3 actions with triggers.

If user asks for an artifact ("let me check this weekly"), build an HTML artifact.

## Mandatory disclaimer in every output.
