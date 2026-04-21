# Supply chain, customers, vendors — methodology

Goal: understand who the company actually depends on. This is where theses break — not in the financials.

The MCP doesn't cover this well. Most of this is from SEC filings and web search.

## Data to pull

```
get_ticker_info(symbol, fast=false)                     # business summary, segments
get_ticker_calendar(symbol, "sec_filings")              # latest 10-K, 10-Q, 8-K links
get_ticker_calendar(symbol, "news")                     # recent developments
```

Then web search:
- "{company} 10-K customer concentration"
- "{company} major suppliers"
- "{company} supply chain China / Taiwan / Mexico" (geographic exposure)
- "{company} key customers" — sometimes disclosed in press releases
- "{company} risk factors 10-K" — list of what the company says could go wrong

## What to extract

### Revenue segments
From 10-K segment reporting:
- Business lines and their revenue %
- Growth trajectories per segment
- Which segment is growing / shrinking
- Geographic revenue mix (US vs. international)

### Customer concentration
- Any customer > 10% of revenue? The SEC requires disclosure. This is a major risk — loss of that customer is catastrophic.
- Contract length (multi-year vs. transactional)
- Customer churn signals (retention rates if disclosed)
- End-market exposure (if customer industry struggles, so does this company)

Examples:
- AAPL supplier dependency on Apple — enormous % for companies like SWKS, QRVO, AVGO
- Enterprise SaaS dependency on a handful of Fortune 500 — check if top 5 customers are > 30% of ARR
- Defense contractors with US DoD as dominant customer — political exposure

### Supplier and vendor concentration
- Key input suppliers
- Sole-source suppliers (single point of failure)
- Contract manufacturers
- Critical components (chips, batteries, rare earths)

Examples:
- Everyone depending on TSMC for leading-edge nodes
- EV makers depending on battery suppliers (CATL, LG, Panasonic)
- Pharma depending on Indian/Chinese active pharmaceutical ingredient (API) suppliers

### Geographic supply chain exposure
- Where is manufacturing?
- Where are raw materials sourced?
- Where are assembly and testing?
- Exposure to specific countries with geopolitical / trade policy risk

Common vectors:
- China (tariffs, export controls, tensions)
- Taiwan (semiconductor concentration; geopolitical tail risk)
- Mexico (USMCA; labor costs)
- Europe (energy dependency, regulatory intensity)

### Commodity exposure
- Oil / gas (fuel and petrochemical inputs)
- Metals (copper, steel, aluminum, lithium, cobalt, rare earths)
- Agricultural (food & bev)
- Freight rates (shipping, trucking)

A 10% commodity price move can crush margins for commodity-exposed names.

## Red flags to surface

1. **Top 1–3 customers > 25% of revenue** — single-point-of-failure revenue risk
2. **Single-source critical suppliers** — operational fragility
3. **>50% of manufacturing in a single country** — geopolitical tail risk
4. **Fixed-price contracts when input costs are rising** — margin compression coming
5. **Supplier concentration that matches a competitor's concentration** — both fight for the same capacity
6. **"Material weakness" or "significant deficiency" in 10-K** — accounting controls risk
7. **Disclosed but unquantified litigation** — binary event risk

## Moat through the supply chain lens

Durable moats often show up as:
- **Scale advantages**: largest buyer gets best pricing from suppliers
- **Vertical integration**: less dependency on suppliers (e.g., AMZN logistics, TSLA batteries)
- **Exclusive supplier contracts**: locked-in capacity (important in constrained markets)
- **Diversified supplier base**: no single point of failure
- **Pricing power with customers**: can pass through input cost increases

Conversely, moats erode when:
- A supplier integrates forward and becomes a competitor
- A customer integrates backward and replaces you
- A new supplier undercuts established relationships
- A geopolitical shock forces supply chain relocation

## What to produce

A short narrative block (4–6 sentences) in the research report covering:
1. How the company makes money (segments + revenue mix)
2. Biggest customer exposures
3. Biggest supplier / vendor dependencies
4. Geographic supply chain concentration
5. Commodity / input cost exposure
6. Specific fragility points to watch

This feeds directly into the risk register in Phase 7.
