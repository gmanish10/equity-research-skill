# Options analytics — methodology

Goal: extract signals from the options market and, where appropriate, recommend options-based expressions of a thesis.

## Data to pull

```
get_options(symbol)                        # returns list of expirations
get_options(symbol, <target_expiry>)       # returns full chain for that expiry
```

Typical expiries to analyze:
- **Weekly** (nearest Friday) — most tactical, biggest gamma
- **Monthly** (third Friday of upcoming month) — most open interest, cleanest read
- **Next earnings** — for event-driven positioning
- **LEAPS** (≥1Y out) — for long-term directional bets

## Signals to extract

### Implied volatility

- **IV level**: ATM (at-the-money) implied volatility — what the market expects the stock to do
- **IV rank**: current IV vs. its 52-week range → 0 = lowest, 100 = highest. High IV rank = options are expensive (favor selling). Low IV rank = options are cheap (favor buying).
- **IV percentile**: % of days in last year when IV was below current. Similar to rank but more stable.
- **Term structure**: IV across expirations. Normal is upward-sloping. Backwardation (near-term IV > long-term IV) signals event risk or stress.

### Skew

- OTM put IV vs. OTM call IV
- Normal: puts trade at higher IV than calls (people pay for downside protection)
- Extreme put skew = market pricing in crash risk
- Call skew (calls > puts IV) = euphoria / squeeze pricing, often unsustainable

### Put/call ratios

- OI ratio: total put OI / total call OI
- Volume ratio: daily put volume / call volume
- Volume ratio is more timely (today's positioning), OI is more sticky

Typical reads:
- P/C volume > 1.5 = bearish sentiment (often contrarian bullish)
- P/C volume < 0.5 = bullish sentiment (often contrarian bearish)
- Extreme readings often mark reversals

### Max pain

The strike where the most options (by dollar value) expire worthless. Market makers have a structural interest in price migrating to max pain by expiry. Useful as a magnet level into the last week before monthly expiry.

Computed by `scripts/options_analytics.py`.

### Magnet / high-OI strikes

Identify strikes with outsized open interest. These often act as support or resistance. The larger the position, the stronger the magnetism.

### Unusual activity

Strikes where today's volume > 3× open interest, especially at strikes far from ATM. Could signal:
- Directional bet by a large participant
- Earnings positioning
- Hedging by an institution

Large block prints (single trades > 500 contracts) at OTM strikes are often smart-money signals worth investigating.

### Implied move around earnings

ATM straddle (call + put at the strike closest to current price) / stock price = implied % move by expiry. Compare to historical average post-earnings move.

Example: stock at $100, ATM straddle at $5 → implied move ±5%. If last 4 earnings moved 3%, 4%, 3%, 4% → 5% is expensive and options are pricing in elevated expectations.

## Strategies — matching thesis to expression

### Bullish thesis
- Moderate conviction, low IV: long calls (ATM or slightly OTM), 30–90 DTE
- High conviction, low IV: long calls closer to expiry for leverage
- Moderate conviction, high IV: bull call spreads (limit cost, cap upside)
- Already own stock: covered calls for income
- Low IV rank + bullish: cash-secured puts at support → get paid to wait for a pullback

### Bearish thesis
- Short-term bearish: long puts, 30–60 DTE
- Moderate bearish: bear call spreads (credit spreads, defined risk)
- Hedging existing long: protective puts at 5–10% below current

### Event-driven (earnings, FDA, macro event)
- Expect a big move either way: long straddle or strangle
- Expect a contained move (IV is overpriced): iron condor (sell the range)

### High conviction long-term
- LEAPS calls (≥1Y expiry) → synthetic leveraged stock ownership with defined risk

## Rules for aggressive option use

- **Size small**: 1–5% of the portfolio per options trade, max 15–20% of the book in options at any time
- **Never buy lottery tickets at earnings** without understanding IV crush — IV often drops 30–50% after the event
- **Avoid options on thinly traded underlyings** (wide spreads eat returns)
- **Know your max loss before entering** — long options can go to zero; short options have asymmetric downside
- **Exit discipline**: define take-profit and stop-loss levels in contract value, not just underlying price

Options are leverage. Used well, they amplify aggressive-growth returns. Used badly, they cut the account in half.
