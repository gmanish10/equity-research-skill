---
description: ETF analysis — holdings, methodology, factor exposure, role fit
argument-hint: TICKER
---

# /analyze-etf

Deliver an ETF one-pager for `$ARGUMENTS`. ETFs are not stocks — don't analyze them like one.

## Workflow

Follow `skills/equity-research/references/etf-analysis.md` in full. Summary of what to produce:

### 1. Identity
- Name, sponsor, inception date, AUM
- Expense ratio
- ADV, bid-ask spread, premium/discount to NAV

### 2. Methodology
- What index / rulebook does it follow?
- Cap-weighted / equal-weighted / smart-beta / active?
- Rebalance frequency

### 3. Holdings
- Top 10 holdings + % of fund
- Number of holdings total
- Sector breakdown
- Country / geographic exposure
- Concentration (% in top 10)

### 4. Factor exposure
- Growth / value / quality / momentum / size / low-volatility tilt
- Use `get_ticker_info` on top holdings to infer

### 5. Performance
- 1Y, 3Y, 5Y total return
- Max drawdown
- Sharpe ratio (if computable from `get_price_history`)
- Performance vs. SPY and vs. direct peers

### 6. Correlation
- Correlation with SPY over 1Y
- If the user has shared a portfolio: correlation with their existing book → does this ETF add real diversification or is it redundant?

### 7. Role fit
- Core (SPY, VOO, VTI)
- Satellite (sector-specific, thematic)
- Hedge (gold, bonds, inverse)
- Thematic / tactical

### 8. Risks
- Concentration (top-10 > 50%?)
- Liquidity (ADV < 100k shares is thin)
- Sponsor risk (niche issuers)
- Tax inefficiency (K-1 filers, high turnover)
- For leveraged ETFs: daily-reset decay — explicitly warn

### 9. Verdict

Rating block (aggressive-growth lens):
```
Rating:       [Buy / Hold / Avoid]
Role in portfolio: [core / satellite / hedge / avoid]
Conviction:   [High / Medium / Low]
WHAT KILLS THIS TRADE: [specific scenario + estimated drawdown]
Entry approach: [lump sum / DCA / on pullback to $X]
```

## Deliverable

Chat one-pager by default. Offer a .docx if the user wants to share.

Include the mandatory disclaimer.
