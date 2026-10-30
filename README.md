# GnuCash for Mere Mortals

Most money tracking is a list: money came
in, money went out, and the list is the
whole story. **GnuCash** keeps the same
facts a stricter way. Every payment is
recorded as a movement between two
places — out of this account, into that
one — and the books must balance after
every single entry. That discipline is
called **double-entry bookkeeping**, it
is five centuries old, and it is why a
GnuCash book can *prove* it agrees with
itself instead of merely hoping so.

This guide explains the idea in plain
words first — where money sits, where it
flows, and the one equation that must
always hold — then builds a small
household book for real: an account tree,
eight transactions, one of them split
three ways. Then it checks the book two
independent ways: every leg of every
transaction added up (the total must be
exactly zero), and the accounting
equation balanced to the cent. Both
checks are run by GnuCash's own engine,
not by the guide's arithmetic.

The lab that wrote this guide had no
screen it could click on, so it drove
GnuCash through the program's official
Python bindings — the same engine, the
same file format, the same numbers the
window program computes. The book it
built is an ordinary GnuCash file: the
guide opens it with a database tool and
counts the rows, and runs two of
GnuCash's own reports over it. What the
lab could not do — clicking through the
window, fetching share prices, importing
a bank statement — it did not fake:
those parts are taught from the
documentation and labelled as such
wherever they appear. `criteria.md`
keeps the full ledger.

The household in these pages is invented:
round numbers, generic names, nobody's
real finances. Bookkeeping is private by
nature; the examples keep it that way.

## What this guide covers

- [**What GnuCash is**](what-gnucash-is.md) —
  the mental model: money sits in accounts
  and moves between them, and the equation
  that must always hold
- [**The moving parts**](the-moving-parts.md) —
  the book, the account tree, transactions
  and splits, currencies — and which part
  holds what
- [**Installing GnuCash**](installing-gnucash.md) —
  the packages, the command-line companion,
  and the version check that proves it runs
- [**Your first book**](your-first-book.md) —
  the account tree a household needs, and
  the lab book this guide builds and checks
- [**Entering transactions**](entering-transactions.md) —
  two-legged movements: salary in, rent out,
  a card purchase and its payoff
- [**Split transactions**](split-transactions.md) —
  one payment with several destinations,
  and the imbalance GnuCash refuses to hide
- [**Proving the books balance**](proving-the-books-balance.md) —
  the trial balance and the accounting
  equation, checked against the engine
- [**The book is a database**](the-book-is-a-database.md) —
  the SQLite file opened and counted, the
  XML format, and what to back up
- [**Reports**](reports.md) — the balance
  sheet and income statement, and running
  a report without opening the window
- [**Recipes**](recipes.md) — the monthly
  routine, reconciling against a statement,
  and keeping the book safe
- [**The neighbours**](the-neighbours.md) —
  spreadsheets, the plain-text ledgers, and
  the web bookkeeping apps: what each does
  that GnuCash doesn't, and vice versa
- [**Limits**](limits.md) — one writer at
  a time, no live collaboration, and the
  scripting wart this guide's lab hit
- [**Troubleshooting**](troubleshooting.md) —
  the locked book, the imbalance account,
  and the error messages worth recognising
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Tax preparation and filing — GnuCash can
organise the numbers a tax return needs,
but it is not tax software and this guide
is not tax advice. Payroll, invoicing
workflows for a growing business, and
investment portfolio management are
pointed at, not taught; the guide's
household uses none of them. Connecting
to banks for automatic downloads depends
on your country and your bank, and is
described, not demonstrated.

## How to use this guide

Read chapter 1 slowly — the equation is
the whole subject in one line, and every
later chapter is bookkeeping to keep it
true. Chapters 2 and 3 get you the
program. Chapters 4 to 6 build the book;
chapter 7 proves it. The lab's scripts
live in `gnucash-lab/` with its
transcripts; nothing in them needs a
real household — the invented one is
enough to learn on, and safer.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [SQLite for Mere Mortals](https://paulsullivan33-dev.github.io/sqlite-for-mere-mortals/)
- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)
- [LibreOffice for Mere Mortals](https://paulsullivan33-dev.github.io/libreoffice-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/gnucash-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/gnucash-for-mere-mortals/blob/main/LICENSE-CODE).
