---
description: Options-flow read — IV, skew, unusual activity, magnet levels, implied move
argument-hint: TICKER [expiration: nearest|monthly|YYYY-MM-DD (default: nearest)]
---

# /options-flow

Options-flow read on `$ARGUMENTS`. Follow `skills/equity-research/references/options.md` for methodology.

## Workflow

### 1. Get expirations
- `get_options($TICKER)` — returns available expiration dates
- Pick the target expiry based on the user's argument (default: nearest)

### 2. Pull the chain
- `get_options($TICKER, <expiry>)` — full calls and puts

### 3. Compute / read the signals

Use `skills/equity-research/scripts/options_analytics.py` where applicable:

- **IV level, IV rank, IV percentile** — is vol elevated or cheap?
- **Put/call open interest ratio** — sentiment skew
- **Put/call volume ratio** — flow skew (more timely than OI)
- **Skew** — are OTM puts expensive relative to OTM calls? (fear pricing)
- **Max pain** — where the most open interest expires worthless
- **Magnet levels** — strikes with outsized open interest (often act as S/R)
- **Unusual activity** — strikes with volume > 3× open interest, large block prints
- **Implied move** — straddle at the ATM strike → ±% expected move by expiry

### 4. Connect to price action
- Where is the current price relative to max pain and high-OI strikes?
- Does the options market expect a bigger or smaller move than recent realized vol?

### 5. Aggressive-lens verdict

```
Setup:        [bullish / bearish / neutral / event-driven]
Conviction:   [High / Medium / Low]
Suggested play: [long calls / long puts / credit spread / buy stock + sell covered call / straddle]
Strike guidance: [specific strikes]
Expiry:       [specific date]
WHAT KILLS THIS TRADE: [max loss + scenarios]
Position sizing: [max % of options P&L budget]
```

**Options warning:** options can go to zero. Size accordingly and never use them with money you can't afford to lose. This is extra-emphasized even for aggressive investors.

## Deliverable

Chat response. Include charts only if useful (straddle P&L, payoff diagram via matplotlib).

Mandatory disclaimer + options-specific risk warning.
