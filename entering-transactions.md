# Entering Transactions

**Outcome: eight ordinary transactions
are in the book — salary, rent, a card
purchase and its payoff among them — and
each one names both halves.** This is
the daily act of bookkeeping; everything
else is reporting on it.

## The shape of an entry

In the window, you enter a transaction
in a **register** — the ledger page of
one account, most often the checking
account. Each line asks for a date, a
description, a **transfer account** (the
other half), and an amount in the right
column (deposit or withdrawal, receive
or spend — the labels adapt to the
account). Press Enter and GnuCash writes
*both* splits: the one you see and its
mirror in the transfer account.

The transfer account is the whole
discipline. "Withdrawal, $1,200" is a
list entry. "Withdrawal, $1,200,
transfer: Expenses:Rent" is bookkeeping:
the same line now says what the money
was *for*, and the Rent account gains
exactly what Checking lost.

## The lab book's January

The lab entered these eight through the
engine (`create-book.py`, transcript
`t02-create-book.txt`). Read them as the
register would show them; amounts are
dollars.

| Date | Description | From → To | Amount |
|---|---|---|---|
| Jan 1 | Opening balance | Equity:Opening Balances → Checking | 3,000.00 |
| Jan 5 | Monthly salary | Income:Salary → Checking | 2,500.00 |
| Jan 7 | January rent | Checking → Expenses:Rent | 1,200.00 |
| Jan 10 | Groceries on the card | Credit Card → Expenses:Groceries | 85.40 |
| Jan 12 | Weekly shop | Checking → three expense accounts | 130.00 |
| Jan 15 | Pay the card off | Checking → Credit Card | 85.40 |
| Jan 20 | Move money to savings | Checking → Savings | 500.00 |
| Jan 31 | Savings interest | Income:Interest Income → Savings | 3.25 |

Four of these deserve a second look:

**The opening balance (Jan 1).** The
household did not earn its starting
$3,000 in January; it *began* with it.
Its other half is Equity — the "was
already mine" family. Every book starts
with entries like this, one per account
that opens with a balance.

**The card purchase (Jan 10).** No bank
money moved. The groceries were paid for
by a promise, so the split pair is
Groceries +85.40 against Credit Card
−85.40: the expense is real now, the
debt is real now, and the bank is
untouched.

**The payoff (Jan 15).** Checking
−85.40, Credit Card +85.40 — and note
what is *not* here: no expense. Paying
the card is not spending; the spending
happened on Jan 10. Households that
record the payoff as an expense count
every card purchase twice. The card
account returns to exactly $0.00, which
chapter 7 will use as a check.

**Interest (Jan 31).** Three dollars and
change, entered anyway. Small income is
still income, and a book that only
records the round numbers drifts from
the bank's version of the truth by
exactly these amounts.

## Sign conventions, once

The engine stores one signed number per
split: money arriving in an asset
account is positive; money recorded
against income, liability and equity
accounts is stored negative, because
those families sit on the other side of
the equation. The window translates this
into friendly columns and you need never
see it — but chapter 7's proof reads the
engine's own numbers, so the translation
is shown there rather than hidden.

**The check.** After these entries, and
before any proof chapter: Checking holds
3,584.60 (3,000 + 2,500 − 1,200 − 130
− 85.40 − 500). You can do that sum on
paper — that is the point of the design:
the book's arithmetic stays auditable by
a person, and the next chapters audit
it.
