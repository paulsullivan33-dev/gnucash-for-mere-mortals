# The Neighbours

**Outcome: you can say what the nearby
tools do better and worse, and when a
household should choose one of them
instead.** GnuCash is one answer to
"where does the money go"; it is not the
only shape an answer takes. (These tools
are characterised from their
documentation, not run — the lab
verified GnuCash only.)

## The spreadsheet

A spreadsheet (this series' LibreOffice
guide covers the suite) is where most
household budgets live, and for a simple
list it is genuinely fine: total
freedom, no concepts to learn. Its
weakness is the one this whole guide
exists to answer — a spreadsheet cannot
tell you it is wrong. Delete a row,
mistype a formula, sort half a table,
and the total still prints, smiling.
Double-entry is the discipline a
spreadsheet makes you invent by hand,
one check-sum at a time. If your checks
keep failing in the spreadsheet, you
have outgrown it; if they never fail and
the questions stay simple, you may never
need to leave.

## The plain-text ledgers

**Ledger**, **hledger** and **Beancount**
keep the book as a text file you edit,
and compute reports from it — double-
entry with the same rigour, in a file
you can diff, grep and version. For a
person who lives in a text editor and a
terminal, they are superb, and their
files will outlive any program. What
they ask in return: comfort with the
command line for everything, and no
register window, no reconcile dialogue,
no gentle start. GnuCash is the same
accounting with the machinery worn on
the outside.

## The web bookkeepers

**Firefly III** and similar self-hosted
web apps track budgets, bills and
categories in a browser, with pretty
dashboards and rule-based import. They
are friendlier for pure budgeting —
*what did we spend on eating out* — and
several sync or import from banks more
eagerly. Underneath, most are
single-entry with good manners: they
track flows well, but the balance-sheet
proof of chapter 7 is not their native
language, and net worth becomes a
feature rather than the foundation.
Hosted services (the subscription apps)
add bank feeds and remove the file from
your hands entirely — a fair trade for
some households, and a real one: the
day the service closes, your history is
an export file, if you remembered.

## GnuCash's own position

Local file, exact arithmetic, five
centuries of method, no account, no
subscription, no feed. It asks for the
transfer-account decision on every entry
and gives proof in return. For a
household or a very small business that
wants its books to *check*, that trade
is the subject of this guide.

**The check.** The deciding question is
not features but failure style: when —
not if — an entry is wrong, which tool
tells you, and how loudly? Choose the
one whose answer you trust.
