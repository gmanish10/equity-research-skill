# Social sentiment and news — methodology

Goal: read the crowd. Sentiment rarely predicts returns alone, but divergence between fundamentals and sentiment is actionable.

## Data sources (web search required)

### News sources
- **Yahoo Finance news**: `get_ticker_calendar(symbol, "news")` — first stop, MCP-sourced
- **SEC filings**: `get_ticker_calendar(symbol, "sec_filings")` — primary-source catalysts
- **Bloomberg, Reuters, CNBC** — mainstream financial news
- **Seeking Alpha** — analyst opinions, often contrarian
- **Company IR page** — press releases, earnings transcripts

### Social platforms
- **Reddit**: r/wallstreetbets (retail momentum/YOLO energy), r/investing (more considered), r/stocks (balanced), r/SecurityAnalysis (deep dives)
- **Twitter / X**: finance Twitter — "fintwit." Look at posts from well-known analysts, the CEO if active, and any trending topic around the ticker
- **StockTwits**: retail sentiment tracker — bullish/bearish % for every ticker
- **Discord / Substack**: harder to search but sometimes show up in news

### Key-person commentary
- CEO / CFO X posts — look for anything recent that could move the stock
- Earnings call transcripts — tone, hedging language, Q&A answers
- Analyst day / investor day presentations
- Conference presentations (industry conferences, sell-side investor conferences)

## What to look for

### Sentiment direction
- Is the crowd bullish, bearish, or indifferent?
- Has sentiment shifted recently (catalyst-driven)?
- Note the magnitude — mildly bullish ≠ euphoric

### Sentiment vs. fundamentals divergence
The most actionable pattern:
- **Fundamentals improving + sentiment negative** → classic contrarian long
- **Fundamentals deteriorating + sentiment euphoric** → classic contrarian short / avoid
- **Both aligned** → trend continuation likely

### Narratives and memes
- What story is the crowd telling about this stock?
- Is it backed by fundamentals or is it pure narrative?
- Memes can persist longer than you'd think (GME, AMC) but eventually revert
- Aggressive traders can ride memes but need hard stops

### Controversies
- Short-seller reports (Hindenburg, Muddy Waters, Citron)
- Management controversies (SEC investigations, lawsuits, allegations)
- Product failures or recalls
- Regulatory actions
- ESG scandals

Distinguish noise from signal — many short reports are wrong, but a high-quality report on a company with accounting flags is a real warning.

### Catalyst watch
- Upcoming earnings
- Product launches
- Regulatory decisions (FDA PDUFA, FTC rulings)
- Analyst days
- Macro events that disproportionately affect this name

Use `get_market_calendar("earnings")` and `get_market_calendar("economic")` for structured calendar data.

## Insider activity as sentiment

From `get_holders(symbol, "insider_purchases")` and `get_holders(symbol, "insider_transactions")`:

- Open-market purchases (vs. option exercises) are the meaningful signal
- CEO buying > CFO buying > directors buying > option-exercise noise
- Cluster buying (multiple insiders over 30 days) is strongly bullish
- Persistent selling across multiple insiders is a negative signal — but context matters (scheduled 10b5-1 sales are neutral; unscheduled cluster sells are not)
- Zero insider buying in a beaten-down stock that should be "obvious value" is itself a signal — insiders know something

## Institutional positioning

From `get_holders(symbol, "institutional")`:
- Top holders — are they big quality allocators (Vanguard, BlackRock, Fidelity passive) or hedge funds with actual views?
- Changes in institutional ownership quarter-over-quarter (from 13F filings, web search)
- Increasing institutional ownership = accumulation; decreasing = distribution

## Short interest

From `get_ticker_info` → `shortPercentOfFloat`, `shortRatio`:
- >20% short is heavily shorted — either deep issues or squeeze potential
- Days-to-cover > 5 makes squeeze setups more plausible
- Rising short interest on a rising stock = powerful squeeze potential
- Rising short interest on a falling stock = confirmation of bearish thesis

## How to summarize in the research report

Keep the sentiment section short and actionable (4–6 sentences). Include:

1. Prevailing retail sentiment (bullish/bearish/mixed) and direction of change
2. Any notable divergence from fundamentals
3. Recent catalysts or news items
4. Insider activity net direction
5. Short interest level + trajectory
6. Key upcoming catalysts

Don't write an essay on sentiment. Connect it to the rating.

## Rules for aggressive-lens sentiment reads

- **Strong fundamentals + negative sentiment** is the best aggressive setup
- **Institutional accumulation + insider buying + crowd bearish** → contrarian long
- **Euphoric sentiment + extended price + no new fundamental support** → time to trim
- **Short squeeze setups** are exciting but fleeting — size small, set stops, don't marry them
- **Meme momentum** is real but not a thesis — use it for short-term trades, not core positions
