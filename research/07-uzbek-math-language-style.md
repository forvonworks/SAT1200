# Uzbek Math Language Style: Writing Like a Native Textbook, Not a Translation

Research notes for a 3-book bilingual (Uzbek/English) SAT Math prep series. Goal: characterize how **genuine, natively-written Uzbek math-educational prose** phrases things, so the existing "Concepts" pages (which currently read like direct Google Translate output) can be rewritten in natural register.

**Methodology and honesty note (read this first):** I do not have direct browser/fetch access to Uzbek websites in this environment — `WebFetch` and direct `curl` to `.uz` domains (infoedu.uz, n.ziyouz.com, uz.wikipedia.org) were both blocked (DNS/proxy policy denial on this host). What I *do* have is a web-search tool whose backend fetches and summarizes pages I cannot reach directly, and in several cases it returned **verbatim quoted Uzbek sentences** from real sources (Uzbek university lecture PDFs, an Uzbek pedagogical-glossary PDF, an Uzbek academic-journal article, and Ministry-approved textbook table-of-contents pages). Those verbatim quotes are the strongest evidence here and are marked **[found-in-source]** with their origin. Where I could only get a search engine's paraphrased *description* of a source's content (not an exact quote), I mark it **[paraphrase-of-source]** — treat the paraphrase as directionally reliable but not safe to quote word-for-word. Where no source material was available at all and I'm extrapolating from general knowledge of Uzbek grammar/register, I mark it **[reasoned-from-general-Uzbek-grammar]**. I was **not able** to retrieve full running prose from a K-12 textbook page (e.g., a full "ta'rif" + worked example as it appears printed in the Alimov Algebra 9-sinf book) — only its front matter, table of contents, and search-engine-surfaced fragments from other academic sources that use the same genre conventions. This is a real gap; it should not be papered over with invented example sentences.

---

## 1. How Uzbek math texts phrase a definition (ta'rif), and typical sentence structure

**Confidence: found-in-source for structure/pattern; the specific sentences below are real quotes from Uzbek academic/pedagogical sources (university lecture notes, a teaching glossary, an academic paper), not from a K-12 textbook specifically, since I could not retrieve K-12 running prose directly.**

The clearest, most repeated structural pattern across every Uzbek-language math source I could access is: **the term-to-be-defined comes first in the sentence, marked with "deb," and the verb that actually means "is called" comes at the very end of the sentence** — the opposite of English's "An X is a Y that..." order, which puts the defining predicate first and the "is called X" part nowhere, or at the end as an afterthought.

**[found-in-source]**, from an Uzbek university lecture/methodical-guide PDF (staff.tiiame.uz, matrix-algebra lecture) defining the sum of two matrices:
> "A=(aᵢⱼ) va B=(bᵢⱼ) matritsalarning yig'indisi deb, elementlari cᵢⱼ=aᵢⱼ+bᵢⱼ kabi aniqlanadigan C=A+B matritsaga aytiladi."

Structurally: *[Term being defined] + deb, [full description of what it is] + ga aytiladi.* Literally: "The sum of matrices A and B, **is called**, as the matrix C=A+B whose elements are defined as cᵢⱼ=aᵢⱼ+bᵢⱼ." Note the term sits at the *front*, the predicate-verb "aytiladi" ("is called/is said") sits at the very *end*, and everything in between is the actual mathematical content. This "deb ... aytiladi" (or its twin "deb ataladi") sandwich-with-predicate-at-the-end is the single most important structural marker of natively-written Uzbek definitions.

A second, equally real pattern uses **"deganda... tushuniladi"** ("by X is understood..."), which again defers the real sense of the sentence to the final verb:

**[found-in-source]**, from an Uzbek pedagogy-journal article (inlibrary.uz) about equations:
> "Tenglama deganda ko'pincha real hayotdagi turli amaliy masalalarning matematik ifodasi tushuniladi."
("By 'equation,' what is usually understood is the mathematical expression of various practical real-life problems.")

A third real pattern states explicitly when a definition is *withheld* at a given level — useful for understanding register at the elementary level:

**[found-in-source]**, from the same subject area (a primary-methodology paper):
> "Boshlang'ich sinf matematika kursida 'Tenglama' tushunchasining aniq ta'rifi berilmaydi."
("In the primary-school mathematics course, no precise definition of the concept 'equation' is given.")

A fourth confirmed variant, from an Uzbek matrix-algebra teaching guide (oefen.uz), puts the condition for the definition to hold in a trailing "agar ... bajarilsa" ("if ... holds") clause **after** the main defining clause, not before it as English would do ("if X, then Y is called Z"):

**[found-in-source]**:
> "B matritsalarning yig'indisi deb aytiladi va C = A + B deb belgilanadi, agar i va j indekslarning hamma qiymatlari uchun tenglik bajarilsa."
("B is called the sum of the matrices and is denoted C = A + B, if the equality holds for all values of the indices i and j.")

**General structural takeaways (reasoned-from-general-Uzbek-grammar, consistent with the found examples above):** Uzbek is an SOV (subject–object–verb) agglutinative language, so the main verb of any sentence — including the "is called" / "is defined as" verb of a definition — naturally falls at or near the sentence's end, with everything that modifies or describes the term piling up *before* the verb, often in long compound noun-phrase and participial-clause strings. A literal English-order translation that puts "is called" or "is defined as" in the *middle* of the Uzbek sentence (mimicking English's early verb placement) is a strong tell of machine/direct translation, because it breaks this head-final pattern (see Section 3).

**Register:** All examples found are from formal written/academic Uzbek — not conversational. Textbook and lecture-note Uzbek uses full literary-standard grammar (e.g., "-ladi" plain-tense endings, no contractions, formal connective adverbs), closer to a textbook's "neutral-formal" register than to spoken classroom Uzbek. I found no evidence of a looser "teaching voice" (e.g., direct address to the student, imperative-heavy phrasing like "Keling, ko'raylik" / "let's look") in the textbook-adjacent sources I could access — though Telegram/YouTube tutoring-channel material (Section 2 below) does skew more conversational and mixes in English/Russian loanwords casually, suggesting that *informal* Uzbek math-teaching register exists and is somewhat looser and more code-mixed, but I could not get verbatim quotes from it to characterize it precisely. **Flag this as a genuine open question**: if the SAT-prep book wants a warmer, second-person "teaching voice" rather than strict textbook-formal register, that specific register has not been directly evidenced here and would benefit from a native-speaker sanity check rather than extrapolation.

---

## 2. Connector words/phrases for rules, examples, and steps

**Confidence: found-in-source for the items marked so; a few common ones are marked reasoned-from-general-Uzbek-grammar because the search tool's snippets, while plausible, did not always hand back a clean standalone quote.**

From a real worked solution in the Alimov/Xolmuhamedov *Algebra 9-sinf* textbook (search-engine-extracted fragment, **[found-in-source]**, ziyouz.com PDF):

> "Shartga ko'ra x² + 4x – 5 = –9, bundan x² + 4x + 4 = 0."
("According to the condition, x² + 4x – 5 = –9, **from this/hence** x² + 4x + 4 = 0.")

> "Demak, y(2) = 7 va y(–6) = 7."
("**So/therefore,** y(2) = 7 and y(–6) = 7.")

These two single-word sentence-openers — **"bundan"** (hence, from this) and **"demak"** (so, therefore, meaning) — are the real connective workhorses for moving between steps of a derivation in an actual Uzbek textbook solution, confirmed directly from source text. They are short, placed at the very start of the clause, followed by a comma, and are *not* elaborate connective phrases — a useful corrective if the current drafts over-translate English "this means that..." or "therefore, we can conclude that..." into long, English-syntax Uzbek calques.

Additional connector/step markers, **[reasoned-from-general-Uzbek-grammar + partial source support]** (seen in fragments/paraphrase, not always as a clean full quote):
- **"Shartga ko'ra"** — "according to the condition" (confirmed in the Alimov quote above) — opens a step by referencing the given data.
- **"Bunda"** — "in this case / here," confirmed in the matrix-addition source ("Bunda yig'indi matritsa qo'shiluvchi matritsalar bilan bir xil o'lchamga ega bo'ladi" — "In this case, the sum matrix has the same size as the matrices being added.") **[found-in-source]**.
- **"Ya'ni"** — "that is / i.e." — appears in theorem-and-proof academic Uzbek writing per search-engine description of a BuxDU journal article; this matches general knowledge of Uzbek as the standard restatement/clarification connector, but I did not get a clean standalone quote, so flag as **[reasoned-from-general-Uzbek-grammar, partially source-supported]**.
- **"Masalan"** — "for example" — this is the standard, universally known Uzbek word for introducing an example in any register; I did not retrieve a dedicated math-text quote using it in this search session, so it is **[reasoned-from-general-Uzbek-grammar]** (very high confidence as general Uzbek vocabulary, but not independently re-confirmed in a fetched math source this session).
- **"Misol uchun"** — a near-synonym of "masalan," slightly more formal/explicit ("for the sake of/by way of example") — same confidence level as above.
- **"Shuningdek"** — "likewise / also" — general connective for adding a related point; **[reasoned-from-general-Uzbek-grammar]**.
- **"Xulosa qilib aytganda" / "Xulosa:"** — "to conclude / in conclusion" — general academic-Uzbek concluding phrase; **[reasoned-from-general-Uzbek-grammar]**, not independently confirmed this session in a math-specific fetched source.

**What I could not confirm:** I looked specifically for "e'tibor bering" (pay attention/note that), "bundan ko'rinadiki" (from this it is evident that), and "shuni ta'kidlash joiz" (it is worth emphasizing that) inside actual Uzbek math sources, and none of my searches surfaced a verbatim hit for these exact phrases in a math context. They are plausible, grammatically correct, commonly-taught Uzbek academic-writing connectors in general — but I'm explicitly flagging that I have **no direct source confirmation** they are the phrases a real Uzbek math textbook uses at these junctures, as opposed to some other equally valid phrasing. Do not treat them as verified textbook idiom; treat them as reasonable candidates to test with a native speaker/editor.

---

## 3. Markers that give away "translated from English" vs. natively written Uzbek

**Confidence: reasoned-from-general-Uzbek-grammar, cross-checked against the structural evidence in Section 1.** This section is necessarily more inferential since I'm diagnosing an absence (what a translation does wrong) rather than quoting a confirmed error; I'm grounding it in (a) the real native-Uzbek sentence structures found above and (b) well-established facts about Uzbek grammar (SOV word order, agglutinative suffixation, limited native passive-voice use) that any accurate grammar reference would confirm.

Likely markers of direct-translation Uzbek in a math-explanation context:

1. **Verb-medial or verb-early sentence order mimicking English.** English definitions put the "is" / "is called" near the front-middle ("A quadratic equation is an equation of the form..."). A literal translation often keeps that order in Uzbek ("Kvadrat tenglama — bu ... ko'rinishdagi tenglamadir" structured so the predicate-noun sits early). The real found-in-source Uzbek pattern instead defers the naming verb ("aytiladi"/"ataladi"/"tushuniladi") to the very end of the sentence, with the full descriptive content piled up before it (Section 1). A sentence that reads naturally in English word-for-word translated into Uzbek, verb-and-all, in the same position, is a strong tell.

2. **Overuse of "bu" as an English-style copula/dummy subject.** English math prose leans heavily on constructions like "This is...", "This means that...", "This gives us...". A direct translation tends to render every one of these as "Bu..." at the start of a Uzbek sentence. Native Uzbek math prose, per the found examples, prefers to fold that meaning into a connector adverb (bundan, demak, bunda) or a participial clause rather than a standalone "Bu" + copula sentence. Repeated "Bu ... hisoblanadi" / "Bu ... bo'ladi" openers, sentence after sentence, is a pattern-level giveaway, even though "Bu" itself is a perfectly normal word.

3. **English-pattern passive voice.** English math writing uses passive constructions a lot ("is defined as," "is given by," "is calculated as"). Uzbek has a passive voice morphologically (the -il-/-l- suffix), but natively-written Uzbek math/academic prose more often prefers the **"deb ataladi / deb aytiladi" naming-construction** (grammatically closer to an impersonal "one calls X Y" than a true passive) or the **"-iladi" general/habitual present** for *process* statements ("hisoblanadi" = "is calculated," which *is* native and fine) rather than chains of passive clauses stacked the way English does. The giveaway isn't passive voice per se (Uzbek has it and uses it, e.g. "hisoblanadi," "aniqlanadi," "beriladi" are all normal) — it's **stacking multiple English-style passives in a row** where a native writer would switch to an active "biz topamiz" (we find) or a connector-led step ("bundan ... kelib chiqadi" — from this it follows that...) instead.

4. **Loan-word overuse / wrong register of loanword vs. native Turkic term.** Uzbek math vocabulary is a real mix of Arabic-origin (fully naturalized: isbot=proof, hisob=calculation, miqdor=quantity, nisbat=ratio), Persian-origin, and Russian/international loanwords (funksiya, grafik, koordinata, modul, teorema, gipoteza — these are the **standard, correct, expected** terms; they are not "untranslated English," they're loanwords Uzbek genuinely uses). The actual translation-tell is different: using an *English-sounding* loanword where Uzbek has long settled on a Russian-derived one (or vice versa), or calquing an English idiom literally instead of using the settled loan/native term — e.g., a direct translation might render "domain" as some invented literal compound instead of the settled "aniqlanish sohasi," or render "counterexample" as a clumsy literal calque instead of the attested natural phrase **"teskari misol"** (found in an Uzbek bilingual glossary, **[found-in-source]**, rcsdk12.org Uzbek-English Integrated Algebra glossary) or "qarshi misol." The tell is *inventing* vocabulary where settled Uzbek math terminology already exists, not loanword use per se.

5. **Overly literal idiom/hedge translation.** English math prose uses soft hedges like "it turns out that," "notice that," "it can be shown that," "in other words." A direct translation often renders these character-for-character ("bu ma'noda," "shuni ta'kidlaymiz" used identically every time, mechanically, regardless of whether a native writer would use a single terse connector like "demak" or "bundan" instead, or skip the hedge entirely). Natural Uzbek math prose, per the found examples, is comparatively terse at transition points (single-word "Demak," / "Bundan," openers) rather than English's more hedge-heavy, qualifier-heavy academic style.

6. **Conditional/if-clause ordering.** English states the condition first: "If X, then Y is called Z." The found-in-source Uzbek example (Section 1, matrix-sum "agar ... bajarilsa") puts the condition **after** the main clause, as a trailing "agar ... -sa" subordinate clause. A translation that keeps the English if-first order throughout (instead of varying with native-typical trailing conditionals) will read subtly foreign to a native reader even though it's grammatically parseable.

7. **Title/heading style.** Found textbook chapter headings are short noun phrases in caps, not full sentences (e.g., "I bob. ALGEBRAIK IFODALAR," "II bob. BIR NOMA'LUMLI BIRINCHI DARAJALI TENGLAMALAR" — **[found-in-source]**, infoedu.uz 7-sinf algebra page). A translated heading that keeps an English full-sentence or gerund-phrase heading style ("Tenglamalarni yechish haqida" as a direct calque of "About Solving Equations" rather than the terser native noun-phrase convention) would read as translated.

---

## 4. Natural Phrasing Patterns (glossary-style)

Each entry is tagged **[found-in-source]** (an attested real sentence/fragment, safe to use as a model), **[paraphrase-of-source]** (a search engine's description of real source content, directionally reliable, not a safe verbatim quote), or **[reasoned]** (general Uzbek-grammar knowledge, not independently re-verified against a fetched math source this session — recommend a native-speaker check before locking into the book).

### Defining a term ("X deb ataladi" family)

- **[found-in-source]** Pattern: *[Term] deb, [full description] -ga aytiladi.*
  Real example: "A=(aᵢⱼ) va B=(bᵢⱼ) matritsalarning yig'indisi deb, elementlari cᵢⱼ=aᵢⱼ+bᵢⱼ kabi aniqlanadigan C=A+B matritsaga aytiladi."
- **[found-in-source]** Pattern: *[Term] deganda, [description] tushuniladi.*
  Real example: "Tenglama deganda ko'pincha real hayotdagi turli amaliy masalalarning matematik ifodasi tushuniladi."
- **[reasoned]** Equivalent, commonly-taught variant: *[Description] [Term] deb ataladi.* (description first, term-naming verb last) — the mirror image of the first pattern, also standard; not independently re-confirmed with a fresh quote this session, but consistent with the attested "deb ataladi / deb aytiladi" family and with Uzbek's head-final syntax.
- **[found-in-source]** Stating that a definition is deliberately not given at a level: "[Tushuncha]ning aniq ta'rifi berilmaydi" (no precise definition of [concept] is given) — useful if the book wants to flag "we're giving you an informal/intuitive sense here, not the full formal definition."

### Stating a condition attached to a definition/rule

- **[found-in-source]** Pattern: *[Main defining clause], agar [condition] bo'lsa / bajarilsa.* (condition trails the main clause)
  Real example: "...deb aytiladi va C = A + B deb belgilanadi, agar i va j indekslarning hamma qiymatlari uchun tenglik bajarilsa."
- **[found-in-source]** Pattern for scope restriction: "[Amal] faqat [shart] uchun kiritiladi." (The operation is only introduced/defined for [condition].)
  Real example: "Matritsalarni qo'shish va ayirish amallari bir xil o'lchamli matritsalar uchun kiritiladi."

### Moving between steps of a derivation / "this means" equivalents

- **[found-in-source]** "Bundan, [next step]." — "From this/hence, [next step]." Real example: "...x² + 4x – 5 = –9, bundan x² + 4x + 4 = 0."
- **[found-in-source]** "Demak, [conclusion]." — "So/therefore, [conclusion]." Real example: "Demak, y(2) = 7 va y(–6) = 7."
- **[found-in-source]** "Shartga ko'ra, [restating the given]." — "According to the condition/given, [...]" — used to open a step by anchoring it to the problem's stated data.
- **[found-in-source]** "Bunda, [elaboration]." — "In this case/here, [elaboration]" — used to add a clarifying consequence right after stating a rule.

### Introducing an example

- **[reasoned]** "Masalan, [example]." — "For example, [...]" — standard, extremely high-confidence general Uzbek usage; not re-confirmed with a fresh math-specific quote this session.
- **[reasoned]** "Misol uchun, [example]." — near-synonym, slightly more formal/explicit framing of "by way of example."
- **[reasoned]** "Quyida misol ko'rib chiqamiz." — "Below, we will look at an example." — plausible textbook-style lead-in to a worked example; not independently source-confirmed this session.

### Stating a rule (qoida)

- **[reasoned]** Textbooks appear to use a labeled "Qoida:" callout (inferred from a confirmed table-of-contents entry "Qavslarni ochish qoidalari" = "rules for opening brackets," **[found-in-source]** for the heading only, infoedu.uz 7-sinf algebra TOC) followed by the rule statement itself — but I could not retrieve the actual rule-statement sentence that follows such a heading, so the surrounding sentence structure for a labeled "Qoida:" box is **[reasoned]**, not confirmed.

### Terminology notes (loanword vs. native term — found-in-source)

- **[found-in-source]** "isbot" = proof (naturalized Arabic-origin loan, standard).
- **[found-in-source]** "taxmin, gipoteza" = conjecture (native Turkic "taxmin" alongside international loan "gipoteza," both attested together in the same bilingual glossary).
- **[found-in-source]** "teskari misol" = counterexample (native compound, not a Russian/English loan — a good example of settled native vocabulary that a direct translation might miss in favor of inventing a calque).
- **[paraphrase-of-source]** "aniqlanish sohasi" = domain (of a function), "qiymatlar sohasi" = range — both appear as the settled terms in an Uzbek academic-journal description of function definitions; I could not get the exact sentence using them, so treat the terms themselves as reliable but do not quote a full sentence around them as verbatim.

---

## Sources

Because direct page fetches to `.uz` domains were blocked in this environment, all of the following were accessed via a web-search tool whose backend fetched/summarized the pages; quoted sentences above came through as verbatim extracts in that tool's output, which I'm treating as reliable quotes but have not independently re-verified by opening the raw page myself.

- **infoedu.uz** — Ministry-aligned Uzbek textbook download pages by grade (1–11), including table-of-contents fragments for grade 7 and 8 algebra (e.g., "I bob. ALGEBRAIK IFODALAR," "Qavslarni ochish qoidalari"). https://infoedu.uz/darsliklar/7/7-sinf-algebra , https://infoedu.uz/darsliklar/8/8-sinf-algebra
- **n.ziyouz.com** — *Algebra. 9-sinf* (2014, Sh. Alimov, O. Xolmuhamedov, M. Mirzaahmedov), Ministry-approved textbook PDF; source of the "bundan"/"demak" worked-solution fragment. https://n.ziyouz.com/books/darsliklar/yangi/9-sinf/Algebra.%209-sinf%20(2014,%20Sh.Alimov,%20O.Xolmuhamedov).pdf
- **staff.tiiame.uz** — university lecture/presentation PDFs on matrix algebra, source of the "deb ... aytiladi" matrix-sum definition and the "agar ... bajarilsa" conditional pattern. https://staff.tiiame.uz/storage/users/185/presentations/XSQKhZVLNP8zHoQDjUPfPQKaxNQDVU5jLAdt41df.pdf (and sibling files on the same host)
- **oefen.uz** — Uzbek-language methodical/teaching-guide documents ("matrisalar uslubiy"), source of the "Bunda yig'indi matritsa..." sentence. https://oefen.uz/uz/documents/referatlar/umumiy/matrisalar-uslubiy
- **inlibrary.uz** — Uzbek academic-journal articles (education/pedagogy), source of the "Tenglama deganda..." and "aniq ta'rifi berilmaydi" sentences, and background on Al-Khwarizmi/algebra history in Uzbek academic prose. https://inlibrary.uz/index.php/zdaf/article/view/101864 (and related articles on the same host)
- **library.tuit.uz** — Tashkent State Pedagogical University (TDPU) methodological glossary of 184 algebra/mathematical-analysis terms (Yarqulov & Barakayeva, 2011) — referenced for register and terminology, not directly quoted beyond its own description of itself. https://library.tuit.uz/knigiPDF/tex/1-1072.pdf
- **rcsdk12.org** — a bilingual (English-Uzbek) "Reasoning and Proof" vocabulary glossary for an Integrated Algebra course, source of "isbot" (proof), "taxmin, gipoteza" (conjecture), "teskari misol" (counterexample). https://www.rcsdk12.org/cms/lib/NY01001156/Centricity/Domain/4194/hs_integrated_algebra_uzbek-12p.pdf
- **talimxabarlari.uz** — Uzbekistan Ministry of Preschool and School Education quarterly test-paper PDFs by grade (7–11), surfaced repeatedly as real but not deeply quoted in this session (used mainly to confirm genre/existence, not for sentence-level extraction). e.g. https://talimxabarlari.uz/wp-content/uploads/8-sinf_uzb_1.pdf
- **academy.uz** — page on Rustam Turdibayev (Uzbekistan Academy of Sciences V.I. Romanovskiy Institute of Mathematics researcher), referenced for the existence of Uzbek-language math-olympiad video content (YouTube channel "rustamt," Telegram channel @imouz) — not quoted directly; description only.
- **Telegram channel descriptions** (via third-party analytics aggregators telegramadsarchive.com / tlmtr.io, since Telegram itself was not directly reachable): @ziyoly, @math_mentor, "ma tema tika" (@ma_tema_tika) — used only to characterize that informal/tutoring-register Uzbek math content exists and mixes in English/Russian terms casually (e.g., "AI-driven," "individual math lessons"); not used for any quoted sentence-pattern evidence, since these are third-party paraphrases of channel descriptions, not the descriptions themselves.
- **Uzbek Wikipedia (uz.wikipedia.org)**: **could not be reached or retrieved** in this session — every direct URL attempt and targeted search for specific articles (Funksiya, Kvadrat tenglama, Tenglama, Natural sonlar) failed to surface actual article text. This is a notable gap; Uzbek Wikipedia math articles were explicitly requested as a source and are **not represented** in the findings above beyond a failed attempt.

**What was NOT found / explicit gaps:**
- No verbatim full running prose from a K-12 textbook's actual body text (definition + worked example as printed) — only its table of contents, front matter, and fragments surfaced via unrelated-source search hits.
- No confirmed Uzbek Wikipedia math-article text at all.
- No verbatim confirmation of several commonly-assumed connector phrases ("e'tibor bering," "bundan ko'rinadiki," "shuni ta'kidlash joiz," "masalan" in a math-specific sentence, "xulosa qilib aytganda") inside an actual fetched Uzbek math source this session — these remain plausible but unverified, and are flagged as such in Section 4.
- No direct quote of a "Qoida:" rule-statement box as it appears printed in a textbook, only confirmation that such section headings exist (e.g., "Qavslarni ochish qoidalari").
- No characterization of a looser, second-person "teaching voice" register with direct source backing (see closing paragraph of Section 1) — if the book wants that warmer register specifically (as opposed to textbook-formal), that choice is a stylistic decision not directly evidenced here and should ideally be checked against actual informal Uzbek tutoring content (YouTube video transcripts, Telegram channel posts) that this session could not access.
