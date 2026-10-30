# Book 1 — Lesson 5: Algebraic Expressions

**Source content file.** This is the authored content, not the final page — it gets
typeset against `research/14-design-spec.md`. Structure follows that spec's
content-block pattern exactly (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary, repeated per concept on this lesson.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` and
`research/04-common-student-mistakes.md` both name **sign errors distributing
a negative** as the single most frequently cited careless-error category
across independent sources (RevisionDojo, OnePrep, Mathnasium), with roots
traced back to exactly this stage — simplifying expressions — rather than to
later equation-solving. This lesson is pre-equation-solving: Lesson 6 covers
*solving for a variable*; this lesson only covers *rewriting an expression in
an equivalent, simpler form*. No equals-sign-balancing here.

---

## Concept 1 — O'zgaruvchilar, Hadlar va Koeffitsientlar

### Definition

*Qiymati turlicha bo'lishi mumkin bo'lgan va harf bilan belgilanadigan miqdor
o'zgaruvchi deb ataladi. Ifodani tashkil etuvchi, qo'shish yoki ayirish
belgilari bilan ajratilgan har bir qism had deb ataladi. Haddagi o'zgaruvchi
oldidagi sonli ko'paytuvchi esa koeffitsient deb ataladi; faqat sondan iborat
had erkin had deb ataladi.*

<small>(A quantity that can take different values, represented by a letter,
is called a variable. Each part of an expression separated by a + or − sign
is called a term. The numerical factor in front of a term's variable is
called its coefficient; a term that is just a number is called a constant
term.)</small>

**Why this matters for the SAT:** nearly every Algebra and Advanced Math
question is written using this vocabulary in its explanation/rationale text
("the coefficient of x," "the constant term") — recognizing the parts of an
expression by name, instantly, is a prerequisite for reading any worked
solution, not just writing one.

### Quick reference

In the expression $5x - 3y + 7$:

| Part | Nomi (Name) | English |
|---|---|---|
| $5x$ | had, koeffitsienti $5$ | term, coefficient $5$ |
| $-3y$ | had, koeffitsienti $-3$ | term, coefficient $-3$ |
| $7$ | erkin had | constant term |

*(No model/your-turn pair here — this is a naming/fluency check, not new
material. Moving to the real content.)*

---

## Concept 2 — O'xshash Hadlar va Ularni Ixchamlash

### Definition

*Bir xil o'zgaruvchiga va bir xil darajaga ega bo'lgan hadlar o'xshash hadlar
deb ataladi. O'xshash hadlarni ixchamlashda ularning koeffitsientlari
qo'shiladi (yoki ayiriladi), o'zgaruvchi qismi esa o'zgarishsiz qoladi.*

<small>(Terms with the same variable raised to the same power are called
like terms. To combine like terms, add or subtract their coefficients — the
variable part itself never changes.)</small>

### Model Example (1-misol)

$$4x + 3y - x + 7 = ?$$

**Yechish:** Ifodada ikkita $x$ li had bor: $4x$ va $-x$. Ularning
koeffitsientlari qo'shiladi: $4 - 1 = 3$, ya'ni $3x$. $3y$ va $7$ hadlariga
o'xshash boshqa had yo'q, shuning uchun ular o'zgarishsiz qoladi.

**Javob:** $3x + 3y + 7$

### Your-Turn Example (O'zingiz bajaring)

$$5a + 2b - 3a + b = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Faqat o'zgaruvchisi bir xil bo'lgan, ammo darajasi
har xil bo'lgan hadlarni ham o'xshash deb hisoblab, ularni qo'shib yuborish —
masalan, $4x + 3x^2$ ni $7x^2$ yoki $7x$ deb soddalashtirish.

**To'g'ri qoida:** $x$ va $x^2$ — bir xil o'zgaruvchi bo'lsa-da, darajasi har
xil bo'lgani uchun o'xshash had emas. Ularni faqat shunday qoldirish kerak:
$4x + 3x^2$ allaqachon eng sodda ko'rinishda — bu yerda qo'shib
bo'lmaydigan ikki had bor.

*(Research basis: "equivalent algebraic expressions" is explicitly flagged
as testing "structure recognition" — correctly identifying which parts of an
expression can and cannot be combined — see `research/04`.)*

---

## Concept 3 — Ko'paytirishning Qo'shishga Nisbatan Taqsimot Xossasi

### Definition

*$a(b+c) = ab + ac$ ko'rinishidagi tenglik ko'paytirishning qo'shish
(yoki ayirish) amaliga nisbatan taqsimot xossasi deb ataladi: qavs oldidagi
ko'paytuvchi qavs ichidagi har bir hadga alohida ko'paytiriladi.*

<small>(The equality a(b+c) = ab + ac is called the distributive property:
the factor outside the parentheses is multiplied by each term inside the
parentheses separately.)</small>

### Model Example (1-misol)

$$3(2x - 5) = ?$$

**Yechish:** Qavs oldidagi $3$ qavs ichidagi har bir hadga alohida
ko'paytiriladi: $3 \times 2x = 6x$ va $3 \times (-5) = -15$.

**Javob:** $6x - 15$

### Your-Turn Example (O'zingiz bajaring)

$$4(3x - 2) = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Qavs oldida manfiy ishora bo'lganda, uni faqat
qavsdagi birinchi hadga tatbiq etib, ikkinchi hadning ishorasini
o'zgartirmaslik — masalan, $-(3x - 5)$ ni $-3x - 5$ deb soddalashtirish.

**To'g'ri qoida:** Qavs oldidagi manfiy ishora ($-1$ ga ko'paytirish bilan
bir xil) qavs ichidagi **har bir** hadga tatbiq etiladi, shu jumladan
ikkinchi, uchinchi hadlarga ham: $-(3x - 5) = -3x + 5$, chunki
$-1 \times (-5) = +5$.

*(Research basis: sign errors distributing a negative are named as the
single most frequently cited careless-error category across multiple
independent sources — RevisionDojo, OnePrep, Mathnasium — and the
recommended fix is to rewrite the negative-distributed expression as an
explicit separate step before simplifying further. See `research/02` and
`research/04`.)*

$$-(3x - 5) \;\ne\; -3x - 5 \qquad\qquad -(3x-5) = -3x + 5$$

---

## Concept 4 — Ko'p Hadli Ifodalarni Soddalashtirish

### Definition

*Taqsimot xossasini qo'llab qavslarni ochish va so'ngra hosil bo'lgan
o'xshash hadlarni ixchamlash orqali ifodani eng sodda ko'rinishga keltirish
ifodani soddalashtirish deb ataladi.*

<small>(Opening parentheses using the distributive property and then
combining the resulting like terms, to rewrite an expression in its
simplest equivalent form, is called simplifying an expression.)</small>

### Model Example (1-misol)

$$4(x + 3) - 2(x - 1) = ?$$

**Yechish:** Avval har ikkala qavs taqsimot xossasi bilan ochiladi:
$4(x+3) = 4x + 12$ va $-2(x-1) = -2x + 2$ (manfiy ishora ikkala hadga ham
tatbiq etiladi). Ifoda: $4x + 12 - 2x + 2$. Endi o'xshash hadlar
ixchamlanadi: $4x - 2x = 2x$ va $12 + 2 = 14$.

**Javob:** $2x + 14$

### Your-Turn Example (O'zingiz bajaring)

$$5(x - 2) + 3(x + 4) = \underline{\hspace{25mm}}$$

*(No separate common-mistake box here — this concept combines the two
documented errors from Concepts 2 and 3 above; Set 5 and Set 6 in the
problems file drill exactly that combination.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Variable | O'zgaruvchi |
| Term | Had |
| Coefficient | Koeffitsient |
| Constant term | Erkin had |
| Like terms | O'xshash hadlar |
| Combine like terms | O'xshash hadlarni ixchamlash |
| Distributive property | Taqsimot xossasi |
| Expression | Ifoda |
| Simplify | Soddalashtirish |
| Equivalent | Teng kuchli (ekvivalent) |

---

## Notes for the problems file (Sets 1–7)

- Set 1: combine like terms, single operation, positive coefficients — builds
  the basic recognition habit.
- Set 2: combine like terms with subtraction/negative coefficients, including
  two items whose coefficients sum to zero (a valid, common result worth
  normalizing, not an error).
- Set 3: distributive property with a positive multiplier.
- Set 4: distributive property with a negative multiplier — the
  highest-value drill, directly targeting the documented sign-distribution
  error from Concept 3's common-mistake box.
- Set 5: mixed — distribute then combine like terms, real-test density.
- Set 6: "spot the error" format, targeting the negative-distribution error,
  the unlike-terms error, and a partial-distribution error (multiplying only
  one term in the parentheses) — the erroneous-examples technique
  `06-concept-explanation-pedagogy.md` calls appropriate for documented
  common errors.
- Set 7 (bonus/challenge): nested parentheses and two-variable expressions,
  closer to how these appear embedded inside real SAT algebra items.
