# Equity Research Plugin (Aggressive-Growth Edition)

> **Disclaimer — read this first.** This plugin produces opinionated investment analysis for educational and informational purposes only. It is **not personalized financial advice**. Nothing produced by this plugin should be taken as a recommendation to buy, sell, or hold any security. Data is delayed ~15 minutes. Consult a qualified financial advisor before making investment decisions. Past performance does not predict future returns. Options involve substantial risk and can expire worthless. Leveraged ETFs are not long-term investments. You can lose money. Use at your own risk.

A Claude Code and Codex plugin for opinionated, aggressive-growth equity research — stocks, options, ETFs, sectors, and full portfolio reviews. Uses the Yahoo Finance MCP for quantitative data and web search for qualitative context.

## What it does

- **Deep stock research** — a 7-phase workup (business, sector, fundamentals, technicals, options, sentiment, verdict) culminating in a multi-horizon rating with explicit, quantified risk callouts for short / mid / long-term horizons.
- **Portfolio analysis** — intake from Excel, CSV, screenshots, broker PDFs, or typed text. Normalized, confirmed back, then run through concentration, correlation, beta, drawdown, and factor analysis.
- **ETF analysis** — methodology, holdings, factor exposure, correlation with your existing book, role fit.
- **Sector briefs** — composition, aggregates, regime fit, best-in-class names, entry vehicles.
- **Options flow** — IV rank, skew, put/call ratios, max pain, magnet strikes, implied moves, unusual activity.
- **Rebalance plans** — concrete action matrices with triggers, deadlines, and risk callouts per line.

## The framing

This plugin defaults to an **aggressive growth, higher-than-average risk tolerance** lens. It's willing to take a stance. It considers higher-beta names, thematic plays, leveraged ETFs (with warnings), and options overlays.

**But every aggressive recommendation carries a mandatory, quantified risk callout** — a `WHAT KILLS THIS TRADE` block specifying exactly what would invalidate the thesis and how much it would cost. Aggressive != reckless.

## Install on Claude Code

This repo includes Claude Code plugin marketplace metadata. Install it with two commands from inside Claude Code:

```
/plugin marketplace add gmanish10/equity-research-skill
/plugin install equity-research@comprehensive-equity-research
```

After install, restart Claude Code to pick up the new slash commands.

## Install on Codex

This repo also includes Codex plugin metadata:

- `.codex-plugin/plugin.json` — plugin manifest
- `.agents/plugins/marketplace.json` — Codex marketplace manifest
- `skills/equity-research/SKILL.md` — skill entry point
- `commands/*.md` — slash-command prompts

Add the marketplace from Codex CLI:

```bash
codex plugin marketplace add gmanish10/equity-research-skill
```

Then enable the plugin in the Codex plugin UI. If you are installing manually, add this stanza to `~/.codex/config.toml` after adding the marketplace:

```toml
[plugins."equity-research@comprehensive-equity-research"]
enabled = true
```

Restart Codex or open a fresh session after enabling the plugin.

### Prerequisites

- Claude Code or Codex with plugins enabled
- [Yahoo Finance MCP](https://github.com/yahoofinance-mcp) server configured
- Python 3.10+ on the machine running Claude Code or Codex
- Python packages: `pandas numpy openpyxl rapidfuzz yfinance python-docx`

  ```bash
  pip install pandas numpy openpyxl rapidfuzz yfinance python-docx
  ```

## Install as a standalone skill

If you're not using a plugin-capable client, you can install just the skill (without the slash commands) by packaging or copying `skills/equity-research/` into your client's skill location. In clients that support `.skill` files, use the release asset if one is published.

## Usage

Slash commands exposed by the plugin:

| Command | What it does |
|---|---|
| `/research-stock TICKER` | Full 7-phase deep dive |
| `/analyze-portfolio [file]` | End-to-end portfolio review with intake |
| `/analyze-etf TICKER` | ETF one-pager |
| `/sector-brief SECTOR` | Sector analysis + best-in-class picks |
| `/options-flow TICKER` | Options setup read |
| `/rebalance-plan` | Action matrix after a portfolio review |

Or just ask naturally — the skill's description triggers automatically on investment-related queries:

- "Do a deep research workup on NVDA. I want short/mid/long-term views."
- "Here's my portfolio (attaches file). Review it with an aggressive growth lens."
- "What's the options setup on TSLA for next month?"
- "Give me a sector brief on semiconductors."
- "Based on the review, what should I actually do this week?"

## Directory structure

```
equity-research-skill/
|-- .agents/
|   \-- plugins/
|       \-- marketplace.json           # Codex marketplace manifest
|-- .claude-plugin/
|   |-- marketplace.json               # Plugin marketplace manifest
|   \-- plugin.json                    # Claude plugin manifest
|-- .codex-plugin/
|   \-- plugin.json                    # Codex plugin manifest
|-- commands/                          # Slash commands (plugin root)
|   |-- research-stock.md
|   |-- analyze-portfolio.md
|   |-- analyze-etf.md
|   |-- sector-brief.md
|   |-- options-flow.md
|   \-- rebalance-plan.md
|-- skills/
|   \-- equity-research/               # The skill
|       |-- SKILL.md                   # Skill entry point
|       |-- references/                # Deep-dive methodology docs
|       |   \-- report-templates/      # Deliverable templates
|       |-- scripts/                   # Python - technicals, ratios, portfolio intake, etc.
|       \-- evals/                     # Eval test cases
|-- README.md
|-- LICENSE
|-- DISCLAIMER.md
\-- .gitignore
```

## Credits

Built on top of Anthropic's bundled `stock-analyst` skill. The Yahoo Finance MCP orchestration patterns are adapted from that foundation. Specialization (multi-horizon ratings, aggressive-growth framing, ETF workflow, multi-format portfolio intake, risk-callout mandate) is original to this plugin.

## Contributing

Open an issue or PR. Useful directions:

- Additional broker-statement parsers in `skills/equity-research/scripts/parse_portfolio.py`
- More sophisticated DCF / fair value modeling
- Backtesting harness for rating accuracy
- Earnings-call transcript summarization
- Alternative data integrations (e.g., short-seller report tracking)

## License

MIT. See `LICENSE`.

## One more time - this is not financial advice

The plugin is opinionated by design. That does not mean its opinions are correct. Do your own research. Consult a professional. Size positions appropriately. Know what you can afford to lose. Markets are adversarial and humbling.
