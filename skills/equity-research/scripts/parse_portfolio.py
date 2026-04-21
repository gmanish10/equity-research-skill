"""
Multi-format portfolio intake.

Handles:
- Excel (.xlsx, .xls)
- CSV
- Typed / pasted text blocks
- JSON (if user gives structured)

For screenshots / images: the skill reads those directly with vision,
then calls this script with parsed text or a normalized JSON.

For PDF broker statements: use the `pdf` skill to extract tables first,
then feed the extracted text to --text mode.

Install: pip install pandas openpyxl rapidfuzz

Usage:
    python scripts/parse_portfolio.py --file portfolio.xlsx
    python scripts/parse_portfolio.py --text "AAPL 100 @ 150\\nMSFT 50 @ 320"
    python scripts/parse_portfolio.py --file portfolio.csv --sheet "Holdings"

Output: JSON on stdout (pipe into jq or consume from the skill).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pandas as pd

try:
    from rapidfuzz import fuzz
    HAS_FUZZ = True
except ImportError:
    HAS_FUZZ = False


# ---------- column name matching ----------

COLUMN_CANDIDATES = {
    "ticker": [
        "ticker", "symbol", "stock", "sym", "security", "securitysymbol",
        "instrument", "instrumentname", "tickersymbol",
    ],
    "shares": [
        "shares", "qty", "quantity", "units", "shareqty", "shareqty",
        "numshares", "numberofshares", "position", "holding",
    ],
    "avg_cost": [
        "avg cost", "average cost", "cost", "cost basis", "basis",
        "avgprice", "costpershare", "pricepaid", "purchaseprice",
        "costpershare", "avgpurchaseprice", "averageprice",
    ],
    "cost_basis_date": [
        "date", "purchase date", "trade date", "acquired",
        "acquisition date", "bought on",
    ],
    "account": [
        "account", "account type", "acct", "acct type", "portfolio",
    ],
}


def _normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower().strip())


def _best_match(header: str, candidates: list[str], threshold: int = 80) -> bool:
    """Fuzzy-match a column header to a list of candidate names."""
    h = _normalize(header)
    if h in {_normalize(c) for c in candidates}:
        return True
    if HAS_FUZZ:
        scores = [fuzz.ratio(h, _normalize(c)) for c in candidates]
        return max(scores) >= threshold
    return any(c.lower() in header.lower() for c in candidates)


def _map_columns(df: pd.DataFrame) -> dict[str, str]:
    """Return a mapping of field_name → actual column name in df."""
    mapping: dict[str, str] = {}
    for field, candidates in COLUMN_CANDIDATES.items():
        for col in df.columns:
            if _best_match(str(col), candidates):
                mapping[field] = col
                break
    return mapping


# ---------- parsers ----------

def parse_tabular(df: pd.DataFrame) -> list[dict]:
    """Parse a DataFrame of positions into the normalized schema."""
    mapping = _map_columns(df)
    if "ticker" not in mapping:
        raise ValueError(
            f"Could not find a ticker column. Columns were: {list(df.columns)}. "
            "Please rename the ticker column to 'ticker' or 'symbol'."
        )
    if "shares" not in mapping:
        raise ValueError(
            f"Could not find a shares/quantity column. Columns were: {list(df.columns)}. "
            "Please rename the shares column to 'shares' or 'quantity'."
        )

    positions: list[dict] = []
    for _, row in df.iterrows():
        ticker_raw = row[mapping["ticker"]]
        if pd.isna(ticker_raw):
            continue
        ticker = str(ticker_raw).strip().upper()
        # skip totals / summary rows
        if ticker in {"TOTAL", "TOTALS", "CASH", "SUMMARY", ""}:
            continue
        # skip non-ticker-looking entries
        if not re.match(r"^[A-Z\.\-]{1,10}$", ticker):
            continue

        try:
            shares = float(str(row[mapping["shares"]]).replace(",", ""))
        except (ValueError, TypeError):
            continue
        if shares <= 0:
            continue

        pos: dict = {"ticker": ticker, "shares": shares}

        if "avg_cost" in mapping:
            try:
                cost_str = str(row[mapping["avg_cost"]]).replace("$", "").replace(",", "")
                pos["avg_cost"] = float(cost_str)
            except (ValueError, TypeError):
                pass

        if "cost_basis_date" in mapping:
            try:
                pos["cost_basis_date"] = str(pd.to_datetime(row[mapping["cost_basis_date"]]).date())
            except (ValueError, TypeError):
                pass

        if "account" in mapping:
            acct = row[mapping["account"]]
            if not pd.isna(acct):
                pos["account"] = str(acct).strip()

        positions.append(pos)

    return positions


def parse_text(text: str) -> list[dict]:
    """
    Parse pasted text. Supports common formats:
        AAPL 100 @ 150
        AAPL, 100, 150
        AAPL 100 shares at $150
        AAPL x 100
        100 shares AAPL
    """
    positions: list[dict] = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # patterns, tried in order
        patterns = [
            # AAPL 100 @ 150  or  AAPL, 100, 150
            r"([A-Z\.\-]{1,10})[\s,]+(\d+(?:\.\d+)?)[\s,@xX]+\$?(\d+(?:\.\d+)?)",
            # AAPL 100 shares at $150
            r"([A-Z\.\-]{1,10})\s+(\d+(?:\.\d+)?)\s*shares?\s*(?:at|@)\s*\$?(\d+(?:\.\d+)?)",
            # 100 shares of AAPL at $150
            r"(\d+(?:\.\d+)?)\s*shares?\s*(?:of)?\s*([A-Z\.\-]{1,10})\s*(?:at|@)?\s*\$?(\d+(?:\.\d+)?)?",
            # AAPL 100 (no cost)
            r"([A-Z\.\-]{1,10})[\s,x]+(\d+(?:\.\d+)?)$",
        ]

        matched = False
        for i, pat in enumerate(patterns):
            m = re.match(pat, line)
            if not m:
                continue
            groups = m.groups()
            try:
                if i in (0, 1):
                    ticker, shares, cost = groups
                    positions.append({
                        "ticker": ticker.upper(),
                        "shares": float(shares),
                        "avg_cost": float(cost),
                    })
                elif i == 2:
                    shares, ticker, cost = groups
                    pos = {
                        "ticker": ticker.upper(),
                        "shares": float(shares),
                    }
                    if cost:
                        pos["avg_cost"] = float(cost)
                    positions.append(pos)
                elif i == 3:
                    ticker, shares = groups
                    positions.append({
                        "ticker": ticker.upper(),
                        "shares": float(shares),
                    })
                matched = True
                break
            except (ValueError, TypeError):
                continue

        if not matched:
            print(f"[warn] could not parse line: {line}", file=sys.stderr)

    return positions


def parse_file(path: Path, sheet: str | None = None) -> list[dict]:
    ext = path.suffix.lower()
    if ext in {".xlsx", ".xls"}:
        xl = pd.ExcelFile(path)
        if sheet is None:
            if len(xl.sheet_names) > 1:
                print(
                    f"[info] multiple sheets found: {xl.sheet_names}. Using first. "
                    "Pass --sheet to select a different one.",
                    file=sys.stderr,
                )
            sheet = xl.sheet_names[0]
        df = pd.read_excel(path, sheet_name=sheet)
        return parse_tabular(df)
    elif ext == ".csv":
        df = pd.read_csv(path)
        return parse_tabular(df)
    elif ext == ".json":
        with path.open() as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "positions" in data:
            return data["positions"]
        raise ValueError("JSON must be a list of positions or a dict with 'positions'")
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


# ---------- CLI ----------

def _cli() -> int:
    parser = argparse.ArgumentParser(description="Multi-format portfolio intake")
    parser.add_argument("--file", help="Path to .xlsx/.csv/.json file")
    parser.add_argument("--text", help="Pasted text block")
    parser.add_argument("--sheet", help="Sheet name (for Excel files)")
    parser.add_argument(
        "--cash", type=float, default=None, help="Cash balance to attach to portfolio"
    )
    args = parser.parse_args()

    if not args.file and not args.text:
        parser.error("Provide --file or --text")

    positions = (
        parse_file(Path(args.file), args.sheet)
        if args.file
        else parse_text(args.text)
    )

    portfolio = {
        "positions": positions,
        "cash": args.cash,
        "currency": "USD",
    }
    json.dump(portfolio, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
