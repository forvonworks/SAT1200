# Book 2 — Lesson 15: Statistics Fundamentals

**Source content file**, paired with `problems.md`. Domain: Problem-Solving &
Data Analysis. TOC entry: "Mean/median/mode, spread, outlier sensitivity."

**Why this lesson needs extra care:** per `research/05-uzbek-student-considerations.md`,
statistics and probability are structurally underweighted in the Uzbek
curriculum (Soviet-tradition math education historically treated probability
and statistics as minor/late additions, and the current Uzbek exam
specification weights "Statistika va ehtimollik" at only ~7.5% of items).
Unlike most Book 2 lessons, this one should **not** assume strong prior
fluency — treat the core definitions as genuinely new, not a refresher.

**Documented error this lesson is built around:** per
`research/04-common-student-mistakes.md`, the single most-cited statistics
mistake is *averaging two averages instead of recombining the underlying
groups* — given the mean of group A and the mean of group B, incorrectly
computing $\frac{\text{mean}_A + \text{mean}_B}{2}$ instead of
$\frac{\text{sum}_A + \text{sum}_B}{\text{count}_A + \text{count}_B}$. This
only coincidentally gives the right answer when the two groups are the same
size — which is exactly why it survives as a habit. Concept 2 below is built
entirely around exposing this.

Also per `research/04`: forgetting to sort data before finding the median,
miscounting the middle position, forgetting the even-count averaging rule,
and not knowing which measure (mean vs. median) resists an outlier are all
separately documented — each gets its own explicit callout rather than being
folded silently into a definition.

---

## Concept 1 — O'rta Qiymatlar: Arifmetik O'rta, Mediana va Moda (Measures of Center: Mean, Median, Mode)

### Definition

*Berilgan sonlar to'plamidagi barcha qiymatlarning yig'indisini qiymatlar
soniga bo'lish orqali topiladigan ko'rsatkich arifmetik o'rta (mean) deb
ataladi. Qiymatlarni o'sish tartibida tizgandan so'ng, to'plamning aynan
o'rtasida turadigan qiymat — toq sondagi qiymatlar uchun — yoki ikkita
o'rtadagi qiymatning arifmetik o'rtasi — juft sondagi qiymatlar uchun —
mediana (median) deb ataladi. To'plamda eng ko'p marta takrorlanadigan
qiymat moda (mode) deb ataladi; agar bir nechta qiymat teng darajada eng
ko'p takrorlansa, to'plam bir nechta modaga ega bo'lishi mumkin, agar hech
qanday qiymat takrorlanmasa, moda umuman mavjud bo'lmaydi.*

<small>(The result of adding every value in a data set and dividing by the
number of values is called the mean. After sorting the values in increasing
order, the exact middle value — for an odd count — or the mean of the two
middle values — for an even count — is called the median. The value that
appears most often is called the mode; a data set can have more than one
mode, or none at all.)</small>

**Nima So'ralmoqda? (What's Actually Being Asked?):** SAT statistics
questions frequently give you a data set and ask for one specific measure —
"What is the median of..." — while the distractor answers are built from the
*other* two measures. Before calculating anything, underline which of the
three (mean / median / mode) the question actually wants, so you don't
correctly compute the mean and then bubble it in for a question that asked
for the median.

### Quick Reference Table

| Atama (Term) | Formula / Qoida | Belgisi | English |
|---|---|---|---|
| Arifmetik o'rta | $\dfrac{\text{yig'indi}}{\text{son}}$ | mean, $\bar{x}$ | Mean (average) |
| Mediana | O'rtadagi qiymat (toq) / o'rtadagi ikkitaning o'rtachasi (juft) | median | Median |
| Moda | Eng ko'p takrorlangan qiymat | mode | Mode |

**Sign/count warning:** the median rule depends entirely on whether the
*count* of values is odd or even — this is a counting step, not a
calculation step, and it's worth doing explicitly every time rather than
eyeballing "the middle."

### Model Example (1-misol)

Quyidagi ma'lumotlar to'plami berilgan: $4, 8, 6, 8, 2$. Arifmetik o'rta,
mediana va modani toping.

**Yechish:** Avval yig'indini topamiz: $4+8+6+8+2=28$. Qiymatlar soni $5$
(toq son). Arifmetik o'rta: $28 \div 5 = \dfrac{28}{5} = 5.6$.

Mediana uchun avval qiymatlarni o'sish tartibida tizamiz: $2, 4, 6, 8, 8$.
Qiymatlar soni toq ($5$) bo'lgani uchun, mediana — aynan o'rtadagi (3-chi)
qiymat: $6$.

Moda — eng ko'p takrorlangan qiymat. Tizilgan qatorda $8$ ikki marta
uchraydi, qolganlari bir martadan. Demak, moda $= 8$.

**Javob:** Arifmetik o'rta $=5.6$, mediana $=6$, moda $=8$.

*(E'tibor bering: uchta javob uchtasi ham turlicha — bu tasodif emas, aksar
ma'lumotlar to'plamida shunday bo'ladi. Ular bir xil bo'lishi shart emas.)*

### Your-Turn Example (O'zingiz bajaring)

Ma'lumotlar to'plami: $10, 12, 10, 15, 13$. Arifmetik o'rta
$=\underline{\hspace{15mm}}$, mediana $=\underline{\hspace{15mm}}$, moda
$=\underline{\hspace{15mm}}$.

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Juft sondagi qiymatlar to'plamida medianani
topishda, o'rtadagi ikkita qiymatdan birini (masalan, kattasini yoki
tasodifan birinchi kelganini) mediana deb olish — ularning arifmetik
o'rtasini hisoblashni unutib qo'yish.

**To'g'ri qoida:** Qiymatlar soni juft bo'lganda, mediana — bu ikkita
o'rtadagi qiymatning o'zi emas, balki ularning arifmetik o'rtasi. Masalan,
$\{1, 3, 5, 7\}$ to'plamida o'rtadagi ikkita qiymat $3$ va $5$; mediana
$3$ ham, $5$ ham emas, balki $\dfrac{3+5}{2}=4$.

**Ikkinchi keng tarqalgan xato:** medianani topishdan oldin qiymatlarni
o'sish tartibida tizishni unutish — tizilmagan tartibda "o'rtadagi" deb
ko'ringan qiymatni olish, bu odatda noto'g'ri javob beradi.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Mean (average) | Arifmetik o'rta |
| Median | Mediana |
| Mode | Moda |
| Data set | Ma'lumotlar to'plami |
| Sum | Yig'indi |
| Count (number of values) | Qiymatlar soni |
| Sorted / in increasing order | O'sish tartibida tizilgan |
| Odd count / even count | Toq son / juft son |

---

## Concept 2 — Guruhlarni To'g'ri Birlashtirish (Combining Groups Correctly — the Weighted Mean)

### Definition

*Ikki yoki undan ortiq guruhning birlashtirilgan (umumiy) arifmetik
o'rtachasini topish uchun, har bir guruhning yig'indisini alohida hisoblab
(guruh o'rtachasini guruhdagi qiymatlar soniga ko'paytirib), so'ngra barcha
yig'indilarni qo'shib, natijani umumiy qiymatlar soniga bo'lish kerak; bu
usul og'irlikli o'rtacha (weighted mean) deb ataladi — guruhlarning
o'rtachalarini to'g'ridan-to'g'ri qo'shib, ikkiga bo'lish **emas**.*

<small>(To find the combined mean of two or more groups, compute each
group's sum separately — group mean times group count — add the sums
together, then divide by the total count. This is called the weighted mean.
It is NOT the same as adding the group means and dividing by two.)</small>

**Why the wrong shortcut survives:** if the two groups happen to be the
*same size*, averaging the two means and computing the true weighted mean
give the identical answer — so a student who learned the shortcut on
equal-size examples never gets corrected until an unequal-size problem
exposes it. The SAT routinely uses unequal group sizes specifically to test
this.

### Model Example (2-misol) — Wrong Method vs. Right Method, Side by Side

A sinfida $8$ o'quvchi bor, ularning o'rtacha bahosi $70$. B sinfida $12$
o'quvchi bor, ularning o'rtacha bahosi $90$. Ikki sinfni birlashtirganda,
umumiy o'rtacha baho nechaga teng?

**Noto'g'ri usul (guruh hajmini e'tiborsiz qoldirish):**
$$\frac{70+90}{2} = 80 \quad \text{— NOTO'G'RI}$$
Bu usul ikki sinfdagi o'quvchilar sonini butunlay e'tiborga olmaydi, xuddi
ikkala sinfda bir xil sonli o'quvchi bordek hisoblaydi.

**To'g'ri usul (har bir guruhning yig'indisini topib, qo'shish):**
A sinfning yig'indisi: $8 \times 70 = 560$. B sinfning yig'indisi:
$12 \times 90 = 1080$. Umumiy yig'indi: $560+1080=1640$. Umumiy o'quvchilar
soni: $8+12=20$. Umumiy o'rtacha: $\dfrac{1640}{20}=82$.

**Javob:** To'g'ri birlashtirilgan o'rtacha $=82$, noto'g'ri usul $80$ ni
beradi — bu farq kichik ko'rinsa ham, SAT testida aynan shu farq noto'g'ri
javobni to'g'ri javobdan ajratadi.

*(Diqqat: agar ikki sinfda ham $10$ tadan o'quvchi bo'lganida edi, ikki usul
ham bir xil javob $80$ ni berardi — chunki guruhlar teng hajmda bo'lganda
bu tasodifan to'g'ri chiqadi. Aynan shuning uchun bu xato shu paytgacha
sezilmay qolishi mumkin edi.)*

### Your-Turn Example (O'zingiz bajaring)

Guruh A: $5$ kishi, o'rtachasi $12$. Guruh B: $20$ kishi, o'rtachasi $20$.
Ikki guruhni birlashtirgandagi umumiy o'rtacha
$=\underline{\hspace{20mm}}$.

*(Avval har ikki usulni ham sinab ko'ring — noto'g'ri qisqa yo'l qanday
javob beradi, to'g'ri usul qanday javob beradi — va ular bir-biridan farq
qilishini tasdiqlang.)*

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Ikki guruhning o'rtachalarini oddiy qo'shib, ikkiga
bo'lish — guruh hajmlarini (necha kishi, necha element) butunlay unutib
qo'yish.

**To'g'ri qoida:** Har doim avval har bir guruhning **yig'indisini**
tiklash (o'rtacha $\times$ son), keyin yig'indilarni qo'shish, keyin umumiy
songa bo'lish. Guruh hajmlari teng bo'lmaguncha, qisqa yo'l (o'rtachalarni
to'g'ridan-to'g'ri o'rtachalash) deyarli har doim noto'g'ri javob beradi.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Combined / weighted mean | Birlashtirilgan / og'irlikli o'rtacha |
| Group | Guruh |
| Group size (count) | Guruh hajmi |
| Sum (reconstructed from mean × count) | Yig'indi |

---

## Concept 3 — O'zgarish Kengligi va Chetga Chiqib Ketgan Qiymatlar (Range and Outlier Sensitivity)

### Definition

*To'plamdagi eng katta va eng kichik qiymat orasidagi farq o'zgarish
kengligi (range) deb ataladi: $\text{range} = \text{max} - \text{min}$.
To'plamga qolgan qiymatlardan sezilarli darajada farq qiluvchi juda katta
yoki juda kichik qiymat qo'shilsa, u chetga chiqib ketgan qiymat (outlier)
deb ataladi; outlier qo'shilganda arifmetik o'rta sezilarli darajada
o'zgaradi, biroq mediana ko'pincha deyarli o'zgarmaydi — chunki mediana
faqat tizimning o'rtasidagi joylashuvga bog'liq, qiymatlarning o'zi qanchalik
katta yoki kichik bo'lishiga emas.*

<small>(The difference between the largest and smallest value in a data set
is the range. A value added to a data set that differs sharply from the
rest is called an outlier; adding one shifts the mean significantly, but
usually barely moves the median — because the median only cares about
sorted position, not magnitude.)</small>

**Nima So'ralmoqda? (What's Actually Being Asked?):** a very common SAT
phrasing is "which measure changes the most/least when this value is
added/removed" — this is asking you to compare *sensitivity*, not to
recompute every statistic from scratch and then guess. Know the rule
(mean = sensitive, median = resistant) going in.

### Model Example (3-misol)

Ma'lumotlar to'plami: $4, 5, 6, 7, 8$. Bu to'plamga $50$ qiymati
qo'shilsa, arifmetik o'rta va mediana qanday o'zgaradi?

**Yechish:** Boshlang'ich to'plam uchun: yig'indi $=30$, son $=5$, arifmetik
o'rta $=6$; tizilgan qator allaqachon tartibda, mediana (o'rtadagi,
3-qiymat) $=6$.

$50$ qo'shilgandan so'ng: $4,5,6,7,8,50$. Yangi yig'indi
$=30+50=80$, yangi son $=6$, yangi arifmetik o'rta
$=\dfrac{80}{6}=\dfrac{40}{3}\approx13.33$ — bu boshlang'ich $6$ dan juda
katta siljish.

Yangi mediana uchun avval tartibni tekshiramiz (allaqachon tartibda):
$4,5,6,7,8,50$ — olti qiymat (juft son), mediana $=$ 3- va 4-qiymatlarning
o'rtachasi $=\dfrac{6+7}{2}=6.5$ — bu boshlang'ich $6$ dan atigi $0.5$ ga
siljigan.

**Javob:** Arifmetik o'rta $6$ dan $\approx13.33$ ga (katta siljish), mediana
$6$ dan $6.5$ ga (kichik siljish) o'zgardi. Bitta o'ta katta qiymat
arifmetik o'rtani kuchli tortadi, medianani esa deyarli joyidan
qimirlatmaydi.

### Your-Turn Example (O'zingiz bajaring)

Ma'lumotlar to'plami: $10, 12, 14, 16, 18$. Bu to'plamga $-40$ qiymati
qo'shilsa (ya'ni g'ayrioddiy kichik qiymat), yangi arifmetik o'rta
$=\underline{\hspace{15mm}}$, yangi mediana $=\underline{\hspace{15mm}}$.
Qaysi ko'rsatkich ko'proq o'zgardi?

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** "Qaysi ko'rsatkich ko'proq o'zgaradi" degan savolga
javob berishdan oldin, mediana ham arifmetik o'rta kabi har bir qiymatga
sezgir deb o'ylash — ikkalasini ham qayta hisoblamasdan, intuitiv taxmin
qilish.

**To'g'ri qoida:** Mediana faqat tartiblangan qatordagi *o'rin*ga bog'liq —
agar yangi qiymat shunchaki eng katta (yoki eng kichik) bo'lib qo'shilsa,
u o'rtadagi qiymatlarning joyini unchalik o'zgartirmaydi. Arifmetik o'rta
esa barcha qiymatlarning aniq kattaligiga bog'liq, shuning uchun bitta juda
katta yoki juda kichik qiymat uni kuchli tortadi. Har doim ikkalasini ham
qayta hisoblab solishtiring — taxmin qilmang.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Range | O'zgarish kengligi |
| Outlier | Chetga chiqib ketgan qiymat |
| Spread | Tarqalish / yoyilganlik |
| Sensitive (changes a lot) | Sezgir |
| Resistant (changes little) | Chidamli / barqaror |

---

## Notes for the problems file (Sets 1–7)

1. Pure drill — mean/median/mode on small odd- and even-count data sets.
2. Harder variant — frequency-table data, and "find the missing value given
   the mean" reverse problems.
3. Combining groups correctly — weighted-mean problems, both equal-size
   (coincidence check) and unequal-size (the real test) group sizes.
4. Outlier-effect identification — range calculations, and before/after
   mean-vs-median comparisons when an outlier is added.
5. Mixed practice — word problems combining 2+ skills above, including a
   "Nima So'ralmoqda?" trap (question asks for a total sum, not a mean, or
   asks for one subgroup's mean reconstructed from a sum).
6. Spot the error — each item targets one of this lesson's documented
   mistakes: averaging two averages instead of weighting, forgetting to
   sort before finding the median, forgetting the even-count averaging
   rule, miscounting the mode, computing range as max+min instead of
   max−min.
7. Bonus/Mastery Check — timed, hardest: solve for an unknown group size or
   unknown data value given a combined mean, sometimes layered with an
   outlier.
