#!/usr/bin/env python3
"""Peek inside a GnuCash SQLite book with plain SQL.

A book saved in the SQLite format is an ordinary database file:
no GnuCash needed to look at its tables. This script lists the
tables that matter, counts the rows, and adds up the splits two
ways -- per account, and in total -- using nothing but Python's
built-in sqlite3 module.

It only reads. Run it on a copy if the book is open elsewhere:
GnuCash locks its book while it works.

    python3 peek-book.py household.sqlite3
"""

import sqlite3
import sys
from decimal import Decimal


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: peek-book.py BOOKFILE")
    db = sqlite3.connect(f"file:{sys.argv[1]}?mode=ro", uri=True)

    tables = [row[0] for row in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "ORDER BY name")]
    print(f"Tables in the book: {len(tables)}")
    for name in ("books", "accounts", "transactions", "splits",
                 "commodities"):
        count = db.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
        print(f"  {name:<14} {count} rows")

    print()
    print("Accounts (name, type):")
    for name, acct_type in db.execute(
            "SELECT name, account_type FROM accounts "
            "WHERE name != 'Root Account' ORDER BY name"):
        print(f"  {name:<18} {acct_type}")

    print()
    print("Split totals by account (engine sign convention):")
    per_account = {}
    for name, num, denom in db.execute(
            "SELECT a.name, s.value_num, s.value_denom FROM splits s "
            "JOIN accounts a ON a.guid = s.account_guid"):
        value = Decimal(num) / Decimal(denom)
        per_account[name] = per_account.get(name, Decimal(0)) + value
    total = Decimal(0)
    for name in sorted(per_account):
        total += per_account[name]
        print(f"  {name:<18} {per_account[name]:>10,.2f}")
    print(f"  {'TOTAL':<18} {total:>10,.2f}  (must be 0.00)")


if __name__ == "__main__":
    main()
