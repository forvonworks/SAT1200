# Book 3 spec — "SAT 1200+ · Book 3 · ≈800 · Master SAT TRICKS for a Perfect Score"

Decisions made by the owner (do not re-litigate):

- English-only content (as Book 2). Uzbek only in bracketed terms on rules sheets, in the small
  "New words" card, and on front/back matter.
- Palette: **pine green** only. `accent #0F6A52`, `badge #A9CFC2` (tints), `ink #2A2E30`. No red.
  Cover = green background, white text.
- Cover wording: "SATmath ≈800" (not 700+) and "MASTER SAT TRICKS FOR PERFECT SCORE"
  (not "Complete guide book").
- **9 lessons** (no bonus logs/unit-circle lesson), then **10 full mock tests**, then one
  **Answer sheets** section at the very end of the book (no answers printed right after a mock).
- **Vocabulary:** no big vocab page. Each lesson ends its rules sheet with a small
  **"New words" card of 10–15 terms** (English | O'zbekcha) that continue the lesson's concepts/formulas.
- **5 problem sets per lesson**, ~70–80 problems total per lesson, all Medium→Hard.
  Set 1 bridge (Medium/Hard), Sets 2–4 Hard by sub-skill, Set 5 "Summit" = ~20 hardest SAT-style
  mixed problems for the lesson. Mix of 4-choice MC and student-produced (grid-in) answers.
- After the last set: a **Qaydlar uchun** notes page (copy Book 2's `notes-lesson-template.tex`
  recolored), then the **Answer Key** with a short worked solution for *every* problem
  (1–3 lines each). Thin hard-problem explanations are the #1 complaint about competitors.
- Every problem original. Study real College Board Question Bank items for the *method* and the
  *wrong-answer traps*, never copy their wording, context or numbers. Verify every answer by script.

## Lessons (new numbering)

| # | Lesson | Source/notes |
|---|---|---|
| 1 | Disguised & multi-step word problems | old `lesson-01-disguised-word-problems` |
| 2 | Hard linear equations, systems & parameters | **new** (no/one/infinite solutions, models in context) |
| 3 | Hard nonlinear functions (vertex, optimization, exponential models, composition & transformation) | merge old lesson 2 + new content |
| 4 | Discriminant edge cases & disguised quadratics | old lesson 3 |
| 5 | **Speed tricks** (Vieta, "don't solve", backsolving, graph-it, factor/remainder, structure) | old lesson 4 + Desmos tricks |
| 6 | Hard percentages, ratios & units | **new** |
| 7 | Data-analysis edge cases | old lesson 6 |
| 8 | Hard circles, area & volume | **new**, split from old lesson 7 |
| 9 | Hard right triangles & chained geometry | old lesson 7 |

Hard-pool weights from `research/15-question-bank-analysis.md` (610 SAT Hard items):
Nonlinear functions 102, nonlinear equations/systems 62, equivalent expressions 34,
linear systems 42, linear equations in 2 vars 33, linear functions 32, linear eq 1 var 20,
linear inequalities 20, right triangles/trig 42, circles 41, area/volume 36, lines/angles/triangles 33,
percentages 34, one-variable data 26, ratios/rates/units 19, two-variable data 11, probability 11,
statistical claims 7, inference/margin of error 5.

## Mock tests (10) — blueprint

Research basis (third-party, estimates — College Board publishes no per-form counts): each Math
section = 2 modules x 22 questions x 35 min; Module 1 has a mix of easy/medium/hard and decides
Module 2; the **harder** Module 2 has far more hard items; the easier Module 2 caps the score.
Within a module items run roughly easy → hard. ~25% are grid-ins (about 5–6 per module).
Domain split: Algebra ~35%, Advanced Math ~35%, Problem-Solving & Data Analysis ~15%,
Geometry & Trigonometry ~15%.

Book 3 is for students chasing ≈800, so every mock gives the **Module 1 (standard mix)** and the
**Module 2 (harder route)**. FINAL blueprint per mock (owner-approved, supersedes earlier numbers):

| | Easy | Medium | Hard | Grid-ins | Algebra | Adv. Math | PSDA | G&T |
|---|---|---|---|---|---|---|---|---|
| Module 1 (22) | 8 (Q1–8) | 11 (Q9–19) | 3 (Q20–22) | 5–6 | 8 | 8 | 3 | 3 |
| Module 2 hard (22) | 2 (Q1–2) | 10 (Q3–12) | 10 (Q13–22) | 5–6 | 8 | 8 | 3 | 3 |

Both modules: ~75/25 MC/grid-in. Only the difficulty mix shifts between modules, as in the real
adaptive routing. Mock 1 was built with an earlier blueprint and is being re-balanced to this one.
Pacing advice for the mock intro: Q1–15 about 18 min, Q16–22 about 17 min, last 2–3 minutes for flagged
items and every blank grid-in (blank = guaranteed zero).

Module 2 must *feel* clearly harder than Module 1: multi-step, disguised, two skills chained, traps in
the distractors, setup errors that cost the point. Q1–3 of Module 2 are still medium-ish, Q10–22 are
genuinely 700–800-level. A module-2 item that a Module-1 student could do in 30 seconds is a defect.

Answers are NOT printed after the module. They go to the end-of-book "Answer sheets" section
(per mock: table of answers for M1 and M2 with domain + difficulty tag for each question).

## Layout (copy Book 2's machinery, recolor)

- Preamble/macros: copy from `book2/lesson-01-linear-equations-inequalities/lesson01-typeset.tex`
  (`\topicheader \pagefooter \colrule \setkicker \pnum \satq \satqw`) and from
  `book2/*/rules-sheet.tex` (`\topicheader \pagekicker \videobanner \pagefooter \cardbg \pill`).
  Replace colors: `accent 0F6A52`, `badge A9CFC2`. Read `book2/RULES-SHEET-SPEC.md` for the 8 layout
  safety rules (card height vs content, tikz bounding boxes, table widths, header cells with
  `\cellcolor` + `\textcolor{white}`, true-scale diagrams only, etc.).
- Rules sheet: pill title + formula + at most one bare example per card, a "WATCH THE VIDEO BEFORE YOU
  SOLVE" banner with QR placeholder on page 1, and a final **"New words"** card (10–15 rows).
- XeLaTeX, Libertinus fonts. A4, textpos absolute layout. Footer page numbers: just number pages from
  the first page of your deliverable (renumbered at book assembly).
- Never run git. Do not touch files outside your assigned folder (except reading).
- Question-bank study: `Materials/SAT MATH.pdf` (2030 pages, one official question per page; the file is
  present). `python3 tools/qbank_find.py "<skill>" <Easy|Medium|Hard> --limit 4`, then render with
  `pdftoppm -png -r 150 -f N -l N "Materials/SAT MATH.pdf" /tmp/q` and read the image (numbers are in an
  embedded font; text extraction misses them).

## Repo layout (Book 3)

- `book3/lesson-NN-<slug>/` — new lessons (problems.md, verify.py, rules-sheet.*, lessonNN-typeset.*, notes-page.*)
- `book3/mocks/mock-NN/` — mocks (mockNN-problems.md, verify.py, mockNN-typeset.*, mockNN-answer-sheet.*)
- `book3/old-drafts/` — old Uzbek/English-mix drafts, INPUT ONLY (ideas), never copy real College Board text
- Reference implementations: `book3/lesson-05-speed-tricks/` (lesson), `book3/mocks/mock-01/` (mock)
- Mocks must not repeat contexts, numbers or problem ideas of other mocks (read the other mocks' problems.md first).

## Worked-solutions spacing (owner requirement)

The answer-key worked-solutions pages must be comfortably spaced (10 pt text, ~3.6 mm between items, two
auto-flowing columns, no item split across columns). After building any lesson typeset, run
`python3 book3/tools/respace_solutions.py lessonNN-typeset.tex` (idempotent) and recompile; it rewrites those pages
with multicol + fancyhdr and a `\pgoff` macro for the footer number (footer = page + \pgoff).
