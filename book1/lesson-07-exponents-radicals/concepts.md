# Book 1 — Lesson 7: Exponents & Radicals (Basic)

**Source content file.** This is the authored content, not the final page — it
gets typeset against `research/14-design-spec.md`. Structure follows that
spec's content-block pattern (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary, repeated per concept on this lesson.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` names basic
exponent rules as a direct prerequisite for the Advanced Math domain (35% of
the real test) — without them, quadratics and exponential-growth questions in
Book 2/3 are unreachable. `research/04-common-student-mistakes.md` documents
four specific, well-sourced error patterns, three of which this lesson builds
a Common Mistake box around directly.

**Scope note — deliberately kept introductory.** Per the annotated table of
contents, advanced exponent/radical work (rational exponents, nth roots
beyond square roots, radical equations and extraneous solutions, rationalizing
denominators) is out of scope here and belongs to Book 2/3. This lesson covers
only: the core same-base exponent rules, zero/negative exponents, and
simplifying/combining basic square roots.

---

## Concept 1 — Exponent Notation & the Same-Base Rules

### Definition

*Biror $a$ sonining o'z-o'ziga $n$ marta ko'paytirilishi natijasida hosil
bo'lgan ifoda $a$ ning $n$-darajasi deb ataladi va $a^n$ ko'rinishida
yoziladi; bunda $a$ — daraja asosi, $n$ — daraja ko'rsatkichi deb ataladi.*

<small>(Multiplying a number by itself $n$ times produces its $n$th power,
written $a^n$; $a$ is called the base, $n$ the exponent.)</small>

*Bir xil asosga ega darajalarni ko'paytirishda ko'rsatkichlar qo'shiladi:
$a^m \times a^n = a^{m+n}$ deb ataladi. Bir xil asosli darajalarni bo'lishda
ko'rsatkichlar ayiriladi: $\dfrac{a^m}{a^n} = a^{m-n}$. Darajani darajaga
ko'tarishda esa ko'rsatkichlar ko'paytiriladi: $(a^m)^n = a^{mn}$.*

<small>(Multiplying same-base powers adds the exponents; dividing subtracts
them; raising a power to a power multiplies them.)</small>

**Why this matters for the SAT:** every Advanced Math question involving
exponential growth/decay, polynomial simplification, or rational expressions
assumes these three rules are automatic — none of them are re-taught on the
real test.

### Model Example (1-misol)

$$(2^3 \times 2^4)^2 \div 2^5 = ?$$

**Yechish:** Avval qavs ichidagi ko'paytirish bajariladi, bir xil asos
bo'lgani uchun ko'rsatkichlar qo'shiladi: $2^3 \times 2^4 = 2^{3+4} = 2^7$.
Ifoda: $(2^7)^2 \div 2^5$.

Daraja darajaga ko'tarilganda, ko'rsatkichlar ko'paytiriladi: $(2^7)^2 =
2^{7 \times 2} = 2^{14}$. Ifoda: $2^{14} \div 2^5$.

Bir xil asosli darajalarni bo'lishda ko'rsatkichlar ayiriladi: $2^{14} \div
2^5 = 2^{14-5} = 2^9$.

$2^9 = 512$.

**Javob:** $512$

### Your-Turn Example (O'zingiz bajaring)

$$(3^2 \times 3^3)^2 \div 3^4 = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** $a^p \times a^p$ (ko'paytirish — ko'rsatkichlar
qo'shiladi) bilan $(a^p)^p$ (darajani darajaga ko'tarish — ko'rsatkichlar
ko'paytiriladi) orasidagi farqni chalkashtirib yuborish.

**To'g'ri qoida:** $2^3 \times 2^3 = 2^{3+3} = 2^6 = 64$ (qo'shiladi), biroq
$(2^3)^3 = 2^{3 \times 3} = 2^9 = 512$ (ko'paytiriladi) — bu ikkisi butunlay
boshqa ifodalar va boshqa natija beradi, garchi ko'rinishi o'xshash bo'lsa
ham.

*(Research basis: documented as a specific, named confusion between the
product rule and the power-of-a-power rule — see `research/04`, Exponents &
Radicals section.)*

---

## Concept 2 — Zero and Negative Exponents

### Definition

*Istalgan nolmas $a$ soni uchun, uning nolinchi darajasi har doim $1$ ga
teng: $a^0 = 1$ deb ataladi. Manfiy ko'rsatkichli daraja esa mos musbat
ko'rsatkichli darajaning teskari sonini bildiradi: $a^{-n} = \dfrac{1}{a^n}$
deb ataladi.*

<small>(For any nonzero $a$: $a^0 = 1$. A negative exponent means the
reciprocal of the corresponding positive power: $a^{-n} = \frac{1}{a^n}$.)</small>

### Model Example (2-misol)

$$5^0 + 2^{-3} \times 4^2 = ?$$

**Yechish:** Istalgan nolmas sonning nolinchi darajasi $1$ ga teng: $5^0 = 1$.

Manfiy daraja teskari sonni bildiradi: $2^{-3} = \dfrac{1}{2^3} =
\dfrac{1}{8}$.

Ifoda: $1 + \dfrac{1}{8} \times 16$. Avval ko'paytirish bajariladi:
$\dfrac{1}{8} \times 16 = 2$.

Oxirida: $1 + 2 = 3$.

**Javob:** $3$

### Your-Turn Example (O'zingiz bajaring)

$$3^0 + 2^{-2} \times 2^4 = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Manfiy ko'rsatkichni asosni manfiy qiladi deb
o'ylash.

**To'g'ri qoida:** $2^{-3}$ ni $-8$ deb hisoblash — noto'g'ri. Manfiy
ko'rsatkich asosni manfiy qilmaydi, balki natijani teskari songa (kasrga)
aylantiradi: $2^{-3} = \dfrac{1}{2^3} = \dfrac{1}{8}$.

*(Research basis: documented as a specific, named misconception — students
treat the negative sign as applying to the base's value rather than to the
operation of taking a reciprocal. See `research/04`.)*

---

## Concept 3 — Simplifying Simple Square Roots

### Definition

*Kvadratga ko'tarilganda $a$ sonini beradigan manfiy bo'lmagan son $a$ ning
kvadrat ildizi deb ataladi va $\sqrt{a}$ ko'rinishida belgilanadi. Kvadrat
ildiz ostidagi sonni soddalashtirish uchun, uning tarkibidagi eng katta
to'liq kvadrat ko'paytuvchisi ajratib olinadi: $\sqrt{ab} = \sqrt{a} \times
\sqrt{b}$ ($a, b \geq 0$) qoidasidan foydalaniladi.*

<small>(The non-negative number that gives $a$ when squared is the square
root of $a$, written $\sqrt{a}$. To simplify, factor out the largest
perfect-square factor using $\sqrt{ab} = \sqrt{a} \times \sqrt{b}$.)</small>

### Model Example (3-misol)

$$\sqrt{72} = ?$$

**Yechish:** $72$ ning tarkibidagi eng katta to'liq kvadrat ko'paytuvchisi
topiladi: $72 = 36 \times 2$, va $36$ — to'liq kvadrat ($6^2 = 36$).

$\sqrt{72} = \sqrt{36 \times 2} = \sqrt{36} \times \sqrt{2} = 6\sqrt{2}$.

**Javob:** $6\sqrt{2}$

### Your-Turn Example (O'zingiz bajaring)

$$\sqrt{50} = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Yig'indining kvadrat ildizini har bir qo'shiluvchining
alohida kvadrat ildizlari yig'indisiga teng deb hisoblash.

**To'g'ri qoida:** $\sqrt{a+b} \neq \sqrt{a} + \sqrt{b}$ — bu tenglik
hamma vaqt noto'g'ri (nolmas $a, b$ uchun). Masalan: $\sqrt{16+9} =
\sqrt{25} = 5$, biroq $\sqrt{16} + \sqrt{9} = 4 + 3 = 7$ — bu ikki natija
teng emas.

*(Research basis: the classic $\sqrt{a+b} \ne \sqrt{a}+\sqrt{b}$ error,
documented as applied by students despite being false for all nonzero
$a,b$. See `research/04`.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Exponent / Power | Daraja |
| Base | Asos |
| Exponent (index) | Ko'rsatkich |
| Zero exponent | Nol darajasi |
| Negative exponent | Manfiy daraja |
| Reciprocal | Teskari son |
| Square root | Kvadrat ildiz |
| Perfect square | To'liq kvadrat |

---

## Notes for the problems file (Sets 1–7)

- Set 1: pure same-base exponent rule drills (product/quotient/power rules),
  no negatives or zero exponents yet — includes a deliberate paired item
  ($2^3\times2^3$ vs. $(2^3)^3$) echoing Concept 1's common-mistake contrast.
- Set 2: zero and negative exponents as given values to evaluate, building
  the reciprocal habit directly.
- Set 3: mixed — all three rules plus zero/negative exponents combined,
  closer to real test density.
- Set 4: simplifying square roots (perfect-square factoring) drill.
- Set 5: combining like radicals after simplifying (addition/subtraction/
  multiplication of radicals) — still basic, no rationalizing denominators.
- Set 6: "spot the error" format — five items, each targeting one of the
  three documented misconceptions above (erroneous-examples technique, per
  `06-concept-explanation-pedagogy.md`).
- Set 7 (bonus/challenge): exponents and radicals combined in one expression,
  timed.
