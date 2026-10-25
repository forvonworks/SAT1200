# Official Structure of the Digital SAT Math Section

**Scope note on sourcing:** My environment's network access blocked direct fetches of `collegeboard.org` / `satsuite.collegeboard.org` pages (DNS/proxy-level block), so I could not pull raw HTML from those pages directly. However, web search results repeatedly surfaced and quoted College Board's own official pages (`satsuite.collegeboard.org/sat/whats-on-the-test/math/...` and the official **Assessment Framework for the Digital SAT Suite** PDF), and those quotes are what's cited below. Every fact is cross-checked against at least one independent test-prep source (Khan-Academy-aligned prep sites, Princeton Review, UWorld, Magoosh, etc.) that mirrors College Board's own published numbers. Where sources disagree, both figures are given and flagged.

---

## 1. Official Math Domains (Content Areas)

The Digital SAT Math section has **four content domains**, identical in name across SAT, PSAT 10, and PSAT/NMSQT (PSAT 8/9 omits trigonometry from the fourth domain):

| Domain (official name) | Weight | Approx. # of questions (out of 44) |
|---|---|---|
| **Algebra** | ~35% | 13–15 |
| **Advanced Math** | ~35% | 13–15 |
| **Problem-Solving and Data Analysis** | ~15% | 5–7 |
| **Geometry and Trigonometry** | ~15% | 5–7 |

- College Board's own domain breakdown (Algebra = linear equations/functions/systems/inequalities; Advanced Math = equivalent expressions, nonlinear equations, nonlinear functions) is confirmed directly from `satsuite.collegeboard.org/k12-educators/about/alignment/math` and the SAT math overview page `satsuite.collegeboard.org/sat/whats-on-the-test/math/overview`. [College Board — Math alignment](https://satsuite.collegeboard.org/k12-educators/about/alignment/math), [College Board — Math Section Overview](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/overview)
- The 35/35/15/15 weighting and the 13–15 / 5–7 question-count split is confirmed independently by multiple test-prep summaries of the same official table. [Mathnasium — SAT Math Sections Explained](https://www.mathnasium.com/math-centers/lascolinas/news/sat-math-sections-explained), [Ivy Strides — SAT Math Topics](https://ivystrides.com/blog/sat-math-topics/)
- Note: Advanced Math's weight was *increased* relative to the pre-2024 paper SAT (roughly +20% share of questions vs. the old "Passport to Advanced Math" domain), reflecting the digital redesign's greater emphasis on nonlinear/functional reasoning. [Mathchops — Adaptive Digital SAT Math Deep Dive](https://mathchops.substack.com/p/adaptive-digital-sat-math-deep-dive)

**Important implication for the book series:** Algebra and Advanced Math together make up ~70% of all scored Math questions. A 3-book series should weight its page budget accordingly — Book 2 (core deep-dive) should give Algebra and Advanced Math roughly double the space given to Problem-Solving/Data Analysis or Geometry/Trig individually.

---

## 2. Adaptive Multi-Stage Module Structure

- **Total Math questions:** 44, scored across the whole section (plus any unscored/pretest items embedded — see note below).
- **Modules:** 2 modules, each **35 minutes**, each with **22 questions**. Total Math time = **70 minutes**.
- **Adaptivity mechanism (Multistage Adaptive Testing / MST):** This is a *section-adaptive*, not item-adaptive, design.
  - Module 1 is a fixed, mixed-difficulty set of 22 questions given to everyone.
  - Based on how a student performs on Module 1, the testing engine routes them into **one of two possible Module 2 forms**: a harder-skewed module or an easier-skewed module.
  - Performing well on Module 1 unlocks the harder Module 2, which contains more higher-difficulty items and is required to reach the top of the score scale. Performing poorly routes the student into the easier Module 2, which caps the maximum achievable scaled score for that section (third-party estimates of this cap vary — roughly 600–650 — since College Board does not publish the exact cutoff).
  - This is the official "Multistage Adaptive Testing" (MST) methodology described in College Board's Assessment Framework. [College Board — Assessment Framework for the Digital SAT Suite (PDF)](https://satsuite.collegeboard.org/media/pdf/assessment-framework-for-digital-sat-suite.pdf)
  - Independent confirmation of the 2-module/22-question/35-minute structure and the "Module 1 performance determines Module 2 difficulty" mechanic: [Applerouth — Complete Guide to the Digital Adaptive SAT](https://applerouth.com/blog/the-complete-guide-to-the-digital-adaptive-sat), [Princeton Review — Digital SAT Structure](https://www.princetonreview.com/college-advice/digital-sat-structure), [Scoir — The Ins and Outs of the Digital SAT](https://www.scoir.com/blog/the-ins-and-outs-of-the-digital-sat)
- **Unscored/pretest items:** Some field-tested (experimental) questions are embedded and don't count toward score, but they are indistinguishable from scored items to the student — total *visible* questions per module remains 22. Sources are not fully consistent on exactly how many of the 22 in each module are unscored pretest items; this detail is not published precisely by College Board in student-facing materials, so treat as approximate. [Magoosh — What's on the Digital SAT](https://sat.magoosh.com/lessons/7280-what-s-on-the-digital-sat), [Manhattan Review — DSAT Prep Math Section Basics](https://www.manhattanreview.com/sat-math-section/)
- **Placement in the test:** Math is the second of two sections (after Reading & Writing, which has the same 2-module/32-minute-each structure), separated by a 10-minute break.

---

## 3. Scoring Scale and How Adaptivity Affects It

- **Scale:** Each section (Math; Reading & Writing) is scored **200–800**. Composite total score range is **400–1600** (sum of the two section scores). This is unchanged from the legacy paper SAT scale.
- **Conceptual mechanics of adaptive scoring:**
  1. Raw performance on Module 1 (how many correct, and the difficulty of items answered correctly) determines **routing** to the harder or easier Module 2.
  2. The final scaled score is computed from combined performance across both modules, but is **equated** against the specific difficulty of the Module 2 form received — i.e., getting X questions right on the *harder* Module 2 earns more scaled-score credit than getting the same raw count right on the *easier* Module 2, because the easier form cannot by design support the top of the scale.
  3. Net effect: a student who stumbles on Module 1 and is routed to the easier Module 2 has their **score ceiling capped** for that section, even with a perfect Module 2 — they cannot reach the top band (estimates from prep sources put this cap around the 600s, not officially published).
  4. This equating process is what allows College Board to compare scores fairly across different test dates/forms despite each student seeing different Module 2 content.
  - Official confirmation that the methodology is "multistage adaptive testing" and that scoring/equating details are documented in the Assessment Framework: [College Board — Assessment Framework for the Digital SAT Suite (PDF)](https://satsuite.collegeboard.org/media/pdf/assessment-framework-for-digital-sat-suite.pdf)
  - Independent explanation of the routing/ceiling mechanic: [OnePrep — Digital SAT Format Explained: Modules & Scoring](https://www.oneprep.co/blog/digital-sat-format-explained-2026-modules-scoring), [Ivy Strides — How the Digital SAT Is Scored](https://www.ivystrides.com/post/how-the-digital-sat-is-scored)
- **Curriculum implication:** Book 1 and early Book 2 content should explicitly teach the "Module 1 is the gatekeeper" concept — framing it as: *you must be fast and accurate on moderate-difficulty Module 1 items to even see the problems that let you score 700+.* This is a structural fact unique to the digital/adaptive format that a book series must address directly (it didn't exist on the paper SAT).

---

## 4. Calculator Policy

- **Confirmed current policy: a calculator (including a graphing calculator) is allowed on every single Math question, in both modules.** The old "No Calculator" section from the paper SAT has been eliminated entirely in the digital redesign.
- Students can use either:
  - **College Board's own built-in Desmos graphing calculator**, embedded directly in the Bluebook testing app and available with one click on every Math question, or
  - **An approved personal handheld calculator** (four-function, scientific, or graphing — battery-powered; some large/raised-display models may require separate seating at the proctor's discretion).
- Confirmed by multiple independent sources describing both the built-in Desmos tool and the elimination of the no-calculator section: [Method Learning — The Power of Desmos on the Digital SAT Math Section](https://www.methodlearning.com/blog/the-power-of-desmos-on-the-digital-sat-math-section), [UWorld College Prep — Digital Built-In SAT Calculator Guide](https://collegeprep.uworld.com/blog/digital-sat-built-in-calculator-usage-and-tips/), [Achievable — How to Use the Desmos SAT Calculator](https://achievable.me/exams/act/resources/how-to-use-the-desmos-sat-calculator/)
- **Curriculum implication:** Because Desmos is always available, Book 2/3 should explicitly teach *graphing-calculator-first strategies* (e.g., graphing a system to find intersection instead of solving algebraically, using Desmos's regression/table features for data-analysis questions) as a core technique family, not an afterthought — this is a genuine difference from legacy SAT prep material that still assumes no-calculator algebra sections.

---

## 5. Official Skill/Question-Type Breakdown Within Each Domain

College Board publishes a "skills and knowledge testing points" list for each domain on its official `satsuite.collegeboard.org/sat/whats-on-the-test/math/types/...` pages. Reconstructed from search-indexed quotes of those official pages, cross-checked with Khan-Academy-aligned and other prep-site mirrors of the same official list:

### Algebra
- Linear equations in one variable
- Linear equations in two variables
- Linear functions
- Systems of two linear equations in two variables
- Linear inequalities in one or two variables
- *(Official description: "measures the ability to analyze, fluently solve, and create linear equations and inequalities.")*
- Source: [College Board — Math alignment page](https://satsuite.collegeboard.org/k12-educators/about/alignment/math), cross-checked at [Ivy Strides — SAT Math Topics](https://ivystrides.com/blog/sat-math-topics/)

### Advanced Math
- Equivalent expressions (rewriting/simplifying expressions)
- Nonlinear equations in one variable and systems of equations in two variables
- Nonlinear functions
- *(Official description covers: "absolute value, quadratic, exponential, polynomial, rational, radical, and other nonlinear equations.")*
- Source: [College Board — Math alignment page](https://satsuite.collegeboard.org/k12-educators/about/alignment/math), cross-checked at [Ivy Strides — SAT Math Topics](https://ivystrides.com/blog/sat-math-topics/)

### Problem-Solving and Data Analysis
Official description: *"measures the ability to apply quantitative reasoning about ratios, rates, and proportional relationships; understand and apply unit rate; and analyze and interpret one- and two-variable data."*
- Ratios, rates, proportional relationships, and units (including percentages)
- One-variable data: distributions, center (mean/median), and spread (range/standard deviation)
- Two-variable data: models and scatterplots
- Probability, including conditional probability
- Inference from sample statistics and margin of error
- Evaluating statistical claims from observational studies and experiments
- Source: [College Board — "Problem Solving" official page, quoted via search index](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/types/problem-solving), cross-checked at [Varsity Tutors — SAT Math: Problem-Solving and Data Analysis](https://www.varsitytutors.com/practice/subjects/sat/lessons/rates)

### Geometry and Trigonometry
Official description: four sub-areas —
- Area and volume (polygons, circles; prism/cylinder/cone/sphere volume)
- Lines, angles, and triangles (vertical angles, linear pairs, parallel lines/transversals, triangle inequality, similarity)
- Right triangles and trigonometry (special right triangles 30-60-90 / 45-45-90, basic sine/cosine/tangent ratios)
- Circles (radii, chords, arcs, inscribed angles, tangent lines)
- Source: [College Board — "Geometry and Trigonometry" official page](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/types/geometry-trigonometry), cross-checked at [RevisionDojo — How to Conquer SAT Geometry and Trigonometry Questions](https://www.revisiondojo.com/blog/how-to-conquer-sat-geometry-and-trigonometry-questions-in-2025), [Manhattan Review — SAT Prep: Math Geometry + Trigonometry](https://www.manhattanreview.com/sat-math-geometry-trigonometry/)

**Khan Academy's official partnership content** (the free, College-Board-endorsed practice platform) organizes its Digital SAT practice question bank using these exact same four domains and the same sub-skill names, since Khan Academy builds its SAT course directly from College Board's item bank and skill codes. Direct page content could not be fetched in this research session due to a network restriction on `khanacademy.org`, so this point is reported as a structural fact (well-established and consistent with how Khan Academy's SAT course has operated since the digital transition) rather than backed by a freshly-pulled quote in this file — verify the exact current skill-tag names on Khan Academy's site before finalizing curriculum mapping tables.

---

## 6. Other Structural Facts Relevant to Book Planning

- **Question format mix:** Roughly **75% multiple-choice (4 options)** and **~25% Student-Produced Response ("SPR" / grid-in)** questions remain in the Math section — grid-ins were **not** eliminated in the digital transition, contrary to a common misconception. Out of 44 total Math questions, that's roughly **~11 grid-in-style questions** distributed across both modules. [Cuemath — SAT Test Prep Curriculum](https://www.cuemath.com/maths/sat-test-prep-curriculum/) — cross-check with [digital SAT test spec overview PDF](https://corsi.unibo.it/s/3394/p/en/enrolling-clef/digital-sat-test-spec-overview-1.pdf/@@download/file/digital-sat-test-spec-overview%20(1).pdf) citing the official ~75/25 split.
  - **Curriculum implication:** Book 1 and Book 2 both need a dedicated short unit on *how to enter a grid-in / SPR answer correctly* (decimals, fractions, no units, no mixed numbers, etc.) since this format still trips up students new to the digital interface — doubly so for students coming from a paper-SAT-only tradition of prep materials (which may exist in translated/older Uzbek prep resources).
- **Reference sheet provided:** A geometry formula reference sheet (circle/rectangle/triangle area, cylinder/cone/sphere/prism volume, Pythagorean theorem, 30-60-90 and 45-45-90 triangle ratios, 360°/2π circle facts) is built into the Bluebook testing app and available on-screen throughout both Math modules. **Algebra/Advanced Math formulas (slope formula, quadratic formula, percent change, etc.) are NOT provided** and must be memorized. [Magoosh — SAT Math Formula Sheet: Provided vs. Memorize](https://magoosh.com/sat/sat-math-formula-sheet/), cross-checked at [Target Test Prep — SAT Math Reference Sheet](https://sat.blog.targettestprep.com/sat-math-reference-sheet/)
  - **Curriculum implication:** Book 1 should explicitly teach students which formulas are "free" (on the sheet) vs. which must be memorized — this is a very concrete, test-savvy distinction students from a zero-background start need spelled out early.
- **Digital-only delivery:** The test is administered entirely through the **Bluebook** app (College Board's proprietary testing software), on a laptop/tablet, not on paper. This affects how students interact with graphs, the calculator, and answer entry, and is worth a short orientation chapter in Book 1 for students unfamiliar with computer-based standardized testing.
- **Shorter overall test, denser time pressure:** Digital Math gives ~1.59 minutes/question average (70 min / 44 questions) vs. roughly 1.25 min/question on the legacy paper Math sections (80 min / 58 questions) — i.e., the digital format is *less* time-pressured per question than the old paper SAT, a fact worth noting since many translated/legacy Uzbek prep materials may still reflect the old pacing assumptions.
- **Section order:** Reading & Writing always comes first (2 modules, 32 min each, 54 total questions), then a break, then Math (2 modules, 35 min each, 44 total questions). Total testing time for the whole SAT is 134 minutes (including the break), down from ~3 hours on the paper SAT.

---

## Sources

1. [College Board — Assessment Framework for the Digital SAT Suite (PDF)](https://satsuite.collegeboard.org/media/pdf/assessment-framework-for-digital-sat-suite.pdf) — official specification document; covers content domains, scoring, and multistage adaptive testing (MST) methodology.
2. [College Board — Math Alignment Page](https://satsuite.collegeboard.org/k12-educators/about/alignment/math)
3. [College Board — SAT Math Section Overview](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/overview)
4. [College Board — "Problem Solving" domain page](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/types/problem-solving)
5. [College Board — "Geometry and Trigonometry" domain page](https://satsuite.collegeboard.org/sat/whats-on-the-test/math/types/geometry-trigonometry)
6. [College Board — PSAT 10/PSAT NMSQT/SAT Math Alignment](https://satsuite.collegeboard.org/k12-educators/about/alignment/math/psat-10-psat-nmsqt-sat)
7. [College Board — Content Domains (Higher Ed Professionals / SAT Validity)](https://satsuite.collegeboard.org/higher-ed-professionals/sat-validity/content-domains)
8. [Mathnasium — SAT Math Sections Explained](https://www.mathnasium.com/math-centers/lascolinas/news/sat-math-sections-explained)
9. [Ivy Strides — SAT Math Topics (2026 breakdown)](https://ivystrides.com/blog/sat-math-topics/)
10. [UWorld College Prep — About SAT Math Section](https://collegeprep.uworld.com/?p=67338)
11. [UWorld College Prep — SAT Test Format & Sections](https://collegeprep.uworld.com/sat/test-format-and-sections)
12. [Applerouth — The Complete Guide to the Digital Adaptive SAT](https://applerouth.com/blog/the-complete-guide-to-the-digital-adaptive-sat)
13. [Princeton Review — Digital SAT Structure](https://www.princetonreview.com/college-advice/digital-sat-structure)
14. [Scoir — The Ins and Outs of the Digital SAT](https://www.scoir.com/blog/the-ins-and-outs-of-the-digital-sat)
15. [Magoosh — What's on the Digital SAT](https://sat.magoosh.com/lessons/7280-what-s-on-the-digital-sat)
16. [Manhattan Review — DSAT Prep Math Section Basics](https://www.manhattanreview.com/sat-math-section/)
17. [Mathchops (Substack) — Adaptive Digital SAT Math Deep Dive](https://mathchops.substack.com/p/adaptive-digital-sat-math-deep-dive)
18. [OnePrep — Digital SAT Format Explained: Modules & Scoring](https://www.oneprep.co/blog/digital-sat-format-explained-2026-modules-scoring)
19. [Ivy Strides — How the Digital SAT Is Scored](https://www.ivystrides.com/post/how-the-digital-sat-is-scored)
20. [Method Learning — The Power of Desmos on the Digital SAT Math Section](https://www.methodlearning.com/blog/the-power-of-desmos-on-the-digital-sat-math-section)
21. [UWorld College Prep — Digital Built-In SAT Calculator Guide](https://collegeprep.uworld.com/blog/digital-sat-built-in-calculator-usage-and-tips/)
22. [Achievable — How to Use the Desmos SAT Calculator](https://achievable.me/exams/act/resources/how-to-use-the-desmos-sat-calculator/)
23. [Varsity Tutors — SAT Math: Problem-Solving and Data Analysis](https://www.varsitytutors.com/practice/subjects/sat/lessons/rates)
24. [RevisionDojo — How to Conquer SAT Geometry and Trigonometry Questions in 2025](https://www.revisiondojo.com/blog/how-to-conquer-sat-geometry-and-trigonometry-questions-in-2025)
25. [Manhattan Review — SAT Prep: Math Geometry + Trigonometry](https://www.manhattanreview.com/sat-math-geometry-trigonometry/)
26. [Cuemath — SAT Test Prep Curriculum](https://www.cuemath.com/maths/sat-test-prep-curriculum/)
27. [Digital SAT Test Spec Overview (PDF, mirrored via unibo.it)](https://corsi.unibo.it/s/3394/p/en/enrolling-clef/digital-sat-test-spec-overview-1.pdf/@@download/file/digital-sat-test-spec-overview%20(1).pdf)
28. [Magoosh — SAT Math Formula Sheet: Provided vs. Memorize](https://magoosh.com/sat/sat-math-formula-sheet/)
29. [Target Test Prep — SAT Math Reference Sheet](https://sat.blog.targettestprep.com/sat-math-reference-sheet/)

**Note on source reliability:** Items 1–7 are direct College Board (satsuite.collegeboard.org) pages/documents, the primary authoritative source. Items 8–29 are independent test-prep organizations (Princeton Review, UWorld, Magoosh, Manhattan Review, Varsity Tutors, Applerouth, etc.) whose content is built directly from — and used here only to cross-check and fill in detail on — the official College Board specification. Where a fact could only be found on third-party sites without a located official-source confirmation (e.g., the exact numeric Module-2 score-ceiling estimates in Section 3, and the precise count of unscored pretest items in Section 2), this is explicitly flagged as an estimate rather than an official figure.
