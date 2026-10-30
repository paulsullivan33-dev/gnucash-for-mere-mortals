#!/usr/bin/env python3
"""Open a saved book and check its arithmetic with GnuCash's engine.

Prints the account tree with balances, then two proofs:

1. Trial balance -- add up every split of every transaction in the
   book. In double-entry bookkeeping the grand total must be zero,
   because every transaction's legs sum to zero.
2. The accounting equation --
       Assets = Liabilities + Equity + (Income - Expenses)
   computed from the balances the engine reports.

Balances follow the engine's sign convention, not the display
convention: money in an income, liability or equity account shows
as a negative number, because those accounts sit on the credit
side. The tree printout flips the sign for those account types so
it reads the way the GnuCash window shows it; the equation uses
the raw values. A parent account's printed balance is the total
of itself and everything under it, as in the window's account tree.

    python3 check-book.py household.sqlite3
"""

import sys
from decimal import Decimal

from gnucash import (
    ACCT_TYPE_EQUITY,
    ACCT_TYPE_INCOME,
    ACCT_TYPE_LIABILITY,
    Session,
    SessionOpenMode,
)

CREDIT_SIDE = {ACCT_TYPE_INCOME, ACCT_TYPE_LIABILITY, ACCT_TYPE_EQUITY}


def as_decimal(numeric):
    return Decimal(numeric.num()) / Decimal(numeric.denom())


def show(account_type, raw_total):
    """Flip credit-side totals so they read as positive amounts."""
    return -raw_total if account_type in CREDIT_SIDE else raw_total


def collect(account, depth, rows, record):
    """Depth-first: fill rows with (depth, account, subtree_total),
    append every account to record, return the subtree total."""
    record.append(account)
    own = as_decimal(account.GetBalance())
    child_rows = []
    total = own
    for child in account.get_children_sorted():
        total += collect(child, depth + 1, child_rows, record)
    rows.append((depth, account, total))
    rows.extend(child_rows)
    return total


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: check-book.py BOOKFILE")
    bookfile = sys.argv[1]

    session = Session(f"sqlite3://{bookfile}",
                      SessionOpenMode.SESSION_NORMAL_OPEN)
    book = session.book
    root = book.get_root_account()

    print("== Account tree with balances ==")
    record = []
    top_totals = {}
    for top in root.get_children_sorted():
        rows = []
        top_totals[top.GetName()] = collect(top, 0, rows, record)
        for depth, account, subtree in rows:
            print(f"{'  ' * depth}{account.GetName()}: "
                  f"${show(account.GetType(), subtree):,.2f}")

    assets = top_totals["Assets"]
    liabilities = top_totals["Liabilities"]
    equity = top_totals["Equity"]
    income = top_totals["Income"]
    expenses = top_totals["Expenses"]

    print()
    print("== Trial balance ==")
    split_total = Decimal(0)
    split_count = 0
    seen_txns = set()
    for account in record:
        for split in account.GetSplitList():
            split_count += 1
            split_total += as_decimal(split.GetValue())
            seen_txns.add(split.GetParent().GetGUID().to_string())
    print(f"Transactions in book: {len(seen_txns)}")
    print(f"Splits in book:       {split_count}")
    print(f"Sum of all splits:    ${split_total:,.2f}  (must be 0.00)")

    print()
    print("== The accounting equation ==")
    left = assets
    right = -liabilities + -equity + (-income - expenses)
    print(f"Assets:                    ${assets:,.2f}")
    print(f"Liabilities:               ${-liabilities:,.2f}")
    print(f"Equity:                    ${-equity:,.2f}")
    print(f"Income - Expenses:         ${-income:,.2f} - ${expenses:,.2f}"
          f" = ${-income - expenses:,.2f}")
    print(f"Liabilities + Equity + (Income - Expenses) = ${right:,.2f}")
    print(f"Balanced: {left == right}")

    session.end()


if __name__ == "__main__":
    main()
