# Book 2 — Lesson 20: Area & Volume

**Source content file**, paired with `problems.md`. Domain: Geometry & Trigonometry
(official SAT weight ~15%, 5–7 questions). Builds on Lesson 19's triangle/angle
basics as prior knowledge (triangle classification, angle sum — not re-taught
here). Per `research/01-official-sat-math-spec.md`, the Bluebook reference sheet
provides every formula in this lesson on-screen during the real test — so the
skill tested is never "memorize the formula," it's "pick the right formula,
convert the right input, and know whether to add or subtract." That's exactly
what the three concepts below target.

**Two standing notes, true for this entire lesson:**

1. **Figures are not guaranteed to be drawn to scale.** A labeled dimension is
   always trustworthy; the *look* of a figure is not. Never estimate a length
   or angle by eye — only use what's written or marked.
2. **Units.** Area is always reported in square units (sm², m²) and volume in
   cubic units (sm³, m³) — never plain units. If a problem gives mixed units
   (e.g. one side in sm, another in mm), convert *before* computing, not after.

---

## Concept 1 — Standard Area Formulas (Standart Maydon Formulalari)

### Definition

*Yopiq tekis shaklning ichki qismi egallagan o'lchov maydon deb ataladi. Har
bir shakl turi uchun maydonni hisoblashning o'z formulasi mavjud: to'g'ri
to'rtburchak, uchburchak, parallelogramm, trapetsiya va doira — eng ko'p
uchraydigan beshta shakl.*

<small>(The measure of the region enclosed by a flat closed shape is called
its area. Each shape type has its own formula for computing it: rectangle,
triangle, parallelogram, trapezoid, and circle — the five most common
shapes.)</small>

### Quick reference table

| Shakl (Shape) | Formula | Belgilar (Variables) |
|---|---|---|
| To'g'ri to'rtburchak (Rectangle) | $A = l \times w$ | $l$ = uzunlik, $w$ = kenglik |
| Uchburchak (Triangle) | $A = \dfrac{1}{2}bh$ | $b$ = asos, $h$ = balandlik |
| Parallelogramm (Parallelogram) | $A = bh$ | $b$ = asos, $h$ = balandlik |
| Trapetsiya (Trapezoid) | $A = \dfrac{1}{2}(a+b)h$ | $a,b$ = ikki parallel asos, $h$ = balandlik |
| Doira (Circle) | $A = \pi r^2$ | $r$ = radius |

**The one SAT-specific trap in this entire table: radius vs. diameter.** A
problem very often gives the **diameter**, not the radius — but the area
formula needs $r$, not $d$. Skipping the halving step is one of the most
frequently cited SAT geometry errors (`research/04-common-student-mistakes.md`).
Always ask: *am I holding a radius or a diameter right now?* before plugging
into $A=\pi r^2$.

### Model Example (1-misol)

Doiraning diametri $18$ sm ga teng. Doiraning maydonini toping.

**Yechish:** Formula $r$ ni talab qiladi, $d$ ni emas — avval diametrni
ikkiga bo'lamiz: $r = \dfrac{18}{2} = 9$ sm. Endi formulaga qo'yamiz:
$A = \pi r^2 = \pi \times 9^2 = 81\pi$.

**Javob:** $A = 81\pi$ sm²

### Your-Turn Example (O'zingiz bajaring)

Doiraning diametri $24$ sm. Doiraning maydonini toping. $A = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Diametrni to'g'ridan-to'g'ri $r$ o'rniga qo'yish:
$A = \pi(18)^2 = 324\pi$ — bu **noto'g'ri**, chunki $18$ diametr, radius emas.

**To'g'ri qoida:** $A=\pi r^2$ formulasidagi $r$ doim **radius** (markazdan
chetgacha), hech qachon diametr emas. Diametr berilganda, formulaga qo'yishdan
oldin **har doim** ikkiga bo'ling: $r = \dfrac{d}{2}$. Model misoldagi to'g'ri
javob $81\pi$, noto'g'ri yondashuv esa $324\pi$ — aynan to'rt marta katta,
chunki $18^2 = 324$ esa kerakli $9^2=81$ dan to'rt marta katta.

### Vocabulary (shared across this lesson)

| English | O'zbekcha |
|---|---|
| Area | Maydon |
| Volume | Hajm |
| Radius | Radius |
| Diameter | Diametr |
| Rectangle | To'g'ri to'rtburchak |
| Triangle | Uchburchak |
| Parallelogram | Parallelogramm |
| Trapezoid | Trapetsiya |
| Circle | Doira |
| Base / Height | Asos / Balandlik |
| Rectangular prism | To'g'ri burchakli prizma |
| Cylinder | Silindr |
| Cone | Konus |
| Sphere | Shar |
| Composite figure | Murakkab figura |
| Not drawn to scale | Masshtabga mos chizilmagan |

---

## Concept 2 — Standard Volume Formulas (Standart Hajm Formulalari)

### Definition

*Fazodagi jismning egallagan o'rni hajm deb ataladi. To'rt asosiy jism —
to'g'ri burchakli prizma, silindr, konus va shar — uchun hajm formulalari
rasmiy SAT ma'lumotnoma varag'ida berilgan bo'ladi, shuning uchun ularni
yodlash shart emas, lekin **qaysi formula qaysi jismga tegishli ekanini**
va formuladagi $\frac13$ yoki $\frac43$ koeffitsientlarini qachon
ishlatishni bilish shart.*

<small>(The space a solid occupies is called its volume. For the four main
solids — rectangular prism, cylinder, cone, sphere — the SAT's own reference
sheet gives the formulas, so memorizing them isn't required, but knowing
which formula belongs to which solid, and when to apply the $\frac13$ or
$\frac43$ coefficients, is.)</small>

### Quick reference table

| Jism (Solid) | Formula | Eslatma |
|---|---|---|
| To'g'ri burchakli prizma | $V = lwh$ | Uchta o'lchamning ko'paytmasi |
| Silindr | $V = \pi r^2 h$ | Doira asosining maydoni $\times$ balandlik |
| Konus | $V = \dfrac{1}{3}\pi r^2 h$ | Silindrning **uchdan biri** — xuddi shu $r,h$ bilan |
| Shar | $V = \dfrac{4}{3}\pi r^3$ | Faqat $r$ ga bog'liq — balandlik yo'q |

**Where students actually lose points here is not the formula itself — it's
forgetting the $\frac13$ (cone) or $\frac43$ (sphere) coefficient and
computing it as if it were a cylinder.** A cone with the same base and height
as a cylinder holds exactly **one-third** of that cylinder's volume — treat
that relationship as a sanity check, not just a formula to memorize.

### Model Example (2-misol)

Radiusi $6$ sm bo'lgan sharning hajmini toping.

**Yechish:** Shar formulasi faqat $r$ ga bog'liq, balandlik kerak emas:
$V = \dfrac{4}{3}\pi r^3$. Avval $r^3 = 6^3 = 216$. Keyin
$\dfrac{4}{3}\times216 = 4\times72 = 288$.

**Javob:** $V = 288\pi$ sm³

### Your-Turn Example (O'zingiz bajaring)

Radiusi $3$ sm, balandligi $10$ sm bo'lgan konusning hajmini toping.
$V = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Konus yoki sharni silindr kabi hisoblash — ya'ni
$\frac13$ yoki $\frac43$ koeffitsientini tashlab yuborish. Masalan, radiusi
$5$ bo'lgan sharni $V = \pi(5)^3 = 125\pi$ deb hisoblash.

**To'g'ri qoida:** Shar formulasida $\frac43$ koeffitsienti **hech qachon**
tashlanmaydi: $V = \frac43\pi r^3 = \frac43\pi(125) = \dfrac{500}{3}\pi$.
Xuddi shunday, konus formulasida $\frac13$ ham doim bo'lishi shart — aks
holda javob haqiqiy hajmdan **3 marta katta** chiqadi (chunki konus aynan shu
$r,h$ ga ega silindrning uchdan bir qismi).

---

## Concept 3 — Composite Figures (Murakkab Figuralar)

### Definition

*Bir nechta standart shakldan (to'rtburchak, uchburchak, doira va h.k.)
tuzilgan yoki ulardan bir qismi olib tashlangan figura murakkab figura deb
ataladi. Murakkab figuraning maydoni yoki hajmi — qism-figuralarning
maydonlarini/hajmlarini **qo'shish** (agar ular birlashtirilgan bo'lsa) yoki
**ayirish** (agar biridan ikkinchisi kesib olingan/teshik qilingan bo'lsa)
orqali topiladi.*

<small>(A figure built from several standard shapes, or formed by removing
part of one shape from another, is called a composite figure. Its area or
volume is found by **adding** the component areas/volumes — if the shape is
built by joining pieces — or **subtracting** them — if one piece is cut out
of another.)</small>

> **Nima So'ralmoqda? (What is actually being asked?)** A composite-figure
> question almost never stops at "find the total area." It may ask for just
> *one* sub-region (e.g. only the hole's area, or only the leftover strip),
> or it may give you the total area and ask you to work backward for a
> missing dimension (see `problems.md` Set 5). Before computing anything,
> identify exactly which region — or which number — the question wants.

### Model Example (3-misol) — Qo'shish (Addition case)

Figura ikki to'g'ri to'rtburchakdan iborat: birinchisi $10$ sm $\times$ $6$ sm,
ikkinchisi unga yopishtirilgan $4$ sm $\times$ $3$ sm. Figuraning umumiy
maydonini toping.

**Yechish:** Ikki qism bir-biriga **qo'shilgan** (biriktirilgan), teshik yoki
kesilgan joy yo'q — demak qo'shamiz. Birinchi qism: $10\times6=60$. Ikkinchi
qism: $4\times3=12$. Umumiy: $60+12=72$.

**Javob:** $A = 72$ sm²

### Model Example (4-misol) — Ayirish (Subtraction case)

Tomoni $10$ sm bo'lgan kvadratning ichidan radiusi $3$ sm bo'lgan doira
shaklida teshik kesib olingan. Qolgan (bo'yalgan) qismning maydonini toping.

**Yechish:** Bu safar bir qism ikkinchisidan **olib tashlangan** (teshik) —
demak ayiramiz, qo'shmaymiz. Kvadrat maydoni: $10^2=100$. Teshik (doira)
maydoni: $\pi(3)^2=9\pi$. Qolgan qism: $100-9\pi$.

**Javob:** $A = 100 - 9\pi$ sm²

*(E'tibor bering: bu yerda $100+9\pi$ deb yozish — teshikni qo'shib
yuborish — eng ko'p uchraydigan xato. Javob doim **kichikroq** bo'lishi
kerak, chunki biror qism olib tashlangan.)*

### Your-Turn Example (O'zingiz bajaring)

To'g'ri to'rtburchak $12$ sm $\times$ $8$ sm. Uning ichidan tomoni $3$ sm
bo'lgan kvadrat shaklida teshik kesib olingan. Qolgan qismning maydonini
toping. $A = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Teshik/kesilgan qismni umumiy maydonga **qo'shib**
yuborish — go'yo u qo'shimcha qism bo'lgandek. Model 4-misoldagi masalada:
$100+9\pi$ deb yozish.

**To'g'ri qoida:** Agar biror qism *kesib olingan, teshilgan yoki
chiqarib tashlangan* bo'lsa — bu doim **ayirish** amali, hech qachon
qo'shish emas. O'zingizga shuni savol qiling: *"bu qism figuraning bir bo'lagi,
yoki undan olib tashlangan bo'lakmi?"* Javob har doim kesilgan qismdan
**kichikroq** bo'lishi kerak — $100-9\pi \approx 71.7$, kesilmagan to'liq
kvadrat $100$ dan kichik, bu mantiqan to'g'ri; $100+9\pi\approx128.3$ esa
to'liq kvadratdan **katta** chiqadi, bu teshik bor figura uchun mantiqsiz —
shu tekshirish o'zi xatoni darhol fosh qiladi.
