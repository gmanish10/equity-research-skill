---
description: Screen live data for new buy ideas — stocks, ETFs, or options overlays — to fill a mandate or gap
argument-hint: mandate (e.g. "AI exposure", "high-growth software under 40x", "a hedge for my tech book", "dividend ETF")
---

# /find-ideas

Surface **new** candidates to buy for the mandate in `$ARGUMENTS`. This is idea generation, not review of existing holdings. Follow SKILL.md → Section 5, "Idea generation".

## Core rule

**Candidates come from a live screen, never from memory.** A name you simply recall is not a sourced idea and fails the quality bar. Pull the longlist from the tools and prove it survived a real workup.

## Workflow

### 1. Define the mandate → screen criteria
Translate `$ARGUMENTS` into explicit, reproducible filters bounded by the lens caps: sector/theme, market cap, growth, margins, momentum, valuation, yield, beta. State the criteria. If the mandate is vague ("good stocks"), ask one clarifying question or default to the aggressive-growth lens and say so.

### 2. Screen, don't recall
- `screen_stocks` with the filters above for single-name longlist.
- `get_sector_data` / `get_industry_data` for sector/industry leaders and **top ETFs** when an ETF or thematic vehicle fits the mandate.
- For an options-overlay idea, identify the underlying first, then read its chain via `/options-flow` methodology.

### 3. Filter against the book (if one is in context)
Drop candidates redundant with or highly correlated to existing holdings — a new idea must add an exposure the book lacks. Prefer the **ETF equivalent over a mutual fund** for new money (cost, liquidity, tax). 

### 4. Shortlist → mini deep-dive via subagents
Take the top ~3–5 survivors. Dispatch **one Task subagent per candidate** running the 7-phase framework (compact verdict acceptable), each returning only its verdict. Memory-sourced names that don't survive get cut here.

### 5. Rank and recommend
Present survivors best-first, each with:
- The **role / gap it fills** and what it adds that a typical book lacks
- Sizing within lens caps
- Full quality-bar verdict — falsifiable trigger, quantified downside, conviction, opportunity cost (what it beats)
- The **screen criteria + live metrics** behind it ("screened >20% rev growth, <40 fwd P/E, survived workup"), not "great company"

## Gating & deliverable

Candidates are recommendations — **gate them in plan mode** before they ship. Chat ranked list by default; offer a `.docx` if the user wants to share or it's a long shortlist.

Mandatory disclaimer.
