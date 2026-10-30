# Recipes

**Outcome: a monthly routine that keeps
a book true, a reconciliation method
that ties it to the bank's word, and a
backup habit that can survive losing the
machine.** Bookkeeping is a practice,
not an event; these are its smallest
useful forms.

## The monthly half-hour

Once a month, in this order:

1. Enter everything: salary, bills, card
   purchases (from receipts or the card's
   own list), interest however small.
2. Reconcile the bank accounts (below).
3. Glance at the account tree for the
   two alarm names — Imbalance and
   Orphan — both zero.
4. Run the equation check: this guide's
   `check-book.py` if you use the
   bindings, or a balance sheet in the
   window. Both sides equal, or stop and
   find out why while the month is still
   memorable.
5. Save, close, and let the backup
   (below) take its copy.

## Reconciling against a statement

**Reconciling** is the agreement ritual
between your book and the bank's record,
and it is the strongest check a
household book gets, because the bank is
an independent witness. (The mechanics
are described from the documentation —
the lab's invented household has no
bank — but the numbers it works on are
exactly the verified ones.)

Open the account's reconcile window and
type the statement's closing balance and
date. GnuCash lists the account's
entries; tick each one the statement
also shows. The window keeps a running
*difference* between the statement
balance and the ticked total. At zero,
every entry is agreed by both sides and
reconcile marks them with an `r` (the
register shows `n` for new, `c` for
cleared-by-hand, `r` for reconciled).

A difference that will not die is
diagnosed, not forced: it is usually
one of a transposed pair of digits
(difference divisible by 9 is the
classic fingerprint), an entry in the
wrong month, or a bank charge you never
booked — which is itself an entry the
book was missing. In the lab book's
terms: had January's statement shown
3,584.60 for Checking, the reconcile
would close at zero; any other figure is
a specific, findable disagreement.

Do the credit card the same way, against
its own statement — that is why chapter
4 gives each card its own account. A
card that reconciles to a nonzero book
balance after you paid the statement in
full is telling you a purchase is
missing.

## Backing up the book

- Copy the **folder** (chapter 8): the
  book, its timestamped backups, its log
  files. A nightly copy off the machine
  — external drive, network storage,
  your usual backup tool — is enough.
- Keep GnuCash's own dated backups
  enabled (the default). They are the
  undo for a bad session, which a sync
  copy is not: sync faithfully copies
  your mistake to every location.
- **Test the copy once.** Open the
  backed-up book — GnuCash will warn it
  is already open or locked if the
  original is; work on a third copy if
  in doubt — and run the balance check.
  A backup you have never opened is a
  hope, not a backup.

## Starting a new year

Households often close a year: GnuCash's
**Close Book** tool zeroes income and
expense accounts into equity, so the new
year's reports start clean while assets
and liabilities carry on. Optional —
reports can always be run "for last
year" instead — and irreversible-feeling
enough that the dated backups come
first. (Described, not run: the lab book
has one January in it and nothing to
close.)

**The check.** A book in this rhythm
needs no heroics: every month ends with
the bank agreeing, the alarms silent,
the equation balanced, and a copy
somewhere else.
