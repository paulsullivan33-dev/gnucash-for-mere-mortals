# Split Transactions

**Outcome: you can enter one payment
that lands in several places — and you
know what GnuCash does when the legs do
not add up.** Splits are where
double-entry stops being a slogan and
starts being useful.

## One payment, three destinations

The lab book's January 12 entry, the
weekly shop, paid $130.00 from Checking
and landed in three expense accounts:

```text
Weekly shop, split three ways
  Expenses:Groceries      +60.25
  Expenses:Utilities      +45.10
  Expenses:Transport      +24.65
  Assets:Checking        −130.00
                          ------
  Total                     0.00
```

(The utilities and transport legs are a
top-up bought on the same trip — the
point is the shape, not the shopping.)
Four splits, one transaction, one date,
one description. The rule from chapter 1
still holds, generalised: the legs of a
transaction must sum to **zero** — not
"the ins match the outs" as two columns,
but one signed column that cancels.

Why not three separate entries? Because
the bank saw one payment of $130.00.
Three entries would make the book's
Checking register disagree with the
statement by shape, and reconciling
(chapter 10) would become riddles. The
split keeps the book's view and the
bank's view the same event, while the
expense side still answers *what for*,
three ways.

## Entering one in the window

In a register, the **Split** button (or
the split view of a transaction) opens
the transaction into its legs: one line
per account, each with its own amount.
Type the legs; GnuCash keeps a running
remainder and pre-fills the last leg
with what is needed to cancel out. A
split transaction shows a `-- Split
Transaction --` marker in the simple
view, so it is recognisable at a glance.
(The window mechanics here are described
from the documentation — the lab's split
was entered through the engine, where
the same rule is an assertion in the
script: the legs must sum to zero or the
script refuses to build the transaction
at all. `create-book.py` raises an error
on an unbalanced set before GnuCash ever
sees it.)

## When the legs don't cancel

GnuCash does not silently fix an
unbalanced transaction, and it does not
refuse it either: it books the remainder
to an account it creates for the
purpose, **Imbalance-USD** (and its
cousin **Orphan-USD** for legs whose
account is missing). These accounts are
alarms, not features. A healthy book
keeps both at zero forever; a nonzero
Imbalance balance is the program saying
*one of your entries does not say where
all the money went*, with the amount of
the mystery printed on it. Chapter 13
returns to this. Learn to glance at the
account tree for those two names the way
you glance at a dashboard for warning
lights.

**The check.** In the lab book, the
weekly shop's four legs are in the data:
chapter 8's peek counts all 18 splits in
the book and adds every one of them to
$0.00 — the split transaction included,
cancelling exactly.
