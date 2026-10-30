# Proving the Books Balance

**Outcome: the lab book is checked two
independent ways — every split in it
added up, and the accounting equation
balanced — using balances computed by
GnuCash's own engine.** This chapter is
the guide's centre of gravity: the
reason for all the discipline before it.

## The checker

`gnucash-lab/check-book.py` opens the
saved book fresh — a new session, nothing
carried in memory from its creation —
and asks the engine for every account's
balance. Then it does two sums of its
own. The full run is transcript
`t03-check-book.txt`; the results:

```text
== Account tree with balances ==
Assets: $4,087.85
  Checking Account: $3,584.60
  Savings Account: $503.25
Liabilities: $0.00
  Credit Card: $0.00
Income: $2,503.25
  Interest Income: $3.25
  Salary: $2,500.00
Expenses: $1,415.40
  Groceries: $145.65
  Rent: $1,200.00
  Transport: $24.65
  Utilities: $45.10
Equity: $3,000.00
  Opening Balances: $3,000.00
```

Every figure is the one the entries of
chapter 5 predict, including the quiet
ones: the credit card at exactly $0.00
(bought 85.40, paid 85.40), and Groceries
at $145.65 — the card purchase of 85.40
*plus* the split shop's 60.25 leg, two
different transactions meeting correctly
in one account.

## Proof one — the trial balance

```text
== Trial balance ==
Transactions in book: 8
Splits in book:       18
Sum of all splits:    $0.00  (must be 0.00)
```

Add up *every leg of every transaction
in the book* — money in as positive,
money out as negative, in the engine's
sign convention (chapter 5). If each
transaction cancels, the grand total
must be zero, and it is: 18 splits, 8
transactions, $0.00. This is the
accountant's **trial balance** in its
purest form. It cannot prove the entries
are *right* — rent booked to Groceries
still cancels — but it proves they are
*complete*: nothing was created or lost
inside the book. Half of all bookkeeping
errors are exactly that kind.

## Proof two — the equation

```text
== The accounting equation ==
Assets:                    $4,087.85
Liabilities:               $0.00
Equity:                    $3,000.00
Income - Expenses:         $2,503.25 - $1,415.40 = $1,087.85
Liabilities + Equity + (Income - Expenses) = $4,087.85
Balanced: True
```

The household has $4,087.85. It owes
nothing. It started with $3,000 of
equity and gained $1,087.85 across
January (2,503.25 in, 1,415.40 out).
3,000 + 1,087.85 = 4,087.85 — the
equation of chapter 1, holding to the
cent on real data, computed from engine
balances.

One sign note, now visible: the checker
prints income, liabilities and equity as
positive amounts by flipping the
engine's stored sign for those families
(the tree reads the way the window shows
it). The equation itself is computed on
the raw values. Both views are in the
transcript; nothing depends on the
reader trusting the flip, because proof
one uses raw values throughout.

## Why two proofs?

They catch different failures. The trial
balance catches arithmetic and
completeness — a missing leg, a mangled
amount. The equation catches structure —
money parked in the wrong family, an
opening balance booked as income. A book
can pass one and fail the other; a book
that passes both, and whose accounts
also agree with the bank's statements
(chapter 10), is a book you can rely on.

**The check.** Rerun it yourself:
`check-book.py` on the lab book prints
the same figures, and — more usefully —
the same script works unchanged on any
book of your own, where the two proofs
are the first thing to run when a number
feels wrong.
