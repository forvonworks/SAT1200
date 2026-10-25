# Common Student Mistakes on SAT Math — Research Notes

**Purpose:** This document catalogs recurring, specific error patterns that SAT-takers make, organized by topic area, for use in designing worked examples, "watch out" callouts, and practice-question distractors across the 3-book series. Where a claim traces to a specific named source, it is cited. Where a pattern is repeated across many commercial/tutoring sources without a single authoritative citation, it is flagged as **(consensus/folklore)** — true in the sense that nearly every tutoring company independently reports it, but not backed by a single rigorous study.

A general caveat that applies throughout: almost none of this is based on College Board's own released error-rate data (which isn't public at the item level). Most sources are test-prep companies, tutoring blogs, teacher-authored state curriculum notes, and a handful of academic studies on algebra misconceptions generally (not SAT-specific). Academic studies are noted explicitly where used.

---

## Linear Equations

- **Sign error when distributing a negative across parentheses** — e.g., `-(x - 4)` simplified incorrectly to `-x - 4` instead of `-x + 4`. Flagged as the single most common trap in multiple sources. *Why it happens:* procedural/careless — students mechanically "distribute the negative" to the first term and forget it, or treat `-(a - b)` as `-a - b` rather than `-a + b`. [Brilliant SAT Algebraic Manipulations](https://brilliant.org/wiki/sat-algebraic-manipulations), [Axiom Academy SAT traps](https://theaxiomacademy.org/learn/sat-common-traps-avoid), [Mathnasium common algebra mistakes](https://www.mathnasium.com/math-centers/lakewoodco/news/common-algebra-mistakes)
- **Sign flip errors when moving terms across the equals sign** — forgetting to flip the sign of a term when moving it to the other side. (consensus/folklore, repeated across tutoring sources) [Varsity Tutors](https://www.varsitytutors.com/practice/subjects/tachs-math/quiz/one-variable-linear-equations)
- **Treating subtraction of a negative as subtraction of a positive** — e.g., computing `4 - (-2)` as `2` instead of `6`. [Mathnasium](https://www.mathnasium.com/math-centers/lakewoodco/news/common-algebra-mistakes)
- **Inconsistent balancing of the equation** — performing an operation on one side only, or applying it to only part of one side. Noted in a Texas Algebra I state curriculum guide as a recurring error type. [Lead4ward Algebra I QSG](https://account.lead4ward.com/docs/conferences/review23/resources/math/1_m_alg1_linear_functions_qsg.pdf)
- **Solving for the wrong variable/expression** — solving correctly for `x` when the question asks for `8x` (or `2x + 1`, etc.) and bubbling in the value of `x` itself. This is one of the most frequently cited "trap answer" mechanisms across all topics, not just linear equations. *Why it happens:* reading/attention — students stop as soon as they reach a familiar-looking number, not because they lack the math skill. [PrepScholar forum discussion](https://experthub.prepscholar.com/t/preventing-careless-errors-on-sat-math/7572)
- **Fix commonly recommended:** rewrite the negative-distributed expression explicitly as a separate step before simplifying further, and substitute the final answer back into the *original* equation (not an intermediate line) to catch sign errors. [Mathnasium](https://www.mathnasium.com/math-centers/lakewoodco/news/common-algebra-mistakes)

---

## Systems of Equations

- **Arithmetic/sign slips during elimination** — adding or subtracting equations incorrectly, especially when a row must first be multiplied by a negative constant to align coefficients. (consensus/folklore) [Varsity Tutors Systems of Equations](https://internal.varsitytutors.com/practice/subjects/sat-math/help/systems-of-equations)
- **Substituting the wrong value back in** — solving for one variable correctly, then plugging it into the wrong original equation or into the expression the question actually asks about.
- **Choosing substitution vs. elimination poorly** — picking a method that creates fractions or more arithmetic than necessary, increasing the chance of a careless error and costing time. [OneQuery: Why Students Get Stuck on SAT Algebra](https://www.oneprep.co/blog/why-students-get-stuck-on-sat-algebra)
- **Assuming every system has exactly one solution** — missing the "no solution" (parallel lines, same slope/different intercept) and "infinite solutions" (identical lines) cases, which the digital SAT tests explicitly via questions like "for what value of k does this system have no solutions." *Why it happens:* conceptual — students learn systems as "solve for x and y" and don't build a mental model of what a solution geometrically represents.
- **Weak translation from word problems into two equations** — especially mixture, cost, and rate scenarios; some students write only one correct equation and guess at or botch the second. [OneQuery: Avoid SAT Algebra Mistakes](https://www.oneprep.co/blog/avoid-sat-algebra-mistakes)
- **Misunderstanding what counts as "a solution"** — an academic study of 13–14-year-olds (Spain) found errors in interpreting what a solution to a system represents both graphically (intersection point) and algebraically, and in understanding *why* elimination is a valid operation (adding equal quantities to both sides) rather than just a memorized trick. This is a genuine conceptual gap, not a careless error, and likely transfers to SAT-takers who were taught the procedure without the reasoning behind it. [Study hosted at portalinvestigacion.uniovi.es](https://portalinvestigacion.uniovi.es/documentos/6369acd069e22d1dfe08940a)

---

## Quadratics & Functions

- **Not checking for extraneous solutions in radical equations** — squaring both sides of `√(2x+15) = x` produces two algebraic candidates, but only one satisfies the *original* equation; squaring is not a reversible operation and can introduce false roots. The digital SAT's principal-square-root convention (√ always denotes the non-negative root) is exactly why the negative candidate gets rejected. *Fix:* always substitute every candidate back into the original (unsquared) equation. [Open Exam Prep: Radical Equations & Extraneous Solutions](https://open-exam-prep.com/study-guides/sat-math/advanced-math-quadratics/radical-equations-extraneous)
- **Sign and arithmetic errors inside the quadratic formula** — especially losing track of the negative on `-b`, or arithmetic slips computing the discriminant `b² - 4ac`. One tutoring source bluntly states most lost points come not from forgetting the formula but from *misapplying* it. [Ivy Strides: Quadratic Formula Mistakes](https://www.ivystrides.com/post/quadratic-formula-mistakes)
- **Stopping after finding one root** — quadratics have (up to) two solutions; students solve one factor/root and move on without checking the second, especially under time pressure.
- **Choosing an endpoint instead of the vertex in optimization problems** — e.g., "maximum height" or "minimum cost" questions where students evaluate the function at a boundary x-value instead of finding and evaluating at the vertex.
- **Function notation errors (`f(x)` family):**
  - Reading `f(x)` as "f times x" rather than "f evaluated at x" — a genuine conceptual misread of notation. (consensus/folklore, repeated across ACT/SAT/classroom sources)
  - Dropping parentheses when substituting a negative number, e.g. computing `3 · -2²` instead of `3(-2)²`, which silently flips a sign (`-12` vs. `12`).
  - Confusing `f(x + a)` (shift the *input*) with `f(x) + a` (shift the *output*) — these produce different graphs/values and is a common conceptual confusion in transformation questions.
  - Reversing the order of composition, mixing up `f(g(x))` with `g(f(x))`.
  - Partial substitution — e.g., given `f(x) = x²` and asked for `f(2a)`, squaring the `a` but forgetting to square the `2`.
  [General pattern described across ACT/SAT/classroom sources; no single SAT-specific frequency study found]

---

## Exponents & Radicals

- **Multiplying exponents when the rule requires adding them** (and vice versa) — confusing `aᵖ · aᵖ` (add exponents) with `(aᵖ)ᵖ` (multiply exponents). [Albert.io Digital SAT Math](https://www.albert.io/blog/?p=117731)
- **Treating a negative exponent as if it made the base negative** rather than as "take the reciprocal" — e.g., thinking `2⁻³ = -8` instead of `1/8`.
- **Splitting the square root of a sum into a sum of square roots** — the classic `√(a+b) ≠ √a + √b` error, which students apply despite it being false for all nonzero a, b. [Albert.io](https://www.albert.io/blog/?p=117731)
- **Multiplying everything under and outside a radical instead of factoring the radicand properly** when simplifying — e.g., mishandling `√(18)` by not pulling out the largest perfect-square factor. [Virginia DOE radicals teacher notes](https://www.doe.virginia.gov/home/showpublisheddocument/65313/638972408728370000)
- **Incomplete simplification of the radicand** — missing a hidden perfect-square or perfect-cube factor, especially inside higher-order roots (cube roots, fourth roots).
- **Confusing the index of the root** — taking a square root when the problem specifies a cube or fourth root, or only applying the root to part of the radicand.
- **Misreading rational exponents as division** — e.g., writing `81^(1/4) = 4.5` (treating the exponent as "divide by 4") instead of correctly computing the fourth root of 81 = 3. One study of this pattern found it reflects a weak grasp of what a root fundamentally *means*, not just a procedural slip — i.e., it's conceptual, not careless. [Cazoom Maths](https://www.cazoommaths.com/us/math-worksheets/algebra-2-indices-worksheets/)
- **Forgetting `√(x²) = |x|`, not `x`** — a frequently-cited trap, since it matters whenever x could be negative (e.g., solving `x² = 16` and reporting only `x = 4`).
- **Research note:** A 2016 study of college students found they performed *better* on radical-form problems than on equivalent rational-exponent-form problems, and that students who solved radical problems correctly most often used factor-tree methods — suggesting rational exponent notation itself is a harder conceptual hurdle than radicals, worth extra drilling. [cited via SUNY repository search result]
- **Practical fix commonly recommended:** when exponent/radical algebra gets messy, plug in a clean test number (4, 16, 8, 27) and check which answer choice matches numerically, rather than manipulating symbols under time pressure. [Albert.io](https://www.albert.io/blog/?p=117731)

---

## Ratios, Percentages & Proportions

- **Confusing a part-to-part ratio with a part-to-whole fraction** — e.g., reading a 3:2 ratio as the fraction 3/2 of the total, when the total is actually 5 parts, so the correct fraction is 3/5. (consensus/folklore, repeated across several tutoring sources, e.g. [CA Foundation Ratio & Proportion mistakes](https://catestseries.org/blogs/ca-foundation-ratio-and-proportion-common-mistakes-and-corrections))
- **Flipping the order of terms in a proportion** — e.g., setting up boys/girls on one side and girls/boys on the other. *Fix commonly suggested:* label each ratio explicitly and keep the same order on both sides.
- **Dividing by the new value instead of the original value when computing percent change** — percent change must always use the original (starting) quantity as the denominator; dividing by the new value is one of the most common percent errors cited.
- **Forgetting to convert a percent to a decimal before using it in a calculation** — multiplying by 25 instead of 0.25, making the answer 100× too large (or too small, depending on direction). This is listed repeatedly as one of the single most common "silly" SAT percent errors.
- **Mismatched units within a proportion** — putting different units in the numerator on one side versus the other, breaking the proportion's validity.
- **Cross-multiplying incorrectly** — multiplying numerator×numerator and denominator×denominator instead of the correct cross-product (numerator₁×denominator₂ = numerator₂×denominator₁).
- **Forgetting that ratios/ages shift over time in "years from now" problems** — treating a current ratio as fixed when the problem involves elapsed time, requiring the equation to add the same number of years to both quantities before applying the ratio.
- **Why these happen:** mostly procedural/setup mistakes rather than not knowing what a percent or ratio "is" — but the ratio part-to-part/part-to-whole confusion in particular reflects a genuine conceptual gap in what the numbers in a ratio actually represent.

---

## Statistics & Data Analysis

- **Averaging two averages instead of recombining the underlying groups** — e.g., given the mean of group A and the mean of group B, incorrectly averaging those two means together instead of computing total-sum ÷ total-count across the combined group (this only gives the right answer when the two groups are the same size). [PrepScholar: Statistics on SAT Math](https://blog.prepscholar.com/statistics-on-sat-math-strategies-for-mean-median-and-mode) — note: this source itself contains a worked-example arithmetic error (381/5 computed as 76.2 but stated as 72.6), underscoring how easy these calculation errors are to make even when writing instructional material.
- **Forgetting to sort data before finding the median** — especially with messy, non-ordered data sets or frequency tables.
- **Miscounting the middle position**, especially off-by-one errors in larger data sets.
- **Forgetting the even-count rule for the median** — with an even number of data points, the median is the *average of the two middle values*, not either one alone.
- **Not tracking how mean/median/mode change when a value is added, removed, or changed** — SAT questions frequently ask "if a new data point is added, which measure changes the most/least," testing whether students understand *why* the mean is sensitive to outliers while the median is resistant. Mistaking which statistic is outlier-resistant is a genuine conceptual gap, not a careless slip. [OneQuery SAT Probability & Statistics Guide]
- **Misreading axis labels, scales, or units on graphs/tables** — before any statistics calculation even starts, misreading what a bar, point, or cell represents. [UWorld: Avoid Common Mistakes](https://collegeprep.uworld.com/?p=24054)
- **Scatterplot / line-of-best-fit specific errors:**
  - Confusing the slope (rate of change) with the y-intercept (starting value when x = 0).
  - Treating correlation shown in a scatterplot as causation, ignoring possible lurking variables.
  - Extrapolating predictions far outside the observed x-range of the data, where the trend may not hold.
  - Drawing/perceiving the line of best fit as needing to pass through as many points as possible, rather than balancing points above and below it — i.e., treating it like connect-the-dots.
  - Misreading which variable is on which axis — an older classroom study found students plotting coordinate pairs backwards, e.g., plotting (16, 19) as if it were (19, 16).
  [Mathtutoring/classroom sources; plotting-backwards finding is from an older Noyce Foundation student-work study]
- **Probability/statistics distinctness:** confusing "mutually exclusive" with "independent" — these are different concepts, and treating them as synonyms leads to wrong formula choices (addition rule vs. multiplication rule).

---

## Probability

- **Assuming events are independent without checking** — multiplying probabilities (`P(A) × P(B)`) by default, even when the problem describes drawing without replacement or another dependency. *Why it happens:* independence is the "easy" assumption that lets students multiply cleanly, and SAT word problems don't always explicitly say "without replacement," so students default to assuming independence out of habit and time pressure. (consensus/folklore; one source frames this explicitly as a time-pressure-driven habit)
- **Using the independent-events multiplication rule for dependent events** — e.g., in "drawing without replacement" problems, the second probability must be conditioned on the first draw (`P(B|A)`), not treated as an unconditional `P(B)`.
- **Forgetting to subtract the overlap in "at least one" / addition-rule problems** — computing `P(A) + P(B)` for "at least one of A or B" without subtracting `P(A and B)`, which double-counts the overlap. A useful self-check flagged by one source: if `P(A) + P(B) > 1`, you've likely forgotten to subtract the intersection.
- **Confusing "mutually exclusive" with "independent"** — mutually exclusive events (cannot both happen) are a different concept from independent events (one doesn't affect the other's probability); conflating them leads to using the wrong rule.
- **Practical fix commonly recommended:** sketch a two-way table or tree diagram before writing any probability expression, and explicitly test the independence claim (`does P(A and B) = P(A)×P(B)?`) rather than assuming it. [Albert.io probability guides]

---

## Geometry

- **Applying the Pythagorean theorem to a triangle that is not a right triangle** — one of the most-cited conceptual errors; some students treat "hypotenuse" as simply meaning "the longest side of any triangle" rather than specifically the side opposite the right angle in a *right* triangle. [Justin Math: Common Errors and Misconceptions about the Pythagorean Theorem](https://justinmath.com/common-errors-and-misconceptions-about-the-pythagorean-theorem/)
- **Assuming a triangle is right-angled just because it "looks like it" in a diagram** — SAT figures are explicitly not guaranteed to be drawn to scale, and nothing may state or mark a right angle; students who eyeball the figure can get the problem wrong.
- **Treating the missing side as always the hypotenuse** — misapplying `a² + b² = c²` even when the unknown side is actually a *leg*, not the hypotenuse, requiring the formula to be rearranged.
- **Forgetting to take the final square root** — computing `a² + b² = 169` and reporting the answer as 169 instead of √169 = 13.
- **Circle-specific errors:**
  - Confusing radius and diameter — the SAT frequently gives the diameter and expects the solver to halve it before using `A = πr²`; skipping this step is called out explicitly as a common SAT trap.
  - Forgetting to halve the diameter in the area formula specifically (as distinct from the circumference formula, which uses diameter directly), causing students to apply the "halving" habit inconsistently.
  - For semicircles/partial circles: forgetting to double a given half-area before solving for the radius, or forgetting to halve the circumference formula when finding a semicircle's arc length.
  - Mixing up degrees and radians in arc-length/sector-area formulas.
  - Confusing inscribed angles with central angles — forgetting that an inscribed angle measures *half* its intercepted arc, and misapplying this rule to angles formed by tangents or secants, which require different relationships.
  [Varsity Tutors SAT Circles lesson, Brilliant SAT Circles wiki]
- **Similar triangles — assuming corresponding *sides* are equal rather than proportional** — a Virginia DOE teaching resource specifically flags this as a recurring student misconception: treating "similar" as if it meant "congruent" in terms of side length, rather than scaled by a constant ratio. Students also frequently pair up the *wrong* corresponding sides when writing the proportion, even when they correctly understand that the sides are proportional. [Virginia DOE Just in Time Quick Check]
- **Rushing to apply a formula based on recognizing a shape, without reading what's actually being asked** — e.g., calculating area when the question asks for perimeter, or computing the full circle's measure when only a sector is relevant.

---

## Trigonometry

- **Mixing up sine and cosine by misidentifying which side is "opposite" vs. "adjacent"** — called out as the single most common SAT trig mistake; the "wrong" ratio is frequently built directly into a wrong answer choice to catch exactly this error. [Fiveable Digital SAT right triangles & trig](https://fiveable.me/digital-sat/unit-4/right-triangles-and-trigonometry/study-guide/e560NVa0azeI2grw)
- **Not re-identifying opposite/adjacent sides when the reference angle changes** — within the same triangle, which leg counts as "opposite" versus "adjacent" flips depending on which of the two acute angles you're computing from; students who fixed a label for one angle keep using it for the other. [Varsity Tutors]
- **Forgetting/misapplying the complementary angle identity** `sin θ = cos(90° − θ)` — e.g., not recognizing that `sin 20° = cos 70°`, which the digital SAT tests directly (a relatively new, frequently-emphasized item type). [Achievable SAT geometry/trig](https://app.achievable.me/study/sat/learn/geometry-right-triangle-trigonometry)
- **Plugging the hypotenuse into a formula as if it were a leg** — confusing which side is the hypotenuse when setting up Pythagorean or trig-ratio equations.
- **Calculator mode errors** — leaving the calculator in radians when the problem is in degrees (or vice versa), producing a numerically plausible but wrong answer with no red flag to the student. *Why it happens:* careless/procedural — a one-time setting that's easy to forget to check, and the wrong-mode answer often still "looks like a normal number," so nothing tips the student off.
- **Treating multi-step problems (Pythagorean theorem + trig ratio combined) as single-step** — the digital SAT often requires finding a side with Pythagorean theorem first, then using that side in a trig ratio; students who don't read the full question through before starting may do only the first step and submit an intermediate value.

---

## Word Problems (General / Language & Translation Issues)

- **Misreading inequality phrases** — "at least" → ≥, "no more than" / "at most" → ≤, with students regularly flipping the direction, especially when the phrase doesn't map onto the inequality symbol in reading order. (consensus/folklore, repeated very widely)
- **Confusing "less than" with "fewer than"** and similar near-synonym pairs that actually signal count-vs-continuous distinctions in careful usage, though SAT questions are generally written to avoid relying on this distinction — still cited as a trap by multiple prep sources.
- **Reversed phrasing / word order traps** — e.g., "a number less than 5" (= 5 − n or n < 5 depending on context) versus "5 less than a number" (= n − 5); these produce mirror-image expressions and students default to the first interpretation that comes to mind regardless of actual word order. [Ivy Strides SAT Word Problems](https://www.ivystrides.com/post/sat-word-problems)
- **Not checking whether the answer needs to be a whole number or a non-negative quantity** — e.g., getting a fractional number of people, or a negative count, and not recognizing this as a sign of an error (or, on multi-part problems, a sign to round in the direction the context requires rather than mathematically).
- **Overlooking or incorrectly converting units** — one of the most frequently cited grid-in-specific errors: ignoring that the problem states quantities in different units than the final answer requires (e.g., minutes vs. hours, feet vs. inches), and not converting at all, or converting in the wrong direction.
- **Not carrying units through multi-step conversions explicitly** — the recommended fix is to write units into every intermediate step of a calculation (e.g., explicitly writing "mph → ft/s" with the conversion factors shown) so that unit-cancellation errors become visually obvious rather than invisible.
- **Research note — language load as a genuine comprehension barrier, not just carelessness:** A small 2022 study of word-problem-solving among Philippine (English-language-learner) students found that students' most common errors were "encoding errors" (translating the word problem into a mathematical expression), and that one of the most frequently cited underlying difficulties was simply "inability to understand the language used in mathematics" — i.e., students understood the math once correctly translated, but the translation step itself, in a second language, was the actual bottleneck. This is directly relevant for Uzbek students taking the SAT, where English is a second (or third) language: a meaningful share of "math mistakes" on word problems may really be reading-comprehension/vocabulary gaps (not knowing what "revenue," "net," "approximately," or conditional phrasing like "if... then" signal mathematically) rather than an inability to do the arithmetic once the setup is correct. This is not an SAT-specific study, and the sample was small, so treat it as suggestive rather than definitive. [Study cited via DOI 10.21474/ijar01/14358, hosted indexing page]
- **Solving for an intermediate quantity and stopping, rather than the quantity the question actually asks for** — this recurs across every topic area above but is worth stating as a general word-problem pattern: the last sentence of a word problem usually contains the actual target, and many wrong-answer choices are specifically constructed to match the value you'd get by stopping one step early. [OneQuery: Avoid Careless Mistakes](https://www.oneprep.co/blog/avoid-careless-mistakes-on-sat-math)

---

## Time-Management Mistakes

**Structural facts about pacing (digital SAT):** Math is split into two 35-minute modules of 22 questions each (≈1 minute 35 seconds/question on average), and performance on Module 1 determines whether a student is routed to an easier or harder Module 2 — meaning Module 1 pacing/accuracy carries outsized weight, since a poor Module 1 performance locks the student into the lower-scoring ceiling of the easier Module 2, regardless of how well they do on it afterward. [Larry Learns; Apple Routh Digital SAT guides]

- **Spending disproportionate time on a single hard question relative to its point value** — every question is worth the same number of raw points regardless of difficulty, but students frequently sink 4–5 minutes into one question "to get it right" rather than banking the guaranteed points on 3-4 easier questions in that time. This is the single most consistently cited pacing mistake across tutoring sources. (consensus/folklore, very widely repeated)
- **Believing every question must be attempted in order and answered before moving on** — rather than doing a "two-pass" approach (quick pass for everything answerable in under ~60-75 seconds, then returning to flagged harder items with remaining time).
- **Not reserving any buffer time at the end of a module to revisit flagged questions** — some students use the entire module time attempting new questions and leave zero time to recheck flagged or guessed answers.
- **Treating data-analysis/statistics questions (reading tables, graphs, scatterplots) as "quick" because they look like simple reading rather than calculation** — this is a specific pacing trap: these questions often require careful extraction of 2-3 separate numbers from a table/graph *before* any calculation starts, and students underestimate the reading-and-extraction time, leading to rushed misreads (see "misreading axis labels" above) more than on pure-algebra items.
- **Over-relying on the calculator/Desmos for problems answerable faster by reasoning or elimination** — typing an equation into Desmos and waiting for a graph can cost more time than recognizing a shortcut (e.g., plugging in answer choices, using a special-case number). Conversely, calculator errors also arise from input mistakes (sign/parenthesization typos) rather than reasoning errors, meaning the calculator can introduce *new* errors under time pressure even when the math reasoning was correct. [UWorld Digital SAT calculator guide]
- **Rushing through questions perceived as "easy," ironically causing more careless errors there than on hard questions** — several sources specifically flag that students lose more points to carelessness on problems they "already know how to do" than on ones that make them slow down and think. This is a genuine time-management/attention-allocation mistake: students allocate vigilance in inverse proportion to perceived difficulty, when error risk doesn't actually track perceived difficulty that closely.
- **Guessing poorly or leaving blanks rather than eliminating choices and guessing strategically** — since there's no guessing penalty on the SAT, leaving a question blank due to running out of time is a pure and avoidable point loss; the recommended practice is to eliminate obviously wrong choices (narrowing 4 options to 2-3) even under time pressure, which meaningfully raises guess accuracy, rather than leaving it blank or guessing uniformly at random.
- **Grid-in (student-produced response) questions costing extra time relative to their point value** due to format-specific slips: rounding too early and losing precision, entering a fraction in a non-accepted format, or forgetting that equivalent decimal/fraction forms are both acceptable (so some students waste time converting unnecessarily to match a format they assume is required). [Manyagroup: SAT Math Grid-Ins common mistakes]

---

## Sources

- [Brilliant — SAT Algebraic Manipulations](https://brilliant.org/wiki/sat-algebraic-manipulations)
- [Axiom Academy — SAT Common Traps to Avoid](https://theaxiomacademy.org/learn/sat-common-traps-avoid)
- [Mathnasium — 5 Most Common Algebra Test Mistakes](https://www.mathnasium.com/math-centers/lakewoodco/news/common-algebra-mistakes)
- [Varsity Tutors — One-Variable Linear Equations practice](https://www.varsitytutors.com/practice/subjects/tachs-math/quiz/one-variable-linear-equations)
- [Lead4ward — Algebra I Linear Functions Quick Study Guide (TX STAAR)](https://account.lead4ward.com/docs/conferences/review23/resources/math/1_m_alg1_linear_functions_qsg.pdf)
- [Varsity Tutors — Systems of Equations (SAT Math)](https://internal.varsitytutors.com/practice/subjects/sat-math/help/systems-of-equations)
- [OneQuery (OnePrep) — Avoid SAT Algebra Mistakes](https://www.oneprep.co/blog/avoid-sat-algebra-mistakes)
- [OneQuery (OnePrep) — Why Students Get Stuck on SAT Algebra](https://www.oneprep.co/blog/why-students-get-stuck-on-sat-algebra)
- [Academic study on systems-of-equations misconceptions (Spain, ages 13–14), hosted at Universidad de Oviedo repository](https://portalinvestigacion.uniovi.es/documentos/6369acd069e22d1dfe08940a)
- [Open Exam Prep — Radical Equations & Extraneous Solutions](https://open-exam-prep.com/study-guides/sat-math/advanced-math-quadratics/radical-equations-extraneous)
- [Ivy Strides — Quadratic Formula Mistakes](https://www.ivystrides.com/post/quadratic-formula-mistakes)
- [Albert.io — Digital SAT Math Exponents/Radicals Guide](https://www.albert.io/blog/?p=117731)
- [Virginia Department of Education — Just in Time Quick Checks (Radicals)](https://www.doe.virginia.gov/home/showpublisheddocument/65313/638972408728370000)
- [Cazoom Maths — Algebra 2 Indices Worksheets](https://www.cazoommaths.com/us/math-worksheets/algebra-2-indices-worksheets/)
- [CA Foundation — Ratio and Proportion: Common Mistakes and Corrections](https://catestseries.org/blogs/ca-foundation-ratio-and-proportion-common-mistakes-and-corrections)
- [Virginia Department of Education — Practical Applications: Rational Number and Proportional Reasoning](https://doe.virginia.gov/home/showpublisheddocument/30214/638046481597400000)
- [PrepScholar — Statistics on SAT Math: Strategies for Mean, Median, Mode](https://blog.prepscholar.com/statistics-on-sat-math-strategies-for-mean-median-and-mode)
- [UWorld College Prep — How to Avoid Common Mistakes on Digital SAT Math](https://collegeprep.uworld.com/?p=24054)
- [OneQuery (OnePrep) — SAT Probability and Statistics Guide](https://www.oneprep.co/blog/sat-probability-and-statistics-guide)
- [RevisionDojo — Why Students Assume Events Are Independent When They Are Not](https://www.revisiondojo.com/blog/why-students-assume-events-are-independent-when-they-are-not)
- [Justin Math — Common Errors and Misconceptions about the Pythagorean Theorem](https://justinmath.com/common-errors-and-misconceptions-about-the-pythagorean-theorem/)
- [e-GMAT — GMAT Geometry Questions: Most Common Mistakes](https://e-gmat.com/blogs/gmat-geometry-questions-most-common-mistakes)
- [Varsity Tutors — SAT Circles lesson](https://www.varsitytutors.com/practice/subjects/sat/lessons/circles)
- [Brilliant — SAT Circles wiki](https://brilliant.org/wiki/sat-circles)
- [Virginia Department of Education — Just in Time Quick Check (Similar Triangles)](https://www.doe.virginia.gov/home/showpublisheddocument/75325/639027783753470000)
- [Fiveable — Digital SAT Right Triangles & Trigonometry study guide](https://fiveable.me/digital-sat/unit-4/right-triangles-and-trigonometry/study-guide/e560NVa0azeI2grw)
- [Achievable — SAT Geometry: Right Triangle Trigonometry](https://app.achievable.me/study/sat/learn/geometry-right-triangle-trigonometry)
- [Quest for Success — Mastering Trigonometry for SAT](https://www.questforsuccess.in/sat-math-trigonometry-tips/)
- [RevisionDojo — Avoid Costly Mistakes: 15 Common Grammar Pitfalls on SAT Math](https://www.revisiondojo.com/blog/avoid-costly-mistakes-15-common-grammar-pitfalls-on-the-sat-math-section-and-how-to-fix-them)
- [Ivy Strides — SAT Word Problems](https://www.ivystrides.com/post/sat-word-problems)
- [Manyagroup — SAT Math Grid-Ins: 7 Common Mistakes Indian Students Make](https://www.manyagroup.com/blog/sat/sat-math-grid-ins-7-common-mistakes-indian-students-make/)
- [Study on word-problem misconceptions among Filipino (ELL) students, DOI 10.21474/ijar01/14358](https://www.doi.org/10.21474/ijar01/14358)
- [PrepScholar ExpertHub forum — Preventing Careless Errors on SAT Math](https://experthub.prepscholar.com/t/preventing-careless-errors-on-sat-math/7572)
- [PrepScholar — 7 Most Common SAT Math Mistakes and How to Avoid Them](https://blog.prepscholar.com/most-common-sat-math-mistakes)
- [Princeton Review Singapore — SAT Math mistakes](https://www.princetonreview.sg/?p=5973)
- [Applerouth — Digital SAT guide](https://www.applerouth.com/about-test/sat)
- [Larry Learns — How Many Math Questions Are on the SAT](https://www.larrylearns.com/blog/how-many-math-questions-are-on-the-sat)
- [College Board — How Scores Are Calculated](https://satsuite.collegeboard.org/sat/scores/understanding-scores/how-scores-are-calculated)
- Systematic review of algebraic errors/misconceptions in South African secondary students (Kiat's error taxonomy: conceptual/procedural/technical), 9 studies 2014–2024, hosted at [iated Digital Library](https://library.iated.org/view/BANJO2025ASY)
- Grade 9 algebra error study using Koch's error analysis and SOLO taxonomy, Mathaba et al. 2024, *Journal on Mathematics Education*, 15(2), hosted at [DOAJ](https://doaj.org/article/ce09e1ca1f0641848829a1a19ce18161)

**Note on source quality:** The large majority of citations above are commercial test-prep/tutoring company blogs rather than peer-reviewed research, which is the nature of SAT-specific material — College Board does not publish item-level error-rate data. Where a claim is repeated near-identically across many independent tutoring sources without one of them citing primary data, it is marked **(consensus/folklore)** in the body text above rather than presented as a verified statistic. The handful of genuine academic studies cited (systems of equations misconceptions in Spain, algebra error taxonomies in South Africa/Indonesia, word-problem language barriers for Filipino ELL students) are **not SAT-specific** — they study general algebra/word-problem learning — but are included because their findings about *why* certain error types occur (conceptual vs. procedural vs. language-comprehension) plausibly generalize to SAT-takers, and are flagged as such inline.
