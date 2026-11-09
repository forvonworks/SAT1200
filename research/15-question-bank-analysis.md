# College Board Question Bank Analysis (for Book 3)

**Source material:** the three official College Board Question Bank PDF exports in
`Materials/` (`SAT MATH.pdf`, `PSAT-MNQST & PSAT 10.pdf`, `PSAT 8-9.pdf`). Each page is
one official question with structured metadata: **Question ID, Assessment, Test, Domain,
Skill, Difficulty (Easy/Medium/Hard)**, the question itself, the correct answer, and a
full rationale (including why each wrong choice is wrong, for MCQ items).

**Method:** extracted all three PDFs with `pdftotext -layout`, parsed into structured
records (regex-based, handling pdftotext's column-wrapping quirks — domain/skill/assessment
text interleaves across wrapped lines in a predictable pattern, corrected for). Verified
against known facts before trusting the output: domain counts summed to the full total, the
MCQ/grid-in split matched the officially-published ~75/25 ratio almost exactly, and the
13 Advanced-Math/Algebra skill names and 4 domain names matched `research/01`'s official
list exactly. Full parsed dataset (5,212 records) kept in the session scratchpad for the
writing process, not committed to the repo raw — only aggregate findings and the specific
questions actually selected for the book belong in version control.

---

## 1. What's actually in the bank

| Pool | Total Qs | Easy | Medium | Hard |
|---|---|---|---|---|
| SAT (official, calibrated for SAT) | 1,924 | 684 | 630 | **610** |
| PSAT/NMSQT & PSAT 10 | 1,784 | — | — | 755 |
| PSAT 8/9 | 1,504 | — | — | 881 |
| **Total** | **5,212** | | | **2,246** |

Zero duplicate Question IDs across the three pools — these are 5,212 genuinely distinct
official questions, not overlapping exports.

**Format check (SAT pool):** 1,449 MCQ (A–D) / 475 grid-in = 75.3% / 24.7%, matching the
officially-published ~75/25 split almost exactly — good confirmation the parse is sound.

**Decision for Book 3:** source primarily from the **SAT pool's 610 Hard questions** for
lesson content (this is actual-SAT-calibrated difficulty, not PSAT). PSAT/NMSQT-10 and
PSAT 8/9 Hard pools (755 + 881 = 1,636 more) are kept as a secondary reservoir — real,
official College Board math questions, just calibrated for a younger cohort — useful for
mock-test volume and for topping up thin skill categories, but not the primary source for
"hardest of the hard" teaching examples.

---

## 2. SAT Hard-pool breakdown by official skill (n=610)

| Domain | Skill | Hard Qs |
|---|---|---|
| Advanced Math | Nonlinear functions | 102 |
| Advanced Math | Nonlinear equations in one variable and systems of equations in two variables | 62 |
| Advanced Math | Equivalent expressions | 34 |
| **Advanced Math total** | | **198** |
| Algebra | Systems of two linear equations in two variables | 42 |
| Algebra | Linear equations in two variables | 33 |
| Algebra | Linear functions | 32 |
| Algebra | Linear equations in one variable | 20 |
| Algebra | Linear inequalities in one or two variables | 20 |
| **Algebra total** | | **147** |
| Geometry & Trig | Right triangles and trigonometry | 42 |
| Geometry & Trig | Circles | 41 |
| Geometry & Trig | Area and volume | 36 |
| Geometry & Trig | Lines, angles, and triangles | 33 |
| **Geometry & Trig total** | | **152** |
| PSDA | Percentages | 34 |
| PSDA | One-variable data: distributions and measures of center and spread | 26 |
| PSDA | Ratios, rates, proportional relationships, and units | 19 |
| PSDA | Two-variable data: models and scatterplots | 11 |
| PSDA | Probability and conditional probability | 11 |
| PSDA | Evaluating statistical claims: observational studies and experiments | 7 |
| PSDA | Inference from sample statistics and margin of error | 5 |
| **PSDA total** | | **113** |

The same skill distribution pattern holds (same rank order, same relative proportions)
across all three pools — confirms this is a real, stable signal about where SAT difficulty
concentrates, not an artifact of one export.

**Finding worth flagging:** Geometry & Trigonometry is only 15% of the *overall* test but
contributes **152 of 610 Hard questions (25%)** — proportionally the hardest-skewed domain
in the bank, ahead of Algebra. Yet the current Book 3 TOC (7 lessons) has no dedicated
Geometry/Trig hard-edge-cases lesson — Lesson 1's "unfamiliar framing" lesson is explicitly
scoped to "algebra & advanced math" only. See §4.

**Complexity proxy:** rationale length correlates with tagged difficulty (Hard avg 1,148
chars vs. Medium 851 vs. Easy 679, SAT pool) — not proof of difficulty by itself, but a
useful first-pass filter. The actual "hardest of the hard" selection inside each skill's
Hard pool will be done by reading real candidates (favoring long rationales, multi-concept
stacking, and disguised/unfamiliar framing) rather than by length alone.

---

## 3. Closing the two blank TOC cells

The Annotated TOC (Claude Doc) has two Book 3 lessons with no "Covers" description written
yet. The real data gives a concrete answer for both:

- **Lesson 3 — No-Real-Solution Quadratics & Discriminant Edge Cases:** draws from the
  62-question "Nonlinear equations in one variable and systems of equations in two
  variables" Hard pool — specifically the subset testing the discriminant's role in
  solution-counting (0/1/2 real solutions), complex/no-real-solution cases, and systems
  with a disguised quadratic buried in word-problem or rational-equation framing.
- **Lesson 6 — Data-Analysis Edge Cases & Study-Design Critique (Hard):** draws from the
  60-question combined Hard pool across One-variable data (26), Two-variable data (11),
  Probability (11), and Evaluating statistical claims (7), plus Inference from sample
  statistics (5) — i.e., everything in PSDA's Hard tier that *isn't* Percentages or
  Ratios/Rates (which Book 2 already covers at a lower tier; this lesson is the hard-edge
  extension of Book 2 Lessons 15–18, not a repeat of them).

---

## 4. Open decision: the Geometry/Trig gap

Book 3's 7-lesson TOC has no dedicated Geometry/Trig hard-tier lesson, despite G&T
contributing the single largest proportional share of Hard questions (25% of the Hard
pool vs. 15% of the overall test). Two ways to resolve this:

**Option A (recommended default — proceeding with this unless told otherwise):** don't add
an 8th lesson. The G&T Hard pool (152 real hard SAT questions: right-triangle/trig, circles,
area/volume, lines/angles/triangles) feeds the **mock tests** at real proportional weight
instead of getting its own concept lesson — consistent with the observation that G&T's hard
questions tend to be *harder applications of Book 2's existing formulas* (a right-triangle
trig question tangled with a circle, a composite-volume problem with an algebraic twist)
rather than genuinely new conceptual edge cases the way discriminant-sign-counting or
study-design critique are. The "unfamiliar framing" skill taught in Lesson 1 (even though
scoped to algebra/advanced math in its description) transfers directly to G&T's hard
questions too, so students aren't left without a strategy for them.

**Option B:** add an 8th lesson, "Geometry & Trigonometry — Hard Applications," to give this
pool the same dedicated treatment as Lessons 3 and 6.

Flagged to the user; proceeding on Option A unless redirected.

---

## 5. Mock test blueprint (10 full-length mocks, Book 3 closer)

Per the user's direction: each mock has a Module 1 and Module 2, matching the real Digital
SAT's shape, but **not adaptive** (a book can't branch) — Module 1 is fixed at an
easier/mixed difficulty, Module 2 is fixed at the harder-routed difficulty (simulating the
path a student aiming for a top score should be practicing against, per `research/01` §3's
routing mechanic).

**Per module (22 questions, 35 min, matching official structure):**

| | Module 1 (mixed) | Module 2 (harder-routed) |
|---|---|---|
| Easy | ~8 | ~2 |
| Medium | ~11 | ~10 |
| Hard | ~3 | ~10 |

**Domain weight per module (matching the official 35/35/15/15 split, ~8/8/3/3 of 22):**
Algebra ~8, Advanced Math ~8, PSDA ~3, Geometry & Trig ~3 — held constant across both
modules; only the difficulty mix shifts between Module 1 and Module 2.

**Format mix per module:** ~16–17 MCQ (4-choice) / ~5–6 grid-in, matching the confirmed
75/25 real-test ratio.

**Per mock test:** 44 questions total (22 + 22) → **440 questions across 10 mocks.**

**Sourcing policy (per the user's explicit instruction):** a deliberate mix of (a) real
official College Board questions pulled verbatim from the 5,212-question corpus (favoring
the SAT pool first, PSAT pools as secondary inventory to avoid over-reusing the same SAT
questions across multiple mocks) and (b) originally-written questions matched to the same
difficulty/skill/format patterns observed in the real data — not just copied from source,
and not flagged or distinguished in the book which is which. With 5,212 real questions
available and only 440 slots needed across all 10 mocks, repetition of the same real
question across mocks can be kept low by design.

**Process note:** building the actual mocks means (1) selecting real question IDs per
module/domain/difficulty/skill slot from the parsed corpus, reading each one's full text +
rationale to confirm it's genuinely well-formed standalone (a few bank entries reference a
graph/figure the text extraction can't capture — those get described in words, the same
approach used throughout Book 2's geometry lessons, or swapped for a text-only equivalent),
(2) writing original questions to fill the remaining slots in the same style, (3) a full
answer key + rationale for every question, book-authored in the same bilingual
concept-explanation style as Books 1–2 where a rationale teaches something, not just
confirms an answer.

---

## 6. Book 3 lesson-writing implication

Lessons 1, 3, 4, and 6 (and the mock tests) now have a **real, data-grounded basis**
instead of a guessed one: specific skill names, specific real-question counts to draw
teaching examples from, and a specific complexity-ranking method (rationale length as a
first filter, manual reading for final "hardest of hard" selection) rather than writing
Book 3 from general impressions of "what's probably hard."
