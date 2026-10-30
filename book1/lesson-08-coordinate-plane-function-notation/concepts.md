# Book 1 — Lesson 8: Coordinate Plane & Function Notation (Intro)

**Source content file.** This is the authored content, not the final page — it gets
typeset against `research/14-design-spec.md`. Structure follows that spec's
content-block pattern (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary.

**Research grounding:** `research/05-uzbek-student-considerations.md` documents
the exact notation gap this lesson exists to close: "Russian-tradition texts
reportedly call the slope the 'angle coefficient' ... and conventionally write
linear functions as y = kx + b." Uzbek curriculum does not reliably introduce
f(x) notation. This lesson's whole job is bridging the already-known y=kx+b
form to the f(x) notation Book 2 and the SAT assume fluency with.
`research/04-common-student-mistakes.md` documents two concrete, well-attested
f(x) errors used directly in the Common Mistake box below: reading f(x) as
"f times x" rather than "f evaluated at x," and dropping parentheses when
substituting a negative number (e.g. computing `-2²` instead of `(-2)²`).

---

## Concept 1 — Koordinatalar Tekisligi (The Coordinate Plane)

### Definition

*Ikkita o'zaro perpendikulyar sonlar o'qidan iborat tekislik koordinatalar
tekisligi deb ataladi. Gorizontal o'q abssissalar o'qi (Ox), vertikal o'q esa
ordinatalar o'qi (Oy) deb ataladi; ular kesishgan nuqta koordinata boshi deb
ataladi va (0, 0) bilan belgilanadi.*

<small>(A plane made of two mutually perpendicular number lines is called the
coordinate plane. The horizontal axis is the x-axis, the vertical axis the
y-axis; the point where they cross is called the origin, written (0, 0).)</small>

*Tekislikdagi istalgan nuqtaga mos keluvchi, birinchi o'rinda abssissa,
ikkinchi o'rinda ordinata turuvchi (x, y) ko'rinishidagi son juftligi shu
nuqtaning koordinatalari deb ataladi.*

<small>(Every point on the plane corresponds to an ordered pair (x, y), where
the first number is the x-coordinate and the second is the y-coordinate.)</small>

*Koordinatalar o'qlari tekislikni to'rtta qismga ajratadi; ularning har biri
chorak (kvadrant) deb ataladi va I dan IV gacha, soat strelkasiga teskari
yo'nalishda, raqamlanadi.*

<small>(The axes divide the plane into four parts; each part is called a
quadrant, numbered I through IV counterclockwise.)</small>

| Chorak | x ishorasi | y ishorasi |
|---|---|---|
| I | + | + |
| II | − | + |
| III | − | − |
| IV | + | − |

### Model Example (1-misol)

$(3,\ 5)$ nuqtasi qaysi chorakda joylashganini aniqlang.

**Yechish:** Abssissa musbat ($x=3>0$), ordinata ham musbat ($y=5>0$).
Demak, nuqta I chorakda joylashgan.

**Javob:** I chorak.

### Your-Turn Example (O'zingiz bajaring)

$(-9,\ 2)$ nuqtasi qaysi chorakda? $\underline{\hspace{25mm}}$

*(No common-mistake box here — no well-documented error specific to quadrant
identification was found in the research; conditional box rule from the style
guide means skip it rather than force one.)*

---

## Concept 2 — y = kx + b: Allaqachon Tanish Shakl (Already-Known Form)

### Definition

*x ga bog'liq holda qiymati $y = kx + b$ qoidasi bilan aniqlanadigan funksiya
chiziqli funksiya deb ataladi, bunda $k$ va $b$ — berilgan sonlar
(koeffitsientlar).*

<small>(A function whose value depends on x by the rule y = kx + b is called a
linear function, where k and b are given numbers.)</small>

*Bu yerda $k$ burchak koeffitsienti deb ataladi — u to'g'ri chiziqning
qanchalik tik yoki yotiq ekanini ko'rsatadi; $b$ esa funksiya grafigining Oy
o'qi bilan kesishish nuqtasining ordinatasi bo'lib, erkin had deb ataladi.*

<small>(Here k is called the angle coefficient — it shows how steep the line
is; b is the y-coordinate of the point where the graph crosses the y-axis,
called the constant term.)</small>

**SAT uchun muhim ko'prik:** Rus/o'zbek an'anaviy darsliklarida $k$ burchak
koeffitsienti deb atalsa, SAT va ingliz tilidagi manbalarda xuddi shu son
*slope* (qiyalik) deb ataladi va odatda $m$ harfi bilan belgilanadi:
$y = mx + b$. Demak, $k = m$ — faqat nom va harf boshqacha, ma'no bir xil.

### Model Example (2-misol)

$y = -3x + 5$ tenglamasida $k$ va $b$ ni aniqlang.

**Yechish:** Tenglama $y = kx + b$ shakli bilan solishtirilsa, $k = -3$,
$b = 5$ ekani ko'rinadi. $k$ manfiy bo'lgani uchun, chiziq chapdan o'ngga
qarab pasayadi.

**Javob:** $k = -3$ (slope), $b = 5$ (y-intercept).

### Your-Turn Example (O'zingiz bajaring)

$y = 2x - 7$ tenglamasida $k = \underline{\hspace{15mm}}$,
$b = \underline{\hspace{15mm}}$

---

## Concept 3 — f(x): Bir Xil Narsaning Boshqa Nomi (The Bridge)

### Definition

*$y$ ning $x$ ga bog'liqligini ko'rsatuvchi, "$y$" o'rnida ishlatiladigan
$f(x)$ belgisi funksiya belgilanishi deb ataladi; bu yerda $f$ — funksiya
nomi, $x$ — erkin o'zgaruvchi, va $f(x)$ aynan $y$ ning o'zidir, boshqacha
yozilgan, xolos.*

<small>(The notation f(x), used in place of "y," is called function notation;
f is the function's name, x is the independent variable, and f(x) is
literally y, just written differently.)</small>

**Demak:** $y = kx + b$ va $f(x) = kx + b$ — bitta va aynan bir xil chiziqni
ifodalaydi; faqat "$y$" so'zi "$f(x)$" bilan almashtirilgan.

*$f(x)$ ifodasida $x$ o'rniga aniq bir son, masalan $a$, qo'yilganda hosil
bo'lgan natija $f(a)$ deb yoziladi va "funksiyaning $a$ nuqtadagi qiymati"
deb o'qiladi; bu amal $x$ o'rniga shunchaki $a$ sonini qo'yib, ifodani
hisoblashdan iborat.*

<small>(When a is substituted for x in f(x), the result is written f(a) and
read as "the value of the function at a"; computing it means substituting a
for x and evaluating.)</small>

### Model Example (3-misol)

$f(x) = 2x + 3$ bo'lsa, $f(4)$ ni toping.

**Yechish:** $x$ o'rniga $4$ qo'yiladi: $f(4) = 2(4) + 3 = 8 + 3 = 11$.

**Javob:** $f(4) = 11$.

### Model Example (4-misol — manfiy son bilan)

$f(x) = x^2 - 2x$ bo'lsa, $f(-3)$ ni toping.

**Yechish:** $x$ o'rniga $-3$ **albatta qavs ichida** qo'yiladi:
$f(-3) = (-3)^2 - 2(-3) = 9 + 6 = 15$.

**Javob:** $f(-3) = 15$.

### Your-Turn Example (O'zingiz bajaring)

$f(x) = 5x - 4$ bo'lsa, $f(-2) = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Birinchi xato — $f(x)$ ni ko'paytma deb tushunish:**
Noto'g'ri: $f(x) = 2x+3$ bo'lganda, $f(5)$ ni "$f \cdot 5$" deb hisoblab, $f$
ning noma'lum son ekanligini o'ylab chalkashib ketish.
To'g'ri: $f$ shunchaki funksiya nomi, son emas; $f(5)$ — "$f$ funksiyasining
$5$ nuqtadagi qiymati," ko'paytma emas. $f(5) = 2(5)+3 = 13$.

*(Research basis: reading `f(x)` as "f times x" rather than "f evaluated at
x" is documented as a genuine, repeated conceptual misread across
ACT/SAT/classroom sources — see `research/04`.)*

**Ikkinchi xato — manfiy sonni qavssiz qo'yish:**
Noto'g'ri: $f(x) = x^2$ bo'lganda, $f(-4)$ ni hisoblashda qavssiz
$-4^2 = -16$ deb yozish.
To'g'ri: manfiy son har doim qavs ichida qo'yiladi: $f(-4) = (-4)^2 = 16$.
Qavssiz yozilsa, ishora xato chiqadi.

*(Research basis: dropping parentheses when substituting a negative value —
computing `3 · -2²` instead of `3(-2)²`, silently flipping the sign — is
documented in `research/04` as a recurring function-notation error, and
directly connects back to Lesson 1's order-of-operations grouping rules.)*

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Coordinate plane | Koordinatalar tekisligi |
| x-axis / y-axis | Abssissalar o'qi (Ox) / Ordinatalar o'qi (Oy) |
| Origin | Koordinata boshi |
| Ordered pair / coordinates | Son juftligi / Koordinatalar |
| Quadrant | Chorak (kvadrant) |
| Linear function | Chiziqli funksiya |
| Slope (angle coefficient) | Burchak koeffitsienti ($k$) / Slope ($m$) |
| y-intercept (constant term) | Erkin had ($b$) |
| Function notation | Funksiya belgilanishi |
| f(x), "f of x" | $f(x)$, "f dan x" |
| Evaluate a function | Funksiyaning qiymatini hisoblash |

---

## Notes for the problems file (Sets 1–7)

- Set 1: pure drill — identify the quadrant from given coordinates.
- Set 2: extract $k$ and $b$ from various forms of $y=kx+b$, including
  implicit-coefficient ($y=x-5$), no-constant ($y=4x$), and constant-function
  ($y=-6$) edge cases that test real understanding, not pattern-matching.
- Set 3: evaluate $f(a)$ for simple linear functions, positive inputs.
- Set 4: evaluate $f(a)$ with **negative inputs specifically** — directly
  targets the parentheses-dropping mistake, including on a squared term.
- Set 5: mixed — convert between $y=kx+b$ and $f(x)$ notation, evaluate, and
  solve for $x$ given $f(x)$ (light reverse-direction practice).
- Set 6: spot-the-error — both documented mistakes (f(x) as multiplication,
  dropped parentheses) plus a quadrant-sign misread and a simple equation-
  solving slip, for variety.
- Set 7 (bonus/challenge): quadratic $f(x)$, solving for $a$ given $f(a)$,
  solving for an unknown coefficient given $f(2)$ — closer to real SAT
  function-notation item density.
