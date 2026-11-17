# Handoff 2 — Book 2 follow-up: integrate, re-check Lessons 2–9, fix flagged issues

Read `book2/HANDOFF-finish-book2.md` first. All of its rules still apply (original problems
only and never copy College Board text, verify every answer with a script, English only,
purple palette, layout safety, no merged PDFs, at most 3–4 parallel agents, agents never
run git, one lesson per commit). This file covers only what is new.

## 1. Where things stand

A previous session finished Set 8 (Lesson 18: Set 7), the English typeset and the vocab page
for lessons 10–23. Lessons 1–9 were done in the earlier session. Verify it yourself, because
some of this was written by agents.

- The finished work for lessons 14–23 (and some lesson 12–13 fixes) is on branch
  **`origin/claude/book2-set8-typeset-vnjac3`**. It is about 15 commits ahead of
  `claude/tender-planck-dic0r7`. PR #2 already merged part of it. As a check, on
  `tender-planck-dic0r7` lessons 14–23 still show only 5 typeset pages and no vocab page.
- Commit history for several lessons has a "checkpoint (unverified)" commit followed by a
  verified one. That is acceptable; do not rewrite history. The final tree is what matters.

## 2. Step 0 — set up (do this first)

1. **Merge the work.** Check out `claude/tender-planck-dic0r7`, run
   `git fetch --all`, then `git merge origin/claude/book2-set8-typeset-vnjac3`.
   Resolve conflicts, keeping the newer verified lesson files. Then confirm that
   lessons 14–23 each have 10-ish typeset pages and a `vocab-page.pdf`, and push.
2. **Get the real question bank.** `Materials/SAT MATH.pdf` is stored with Git LFS. On a fresh
   checkout it is a ~130-byte text file starting with `version https://git-lfs...`, not a PDF.
   Fix: `git lfs pull --include="Materials/SAT MATH.pdf"` (about 166 MB). Confirm with
   `pdfinfo "Materials/SAT MATH.pdf"` (it should report roughly 2000 pages). If LFS is blocked,
   say so and stop that part rather than guessing. Do **not** invent "study" of the bank.
3. Use `python3 tools/qbank_find.py "<skill>" <Easy|Medium|Hard>` and
   `pdftoppm -png -r 150 -f N -l N "Materials/SAT MATH.pdf" <out>` as before, and read the
   rendered pages.

## 3. Tasks, in priority order

### A. Re-check Lessons 2–9 against the real bank (the biggest gap)
The earlier agents for lessons 2–9 could not read the bank, so their Set 8s were written
without studying real items. For each lesson 2–9:
1. Look up its skill (table in `HANDOFF-finish-book2.md`), render about 3 real pages per
   difficulty and note the item types, traps and distractor patterns.
2. Compare to the lesson's existing Set 8 (15/15/15). Find missing item types (e.g. "value of
   an expression" shortcuts, no-solution / infinite-solution parameters, equation-selection word
   problems, table/graph-style items) and Hard items that are really Medium difficulty.
3. Replace weak items with new original ones that use the same method. Keep 15/15/15, keep
   `problems.md` and the typeset in sync, verify every answer by script, and recompile and check
   the pages. Only change what needs changing; do not rewrite good items.
4. Confirm each Set 8 still has no real College Board wording or numbers.
Lesson 9: three partial-fraction items were already replaced for being out of scope. Re-confirm
that the rest stays within `concepts.md` (polynomial operations only).

### B. Fix the flagged scope problems
- **Lesson 5**, Set 8 Easy 15: a factorable perfect square close to Lesson 7's discriminant
  topic. Replace it with a plain factoring item (Lesson 5 is factoring only).
- **Lesson 20**, Set 7 item 3 (hemisphere): outside the lesson's four solids. It was in the
  file before this project step. Decide with `concepts.md` in hand: replace it with an in-scope
  solid, and update both `problems.md` and the typeset answer key. Mention the change in your
  report.
- **Lesson 22**, Set 8 Hard 11: it needs the Pythagorean theorem, which that lesson's
  `concepts.md` doesn't mention. Replace it with an item using only what the lesson teaches.
  (Pythagorean is Lesson 23's topic.)

### C. Lesson 16 layout
Its typeset is 14 pages and its Set 8 uses an uppercase "EASY" label and a full-width block.
Rebuild the Set 8 pages to match the other lessons (the Lesson 1 and Lesson 7 pattern): two
columns, `\setkicker{Set 8}{Real SAT-style problems.}` starting where Set 7 ends,
`\satq` / `\satqw` items, "Set 8 (cont.)" kickers, no uppercase labels. Aim for about 10 pages.

### D. Items checked by reasoning, not a script
Lesson 16 has 8 of 45, and Lessons 18 and 19 a few. Try to make them checkable (compute the
statistic, use a counting/probability script, or check the geometry numerically). For anything
that stays conceptual, re-read it carefully and confirm exactly one choice is defensible. List
the residual ones in your report.

### E. Smaller items
- **Lesson 19, Set 3** is text-only because its old diagram was removed. Confirm each Set 3
  problem is still solvable and unambiguous without the figure. If a figure is truly needed,
  draw an accurate to-scale tikz one (see the rules in `HANDOFF-finish-book2.md`); otherwise leave it.
- **Sparse last pages** in several lessons. Tighten only where it's easy (e.g. rebalancing
  columns); don't spend long on it.
- **Footer numbers:** leave the current convention alone (each typeset starts at the same number
  as its rules sheet, and the vocab page is one before). Page numbers will be renumbered when the
  whole book is assembled.

### F. Final QA pass over all 23 lessons (do this last)
Write one script and run it over every `book2/lesson-NN-*/`:
- Compile every `lessonNN-typeset.tex` and `vocab-page.tex` with xelatex and report errors
  and any `Overfull` over 3 pt.
- Report page counts, and confirm each vocab page is exactly 1 page.
- Parse the Set 8 (Lesson 18: Set 7) answer-key letters from `problems.md` and compare them to
  the letters in the typeset answer-key page. Any mismatch is a real bug.
- Confirm each `problems.md` Set 8 has exactly 15 Easy, 15 Medium and 15 Hard items.
- Confirm no leftover Uzbek stem text in any typeset file. Uzbek belongs only in the vocab
  page's gloss column and in the bracketed terms on rules sheets.
Then look at the Set 7 → Set 8 transition page and the Set 8 answer-key page of at least a few
lessons per batch, including every lesson you changed.

## 4. How to work

- Do tasks A–E lesson by lesson. Use at most 3–4 agents at once; each gets one lesson and the
  exact scope above. Agents must not run git. You check the compiled output yourself before
  committing, then make one commit per lesson (`Book 2 Lesson NN: <what changed>`) and push to
  `claude/tender-planck-dic0r7`.
- Do not merge PDFs and do not start Book 3 or other new work.
- Finish with a short report listing, per lesson: items replaced, scope issues fixed, anything
  still unresolved, and the QA script results.
