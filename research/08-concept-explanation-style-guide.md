# Concept Explanation Style Guide

Practical, combined guide for writing/rewriting every "Concepts" page in the SAT 1200+ series — both
**how a concept is structured on the page** and **what natural Uzbek actually sounds like**, so pages stop
reading like direct Google Translate output. Synthesizes `06-concept-explanation-pedagogy.md` (cognitive
science / instructional design) and `07-uzbek-math-language-style.md` (real Uzbek source analysis). Read
those two files for full sourcing and confidence tags; this file is the actionable summary to write from.

---

## Part 1 — Page Structure

The research-backed sequence, replacing "definition → straight to practice" with the missing scaffolded
step self-study books need:

**1. Definition / Rule — short, notation integrated inline**
1–3 sentences max. State the rule, show it in symbols immediately next to the words (not in a separate box
below). Introduce the bilingual term right here, inline — not deferred to a separate Vocabulary section.
Avoid low-content "glue" phrases that are disproportionately hard for L2 readers ("in terms of," "with
respect to," "such that") — but keep real connective words ("because," "so that") that carry the logic.

**2. One fully-worked Model example ("I do")**
Every step shown, *including the reasoning for each move* — "divide both sides by 3 **because** we need x
alone," not just the next line of algebra. Any diagram is integrated directly into this example: labels on
the figure itself, numbered steps matched to numbered call-outs, color used only for signaling (never
decoration). No "why does this work?" self-explanation prompts by default — research found they don't
reliably help and can add load; use one only where a concept is genuinely subtle.

**3. One varied, lightly-scaffolded example ("Your Turn")**
Same concept, different surface numbers, with the **last step left blank** for the student to complete.
Placed immediately adjacent to the Model example — same page, never a facing page or after Vocabulary —
to avoid the split-attention cost of separating a diagram/example from its match.

**4. Common-mistake callout — conditional, not automatic**
A "wrong way → why → right way" box **only for concepts with a documented common error** (check
`04-common-student-mistakes.md` per concept). Always pair the wrong version with a correct contrast —
never show an error in isolation. Skip entirely where no well-known error exists; a mistake box on every
page dilutes the effect.

**5. Visual-to-text ratio**
A visual earns its place only if it replaces/compresses text and does real signaling work — cut anything
decorative. Optional for most algebra/arithmetic; near-mandatory and dominant for geometry, coordinate-plane,
and graph-based concepts.

**6. Sequence recap**
Definition+notation → Model example (I do) → Your-Turn example (We do, last step blank) → [conditional]
common-mistake box → Vocabulary → practice Set (You do).

---

## Part 2 — Writing Natural Uzbek (not translated Uzbek)

### The core definition pattern

Real Uzbek definitions put the **term first**, pile the description in the middle, and put the naming verb
**at the very end** — the opposite of English's early-verb order. This is the single biggest structural
tell between native and translated text.

- **`[Term] deb, [full description] -ga aytiladi.`**
  *(the term, "deb," then description, then "aytiladi" — "is called" — right at the end)*
- **`[Term] deganda, [description] tushuniladi.`**
  *("by [term], what is understood is [description]")*
- Mirror form also standard: **`[Description] [Term] deb ataladi.`** (description first, naming verb last)

### Connectors for moving between steps

Real textbook-solution Uzbek is **terse** at transition points — single-word sentence-openers, not English's
hedge-heavy "this means that..." / "it follows that...":

| Uzbek | Use for |
| --- | --- |
| **Bundan,** | "Hence / from this" — introduces the next derived step |
| **Demak,** | "So / therefore" — introduces a conclusion |
| **Shartga ko'ra,** | "According to the condition" — opens a step by anchoring to given data |
| **Bunda,** | "In this case / here" — adds a clarifying consequence right after a rule |

### Condition ordering

English states the condition first ("If X, then Y is called Z"). Natural Uzbek trails it:
**`[main defining clause], agar [condition] bo'lsa/bajarilsa.`** A translation that keeps English's
if-first order throughout reads subtly foreign even when grammatically correct.

### What to stop doing (translation tells)

1. **Verb-medial sentences mimicking English** — e.g. "Kvadrat tenglama — bu ... ko'rinishdagi tenglamadir"
   (predicate-noun placed early, English-style) instead of deferring "deb ataladi" to the end.
2. **Overusing "Bu..." as a dummy subject** — "Bu shuni anglatadiki...", "Bu bizga beradi..." sentence after
   sentence, mimicking English "This is.../This means...". Fold that meaning into a connector (bundan, demak)
   or a participial clause instead.
3. **Stacking English-style passives** — Uzbek passive ("-iladi"/"-ladi": hisoblanadi, aniqlanadi, beriladi)
   is normal and fine *individually*; the tell is chaining several in a row where a native writer would
   switch to active ("biz topamiz") or a connector-led step ("bundan ... kelib chiqadi").
4. **Inventing vocabulary instead of using settled terms** — e.g. calquing "counterexample" literally
   instead of using the attested native compound **"teskari misol"**; calquing "domain" instead of the
   settled **"aniqlanish sohasi."** Loanwords themselves (funksiya, grafik, koordinata, teorema) are correct
   and expected — the error is inventing new terms where Uzbek has already settled on one.
5. **Literal hedge translation** — rendering "it turns out that," "notice that" character-for-character
   every time instead of using a terse native connector or dropping the hedge entirely.
6. **Full-sentence headings** — found textbook chapter headings are short noun phrases ("I bob. ALGEBRAIK
   IFODALAR"), not full sentences or gerund phrases ("Tenglamalarni yechish haqida" reads as a translated
   heading style).

### Illustrative before/after

Not a quote from the current book — a template showing the pattern applied to a generic definition:

> **Before (translation tells):** "Kvadrat tenglama bu x² + bx + c = 0 ko'rinishidagi tenglama hisoblanadi.
> Bu tenglamani yechish uchun biz formuladan foydalanamiz."
>
> **After (native pattern):** "x² + bx + c = 0 ko'rinishidagi tenglama **kvadrat tenglama deb ataladi.**
> Uni yechish uchun quyidagi formuladan foydalaniladi."

The term-first/verb-last structure replaces the early "bu...hisoblanadi," and the second sentence drops the
"Bu...biz" opener for a direct process statement.

### Open question — register

Every confirmed source is formal/academic Uzbek. No source confirms a looser, second-person "teaching
voice" (direct address, "Keling, ko'raylik" — "let's look") for math specifically — informal tutoring
content online skews more conversational and code-mixed, but wasn't directly quotable this pass. **If the
series wants a warmer tone than strict textbook-formal, that's a deliberate stylistic choice to make and
sanity-check with a native speaker/editor, not something this research can hand you pre-verified.**

---

## Part 3 — Quick Checklist

Before finishing a Concepts page, check:

- [ ] Definition uses term-first, verb-last structure (deb...aytiladi / deganda...tushuniladi) — not an
      early "bu...hisoblanadi"
- [ ] No sentence-after-sentence "Bu..." openers
- [ ] Step transitions use terse native connectors (bundan, demak, shartga ko'ra, bunda), not translated
      hedges
- [ ] Conditions trail the main clause ("..., agar ... bo'lsa"), not English if-first order
- [ ] Terminology uses settled loanwords/native compounds, nothing invented
- [ ] Heading is a short noun phrase, not a full sentence
- [ ] Page follows Definition → Model example (fully reasoned) → Your-Turn (last step blank) → [conditional]
      mistake box → Vocabulary → Set
- [ ] Any diagram has labels integrated on it, not in a separate block
- [ ] Mistake box included only if `04-common-student-mistakes.md` documents a real common error for this
      concept — otherwise omit it

---

## Sources

Full research and confidence-tagged sourcing: `06-concept-explanation-pedagogy.md`,
`07-uzbek-math-language-style.md` in this same folder.
