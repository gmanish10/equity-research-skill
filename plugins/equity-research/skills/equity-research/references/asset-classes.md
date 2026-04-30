# Asset-class adaptations

The 7-phase framework is tuned for US equities. For non-equity instruments, some phases compress, substitute, or don't apply. This file lists the deltas per asset class. Read the relevant section before running a deep dive on anything that isn't a US operating company.

---

## Crypto (`BTC-USD`, `ETH-USD`, `SOL-USD`, etc.)

Yahoo Finance covers spot-crypto pseudo-tickers with the `-USD` suffix. Crypto-exposure equities (COIN, MSTR, HOOD, MARA, RIOT) are normal stocks — run them through the standard 7 phases.

**Phases that apply as-is:**
- Phase 4 (technicals) — fully applies; crypto is more technical than fundamental
- Phase 6 (news / sentiment) — extra important; crypto is largely sentiment-driven. Social, Twitter/X crypto, and on-chain-analytics news carry real weight.

**Phases that substitute:**
- Phase 1 (business model) → **tokenomics**: total supply, issuance / inflation schedule, stake / burn mechanics, protocol treasury, governance model, validator / miner economics
- Phase 2 (sector context) → **macro-crypto regime**: BTC dominance, ETH/BTC, stablecoin supply, ETF flows; position against risk-on / risk-off equities
- Phase 3 (fundamentals) → **on-chain metrics where available**: active addresses, transaction count, fees paid, TVL (for DeFi), hash rate (for PoW), staking yield (for PoS). Yahoo doesn't provide these — note the data gap and pull from web if the question warrants it
- Phase 5 (options) → not available on Yahoo for spot crypto; crypto-exposure equities retain normal options analysis

**Beta:** compute vs. **BTC** as the market proxy, not SPY. Also compute vs. SPY to gauge correlation-breakdown risk during crypto drawdowns.

**Don't claim:** crypto-equivalent of ROE, P/E, DCF, or dividend yield for non-productive assets. These don't exist.

**Lens interaction:**
- Under `aggressive`: allocations up to 10-15% of book, altcoin sleeves considered
- Under `balanced`: BTC + ETH only, capped at 5% of book
- Under `conservative`: generally not recommended; if held, cap at 2% as a tail-risk / macro-debasement hedge

---

## REITs (`O`, `PLD`, `EQIX`, `AMT`, etc.)

REITs are businesses, but the valuation framework differs from operating companies.

**Phases that apply as-is:** 1, 2, 4, 5, 6, 7.

**Phase 3 substitutions:**
- Use **FFO (Funds from Operations)** and **AFFO**, not EPS. P/FFO is the primary multiple.
- Payout ratio = dividends / AFFO (REITs must distribute ≥90% of taxable income by law)
- **Cap rate** = NOI / property value; compare to 10Y treasury + equity-risk premium
- **Debt / EBITDA** and fixed-charge coverage matter more than net margin
- **Occupancy**, **rent growth**, **WALE** (weighted average lease expiry) are the health metrics
- Property-type exposure (industrial / data center / office / retail / residential / healthcare / self-storage) drives risk profile and is the main factor split
- SS-NOI growth (same-store NOI) separates organic from M&A growth

**Phase 4 note:** REITs trade inversely to the 10Y yield more than equities do. Pull `^TNX` and `TLT` into the correlation matrix.

**Lens interaction:**
- Under `aggressive`: data-center / tower / industrial REITs as secular-growth plays; typically underweight office and retail
- Under `balanced`: diversified REIT ETF (VNQ) or 3-4 quality REITs as an income sleeve, 5-10% of book
- Under `conservative`: high-quality, low-payout-ratio REITs for income, 10-15% of book; avoid highly-levered or secularly-challenged property types

---

## International / ADRs (`TSM`, `BABA`, `NVO`, `ASML`, etc.)

Yahoo covers major international tickers and ADRs normally. Depth varies by market capitalization and listing.

**Phases that apply:** all 7, with the following deltas.

**Phase 1 (business model):** reporting currency ≠ price currency — always note which. A Taiwanese revenue line in TWD converted to a USD ADR price has a currency translation sitting between them.

**Phase 3 (fundamentals):**
- Different accounting standards (IFRS vs. GAAP) — look for reconciliation items, especially R&D capitalization, goodwill impairment rules, lease accounting
- `get_analyst_data` coverage can be thinner — note it
- **Currency risk in earnings**: an ADR can outperform or underperform the local listing purely on FX moves. Pull the relevant FX pair (e.g. `TWD=X`, `EUR=X`) and decompose total return = local return × FX translation.

**Phase 4 (technicals):**
- For ADRs, pull both the ADR ticker AND the local listing if it's on Yahoo (e.g. `TSM` ADR + `2330.TW` local). ADR price gaps at US open reflect overnight local trading — the local chart is the clean technical read.

**Phase 6 (news / sentiment):**
- US coverage is thinner — broaden web search to local sources (FT, Economist, Bloomberg Europe / Asia, Nikkei for Japan, Reuters Asia, local-language outlets translated)
- Regulatory risk is higher — PCAOB for Chinese ADRs, EU regulatory actions, India SEBI rules, UK listing regime changes

**Phase 7 `WHAT KILLS THIS TRADE` additions:**
- **FX depreciation** — a 15% currency move wipes 15% of ADR value regardless of operating performance
- **Delisting / sanctions risk** — especially acute for Chinese ADRs (HFCAA), Russian ADRs (sanctioned), any jurisdiction with capital controls
- **Dividend withholding tax** — varies by country-treaty; matters for yield names (e.g. 35% for Swiss, 15% for most treaty partners)

**Data gaps:** holdings, options, sustainability, and sometimes even earnings history can be thin for non-mega-cap international. Say so rather than inferring.

**Lens interaction:** all three lenses can hold international; aggressive can concentrate in thematic emerging markets, conservative should stick to large-cap developed-market dividend payers.

---

## Fixed-income ETFs (`TLT`, `AGG`, `HYG`, `LQD`, `EMB`, `MUB`, etc.)

Treat as ETFs for structure, but the signals are different.

**Phases that apply:** 2, 4, 6, 7, plus the ETF-analysis backbone from `etf-analysis.md`.

**Phase 3 substitutions:**
- **Duration** (in years) — primary rate-sensitivity metric. 1% rate move ≈ duration × 1% price move.
- **Yield-to-maturity** / SEC yield — the forward yield the fund earns
- **Credit quality mix** — AAA / AA / A / BBB for investment-grade; BB / B / CCC for high-yield. Weight by % of portfolio.
- **Option-adjusted spread (OAS)** — spread over treasuries, adjusted for embedded options (callable bonds, mortgages). Tight vs. wide vs. history = regime indicator.
- **Effective convexity** — second-order rate sensitivity; matters for MBS and callables

**Macro overlay (required):** pull the yield curve as context — `^TNX` (10Y), `^FVX` (5Y), `^TYX` (30Y), and for short end `^IRX` (13-week). Curve shape (steep / flat / inverted) sets the regime.

**Spread products (HYG, LQD, EMB, BKLN):** add a credit-spread regime read — current spread vs. 10y median. Spread widening = price down; spread tightening = price up. This matters more than the yield itself on short timeframes.

**Don't apply:** PEG, P/E, ROE, DCF, options analysis (Phase 5 skip unless the ETF itself has a liquid options chain — TLT does, AGG doesn't really).

**Don't claim:** individual-bond picking, yield-curve positioning beyond what the ETF's duration already expresses, or CUSIP-level credit analysis. That's a different skill / data source.

**Lens interaction:**
- `aggressive`: long-duration (TLT) as a tactical rate-cut play, or HY (HYG) for yield and equity-correlated beta; 0-15% of book
- `balanced`: intermediate-duration core (AGG, BND) at 15-30% of book
- `conservative`: short-duration (SHY, BIL) + intermediate core + muni (MUB) as tax-efficient income; 30-50% of book

---

## FX pairs (`EURUSD=X`, `GBPJPY=X`, etc.)

Yahoo covers major pairs. Treat purely as technical + macro.

**Phases that apply:** 2 (macro regime), 4 (technicals), 6 (news), 7 (verdict).

**Skip:** 1 (no business model), 3 (no fundamentals in the equity sense), 5 (no options on Yahoo for spot FX).

**What matters:** relative rate differentials between the two central banks, balance-of-payments, commodity exposure (AUD/CAD/NOK are commodity currencies), risk-on/risk-off positioning (JPY/CHF are havens).

**Don't pretend** this is a currency-trading desk. FX is a separate discipline; what the skill can do is put an FX view in the macro context of an equity / portfolio decision.

---

## Unsupported — say so, don't fake it

- **Individual bonds** (CUSIP-level): no Yahoo/MCP coverage. Needs Bloomberg / Refinitiv / TRACE.
- **Commodity futures** (`CL=F`, `NG=F`, `GC=F`): Yahoo shows the front-month contract, but rolling costs and contango/backwardation aren't exposed cleanly. Use ETF proxies (USO, UNG, GLD) for directional views — explicitly flag the decay in `WHAT KILLS THIS TRADE`.
- **Private companies, pre-merger SPACs, OTC pinks without Yahoo data**: out of scope. Offer qualitative analysis only if web sources support it; don't fabricate numerical ratings.
- **Leveraged single-stock ETFs** (NVDL, TSLL, etc.): covered as equities with an explicit decay + path-dependence callout in Phase 7.

When the user asks about one of these, say so upfront, offer what you *can* do, and stop.
