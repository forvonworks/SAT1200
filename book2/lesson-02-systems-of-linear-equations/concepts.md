# Book 2 — Lesson 2: Systems of Linear Equations

**Source content file.** Structure follows `research/14-design-spec.md` §6/§10's
content-block pattern: Definition → Model example → Your-turn → common-mistake
box → Vocabulary, repeated per concept. Algebra domain, ~35% of SAT Math
(`research/01-official-sat-math-spec.md`).

**Book 2 framing:** unlike Book 1's bare fundamentals, Book 2 lessons are
taught to real SAT depth and rigor — including the test's own favorite twist
on this topic: asking for a *derived* quantity ($x+y$, $2x-y$), not $x$ and
$y$ themselves, and asking "for what value of $k$" a system has no solution or
infinitely many. Both are worked in below, not left as an afterthought.

**Research grounding:** `research/04-common-student-mistakes.md` names, for
this exact topic: arithmetic/sign slips during elimination (especially when a
row must be multiplied by a negative first), substituting a correct value
back into the wrong equation or the wrong *target* expression, picking
substitution vs. elimination poorly (creating more arithmetic than
necessary), and — the most interesting one — a genuine conceptual gap where
students learn "solve for x and y" as a memorized procedure without ever
building a mental model of what a solution geometrically *is* (an
intersection point), which is exactly why they miss the no-solution/
infinite-solutions cases.

---

## Concept 1 — Tenglamalar Sistemasi va Uning Yechimi

### Definition

*Bir nechta tenglamadan iborat bo'lib, ularning barchasini bir vaqtda
qanoatlantiruvchi $(x, y)$ qiymatlar juftligi talab qilinadigan to'plam
tenglamalar sistemasi deb ataladi. Sistemaning yechimi — grafik jihatdan, bu
ikkala tenglama chizig'ining kesishish nuqtasidir; algebraik jihatdan, bu
har ikkala tenglamani ham to'g'ri tenglikka aylantiradigan $(x,y)$ juftligidir.*

<small>(A system of equations is a set of two or more equations that must be
satisfied simultaneously by the same $(x,y)$ pair. Graphically, the solution
is the point where the lines cross. Algebraically, it's the $(x,y)$ pair that
makes *both* equations true at once.)</small>

**Nega bu tushuncha, shunchaki protsedura emas:** "yechim" nima ekanini
tushunmasdan faqat $x$ va $y$ ni topish qadamlarini yodlab olgan o'quvchi,
keyinroq (Concept 4) "yechimsiz" yoki "cheksiz ko'p yechim" holatlarida
adashadi — chunki ular bu tushunchani sinab ko'rishni emas, faqat protsedurani
bilishadi.

### Model Example (1-misol)

$(x,y)=(2,3)$ juftligi quyidagi sistemaning yechimi ekanligini tekshiring:
$$x+y=5, \qquad 2x-y=1$$

**Yechish:** Har ikkala tenglamaga alohida qo'yib ko'ramiz. Birinchi tenglama:
$2+3=5$ — to'g'ri. Ikkinchi tenglama: $2(2)-3=4-3=1$ — bu ham to'g'ri. Ikkala
tenglama ham qanoatlantirilgani uchun, $(2,3)$ chindan ham yechimdir.

**Javob:** Ha, $(2,3)$ — yechim.

### Your-Turn Example (O'zingiz bajaring)

$(x,y)=(4,1)$ juftligi quyidagi sistemaning yechimi ekanligini tekshiring:
$3x-y=11$, $x+2y=6$. Javob: $\underline{\hspace{25mm}}$

---

## Concept 2 — O'rniga Qo'yish Usuli (Substitution Method)

### Definition

*Tenglamalardan birida bitta o'zgaruvchi ikkinchisi orqali ifodalangan bo'lsa,
shu ifodani ikkinchi tenglamaga qo'yib, bitta noma'lumli tenglamaga
keltirish usuli o'rniga qo'yish usuli deb ataladi.*

<small>(When one equation already expresses one variable in terms of the
other, substitution plugs that expression into the second equation, reducing
the system to a single-variable equation.)</small>

### Model Example (2-misol)

$$y = 2x - 1, \qquad 3x + y = 9$$

**Yechish:** Birinchi tenglamada $y$ allaqachon $x$ orqali ifodalangan.
Shuni ikkinchi tenglamaga qo'yamiz: $3x + (2x-1) = 9$. O'xshash hadlarni
qo'shamiz: $5x - 1 = 9$, demak $5x = 10$, $x = 2$. Endi $x=2$ ni birinchi
tenglamaga qo'yamiz: $y = 2(2)-1 = 3$.

**Javob:** $(x,y) = (2,3)$

### Your-Turn Example (O'zingiz bajaring)

$$y = -x + 7, \qquad 3x + y = 15 \;\Rightarrow\; (x,y) = \underline{\hspace{25mm}}$$

---

## Concept 3 — Qo'shish-Ayirish (Elimination) Usuli

### Definition

*Ikkala tenglamani mos koeffitsientlar bir-birini yo'qotadigan tarzda
ko'paytirib, so'ngra ularni qo'shish yoki ayirish orqali bitta o'zgaruvchini
yo'qotish usuli qo'shish-ayirish usuli (elimination) deb ataladi. Ba'zan bu
ishlashdan oldin, tenglamalardan birini mos songa ko'paytirish kerak bo'ladi.*

<small>(Elimination multiplies one or both equations so that one variable's
coefficients match (or are opposite), then adds or subtracts the equations to
cancel that variable. Sometimes you must multiply one equation first before
anything cancels.)</small>

### Model Example (3-misol)

$$x + 2y = 11, \qquad 3x + y = 18$$

**Yechish:** $y$ ni yo'qotish uchun, ikkinchi tenglamani $2$ ga ko'paytiramiz:
$6x + 2y = 36$. Endi bu yangi tenglamadan birinchisini ayiramiz:
$(6x+2y) - (x+2y) = 36 - 11$, ya'ni $5x = 25$, demak $x = 5$. $x=5$ ni
$x+2y=11$ ga qo'yamiz: $5+2y=11$, $2y=6$, $y=3$.

**Javob:** $(x,y) = (5,3)$

### Your-Turn Example (O'zingiz bajaring)

$$2x + y = 12, \qquad x + 3y = 16 \;\Rightarrow\; (x,y) = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Tenglamalarni ayirishda, faqat bitta hadning ishorasini
o'zgartirib, qolganlarini unutish.

**To'g'ri:** Bir tenglamani ikkinchisidan ayirganda, **ayirilayotgan
tenglamaning HAR BIR hadi** ishorasini o'zgartiradi — faqat bittasi emas.
Masalan, $(6x+2y) - (x+2y)$ da $-x$ **va** $-2y$ ikkalasi ham bo'lishi kerak:
$6x+2y-x-2y = 5x+0y = 5x$. Agar faqat $x$ hadining ishorasi o'zgartirilsa va
$2y$ unutilsa, natija $5x+2y$ bo'lib qoladi — bu esa $y$ ni yo'qotmaydi, butun
usulning maqsadini buzadi. *(Tadqiqotda bu "elimination paytidagi ishora
xatolari" eng ko'p uchraydigan amaliy xato sifatida qayd etilgan —
`research/04`.)*

---

## Concept 4 — Maxsus Holatlar: Yechimsiz va Cheksiz Ko'p Yechim

### Definition

*Agar ikkala tenglama grafik jihatdan parallel chiziqlarni (bir xil qiyalik,
boshqa boshlang'ich nuqta) ifodalasa, sistema yechimga ega emas — bunday
sistema yechimsiz (no solution) deb ataladi. Agar ikkala tenglama aslida
bitta chiziqni ifodalasa (bir-birining karrasi), sistema cheksiz ko'p yechimga
ega bo'ladi.*

<small>(If both equations represent parallel lines — same slope, different
intercept — the system has no solution. If both equations represent the
exact same line, the system has infinitely many solutions.)</small>

**Buni qanday aniqlash mumkin, protsedurasiz:** Ikkala tenglamadagi $x$ va $y$
koeffitsientlari nisbatini solishtiring. Agar nisbat teng bo'lsa-yu, erkin
hadlar (konstantalar) nisbati boshqacha bo'lsa — **yechimsiz**. Agar hamma
narsa (koeffitsientlar ham, konstanta ham) bir xil nisbatda bo'lsa —
**cheksiz ko'p yechim**. Agar koeffitsientlar nisbati teng bo'lmasa — oddiy,
bitta yechimli sistema.

### Model Example (4-misol)

$$2x + 3y = 6, \qquad 4x + 6y = 18$$

**Yechish:** $x$ va $y$ koeffitsientlari nisbatini solishtiramiz: $4/2=2$ va
$6/3=2$ — bu nisbatlar teng, demak chiziqlar parallel. Endi konstantalarni
solishtiramiz: agar birinchi tenglama $2$ ga ko'paytirilsa, $4x+6y=12$ bo'lar
edi — lekin ikkinchi tenglamada bu $18$ ga teng, $12$ ga emas. Nisbat mos
kelmayapti.

**Javob:** Sistema yechimga ega emas (no solution) — chiziqlar parallel,
lekin bir xil emas.

### Your-Turn Example (O'zingiz bajaring)

$x - y = 2$ va $2x - 2y = 4$ sistemasini tekshiring: bitta yechimmi,
yechimsizmi, yoki cheksiz ko'p yechimmi? $\underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Har bir sistema aynan bitta yechimga ega deb o'ylash va
yechimsiz/cheksiz holatlarni butunlay hisobga olmaslik.

**To'g'ri:** Agar siz o'zgaruvchini yo'qotishga harakat qilayotganingizda
**ikkala o'zgaruvchi ham yo'qolib ketsa** (masalan, $0=12$ kabi noto'g'ri son
tenglik chiqsa), bu — yechim yo'qligini bildiradi. Agar natija **har doim
to'g'ri** bo'lsa (masalan, $0=0$), bu — cheksiz ko'p yechim borligini
bildiradi. Bu holatlar "formula ishlamay qoldi" degani emas — bu sizga
muhim ma'lumot berayotgan natija. *(SAT bu holatni ayniqsa "nechta $k$
qiymatida sistema yechimga ega emas?" kabi savollar orqali to'g'ridan-to'g'ri
sinaydi — `research/04`.)*

---

## SAT-Specific Check — "Nima So'ralmoqda?" (What Is Actually Being Asked?)

Tadqiqotda eng ko'p takrorlangan xato turi shu: tenglamani to'g'ri yechib,
keyin **savol so'ragan narsani emas**, oddiygina $x$ yoki $y$ ni javob qilib
yozish.

### Model Example (5-misol)

$$x+y=10, \qquad x-y=2$$

Savol: *$xy$ ning qiymati nechaga teng?* ($x$ yoki $y$ emas!)

**Yechish:** Avval odatdagidek yechamiz: tenglamalarni qo'shib, $2x=12$,
$x=6$; so'ng $y=10-6=4$. Lekin savol $x$ ni emas, $xy$ ni so'ragan — shuning
uchun oxirgi qadam sifatida $x$ va $y$ ni ko'paytiramiz: $6 \times 4 = 24$.

**Javob:** $xy = 24$ (javob $x=6$ yoki $y=4$ emas — ikkalasini ham hisoblab,
so'ralgan amalni oxirida bajarish kerak).

**Qoida:** Har doim tenglamani yechib bo'lgach, savolni qaytadan o'qing — u
$x$ ni, $y$ ni, yoki ularning biror kombinatsiyasini ($x+y$, $2x-y$, $xy$,
va hokazo) so'rayaptimi?

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| System of equations | Tenglamalar sistemasi |
| Solution (of a system) | Yechim |
| Substitution method | O'rniga qo'yish usuli |
| Elimination method | Qo'shish-ayirish usuli |
| Intersection point | Kesishish nuqtasi |
| Parallel lines | Parallel chiziqlar |
| No solution | Yechimsiz |
| Infinitely many solutions | Cheksiz ko'p yechim |

---

## Notes for the problems file (Sets 1–7)

1. Pure substitution drill.
2. Pure elimination drill, including items that require multiplying one
   equation first (per Concept 3).
3. Mixed — student chooses the method (tests the "choosing poorly creates
   more arithmetic" mistake from `research/04` by rewarding the smarter
   choice with less work, not by requiring a specific method).
4. Special cases — classify as one-solution/no-solution/infinite, plus two
   "find the value of $k$" items matching the real SAT question format named
   in `research/04`.
5. "What's actually being asked" — solve the system, then compute a derived
   quantity ($xy$, $x+y$, $2x-y$, etc.), not $x$/$y$ alone.
6. Spot the error — sign-slip during elimination, incomplete substitution,
   and wrongly classifying a no-solution system as infinite.
7. Bonus/challenge — harder coefficients, a sum/difference word pair, and a
   second "find $k$" item.
