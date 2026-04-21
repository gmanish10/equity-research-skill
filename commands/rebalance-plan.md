---
description: Concrete rebalancing plan with gated actions, timelines, and risk callouts
argument-hint: [target tilt: e.g., "more aggressive", "reduce tech concentration", or no argument for general review]
---

# /rebalance-plan

Translate a portfolio review into a concrete, gated action plan. This is the "what do I actually do" command.

## Prerequisites

Portfolio must already be in context. If not, run `/analyze-portfolio` first.

## Workflow

### 1. Define the target
Extract the target tilt from `$ARGUMENTS`. Common cases:
- "more aggressive" — raise beta, concentrate into conviction, add thematic exposure
- "less concentrated" — trim outsized positions, diversify
- "income-tilted" — add dividend ETFs or covered-call overlays
- "defensive" — raise cash, add hedges (unusual given the skill's default mandate)
- No argument — general optimization under the default aggressive-growth mandate

### 2. Build the action matrix

For each action, specify all five fields:

| Field | What goes here |
|---|---|
| Action | BUY / SELL / TRIM / ADD / HEDGE |
| Ticker + size | Exact ticker, dollar amount or % of book |
| Trigger | Price level, technical signal, catalyst, macro event, or "immediate" |
| Deadline | Date or event by which to act if trigger isn't hit |
| WHAT KILLS THIS | Quantified downside scenario |

### 3. Tax considerations
If cost basis is available:
- Flag LTCG vs. STCG on every sell action
- Identify tax-loss harvesting opportunities (sell loser + buy similar-but-not-identical replacement)
- Prefer selling STCG-disadvantaged losers before LTCG winners

### 4. Order of operations
Sequence the actions logically:
1. Sells / trims first (fund the buys)
2. Hedges next (reduce downside during repositioning)
3. Adds / entries last (deploy capital)

### 5. Express the full plan as a table

```
| # | Action | Ticker | Size    | Trigger              | Deadline | Risk callout           |
|---|--------|--------|---------|----------------------|----------|------------------------|
| 1 | TRIM   | NVDA   | Reduce to 15% | Price ≥ $X or 7-day RSI > 75 | 4 weeks | Cap gains tax + FOMO if continues higher |
| 2 | ADD    | TSM    | $X       | Close > 50-DMA       | 2 weeks  | Geopolitical / Taiwan risk |
...
```

### 6. Post-plan summary

Top 3 highest-conviction actions in plain English at the end, so the user has a TL;DR.

## Deliverable

Chat response by default. Offer to write a .docx if the plan has >6 actions or involves complex conditionality.

Mandatory disclaimer.
