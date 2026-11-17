# Module 1 vs Module 2 — Structure Summary

**Purpose:** a consolidated synthesis of what the research establishes about the Digital
SAT Math section's two-module adaptive structure, and how that structure drove the design
of the Book 3 mock tests and pacing strategy. Draws on `research/01-official-sat-math-spec.md`
(§2–3), `research/02-topic-difficulty-taxonomy.md`, `research/15-question-bank-analysis.md`
(§5), and `book3/lesson-08-mock-tests/pacing-strategy.md`.

---

## 1. The structure (what's fixed vs. what adapts)

The Digital SAT Math section is **two modules**, each **22 questions / 35 minutes**
(70 minutes, 44 questions total). The design is **Multistage Adaptive Testing (MST)** —
*section*-adaptive, not question-by-question adaptive:

| | Module 1 | Module 2 |
|---|---|---|
| **Who sees it** | Everyone, identical form | One of **two** forms — harder-routed or easier-routed |
| **Difficulty** | Fixed, mixed difficulty | Depends on your Module 1 performance |
| **Role** | The gatekeeper / router | The score-determiner |

Module 1 is the same mixed-difficulty set for every test-taker. How you do on it decides
**which Module 2 you're routed into**: a harder-skewed form or an easier-skewed form.

*Source: `research/01` §2, citing College Board's Assessment Framework PDF, cross-checked
against Applerouth, Princeton Review, and Scoir.*

---

## 2. The scoring mechanic — why Module 1 is "the gatekeeper"

This is the heart of the research, and the single structural fact that shaped Book 3's
design:

1. **Module 1 performance → routing.** Both your raw count correct *and* the difficulty of
   what you got right determine whether you're sent to the hard or easy Module 2.
2. **The two Module 2 forms are not equal.** Correct answers on the **harder** Module 2
   earn more scaled-score credit than the same raw count on the easier form — because the
   easier form, by design, cannot support the top of the scale.
3. **The easier route caps your ceiling.** A student routed to the easy Module 2 has their
   section score ceiling capped — estimated **~600–650**, even with a *perfect* Module 2.
   College Board does **not** publish the exact cutoff; every number in this range is a
   third-party estimate and is flagged as such.
4. **Equating** across the two forms is what lets scores be compared fairly across test
   dates.

**The takeaway the books teach directly:** *you must be fast and accurate on
moderate-difficulty Module 1 items to even see the problems that let you score 700+.* This
is a structural fact unique to the digital/adaptive format — it did not exist on the paper
SAT — so the curriculum addresses it head-on rather than assuming it.

---

## 3. The problem this creates for a printed book — and the solution

A book **cannot be adaptive** — it can't change Module 2 in real time based on performance.
The research resolved this deliberately (`research/15` §5 and
`book3/lesson-08-mock-tests/pacing-strategy.md`):

- **Module 1 in each mock** → built at **mixed difficulty** (mostly easy/medium, a few
  hard), mirroring the real average Module 1.
- **Module 2 in each mock** → **fixed as the harder-routed version** — the form a high
  performer would receive. The reasoning: a student aiming for 700–800 *should be practicing
  against the hard route*, because that's the only path to the top of the scale.

### The mock-test difficulty blueprint (per 22-question module)

| | Module 1 (mixed) | Module 2 (harder-routed) |
|---|---|---|
| Easy | ~8 | ~2 |
| Medium | ~11 | ~10 |
| Hard | ~3 | ~10 |

**Held constant across both modules:** domain weight at the official 35/35/15/15 split
(~8 Algebra, ~8 Advanced Math, ~3 PSDA, ~3 Geometry & Trig) and the ~75/25 MCQ/grid-in
ratio. **Only the difficulty mix shifts** between Module 1 and Module 2 — which is exactly
what the real adaptive routing does.

This produces 44 questions/mock × 10 mocks = **440 questions**, drawn from the
5,212-question official Question Bank corpus plus original items written to the same
skill/difficulty/format patterns.

---

## 4. The pacing strategy built on top of it

Lesson 8's pacing sheet (bilingual Uzbek/English) frames Module 1 as
**"darvozabon" (the gatekeeper)** and teaches a within-module time budget that applies to
*both* modules:

- **Q1–15:** ~18 min (~1.2 min each) — move fast, flag anything uncertain.
- **Q16–22:** ~17 min (~2.4 min each) — the hard items cluster at the end.
- **Last 2–3 min:** revisit flagged items, fill every blank grid-in (a blank is a
  guaranteed zero; a guess is not).

It also names the diagnostic rule: *if you can't finish Module 2 in time, that's a **speed**
problem, not a knowledge gap* — tying back to the research's observation (`research/02`,
error-patterns) that rushing easy early questions and running out of time before the hard
Module 2 content are the same root cause (poor time awareness) manifesting differently by
score band.

---

## 5. Sourcing caveats the research is honest about

- The **~600–650 easy-route score cap** is a third-party estimate; College Board doesn't
  publish it.
- The **exact count of unscored/pretest items** inside each 22-question module isn't
  published either — treated as approximate.
- `collegeboard.org` was network-blocked during the research, so official facts were
  reconstructed from search-indexed quotes of College Board's own pages plus the Assessment
  Framework PDF, each cross-checked against at least one independent prep source.

---

**In one sentence:** the research establishes that Module 1 is a fixed router whose
difficulty-weighted result decides whether Module 2 (and thus your score ceiling) is the
hard high-ceiling form or the easy capped form — and the books operationalize that by always
drilling students against the *hard* Module 2 while teaching Module-1 speed-and-accuracy as
the gate to a 700+ score.
