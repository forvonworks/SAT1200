# Book 2 — Lesson 22: Right-Triangle Trigonometry

**Source content file**, paired with `problems.md`. This is the *only* trigonometry
the digital SAT tests in-domain (`research/02-topic-difficulty-taxonomy.md`) — no
unit circle, no identities beyond the one complementary-angle relationship taught
below. Builds on Lesson 19 (Lines, Angles & Triangles): triangle angle-sum and
similarity are already established and are *not* re-taught here. For most students
this is genuinely new vocabulary — sine, cosine, and tangent are not assumed to be
familiar words, even though the arithmetic involved (multiply, divide, look up a
calculator value) is simple once the setup is correct.

**Research grounding:** `research/04-common-student-mistakes.md`'s Trigonometry
section names "mixing up sine and cosine by misidentifying which side is opposite
vs. adjacent" as *the single most common SAT trig mistake* — distractor answer
choices are frequently built directly around this exact error. The same source
also names "not re-identifying opposite/adjacent when the reference angle
changes," the complementary-angle identity as a frequently-tested newer item
type, calculator degree/radian mode errors, and multi-step Pythagorean+trig
problems being treated as single-step. All four are addressed explicitly below.

---

## Concept 1 — The Three Ratios: Sine, Cosine, Tangent

### Definition

*To'g'ri burchakli uchburchakning o'tkir burchaklaridan biri tanlanganda,
tanlangan burchakka qarama-qarshi turgan tomon — **qarama-qarshi katet**,
tanlangan burchakka tutashgan, gipotenuzadan boshqa tomon — **qo'shni katet**
deb ataladi; to'g'ri burchakka qarama-qarshi turgan, uchburchakning eng uzun
tomoni esa **gipotenuza** deb ataladi.*

<small>(In a right triangle, once you pick one of the two acute angles, the
side across from it is called the **opposite leg**, the side touching it
(other than the hypotenuse) is called the **adjacent leg**, and the longest
side — across from the right angle — is called the **hypotenuse**.)</small>

*Berilgan o'tkir burchak uchun uning **sinusi** deb, qarama-qarshi katetning
gipotenuzaga nisbatiga aytiladi; **kosinusi** deb, qo'shni katetning
gipotenuzaga nisbatiga aytiladi; **tangensi** deb, qarama-qarshi katetning
qo'shni katetga nisbatiga aytiladi:*

$$\sin\theta = \frac{\text{qarama-qarshi katet}}{\text{gipotenuza}} \qquad
\cos\theta = \frac{\text{qo'shni katet}}{\text{gipotenuza}} \qquad
\tan\theta = \frac{\text{qarama-qarshi katet}}{\text{qo'shni katet}}$$

**Yodda qolish uchun (memory aid):** xalqaro **SOH-CAH-TOA** qisqartmasi
keng tarqalgan: **S**in = **O**pposite/**H**ypotenuse, **C**os =
**A**djacent/**H**ypotenuse, **T**an = **O**pposite/**A**djacent. Bu Uzbek
tilidagi atama emas — xuddi Lesson 1'dagi PEMDAS kabi, xalqaro yordamchi
qisqartma, asosiy tushuncha esa yuqoridagi uch nisbat o'zi.

**Notation note:** $\sin$, $\cos$, $\tan$ are *ratios* — pure numbers with no
units, even though the sides used to compute them are measured in feet,
meters, etc. (the units cancel). Don't write "$\sin 30° = 0.5$ cm" or
similar — the result is unitless.

### The Critical Point: Opposite/Adjacent Depend on *Which Angle You Pick*

**Qaysi Burchakka Nisbatan? (Relative to which angle?)** — "opposite" and
"adjacent" are **not** fixed labels glued to specific sides of a triangle.
They're defined *relative to whichever acute angle you're currently working
with*. The same leg is "opposite" for one angle and "adjacent" for the
other acute angle in the exact same triangle.

### Model Example (1-misol)

To'g'ri burchakli uchburchak $ABC$ berilgan, to'g'ri burchak — $C$ nuqtada.
Katetlar: $BC=3$, $AC=4$; gipotenuza $AB=5$. Burchak $A$ uchun $\sin A$,
$\cos A$, $\tan A$ ni toping.

**Yechish:** Burchak $A$ dan qaraganda, unga qarama-qarshi turgan tomon —
$BC=3$ (chunki $BC$ burchak $A$ ning qarshisida turadi), unga tutashgan
tomon (gipotenuzadan boshqa) — $AC=4$, gipotenuza — $AB=5$.

$$\sin A = \frac{3}{5} \qquad \cos A = \frac{4}{5} \qquad \tan A = \frac{3}{4}$$

**Endi xuddi shu uchburchak, burchak $B$ dan qaralsa:** Burchak $B$ ga
qarama-qarshi turgan tomon endi $AC=4$ (chunki $AC$ endi $B$ ning
qarshisida), unga tutashgan tomon — $BC=3$, gipotenuza o'zgarmaydi — $AB=5$.

| | Burchak $A$ dan qaralganda | Burchak $B$ dan qaralganda |
|---|---|---|
| Qarama-qarshi katet | $BC=3$ | $AC=4$ |
| Qo'shni katet | $AC=4$ | $BC=3$ |
| Gipotenuza | $AB=5$ | $AB=5$ |
| $\sin$ | $\frac{3}{5}$ | $\frac{4}{5}$ |
| $\cos$ | $\frac{4}{5}$ | $\frac{3}{5}$ |
| $\tan$ | $\frac{3}{4}$ | $\frac{4}{3}$ |

**Bir xil uchburchak, bir xil ikki katet — lekin burchak o'zgarganda, qaysi
katet "qarama-qarshi" va qaysi biri "qo'shni" ekanligi butunlay almashadi.**
Gipotenuza hech qachon o'zgarmaydi (u har doim to'g'ri burchakka qarshi
turadi, tanlangan o'tkir burchakka bog'liq emas) — faqat ikki katetning
rollari almashadi.

### Your-Turn Example (O'zingiz bajaring)

To'g'ri burchakli uchburchakda katetlar $5$ va $12$, gipotenuza $13$.
Katet $12$ ga qarama-qarshi turgan burchakni $B$ deb belgilaymiz. $\sin B$,
$\cos B$ va $\tan B$ ni toping:

$\sin B = \underline{\hspace{15mm}} \qquad \cos B = \underline{\hspace{15mm}} \qquad \tan B = \underline{\hspace{15mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Burchak $A$ uchun qarama-qarshi/qo'shni katetlarni
to'g'ri aniqlab, keyin xuddi shu belgilarni (o'zgartirmasdan) burchak $B$
uchun ham ishlatish — ya'ni, bitta burchak uchun topilgan "qarama-qarshi"
va "qo'shni" nomlarini doimiy deb o'ylash.

**To'g'ri qoida:** Har safar burchak o'zgarganda, qarama-qarshi va qo'shni
katetlarni **qaytadan** aniqlash kerak. Yuqoridagi jadvalda ko'rinib
turganidek, $BC=3$ burchak $A$ uchun qarama-qarshi, lekin burchak $B$ uchun
qo'shni katet bo'lib qoladi. Har bir masalani boshlashdan oldin, birinchi
qadam sifatida "men qaysi burchak bilan ishlayapman?" deb so'rab, keyin shu
burchakka nisbatan ikki katetni belgilash kerak.

*(Research basis: `research/04` mas trigonometry findings orasida bu ikkita
xato — sin/cos ni qarama-qarshi/qo'shni noto'g'ri aniqlash orqali almashtirib
yuborish, va burchak o'zgarganda katet nomlarini qayta aniqlamaslik — eng
ko'p uchraydigan SAT trigonometriya xatosi deb ko'rsatilgan.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Right triangle | To'g'ri burchakli uchburchak |
| Leg | Katet |
| Opposite leg | Qarama-qarshi katet |
| Adjacent leg | Qo'shni katet |
| Hypotenuse | Gipotenuza |
| Sine / Cosine / Tangent | Sinus / Kosinus / Tangens |
| Acute angle | O'tkir burchak |
| Ratio | Nisbat |

---

## Concept 2 — Solving for a Missing Side

### Definition

*Uchburchakning bir o'tkir burchagi va bir tomoni ma'lum bo'lganda, qolgan
har qanday tomonni mos trigonometrik nisbat yordamida topish mumkin: ma'lum
va noma'lum tomonlarning har biri burchakka nisbatan qaysi rolni (qarama-
qarshi, qo'shni, gipotenuza) o'ynashini aniqlab, so'ngra mos tenglamani
tuzish kerak.*

<small>(When one acute angle and one side of a right triangle are known,
any other side can be found by identifying which role — opposite, adjacent,
hypotenuse — each known/unknown side plays relative to that angle, then
setting up the matching equation.)</small>

**Qaysi nisbat — sin, cos yoki tan? (Nima So'ralmoqda?)** Qaror ikki
qadamda qabul qilinadi: (1) ma'lum tomon burchakka nisbatan qanday rol
o'ynaydi? (2) noma'lum tomon qanday rol o'ynaydi? Shu ikki rolga qarab,
mos nisbat tanlanadi:

| Ma'lum + Noma'lum | Nisbat |
|---|---|
| Gipotenuza + Qarama-qarshi | $\sin$ |
| Gipotenuza + Qo'shni | $\cos$ |
| Qo'shni + Qarama-qarshi | $\tan$ |

### Model Example (2-misol)

Gipotenuza $12$ ga, burchak $25°$ ga teng. Burchakka qarama-qarshi turgan
tomonni toping.

**Yechish:** Ma'lum tomon — gipotenuza; noma'lum tomon — qarama-qarshi
katet. Jadvalga ko'ra, bu **sinus** nisbati:

$$\sin 25° = \frac{\text{qarama-qarshi}}{12}$$

Ikkala tomonni $12$ ga ko'paytiramiz: qarama-qarshi $= 12 \times \sin 25°$.
Kalkulyatordan (gradus rejimida!) $\sin 25° \approx 0.4226$. Demak,
qarama-qarshi $\approx 12 \times 0.4226 \approx 5.07$.

**Javob:** $\approx 5.07$

### Your-Turn Example (O'zingiz bajaring)

Burchak $52°$ ga, unga qo'shni katet $15$ ga teng. Gipotenuzani toping
(eslatma: bu yerda gipotenuza — noma'lum, qo'shni — ma'lum):

$\cos 52° = \dfrac{15}{\text{gipotenuza}} \implies \text{gipotenuza} = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Kalkulyatorni **radian** rejimida qoldirib,
burchakni gradusda deb hisoblash — masalan, $\sin 30°$ ni gradus o'rniga
radian sifatida kiritish.

**To'g'ri qoida:** Kalkulyator har doim masala boshida **gradus (degree)**
rejimida ekanligini tekshirish kerak. $\sin 30° = 0.5$ (to'g'ri, gradus
rejimida), lekin agar kalkulyator "30" ni radian deb qabul qilsa, natija
butunlay boshqacha va noto'g'ri chiqadi — hech qanday ogohlantirish
bermaydi, chunki chiqqan son hali ham "normal" ko'rinadi.

*(Research basis: calculator degree/radian mode error is named explicitly
in `research/04` as a persistent, "silent" trig error — the wrong-mode
answer looks numerically plausible, so nothing tips the student off.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Known / Unknown | Ma'lum / Noma'lum |
| Degree mode | Gradus rejimi |
| Radian mode | Radian rejimi |

---

## Concept 3 — Solving for a Missing Angle, and the Complementary-Angle Identity

### Definition

*Uchburchakning ikki tomoni ma'lum bo'lganda, o'tkir burchakni topish uchun
**teskari trigonometrik funksiyalar** ($\arcsin$, $\arccos$, $\arctan$ —
ya'ni $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$) qo'llaniladi: avval mos nisbatni
hisoblab, so'ngra unga teskari funksiyani qo'llab, burchakning o'zini
topamiz.*

<small>(When two sides of a right triangle are known, the acute angle is
found using **inverse trig functions** (arcsin, arccos, arctan) — compute
the ratio first, then apply the inverse function to get the angle itself.)</small>

**Diqqat:** nisbatning qiymati (masalan, $0.28$) burchakning o'zi **emas** —
u shunchaki nisbat. Burchakni topish uchun albatta teskari funksiya
qo'llanishi kerak.

### To'ldiruvchi Burchaklar Ayniyati (The Complementary-Angle Identity)

*To'g'ri burchakli uchburchakning ikki o'tkir burchagi yig'indisi $90°$ ga
teng bo'lgani uchun, ular **to'ldiruvchi burchaklar** deb ataladi; bunday
ikki burchak uchun bir burchakning sinusi ikkinchi burchakning kosinusiga
teng bo'ladi:*

$$\sin\theta = \cos(90°-\theta)$$

Bu Concept 1'dagi katet almashinuvidan to'g'ridan-to'g'ri kelib chiqadi:
burchak $A$ uchun qarama-qarshi bo'lgan katet, aynan burchak $B=90°-A$ uchun
qo'shni katet bo'ladi — shuning uchun $\sin A = \cos B$.

### Model Example (3-misol)

To'g'ri burchakli uchburchakda qarama-qarshi katet $7$, qo'shni katet $24$,
gipotenuza $25$ ga teng ($7$-$24$-$25$ uchburchagi). Qarama-qarshi katetga
mos burchak $\theta$ ni toping, so'ngra ikkinchi o'tkir burchakni ham
to'ldiruvchi ayniyat orqali tekshiring.

**Yechish:** Avval nisbatni topamiz: $\sin\theta = \frac{7}{25} = 0.28$.
Endi teskari funksiyani qo'llaymiz: $\theta = \arcsin(0.28) \approx
16.26°$.

Ikkinchi o'tkir burchak: $90° - 16.26° = 73.74°$. To'ldiruvchi ayniyatga
ko'ra, $\cos(73.74°)$ ham $0.28$ ga teng bo'lishi kerak — va haqiqatan ham
shunday ($\cos 73.74° \approx 0.28$), chunki aynan shu $7$ katet ikkinchi
burchak uchun qo'shni katet bo'lib qoladi.

**Javob:** $\theta \approx 16.3°$ (eng yaqin o'ndan birigacha yaxlitlangan)

### Your-Turn Example (O'zingiz bajaring)

To'g'ri burchakli uchburchakda qo'shni katet $9$, gipotenuza $41$ ga teng.
Shu katetga mos burchakni toping:

$\cos\theta = \dfrac{9}{41} \implies \theta = \arccos\left(\dfrac{9}{41}\right) = \underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Nisbatni hisoblab, uni to'g'ridan-to'g'ri burchak
deb e'lon qilish — masalan, $\sin\theta = 0.6$ dan $\theta = 0.6°$ deb
xulosa chiqarish.

**To'g'ri qoida:** $0.6$ — bu nisbatning qiymati, burchakning o'zi emas.
Burchakni topish uchun albatta teskari funksiya qo'llash shart:
$\theta = \arcsin(0.6) \approx 36.9°$, $0.6°$ emas. Bu xato, boshqa
mavzularda "teskari amalni bajarishni unutish" xatosiga o'xshaydi (masalan,
tenglamada oxirgi qadamni o'tkazib yuborish) — bu yerda ham oxirgi, eng
muhim qadam — teskari funksiyani qo'llash — tashlab ketiladi.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Inverse trig function | Teskari trigonometrik funksiya |
| Arcsine / Arccosine / Arctangent | Arksinus / Arkkosinus / Arktangens |
| Complementary angles | To'ldiruvchi burchaklar |
| Angle of elevation | Ko'tarilish burchagi |
| Angle of depression | Tushish burchagi |
