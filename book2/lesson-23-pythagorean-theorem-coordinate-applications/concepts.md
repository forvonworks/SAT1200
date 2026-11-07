# Book 2 — Lesson 23: Pythagorean Theorem & Coordinate Applications

**Source content file.** This is the **last lesson of Book 2** — it closes the
Geometry & Trigonometry domain and, with it, the whole book. It builds
directly on Lesson 19 (triangle basics — what counts as a right angle, how a
triangle's angles/sides relate), Lesson 22 (right-triangle trigonometry — the
Pythagorean theorem and the trig ratios both live inside the same right
triangle, and knowing one often gets you the side you need for the other),
and Book 2 Lesson 3 (Linear Functions & Graphing — the coordinate plane,
plotting points, and slope are already fluent skills here, not new ones).

Per `research/04-common-student-mistakes.md`: **"Applying the Pythagorean
theorem to a triangle that is not a right triangle" is named as one of the
most-cited conceptual geometry errors on the SAT** — some students treat
"hypotenuse" as simply meaning "the longest side of any triangle," rather
than specifically the side opposite the right angle *in a right triangle*.
The research also flags SAT figures as **not guaranteed to be drawn to
scale** and not always marking the right angle explicitly, and separately
flags **"treating the missing side as always the hypotenuse"** — misapplying
$a^2+b^2=c^2$ even when the unknown side is actually a leg. Both get
dedicated, explicit treatment below, not a one-line warning.

Because this lesson closes Book 2, its last problem set (Set 7) deliberately
pulls in slope and equation-solving from earlier lessons — not as review, but
because the distance formula genuinely lives at the intersection of geometry
and coordinate algebra, and that intersection is exactly what Book 2 has been
building toward.

---

## Concept 1 — Pifagor Teoremasi (The Pythagorean Theorem)

### Definition

*To'g'ri burchakli uchburchakning to'g'ri burchak tomonlarini tashkil etuvchi
ikki tomoni **katetlar** deb, to'g'ri burchakka qarshi turgan, undan eng
uzun tomoni **gipotenuza** deb ataladi. Katetlarning kvadratlari yig'indisi
gipotenuzaning kvadratiga teng bo'lishini bildiruvchi qoida **Pifagor
teoremasi** deb ataladi:*

$$a^2+b^2=c^2$$

<small>(The two sides forming the right angle of a right triangle are
called legs; the side opposite the right angle — the longest side — is
called the hypotenuse. The Pythagorean theorem says the sum of the squares
of the legs equals the square of the hypotenuse.)</small>

### Diqqat — bu teorema FAQAT to'g'ri burchakli uchburchaklar uchun ishlaydi

Bu — butun darsning eng muhim ogohlantirishi, shuning uchun alohida ajratib
ko'rsatilmoqda, pastda yashiringan izoh sifatida emas. $a^2+b^2=c^2$
formulasini **faqat** uchburchakda to'g'ri burchak borligi aniq berilgan
yoki chizmada belgilangan holatda qo'llash mumkin. Uchburchak "to'g'ri
burchakka o'xshab ko'rinsa" ham, buning o'zi yetarli emas — SAT'dagi
chizmalar **masshtabga mos chizilishi shart emas**, va ko'pincha to'g'ri
burchak maxsus belgi (kichik kvadratcha) bilan ko'rsatilmasa, u umuman
mavjud emas deb hisoblanishi kerak.

**Noto'g'ri qo'llash:** uchburchakning tomonlari $6$, $7$, $9$ berilgan,
hech qanday to'g'ri burchak belgilanmagan. Shunga qaramay, $6^2+7^2=9^2$ deb
yozib, "gipotenuza $9$" deyish — bu xato, chunki hech kim bu uchburchakning
to'g'ri burchakli ekanini aytmagan (va haqiqatda, $36+49=85\ne81$, demak bu
umuman to'g'ri burchakli uchburchak emas).

**To'g'ri qo'llash:** tomonlari $3$ va $4$ bo'lgan ikki katet orasida to'g'ri
burchak borligi chizmada aniq belgilangan holatda: $3^2+4^2=c^2$,
$9+16=25$, $c=\sqrt{25}=5$.

**Uch tomon berilib, "bu to'g'ri burchakli uchburchakmi?" deb so'ralganda**
(to'g'ri burchak berilmagan, aksincha so'ralmoqda) — teskari tekshiruv
qo'llanadi: eng uzun tomonning kvadratini qolgan ikki tomon kvadratlari
yig'indisi bilan solishtiring. Agar teng bo'lsa — ha, to'g'ri burchakli;
agar teng bo'lmasa — yo'q.

### Model Example (1-misol)

To'g'ri burchak $9$ va $12$ uzunlikdagi ikki katet orasida joylashgan.
Gipotenuzani toping.

**Yechish:** To'g'ri burchak berilgani aniq ko'rsatilgan, demak teorema
qo'llanadi: $9^2+12^2=c^2$. $81+144=225$. $c=\sqrt{225}=15$.

**Javob:** $c=15$

### Your-Turn Example (O'zingiz bajaring)

To'g'ri burchak $8$ va $15$ uzunlikdagi ikki katet orasida joylashgan.
Gipotenuza $= \underline{\hspace{25mm}}$

### Common Mistake Box

**Birinchi xato (asosiy, tadqiqotda tasdiqlangan):** teoremani to'g'ri
burchagi berilmagan yoki belgilanmagan uchburchakka qo'llash — "gipotenuza"
so'zini shunchaki "eng uzun tomon" deb tushunib, uni har qanday uchburchakka
qo'llash mumkin deb o'ylash. **To'g'ri qoida:** gipotenuza faqat to'g'ri
burchakka qarshi turgan tomon — va bu tushuncha faqat to'g'ri burchakli
uchburchakda mavjud.

**Ikkinchi xato (ham tasdiqlangan):** noma'lum tomonni har doim gipotenuza
deb hisoblash, garchi u aslida katet bo'lsa ham. Masalan, gipotenuza $13$,
bir katet $5$ berilgan bo'lsa, noto'g'ri yondashuv $5^2+13^2=x^2$ deb yozib,
$x$ ni "yangi gipotenuza" sifatida hisoblaydi. **To'g'ri qoida:** avval qaysi
tomon gipotenuza (eng uzun, to'g'ri burchakka qarshi) ekanini aniqlang, so'ng
formulani shunga mos tartibda yozing: $5^2+x^2=13^2$, demak
$x=\sqrt{169-25}=\sqrt{144}=12$.

---

## Concept 2 — Masofa Formulasi (The Distance Formula)

### Definition

*Koordinata tekisligida $(x_1,y_1)$ va $(x_2,y_2)$ nuqtalari orasidagi
masofa quyidagi formula bilan topiladi:*

$$d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

<small>(The distance between two points on the coordinate plane is found
with this formula.)</small>

**Bu formula qayerdan kelib chiqadi — yangi qoida emas, eski teoremaning
o'zi.** Ikki nuqta $(x_1,y_1)$ va $(x_2,y_2)$ orasida to'g'ri chiziq
chizilganda, shu chiziqni gipotenuza qilib, gorizontal va vertikal
tomonlardan iborat to'g'ri burchakli uchburchak hosil qilish mumkin:
gorizontal katet $=|x_2-x_1|$ (o'ngga/chapga necha birlik), vertikal katet
$=|y_2-y_1|$ (yuqoriga/pastga necha birlik), va bu ikki o'q doim bir-biriga
to'g'ri burchak ostida kesishadi — demak bu har doim, istisnosiz, to'g'ri
burchakli uchburchak. Pifagor teoremasini to'g'ridan-to'g'ri qo'llasak:

$$(\text{gorizontal katet})^2+(\text{vertikal katet})^2=d^2 \quad\Rightarrow\quad d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

Shuning uchun masofa formulasi alohida yodlanadigan yangi qoida emas — bu
Pifagor teoremasining koordinata tekisligidagi aniq bir holati.

**Ishora haqida (sign-error ogohlantirish):** $(x_2-x_1)$ yoki $(y_2-y_1)$
manfiy chiqishi mumkin — masalan, $2-7=-5$. Bu hech qanday muammo emas,
chunki keyingi qadam uni kvadratga ko'taradi, va $(-5)^2=25$, xuddi $5^2=25$
kabi. Xato aynan shu yerda paydo bo'ladi: ba'zi o'quvchilar $(-5)^2$ ni
noto'g'ri $-25$ deb hisoblaydi (manfiy sonni kvadratga ko'tarishda ishorani
saqlab qoladi). Kvadratga ko'tarilgan har qanday haqiqiy son — musbat yoki
manfiy bo'lsin — doim musbat natija beradi.

### Model Example (2-misol)

$(2,3)$ va $(7,15)$ nuqtalari orasidagi masofani toping.

**Yechish:** $d=\sqrt{(7-2)^2+(15-3)^2}=\sqrt{5^2+12^2}=\sqrt{25+144}=\sqrt{169}=13$.

**Javob:** $d=13$

### Your-Turn Example (O'zingiz bajaring)

$(-4,1)$ va $(4,7)$ nuqtalari orasidagi masofa $= \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** $(x_2-x_1)^2$ o'rniga $(x_2-x_1)$ ni kvadratga ko'tarmasdan
to'g'ridan-to'g'ri ishlatish — masalan, $(1,5)$ va $(4,1)$ nuqtalari uchun
$\sqrt{3^2+(-4)}=\sqrt{9-4}=\sqrt5$ deb hisoblash (ikkinchi ayirmani
kvadratga ko'tarishni unutib).

**To'g'ri:** har ikki ayirma ham, istisnosiz, kvadratga ko'tariladi:
$\sqrt{3^2+(-4)^2}=\sqrt{9+16}=\sqrt{25}=5$.

---

## Concept 3 — Pifagor Uchliklari va Kitob 2 Yakuni

### Definition

*Uchta musbat butun son $a$, $b$, $c$ bo'lib, $a^2+b^2=c^2$ shartini
qanoatlantirsa, ular **Pifagor uchligi** deb ataladi.*

<small>(Three positive integers satisfying $a^2+b^2=c^2$ are called a
Pythagorean triple.)</small>

Eng tez-tez uchraydigan uchliklarni yodlab olish ildiz ostidagi hisoblashni
butunlay chetlab o'tishga yordam beradi — bu test paytida vaqtni tejaydigan
amaliy vosita, yangi nazariya emas:

| Asosiy uchlik | Keng tarqalgan ko'paytmalari |
|---|---|
| $3,4,5$ | $6,8,10$ \ \ $9,12,15$ \ \ $12,16,20$ |
| $5,12,13$ | $10,24,26$ |
| $8,15,17$ | — |
| $7,24,25$ | — |
| $9,40,41$ | — |
| $20,21,29$ | — |

**Diqqat:** har bir uchlikni ko'paytmalari ham ishlaydi — $3,4,5$ ni $2$ ga
ko'paytirsak $6,8,10$ chiqadi, bu ham to'g'ri Pifagor uchligi. Lekin har bir
to'g'ri burchakli uchburchakning tomonlari uchlikka tushishi SHART emas —
ko'pincha javob $\sqrt2$, $\sqrt{10}$ kabi irratsional son bo'ladi, va bu
normal (Kontseptlar 1-2 dagi misollar buni ko'rsatadi).

### Kitob 2 yakuniga qisqa izoh

Bu dars bilan Kitob 2 yopiladi. Oxirgi masalalar to'plami (Set 7) ataylab
burchak koeffitsienti (Dars 3) va tenglama yechish (Dars 1) bilan
birlashtirilgan — bu qayta takrorlash emas, balki haqiqiy ko'rsatkich: SAT
geometriya savollari deyarli har doim koordinata algebrasi bilan
birlashtiriladi, va Pifagor teoremasi/masofa formulasi aynan shu
birlashmaning markazida turadi.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Right triangle | To'g'ri burchakli uchburchak |
| Leg | Katet |
| Hypotenuse | Gipotenuza |
| Pythagorean theorem | Pifagor teoremasi |
| Pythagorean triple | Pifagor uchligi |
| Distance formula | Masofa formulasi |
| Converse (of a theorem) | Teskari tasdiq / teskari tekshiruv |

---

## Notes for the problems file (Sets 1–7)

1. Basic Pythagorean theorem — find the missing side (hypotenuse, then leg),
   right angle always explicitly given.
2. Recognize-and-decide — apply/don't-apply set, directly targeting the
   named misapplication gap; includes converse-check items (given 3 sides,
   is it a right triangle?).
3. Distance formula drill — includes a horizontal case, a vertical case,
   and one irrational (√2) result to normalize non-integer answers.
4. Pythagorean triples speed set — recognize common triples and scaled
   multiples without computing from scratch.
5. Mixed real-world word problems (ladder, TV diagonal, navigation,
   coordinate "cities," rectangular diagonal, baseball diamond).
6. Spot the error — five distinct error flavors: misapplication to a
   non-right triangle (×2, including a "close enough" trap), hypotenuse
   misidentification, distance-formula squaring/sign error, forgetting the
   final square root.
7. Bonus/capstone — combines distance formula with slope (Lesson 3) and
   equation-solving (Lesson 1), closing Book 2.
