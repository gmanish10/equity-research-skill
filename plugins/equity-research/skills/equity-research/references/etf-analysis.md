# ETF analysis — methodology

Goal: understand what an ETF actually does and whether it fits a purpose in the portfolio.

ETFs are not stocks. Don't analyze them like one. A "cheap P/E" on an ETF is meaningless. A "high P/E" may be entirely appropriate.

## Data to pull

```
get_ticker_info(etf_symbol, fast=false)     # expense ratio, AUM, yield, top sectors, category
get_price_history(etf_symbol, period="5y", interval="1d")  # performance + vol
download([etf_symbol, "SPY", alt_etf], period="1y")        # correlation
```

For holdings, `get_ticker_info` returns top holdings and sector weights. For deeper breakdown (e.g., full holdings), web search the ETF issuer's page (iShares, Vanguard, State Street, Invesco).

## The 9 things to check

### 1. Identity
- Full name, sponsor (BlackRock/iShares, Vanguard, State Street/SPDR, Invesco, Schwab, etc.)
- Inception date (older = more data; <3Y = limited track record)
- Structure: ETF, ETN (credit risk to issuer!), closed-end, mutual fund

### 2. Cost + liquidity
- **Expense ratio**: <0.10% is cheap, 0.10–0.30% is fair, >0.50% is expensive (unless thematic/specialized justifies it)
- **AUM**: <$50M is a risk flag (could close). >$1B is safe.
- **Average daily volume**: <100k shares = thin, watch spreads
- **Bid-ask spread**: from `get_ticker_info` — wide spreads erode returns for tactical use
- **Premium/discount to NAV**: should be near zero for a well-functioning ETF

### 3. Methodology
- Underlying index (if any): S&P 500, Nasdaq-100, MSCI, Russell, FTSE, custom
- Weighting: cap-weighted / equal-weighted / revenue-weighted / fundamentally-weighted / factor-weighted / active
- Rebalance frequency: quarterly is typical, monthly is more active, annual is lazy
- Reconstitution frequency (index-level changes)

### 4. Holdings
- Top 10 holdings + % weight in top 10
- Total number of holdings (concentration indicator)
- Sector breakdown
- Country breakdown (for global / international ETFs)
- Concentration check: top 10 > 50% means highly concentrated

### 5. Factor exposure
Infer from top holdings and methodology:
- Growth vs. value
- Quality (high ROE, low debt)
- Momentum
- Size (large / mid / small / micro)
- Low volatility
- Dividend yield

### 6. Performance
- 1Y, 3Y, 5Y, 10Y total return (including dividends)
- Compare to SPY and to direct peers (e.g., IWM vs. VTWO for small-cap)
- Max drawdown
- Sharpe ratio if computable: (ann return − risk-free) / ann vol
- Rolling returns if the user cares about consistency

### 7. Correlation
- With SPY over 1Y
- If user has a portfolio: correlation with their book
- Two high-correlation holdings are the same holding — don't double up. VOO and QQQ have ~0.90 correlation; owning both isn't diversification.

### 8. Role fit
What does this ETF do for the portfolio?
- **Core**: broad diversified exposure (SPY, VOO, VTI, VT, BND)
- **Satellite**: sector or factor tilt (XLK, MTUM, QUAL)
- **Thematic**: concentrated bet on a trend (ARKK, BOTZ, TAN, ICLN)
- **Hedge**: negative correlation to risk assets (GLD, TLT, VXX, SH, SQQQ)

### 9. Risks
- **Concentration**: top 10 > 50% of fund
- **Liquidity**: thin ADV
- **Sponsor**: small issuer, possible closure
- **Tax inefficiency**: high turnover → cap gains distributions. MLPs (K-1). Leveraged ETFs (tax-inefficient compounding).
- **Leveraged ETFs**: daily-reset decay — over long holding periods, a 3× ETF does NOT return 3× the underlying. Sideways markets grind them down. Only for tactical use.
- **Structural**: ETN = unsecured debt of issuer. If issuer fails, ETN can go to zero regardless of what the index did.

## Verdict (aggressive-growth lens)

```
ETF:              [ticker]
Role:             [core / satellite / thematic / hedge / avoid]
Fit for aggressive growth mandate: [strong / moderate / weak]
Redundancy check: [none / overlaps with XXX at Y% correlation]
Cost assessment: [cheap / fair / expensive] relative to peers
Entry approach:  [lump sum / DCA over X weeks / on pullback to $X]
Conviction:      [High / Medium / Low]
WHAT KILLS THIS TRADE: [specific risk + expected drawdown in that scenario]
Position sizing: [% of portfolio]
```

## Common aggressive-growth ETF shortlist

- **Core aggressive**: VOO / VTI (broad US); QQQ / QQQM (Nasdaq-100 tech tilt)
- **Growth factor**: VUG, SCHG, MTUM
- **Small-cap growth**: VBK, SCHA
- **Thematic growth**: SOXX / SMH (semis), ARKK (innovation, high beta), XBI (biotech), BOTZ (robotics/AI), ICLN (clean energy)
- **Leveraged tactical**: TQQQ, SOXL (aggressive only — understand decay)
- **International growth**: VXUS (broad ex-US), EEM / VWO (emerging markets), INDA (India single-country)

Pick based on what role the portfolio needs filled, not just what's "hot."
