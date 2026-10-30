# What GnuCash Is

**Outcome: you can say what double-entry
bookkeeping is, in one sentence, and
state the equation every GnuCash book
must satisfy.** Everything else in this
guide is machinery for keeping that
sentence true.

## The one sentence

Every payment is recorded **twice**:
once where the money came from, once
where it went.

That is all double-entry means. Your
salary is not just "+2,500 in the bank".
It is "+2,500 in the bank" *and*
"−2,500 from Salary" — the bank gained
it, and the salary account is where it
came from. Rent is "−1,200 from the
bank" and "+1,200 to Rent". Nothing
appears from nowhere, and nothing
vanishes into nowhere. GnuCash enforces
this: a transaction whose two sides do
not cancel out is not finished, and the
program will park the difference in a
loudly named account (Imbalance) rather
than let it pass quietly.

## The equation

Because every movement cancels out, a
whole book must satisfy one identity at
all times:

```text
Assets = Liabilities + Equity + (Income − Expenses)
```

Read it as a sentence about a household:

- **Assets** — what you have: bank
  balances, savings, things of value.
- **Liabilities** — what you owe: the
  credit card, a loan.
- **Equity** — what was yours before the
  bookkeeping started: opening balances.
- **Income − Expenses** — what this
  period added or took away.

Your possessions equal what you owe,
plus what you started with, plus what
you gained along the way. If that ever
stops being true, a number somewhere is
wrong — and because every entry is
double-sided, the wrongness can be
found. Chapter 7 checks this equation
against a real book and balances it to
the cent.

Accountants dress the same idea in the
words *debit* and *credit*. You can use
GnuCash for years without them — the
program's household view speaks of
deposits, withdrawals, income and
expenses — but the glossary collects
them, because paperwork from banks and
accountants will use them.

## Why bother, for a household?

A list of spending can tell you what
left the bank. It cannot easily tell you
what you owe, what you are worth, or
whether the list itself is complete.
Double-entry answers all three from the
same records, and it catches its own
mistakes: type 1,200 as 120 in one place
and the books stop balancing, which a
single-sided list would never notice.
The price is one extra decision per
payment — *where did it come from, or
where did it go* — and that decision is
usually the interesting question anyway.

## What GnuCash is, concretely

GnuCash is a free, open-source program
(Windows, macOS, Linux) that keeps one
book — one file — per household or small
business. It has kept books since 1998,
it works entirely offline, and its file
is yours: a document on your disk, in
formats chapter 8 opens up and reads.
The window program is how most people
use it. Underneath sits an *engine* —
the part that checks every transaction
and computes every balance — and this
guide's lab drove that engine directly
through its official scripting bindings
to prove the numbers are the engine's
own, not the guide's arithmetic.

**The check.** Before installing
anything, take one payment from your own
life — a salary, a rent payment — and
say both halves out loud: where it came
from, where it went. If you can, you
already understand the system. The rest
of the guide is detail.
