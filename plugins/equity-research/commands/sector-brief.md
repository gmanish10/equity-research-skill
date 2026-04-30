---
description: Sector analysis and rotation brief — best names, top ETFs, aggressive-lens picks
argument-hint: SECTOR (e.g., technology, energy, healthcare, semiconductors)
---

# /sector-brief

Produce a sector brief for `$ARGUMENTS`. Follow `skills/equity-research/references/sector-analysis.md` for the methodology.

## Workflow

### 1. Sector composition
- `get_sector_data(<sector_key>)` — sub-industries, top companies, top ETFs, top funds
- `get_industry_data(<industry_key>)` for any sub-industry worth drilling into

### 2. Sector-level aggregates
- Aggregate valuation vs. 10Y history (P/E, P/S, P/B) — estimate from top-10 weighted by market cap
- Earnings revision trend — aggregate from `get_analyst_data(eps_trend)` on key names
- Sector performance vs. SPY YTD / 1Y / 3Y

### 3. Macro regime
- What factor regime favors this sector? (rates, dollar, growth, commodity prices)
- Current regime match — is this sector in or out of favor?
- Rotation signals — where is money flowing? (screen_stocks + sector ETF performance)

### 4. Best-in-class and worst-in-class
- Top 3 names by fundamentals + momentum composite
- Bottom 2 names (deteriorating)

### 5. Entry vehicles
- Flagship cap-weighted ETF
- Equal-weight alternative (often better for diversified sector exposure)
- Thematic / leveraged alternative for aggressive bets (with decay warnings)
- Best single-name bet if the user wants concentration

### 6. Aggressive-lens verdict

```
Sector view:  [Overweight / Neutral / Underweight]
Conviction:   [High / Medium / Low]
Best vehicle: [ETF ticker or single name]
Thesis:       [1–2 lines]
WHAT KILLS THIS CALL: [macro / regime / company-specific triggers]
Time horizon: [ST / MT / LT emphasis]
```

## Deliverable

Chat brief by default.

Mandatory disclaimer.
