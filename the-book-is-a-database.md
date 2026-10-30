# The Book Is a Database

**Outcome: you have seen inside the book
file itself — its tables, its rows, its
numbers adding up without GnuCash
involved — and you know the two formats
a book can take and what to back up.**
A book is not an opaque blob the program
keeps secrets in. It is a document, and
reading it directly is the deepest check
this guide does.

## The SQLite format

Save a book "as SQLite3" and the file is
an ordinary SQLite database:

```text
$ file household.sqlite3
household.sqlite3: SQLite 3.x database, ...
```

`gnucash-lab/peek-book.py` opens it with
nothing but Python's built-in database
module — no GnuCash code at all — and
counts (transcript
`t04-peek-inside-the-book.txt`):

```text
Tables in the book: 25
  books          1 rows
  accounts       16 rows
  transactions   8 rows
  splits         18 rows
  commodities    1 rows
```

Sixteen accounts: the fifteen of chapter
4 plus the book's root. Eight
transactions, eighteen splits — the same
census the engine reported in chapter 7,
counted now by a stranger. The peek goes
further and re-adds the splits from the
raw rows:

```text
Split totals by account (engine sign convention):
  Checking Account     3,584.60
  ...
  TOTAL                    0.00  (must be 0.00)
```

The trial balance, reproduced from the
file's bare rows. (The family accounts —
Assets, Income and friends — do not
appear in that list: placeholders hold
no splits of their own, exactly as
chapter 4 said. Their totals are the
sums of their children.)

The other twenty tables are the rest of
GnuCash's world — budgets, scheduled
transactions, prices, business features
this household doesn't use. They sit
empty in a small book, which is itself a
finding: one format serves the household
and the business without either paying
for the other.

## The XML format

The older format, still the default in
many installs, is XML — and compressed:
the file is gzipped, so text tools need
`zcat` (transcript `t07-the-xml-format.txt`):

```text
$ file sample.gnucash
sample.gnucash: gzip compressed data, ...
$ zcat sample.gnucash | head -8
<?xml version="1.0" encoding="utf-8" ?>
<gnc-v2
     xmlns:gnc="http://www.gnucash.org/XML/gnc"
     ...
```

Under the compression it is readable,
structured text: every account,
transaction and split spelled out in
tags. Either format is the whole book;
the choice is taste and tooling. SQLite
wins for this guide's purposes — queries
like the peek above, and changes written
as they happen. XML wins for diffing in
version control and for reading with
nothing but a text editor and `zcat`.

## Files around the book

A working GnuCash folder grows
companions, and a backup should know
them (described here from the
documentation; the lab's book lived
alone in a scratch folder):

- **`name.LCK`** — the lock file, present
  while the book is open. Its leftover
  after a crash is chapter 13's first
  troubleshooting entry.
- **Timestamped backups** — GnuCash keeps
  dated copies (`name.YYYYMMDDHHMMSS.gnucash`)
  beside the book, a configurable number
  of days deep. These are your undo for
  whole sessions.
- **`.log` files** — a transaction log
  per session, used by the "replay"
  repair route after a crash; normally
  safe to ignore, worth keeping with
  backups anyway.

Back up the folder, not just the file —
chapter 10's recipe says how often and
how to test it.

**The check.** Two strangers — the
engine in chapter 7 and a bare database
reader here — opened the same book and
reported the same census and the same
zero. The file is the book; nothing is
hidden in the program.
