# Installing GnuCash

**Outcome: GnuCash is on the machine,
and two commands prove it runs — the
version check and, on Linux, the
scripting bindings opening an empty
book.** Everything after this chapter
assumes both.

## The ordinary routes

GnuCash is free software, and the
ordinary routes are the right ones:

- **Windows and macOS:** download the
  installer from gnucash.org and run it.
- **Linux:** install your distribution's
  `gnucash` package, or the Flatpak from
  Flathub if you prefer your applications
  boxed.
- **The scripting bindings** (optional,
  used by this guide's lab and by chapter
  9's automation): on Debian and Ubuntu
  they are the separate package
  `python3-gnucash`. On other systems
  they may need a build option; if you
  only ever plan to use the window, skip
  them.

The window program is the whole product
for most readers. Two companions ride
along and are worth meeting now:
`gnucash-cli`, a command-line tool that
can run reports and fetch prices over a
book without opening the window, and the
bindings, which let a Python program
drive the engine directly.

## What this guide's lab did

The lab machine was a shared sandbox
with no permission to install system
packages, so the lab downloaded the
genuine Ubuntu 24.04 packages —
`gnucash`, `gnucash-common` and
`python3-gnucash`, version **5.5** —
unpacked them into a folder of their
own, and ran the real binaries from
there (transcript
`gnucash-lab/transcripts/t00-environment-and-versions.txt`).
Nothing was rebuilt or patched; the
programs are the distribution's own.
Your install will be simpler than the
lab's, and the version check is the
same:

```bash
gnucash-cli --version
```

```text
GnuCash 5.5
Build ID: 5.5+(2023-12-16)
```

And the bindings, where they are
installed:

```bash
python3 -c "from gnucash import Session; \
  s = Session(is_new=True); \
  print(s.book.get_root_account().GetName()); s.end()"
```

```text
Root Account
```

An empty book opens, its root account
answers, and the session closes cleanly
(transcript `t01-python-bindings.txt`).
If the import fails, the bindings are
not installed — the window program is
unaffected, and only the scripting parts
of this guide need them.

## First launch

The window's first run offers a welcome
and a choice: create a new book, open an
existing one, or work through the
tutorial. For a first book, chapter 4's
tree is the shape to aim at; GnuCash's
own "common accounts" template is a
reasonable starting set to edit down.
(The lab had no screen to click, so the
welcome flow itself is described from
the documentation, not demonstrated —
the book it matters for is built and
verified in the next chapter by the
engine instead.)

**The check.** `gnucash-cli --version`
prints a version, and the window opens
to the welcome screen. Both done, the
program is installed in every sense that
matters.
