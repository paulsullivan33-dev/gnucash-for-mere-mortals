# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's household is invented, with round numbers.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: one writer at a time, no bank-feed magic, no
   advice or forecasting, the credit-side sign convention, and
   the SQLite creation wart the lab reproduced in the 5.5
   bindings — create, close, reopen — rather than hiding it.
8. **The privacy rule is in the text, early.** Bookkeeping is
   private by nature: the README and chapter 1 state that a
   book is a local file under the reader's control, that no
   account or service is involved, and that every example in
   the guide is an invented household — no real person's
   finances appear anywhere in it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04.5 sandbox with no
display and no permission to install system packages. GnuCash
was therefore obtained as the distribution's own packages —
`gnucash`, `gnucash-common`, `python3-gnucash`, version
**5.5** (1:5.5-1.2build1) — downloaded with `apt-get download`
and unpacked, unmodified, into a lab folder, with the handful
of missing libraries (Guile 3.0, libdbi and its SQLite driver,
libgc) fetched the same way. Because the engine looks for its
modules, data and schemas at compiled-in paths, four temporary
symbolic links bridged those paths into the lab folder while
the lab ran; they were removed when it finished, and the
system itself was never modified otherwise. All transcripts
live in `gnucash-lab/transcripts/`; the scripts are
`gnucash-lab/create-book.py`, `check-book.py` and
`peek-book.py`.

Run for real, with transcripts as evidence:

- Package versions and `gnucash-cli --version` —
  "GnuCash 5.5, Build ID: 5.5+(2023-12-16)" (t00).
- The official Python bindings importing, opening an empty
  session and naming its root account (t01).
- A complete household book built through the bindings: 15
  accounts in the five families, US dollars created as a
  commodity, 8 transactions entered — opening balance, salary,
  rent, a credit-card purchase, a four-leg split transaction,
  the card payoff, a savings transfer, interest — and saved as
  a SQLite database of 212,992 bytes (t02; the creation session's
  `books.guid` error appears in this transcript and is analysed
  in t06).
- The saved book reopened in a fresh session and every balance
  computed by the engine: Checking $3,584.60, Savings $503.25,
  Assets $4,087.85, Credit Card $0.00, Income $2,503.25,
  Expenses $1,415.40, Equity $3,000.00 (t03).
- The trial balance from engine data: 8 transactions, 18
  splits, sum of all splits $0.00; and the accounting equation
  balanced — Assets $4,087.85 = Liabilities $0.00 + Equity
  $3,000.00 + (Income $2,503.25 − Expenses $1,415.40) (t03).
- The book file read with no GnuCash code at all, through
  Python's sqlite3 module: 25 tables; books 1, accounts 16,
  transactions 8, splits 18, commodities 1 rows; per-account
  split totals summed from the raw rows to $0.00 a second time
  (t04).
- Two of GnuCash's own reports run over the book by
  `gnucash-cli`, no window involved: the Balance Sheet (Total
  Assets $4,087.85; Total Liabilities & Equity $4,087.85,
  including the report's own Retained Earnings of $1,087.85)
  and the Income Statement (Total Revenue $2,503.25, Total
  Expenses $1,415.40, Net income $1,087.85) — the HTML output
  is kept at `gnucash-lab/balance-sheet.html` and
  `gnucash-lab/income-statement.html` (t05).
- The SQLite creation wart reproduced in isolation: a
  twelve-line script whose new book ends with only the
  skeleton (1 book row, 1 account) after the verbatim
  `UNIQUE constraint failed: books.guid` errors (t06).
- The XML format created through the same bindings (one
  account, saved in a single session, no wart), identified by
  `file` as gzip data and read with `zcat`: the `gnc-v2`
  header, two `gnc:account` elements, the account names (t07).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything in the window program's interface: the welcome
  flow, the account-template druid, registers and the split
  view, the reconcile window and its marks, Close Book, the
  Reports menu as clicked, and the backup/log file behaviour
  around a working book.
- Importing statements (OFX/QIF/CSV), online banking
  connections, scheduled transactions in use, budgets in use,
  price-quote fetching, and the business features (invoicing,
  customers, payroll-adjacent tools).
- Running GnuCash on a database server, and the neighbour
  tools of chapter 11 (spreadsheets beyond this series' own
  guide, Ledger, hledger, Beancount, Firefly III and the
  hosted services) — characterised, not benchmarked.

Fixtures are this guide's own and deliberately generic: an
invented household, round dollar amounts, generic account and
transaction names, dates in a single invented January. No real
person's finances, accounts or statements appear anywhere.
Amounts are stored by the engine as exact fractions; every
total quoted was produced by GnuCash or summed from its file,
never typed from the guide's own arithmetic — the one sum the
guide does by hand (Checking's running total in chapter 5) is
presented as a reader's check and agrees with the engine.
