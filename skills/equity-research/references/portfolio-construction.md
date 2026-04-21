# Portfolio construction — intake, metrics, review

## Normalized schema

Everything flows into this:

```python
Position = {
    "ticker": str,             # normalized upper-case, e.g., "AAPL"
    "shares": float,           # can be fractional
    "avg_cost": float | None,  # per-share in USD
    "cost_basis_date": str | None,  # ISO date
    "account": str | None,     # "taxable", "IRA", "401k", "Roth", etc.
    "notes": str | None,       # user-provided thesis, target, etc.
}

Portfolio = {
    "positions": list[Position],
    "cash": float | None,
    "currency": str,           # default "USD"
    "as_of_date": str | None,
    "owner_notes": str | None, # overall goals, constraints
}
```

## Input format handlers

### Excel / CSV

Use `scripts/parse_portfolio.py`. It handles:
- Fuzzy column matching — recognizes `ticker`, `symbol`, `stock`, `sym` as ticker; `shares`, `qty`, `quantity`, `units` as share count; `cost`, `avg cost`, `cost basis`, `basis`, `price paid` as avg cost
- Multi-sheet files — asks which sheet if ambiguous
- Blank rows, header in row 2+, totals rows (ignore)
- Broker-specific exports (Fidelity, Schwab, Robinhood, IBKR templates pre-configured)

Confirm the parsed output back to the user as a table before running analysis.

### Screenshot / image
Read the image with vision. Extract rows into the schema. Common sources:
- Brokerage app screenshots (Robinhood, Fidelity, Webull, Schwab)
- Google Sheets screenshots
- Hand-written portfolios
- Photos of printouts

Watch for:
- Truncated tickers (scroll bars cutting off names)
- Rounded share counts
- Missing columns (image may only show ticker + value)

### PDF broker statement
Invoke the `pdf` skill. Then post-process into the schema.

Broker-specific quirks:
- **Fidelity**: multi-account summary on first page; per-account detail follows. Watch for margin, IRA, brokerage all commingled.
- **Schwab**: positions grouped by asset class. Stocks section is what you want.
- **Robinhood**: simpler layout, ticker + shares + mkt value
- **IBKR**: dense; positions are in the "Open Positions" section
- **Vanguard**: organized by account type; mutual funds mixed with ETFs and stocks

### Typed / pasted text
Common formats to handle:
```
AAPL 100 @ 150
AAPL, 100, 150
100 shares of AAPL at $150
AAPL x 100
```

### Mixed / ambiguous
Ask. Don't guess. Cost of asking is one message; cost of a misparse is 50 wasted MCP calls and potentially wrong advice.

## Confirmation step (mandatory)

Before any analysis:

```
I parsed your portfolio as:
| # | Ticker | Shares | Avg cost | Current value | Weight |
|---|--------|--------|----------|---------------|--------|
| 1 | AAPL   | 100    | $150     | $18,500       | 22.3%  |
...
Total: $82,900 + $5,000 cash

Does this look right?
```

Only proceed on confirmation or after corrections.

## Fallback rules

| Missing field | Behavior |
|---|---|
| avg_cost | Run analysis, skip tax-aware recommendations |
| shares but % weights given | Work in percentages, flag that dollar-level math is skipped |
| ticker invalid | Call `lookup()`, ask user if still unclear |
| cash balance | Assume 0, note the assumption |
| account type | Assume taxable, note the assumption |

## Portfolio-level metrics (what to compute)

### Concentration
- % in top 1, top 3, top 5, top 10 positions
- % in single sector, top 3 sectors
- % in single country
- % in single market cap bucket

Flag:
- Any single position > 15%
- Single sector > 35%
- <3 sectors covered

### Risk
- Weighted portfolio beta (from individual `get_ticker_info` betas)
- Correlation matrix (from `download([all], period="1y")`)
  - Average pairwise correlation > 0.7 = effectively one bet
- Drawdown simulation: position P&L in -15%, -25%, -40% market, given beta
- Short interest across book
- Liquidity risk (any position in sub-500k ADV name?)

### Performance
- Book P&L if cost basis available
- Realized / unrealized
- LTCG vs. STCG breakdown
- vs. SPY benchmark return since cost basis date (if dates given)

### Income
- Weighted dividend yield
- Yield-on-cost (if cost basis given)
- Dividend growth rate of top holdings

### Factor exposure
- Growth / value tilt (from P/E and growth rates)
- Quality tilt (ROIC, debt)
- Momentum tilt (6M relative performance)
- Size tilt (mcap-weighted average)
- International exposure

## Aggressive-growth mandate — the review lens

Under the default mandate, prefer:
- Higher beta (>1.0 portfolio beta acceptable, >1.3 for conviction)
- Growth factor tilt
- Concentration in conviction names (up to 15% single-position for true high-conviction bets)
- Thematic exposure (one or two genuinely aggressive positions — TQQQ, ARKK, single-name high-beta)
- International satellite (EEM, INDA, or similar for emerging market upside)

Avoid in this mandate:
- Large cash drags (>20% cash without reason)
- Excessive defensive positioning (staples, utilities, long bonds) unless tactical
- Dividend-heavy tilt unless explicitly income-seeking
- Over-diversification (40+ positions dilute alpha)

## Thesis integrity check

For each meaningful position, ask:
- Why did you buy this? (ask user if unclear)
- Does that thesis still apply given current evidence?
- If you didn't own it, would you buy it now at current price?

Categorize each position:
- **Thesis intact, conviction high** → potentially add
- **Thesis intact, conviction moderate** → hold
- **Thesis weakening** → trim or set tight stop
- **Thesis broken** → exit
- **Legacy / unclear** → evaluate from scratch as if buying today

The "would you buy it today?" question is the most honest filter.
