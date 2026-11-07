# Book 2 — Lesson 6: Quadratics II — Completing the Square & the Quadratic Formula

**Source content file.** Follows Lesson 5 (Quadratics I — factoring, zero-product
property). This lesson does not re-teach factoring — it exists for the quadratics
that *don't* factor nicely over integers, which is most of them. Book 2 is "every
SAT topic beyond the SAT's own ceiling": the quadratic formula isn't just handed
down here, it's derived, because a student who has watched it fall out of
completing the square trusts it under pressure in a way that memorization alone
doesn't survive.

**Research grounding:** `research/04-common-student-mistakes.md` is explicit that
for the quadratic formula, "most lost points come not from forgetting the formula
but from *misapplying* it" — specifically losing track of the negative on $-b$,
and arithmetic slips in the discriminant $b^2-4ac$. It also separately flags
**stopping after finding one root** as a common error (quadratics have up to two
solutions). Both are addressed directly below, not left implicit.

---

## Nima So'ralmoqda? (What Is Actually Being Asked?)

Kvadrat tenglamani yechishda ko'pincha ikkita ildiz chiqadi — savol "ildizlarni
toping" desa, ikkalasini ham yozish kerak, faqat birinchisini topib to'xtash
yetarli emas. Ba'zan savol ildizlarning o'zini emas, ularning yig'indisini yoki
ko'paytmasini so'raydi — tenglamani yechgandan keyin, savol aynan nimani
so'raganini qayta o'qing.

---

## Concept 1 — To'liq Kvadratga Keltirish (Completing the Square)

### Definition

*Kvadrat uch hadni $a(x-h)^2+k$ ko'rinishiga keltirish usuli to'liq kvadratga
keltirish deb ataladi; bu yerda $(h,k)$ parabolaning uchi (vertex) koordinatalari
hisoblanadi.*

<small>(Converting a quadratic trinomial to the form $a(x-h)^2+k$ is called
completing the square; $(h,k)$ are the coordinates of the parabola's vertex.)</small>

### Model Example (1-misol)

$y = x^2 - 6x + 5$ ni vertex shakliga keltiring.

**Yechish:** $x$ ning koeffitsientini ikkiga bo'lamiz: $-6 \div 2 = -3$. Buni
kvadratga ko'taramiz: $(-3)^2=9$. Shu $9$ ni qo'shib va ayirib, ifodani
buzmasdan to'ldiramiz: $y = (x^2-6x+9) - 9 + 5 = (x-3)^2 - 4$.

**Javob:** $y = (x-3)^2 - 4$, vertex $(3,-4)$.

### Your-Turn Example (O'zingiz bajaring)

$y = x^2 + 4x + 1$ ni vertex shakliga keltiring. $y = \underline{\hspace{30mm}}$

---

## Concept 2 — Kvadrat Formulani Keltirib Chiqarish (Deriving the Quadratic Formula)

### Definition

*Har qanday $ax^2+bx+c=0$ ($a\ne0$) ko'rinishidagi tenglamani umumiy holda
to'liq kvadratga keltirish orqali olinadigan, $x$ ni to'g'ridan-to'g'ri
ifodalovchi formula kvadrat formula deb ataladi.*

<small>(Applying completing-the-square to the general form $ax^2+bx+c=0$
produces a formula that solves for $x$ directly — the quadratic formula.)</small>

**Keltirib chiqarish (the derivation):**

Boshlang'ich tenglama: $ax^2+bx+c=0$. Ikkala tomonni $a$ ga bo'lamiz:
$x^2 + \dfrac{b}{a}x + \dfrac{c}{a} = 0$. Erkin hadni o'ng tomonga o'tkazamiz:
$x^2 + \dfrac{b}{a}x = -\dfrac{c}{a}$. Ikkala tomonga $\left(\dfrac{b}{2a}\right)^2$
ni qo'shamiz (to'liq kvadratga keltirish qadami):

$$x^2 + \dfrac{b}{a}x + \left(\dfrac{b}{2a}\right)^2 = -\dfrac{c}{a} + \left(\dfrac{b}{2a}\right)^2$$

Chap tomon endi to'liq kvadrat: $\left(x+\dfrac{b}{2a}\right)^2 = \dfrac{b^2-4ac}{4a^2}$.
Ikkala tomondan ildiz chiqaramiz (musbat va manfiy, $\pm$ bilan):

$$x + \dfrac{b}{2a} = \pm\dfrac{\sqrt{b^2-4ac}}{2a}$$

Oxirida $\dfrac{b}{2a}$ ni o'ng tomonga o'tkazamiz:

$$x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}$$

*(Diqqat: $b^2-4ac$ ildiz ostidagi qism diskriminant deb ataladi — uning ildizlar
soniga qanday ta'sir qilishi to'liq ravishda Lesson 7 da ko'riladi; bu yerda
faqat formulaning bir qismi sifatida tanishamiz.)*

---

## Concept 3 — Kvadrat Formulani Qo'llash (Applying the Quadratic Formula)

### Definition

*Faktorlash qulay bo'lmagan (butun sonli ko'paytuvchilarga ajralmaydigan)
kvadrat tenglamalar kvadrat formula yordamida yechiladi: $a$, $b$, $c$
koeffitsientlarini aniqlab, ularni to'g'ridan-to'g'ri formulaga qo'yish kerak.*

### Model Example (2-misol)

$x^2 + 4x + 1 = 0$ tenglamasini yeching.

**Yechish:** $a=1$, $b=4$, $c=1$. Diskriminant: $b^2-4ac = 16-4=12$. Formula:
$x = \dfrac{-4 \pm \sqrt{12}}{2}$. $\sqrt{12}=2\sqrt3$ ga soddalashtiramiz:
$x = \dfrac{-4\pm2\sqrt3}{2} = -2\pm\sqrt3$.

**Javob:** $x = -2+\sqrt3$ yoki $x=-2-\sqrt3$ — **ikkala ildiz ham yoziladi.**

### Your-Turn Example (O'zingiz bajaring)

$x^2 - 2x - 2 = 0$ tenglamasini yeching. $x = \underline{\hspace{30mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** $x^2-6x+4=0$ ni yechishda, $b=-6$ ekanligini unutib,
formulaga $-b$ o'rniga $b$ ni to'g'ridan-to'g'ri qo'yish: $x = \dfrac{-6\pm\sqrt{36-16}}{2}$
(bu yerda $-b=-(-6)=6$ bo'lishi kerak edi, lekin $-6$ qo'yilgan).

**To'g'ri:** $b=-6$ bo'lgani uchun $-b = -(-6) = 6$. Diskriminant: $36-16=20$.
$x = \dfrac{6\pm\sqrt{20}}{2} = \dfrac{6\pm2\sqrt5}{2} = 3\pm\sqrt5$.

*(Research basis: `research/04` names losing track of $-b$'s sign as the
single most frequently cited error applying the quadratic formula — more
common than forgetting the formula itself. The second, equally real error:
stopping after finding one root. A quadratic can have up to two solutions —
unless the question explicitly asks for only one, write both.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Completing the square | To'liq kvadratga keltirish |
| Vertex form | Vertex (uchi) shakli |
| Quadratic formula | Kvadrat formula |
| Discriminant | Diskriminant |
| Root / solution | Ildiz / yechim |

---

## Notes for the problems file (Sets 1–7)

1. Complete the square → vertex form (clean integer vertices).
2. Quadratic formula drill, clean/perfect-square discriminants (builds trust in the formula before irrational answers show up).
3. Quadratic formula, genuinely irrational roots.
4. Mixed — student chooses technique.
5. Two-root verification — find both roots, substitute back to confirm both equal zero (directly targets the "stopping after one root" error).
6. Spot the error — targets the $-b$ sign trap and incomplete answers.
7. Bonus/challenge — $a\ne1$, messier coefficients, still exact answers.
