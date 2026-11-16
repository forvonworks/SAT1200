# Handoff — Finish Book 2 (Set 8 + English typeset + vocab page, Lessons 2–23)

You are continuing a commercial SAT Math prep book series for Uzbek students
("SAT 1200+"). Repo: `forvonworks/SAT1200`, branch `claude/tender-planck-dic0r7`
(commit and push only there). Book 2 = 23 lessons in `book2/lesson-NN-*/`.

**Goal:** bring Lessons 2–23 to the same finished state as **Lesson 1** and
**Lesson 7** (both done — use them as your reference). Per lesson that means
three deliverables, built in English:

1. **Set 8** in `problems.md`: 45 original SAT-style multiple-choice problems.
   Lesson 18 is the exception: its last set is Set 6, so its new set is **Set 7**.
2. **`lessonNN-typeset.tex/.pdf`**, rebuilt in English with the new set added.
3. **`vocab-page.tex/.pdf`**, a one-page glossary in Book 1's flat-table style.

**Do NOT merge PDFs** (no `lessonNN-complete.pdf`); the user wants individual
lesson files only for now. Lesson 1 has a merged file from an earlier
experiment; leave it alone.

---

## 1. Current state (as of handoff)

| Lesson | Set 8 in problems.md | Typeset | Vocab | What's left |
|---|---|---|---|---|
| 01 | done | done | done | nothing (reference) |
| 02 | written, **answer key missing** — check all 45 are there | still Uzbek, no Set 8 | no | verify Set 8 + add key, typeset, vocab |
| 03 | done + key | still Uzbek, no Set 8 | no | typeset, vocab |
| 04, 05, 06, 08, 09 | done + key | rewritten in English with Set 8, but **unverified** (interrupted mid-check) | no | compile + visually check every page, fix, vocab |
| 07 | done | done | done | nothing (reference) |
| 10–23 | not started | still Uzbek | no | everything |

The Set 8 answers written so far were checked with sympy by the agents that wrote them.
Spot-check 2–3 per lesson anyway.

---

## 2. Where the materials are

- **Lesson content:** `book2/lesson-NN-*/concepts.md` (topic and scope) and
  `problems.md`. Sets 1–7 in `problems.md` are already in **English**, and that
  file is the source of truth. The old `lessonNN-typeset.tex` files for
  lessons 10–23 are stale **Uzbek** versions of the same sets.
- **Real SAT question bank (for studying methods only):** `Materials/SAT MATH.pdf`
  — one official College Board question per page (with skill, difficulty, answer
  and rationale).
  - Find pages with: `python3 tools/qbank_find.py "<skill substring>" <Easy|Medium|Hard> --limit 4`
    (builds a text cache in `/tmp` on first run, ~1 min).
  - Render a page: `pdftoppm -png -r 150 -f N -l N "Materials/SAT MATH.pdf" /tmp/q`
    then view the PNG. The math is in an embedded font, so text extraction misses
    the numbers; always render the page and read the image.
- **Design references:**
  - `book2/lesson-01-linear-equations-inequalities/lesson01-typeset.tex` — copy its
    whole preamble (colors, macros `\topicheader \pagefooter \colrule \setkicker
    \pnum \satq \satqw \qrbox`, answer-table styling).
  - `book2/lesson-01-.../vocab-page.tex` — copy it as the vocab template.
  - `book2/lesson-07-quadratic-graphs-discriminant/` — second finished example.
- `research/15-question-bank-analysis.md` — background on the bank.

### Lesson → official skill to study

| Lesson | Skill substring for `qbank_find.py` |
|---|---|
| 02 Systems of linear eq. | `Systems of two linear` |
| 03 Linear functions | `Linear functions` (+ `Linear equations in two`) |
| 04 Word-problem translation | `Linear equations in one` + `Linear inequalities` — favor word-problem items |
| 05 Quadratics: factoring | `Nonlinear equations` — factoring only, no formula/completing square |
| 06 Completing square / formula | `Nonlinear equations` — items needing those methods |
| 08 Exponential growth/decay | `Nonlinear functions` — exponential items |
| 09 Polynomial operations | `Equivalent expressions` |
| 10 Rational expressions/equations | `Equivalent expressions` + `Nonlinear equations` (watch extraneous roots) |
| 11 Function notation/composition/transformation | `Nonlinear functions` |
| 12 Nonlinear systems | `Nonlinear equations` — systems subset |
| 13 Ratios, rates, proportions | `Ratios, rates` |
| 14 Percentages | `Percentages` |
| 15 Statistics fundamentals | `One-variable data` |
| 16 Data representations | `Two-variable data` (+ `One-variable data`) |
| 17 Probability | `Probability and conditional` |
| 18 Study design (new set = **Set 7**) | `Evaluating statistical` + `Inference from` |
| 19 Lines, angles, triangles | `Lines, angles` |
| 20 Area & volume | `Area and volume` |
| 21 Circles | `Circles` |
| 22 Right-triangle trig | `Right triangles` |
| 23 Pythagorean / coordinates | `Right triangles` (Pythagorean items) + `Linear equations in two` |

Stay inside the lesson's scope as `concepts.md` defines it (e.g. Lesson 5 must not use the quadratic formula).

---

## 3. Hard rules

- **Copyright:** never reproduce a real College Board question — not its text, its numbers, or its
  context. Study the *method* only, then write a new problem with new numbers,
  names and setting that needs the same solving steps. College Board does not
  license SAT material for commercial use at all, so attribution doesn't make it OK.
- **Verify every answer** programmatically (sympy / `fractions`), and make sure
  exactly one choice is correct and the wrong choices are plausible mistakes.
- **English only** in the typeset and in `problems.md`. Uzbek appears only in the
  vocab page's gloss column.
- **Colors:** purple only — `accent=#602785`, `badge=#B8A0C8`, `ink=#2A2E30`. No red.
  Fonts: Libertinus Serif/Sans/Math. Compile with **xelatex**.
- **Layout safety** (these caused real bugs earlier):
  - Each 2-column page has 238 mm of usable height per column (y = 32 → 270 mm).
    Before you finalize a page, add up the heights of everything in each column.
  - No `\checkmark`, `\xRightarrow`, or other mathtools/amssymb-only commands
    (those packages aren't loaded).
  - Table column widths plus about 14 mm of padding must fit the block width.
  - Any tikz diagram must be drawn to true scale and agree with its own numbers;
    if it can't, make the problem text-only.
  - After compiling, `grep -n "^! \|Overfull" *.log`, then render every page
    (`pdftoppm -png -r 110`) and look at each one. An overfull of about 1–2 mm on
    a table border is fine; anything visible is not.
- **Never run git from parallel agents**; only the main session commits, one
  lesson at a time.

---

## 4. Steps per lesson

### A. Set 8 content (`problems.md`)
1. Read `concepts.md` and `problems.md`.
2. Run `qbank_find.py` for the lesson's skill(s): about 3 pages each for Easy,
   Medium and Hard. Render the pages, read them, and note each item's *method*,
   trap and distractor style.
3. Write 45 problems: **15 Easy, 15 Medium, 15 Hard**, multiple choice (A)–(D).
   Mix equation items, word problems, "what is the value of [expression]"
   shortcuts, parameter / no-solution items, and so on — whatever the real items
   in that skill use.
4. Verify all 45 with a script.
5. Insert before `## Answer Key`, using `## Set 8 — Official SAT-Style Application` with `### Easy / ### Medium / ### Hard`
   subsections (copy the Lesson 1 format), followed by the sourcing note paragraph from
   Lesson 1. Add these three lines to the Answer Key:
   `**Set 8 — Easy:** 1) C  2) …`, `**Set 8 — Medium:** …`, `**Set 8 — Hard:** …`.

### B. Typeset (`lessonNN-typeset.tex`)
1. Rebuild from the Lesson 1 preamble. Keep the lesson's existing
   `\topicheader{N}{English title}` (take the English title from that lesson's
   `rules-sheet.tex`) and keep the original **footer starting number**.
2. Sets 1–7: same layout and spacing as the old Uzbek file (`\pnum` items with
   blank work space), but every label and stem in English, copied from
   `problems.md`. Use "Set N" for the kickers.
3. **Set 8 starts right where Set 7 ends** — normally the right column of the
   Set 7 page — under a short kicker:
   `\setkicker{Set 8}{Real SAT-style problems.}`. No long explanation and no
   separate intro page. Continue on 2-column pages using
   `\setkicker{Set 8 (cont.)}{Choose the correct answer.}`.
4. MC items: use `\satq{n}{stem}{A}{B}{C}{D}` for short choices (2×2 grid), and
   `\satqw` (stacked) for long choices such as coordinate lists or equations.
   Roughly 6 short items or 4 long ones fit in a column.
5. Put the sourcing note (small italic, 8 pt) at the bottom of the last Set 8 page,
   as Lesson 1 does.
6. Answer key: the Sets 1–7 table translated to English, then a separate
   **"Answer Key -- Set 8"** page with Easy/Medium/Hard rows of letters (the title
   textblock goes at y = 30 mm, not 20, or it overlaps the header rule), plus
   the YouTube/Telegram QR placeholders.
7. Number the footers sequentially, then compile, check the log, and render and
   inspect every page.

### C. Vocab page (`vocab-page.tex`)
1. Copy Lesson 1's `vocab-page.tex` and change the topicheader, the footer
   (Lesson 1's page number minus one, i.e. the page just before the rules sheet;
   check `rules-sheet.tex` for the lesson's first page number), and the rows.
2. 15–20 rows, two columns (**English** in bold | **O'zbekcha** in italics). Use
   only terms and phrases that actually appear in that lesson's problems:
   math terms first, then word-problem phrases ("at least", "no more than",
   "combined weight", …). Not a full glossary, and no concept explanations.
3. A flat table only (accent header row, rows alternating with `badge!18`). No
   rounded cards or boxes: an earlier card version overflowed its box. It must
   fit on one page.

### D. Finish
Delete build files (`*.aux *.log missfont.log`, render PNGs — `.gitignore`
already ignores them under `book2/`). Commit **one lesson per commit**, for example
`Book 2 Lesson NN: Set 8, English typeset, vocab page`, then push.

---

## 5. Working efficiently (usage limits)

The previous session hit its usage limit twice by running 20 parallel
agents. Run **at most 3–4 agents at once** (or do lessons sequentially yourself).
Each agent handles exactly one lesson, never runs git, and reports back. Before
you commit a lesson, check it yourself: compile it, look at the page count, and
view the Set 7→8 transition page, the Set 8 answer-key page and the vocab page.

Suggested order: 03 and 02 → 04, 05, 06, 08, 09 (verify only + vocab) → 10–23.
