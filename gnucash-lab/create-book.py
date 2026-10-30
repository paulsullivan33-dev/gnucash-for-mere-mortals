#!/usr/bin/env python3
"""Create a small household book with GnuCash's own Python bindings.

Builds an account tree, enters eight transactions (one of them a
split with three expense legs), and saves the book as a SQLite database -- the
same file format the GnuCash window program writes.

The household is invented: round numbers, generic names, nobody real.

Run with the GnuCash bindings importable, e.g. on a machine where
python3-gnucash is installed:

    python3 create-book.py household.sqlite3
"""

import sys
from datetime import datetime, timezone

from gnucash import (
    ACCT_TYPE_ASSET,
    ACCT_TYPE_BANK,
    ACCT_TYPE_CREDIT,
    ACCT_TYPE_EQUITY,
    ACCT_TYPE_EXPENSE,
    ACCT_TYPE_INCOME,
    ACCT_TYPE_LIABILITY,
    Account,
    GncCommodity,
    GncNumeric,
    Session,
    SessionOpenMode,
    Split,
    Transaction,
)


def money(cents):
    """GnuCash counts in exact fractions: 12345/100 is $123.45."""
    return GncNumeric(cents, 100)


def make_account(book, parent, name, acct_type, commodity, placeholder=False):
    acct = Account(book)
    acct.BeginEdit()
    acct.SetName(name)
    acct.SetType(acct_type)
    acct.SetCommodity(commodity)
    if placeholder:
        acct.SetPlaceholder(True)
    parent.append_child(acct)
    acct.CommitEdit()
    return acct


def add_transaction(book, currency, when, description, legs):
    """legs is a list of (account, cents). The cents must sum to zero:
    every transaction takes from somewhere and puts somewhere."""
    total = sum(cents for _acct, cents in legs)
    assert total == 0, f"transaction does not balance: {description}"
    txn = Transaction(book)
    txn.BeginEdit()
    txn.SetCurrency(currency)
    stamp = datetime(when[0], when[1], when[2], 12, 0, tzinfo=timezone.utc)
    txn.SetDatePostedSecs(int(stamp.timestamp()))
    txn.SetDescription(description)
    for acct, cents in legs:
        split = Split(book)
        split.SetParent(txn)
        split.SetAccount(acct)
        split.SetValue(money(cents))
        split.SetAmount(money(cents))
    txn.CommitEdit()
    return txn


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: create-book.py BOOKFILE")
    bookfile = sys.argv[1]
    uri = f"sqlite3://{bookfile}"

    # Two sessions, on purpose. Opening a brand-new SQL book makes
    # the engine write the book's skeleton (its tables and root
    # account) immediately, and in GnuCash 5.5 that same session
    # then refuses to store anything else -- a later save trips
    # over the skeleton's book row ("UNIQUE constraint failed:
    # books.guid", reproduced in the lab's transcripts). Closing
    # and reopening the file sidesteps it: from then on, every
    # change is written to the database as it is committed, which
    # is how the SQL backend is designed to work. No save() call
    # is needed, or wanted, in the second session.
    Session(uri, SessionOpenMode.SESSION_NEW_STORE).end()

    session = Session(uri, SessionOpenMode.SESSION_NORMAL_OPEN)
    book = session.book
    root = book.get_root_account()

    usd = GncCommodity(book, "US Dollar", "ISO4217", "USD", "840", 100)

    assets = make_account(book, root, "Assets", ACCT_TYPE_ASSET, usd, True)
    checking = make_account(book, assets, "Checking Account", ACCT_TYPE_BANK, usd)
    savings = make_account(book, assets, "Savings Account", ACCT_TYPE_BANK, usd)

    liabilities = make_account(book, root, "Liabilities", ACCT_TYPE_LIABILITY, usd, True)
    card = make_account(book, liabilities, "Credit Card", ACCT_TYPE_CREDIT, usd)

    income = make_account(book, root, "Income", ACCT_TYPE_INCOME, usd, True)
    salary = make_account(book, income, "Salary", ACCT_TYPE_INCOME, usd)
    interest = make_account(book, income, "Interest Income", ACCT_TYPE_INCOME, usd)

    expenses = make_account(book, root, "Expenses", ACCT_TYPE_EXPENSE, usd, True)
    groceries = make_account(book, expenses, "Groceries", ACCT_TYPE_EXPENSE, usd)
    rent = make_account(book, expenses, "Rent", ACCT_TYPE_EXPENSE, usd)
    utilities = make_account(book, expenses, "Utilities", ACCT_TYPE_EXPENSE, usd)
    transport = make_account(book, expenses, "Transport", ACCT_TYPE_EXPENSE, usd)

    equity = make_account(book, root, "Equity", ACCT_TYPE_EQUITY, usd, True)
    opening = make_account(book, equity, "Opening Balances", ACCT_TYPE_EQUITY, usd)

    # Money arrives with a plus on the account it lands in and a minus
    # on the account it came from. Income and equity therefore carry
    # negative split values; the checker script shows what that means.
    add_transaction(book, usd, (2026, 1, 1), "Opening balance",
                    [(checking, 300000), (opening, -300000)])
    add_transaction(book, usd, (2026, 1, 5), "Monthly salary",
                    [(checking, 250000), (salary, -250000)])
    add_transaction(book, usd, (2026, 1, 7), "January rent",
                    [(rent, 120000), (checking, -120000)])
    add_transaction(book, usd, (2026, 1, 10), "Groceries on the card",
                    [(groceries, 8540), (card, -8540)])
    add_transaction(book, usd, (2026, 1, 12), "Weekly shop, split three ways",
                    [(groceries, 6025), (utilities, 4510), (transport, 2465),
                     (checking, -13000)])
    add_transaction(book, usd, (2026, 1, 15), "Pay the card off",
                    [(card, 8540), (checking, -8540)])
    add_transaction(book, usd, (2026, 1, 20), "Move money to savings",
                    [(savings, 50000), (checking, -50000)])
    add_transaction(book, usd, (2026, 1, 31), "Savings interest",
                    [(savings, 325), (interest, -325)])

    session.end()
    print(f"Book written to {bookfile}")
    print(f"Accounts in book: {root.n_descendants()}")


if __name__ == "__main__":
    main()
