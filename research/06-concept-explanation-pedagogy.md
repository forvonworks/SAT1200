# 06 — Concept-Explanation Pedagogy for Self-Study SAT Math

**Purpose:** Before locking in a page-layout standard for the "Concepts" pages, this doc researches what
cognitive-science and instructional-design literature says about how a math concept should be explained
on the page to a **self-study** student (no teacher present, often a non-native English reader), and what
structural pattern well-regarded prep books/resources use. Confidence levels are flagged throughout —
some claims are strong experimental findings (worked-example effect), others are practitioner consensus
without controlled studies (ESL visual-scaffolding specifics, "best" rankings of competitor books).

---

## 1. Text vs. visuals: when does a diagram actually help?

**Confidence: Well-documented for the underlying theories; math-specific evidence is present but thinner
than general multimedia-learning evidence.**

Three linked theories govern this:

- **Cognitive Load Theory (Sweller).** Working memory is severely limited. Instruction should minimize
  *extraneous* load (poor layout, clutter, unnecessary decoration), manage *intrinsic* load (the inherent
  difficulty of the concept — chunk it, don't dump it all at once), and protect capacity for *germane* load
  (the effortful processing that actually builds schemas/understanding). The direct design implication: a
  visual is good **only if it reduces processing effort toward the concept**; a visual that is merely
  decorative, or that forces the student to visually search and mentally merge separated information,
  **adds** load and hurts learning.
- **Dual Coding Theory (Paivio).** Paivio's model posits two separate but interconnected mental channels —
  verbal and nonverbal/imagistic. A learner who encodes the same idea in both channels has more retrieval
  paths than one who encodes it in only one. Note: Paivio's own theory described how memory *might* be
  structured; it was not a classroom prescription — later researchers (notably Mayer) turned it into
  actionable multimedia-design principles. Caution: some researchers (e.g., David Didau) argue "dual
  coding" is sometimes applied uncritically in schools without matching the specific evidence base — worth
  knowing so the team doesn't over-claim the theory.
- **Mayer's Multimedia Learning Principles** (direct, actionable descendant of dual coding + CLT, with the
  most experimental backing of the three for *how* to pair text and visuals):
  - **Spatial contiguity:** put related text and image physically close together (captions ON the diagram,
    not in a separate callout far away).
  - **Temporal/sequential alignment:** if steps unfold, the explanation and the visual should unfold in the
    same order, not visual-then-wall-of-text or vice versa.
  - **Signaling:** use arrows, color, bolding, or numbering to point directly at what matters in a diagram
    rather than making the student hunt for it.
  - **Redundancy principle:** do not force the student to read identical information twice in two different
    forms (e.g., a fully verbose paragraph restating exactly what a labeled diagram already shows) — this
    wastes channel capacity rather than doubling it.
  - **Coherence principle:** cut anything — decorative images, tangential text, "fun fact" boxes near the
    core explanation — that doesn't serve the concept being taught. Decoration measurably *hurts*
    comprehension by competing for attention, it doesn't just fail to help.
  - **Segmenting:** break a multi-step explanation into discrete, separated chunks the reader can process
    one at a time rather than one unbroken block.
- **Split-Attention Effect (Sweller/Chandler).** This is the single most directly actionable finding for a
  print workbook: when a diagram and the text that explains it are physically separated (e.g., diagram at
  top of page, explanatory labels/paragraph at the bottom, or on a facing page), the student must hold
  fragments in working memory while visually searching to match them up — this search is a *prerequisite
  cost* paid before any real learning starts, and it measurably increases load, time-on-task, and lowers
  problem-solving performance versus an **integrated** format (labels placed directly on/beside the parts
  of the diagram they describe). The fix is physical/spatial, not more explanation: move labels onto the
  diagram, use numbered call-outs tied to numbered steps, etc.

**Net implication for this book:** A visual earns its place only when it (a) is physically integrated with
the text it supports (no separate "see diagram above" split), (b) replaces or compresses verbal explanation
rather than merely illustrating it decoratively, and (c) uses signaling (arrows/color/numbering) to direct
attention. A visual that recreates in picture form something the text already explains in full is waste,
not reinforcement, under the redundancy principle.

---

## 2. Structural pattern used by well-regarded test-prep books/resources

**Confidence: Moderate.** Retailer/publisher descriptions and secondary reviews are the main evidence for
competitor book structure (no independent academic study of SAT-prep-book pedagogy exists); the general
instructional patterns (I-We-You, Rosenshine) are well-documented in education research.

- **PWN the SAT: Math Guide (McClenathan)** — found in this project's earlier competitor research
  (`03-competitor-book-landscape.md`) to be the most consistently well-regarded book for strong scorers.
  Its structure, per that research and retailer/publisher descriptions:
  - Organized by official College Board content domain (Heart of Algebra, Passport to Advanced Math,
    Problem Solving & Data Analysis, Additional Topics), plus a separate "Techniques" section for
    cross-cutting strategy.
  - Each chapter/concept is **tightly scoped to what is actually tested** (not generic textbook math) —
    this specificity, not visual design, is repeatedly cited as its strength.
  - Each chapter **ends with a curated list of real, retired official SAT questions** that use the concept
    just taught, cross-referenced so the student immediately drills what was just explained.
  - Practice questions are explicitly labeled calculator/no-calculator.
  - Written in an engaging, informal voice (a stylistic choice, not a structural one) — reviewers credit the
    voice for keeping a self-study reader going, separate from the content organization itself.
  - Its documented *weakness* is at the foundations end — it assumes a base of competence and isn't built
    to take a weak/beginner student from zero. This is directly relevant since this series' Book 1 is
    explicitly a fundamentals book — PWN's structural pattern (scope tightly, example, then drill
    immediately on real questions) is worth adopting, but the *foundations-first* framing needs to be
    original to this series since PWN doesn't model that well.
  - [PWN the SAT: Math Guide — AbeBooks listing](https://www.abebooks.com/PWN-SAT-Math-Guide-McClenathan-Mike/32111553192/bd)
  - [PWN the SAT: Math Guide — Goodreads ratings page](https://www.goodreads.com/book/show/29425370)
  - [PWN the SAT: Math Guide product listing](https://wald.de/products/pwn-the-sat-math-guide/219449730/)

- **College Panda's SAT Math** (also well-regarded per prior research) pairs content + strategy and is
  praised for teaching "multiple ways to solve a problem" — i.e., showing more than one worked approach per
  concept where relevant, though its answer explanations are flagged (in `03`) as sometimes terse —
  reinforcing that the *explanation quality*, not just presence of practice volume, is what separates
  well-regarded from merely-high-volume books (Barron's/Kaplan, by contrast, are praised for volume of
  practice but explicitly criticized for thin explanatory depth).

- **Generic classroom instructional pattern — "I do / We do / You do"** (direct modeling → guided practice →
  independent practice): the dominant sequence taught in teacher training, directly descended from
  Rosenshine's Principles of Instruction (Principle 4: "provide models and worked examples" as an explicit
  modeling strategy that reduces cognitive load by letting the learner focus on the task rather than
  searching for a method; Principle 8: scaffolds like worked examples and cue cards are *temporary* support
  withdrawn as fluency grows). Mapped onto a workbook (no teacher to do the "We do" step live):
  **Concept/definition → fully worked example (the "I do," on the page) → a lighter-scaffolded example or
  "your turn" guided step (the "We do," can be a partially-worked example on the page) → independent
  practice set (the "You do").** This maps very cleanly onto this book's existing Concepts → Vocabulary →
  practice Sets flow — it just means the Concepts page itself should contain the "I do" (and ideally a
  mini "We do") rather than jumping straight from definition to an unscaffolded practice set.
  - One dissenting view exists (ASCD, "a better way to model math") recommending **You-do → We-do → I-do**
    (struggle first, then model) — this is a live-classroom productive-struggle approach and is harder to
    make work in a self-study print book with no facilitator to manage the struggle phase, so it's noted
    but not recommended for this project's format.
  - [Third Space Learning — "I Do, We Do, You Do"](https://thirdspacelearning.com/blog/i-do-we-do-you-do)
  - [Eton College CIRL — Rosenshine's worked-example principle](https://cirl.etoncollege.com/?p=669)
  - [ASCD — "A Better Way to Model Math"](https://ascd.org/blogs/a-better-way-to-model-math)

- **Khan Academy's video+practice model** — evidence is mixed and mostly descriptive/correlational, not
  experimental:
  - An SRI/Gates-funded study found positive association with usage and test scores, plus reduced math
    anxiety and improved self-efficacy, but the authors explicitly caution it was **not a randomized or
    causal study**.
  - Multiple independent studies (South Africa, Philippines, a small single-case special-education study)
    found videos alone work for simpler concepts but are **ineffective or null for harder concepts** — one
    quasi-experimental study on order of operations found no significant difference at all.
  - The most consistent finding across sources: **the practice problems and progress tracking, not the
    videos, are what teachers and students report as the actually useful part.** This is a meaningful
    caution against over-investing production value in the "explanation" media itself at the expense of a
    well-sequenced practice set — the explanation's job is to get the student *competent enough to
    practice*, not to be engaging in isolation.
  - [SRI/Gates Khan Academy study summary — KQED MindShift](https://www.kqed.org/mindshift/35412)
  - [Effectiveness of Khan Academy order-of-operations videos (quasi-experimental, null result)](https://repository.capsu.edu.ph/handle/123456789/840?show=full)

---

## 3. How much text is too much — readability and L2 readers

**Confidence: Mixed.** General readability research is mature; math-specific and ESL/L2-specific research
exists but is thinner, and this project's own prior research (`05-uzbek-student-considerations.md`) already
established strong, directly relevant findings that this section builds on rather than duplicates.

- **Sentence length is a core readability variable in math text specifically**, confirmed by a 2020 study
  analyzing Turkish 5th–8th grade math textbooks with teacher and student input — sentence length was
  flagged as one of the important variables driving readability scores.
- **Caution on readability formulas:** multiple sources warn that standard readability formulas (Flesch,
  etc.) do not account for *concept load* — a short sentence can still be hard if it's conceptually dense
  (e.g., "A line's slope is the ratio of its rise to its run" is short but concept-loaded). One study of
  3rd–6th graders found formula-based readability had **no relationship** to students' actual ability to
  solve the problems. Practical implication: don't just chase a low Flesch-Kincaid score — shortening
  sentences without simplifying the underlying idea-density doesn't help, and can even strip out
  connective words that aid comprehension.
- **L2/ELL-specific finding (directly actionable):** a systematic review (TU Delft) found that the negative
  effect of sentence complexity on comprehension is **more pronounced in learners with limited English
  proficiency**, and that small, low-content words — prepositions especially — are disproportionately
  hard for L2 readers, even though they're easy to overlook as "simple" words. This matters directly for
  this series: phrases like "in terms of," "with respect to," "such that," "in order to" should be flagged
  and minimized or explained, not just big vocabulary words.
- **This project's own prior ESL research (`05-uzbek-student-considerations.md`) already found:**
  Moschkovich's influential work argues math-language proficiency is not just a vocabulary list — it
  includes syntax, discourse patterns, and a distinct "math register" — and frames the student's home
  language as a resource (supports this series' existing bilingual term callouts, e.g. "Fraction – Kasr")
  rather than something to suppress. It also catalogued real vocabulary traps (words with everyday meanings
  that differ from math meanings — *product, table, volume, degree, mean* — and notation differences, e.g.
  Russian/Uzbek-tradition decimal commas and "angle coefficient" for slope). These are concrete content
  items for the Vocabulary sections, and reinforce visuals' particular value for L2 readers: a diagram
  lets a non-native reader verify meaning without depending entirely on parsing English syntax.
- **No direct count exists in the literature for "ideal sentence length for SAT-prep math text,"** so the
  practical recommendation below is a synthesis, not a cited number.
  - [Readability in Turkish math textbooks — Ankara University](https://avesis.ankara.edu.tr/yayin/629cde90-1071-42f1-8175-00c4495ed19e/teachers-and-students-views-on-the-readability-and-comprehensibility-of-texts-in-secondary-school-mathematics-textbooks)
  - [TU Delft — sentence complexity and ELL math comprehension review](https://repository.tudelft.nl/file/File_4b7e60bb-6c73-464b-9af1-288a4b24659f)
  - [Exeter PME — "Comprehension of Mathematical Text" (readability-formula caution)](https://www.exeter.ac.uk/research/groups/education/pmej/pome17/lwiest.htm)
  - [Great Minds/Eureka Math — "Improving Readability in Math Without Compromising Rigor"](https://gm.greatminds.org/improving-readability-in-math-without-compromising-rigor)

---

## 4. Worked-example design: how many, how granular, show mistakes?

**Confidence: Well-documented for the core worked-example effect; moderate/mixed for mistake-based
("erroneous") examples and for exact counts.**

- **The worked-example effect is one of the most replicated findings in cognitive load research.**
  Sweller & Cooper's original 1985 algebra study found students given worked examples learned faster
  (~6x less time) and made fewer errors than those given conventional problem-solving practice. Mechanism:
  a novice solving from scratch burns working-memory capacity *searching* for a method; a worked example
  spends that capacity on *understanding* the method instead. The effect is strongest **early** in learning
  a concept and fades (or can reverse — the "expertise reversal effect") once the learner has some fluency,
  at which point unscaffolded practice becomes more valuable than more examples.
- **A 2023 meta-analysis (Barbieri, Miller-Cotto, Clerjuste, & Chawla; *Educational Psychology Review*, 55
  studies, elementary through adult) found an average 18-percentile-point improvement** from studying
  worked examples vs. problem-solving alone (effect size g = 0.43, small-to-medium, high heterogeneity).
  Two findings from this meta-analysis are directly load-bearing for page design decisions:
  - **Self-explanation prompts** ("explain to yourself why this step works") paired with worked examples
    **did not help, and in some comparisons performed worse** than worked examples alone. This cuts against
    reflexively adding "why does this work?" prompts to every example — if included, they should be used
    sparingly and only where genuinely useful, not as a default formula.
  - **Examples using correct solutions produced larger gains than examples using incorrect solutions.**
    This is an important nuance against a naive "always show the wrong way" rule (see next point).
- **Multiple examples per concept, varied, not just repeated:** Atkinson et al.'s widely-cited review
  recommends **more than one example per conceptual problem type**, varying surface format while keeping
  the underlying structure constant (so the student learns to recognize the *pattern*, not just one
  specific numeric instance), and placing examples in close proximity to the matched practice problems
  that follow (again reinforcing the split-attention concern — don't separate the model from the practice
  that uses it). No source gives a single "magic number"; 2 is the implied practical floor (one example
  risks the student pattern-matching to surface details rather than structure; one well-chosen variant
  example is usually enough to signal "this generalizes" without bloating the page).
- **Step granularity — "fading"/"completion strategy" (Van Merriënboer; Atkinson, Renkl & Merrill):** the
  research-backed progression is: (1) one fully worked example showing every step and the *reasoning*
  between steps, not just the algebra; (2) a partially-worked example with one or more steps left for the
  student to fill in (this is the natural home for a "Your Turn" box with blanks); (3) full independent
  practice. Backward fading (withhold the *last* step first, then more) has shown a positive effect in
  recent studies and is easier to scaffold because the student always starts from a provided setup.
  Crucially: show the *reasoning between steps*, not just the algebra — a worked example that jumps lines
  without a stated reason for the move reintroduces the very search-for-method cost the technique is meant
  to eliminate.
- **Showing mistakes explicitly — "erroneous examples":** a real, actively-researched sub-literature exists
  (Zhao & Acosta-Tello 2016; Tsovaltzi et al. 2009; Durkin & Rittle-Johnson; Melis & Kriesell), and it is
  **more positive than the Barbieri caveat above suggests, but conditional:**
  - Pairing an **incorrect example alongside a correct one** (not incorrect-only) improved conceptual
    understanding over two correct examples in at least one controlled study (Zhao & Acosta-Tello).
    A third-grade study (85 students) found post-test scores significantly higher for the erroneous-example
    condition than for the standard worked-example condition.
    This matches exactly this project's own earlier finding (`04-common-student-mistakes.md` presumably
    documents the actual mistake patterns) — a "here's the wrong way, here's why it's wrong, here's the
    right way" box is well-supported **specifically when a well-known, predictable mistake exists for that
    concept** (e.g., sign errors, flipping an inequality, misapplying a formula) — it should not be used as
    a mandatory box on every single Concepts page regardless of whether a common error exists.
  - Mechanistically, researchers believe the benefit comes from directly confronting and correcting a
    misconception, and there's a secondary emotional benefit: seeing *someone else's* mistake named and
    explained may reduce the embarrassment/anxiety of making that mistake oneself, which matters for a
    self-study, no-teacher context.
  - Caveat: the field is still described by its own researchers as "very much open" — findings are
    promising but mostly small/single-site studies, and erroneous-examples-only (without a correct contrast)
    perform worse than correct examples per Barbieri. **Reconciling this with the Barbieri caveat above:**
    the right design is "correct example first, then a short wrong-way/right-way contrast box for the
    concept's known common error" — not "replace a correct example with an incorrect one," and not a
    mistake box on every page regardless of whether the concept has a well-documented common error.
  - [Worked-example effect — overview](https://en.wikipedia.org/wiki/Worked-example_effect)
  - [Barbieri et al. meta-analysis — UDel summary/poster](https://www.cehd.udel.edu/wp-content/uploads/2022/02/Worked-Examples-Meta-Poster_022722_SC.pdf)
  - [Learning Scientists guest post on the Barbieri meta-analysis](https://www.learningscientists.org/blog/2024/1/25-1)
  - [Structural Learning — "Worked examples: how to design and fade support"](https://www.structural-learning.com/post/worked-examples)
  - [Erroneous examples — effects in individual/collaborative settings (DLSU)](https://agpci.dlsu.edu.ph/agpci/article.php?a=23000)

---

## 5. "Concept explanation before practice" page design in print workbooks specifically

**Confidence: Low-moderate.** Peer-reviewed research on *print workbook page layout* specifically (as
distinct from full textbooks or digital/classroom instruction) is sparse; most of what's below is
triangulated from the CLT/multimedia principles above (which generalize to any print medium) plus
commercial-workbook descriptive conventions, which are informative but not independently verified research.

- **No dedicated controlled-study literature exists on "workbook concept-page template design"** as its own
  research subfield — this is a genuine gap. The applicable evidence is the general CLT/dual-coding/
  worked-example research above, applied to the printed-page medium, plus descriptive conventions from
  commercially successful workbooks.
- **A commercial convention worth noting (Go Math! and similar basal workbook series):** typical unit
  layout is concept introduction with brief explanation + integrated visual aid → practice problems →
  application/transfer task → review. The "brief explanation + integrated visual" framing (not long prose)
  is the consistent descriptive pattern across commercial math workbooks, though this is publisher
  marketing description, not independent research, so it should be treated as corroborating rather than
  authoritative.
- **Split-page I-do/We-do convention from teacher-training materials** (not a controlled study, but a
  specific, reusable print-layout idea): one teacher-training resource describes a page with the fully
  modeled ("I do") example on one side and a parallel, lightly-scaffolded ("We do") example on the other,
  deliberately structured so the student can compare the two side by side and see what changed. This
  translates directly into a two-column or stacked "Model / Your Turn" layout for a Concepts page — a
  concrete, implementable idea even without a controlled-study citation behind the print-specific version.
- **The strongest actually-applicable finding for workbook page design remains split-attention/spatial
  contiguity** (Section 1): in a static print page, there is no "narration" channel to offload text onto
  (unlike video), so **all** text-visual integration must happen through layout alone — labels on the
  diagram, steps numbered to match a numbered visual, color used consistently and sparingly as the one
  signaling tool available on a static page. This is arguably the single most important, well-evidenced
  design constraint specific to a *print* (vs. video or live-classroom) format.
- **Net honest assessment:** this section's conclusions are a sound, defensible extrapolation from strong
  general principles (CLT, dual coding, worked-example effect, split-attention) into the print-workbook
  medium, not a direct citation of print-workbook-specific controlled studies, because that specific
  literature does not appear to exist in a form this search surfaced. The Recommended Pattern below should
  be understood on that basis.

---

## Recommended Pattern

A concrete, practical template for this book's Concepts pages, synthesizing all five sections above:

**1. Definition / Rule (short, integrated with notation)**
- 1–3 sentences max for the core rule itself. State it, then immediately show it in symbols right next to
  the words (not in a separate box far below) — satisfies dual coding (verbal + symbolic channel) and
  spatial contiguity in one move.
- Avoid low-content "glue" phrases that are hard for L2 readers ("in terms of," "with respect to," "such
  that") — prefer direct phrasing. Keep sentences short, but don't strip connective words that carry the
  logic (e.g., "because," "so that") — the goal is low idea-density per sentence, not artificially choppy
  text.
- Any bilingual vocabulary term (Uzbek/English, per the existing "Fraction – Kasr" convention) gets
  introduced right here, inline, not deferred entirely to a separate Vocabulary section.

**2. One fully-worked Model example ("I do")**
- Show every step, including the *reasoning* for each move (not just the algebra) — "divide both sides by
  3 **because** we need x alone," not just the next line of math.
- Integrate any diagram directly into this example: labels on the figure itself, numbered steps matched to
  numbered diagram call-outs, consistent color used only for signaling (e.g., the term being isolated),
  never decoratively.
- No self-explanation prompts here ("why does this work?") as a default — evidence suggests they don't
  reliably help and can add load. Only include one where a concept is genuinely subtle enough to warrant it.

**3. One varied, lightly-scaffolded example ("We do" / "Your Turn")**
- Same underlying concept, different surface numbers/context, with the **last step (or two) left blank**
  for the student to complete (backward-fading — shown to work well and easy to scaffold). This single
  step is what separates "read a worked example" from "practice," before the student hits the full
  practice Set — it is the bridge Rosenshine's model calls for and this book's Concepts→Set structure
  currently skips.
- Placed immediately adjacent to the Model example (same page, side-by-side or directly below) — never on
  a facing page or after the Vocabulary section — to avoid split-attention costs between the two.

**4. Common-mistake callout — conditional, not automatic**
- Include a "wrong way → why it's wrong → right way" box **only for concepts with a well-documented,
  predictable common error** (this project's own `04-common-student-mistakes.md` is the source list to
  check against for each concept). Always pair the wrong version *with* a correct contrast — never show an
  incorrect example in isolation.
- Skip this box entirely for concepts without a well-known predictable error; forcing one onto every page
  dilutes its effect and adds length without benefit.

**5. Visual-to-text ratio**
- Rule of thumb: if a diagram/visual doesn't replace or compress words (not just echo them), cut it. Every
  visual must be integrated (labels on it, not beside it in a separate block) and must do real signaling
  work (arrows/color pointing at what matters), not decoration. For most algebra/arithmetic concepts this
  means a visual is optional; for anything geometric, coordinate-plane-based, or involving a graph/figure,
  an integrated visual is mandatory and should dominate the example over prose.

**6. Length discipline**
- Target the whole Concepts page (definition + both examples + optional mistake box) to be scannable in one
  sitting without turning a page mid-concept — this is less about a specific word count than about applying
  the coherence principle ruthlessly: no tangential "fun fact" asides, no restating in prose what a labeled
  diagram or a worked step already shows.

**7. Sequence recap:** Definition+notation → Model example (I do, fully worked, reasoned) → Your-Turn
example (We do, last step blank) → [conditional] common-mistake contrast box → Vocabulary → practice Set
(You do). This keeps the existing Concepts → Vocabulary → Sets skeleton but inserts the missing scaffolded
step research says a self-study book needs between "here's the rule" and "now go solve 15 problems alone."

---

## Sources

**Cognitive load / dual coding / multimedia:**
- [Worked-example effect — Wikipedia overview](https://en.wikipedia.org/wiki/Worked-example_effect)
- [Split attention effect — Wikipedia overview](https://en.wikipedia.org/wiki/Split_attention_effect)
- [Mayer's 12 Principles of Multimedia Learning — Dartmouth](https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655)
- [Mayer's 12 Principles of Multimedia Learning — Lucidea](https://lucidea.com/blog/mayers-12-principles-of-multimedia-learning)
- [David Didau — "The Dual Coding Delusion" (critical perspective)](https://daviddidau.substack.com/p/the-dual-coding-delusion)
- [Split-attention in worked examples — Kalyuga et al., tecfa.unige.ch](https://tecfa.unige.ch/tecfa/teaching/methodo/Kalyuga99.pdf)

**Worked-example research:**
- [Manson & Ayres (2019), worked examples review — USP repository](https://repository.usp.ac.fj/id/eprint/14334/4/Manson%20Ayres%20%282019%29.pdf)
- [Barbieri, Miller-Cotto, Clerjuste & Chawla meta-analysis summary poster — UDel](https://www.cehd.udel.edu/wp-content/uploads/2022/02/Worked-Examples-Meta-Poster_022722_SC.pdf)
- [Learning Scientists — guest post on the Barbieri meta-analysis](https://www.learningscientists.org/blog/2024/1/25-1)
- [Structural Learning — "Worked examples: how to design and fade support" (fading/completion strategy)](https://www.structural-learning.com/post/worked-examples)
- [Erroneous examples in individual/collaborative settings — DLSU](https://agpci.dlsu.edu.ph/agpci/article.php?a=23000)
- [Tsovaltzi et al. 2009 — erroneous examples, ECTEL (PDF)](https://www-live.dfki.de/fileadmin/user_upload/import/4653_Tsovaltzietal-ErroneousExamples-ECTEL-2009.pdf)

**Instructional sequencing:**
- [Eton College CIRL — Rosenshine's worked-example and scaffolding principles](https://cirl.etoncollege.com/?p=669)
- [Third Space Learning — "I Do, We Do, You Do: How to Introduce New Learning Effectively"](https://thirdspacelearning.com/blog/i-do-we-do-you-do)
- [ASCD — "A Better Way to Model Math" (You-do/We-do/I-do dissent)](https://ascd.org/blogs/a-better-way-to-model-math)

**Readability / L2 / ESL:**
- [Readability of secondary-school math textbooks (Turkish study) — Ankara University](https://avesis.ankara.edu.tr/yayin/629cde90-1071-42f1-8175-00c4495ed19e/teachers-and-students-views-on-the-readability-and-comprehensibility-of-texts-in-secondary-school-mathematics-textbooks)
- [TU Delft repository — sentence complexity and ELL math comprehension](https://repository.tudelft.nl/file/File_4b7e60bb-6c73-464b-9af1-288a4b24659f)
- [Exeter PME — "Comprehension of Mathematical Text"](https://www.exeter.ac.uk/research/groups/education/pmej/pome17/lwiest.htm)
- [Great Minds/Eureka Math — "Improving Readability in Math Without Compromising Rigor"](https://gm.greatminds.org/improving-readability-in-math-without-compromising-rigor)
- This project's own prior research: `/home/user/SAT1200/research/05-uzbek-student-considerations.md` (Moschkovich math-register findings, vocabulary false-friends, notation differences)

**Test-prep / Khan Academy:**
- [PWN the SAT: Math Guide — AbeBooks listing](https://www.abebooks.com/PWN-SAT-Math-Guide-McClenathan-Mike/32111553192/bd)
- [PWN the SAT: Math Guide — Goodreads](https://www.goodreads.com/book/show/29425370)
- [SRI/Gates Khan Academy study — summarized via KQED MindShift](https://www.kqed.org/mindshift/35412)
- [Khan Academy order-of-operations video effectiveness (null result) — CapSU repository](https://repository.capsu.edu.ph/handle/123456789/840?show=full)
- This project's own prior research: `/home/user/SAT1200/research/03-competitor-book-landscape.md` (PWN/College Panda/Barron's/Kaplan structural and reputation details)
