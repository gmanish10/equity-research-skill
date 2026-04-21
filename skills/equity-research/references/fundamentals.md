# Fundamentals — methodology

Goal: answer "is this a good business, and is it priced to own?"

Pull data via the MCP. Compute ratios yourself — don't trust pre-computed ones. Consistency beats convenience.

## Data to pull

```
get_financials(symbol, "income",   "yearly")     # 5 years
get_financials(symbol, "income",   "quarterly")  # 8 quarters
get_financials(symbol, "balance",  "yearly")
get_financials(symbol, "cashflow", "yearly")
get_earnings(symbol, "quarterly", include_dates=true)
get_analyst_data(symbol, "estimates")
get_analyst_data(symbol, "eps_trend")
get_analyst_data(symbol, "growth")
get_analyst_data(symbol, "price_targets")
get_dividends_splits(symbol)
get_ticker_info(symbol, fast=false)   # for market cap, ratios, 52-week range
```

For peer comparison: `get_industry_data` → `get_tickers_info([peers])` in a single batch call.

## What to compute

### Growth

- Revenue YoY and QoQ — is growth accelerating or decelerating?
- EPS YoY and QoQ — same question
- FCF YoY — actual cash, not adjusted metrics
- 3Y and 5Y revenue / EPS / FCF CAGR
- Segment-level growth (from 10-K) if disclosed

Signal: accelerating revenue with accelerating margins is the best setup for aggressive positioning. Decelerating revenue with expanding margins is a late-cycle setup — be cautious.

### Margins

- Gross margin = gross profit / revenue
- Operating margin = operating income / revenue
- Net margin = net income / revenue
- EBITDA margin = EBITDA / revenue
- R&D as % of revenue, SG&A as % of revenue (the opex line items)
- Trend: expanding / stable / compressing? Why?

Expanding gross margin with stable opex is the cleanest sign of pricing power and operating leverage.

**Mandatory margin-trajectory check (aggressive-growth lens):** compute margin deltas across the last four fiscal years AND print them explicitly in the report. Do not rely on absolute levels alone. A company at a 71% gross margin looks great in isolation, but if that's down 390 bps from 75% the year prior, the aggressive case has to reckon with it. Call out any line-item that has moved by more than 200 bps YoY and explain the driver (mix shift, input cost, pricing concession, acquisition-related comp, etc.). "Gross margin 71%, down from 75%" is the honest read; "gross margin 71%" alone is the misleading one.

### Returns

- ROE = net income / avg equity
- ROIC = NOPAT / invested capital (net debt + equity)
- ROA = net income / avg assets

ROIC above WACC means the business is creating value. ROIC consistently above sector average is moat evidence.

### Balance sheet health

- Net debt = total debt − cash and equivalents
- Net debt / EBITDA (leverage ratio)
- Interest coverage = EBIT / interest expense
- Current ratio = current assets / current liabilities
- Quick ratio = (current assets − inventory) / current liabilities
- Goodwill + intangibles as % of total assets (acquisition quality flag)
- Debt maturity schedule if available from 10-K

### Cash flow quality

- FCF = operating cash flow − capex
- FCF yield = FCF / market cap (compare to risk-free rate)
- FCF conversion = FCF / net income (>1.0 is healthy, <0.8 is suspicious)
- Capex intensity = capex / revenue (growing businesses invest; mature ones should return cash)
- Capital allocation: dividends vs. buybacks vs. M&A vs. debt paydown — where's the cash going?

### Earnings quality

- Earnings surprise history (beats vs. misses, magnitude)
- `get_analyst_data(eps_trend)` — estimate revisions over last 30/60/90 days. Upward revisions are a strong positive signal.
- Accruals as flag: if net income grows much faster than operating cash flow, earnings quality is degrading
- Look for one-offs in income statement (gains on sale, impairments, litigation)

## Valuation

### Multiples (from `get_ticker_info`)

- P/E (trailing and forward)
- P/S (useful for unprofitable growth names)
- P/B (useful for financials)
- EV/EBITDA (cleanest cross-capital-structure comparison)
- EV/Revenue (for growth names)

Always compare to:
1. The stock's own 5-year history (is it rich / cheap vs. itself?)
2. Direct peers (get_tickers_info on peer set)
3. Sector median

### PEG ratio

PEG = forward P/E / earnings growth rate. <1.0 is cheap-for-growth, 1.0–2.0 fair, >2.0 expensive.

### DCF sanity check

For names where fundamentals warrant it, run a simple DCF:
- Start with TTM FCF
- Grow at analyst consensus rate for 5Y, then fade to GDP-like (2–3%) in years 6–10
- Terminal value: Gordon growth (FCF × (1+g) / (r−g)) or exit EV/EBITDA multiple
- Discount rate: risk-free (10Y treasury) + beta × equity risk premium (5–6%)
- Sum PV of cash flows + terminal value → enterprise value
- Subtract net debt → equity value
- Divide by shares → per-share fair value

Don't pretend DCF is precise — it's a sensitivity tool. Run base / bull / bear cases by varying growth rate and discount rate.

### Analyst consensus

- `get_analyst_data(price_targets)` — current price vs. low / mean / high target
- High target − current price = analyst-implied upside (anchor, not truth)
- `get_analyst_data(upgrades_downgrades)` — momentum of sentiment
- `get_analyst_data(estimates)` — forward revenue and EPS

Trend matters more than level. Upgrades + rising estimates + rising price = momentum. Upgrades + rising estimates + falling price = opportunity. Downgrades + falling estimates + rising price = danger.

## Aggressive-growth lens on fundamentals

For aggressive-growth investing, weight these signals highest:

1. **Accelerating revenue growth** (durable, not one-off)
2. **Expanding operating margins**
3. **Positive estimate revisions** (eps_trend)
4. **High ROIC** (capital discipline)
5. **Growing FCF** (reinvestment capacity)

Willing to pay high multiples when growth and returns justify them. Unwilling to pay high multiples for decelerating names.

## Red flags

- Net income growing faster than revenue forever (eventually mean-reverts)
- FCF conversion < 0.7 for multiple years
- Rising net debt + rising intangibles (debt-fueled acquisitions)
- Declining estimate revisions
- Aggressive capitalization of operating costs
- Frequent non-GAAP adjustments that never repeat
- Share count growing faster than revenue (dilution)
