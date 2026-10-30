# Troubleshooting

**Outcome: the failures a GnuCash user
actually meets — the locked book, the
alarm accounts, a reconcile that won't
close, and the scripting error of
chapter 12 — each with a cause and a
way out.** Kept in the order you are
likely to meet them.

## "GnuCash could not obtain the lock"

**Cause.** A `.LCK` file sits beside the
book (chapter 8). Either the book really
is open in another GnuCash, or a crash
left the lock behind.

**Way out.** If it is open elsewhere,
stop — two writers are exactly what the
lock exists to prevent (chapter 12). If
you are sure nothing has it open (the
machine crashed, the other copy is
closed), choose **Open Anyway**; GnuCash
may offer to replay the session's log
file, which restores entries made after
the last save. Deleting the `.LCK` file
by hand achieves the same and skips the
log offer — prefer the dialogue.

## The Imbalance or Orphan account is not zero

**Cause.** A transaction's legs did not
cancel (Imbalance) or named an account
that no longer exists (Orphan). The
amount shown is the size of the mystery,
and the account's register lists the
offending entries — the alarm comes with
its own evidence.

**Way out.** Open the alarm account,
open each transaction in split view,
and give the stray leg its real account.
It is almost always an entry made in a
hurry. When the last one is fixed the
balance returns to zero; leave the
account itself in place as a standing
alarm.

## Reconcile won't reach zero

**Cause.** The statement and the book
disagree by the amount shown in the
reconcile window's difference.

**Way out.** Work the fingerprints
before re-checking everything: a
difference divisible by 9 points at two
transposed digits (1,290 entered as
1,920 differs by 630); a difference
equal to one of the month's entries
points at a duplicate or a missing line;
a difference equal to a round fee points
at a bank charge never booked — book it,
to a bank-charges expense. Never "fix"
it by editing an old, already-reconciled
entry: that moves the disagreement into
a closed month.

## Balances look wrong by sign in a script

**Cause.** The engine stores credit-side
balances (income, liabilities, equity)
as negative numbers; the window flips
them for display and scripts do not
(chapter 5).

**Way out.** Flip for those three
account types when presenting, as
`check-book.py` does — and never flip
before computing: chapter 7's equation
needs the raw values.

## `UNIQUE constraint failed: books.guid`

**Cause.** The scripting wart of
chapters 4 and 12: in GnuCash 5.5, a
brand-new **SQLite** book created
through the bindings gets its skeleton
written at creation, and storing more in
that same session collides with it
(transcript
`t06-the-sqlite-creation-wart.txt`).
Data entered in the creation session
does not persist; the file holds only
the skeleton (1 book row, 1 account —
the root).

**Way out.** Create the session, end it,
reopen the file normally, and work in
the second session — every commit then
writes as it lands, and no `save()` call
is needed. Or create the book in the
window or in XML format, neither of
which has the wart.

## A report prints accounts at $0.00

**Cause.** Usually the report is doing
exactly what it was told: parent
accounts show $0.00 of their own on some
report settings because their money
lives in their children (the lab's own
reports show this for the family rows),
or the report's date range excludes the
entries.

**Way out.** Check the report's date and
account-depth options before suspecting
the data; then prove the data with
chapter 7's checker, which has no
options to get wrong.

**The check.** Every entry above ends
the same way: the alarm quiet, the
figures agreeing with an independent
source — the statement, the checker, the
raw file. If a fix doesn't end there, it
isn't finished.
