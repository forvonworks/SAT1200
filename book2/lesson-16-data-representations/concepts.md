# Book 2 — Lesson 16: Data Representations

**Source content file**, paired with `problems.md`. Covers reading one-way
frequency tables, two-way tables (the lesson's main payoff), and scatterplots.
Builds directly on Lesson 15 (mean/median/mode, spread) — the same data skills
now show up *packaged inside a table or graph* instead of a plain list of
numbers — and reuses Lesson 14's percent-in-context fluency for every
percentage computed from a table cell. Per `05-uzbek-student-considerations.md`,
data/statistics topics are underweighted in the local curriculum, so this
lesson assumes no prior comfort with reading tables as data objects — it
starts from "what a frequency table even is," not from two-way tables
directly.

---

## Concept 1 — Chastota jadvali (Frequency Table)

### Ta'rif (Definition)

Ma'lum bir to'plamdagi har bir qiymat yoki toifaning necha marta uchrashini
ko'rsatadigan jadval **chastota jadvali** (frequency table) deb ataladi.
Jadvalning oxirgi qatori odatda **jami (total)** qiymatni ko'rsatadi — bu
barcha chastotalarning yig'indisidir: $\text{jami} = \sum(\text{har bir
toifaning chastotasi})$.

*(A frequency table shows how many times each value or category occurs; its
total row is the sum of every individual frequency.)*

### Model Example (1-misol)

50 nafar o'quvchidan "Eng sevimli fan qaysi?" deb so'ralgan va natijalar
quyidagi jadvalda keltirilgan:

| Fan | O'quvchilar soni |
|---|---|
| Matematika | 18 |
| Fizika | 9 |
| Biologiya | 13 |
| Tarix | 10 |
| **Jami** | **50** |

**Savol:** Matematikani tanlagan o'quvchilar jamining necha foizini tashkil
qiladi?

**Yechish:** Avval jadvalda matematika qatoridagi sonni topamiz: $18$.
Shartga ko'ra jami o'quvchilar soni $50$. Foizni topish uchun qismni jamiga
bo'lib, $100$ ga ko'paytiramiz: $\dfrac{18}{50}\times100\% = 36\%$.

**Javob:** $36\%$

### Your-Turn Example (O'zingiz bajaring)

Xuddi shu jadvalda biologiyani tanlagan o'quvchilar jamining necha foizini
tashkil qiladi? $= \underline{\hspace{25mm}}$

---

## Concept 2 — Ikki tomonlama jadval (Two-Way Table)

### Ta'rif (Definition)

Bir vaqtning o'zida ikki xil belgi (masalan, jins va sport turi) bo'yicha
ma'lumotni qator va ustunlarda birgalikda ko'rsatadigan jadval **ikki
tomonlama jadval** (two-way table) deb ataladi. Har bir qatorning o'z
**qator jami**si, har bir ustunning o'z **ustun jami**si bo'ladi, va
jadvalning pastki-o'ng burchagida hammasini qamrab oluvchi **umumiy jami
(grand total)** turadi — bu yerda o'quvchilar ikki marta sanalmaydi, faqat
bitta guruh ikki xil belgi bo'yicha birga ko'rsatiladi.

*(A two-way table records two categorical facts about the same group of
people at once — row totals, column totals, and one grand total, with no
one counted twice.)*

### Model Example (2-misol)

90 nafar o'quvchidan jinsi va yoqtirgan sport turi so'ralgan:

| | Basketbol | Voleybol | **Qator jami** |
|---|---|---|---|
| **Qizlar** | 14 | 26 | **40** |
| **Yigitlar** | 33 | 17 | **50** |
| **Ustun jami** | **47** | **43** | **90** |

**Yechish (jadvalni o'qish):** Har bir katakcha ikkala belgining kesishgan
joyidagi sonni ko'rsatadi — masalan, $26$ soni "voleybolni tanlagan
qizlar" sonini bildiradi, "voleybolni tanlagan barcha o'quvchilar" sonini
emas (bu $43$). Qator jami ($40$, $50$) — har bir jinsning umumiy soni.
Ustun jami ($47$, $43$) — har bir sportni tanlaganlarning umumiy soni.
Umumiy jami ($90$) — ikkalasi ham to'g'ri hisoblanganini tekshirish uchun:
$40+50=90$ va $47+43=90$.

### Qaysi Guruh Haqida So'ralmoqda? (Nima Aniq So'ralayotganini Tekshirish)

Ikki tomonlama jadvaldagi eng ko'p xato — **noto'g'ri maxrajni tanlash**.
Savolning so'z tartibi qaysi sonni maxraj (bo'linuvchi) qilib olish kerakligini
aniq ko'rsatadi:

- **"Qizlarning necha foizi voleybolni tanladi?"** — bu yerda gap avval
  **qizlar** haqida (ularning "necha foizi" so'ralmoqda), demak maxraj —
  faqat qizlar guruhi ichida qolamiz: qizlar qator jami $=40$.
  $\dfrac{26}{40}\times100\%=65\%$.
- **"Voleybolni tanlagan o'quvchilar ichida necha foizi qiz?"** — bu yerda
  gap avval **voleybolni tanlaganlar** haqida, demak maxraj — voleybol
  ustun jami $=43$. $\dfrac{26}{43}\times100\%\approx60.5\%$.

Ikkala savol xuddi shu $26$ sonidan foydalanadi, lekin **turli maxrajlar**
bilan — va javoblar har xil ($65\%$ va $\approx60.5\%$). Bunda, qaysi
guruh "ichida" so'ralganini — qator ($40$ yoki $50$), ustun ($47$ yoki
$43$) yoki butun jadval ($90$) — har safar savolni qayta o'qib aniqlash
kerak, javobni ko'rinishidan taxmin qilish emas.

*(Diqqat — ishora/yo'nalish eslatmasi: ikki guruh orasidagi farqni
hisoblashda ham tartib muhim — "A dan B qancha ko'p" uchun kattasidan
kichigini ayirish kerak, aks holda manfiy javob chiqadi va bu javobning
ma'nosi noto'g'ri bo'lib qoladi.)*

### Umumiy Xato (Common Mistake)

**Noto'g'ri yechim:** "Voleybolni tanlagan o'quvchilar ichida necha foizi
qiz?" — *"$\dfrac{26}{40}=65\%$, demak javob $65\%$."*

**Xato nimada:** Savol "voleybolni tanlaganlar ICHIDA" deb so'ragan, ya'ni
maxraj voleybol ustun jamisi ($43$) bo'lishi kerak edi, lekin $40$ (qizlar
qator jami) ishlatilgan.

**To'g'ri yechim:** $\dfrac{26}{43}\times100\%\approx60.5\%$.

### Your-Turn Example (O'zingiz bajaring)

Xuddi shu jadvalda: yigitlarning necha foizi basketbolni tanladi?
$= \underline{\hspace{25mm}}$

---

## Concept 3 — Sochilish diagrammasi (Scatterplot)

### Ta'rif (Definition)

Ikki sonli miqdor orasidagi bog'lanishni har bir kuzatuvni tekislikda bitta
nuqta sifatida tasvirlab ko'rsatadigan diagramma **sochilish diagrammasi**
(scatterplot) deb ataladi. Nuqtalar chapdan o'ngga qarab umuman olganda
yuqoriga ko'tarilib borsa, bu **musbat bog'lanish (positive correlation)**ni;
pastga tusha borsa, **manfiy bog'lanish (negative correlation)**ni bildiradi;
nuqtalar tartibsiz tarqalgan bo'lsa, aniq bog'lanish yo'q deyiladi.

*(Notation note: SAT odatda bog'lanishni son — "r qiymati" — bilan emas, so'z
bilan tasvirlashni so'raydi: "kuchli musbat," "zaif manfiy," "bog'lanish
yo'q." Shu so'zlarni ishlatishni o'rganish kifoya, r formulasi kerak emas.)*

### Model Example (3-misol)

7 nafar talabaning haftalik mashq soati ($x$) va yugurgan masofasi, km
($y$) ro'yxatga olindi: $(2,4),\ (3,5),\ (4,7),\ (5,8),\ (5,10),\ (7,12),\
(8,13)$.

**Yechish:** $x$ qiymatlari o'sib borgani sari, $y$ qiymatlari ham umuman
olganda o'sib boradi (ba'zi joyda bir xil $x=5$ da ikki xil $y$ bo'lsa
ham — bu normal, real ma'lumotlar mukammal chiziqda yotmaydi). Demak,
nuqtalar o'rtasida **musbat bog'lanish** bor.

**Diqqat — bog'lanish sabab-oqibat emas:** Bu ma'lumotlar mashq ko'paygani
SABAB BO'LIB yugurish masofasini oshirishini ISBOTLAMAYDI — faqat ikkisi
birga o'sish tendensiyasida ekanligini ko'rsatadi. Boshqa omillar (masalan,
umumiy jismoniy tayyorgarlik) ham ikkalasiga ta'sir qilishi mumkin.

### Your-Turn Example (O'zingiz bajaring)

Yangi ma'lumotlar to'plamida $x$ oshgani sari $y$ kamayib boradi. Bu qanday
bog'lanish turi? $= \underline{\hspace{25mm}}$

### Umumiy Xato (Common Mistake)

**Noto'g'ri yechim:** "Diagrammada mashq soati bilan yugurish masofasi
orasida musbat bog'lanish bor, demak mashq qilish YUGURISH QOBILIYATINI
OSHIRISHGA SABAB BO'LADI."

**Xato nimada:** Bog'lanish (correlation) borligi sabab-oqibat
(causation) borligini anglatmaydi — boshqa omillar hisobga olinmagan,
demak "sabab bo'ladi" degan xulosa ma'lumotlardan kelib chiqmaydi.

**To'g'ri yechim:** "Ma'lumotlar mashq soati va yugurish masofasi orasida
musbat bog'lanish borligini ko'rsatadi" — sabab-oqibat haqida hech narsa
da'vo qilmasdan.

---

## Vocabulary

| O'zbek | English |
|---|---|
| Chastota jadvali | Frequency table |
| Jami / Qator jami / Ustun jami | Total / Row total / Column total |
| Umumiy jami | Grand total |
| Ikki tomonlama jadval | Two-way table |
| Shartli ulush (guruh ichidagi foiz) | Conditional (within-group) percentage |
| Sochilish diagrammasi | Scatterplot |
| Musbat bog'lanish | Positive correlation |
| Manfiy bog'lanish | Negative correlation |
| Bog'lanish (correlation) | Correlation |
| Sabab-oqibat (causation) | Causation |
| Ekstrapolyatsiya | Extrapolation |

---

## Notes for the problems file

Seven sets, following the lesson's own concept order and deepening the
two-way-table skill specifically (per the directive):

1. Basic one-way frequency table reading (one table, several questions).
2. Two-way table — **row-conditioned** percentages (same sports table as the
   Model Example).
3. Two-way table — **column-conditioned** percentages (same table, forcing
   direct contrast with Set 2's denominators).
4. Mixed two-way table (a new table) combining row/column questions with a
   Lesson-14-style percent-increase question and a signed-difference question.
5. Scatterplot — trend description, reading an approximate value, and a
   causation/extrapolation conceptual question.
6. Spot the error — wrong-denominator mistakes (row vs. column vs. grand
   total) and one causation-claim error, each with the broken step named and
   corrected.
7. Bonus — a 3×3 two-way table, including one question where all three row
   groups give the *same* within-group percentage (testing careful
   calculation over visual guessing).
