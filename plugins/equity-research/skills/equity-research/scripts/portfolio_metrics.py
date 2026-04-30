"""
Portfolio-level metrics: weighted beta, correlation matrix, drawdown simulation.

STUB with working interfaces. The skill can call these functions once yfinance
data is pulled in. Fill in the TODOs as needed or the skill can use the
interfaces as a contract and call yfinance inline.

Install: pip install pandas numpy yfinance
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class PositionMetric:
    ticker: str
    weight: float
    beta: float
    sector: str
    value: float


def compute_weights(positions: list[dict], prices: dict[str, float]) -> pd.DataFrame:
    """
    Given positions [{ticker, shares, ...}] and a dict of current prices,
    return a DataFrame with ticker, shares, price, value, weight.
    """
    rows = []
    for p in positions:
        price = prices.get(p["ticker"])
        if price is None:
            continue
        value = p["shares"] * price
        rows.append({"ticker": p["ticker"], "shares": p["shares"], "price": price, "value": value})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["weight"] = df["value"] / df["value"].sum()
    return df.sort_values("weight", ascending=False).reset_index(drop=True)


def weighted_beta(weights: pd.DataFrame, betas: dict[str, float]) -> float:
    """Portfolio beta = sum(weight_i * beta_i)."""
    return float(
        sum(
            row["weight"] * betas.get(row["ticker"], 1.0)
            for _, row in weights.iterrows()
        )
    )


def correlation_matrix(price_history: pd.DataFrame) -> pd.DataFrame:
    """
    price_history: DataFrame of daily close prices, columns=tickers, index=dates.
    Returns the correlation matrix of daily returns.
    """
    returns = price_history.pct_change().dropna()
    return returns.corr()


def drawdown_scenario(
    weights: pd.DataFrame, betas: dict[str, float], market_decline_pct: float
) -> dict:
    """
    Estimate portfolio loss in a market drawdown scenario.
    Uses the simple model: position_loss ≈ weight * beta * market_decline.
    """
    per_position = []
    total_loss = 0.0
    for _, row in weights.iterrows():
        beta = betas.get(row["ticker"], 1.0)
        loss_pct = beta * market_decline_pct
        loss_dollar = row["value"] * (loss_pct / 100)
        per_position.append(
            {
                "ticker": row["ticker"],
                "weight": row["weight"],
                "beta": beta,
                "loss_pct": loss_pct,
                "loss_dollar": loss_dollar,
            }
        )
        total_loss += loss_dollar
    return {
        "market_decline_pct": market_decline_pct,
        "portfolio_loss_dollar": total_loss,
        "portfolio_loss_pct": total_loss / weights["value"].sum() * 100,
        "per_position": per_position,
    }


def concentration_stats(weights: pd.DataFrame) -> dict:
    """Top-N concentration percentages."""
    w = weights.sort_values("weight", ascending=False)
    return {
        "top_1_pct": float(w["weight"].head(1).sum() * 100),
        "top_3_pct": float(w["weight"].head(3).sum() * 100),
        "top_5_pct": float(w["weight"].head(5).sum() * 100),
        "top_10_pct": float(w["weight"].head(10).sum() * 100),
        "num_positions": int(len(w)),
        "herfindahl": float((w["weight"] ** 2).sum()),
    }


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Portfolio metrics")
    parser.add_argument("--portfolio-json", required=True, help="Path to portfolio JSON")
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch prices and betas from yfinance (requires internet)",
    )
    args = parser.parse_args()

    with open(args.portfolio_json) as f:
        portfolio = json.load(f)
    positions = portfolio["positions"]

    if args.fetch:
        try:
            import yfinance as yf  # type: ignore
        except ImportError:
            print("yfinance not installed. pip install yfinance", file=sys.stderr)
            return 1
        tickers = [p["ticker"] for p in positions]
        info = {}
        prices = {}
        for t in tickers:
            tk = yf.Ticker(t)
            tk_info = tk.fast_info if hasattr(tk, "fast_info") else {}
            prices[t] = getattr(tk_info, "last_price", None) or tk.info.get("regularMarketPrice")
            info[t] = tk.info
        betas = {t: info[t].get("beta", 1.0) or 1.0 for t in tickers}
    else:
        print(
            "[info] --fetch not passed; expecting prices/betas in portfolio JSON",
            file=sys.stderr,
        )
        prices = portfolio.get("prices", {})
        betas = portfolio.get("betas", {})

    weights = compute_weights(positions, prices)
    if weights.empty:
        print(json.dumps({"error": "no weights computed — missing prices?"}))
        return 1

    result = {
        "weights": weights.to_dict(orient="records"),
        "portfolio_beta": weighted_beta(weights, betas),
        "concentration": concentration_stats(weights),
        "drawdowns": {
            "-15%": drawdown_scenario(weights, betas, -15),
            "-25%": drawdown_scenario(weights, betas, -25),
            "-40%": drawdown_scenario(weights, betas, -40),
        },
    }
    json.dump(result, sys.stdout, indent=2, default=float)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
