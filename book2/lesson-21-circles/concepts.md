# Book 2 — Lesson 21: Circles

**Source content file.** Follows Lesson 20 (Area & Volume), which already covers
basic circle area ($\pi r^2$) and circumference ($2\pi r$) and the
radius-vs-diameter distinction — none of that is retaught here. This lesson
goes one layer deeper: *parts* of a circle (arcs, sectors) instead of the
whole circle, and the circle's own equation on the coordinate plane. The
completing-the-square technique from Lesson 6 (quadratics) gets reused here
almost unchanged — same algebra, new geometric meaning.

**Research grounding:** `research/01-official-sat-math-spec.md` confirms the
digital SAT's Geometry and Trigonometry domain names "circles (radii, chords,
arcs, inscribed angles, tangent lines)" as an official sub-area, and that a
reference sheet with "360°/2π circle facts" is provided on-screen — so the
degree-to-full-circle proportion itself is "free," but knowing *when* to use
it is not. `research/04-common-student-mistakes.md` documents mixing up
degrees and radians in arc-length/sector-area formulas as a recurring circle
error, and confusing inscribed with central angles. **Notation note:** the
digital SAT works in **degrees**, never radians — every angle in this lesson
and in the real test is a degree value; radians do not appear on the SAT.

---

## Nima So'ralmoqda? (What Is Actually Being Asked?)

Bitta doiraning bir yoyi haqida ikki xil savol berilishi mumkin, va ular
ikki xil narsa: **yoy o'lchovi** — bu burchak qiymati, darajada o'lchanadi
($40°$, $120°$ kabi) — va **yoy uzunligi** — bu masofa, radius bilan bir xil
birlikda o'lchanadi (sm, m). Ikkalasi ham bitta markaziy burchakdan kelib
chiqadi, shuning uchun ularni aralashtirish xavfi real: savol "yoyning
uzunligini toping" desa, javob daraja emas, masofa bo'lishi kerak — radius
berilmagan bo'lsa, yoy uzunligini umuman topib bo'lmaydi. Xuddi shunday,
**sektor yuzi** so'ralganda, javob $\pi r^2$ ning bir qismi (yuza birligida),
**yoy uzunligi** so'ralganda — $2\pi r$ ning bir qismi (masofa birligida).
Har bir masalada avval nima so'ralayotganini — daraja, masofa, yoki
yuza — aniq ajrating.

---

## Concept 1 — Yoy Uzunligi va Yoy O'lchovi (Arc Length and Arc Measure)

### Definition

*Aylananing markaziy burchagiga mos keluvchi bo'lagi yoy deb ataladi. Yoyning
daraja bilan ifodalangan kattaligi yoy o'lchovi deb, yoyning haqiqiy uzunligi
(masofa sifatida) esa yoy uzunligi deb ataladi.*

<small>(The part of a circle cut off by a central angle is called an arc.
The arc's size expressed in degrees is its arc measure; the arc's actual
length as a distance is its arc length.)</small>

Yoy o'lchovi markaziy burchakka teng — qo'shimcha hisoblash kerak emas.
Yoy uzunligi esa, to'liq aylana uzunligining ($2\pi r$) markaziy burchak
to'liq burchakka ($360°$) nisbatan qanday qismini tashkil qilishiga teng:

$$\text{Yoy uzunligi} = \frac{\text{markaziy burchak}}{360°} \times 2\pi r$$

### Model Example (1-misol)

Radiusi $9$ sm bo'lgan doirada markaziy burchak $60°$ ga teng. Yoyning
uzunligini toping.

**Yechish:** To'liq aylana uzunligi: $2\pi \times 9 = 18\pi$. Markaziy
burchak to'liq burchakning qaysi qismi: $\dfrac{60}{360} = \dfrac{1}{6}$.
Yoy uzunligi: $\dfrac{1}{6} \times 18\pi = 3\pi$ sm.

**Javob:** $3\pi$ sm

### Your-Turn Example (O'zingiz bajaring)

Radiusi $12$ sm bo'lgan doirada markaziy burchak $90°$ ga teng. Yoy
uzunligi $= \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** "Yoy uzunligi $40°$ ga teng" — markaziy burchakning qiymatini
(daraja) to'g'ridan-to'g'ri yoyning uzunligi (masofa) deb javob sifatida
yozish.

**To'g'ri:** $40°$ — bu yoy o'lchovi, masofa emas. Yoy uzunligini topish
uchun radius kerak va yuqoridagi formuladan foydalanish shart:
$\dfrac{40}{360}\times2\pi r$. Radius berilmagan bo'lsa, yoy uzunligini
hisoblab bo'lmaydi — faqat yoy o'lchovini (daraja) aytish mumkin.

*(Ikkalasi bitta berilgan ma'lumotdan — markaziy burchakdan — kelib
chiqgani uchun, ularni aralashtirish real xavf: biri son (daraja), ikkinchisi
masofa, va ular faqat radius orqali bog'lanadi.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Arc | Yoy |
| Arc measure (degrees) | Yoy o'lchovi |
| Arc length (a distance) | Yoy uzunligi |
| Central angle | Markaziy burchak |
| Circumference | Aylana uzunligi |

---

## Concept 2 — Sektor Yuzi (Sector Area)

### Definition

*Aylananing ikkita radius va ularga mos yoy bilan chegaralangan qismi sektor
deb ataladi. Sektor yuzi, to'liq doira yuzining ($\pi r^2$) markaziy burchak
to'liq burchakka nisbatan qanday qismini tashkil qilishiga teng.*

<small>(The region bounded by two radii and the arc between them is called
a sector. A sector's area is the same fraction of the full circle's area
($\pi r^2$) that the central angle is of $360°$.)</small>

$$\text{Sektor yuzi} = \frac{\text{markaziy burchak}}{360°} \times \pi r^2$$

*(E'tibor bering: formulaning tuzilishi yoy uzunligi formulasiga juda
o'xshash — faqat $2\pi r$ o'rniga $\pi r^2$ qo'yiladi, chunki bu safar
masofa emas, yuza hisoblanadi. Ikki formulani aralashtirib yubormaslik
uchun, har doim "bu yuza (sm²) yoki masofa (sm) so'ralmoqda?" deb o'zingizga
savol bering.)*

### Model Example (2-misol)

Radiusi $6$ sm bo'lgan doirada markaziy burchak $120°$ ga teng. Sektor
yuzini toping.

**Yechish:** To'liq doira yuzi: $\pi \times 6^2 = 36\pi$. Markaziy burchak
to'liq burchakning qismi: $\dfrac{120}{360} = \dfrac{1}{3}$. Sektor yuzi:
$\dfrac{1}{3}\times36\pi = 12\pi$ sm².

**Javob:** $12\pi$ sm²

### Your-Turn Example (O'zingiz bajaring)

Radiusi $10$ sm bo'lgan doirada markaziy burchak $144°$ ga teng. Sektor
yuzi $= \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Sektor yuzini topishda, aylana uzunligi formulasidan
foydalanish: "Sektor yuzi $= \dfrac{90}{360}\times2\pi\times10 = 5\pi$"
(bu yerda $\pi r^2$ o'rniga $2\pi r$ qo'llanilgan — bu yoy uzunligi
formulasi, yuza formulasi emas).

**To'g'ri:** Yuza so'ralganda, albatta $\pi r^2$ dan boshlanadi:
$\dfrac{90}{360}\times\pi\times10^2 = \dfrac{1}{4}\times100\pi = 25\pi$ sm².

### Vocabulary

| English | O'zbekcha |
|---|---|
| Sector | Sektor |
| Sector area | Sektor yuzi |
| Full circle area | To'liq doira yuzi |

---

## Concept 3 — Aylana Tenglamasi (Equation of a Circle)

### Definition

*Markazi $(h,k)$ nuqtada, radiusi $r$ bo'lgan aylananing barcha nuqtalari
$(x-h)^2+(y-k)^2=r^2$ tenglamasini qanoatlantiradi; shu tenglama aylana
tenglamasi deb ataladi.*

<small>(Every point on a circle with center $(h,k)$ and radius $r$ satisfies
$(x-h)^2+(y-k)^2=r^2$ — this is called the equation of the circle.)</small>

Tenglama ko'pincha ochilgan (umumiy) ko'rinishda beriladi:
$x^2+y^2+Dx+Ey+F=0$. Markaz va radiusni topish uchun, Lesson 6 dagi
**to'liq kvadratga keltirish** usuli qo'llaniladi — faqat bu safar $x$ va
$y$ uchun alohida-alohida bajariladi.

### Model Example (3-misol)

$x^2+y^2-6x+4y-12=0$ tenglamasi berilgan. Markaz va radiusni toping.

**Yechish:** $x$ va $y$ hadlarini guruhlaymiz, erkin hadni o'ng tomonga
o'tkazamiz (ishorasi o'zgaradi): $(x^2-6x)+(y^2+4y)=12$.

Har bir guruhni to'liq kvadratga keltiramiz: $x$ uchun koeffitsientni
ikkiga bo'lib kvadratga ko'taramiz — $(-6\div2)^2=9$; $y$ uchun —
$(4\div2)^2=4$. Shu sonlarni ikkala tomonga qo'shamiz:

$$(x^2-6x+9)+(y^2+4y+4)=12+9+4$$
$$(x-3)^2+(y+2)^2=25$$

**Javob:** Markaz $(3,-2)$, radius $r=\sqrt{25}=5$.

*(Diqqat: $(y+2)^2$ shaklidagi markaz koordinatasi $-2$, $+2$ emas — chunki
tenglama $(y-k)^2$ ko'rinishida, $(y+2)^2=(y-(-2))^2$, demak $k=-2$.)*

### Your-Turn Example (O'zingiz bajaring)

$x^2+y^2+8x-2y+8=0$ tenglamasi berilgan. Markaz $=\underline{\hspace{20mm}}$,
radius $=\underline{\hspace{15mm}}$

### Common Mistake Box (conditional — documented error, include)

**Birinchi xato (ishora xatosi, erkin hadni ko'chirishda):** $-12$ ni o'ng
tomonga ko'chirishda ishorani o'zgartirmasdan qoldirish — $(x^2-6x)+(y^2+4y)=-12$
yozish ($+12$ o'rniga). Bu butun qolgan yechimni buzadi.

**Ikkinchi xato (markazni o'qishda ishora aralashtirish):** $(x+6)^2+(y-3)^2=49$
tenglamasida markazni $(6,3)$ deb o'qish. **To'g'ri:** tenglama
$(x-h)^2+(y-k)^2$ shaklida, $(x+6)^2=(x-(-6))^2$, shuning uchun markaz
$(-6,3)$ — $x$ koordinatasining ishorasi teskari.

*(Ikkala xato ham Lesson 6 da kvadrat formula bilan uchragan "$-b$ ishorasini
yo'qotish" xatosining geometrik ko'rinishi — bir xil ehtiyotkorlik talab
qiladi.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Equation of a circle | Aylana tenglamasi |
| Center | Markaz |
| Radius | Radius |
| General/expanded form | Ochilgan (umumiy) ko'rinish |
| Standard (center-radius) form | Markaz-radius ko'rinishi |

---

## Notes for the problems file (Sets 1–7)

1. Arc length/measure drill, including two reverse items (given length and
   radius, find the angle) and one item explicitly testing the
   measure-vs-length distinction.
2. Sector area drill, including two reverse items (given area and radius,
   find the angle).
3. Mixed — same circle and same angle, one item asks for arc length and the
   next asks for sector area, forcing the two formulas to stay distinct;
   closes with a two-part context (sprinkler) problem.
4. Circle equation reading (standard form given, find center/radius),
   including items designed to test the center-sign-flip trap.
5. Circle equation via completing the square (general form → standard
   form).
6. Spot the error — five items: arc-length-vs-measure conflation, sector
   formula swapped for the arc-length formula, a sign error moving the
   constant term, a center-sign-flip misread, and an arc-length formula
   swapped for the sector-area formula.
7. Bonus/challenge — working backward from sector area or arc length to
   find the radius, a two-step arc-length-then-sector-area problem, a
   circle-equation problem with a follow-up point-position question, and a
   fraction-of-circle problem.
