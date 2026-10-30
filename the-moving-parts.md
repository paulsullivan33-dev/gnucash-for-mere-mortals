# The Moving Parts

**Outcome: you can name the five pieces
a book is made of, and say which piece
holds what.** When something later looks
wrong, this chapter is how you name the
problem.

## The book

One **book** is one set of accounts: a
household, or a small business. It lives
in one file. A book holds accounts,
transactions, and a small amount of
bookkeeping about itself (its currency
settings, its creation data). Most
people need exactly one book; a second
one is for a genuinely separate set of
finances, not for a second person in the
same household — people are handled by
separate *accounts*, below.

## Accounts and the tree

An **account** is a place money sits or
flows through: a bank account, a credit
card, "Groceries", "Salary". Accounts
form a **tree**. At the top sit the five
families from the equation — Assets,
Liabilities, Equity, Income, Expenses —
and real accounts nest under them:

```text
Assets
  Checking Account
  Savings Account
Expenses
  Groceries
  Rent
```

Families are usually *placeholder*
accounts: they hold no money themselves,
they group their children, and their
balance is the total of everything under
them. Each account has a **type** (Bank,
Credit Card, Expense, Income, and more),
which tells GnuCash how to treat its
numbers — including which side is "up".
That sign question matters later: money
in an income account is stored as a
negative number by the engine, because
income sits on the opposite side of the
equation from assets. The window hides
this; chapter 7 shows it in the open,
because the proof needs it.

## Transactions and splits

A **transaction** is one movement of
money on one date: "Monthly salary",
"January rent". It is made of **splits**
— the legs. Each split names one
account and one signed amount. A simple
transaction has two splits that cancel;
a complicated one has more (chapter 6).
The transaction also carries the date,
the description, and the **currency**
the amounts are in.

## Commodities and currencies

A currency is one kind of
**commodity** — GnuCash's word for
"a kind of thing an account can hold".
Shares and funds are commodities too,
priced in a currency; a household book
usually meets only currencies. Amounts
are stored as exact fractions (12345/100,
never a rounded decimal float), which is
why GnuCash's totals agree to the cent
with a bank's: there is no rounding
error to accumulate.

## The engine, the window, the file

Three layers, worth keeping apart:

- The **engine** checks every split,
  computes every balance, and owns the
  rules. It is the same engine whoever
  is driving.
- The **window program** (and its
  command-line companion `gnucash-cli`,
  and the scripting bindings) are ways
  of driving the engine.
- The **file** is what the engine saves:
  one book, as gzipped XML or as a
  SQLite database (chapter 8).

**The check.** Look at the account tree
above and the equation in chapter 1, and
match them: the tree's five top-level
families *are* the equation's five
terms. A book is the equation, drawn as
folders.
