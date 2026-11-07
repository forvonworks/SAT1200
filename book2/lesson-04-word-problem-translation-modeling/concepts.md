# Book 2 — Lesson 4: Word-Problem Translation & Modeling

**Source content file.** Follows the same content-block pattern as Book 1
(`research/14-design-spec.md` §6: Definition → Model example → Your-turn →
conditional Common Mistake → Vocabulary). Book 2 goes beyond Book 1's bare
fundamentals — this lesson is Book 2's clearest case of that, because the
skill it teaches (translation) barely exists as a named skill in most prep
books at all.

**Research grounding — why this lesson exists and is shaped the way it is:**
`research/04-common-student-mistakes.md` cites a 2022 study of Philippine
(English-language-learner) students solving word problems: the most common
error type was "encoding errors" — mistranslating the word problem into a
mathematical expression — and the most frequently cited underlying cause was
simply not understanding the English used, not an inability to do the
algebra once the setup was correct. `research/05-uzbek-student-considerations.md`
independently confirms this for an L2-English population generally, and
explicitly calls out "if...then," "at least," "no more than," and passive
phrasing like "is increased by" as deserving their own mini-lesson treatment
— exactly what this lesson is. **Conclusion for this lesson: translation is
taught here as its own explicit skill, separate from and before the algebra
needed to solve what gets translated.** A student who can solve 3x+5=17 in
their sleep but can't produce that equation from "five more than three times
a number is seventeen" has not actually failed at algebra — Book 1 already
proved they can do the algebra. They've failed at a different, nameable
skill, and that skill gets its own lesson here rather than being assumed.

---

## Concept 1 — The Phrase-to-Symbol Dictionary

### Definition

*Og'zaki ifodalangan matematik munosabatni belgilar va amallar yordamida
yozish jarayoni so'zlarni tenglamaga tarjima qilish deb ataladi.*

<small>(The process of writing a verbally-stated mathematical relationship
using symbols and operations is called translating words into an equation.)</small>

**Why this gets its own lesson, not a side note:** every SAT algebra word
problem is really two separate tasks stacked on top of each other —
translate, then solve. Book 1 already taught "solve." This lesson teaches
"translate" as its own skill, with its own vocabulary, its own common traps,
and its own practice (Set 1 below asks you to translate *without* solving,
on purpose — so the skill can be checked on its own, not hidden inside a
final numeric answer).

### Quick reference table

| English phrase | Belgi | O'zbekcha |
|---|---|---|
| sum, total, increased by, more than *(added after)* | $+$ | yig'indi, ortiq, ko'paygan |
| difference, decreased by, less than *(see Concept 2 — order reverses)* | $-$ | ayirma, kamaygan |
| product, times, twice, double | $\times$ | ko'paytma, baravar |
| quotient, divided by, per | $\div$ or $\dfrac{a}{b}$ | bo'linma |
| is, was, equals, results in, gives | $=$ | teng, bo'ladi |
| a number *(unknown quantity)* | $x$, $n$, etc. | bir son, noma'lum son |

*(No model/your-turn pair here — this table is the reference itself; Concept
2 immediately puts the one genuinely tricky row — "less than" — under its
own spotlight.)*

---

## Concept 2 — The Reverse-Order Trap

### Definition

*"Less than" va "subtracted from" iboralari ingliz tilida yozilish tartibini
teskarisiga aylantiradi: gapda avval ayiriladigan miqdor aytiladi, lekin
ifodada u songdan keyin, ayiruvchi sifatida yoziladi.*

<small>(The phrases "less than" and "subtracted from" reverse English's
normal left-to-right order: the amount being subtracted is named *first* in
the sentence, but it's written *second* — as the thing being subtracted —
in the expression.)</small>

**The trap, stated plainly:** "Eight less than a number $n$" does **not**
mean $8-n$, even though "eight" is the first word. It means $n-8$ — take the
number, then subtract eight from it. The same reversal happens with
"subtracted from": "six subtracted from a number $y$" means $y-6$, not $6-y$.

**A note that works in this book's favor:** Uzbek's own phrasing for this
same relationship — "$n$ dan 8 kam" (literally "8 less *from* $n$") —
already puts the number first and the subtracted amount second, matching
the correct math order. Students don't need to fight their own language
here; they need to stop reading the English sentence strictly left to right
and instead map it onto the Uzbek structure they already use correctly.

**A second, separate trap hiding in the same words:** "less than" and "more
than" mean something completely different when they're comparing two
things instead of combining them. "5 more than $x$" is addition ($x+5$).
"$x$ is more than 5" is a comparison ($x>5$) — no addition at all. Same
words, opposite grammatical role. Concept 3 below covers this comparison
use directly.

### Model Example (1-misol)

Tarjima qiling: "Eight less than a number $n$."

**Yechish:** "Less than" so'zi tartibni teskarisiga aylantiradi — gapda
birinchi aytilgan miqdor ($8$) ifodada *ikkinchi* o'rinda, ayiriluvchi
sifatida yoziladi. Avval son ($n$) yoziladi, keyin undan $8$ ayiriladi.

**Javob:** $n - 8$ *(emas $8 - n$)*

### Your-Turn Example (O'zingiz bajaring)

Tarjima qiling: "Twelve less than a number $y$."

$\underline{\hspace{30mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Gapni chapdan o'ngga, so'zma-so'z o'qib, birinchi
uchragan sonni birinchi yozish — "eight less than a number $n$" ni
$8-n$ deb tarjima qilish.

**To'g'ri qoida:** "Less than" va "subtracted from" iboralarida miqdorlar
tartibi teskari bo'ladi. Tekshirish usuli: gapni "[son] dan [miqdor] kam"
shaklida qayta tuzib ko'ring — bu shakl to'g'ri tartibni ko'rsatadi.
"Eight less than $n$" → "$n$ dan sakkiz kam" → $n-8$.

*(Research basis: this exact reversal is the single most commonly cited
word-problem translation trap in algebra-pedagogy sources — see the targeted
research pass for this lesson. It is distinct from, and compounds with, the
general L2-comprehension finding in `research/04`.)*

---

## Concept 3 — Comparison Words: Inequality Phrases

### Definition

*Ikki miqdorni taqqoslash uchun ishlatiladigan iboralar tengsizlik
belgilariga mos keladi: ular qo'shish yoki ayirishni emas, balki
nisbatni bildiradi.*

<small>(Phrases that compare two quantities map to inequality symbols — they
signal a relationship, not an operation to perform.)</small>

| English phrase | Belgi |
|---|---|
| at least, no less than | $\geq$ |
| no more than, at most | $\leq$ |
| more than *(comparison, no "by" amount attached)* | $>$ |
| less than, fewer than *(comparison)* | $<$ |

**The pair that looks identical but isn't:** "A number increased by 5 is at
least 20" → $x+5 \geq 20$ (addition, *then* a comparison). "A number is at
least 20" → $x \geq 20$ (comparison only, nothing added). Read for *whether
an amount is being combined with the number* before reaching for a symbol —
don't pattern-match on the word "least" alone.

*(No model/your-turn pair here — Set 5 in the problems file is dedicated
practice for this concept specifically.)*

---

## Concept 4 — Translating and Solving a Full Word Problem

### Definition

*Bir nechta gapdan iborat masalani yechishda, avval har bir ma'lumotni
alohida-alohida belgilarga o'tkazish, so'ngra ularni bitta tenglamaga
birlashtirish kerak.*

<small>(Solving a multi-sentence word problem means translating each piece
of given information separately first, then combining them into one
equation.)</small>

**The step this lesson adds on top of Concepts 1-3:** a real word problem is
rarely one clean sentence — it's two or three sentences that each contribute
one piece, plus a final question that names exactly what to solve for. The
**last sentence is almost always the actual question** — and research
(`research/04`) confirms that solving for the wrong quantity (an
intermediate value instead of what was actually asked) is one of the most
common SAT word-problem errors, by design: wrong-answer choices are often
built specifically to match the value you'd get by stopping one step early.
**Always re-read the final question before writing down a final answer.**

### Model Example (2-misol)

"A rectangle's length is 3 more than twice its width. The perimeter is 36.
Find the **width**."

**Yechish:** Avval berilganlarni belgilaymiz: eni — $w$. Bo'yi ikki marta
eniga teng, ustiga 3 qo'shilgan: bo'yi $= 2w+3$. Perimetr formulasi:
$2(\text{bo'yi}+\text{eni})=36$. Qo'yib chiqamiz: $2((2w+3)+w)=36$. Qavs
ichini soddalashtiramiz: $2(3w+3)=36$, ya'ni $6w+6=36$. Ikkala tomondan $6$
ni ayiramiz: $6w=30$. $6$ ga bo'lamiz: $w=5$.

**Savolni qayta tekshirish:** masala **eni**ni so'ragan — bo'yini emas.
$w=5$ aynan javob beradigan narsa, shuning uchun bu yerda to'xtaymiz.

**Javob:** eni $= 5$

### Your-Turn Example (O'zingiz bajaring)

"A rectangle's length is 4 less than three times its width. The perimeter
is 56. Find the **length**."

*(E'tibor bering: bu safar savol bo'yini emas, uzunlikni so'ramoqda — avval
eni uchun tenglama tuzing, keyin uzunlikni hisoblang.)*

$\underline{\hspace{30mm}}$

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Translate (words → equation) | Tarjima qilish |
| Expression | Ifoda |
| Equation | Tenglama |
| Inequality | Tengsizlik |
| Sum / Difference / Product / Quotient | Yig'indi / Ayirma / Ko'paytma / Bo'linma |
| Increased by / Decreased by | Ko'paygan / Kamaygan |
| At least / No more than | Kamida / Ko'pi bilan |
| Consecutive integers | Ketma-ket butun sonlar |
| Perimeter | Perimetr |

---

## Notes for the problems file (Sets 1–7)

- Set 1: **Translate only, don't solve** — isolates the translation skill
  from the solving skill on purpose. Answer key gives the expression/
  equation, not a number.
- Set 2: Translate and solve, one-step equations.
- Set 3: Translate and solve, two-step equations.
- Set 4: Full multi-sentence word problems (rectangles, consecutive
  integers, age, cost, percent) — requires setting up the equation from a
  scenario, not a single templated sentence.
- Set 5: Inequality-phrase translation and solving (Concept 3).
- Set 6: Spot the error — every item is the reverse-order trap from
  Concept 2 in a different disguise.
- Set 7 (bonus/challenge): multi-step word problems combining translation,
  consecutive integers/age/cost structures, and percent — closer to the
  density of an actual hard SAT word problem.
