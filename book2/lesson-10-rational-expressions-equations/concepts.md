# Book 2 — Lesson 10: Rational Expressions & Equations

**Source content file.** Structure follows `research/14-design-spec.md` §10
(Definition → Model → Your-turn → conditional Common Mistake → Vocabulary),
matching Book 1 Lesson 1's established pattern.

**Research grounding:** `research/01-official-sat-math-spec.md` (rational
equations named explicitly in Advanced Math's official scope — "absolute
value, quadratic, exponential, polynomial, rational, radical, and other
nonlinear equations"), `research/04-common-student-mistakes.md` (the
extraneous-solution finding for radical equations generalizes directly to
rational equations — squaring/clearing denominators is not always reversible),
plus a targeted search confirming the single most-cited error for this exact
topic: **canceling terms instead of factors**.

This lesson builds directly on two things already taught: Book 1 Lesson 2
(fraction mechanics — simplify, multiply, divide) and Book 2 Lesson 9
(factoring polynomials). The only genuinely new idea here is that fractions
with *variables* in them follow the exact same rules — but simplifying now
requires factoring first, and solving now requires tracking which values
would make a denominator zero.

---

## Concept 1 — Ratsional Ifodalarni Soddalashtirish (Simplifying Rational Expressions)

### Definition

*Surati va maxraji ko'phad bo'lgan kasr ratsional ifoda deb ataladi. Uni
soddalashtirish uchun avval surat va maxrajni to'liq ko'paytuvchilarga
ajratish, so'ngra faqat ikkalasida ham umumiy bo'lgan ko'paytuvchini
qisqartirish kerak — alohida hadlarni emas.*

<small>(A fraction whose numerator and denominator are both polynomials is
called a rational expression. To simplify one, fully factor the numerator
and denominator first, then cancel only a factor common to both — never a
bare term.)</small>

**Nima so'ralmoqda? (What is actually being asked?):** "soddalashtiring"
degani — kasrni eng kichik ko'phadlar nisbatiga keltirish, demak, javobda
hali ham surat/maxraj qoldirilgan bo'lishi mumkin; bu "x ni toping"
degani emas. Shuningdek, qisqartirilgan ko'paytuvchi maxrajni nolga
tenglashtiradigan $x$ qiymatlarini (ruxsat etilmagan qiymatlar) ifodadan
olib tashlamaydi — ular hamon ta'qiqlangan bo'lib qoladi.

### Model Example (1-misol)

$$\frac{x^2-4}{x^2+5x+6} = ?$$

**Yechish:** Surat va maxrajni ko'paytuvchilarga ajratamiz: surat
$x^2-4=(x-2)(x+2)$ (kvadratlar ayirmasi), maxraj $x^2+5x+6=(x+2)(x+3)$.
Ifoda: $\dfrac{(x-2)(x+2)}{(x+2)(x+3)}$. Ikkala qismda ham umumiy
ko'paytuvchi $(x+2)$ ni qisqartiramiz (bu — haqiqiy ko'paytuvchi, alohida
had emas, shuning uchun qisqartirish to'g'ri):

**Javob:** $\dfrac{x-2}{x+3}$, bunda $x\ne-2$ va $x\ne-3$.

### Your-Turn Example (O'zingiz bajaring)

$$\frac{x^2-9}{x^2+x-6} = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri (1):** $\dfrac{x+5}{x}$ ifodasida $x$ larni qisqartirib,
javobni $5$ deb hisoblash.

**To'g'ri:** $x$ — suratning ($x+5$) ko'paytuvchisi emas, balki uning bir
qismi (qo'shiluvchisi). Faqat butun ifodaning ko'paytuvchisi bo'lgan narsa
qisqartirilishi mumkin. $\dfrac{x+5}{x}$ allaqachon eng sodda holatda —
uni bundan buyon soddalashtirib bo'lmaydi.

**Noto'g'ri (2):** $\dfrac{x^2-4}{x+2}$ ni soddalashtirganda, barcha
hadlar "qisqarib ketgani" uchun javobni $0$ deb hisoblash.

**To'g'ri:** $\dfrac{(x-2)(x+2)}{x+2}=x-2$. Qisqartirishdan keyin qolgan
ko'paytuvchi javob bo'ladi — u hech qachon avtomatik ravishda $0$ yoki $1$
bo'lib qolmaydi; har doim nima qolganini tekshiring (masalan, koeffitsient
qolishi ham mumkin, pastdagi 2-tushunchaga qarang).

*(Research basis: "canceling terms instead of factors" and "assuming
everything cancels to zero" are the two most consistently cited errors for
this exact topic across independent test-prep and teaching sources.)*

---

## Concept 2 — Ratsional Ifodalarni Ko'paytirish va Bo'lish

### Definition

*Ratsional ifodalarni ko'paytirish — oddiy kasrlardagi kabi, suratni
suratga, maxrajni maxrajga ko'paytirish, lekin BUNDAN OLDIN har bir
ifodani ko'paytuvchilarga ajratib, qisqartirish mumkin bo'lgan joylarni
topish kerak. Bo'lish — ikkinchi kasrning teskarisiga ko'paytirish bilan
bajariladi, xuddi oddiy kasrlarda bo'lgani kabi (Book 1, Lesson 2).*

<small>(Multiplying rational expressions works like multiplying fractions
— but factor everything first. Dividing means multiplying by the
reciprocal, exactly as with numeric fractions.)</small>

### Model Example (2-misol)

$$\frac{x^2-9}{2x} \times \frac{x}{x+3} = ?$$

**Yechish:** Suratni ko'paytuvchilarga ajratamiz: $x^2-9=(x-3)(x+3)$.
Ifoda: $\dfrac{(x-3)(x+3)}{2x}\times\dfrac{x}{x+3}$. Umumiy
ko'paytuvchilarni — $(x+3)$ va $x$ — qisqartiramiz.

**Javob:** $\dfrac{x-3}{2}$

### Your-Turn Example (O'zingiz bajaring)

$$\frac{x^2-16}{x+3} \div \frac{x-4}{x+3} = \underline{\hspace{25mm}}$$

---

## Concept 3 — Ratsional Tenglamalarni Yechish va Begona Yechimlar (Extraneous Solutions)

### Definition

*Ratsional tenglamani yechish uchun barcha hadlarni umumiy maxrajga
ko'paytirib, maxrajlardan xalos bo'linadi va hosil bo'lgan oddiy
tenglama yechiladi. Lekin har bir topilgan yechim albatta DASTLABKI
tenglamaga qo'yib tekshirilishi kerak — agar u biror maxrajni nolga
aylantirsa, bu yechim begona (extraneous) deb ataladi va rad etiladi.*

<small>(To solve a rational equation, clear every denominator by
multiplying through, then solve the resulting equation — but every
candidate solution must be checked against the ORIGINAL equation. If it
makes any original denominator zero, it's an extraneous solution and must
be rejected.)</small>

**Nima so'ralmoqda? (What is actually being asked?):** savol "$x$ ni
toping" deb tursa ham, agar algebraik jarayon orqali topilgan qiymat
asl tenglamani aniqlanmagan holga keltirsa, to'g'ri javob bu qiymat
EMAS — balki "yechim yo'q" bo'lishi mumkin. Har doim oxirgi qadam
sifatida tekshiring, hatto vaqt tig'iz bo'lsa ham.

### Model Example (3-misol — begona yechim)

$$\frac{x}{x-2} + 1 = \frac{2}{x-2}$$

**Yechish:** Ikkala tomonni $(x-2)$ ga ko'paytiramiz:
$x + (x-2) = 2$. Soddalashtiramiz: $2x-2=2$, $2x=4$, $x=2$.

**Tekshirish:** Asl tenglamada maxraj $x-2$ edi. $x=2$ qo'yilsa,
maxraj $2-2=0$ bo'ladi — bu aniqlanmagan! Demak, $x=2$ — begona yechim.

**Javob:** Yechim yo'q (no solution).

### Second Model Example (4-misol — haqiqiy yechim, tafovutni ko'rsatish uchun)

$$\frac{x+2}{x-1} = 3$$

**Yechish:** Ikkala tomonni $(x-1)$ ga ko'paytiramiz: $x+2=3(x-1)=3x-3$.
$2x=5$, $x=\dfrac{5}{2}$. Tekshirish: maxraj $x-1=\frac52-1=\frac32\ne0$ —
yaroqli.

**Javob:** $x=\dfrac{5}{2}$

*(Ikkala misolni solishtiring: ko'rinishi bo'yicha bir xil jarayon, lekin
biri rad etiladi, ikkinchisi qabul qilinadi — farqni FAQAT tekshirish
orqali bilib bo'ladi, oldindan taxmin qilib bo'lmaydi.)*

### Your-Turn Example (O'zingiz bajaring)

$$\frac{x}{x+1} = \frac{4}{x+1} - 1 = \underline{\hspace{25mm}}$$

*(Bu safar yechim begona emas — tekshirib ko'ring.)*

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Maxrajlardan xalos bo'lib, $x$ ni topgandan so'ng, uni
tekshirmasdan to'g'ridan-to'g'ri javob deb yozish.

**To'g'ri:** Har doim so'nggi qadam — topilgan qiymatni ASL (maxrajli)
tenglamaga qo'yib ko'rish. Agar biror maxraj nolga aylansa, bu yechim
rad etiladi. Bu xuddi ildiz tenglamalarida ikkala tomonni kvadratga
ko'tarish qaytarilmas amal bo'lgani kabi (`research/04`) — maxrajdan xalos
bo'lish ham har doim qaytariladigan amal emas.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Rational expression | Ratsional ifoda |
| Simplify | Soddalashtirish |
| Common factor | Umumiy ko'paytuvchi |
| Excluded value | Ruxsat etilmagan qiymat |
| Extraneous solution | Begona yechim |
| Clear the denominator | Maxrajdan xalos bo'lish |
| Reciprocal | Teskari son/ifoda |

---

## Notes for the problems file (Sets 1–7)

1. Simplify by factoring + canceling factors (no equations yet).
2. Multiply/divide rational expressions.
3. Solve rational equations — no extraneous case, clean practice.
4. Solve rational equations where a candidate must be checked — includes
   both reject-the-candidate items and at least one confirm-the-candidate
   item, so students learn to actually check rather than assume every
   problem is a trap.
5. Mixed — simplify/multiply/solve together, including one "cancels to a
   constant" case (research-documented trap: students assume full
   cancellation always means 0, when a coefficient can remain).
6. Spot the error — five items targeting term-vs-factor cancellation,
   over-cancellation to zero, and skipping the extraneous-solution check.
7. Bonus/challenge — unlike-denominator combination and quadratic-after-
   clearing cases.
