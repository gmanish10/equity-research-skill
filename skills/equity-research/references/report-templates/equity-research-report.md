# Equity research report — deliverable template

Structure to use when building the .docx report for a full stock deep-dive. `scripts/report_builder.py` reads this structure.

## Document structure

### Cover
- Title: `{Company Name} ({Ticker}) — Equity Research Report`
- Subtitle: `{Report date} | Aggressive-Growth Analysis`
- Prepared by: `Equity Research Skill`
- **Disclaimer** (prominent, not small print): "This document is for educational and informational purposes only. Not personalized financial advice."

### 1. Executive summary (first page, always)
- One-line verdict: e.g., "BUY — short-term tactical setup, mid-term growth thesis intact, long-term moat strengthening"
- Current price vs. short / mid / long targets in a single line
- Top three reasons to own
- Top three reasons to avoid
- Key risks (one line each)

### 2. Investment thesis
One paragraph, then three bullets: the central bull case.

### 3. Bull / Base / Bear cases
Each with:
- Price target
- Probability (subjective — high / medium / low)
- Key assumptions that must hold

### 4. Business model (Phase 1)
From `references/supply-chain-research.md`:
- Revenue segments with % mix
- Customer concentration
- Supplier / vendor dependencies
- Supply chain geography
- Commodity exposure
- Moat assessment

### 5. Sector context (Phase 2)
From `references/sector-analysis.md`:
- Sector + sub-industry
- Macro regime fit
- Peer comparison table (8–12 names, key metrics)
- Sector valuation vs. history

### 6. Fundamentals (Phase 3)
From `references/fundamentals.md`:
- Growth: revenue / EPS / FCF CAGR + trajectory commentary
- Margins: table of 5Y gross / operating / net margins
- Returns: ROE, ROIC, ROA
- Balance sheet snapshot
- Cash flow quality + capital allocation commentary
- Valuation: multiples table (stock vs. 5Y avg vs. peers vs. sector)
- Analyst consensus snapshot

### 7. Technicals (Phase 4)
From `references/technicals.md`:
- Trend summary (primary, secondary, short-term)
- Moving average positioning (20/50/200)
- Momentum (RSI, MACD)
- Support / resistance levels
- Relative strength vs. SPY
- Chart pattern if present
- **Include 1Y chart image** if `scripts/report_builder.py` can embed matplotlib

### 8. Options (Phase 5)
From `references/options.md`:
- IV level + rank/percentile
- Put/call ratio
- Max pain + nearby magnet strikes
- Implied move around next earnings
- Notable unusual activity

### 9. News, ownership, sentiment (Phase 6)
From `references/social-sentiment.md`:
- Recent material news (last 30 days)
- Insider activity summary
- Institutional positioning
- Retail sentiment read
- Short interest

### 10. Multi-horizon rating blocks (Phase 7)
Three full rating blocks in the exact structure defined in SKILL.md. Bold the rating. Include WHAT KILLS THIS TRADE on every horizon.

### 11. Risk register
Ranked list of specific risks, each with:
- Scenario description
- Estimated probability (low / medium / high)
- Estimated impact (% drawdown)
- Mitigation or monitoring approach

### 12. Opportunities / upside catalysts
Specific events or conditions that could drive the name higher.

### 13. Data appendix
- Full peer comp table
- 5-year financial summary table
- Price chart (annotated)
- Any supporting visualizations

### Back page
- Methodology note
- Data sources
- **Disclaimer** (repeated)

## Formatting notes

- Use tables wherever data is tabular
- Bold all key numbers (ratings, targets, critical risk metrics)
- Use section dividers (horizontal rules)
- Include the mandatory disclaimer on cover AND back page
- Report length target: 6–10 pages for a standard stock; 12–16 for a full deep-dive with extensive peer analysis
