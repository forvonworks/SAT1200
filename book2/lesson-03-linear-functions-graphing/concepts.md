# Book 2 — Lesson 3: Linear Functions & Graphing

**Source content file.** Builds directly on Book 1 Lesson 8 (Coordinate Plane &
Function Notation), which already covered the coordinate plane, $y=kx+b$, and
the basic $f(x)$ bridge. That's assumed prior knowledge here — this lesson goes
deeper: slope as rate of change, writing a line's equation, parallel/
perpendicular lines, and reading a line's real-world meaning. Per Book 2's
cross-cutting requirements: every concept below is checked against the official
skill list in `research/01-official-sat-math-spec.md` (Algebra domain —
"Linear functions" is an explicitly tested skill), flags sign-error risk where
documented, and calls out the confirmed Uzbek/Russian-tradition notation gap
from `research/05-uzbek-student-considerations.md` directly rather than
assuming it away.

**Formula note:** the slope formula is **not** on the Bluebook reference sheet
— per `research/01`, Algebra/Advanced Math formulas must be memorized, unlike
the geometry formulas the app provides on-screen.

---

## Concept 1 — Burchak Koeffitsienti (Slope)

### Definition

*Ikki nuqta orqali o'tuvchi to'g'ri chiziqning tikka o'zgarishi (Δy) ning
gorizontal o'zgarishiga (Δx) nisbati shu chiziqning burchak koeffitsienti
(moyillik) deb ataladi va quyidagi formula bilan topiladi:*

$$m = \frac{y_2-y_1}{x_2-x_1}$$

<small>(Slope measures how steep a line is — how much $y$ changes for every
one-unit change in $x$.)</small>

**Diqqat — atama ko'prigi:** o'zbek/rus an'anasida bu kattalik ko'pincha $k$
harfi bilan belgilanadi va to'g'ri chiziq tenglamasi $y=kx+b$ ko'rinishida
yoziladi — bu sizga Kitob 1, 8-darsdan tanish. SAT esa aynan shu kattalikni
**slope** deb ataydi va $m$ harfi bilan belgilaydi: $y=mx+b$. Bu ikkisi — $k$
va $m$ — bir xil narsa, faqat nom va harf boshqacha. SAT savollarida "slope,"
"rate of change," va $m$ so'zlarini ko'rganingizda, bu aynan sizga tanish
burchak koeffitsienti ekanini eslang.

### Model Example (1-misol)

$(3,2)$ va $(7,10)$ nuqtalari orqali o'tuvchi chiziqning burchak koeffitsientini
toping.

**Yechish:** $m = \dfrac{10-2}{7-3} = \dfrac{8}{4} = 2$.

**Javob:** $m=2$

### Your-Turn Example (O'zingiz bajaring)

$(1,5)$ va $(4,-1)$ nuqtalari orqali o'tuvchi chiziqning burchak koeffitsienti
$= \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** formulani teskari qo'llab, $\dfrac{x_2-x_1}{y_2-y_1}$ ni
hisoblash (ya'ni "run ÷ rise," "rise ÷ run" o'rniga) — bu formulani
yodlashdagi eng keng tarqalgan xato.

**To'g'ri:** har doim **tepaga (y) o'zgarish — pastga (x) o'zgarish** tartibida:
$m=\dfrac{y_2-y_1}{x_2-x_1}$.

**Ikkinchi keng tarqalgan xato** (tadqiqotda alohida qayd etilgan,
`research/04`): $y=mx+b$ tenglamasida $m$ (qiyalik) va $b$ (kesilgan nuqta) ni
aralashtirib yuborish — masalan, $y=5x-3$ da "qiyalik $-3$" deb aytish. $-3$ —
bu $b$ (y o'qini kesish nuqtasi), qiyalik esa $5$.

---

## Concept 2 — To'g'ri Chiziq Tenglamasini Yozish

### Definition

*Berilgan nuqta $(x_1,y_1)$ va burchak koeffitsienti $m$ orqali to'g'ri chiziq
tenglamasini yozish usuli nuqta-qiyalik shakli (point-slope form) deb ataladi:*

$$y-y_1 = m(x-x_1)$$

<small>(Once you know a point on a line and its slope, point-slope form lets
you write the full equation — then simplify to $y=mx+b$.)</small>

### Model Example (2-misol)

Qiyaligi $4$ ga teng va $(1,3)$ nuqtasidan o'tuvchi chiziq tenglamasini yozing.

**Yechish:** $y-3=4(x-1)$. Qavsni ochamiz: $y-3=4x-4$. Ikkala tomonga $+3$:
$y=4x-1$.

**Javob:** $y=4x-1$

### Model Example (3-misol — ikki nuqta orqali)

$(2,1)$ va $(4,7)$ nuqtalari orqali o'tuvchi chiziq tenglamasini yozing.

**Yechish:** Avval qiyalikni topamiz: $m=\dfrac{7-1}{4-2}=\dfrac{6}{2}=3$.
Endi nuqta-qiyalik shaklidan foydalanamiz (ixtiyoriy nuqtani, masalan $(2,1)$
ni olamiz): $y-1=3(x-2)$. Qavsni ochib soddalashtiramiz: $y-1=3x-6$, demak
$y=3x-5$.

**Javob:** $y=3x-5$

### Your-Turn Example (O'zingiz bajaring)

Qiyaligi $\frac12$ ga teng va $(4,-1)$ nuqtasidan o'tuvchi chiziq tenglamasi
$= \underline{\hspace{25mm}}$

---

## Concept 3 — Parallel va Perpendikulyar Chiziqlar

### Definition

*Agar ikki to'g'ri chiziqning burchak koeffitsientlari (m qiymatlari) teng
bo'lsa, ular parallel chiziqlar deb ataladi. Agar ularning ko'paytmasi $-1$ ga
teng bo'lsa (ya'ni biri ikkinchisining manfiy teskarisi bo'lsa), ular
perpendikulyar chiziqlar deb ataladi.*

$$m_1 = m_2 \ \text{(parallel)} \qquad\qquad m_1 \times m_2 = -1 \ \text{(perpendikulyar)}$$

### Model Example (4-misol)

$y=2x-5$ chizig'iga perpendikulyar bo'lgan va $(4,1)$ nuqtasidan o'tuvchi
chiziq tenglamasini toping.

**Yechish:** Berilgan chiziqning qiyaligi $2$. Perpendikulyar chiziqning
qiyaligi uning manfiy teskarisi: $-\dfrac12$. Nuqta-qiyalik shaklidan:
$y-1=-\dfrac12(x-4)$. Qavsni ochamiz: $y-1=-\dfrac12x+2$, demak
$y=-\dfrac12x+3$.

**Javob:** $y=-\dfrac12x+3$

### Your-Turn Example (O'zingiz bajaring)

$y=-\dfrac13x+2$ chizig'iga perpendikulyar bo'lgan va $(-2,0)$ nuqtasidan
o'tuvchi chiziq tenglamasi $= \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** perpendikulyar chiziq uchun shunchaki teskari sonni olib, ishora
(minus)ni unutish — masalan, $\frac23$ ning "teskarisi" sifatida $\frac32$ ni
yozib, $-\frac32$ emasligini unutish.

**To'g'ri:** perpendikulyar qiyalik har doim ham teskari, ham ishorasi
qarama-qarshi bo'ladi: $\frac23 \to -\frac32$.

---

## Concept 4 — Qiyalik va Kesilgan Nuqtaning Amaliy Ma'nosi

### Definition

*Amaliy (real-life) masalada to'g'ri chiziq funksiyasining qiyaligi
o'zgarishning tezligini (har bir birlik uchun qancha o'zgarishini), kesilgan
nuqta esa boshlang'ich (x=0 dagi) qiymatni bildiradi.*

<small>(In a word problem, slope is the rate of change and the y-intercept is
the starting value — reading which is which from the question is itself part
of the skill.)</small>

**Nima so'ralmoqda? — tekshirish odati:** savolni ikkinchi marta o'qing va
aniq nimani so'rayotganini ayting: qiyalikning o'zi so'ralyaptimi (masalan,
"necha so'm/km"), yoki ma'lum bir $x$ dagi to'liq qiymat so'ralyaptimi ("necha
so'm bo'ladi"), yoki $x$ ning o'zi so'ralyaptimi ("necha kilometrda tugaydi")?
Bu uchalasi ham boshqa-boshqa amal talab qiladi — savolni oxirigacha
o'qimasdan hisoblashni boshlash eng ko'p ball yo'qotadigan xato
(`research/04`da tasdiqlangan, "solved for the wrong thing").

### Model Example (5-misol)

Taksi xizmati $5000$ so'm boshlang'ich to'lov va har kilometr uchun $2000$
so'm oladi: $C(x) = 2000x+5000$, bu yerda $x$ — kilometr. $10$ km uchun
to'lov qancha bo'ladi?

**Yechish:** $C(10) = 2000(10)+5000 = 20000+5000=25000$.

**Javob:** $25000$ so'm. (Bu yerda $2000$ — qiyalik, ya'ni har km uchun narx;
$5000$ — kesilgan nuqta, ya'ni boshlang'ich to'lov.)

### Your-Turn Example (O'zingiz bajaring)

Suv bak $60$ litr suv bilan to'la va daqiqasiga $5$ litrdan oqizilmoqda:
$V(x)=-5x+60$. Bak qachon (necha daqiqada) bo'shab qoladi? $x = \underline{\hspace{25mm}}$

*(Diqqat: bu yerda qiyalik manfiy — $-5$ — chunki hajm kamayib bormoqda, ko'payib
emas. Ishoraning ma'nosini kontekstda to'g'ri o'qing.)*

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Slope / rate of change | Burchak koeffitsienti / qiyalik / o'zgarish tezligi |
| y-intercept | Y o'qidagi kesilgan nuqta / boshlang'ich qiymat |
| Point-slope form | Nuqta-qiyalik shakli |
| Slope-intercept form | Qiyalik-kesilgan nuqta shakli |
| Parallel | Parallel |
| Perpendicular | Perpendikulyar |
| Negative reciprocal | Manfiy teskari son |

---

## Notes for the problems file (Sets 1–7)

1. Pure slope-from-two-points drill (clean integers, includes a horizontal case).
2. Harder slope drill (fractional/negative results).
3. Write a line's equation — mixed point+slope and two-point setups.
4. Parallel/perpendicular equations, including horizontal/vertical edge cases.
5. Context word problems — evaluate and solve, with an explicit sign-meaning item.
6. Spot the error — targets the inverted-formula, slope/intercept-swap,
   same-slope-for-perpendicular, and distribution-sign mistakes directly.
7. Bonus/challenge — multi-step: parallel/perpendicular combined with solving
   for an unknown coefficient, and matching two different equation forms of
   the same line.
