# Your First Book

**Outcome: a book exists with the
account tree a small household needs —
and you have seen that tree built and
counted by the engine, not just drawn in
a picture.** Chapter 4's tree is the one
the rest of the guide spends from.

## The tree

Here is the whole design, the lab book
this guide builds:

```text
Assets                     (placeholder)
  Checking Account         Bank
  Savings Account          Bank
Liabilities                (placeholder)
  Credit Card              Credit Card
Income                     (placeholder)
  Salary                   Income
  Interest Income          Income
Expenses                   (placeholder)
  Groceries                Expense
  Rent                     Expense
  Utilities                Expense
  Transport                Expense
Equity                     (placeholder)
  Opening Balances         Equity
```

Fifteen accounts under a hidden root.
Design notes, in the order they bite:

- **Keep the families.** The five
  top-level placeholders are the
  equation's five terms. Delete one and
  its children have nowhere true to sit.
- **One account per real thing.** A bank
  account in the book for each bank
  account in life; one credit-card
  account per card. When the statement
  arrives, each book account has exactly
  one statement to agree with.
- **Expenses by question, not by shop.**
  "Groceries" and "Transport" answer
  *where does it go?* A "Supermarket"
  account would mix food, cleaning
  supplies and fuel into one number that
  answers nothing.
- **Opening Balances is not optional.**
  The money you already have on day one
  must come *from* somewhere, or the
  equation has a hole in it. It comes
  from Equity — chapter 5's first entry.

In the window, a new book's account
template ("Common Accounts") offers a
superset of this; deleting what you
don't use is easier than inventing the
shape from nothing. Naming the file:
`household.gnucash` is fine, and saving
as SQLite (chapter 8) is the lab's
choice.

## The lab builds it with the engine

The lab had no window, so it built this
exact tree through the bindings —
`gnucash-lab/create-book.py`, which the
next chapters extend with transactions.
The script's running is transcript
`t02-create-book.txt`; it ends:

```text
Book written to .../household.sqlite3
Accounts in book: 15
```

Fifteen: the count the tree above
promises (the book's own root is not
counted). The script creates the book
file in two steps — create, close,
reopen — for a reason worth its own
callout, because script users will meet
it: with a brand-new *SQLite* book, the
engine writes the book's skeleton at
creation time, and in GnuCash 5.5 that
first session then trips over its own
skeleton when asked to store more
("UNIQUE constraint failed: books.guid",
kept verbatim in transcript
`t06-the-sqlite-creation-wart.txt` and
dissected in chapter 13). Closing and
reopening sidesteps it; from the reopen
onward, every change is written to the
database as it is committed, which is
how the SQL format is meant to work.
The XML format does not have this wart.
Window users never see any of it.

**The check.** Open the book (window, or
the checker script of chapter 7) and
count: five families, fifteen accounts,
every balance zero. An empty, balanced
book is the correct starting point —
money enters it only through chapter 5's
door.
