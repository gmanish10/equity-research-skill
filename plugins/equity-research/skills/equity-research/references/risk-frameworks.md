# Risk frameworks — the risk callout template

**Non-negotiable rule:** every aggressive rating and every aggressive recommendation ships with a quantified risk callout. No exceptions.

## The risk callout structure

```
WHAT KILLS THIS TRADE:
- [Scenario 1 — specific trigger] → estimated loss: X%
- [Scenario 2 — specific trigger] → estimated loss: Y%
- [Scenario 3 — specific trigger] → estimated loss: Z%
Max plausible drawdown: ~W%
Invalidation level: $A (close below = thesis broken)
```

Every item must be:
- **Specific** (not "market goes down")
- **Quantified** (estimated % loss or $ impact)
- **Tied to observable triggers** (price levels, news events, macro data)

## Example — good risk callouts

### Example A — NVDA bullish call
```
WHAT KILLS THIS TRADE:
- Hyperscaler capex guide-down (MSFT/META/GOOGL/AMZN cut AI spend plans) → -25–35%
- China export controls escalate to full ban → -15–20%
- AMD/custom ASIC gains material cloud share → -20–30% over 12 months
- Next-gen chip delay (Blackwell / Rubin pushed out) → -10–15%
Max plausible drawdown: -40% in 12M
Invalidation level: weekly close below 50-WMA ($X)
```

### Example B — TQQQ aggressive bullish
```
WHAT KILLS THIS TRADE:
- Nasdaq-100 sharp selloff (>10% in 30 days) → -30%+ due to 3× daily reset
- Sideways chop for 6+ months → -15–25% decay even if Nasdaq is flat
- Fed hawkish surprise (rate path reset) → -25% in weeks
- VIX regime shift above 25 sustained → -20% decay acceleration
Max plausible drawdown: -50–60% (precedent: 2022)
Invalidation level: QQQ weekly close below 40-WMA
```

### Example C — Small-cap aggressive long
```
WHAT KILLS THIS TRADE:
- Recession signal (ISM < 45, unemployment > 5%) → -25–35% (small caps are most sensitive)
- Credit spreads widen past 500bps → -15–20%
- Company-specific: next earnings guide below street by >10% → -20–30%
- Liquidity event (ADV drops below 200k) → wider spreads, forced trim
Max plausible drawdown: -40%
Invalidation level: daily close below prior major swing low
```

## Example — bad risk callouts (do not do this)

```
WHAT KILLS THIS TRADE:
- Market sells off
- Company misses earnings
- Macro headwinds
```

Too generic, unquantified, unactionable. Rewrite it.

## Position sizing guidance

Pair every aggressive rating with position sizing. Use this framework:

| Conviction | Stability | Max position size |
|---|---|---|
| High | Stable (e.g., AAPL, MSFT) | 10–15% |
| High | Volatile (e.g., TSLA, NVDA) | 7–12% |
| High | Highly volatile (small cap growth, leveraged ETF, meme) | 3–7% |
| Medium | Stable | 5–8% |
| Medium | Volatile | 3–5% |
| Medium | Highly volatile | 1–3% |
| Low / speculative | Any | ≤2% |

Options positions: sum of premium-at-risk across all options ≤ 15–20% of portfolio.

## Hedging considerations

When the portfolio has heavy concentration or the macro regime is hostile, consider:

- **Protective puts** on outsized positions (3–6 month puts 10–15% below current)
- **Collars** (long put + short call) — finances downside protection by capping upside
- **VIX calls or VXX** — explicit vol hedge (decay risk — don't hold long)
- **Index puts** (SPY / QQQ) — portfolio-level hedge if book is highly correlated
- **Inverse ETFs** (SH, PSQ) — tactical shorts; SQQQ / SPXU only for short holds
- **Gold exposure** (GLD, IAU) — uncorrelated tail hedge
- **Cash raise** — never underrated; dry powder has option value

Don't over-hedge an aggressive portfolio — the cost of hedging compounds and erodes alpha. Hedge when the scenario warrants it, not as standing practice.

## Stop-loss discipline

Aggressive ≠ stop-less. Every position should have a defined invalidation level at entry:

- Technical: prior swing low, 50-DMA, or 200-DMA
- ATR-based: 2× ATR below entry
- Fundamental: thesis-specific (e.g., "exit if next earnings guide misses by >5%")
- Time-based: "exit in 6 months if thesis hasn't played out" (especially for options)

Stops should be mental OR hard orders. Mental stops without discipline = no stops.

## Tail-risk awareness

Even an aggressive portfolio should consider low-probability, high-impact events:

- Market crashes (-30%+ in weeks)
- Single-stock blowups (accounting fraud, drug trial failures, geopolitical seizure)
- Black swan macro events (pandemic, major war, currency crisis)
- Broker / counterparty failure (keep assets at regulated, insured brokers)

These don't appear in normal risk models. Mention them explicitly when they're in the frame.

## The one-paragraph risk summary

At the end of any deliverable with multiple aggressive recommendations, include a portfolio-level risk paragraph:

> "Combined, this set of recommendations produces a portfolio with [X] beta, [Y]% concentration in [top sector], and estimated maximum drawdown of [Z]% in a SPY -25% scenario. The largest single-name risk is [ticker] at [A]% weight. The largest thematic risk is [theme] at [B]%. Consider [specific hedge] if [specific condition]."

One paragraph. Everything quantified.
