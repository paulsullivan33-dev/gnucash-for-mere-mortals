# Reports

**Outcome: two of GnuCash's own reports
— a balance sheet and an income
statement — are run over the lab book,
from the command line, and their totals
agree with the proofs of chapter 7.**
Reports are the point of the exercise:
the book, summarised into the two
documents anyone — a partner, a bank, an
accountant — actually reads.

## The two that matter

- The **balance sheet** is a photograph
  at one date: what you have, what you
  owe, and the difference, which is your
  net worth in the book's terms. Assets
  on one side; liabilities and equity on
  the other; the two sides equal by
  construction — chapter 1's equation,
  typeset.
- The **income statement** (the window
  also calls its twin Profit & Loss) is
  a film over a period: income in,
  expenses out, and the difference —
  what the period gained or lost.

In the window these live under
**Reports**, and open as pages you can
print or export as HTML. Their options
(which accounts, which date, how deep
the tree is shown) are worth exploring
on a real book; the defaults are sane.

## Running one without the window

`gnucash-cli` runs a report over a book
and writes HTML — the route a script, a
cron job, or a headless machine uses.
The lab ran both reports over
`household.sqlite3` (transcript
`t05-reports-from-the-command-line.txt`):

```bash
gnucash-cli --report run --name "Balance Sheet" \
    household.sqlite3 > balance-sheet.html
gnucash-cli --report run --name "Income Statement" \
    household.sqlite3 > income-statement.html
```

Both exited 0 and wrote real reports —
kept in the lab as
`gnucash-lab/balance-sheet.html` and
`gnucash-lab/income-statement.html`.
Their numbers, with the styling
stripped:

```text
Balance Sheet
  Total Assets                    $4,087.85
  Total Liabilities               $0.00
  Opening Balances                $3,000.00
  Retained Earnings               $1,087.85
  Total Equity                    $4,087.85
  Total Liabilities & Equity      $4,087.85

Income Statement (for 2026 — every entry in the book is dated that January)
  Total Revenue                   $2,503.25
  Total Expenses                  $1,415.40
  Net income for Period           $1,087.85
```

Read the balance sheet's equity section
slowly, because it is the equation
wearing its formal clothes: opening
equity 3,000.00, plus **Retained
Earnings** 1,087.85 — the report's own
name for income-minus-expenses, computed
by the report itself — gives total
equity 4,087.85, which equals total
assets with liabilities at zero. Three
routes through this book (the checker's
two proofs, and now the report) arrive
at the same $4,087.85 and the same
$1,087.85. Agreement between independent
computations is what "the books are
right" actually means.

One wrinkle the lab hit, kept for
honesty: `gnucash-cli`'s `--export-type`
option only serves a handful of reports
with special exporters (charts, tax
schedules). For the standard reports,
leave it off — HTML on standard output
is the export, as above.

**The check.** Open either HTML file in
a browser: a formatted report, your
account names, your totals. Then compare
one figure against chapter 7. They
agree, because there is only one book
underneath all three readings of it.
