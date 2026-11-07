# Book 2 — Lesson 7: Quadratic Graphs & the Discriminant

**Source content file.** Follows Lesson 5 (factoring, zero-product property) and
Lesson 6 (completing the square, vertex form, the quadratic formula — already
derived there, including $b^2-4ac$ as the piece under the radical). This lesson
does **not** re-derive the formula — it connects the algebra you already have to
the graph, and gives the discriminant its own dedicated job: predicting *how
many* real solutions an equation has before you solve it.

Research grounding: `research/01-official-sat-math-spec.md` (Advanced Math
domain), `research/04-common-student-mistakes.md`. Book 2 lessons run more
rigorously than Book 1 per the series design — this lesson assumes full comfort
with vertex form and the quadratic formula from Lesson 6.

---

## Concept 1 — Parabolaning Tuzilishi (Parabola Anatomy)

### Definition

*Kvadrat funksiyaning grafigi parabola deb ataladi. Parabolaning eng past
yoki eng baland nuqtasi uning cho'qqisi (vertex) deb ataladi, va parabola shu
nuqtadan o'tuvchi vertikal chiziqqa nisbatan simmetrik joylashadi — bu chiziq
simmetriya o'qi deb ataladi.*

<small>(A quadratic function's graph is a parabola. Its highest or lowest
point is called the vertex, and the parabola is symmetric about the vertical
line through that point — the axis of symmetry.)</small>

**Vertex form bilan o'qish:** $y=a(x-h)^2+k$ ko'rinishida (Lesson 6'dan
tanish), cho'qqi to'g'ridan-to'g'ri $(h,k)$ nuqtasida joylashadi, simmetriya
o'qi esa $x=h$ to'g'ri chizig'idir.

**$a$ ning ishorasi va kattaligi ikki narsani belgilaydi:**
- $a>0$ bo'lsa, parabola **yuqoriga** ochiladi (cho'qqi — eng past nuqta);
  $a<0$ bo'lsa, **pastga** ochiladi (cho'qqi — eng baland nuqta).
- $|a|$ qancha katta bo'lsa, parabola shuncha **tor** (ingichka); $|a|$
  qancha kichik bo'lsa, shuncha **keng**.

### Model Example (1-misol)

$y=3(x-1)^2+4$ berilgan. Cho'qqini, simmetriya o'qini, va ochilish yo'nalishini
toping.

**Yechish:** Vertex form $a(x-h)^2+k$ bilan solishtiramiz: $h=1$, $k=4$,
$a=3$. Cho'qqi: $(1,4)$. Simmetriya o'qi: $x=1$. $a=3>0$ bo'lgani uchun
parabola yuqoriga ochiladi, va $|a|=3>1$ bo'lgani uchun u $y=x^2$ ga
qaraganda torroq.

**Javob:** Cho'qqi $(1,4)$, simmetriya o'qi $x=1$, yuqoriga ochiladi, tor.

### Your-Turn Example (O'zingiz bajaring)

$y=-\dfrac{1}{2}(x-2)^2+6$ berilgan. Cho'qqi $= \underline{\hspace{15mm}}$,
simmetriya o'qi $= \underline{\hspace{15mm}}$, yo'nalishi va kengligi
$= \underline{\hspace{25mm}}$

---

## Concept 2 — X-kesmalar Ildizlar Sifatida (x-Intercepts Are Roots)

### Definition

*Parabolaning $x$ o'qini kesib o'tgan nuqtalari uning $x$-kesmalari deb
ataladi, va ular aynan tenglamaning ildizlari (yechimlari) bilan bir xil
qiymatlardir — chunki $x$-kesmada $y=0$ bo'ladi.*

<small>(The points where a parabola crosses the x-axis are its x-intercepts
— and these are exactly the same values as the equation's roots/solutions,
because y=0 at an x-intercept.)</small>

**Nima so'ralmoqda? (What is actually being asked?)** "x-kesma," "ildiz," va
"yechim" — uchalasi ham bir xil narsa, faqat turli nomlar bilan so'raladi.
Ammo **y-kesma** butunlay boshqa narsa — u $x=0$ bo'lgandagi qiymat, va odatda
tenglamadagi erkin had ($c$) ga teng. Savolda qaysi biri so'ralganini
aniqlashtirmasdan boshlamang.

### Model Example (2-misol)

$y=x^2-7x+10$ ning $x$-kesmalarini toping.

**Yechish:** $y=0$ qo'yamiz: $x^2-7x+10=0$. Ko'paytuvchilarga ajratamiz:
$(x-2)(x-5)=0$. Demak $x=2$ yoki $x=5$.

**Javob:** $x$-kesmalar: $(2,0)$ va $(5,0)$ — ya'ni $x=2$ va $x=5$.

### Your-Turn Example (O'zingiz bajaring)

$y=x^2+x-12$ ning $x$-kesmalarini toping: $x = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Ko'paytuvchilarga ajratgandan so'ng ishorani unutib qo'yish —
masalan $x^2-5x+6=0 \Rightarrow (x-2)(x-3)=0$ dan $x=-2, x=-3$ deb yozish.

**To'g'ri:** $(x-2)=0$ dan $x=2$ chiqadi, $-2$ emas — ko'paytuvchi ichidagi
ishorani, tenglamani yechishda **teskarisiga** aylantirish kerak. To'g'ri
javob: $x=2$ va $x=3$.

---

## Concept 3 — Diskriminant: Yechimlar Sonini Oldindan Bilish

### Definition

*Kvadrat tenglamaning haqiqiy yechimlari sonini, ularni hisoblamasdan
turib aniqlashtiruvchi ifoda diskriminant deb ataladi va $D=b^2-4ac$
ko'rinishida yoziladi (bu — Lesson 6'da kvadrat formulaning ildiz ostidagi
qismi).*

<small>(The discriminant, D = b²−4ac, predicts how many real solutions a
quadratic equation has — before you solve it. It's literally the piece under
the square root in the quadratic formula from Lesson 6.)</small>

$$D>0 \Rightarrow \text{2 ta haqiqiy ildiz} \qquad D=0 \Rightarrow \text{1 ta haqiqiy ildiz} \qquad D<0 \Rightarrow \text{haqiqiy ildiz yo'q}$$

**Grafikda nimani anglatadi:** $D>0$ — parabola $x$ o'qini **ikki marta**
kesib o'tadi. $D=0$ — parabola $x$ o'qiga faqat **bitta nuqtada tegib**
o'tadi (cho'qqisi aynan $x$ o'qida). $D<0$ — parabola $x$ o'qini **umuman
kesib o'tmaydi** (butunlay yuqorida yoki butunlay pastda qoladi, $a$ ning
ishorasiga qarab).

### Model Example (3-misol)

$x^2+2x+5=0$ nechta haqiqiy yechimga ega?

**Yechish:** $a=1$, $b=2$, $c=5$. $D=b^2-4ac=2^2-4(1)(5)=4-20=-16$.
$D<0$ bo'lgani uchun tenglama haqiqiy yechimga ega emas — grafigi $x$
o'qini umuman kesib o'tmaydi.

**Javob:** $D=-16$, haqiqiy yechim yo'q (0 ta).

### Your-Turn Example (O'zingiz bajaring)

$2x^2-4x+2=0$ ning diskriminantini toping va nechta haqiqiy yechimi borligini
ayting: $D=\underline{\hspace{15mm}}$, yechimlar soni $=\underline{\hspace{10mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** $D=0$ ni "yechim yo'q" deb talqin qilish, chunki "nol — hech
narsa emas" degan intuitiv (lekin noto'g'ri) fikr.

**To'g'ri:** $D=0$ — bu **aynan bitta** haqiqiy yechim degani (ikkala ildiz
bir xil qiymatga tushib qoladi, ya'ni parabola $x$ o'qiga tegib o'tadi).
Yechim yo'qligi faqat $D<0$ bo'lganda bo'ladi.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Parabola | Parabola |
| Vertex | Cho'qqi |
| Axis of symmetry | Simmetriya o'qi |
| x-intercept / root / solution | X-kesma / ildiz / yechim |
| y-intercept | Y-kesma |
| Discriminant | Diskriminant |
| Real solution | Haqiqiy yechim |
| To open upward / downward | Yuqoriga / pastga ochilish |

---

## Notes for the problems file (Sets 1–7)

1. Vertex/direction/width identification from vertex form (pure drill).
2. Discriminant computation + solution-count classification (standard form).
3. Finding x-intercepts (factoring/formula), tying back to Concept 2.
4. Mixed — given standard form, find vertex, discriminant, AND roots together.
5. "Find $k$" discriminant problems — the real SAT question format (given a
   parameter, find values making the equation have 0/1/2 solutions).
6. Spot the error — vertex-sign flip, discriminant-sign misread, direction
   misread from $a$, factoring-sign slip, $D=0$ misinterpretation.
7. Bonus/Challenge — includes a projectile-height word problem (vertex =
   max height) and a "build the equation from its vertex and a point" item.
