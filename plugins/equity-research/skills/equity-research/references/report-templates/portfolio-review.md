# Portfolio review — deliverable template

Structure for the .docx portfolio review. Consumed by `scripts/report_builder.py`.

## Document structure

### Cover
- Title: `Portfolio Review — {User Name or "Client"}`
- Subtitle: `{Review date} | Aggressive-Growth Lens`
- **Disclaimer** (prominent): "This document is for educational and informational purposes only. Not personalized financial advice."

### 1. Executive summary
- Portfolio value (if known)
- Weighted beta
- Top three actions (with triggers and timelines)
- Key risks in one paragraph
- Overall assessment: e.g., "Aggressively positioned but over-concentrated in semis. Recommend trimming two names and adding one ETF to complement."

### 2. Portfolio snapshot
Table of all positions:
| # | Ticker | Shares | Avg cost | Current price | Value | Weight | Sector | 6M return |

Summary stats:
- Number of positions
- Largest position + weight
- Cash %
- Sector breakdown table

### 3. Concentration and diversification
- Single-name concentration flags
- Sector concentration
- Geography breakdown
- Correlation matrix (heatmap if possible)
- Average pairwise correlation — is this one bet or many?

### 4. Risk profile
- Weighted beta
- Simulated drawdowns:
  - -15% market scenario
  - -25% market scenario
  - -40% market scenario
- Short interest exposure
- Liquidity risk flags
- Factor exposure summary

### 5. Per-position assessment
For each position — a brief rating table:

| # | Ticker | Weight | Thesis status | Quality | Momentum | Action |
|---|--------|--------|---------------|---------|----------|--------|
| 1 | NVDA   | 22%    | Intact        | Strong  | Strong   | TRIM to 15% |
| 2 | MSFT   | 18%    | Intact        | Strong  | Strong   | KEEP |

For top 10 positions, include a 2–3 sentence narrative each.

### 6. Action matrix (the centerpiece)
The full action matrix from `/rebalance-plan`:

| # | Action | Ticker | Size | Trigger | Deadline | Risk callout |

### 7. Proposed portfolio
After all recommended actions, show the target-state portfolio:
- New weight table
- New weighted beta
- New concentration / sector breakdown
- Expected risk profile change

### 8. Hedging considerations
If concentration or macro warrants hedging — specific suggestions with cost and coverage.

### 9. Tax considerations
If cost basis provided — LTCG / STCG on proposed sells, tax-loss harvesting opportunities.

### 10. Portfolio-level risk paragraph
The one-paragraph summary from `references/risk-frameworks.md`.

### 11. What to monitor
Specific conditions, price levels, and catalysts to watch that would trigger action:
- "If 10Y yield breaks 5%, revisit the growth sleeve"
- "If NVDA earnings guide below $X, execute trim immediately"
- etc.

### Back page
- Methodology
- Data sources
- **Disclaimer** (repeated)

## Formatting

- Heavy use of tables — portfolios are tabular by nature
- Color-code actions (red = trim/sell, green = add/buy, neutral = keep) if docx styling allows
- Sector breakdown as a pie chart (via matplotlib in report_builder)
- Correlation matrix as a heatmap
- Report length target: 8–12 pages
