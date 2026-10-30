# Limits

**Outcome: you know where GnuCash's
edges are before you lean on them —
who can write, what it won't do, and the
rough corners this guide verified rather
than smoothed over.**

## One writer at a time

A book is locked while it is open. Two
people cannot edit the same book at
once — not in the window, and not
safely over a network share, where the
SQLite format's own locking assumptions
also stop applying. A household book has
one bookkeeper, or takes turns. Tools
built for several simultaneous users
keep their data in a server database
with accounts and permissions; GnuCash
deliberately is not that tool. (Its
database formats can also live on a
real database server in some setups —
documented, rarely worth it at household
scale, and not multi-writer magic even
then.)

## It is not a bank feed

GnuCash can import statements (OFX/QIF,
CSV with a mapping step) and, in some
countries, connect to banks directly —
but it is not a subscription aggregator
that silently gathers every transaction
for you. If your standard is "the app
already knows what I spent", a hosted
service (chapter 11) fits better.
GnuCash's standard is "the book is
right", and it reaches that by ritual
(chapter 10) rather than by feed.

## No advice, thin forecasting

Budgets exist, and scheduled
transactions handle the regular bills,
but GnuCash does not forecast your cash
flow, warn you about next month, or
advise on anything. It is a ledger with
reports, and its honesty about that is
part of its reliability: the numbers it
shows are your numbers, computed plainly.

## Verified rough corners

Things this guide's lab ran into and
kept, because a reader scripting against
the same engine will meet them:

- **The SQLite creation wart (5.5).**
  Creating a new book in the SQLite
  format through the bindings: the
  engine writes the book's skeleton at
  creation, then a `save()` in that same
  session tries to insert the book's row
  again — `UNIQUE constraint failed:
  books.guid` — and data entered in the
  first session does not persist.
  Transcript `t06-the-sqlite-creation-wart.txt`
  reproduces it in twelve lines. The
  workaround is chapter 4's: create,
  close, reopen, then work. The window's
  Save-As flow does not show this; it is
  a scripting-path wart, and the XML
  format does not have it.
- **Error text is terse.** The engine
  reports that failure as low-level SQL
  messages on standard error, and one
  backend exception name
  (`ERR_BACKEND_NO_HANDLER`) that does
  not explain itself. Chapter 13 collects
  the messages worth recognising.
- **Sign conventions are the engine's,
  not yours.** Scripts read credit-side
  balances as negative numbers (chapter
  5). It is consistent and documented
  here, and it surprises everyone once.

## What it will not grow into

Payroll departments, inventory at
scale, multi-currency trading books and
client accounting for other people's
businesses all outgrow GnuCash before
they outgrow its format. The book file
stays readable — chapter 8 read it with
strangers' tools — so leaving is a
migration, not a rescue. That is the
right kind of limit for a tool to have.

**The check.** None of these limits is a
surprise after this chapter: one writer,
imports by ritual, no advice, a wart on
one scripting path — and a file you can
always take with you.
