# Sector analysis — methodology

Goal: understand where a stock lives and whether the neighborhood is good.

## The 11 GICS sectors

Technology, Healthcare, Financials, Consumer Discretionary, Communication Services, Industrials, Consumer Staples, Energy, Utilities, Real Estate, Materials.

Each has its own valuation norms, cyclicality, and macro sensitivity. Don't apply technology norms to utilities.

## Data to pull

```
get_sector_data(<sector_key>)               # top industries, companies, ETFs, funds
get_industry_data(<industry_key>)           # peers, ETFs within an industry
get_tickers_info([top_8_peers])             # peer valuation snapshot in one call
get_price_history(<sector_etf>, period="5y", interval="1mo")  # long-term sector context
```

## Sector cheat sheet — what to check per sector

| Sector | Primary drivers | Macro sensitivity |
|---|---|---|
| Technology | Innovation cycle, capex, rates | Inverse to long rates |
| Healthcare | Demographics, pipeline, pricing | Somewhat defensive |
| Financials | Yield curve, credit cycle | Banks love steep curves, hate inversions |
| Consumer Discretionary | Consumer spending, wages | Pro-cyclical |
| Communication | Ad spend, content cycles | Mixed |
| Industrials | Capex, ISM, trade | Pro-cyclical |
| Consumer Staples | Defensive, pricing power | Counter-cyclical |
| Energy | Oil price, rig count | Direct commodity |
| Utilities | Rates, regulation | Inverse to rates |
| Real Estate | Rates, cap rates, demographics | Inverse to rates |
| Materials | Commodity prices, China | Global cyclical |

## Regime analysis

Different macro regimes favor different sectors:

| Regime | Favored | Avoid |
|---|---|---|
| Growth accelerating, rates falling | Tech, Discretionary, Comm Services | Staples, Utilities |
| Growth decelerating, rates falling | Staples, Utilities, Healthcare, REITs | Cyclicals, Financials |
| Growth accelerating, rates rising | Energy, Industrials, Financials, Materials | Rate-sensitive growth |
| Growth decelerating, rates rising | Defensive value, cash, gold | Everything cyclical |

Use web search to establish current regime: Fed stance, GDP nowcast, ISM, yield curve shape, inflation trajectory.

## Aggregate sector metrics to compute

- **Aggregate valuation**: market-cap-weighted P/E, P/S, EV/EBITDA of top 10 sector names
- **vs. 10Y history**: where does current valuation sit in its own range? (require SPY-relative for cleaner read)
- **Earnings revision trend**: aggregate `get_analyst_data(eps_trend)` signals across top names — revisions up = positive; down = warning
- **Sector ETF performance**: 1M / 3M / YTD / 1Y total return vs. SPY

## Best-in-class within the sector

Build a peer comp table of the top 8–12 names:

| Ticker | Market cap | Rev growth | Op margin | ROIC | Fwd P/E | EV/EBITDA | 6M rel perf |
|--------|------------|------------|-----------|------|---------|-----------|-------------|

Sort by a composite score (growth × quality × momentum). Top 2–3 = best-in-class candidates. Bottom 2 = avoids.

## Entry vehicles

Give the user options at different conviction levels:

1. **Flagship sector ETF** (cap-weighted) — easiest, highest liquidity
   - Examples: XLK (tech), XLE (energy), XLV (healthcare)
2. **Equal-weight alternative** — reduces concentration in mega-caps; often better risk-adjusted returns
   - Examples: RSPT (tech EW), RYE (energy EW)
3. **Thematic / narrow ETF** — more targeted exposure
   - Examples: SOXX (semiconductors), XBI (biotech), TAN (solar)
4. **Leveraged ETF** — 2× or 3× for aggressive tactical bets. WARN about daily-reset decay — these lose value in sideways markets even if the underlying is flat.
   - Examples: TQQQ, SOXL, FAS
5. **Single-name leader** — highest upside, highest single-company risk
   - Identify via the peer comp

## Sector verdict template

```
Sector:         [name]
Current regime fit: [match / partial match / mismatch]
Valuation:      [rich / fair / cheap] vs. 5Y history
Earnings revisions: [up / flat / down]
6M rel performance vs. SPY: [+X% / flat / -X%]
Overall view:   [Overweight / Neutral / Underweight]
Conviction:     [High / Medium / Low]
Best vehicle:   [ETF or single name]
WHAT KILLS THIS CALL: [specific triggers]
```
