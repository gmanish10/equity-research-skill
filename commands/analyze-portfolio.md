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

### Step 1 — Progressive-depth research (see SKILL.md for full rules)

Three-pass escalation — no hard caps on position depth:

- **Pass A (whole book, 2 batch calls)**: `get_tickers_info([all])` + `download([all, SPY, sectors], 1y, 1wk)`. Pipe `download()` output to `scripts/portfolio_metrics.py`; consume only the summary — do NOT inline raw OHLCV.
- **Pass B (every position, parallelized)**: `get_analyst_data(recommendations + price_targets)` for all tickers. For positions ≥3% of book, also pull yearly financials, earnings, `eps_trend`, and `institutional + insider_purchases` holders.
- **Pass C (flagged + top 3, full 7-phase)**: auto-escalate positions that trip any of these flags — broken thesis (price down >20% from avg cost, or 6m return >15% below sector), rich valuation (fwd P/E > 1.5× 5y median), weakening momentum (< 50-DMA + RSI < 45 + 3m negative), net analyst downgrades in last 90d, insider selling > $10M, fresh catalyst in last 30d, any position >10% of book, or explicit user callout. The top 3 positions by weight always auto-escalate.

Parallelize aggressively within each pass. No per-ticker serial loops.

### Step 2 — Portfolio-level metrics

Run `skills/equity-research/scripts/portfolio_metrics.py` against the Pass A `download()` output. Consume only the summary — never hand raw OHLCV to the model. Produces:
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
