# Technical analysis — methodology

Goal: answer "is now a good time to enter, and where do I get out?"

Pull price data via MCP, compute indicators via `scripts/technicals.py`. Don't eyeball — compute.

## Data to pull

```
get_price_history(symbol, period="1y",  interval="1d")   # daily primary
get_price_history(symbol, period="5y",  interval="1wk")  # weekly for long-term trend
get_price_history(symbol, period="3mo", interval="1h")   # intraday setup if needed
download([symbol, "SPY", sector_etf], period="6mo")      # relative strength
```

## Trend

- Primary trend = direction of the 200-DMA
  - Rising 200-DMA = bull regime
  - Falling 200-DMA = bear regime
  - Flat 200-DMA = range-bound
- Secondary trend = direction of 50-DMA
- Short-term trend = price vs. 20-DMA
- Trend structure:
  - Higher highs + higher lows = uptrend
  - Lower highs + lower lows = downtrend
  - Mixed = consolidation

### Key crosses

- Golden cross: 50-DMA crosses above 200-DMA → bullish intermediate signal
- Death cross: 50-DMA crosses below 200-DMA → bearish intermediate signal

These are lagging; by the time they trigger, the move is often underway. Use them as confirmation, not entry.

## Momentum

### RSI (14-period)
- `>70` = overbought (not a sell signal by itself; strong trends can stay overbought)
- `<30` = oversold
- `40–60` = neutral
- Divergence matters: price making new highs while RSI isn't → weakening momentum

### MACD
- MACD line = 12-EMA − 26-EMA
- Signal line = 9-EMA of MACD
- Histogram = MACD − Signal
- Bullish when MACD crosses above signal, especially above zero line
- Divergence from price is a warning

### Stochastics (less critical — RSI + MACD usually cover it)
- %K and %D — similar overbought/oversold reads

## Support and resistance

- Swing highs/lows on daily chart — look for levels tested 3+ times
- Round numbers ($50, $100, $200) often act as psychological levels
- Volume profile: high-volume-node levels (where most trading happened) act as magnets
- Prior all-time highs act as resistance; former resistance becomes support after a breakout

### Options-implied levels

Use `get_options(symbol, nearest_expiry)` to find strikes with outsized open interest. These often act as magnetic levels, especially into expiry. See `references/options.md`.

## Volume

- 20-day average volume from `get_ticker_info`
- Volume spike: current > 1.5× avg
- Accumulation days (up on high volume) vs. distribution days (down on high volume) — track count over 20 days
- 4+ distribution days in 20 sessions is a warning for institutional selling

## Volatility

- ATR (Average True Range, 14-period) — for stop placement (common: 2× ATR below entry)
- Bollinger Bands (20-period, 2 std dev) — mean reversion signals when price touches the bands
- Historical volatility — compare to implied volatility from options

## Relative strength

- Compute (stock / SPY) ratio — is it trending up (outperforming) or down (underperforming)?
- Same vs. sector ETF — is the stock leading or lagging its own sector?
- Relative-strength leadership is one of the most durable alpha signals

## Beta and correlation (compute — don't trust the ticker field)

`get_ticker_info` returns a `beta` field, but it is often stale, uses a mystery lookback window, and can disagree materially with a properly-computed figure. Always compute beta yourself from daily returns and report BOTH numbers, with the delta and the sample window used.

Procedure:

1. Load 1y of daily closes for the stock, SPY, and the sector ETF (from the `download([stock, "SPY", sector_etf], period="1y", interval="1d")` call in Batch 1).
2. Compute simple daily returns: `ret = close.pct_change().dropna()`.
3. Beta vs. benchmark = `cov(stock_ret, bench_ret) / var(bench_ret)`.
4. Correlation vs. benchmark = Pearson `corrcoef(stock_ret, bench_ret)[0,1]`.
5. Do this once vs. SPY and once vs. the sector ETF.

```python
import numpy as np
beta_spy = np.cov(stock_ret, spy_ret)[0,1] / np.var(spy_ret)
corr_spy = np.corrcoef(stock_ret, spy_ret)[0,1]
```

Report format (insert into the technical verdict block):

```
Beta (1y daily vs SPY):     [computed]   | Yahoo-reported: [field]   | delta: [pp]
Beta (1y daily vs sector):  [computed]
Correlation vs SPY (1y):    [0.xx]
```

**Mandatory callout:** if the computed beta differs from Yahoo's reported beta by more than 20% (relative), flag the discrepancy explicitly in the report and prefer the computed figure for downstream sizing / stop math. Yahoo's field is a reference point, not the answer.

## Chart patterns (pattern recognition)

Look for structure, don't invent it:
- Cup and handle, ascending triangle, flag / pennant, breakout from base — bullish
- Head and shoulders, descending triangle, rising wedge — bearish
- Double bottom / double top — reversal patterns

Pattern validity requires volume confirmation. Patterns without volume are noise.

## Putting it together — the technical verdict

Produce a summary block:

```
Trend:           [bullish / neutral / bearish] — [primary driver]
Momentum:        RSI [X], MACD [above/below signal, above/below zero]
Support:         $A (primary), $B (secondary)
Resistance:      $C (primary), $D (secondary)
Relative strength vs. SPY (6M): [outperform / match / underperform]
Volume:          [accumulation / neutral / distribution]
Volatility:      IV [X%], HV [Y%], IV rank [Z%]
Entry zone:      $E–F
Stop:            $G (based on [swing low / 2× ATR / 50-DMA])
```

## For aggressive-growth positioning

- Prefer names in confirmed uptrends over base-building setups (leaders lead)
- Breakouts from multi-month bases on heavy volume are the highest-probability setups
- Don't chase — use pullbacks to 20-DMA or 50-DMA as entry zones in strong trends
- Size into weakness within an intact uptrend, not strength at resistance
- Hard stops below the 50-DMA or prior swing low — aggressive does not mean hope-based
