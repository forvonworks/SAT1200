# Book 2 — Lesson 9: Polynomial Operations

**Source content file.** Follows the design spec pattern: Definition → Model
→ Your-turn → conditional Common Mistake → shared Vocabulary. Book 2 framing:
more rigorous than Book 1 — this lesson assumes Book 1 Lesson 5 (algebraic
expressions: like terms, distributive property) is already solid, and builds
straight into real polynomial work without re-teaching that foundation.

**Research grounding:** `research/01-official-sat-math-spec.md` (official
scope explicitly names "polynomial... equations" among tested nonlinear
content). Targeted web research confirmed the three dominant error patterns
used below: (1) flipping only the first sign when subtracting a polynomial
instead of every term's sign, (2) incomplete distribution when multiplying
binomials (skipping a cross term), (3) adding exponents instead of keeping
them unchanged when combining like terms (confusing $x^2+x^2$ with $x^2\times
x^2$). All three are independently documented across multiple sources,
including a university thesis on polynomial-simplification error patterns.

---

## Concept 1 — Ko'phadlar: Hadlar, Daraja va Qo'shish/Ayirish

### Definition

*Bir yoki bir nechta hadning yig'indisi yoki ayirmasidan iborat ifoda ko'phad
deb ataladi. Ko'phaddagi har bir hadning darajasi orasidan eng kattasi shu
ko'phadning darajasi deb ataladi. Ko'phad hadlari darajasi kamayib boruvchi
tartibda yozilsa, bu uning standart shakli deb ataladi. Bitta hadli ifoda —
bir hadli, ikki hadli ifoda — ikki hadli, uch hadli ifoda — uch hadli deb
ataladi.*

<small>(A polynomial is a sum/difference of one or more terms. Its degree is
the highest exponent among its terms. Writing terms from highest to lowest
degree is standard form. One term = monomial, two terms = binomial, three
terms = trinomial.)</small>

**Qo'shish va ayirish — Book 1 Lesson 5'dagi o'xshash hadlar qoidasi bilan bir
xil, faqat endi hadlar ko'proq va darajalar har xil.** Ayirishda **eng muhim
qoida**: ayirilayotgan ko'phadning **har bir** hadi ishorasini o'zgartirishi
kerak, faqat birinchisi emas.

### Model Example (1-misol)

$$(5x^3 - 2x + 1) - (2x^3 + 3x - 4) = ?$$

**Yechish:** Ayirishni qo'shishga aylantiramiz — ikkinchi qavs ichidagi
**har bir** hadning ishorasini o'zgartiramiz: $5x^3-2x+1-2x^3-3x+4$. Endi
o'xshash hadlarni guruhlaymiz: $(5x^3-2x^3) + (-2x-3x) + (1+4)$. Hisoblaymiz:
$3x^3 - 5x + 5$.

**Javob:** $3x^3 - 5x + 5$

### Your-Turn Example (O'zingiz bajaring)

$$(6x^2 - 3x) - (2x^2 - 3x + 5) = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Ayirishda faqat birinchi hadning ishorasini o'zgartirish —
masalan, $(x^2+3x)-(x^2-2x+5)$ ni $x^2+3x-x^2-2x+5=x+5$ deb hisoblash (faqat
birinchi had ishorasi o'zgartirildi, qolganlari o'zgarmadi).

**To'g'ri:** Qavs oldidagi minus belgisi ichidagi **barcha** hadlarga
taqsimlanadi: $x^2+3x-x^2+2x-5 = 5x-5$.

*(Ikkinchi keng tarqalgan xato — bu yerga tegishli emas, lekin eslatib
o'tish kerak: $x^2+x^2$ ni $x^4$ deb hisoblash — bu amalda darajalar
qo'shilmaydi, chunki bu qo'shish, ko'paytirish emas. To'g'ri javob: $2x^2$.)*

---

## Concept 2 — Ko'phadlarni Ko'paytirish

### Definition

*Ikki hadli ifodani boshqa ikki hadli ifodaga ko'paytirishda, birinchi
ifodaning har bir hadi ikkinchi ifodaning har bir hadiga ko'paytiriladi va
natijalar qo'shiladi. Bu usul ingliz tilida FOIL (First, Outer, Inner, Last)
deb nomlanadi — ammo hadlar soni ikkitadan ko'p bo'lsa ham, qoida bir xil:
**har bir had — har bir hadga**.*

<small>(Multiplying two binomials: every term in the first multiplies every
term in the second, then combine. "FOIL" is just a memory aid for the
two-by-two case — the real rule, every-term-by-every-term, is what scales to
bigger polynomials.)</small>

### Model Example (2-misol)

$$(x+4)(2x^2-x+3) = ?$$

**Yechish:** $x$ ni uch hadning har biriga ko'paytiramiz:
$x\times2x^2=2x^3$, $x\times(-x)=-x^2$, $x\times3=3x$. Endi $4$ ni uch
hadning har biriga ko'paytiramiz: $4\times2x^2=8x^2$, $4\times(-x)=-4x$,
$4\times3=12$. Hammasini qo'shamiz: $2x^3-x^2+3x+8x^2-4x+12$. O'xshash
hadlarni guruhlaymiz: $2x^3+(-x^2+8x^2)+(3x-4x)+12 = 2x^3+7x^2-x+12$.

**Javob:** $2x^3+7x^2-x+12$

### Your-Turn Example (O'zingiz bajaring)

$$(x-6)(x-6) = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** $(x+3)(x-4)$ ni hisoblashda faqat birinchi va oxirgi hadlarni
ko'paytirib, o'rtadagi ikkita hadni ("outer" va "inner" ko'paytmalarni)
unutish — natijada $x^2-12$ kabi noto'liq javob chiqadi.

**To'g'ri:** Barcha to'rtta ko'paytma hisoblanishi kerak:
$x\times x + x\times(-4) + 3\times x + 3\times(-4) = x^2-4x+3x-12 = x^2-x-12$.

---

## Concept 3 — Ko'phadlarni Bo'lish

### Definition

*Ko'phadni bir hadli songa bo'lishda, ko'phadning har bir hadi alohida shu
songa bo'linadi. Ko'phadni ikki hadli ifodaga bo'lish esa oddiy sonlarni
ustunlab bo'lishga o'xshaydi: natija (bo'linma) va, ba'zan, qoldiq hosil
bo'ladi. Qoldiq nolga teng bo'lsa, bo'luvchi ko'phadning ko'paytuvchisi
hisoblanadi.*

<small>(Dividing by a monomial: divide each term separately. Dividing by a
binomial works like long division with numbers — you get a quotient and
sometimes a remainder; a zero remainder means the divisor is a factor.)</small>

**Nima so'ralmoqda?** Savolda "bo'linma"mi yoki "qoldiq"mi, yoki ikkalasi
ham so'ralayotganini aniq o'qing — ko'pincha faqat bo'linma kerak bo'ladi,
lekin savol qoldiqni alohida so'rashi ham mumkin.

### Model Example (3-misol)

$$(x^2+5x+6) \div (x+2) = ?$$

**Yechish:** Ustunlab bo'lish: $x^2 \div x = x$ — bu bo'linmaning birinchi
hadi. $x\times(x+2) = x^2+2x$. Ayiramiz: $(x^2+5x+6)-(x^2+2x) = 3x+6$. Endi
$3x\div x=3$ — bo'linmaning keyingi hadi. $3\times(x+2)=3x+6$. Ayiramiz:
$(3x+6)-(3x+6)=0$. Qoldiq $0$ ga teng, demak $(x+2)$ bu ko'phadning
ko'paytuvchisi.

**Javob:** $x+3$ (qoldiqsiz)

### Your-Turn Example (O'zingiz bajaring)

$$(8x^2+12x) \div 4x = \underline{\hspace{25mm}}$$

### Vocabulary

| English | O'zbekcha |
|---|---|
| Polynomial | Ko'phad |
| Term / Degree | Had / Daraja |
| Standard form | Standart shakl |
| Monomial / Binomial / Trinomial | Bir hadli / Ikki hadli / Uch hadli |
| Quotient / Remainder / Divisor | Bo'linma / Qoldiq / Bo'luvchi |
| Expand | Yoyish |

---

## Notes for the problems file (Sets 1–7)

1. Add/subtract drill (6) — the subtraction-sign trap is the headline skill.
2. Multiply binomials, FOIL (6).
3. Harder multiply — squares, binomial×trinomial, three-factor products (6).
4. Division — by monomial, then clean binomial division with zero remainder (6).
5. Mixed — combine add/subtract/multiply in one problem, closer to real
   test density (6).
6. Spot the error — 5 items, each naming one of the three documented
   misconceptions above (subtraction sign, incomplete FOIL, exponent
   addition) plus one division-specific slip (dividing only one term).
7. Bonus/challenge — three-factor products, division with a non-monomial
   quotient term, difference-of-squares-by-expansion pattern recognition (5).
