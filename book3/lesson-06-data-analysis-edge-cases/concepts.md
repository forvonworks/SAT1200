# Book 3 — Lesson 6: Data-Analysis Edge Cases & Study-Design Critique (Hard)

**Source content file**, paired with `problems.md`. Domain: Problem-Solving & Data
Analysis, hard tier. This is the hard-edge extension of Book 2 Lessons 15 (Statistics
Fundamentals), 16 (Data Representations), 17 (Probability Fundamentals), and 18 (Study
Design & Statistical Claims) — it assumes everything in those four lessons is solid and
does **not** re-teach mean/median/mode, basic table reading, basic probability, or the
random-sample/random-assignment framework from scratch. It does **not** cover percentages
or ratios/rates (Book 2 Lessons 13–14 already go deep there).

**This lesson is grounded in real official College Board Hard-tagged questions**, pulled
from the Question Bank export in `Materials/` and read directly off the rendered PDF pages
per the pipeline in `research/15-question-bank-analysis.md` (the bank's text layer drops
all numbers — a custom font with no Unicode mapping — so every real question below was
recovered by rendering its exact page to an image and reading the real numbers off it, not
by text-scraping). Five real Hard questions anchor this lesson's five concepts: `f8a322d9`,
`e7d48c8a`, `241f1db7`, `f496d2c0`, `89ff6a0a`, `2e8027b0`, `9ba3e283` (all from
`Materials/SAT MATH.pdf`). The common-mistake boxes below are built directly from the real
wrong-answer-choice rationales printed in the bank for these exact questions — a stronger
source than inferred mistakes, since College Board itself states what a wrong answer
represents.

---

## Concept 1 — Guruhlangan Ma'lumotlarda Eng Katta/Eng Kichik O'rtacha (Min/Max Mean in Grouped Data)

### Definition

*Ma'lumotlar aniq qiymatlar bilan emas, balki oraliqlar (masalan, "20 dan katta yoki teng,
ammo 30 dan kichik") bilan guruhlangan bo'lsa, har bir oraliq ichidagi haqiqiy qiymatlar
noma'lum qoladi — shuning uchun bunday to'plamning arifmetik o'rtasi **bitta aniq son
emas**, balki har bir oraliqning eng kichik va eng katta mumkin bo'lgan qiymatlariga
qarab o'zgaradigan **oraliq** hosil qiladi; bu oraliqning ikki chetini topish uchun, eng
kichik o'rtachani hisoblashda har bir guruhning **eng kichik** qiymatidan, eng katta
o'rtachani hisoblashda esa har bir guruhning **eng katta** qiymatidan foydalaniladi.*

<small>(When data is reported in intervals rather than exact values — "at least 20 but
less than 30" — the real values inside each interval are unknown, so such a data set's
mean isn't one fixed number: it ranges between a smallest-possible and largest-possible
mean, found by using each interval's smallest value for the lower bound and its largest
value for the upper bound.)</small>

**Why this is genuinely new, not a harder Book 2 L15 problem:** Book 2 always gave you
exact values. Here the question is unanswerable with one number — you must reason about
the *range of possible means*, which is a different skill (bounding, not computing).

### Model Example (1-misol) — Real SAT Hard Question

Ikkita ma'lumotlar to'plami — $A$ va $B$ — har biri $23$ ta butun sondan iborat, quyidagi
chastota jadvallari bilan berilgan (har bir oraliq "chapdagi songa teng yoki undan katta,
ammo o'ngdagi songa kichik" degan ma'noni bildiradi):

| To'plam $A$ | Chastota | | To'plam $B$ | Chastota |
|---|---|---|---|---|
| $[20,30)$ | $3$ | | $[10,20)$ | $3$ |
| $[30,40)$ | $4$ | | $[20,30)$ | $4$ |
| $[40,50)$ | $7$ | | $[30,40)$ | $7$ |
| $[50,60)$ | $9$ | | $[40,50)$ | $9$ |

$A$ to'plamining arifmetik o'rtasi bilan $B$ to'plamining arifmetik o'rtasi orasidagi eng
kichik mumkin bo'lgan farqni toping.

**Yechish:** Ikkala to'plam ham bir xil shaklga ega, lekin $A$ ning qiymatlari $B$
nikidan $10$ ga katta oraliqda joylashgan — demak $A$ ning o'rtachasi doim $B$ nikidan
katta. Shuning uchun **eng kichik farq** — bu $A$ ning **eng kichik mumkin bo'lgan**
o'rtachasi bilan $B$ ning **eng katta mumkin bo'lgan** o'rtachasi orasidagi farq.

$A$ ning eng kichik o'rtachasi (har bir oraliqning chap chetidan foydalanib):
$$\frac{3(20)+4(30)+7(40)+9(50)}{23}=\frac{910}{23}$$

$B$ ning eng katta o'rtachasi (har bir oraliqning eng katta butun sonidan — ya'ni
o'ngdagi songa $1$ kam qiymatdan — foydalanib, masalan $[10,20)$ uchun $19$):
$$\frac{3(19)+4(29)+7(39)+9(49)}{23}=\frac{887}{23}$$

Farq: $\dfrac{910}{23}-\dfrac{887}{23}=\dfrac{23}{23}=1$.

**Javob:** Eng kichik mumkin bo'lgan farq $=1$.

### Your-Turn Example (O'zingiz bajaring)

Ikkita to'plam, $P$ va $Q$, har biri $20$ ta butun sondan iborat:

| To'plam $P$ | Chastota | | To'plam $Q$ | Chastota |
|---|---|---|---|---|
| $[40,50)$ | $4$ | | $[30,40)$ | $4$ |
| $[50,60)$ | $6$ | | $[40,50)$ | $6$ |
| $[60,70)$ | $10$ | | $[50,60)$ | $10$ |

$P$ va $Q$ ning arifmetik o'rtachalari orasidagi eng kichik mumkin bo'lgan farqni toping:
$\underline{\hspace{20mm}}$

### Common Mistake Box (real CB wrong-answer rationale)

**Noto'g'ri yondashuv:** Savol o'rtachalar orasidagi farqni so'raganda, buning o'rniga
to'plamlarning **range** (eng katta − eng kichik qiymat) orasidagi farqni hisoblash.

**To'g'ri qoida:** Real test materialida aynan shu xato nomlangan: *"bu rangelar
orasidagi eng kichik farq, o'rtachalar orasidagi emas"* — ya'ni range va mean butunlay
boshqa-boshqa ko'rsatkichlar, va ikkalasi ham "eng kichik farq" so'roviga turlicha javob
beradi. Har doim savol **aynan qaysi ko'rsatkichni** (o'rtacha, mediana, range) so'rayotganini
tekshiring, shunchaki "farq" so'zini ko'rib eng oson hisoblanadigan narsani hisoblamang.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Grouped / binned data | Guruhlangan ma'lumotlar |
| Interval | Oraliq |
| Smallest/largest possible mean | Eng kichik/eng katta mumkin bo'lgan o'rtacha |

---

## Concept 2 — Qiymat Qo'shilganda O'rtacha va Mediananing Xatti-Harakati (Mean/Median Behavior When a Value Is Added)

### Definition

*To'plamga yangi qiymat qo'shilganda, arifmetik o'rta **har doim** o'zgaradi (agar
qo'shilgan qiymat eski o'rtachaga teng bo'lmasa), chunki u barcha qiymatlarning yig'indisiga
bog'liq; mediana esa **faqat** qo'shilgan qiymat tartiblangan qatorning o'rta qismidagi
joylashuvni o'zgartirgan taqdirdagina o'zgaradi — agar yangi qiymat juda katta yoki juda
kichik bo'lib, faqat qatorning chetiga qo'shilsa, mediana ko'pincha o'zgarmay qoladi yoki
juda oz o'zgaradi.*

<small>(Adding a value to a data set always changes the mean (unless the value equals the
old mean), since the mean depends on the total sum; the median only changes if the new
value shifts which values occupy the middle of the sorted order — if the new value is
extreme and simply joins one end of the list, the median often doesn't move, or barely
does.)</small>

**Nima So'ralmoqda? — bu Book 2 L15 Concept 3'ning tabiiy davomi, ammo SAT buni ko'pincha
Roman-raqamli (I, II) formatda beradi:** "quyidagilardan qaysi biri (yoki ikkalasi ham)
yangi to'plamda eskisidan katta bo'ladi: I. Mediana II. O'rtacha" — bu format ikkalasini
ham **alohida-alohida** tekshirishni talab qiladi, biri haqiqat bo'lgani uchun ikkinchisi
ham haqiqat deb taxmin qilmang.

### Model Example (2-misol) — Real SAT Hard Question

Quyidagi chastota jadvali bitta bug' favvorasining $13$ marta otilishi haqidagi
ma'lumotlarni (har bir otilishdagi portlashlar soni) ko'rsatadi:

| Portlashlar soni | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| Chastota | $4$ | $5$ | $2$ | $1$ | $1$ |

Agar bu to'plamga yana bitta otilish — $11$ ta portlash bilan — qo'shilsa ($14$ ta otilishdan
iborat yangi to'plam hosil bo'ladi), quyidagilardan qaysi biri yangi to'plamda eskisidan
**katta** bo'ladi?

$\text{I. Mediana} \qquad \text{II. Arifmetik o'rta}$

**Yechish:** Avval eski to'plam uchun: yig'indi $=4(1)+5(2)+2(3)+1(4)+1(5)=4+10+6+4+5=29$,
arifmetik o'rta $=\frac{29}{13}$. Qiymatlar soni toq ($13$), mediana — $7$-qiymat.
Tartiblangan qator: to'rtta $1$, beshta $2$ (bular $5$-$9$ o'rinlarni egallaydi) — demak
$7$-o'rin $2$ ga teng. Eski mediana $=2$.

$11$ qo'shilgandan so'ng ($14$ ta qiymat, juft son): yangi yig'indi $=29+11=40$, yangi
arifmetik o'rta $=\frac{40}{14}=\frac{20}{7}\approx2.857$ — bu $\frac{29}{13}\approx2.231$
dan **katta**.

Yangi mediana — $7$- va $8$-qiymatlarning o'rtachasi. $11$ eng katta qiymat bo'lgani uchun
qatorning oxiriga qo'shiladi, dastlabki $13$ ta qiymatning tartibini o'zgartirmaydi.
$7$- va $8$-o'rinlar hali ham ikkalasi $2$ ga teng (chastota jadvalidan: $5$-$9$ o'rinlar
$2$). Yangi mediana $=\frac{2+2}{2}=2$ — **o'zgarmadi**.

**Javob:** Faqat II (arifmetik o'rta) katta bo'ldi; mediana o'zgarmadi.

### Your-Turn Example (O'zingiz bajaring) — Diqqat, Bu Safar Mediana HAM O'zgaradi

Ma'lumotlar to'plami: $2, 2, 2, 5, 8, 8, 8$ ($7$ ta qiymat). Bu to'plamga $6$ qiymati
qo'shilsa ($8$ ta qiymatdan iborat yangi to'plam hosil bo'ladi): yangi mediana
$=\underline{\hspace{15mm}}$ (eskisi bilan solishtiring — o'zgardimi?). Yangi arifmetik
o'rta $=\underline{\hspace{15mm}}$.

*(Maslahat: avvalgi misolda mediana o'zgarmadi deb, bu safar ham albatta o'zgarmaydi deb
taxmin qilmang — har safar qayta tekshiring.)*

### Common Mistake Box

**Noto'g'ri yondashuv:** Bir misolda mediana o'zgarmaganini ko'rib, "mediana qo'shilgan
qiymatga hech qachon sezgir emas" degan **umumiy qoida** sifatida yodlab olish.

**To'g'ri qoida:** Mediana faqat **tartiblangan qatorning o'rtasidagi aniq joylashuvga**
bog'liq. Agar qo'shilgan qiymat qatorning allaqachon shakllangan o'rta qismiga "kirib
kelsa" (juda katta yoki juda kichik bo'lmasa), u mediana hisoblanadigan o'rinlarni
siljitib, medianani ham o'zgartirishi mumkin — aynan Your-Turn misolidagi kabi. Har bir
holatni alohida, qayta hisoblab tekshiring.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Add a value to a data set | To'plamga qiymat qo'shish |
| Shift (change) | Siljish / o'zgarish |
| Roman-numeral (I/II) answer format | Rim raqamli (I/II) javob formati |

---

## Concept 3 — Ko'p Mezonli Shartli Ehtimollik (Conditional Probability Across More Than One Category)

### Definition

*Jadvalda ma'lumotlar bir nechta qator va ustunga guruhlangan bo'lib, shart (masalan,
"berilgan X emasligi") bir nechta qator yoki ustunni **birgalikda** qamrab olsa, shartli
ehtimollikning maxraji — faqat bitta qator yoki ustun yig'indisi emas, balki shartga mos
keladigan **barcha** qatorlar yoki ustunlarning yig'indisidan iborat bo'ladi.*

<small>(When a table's condition — e.g. "given that it is NOT category X" — spans more
than one row or column together, the denominator of the conditional probability is not
one single row/column total, but the sum of every row or column that satisfies the
condition.)</small>

**Why this is genuinely harder than Book 2 L17:** there, the condition always matched
exactly one row or one column. Here, "not X" or "at least Y" can match *several* rows or
columns at once — you must first identify and sum the *right combination* before dividing.

### Model Example (3-misol) — Real SAT Hard Question

Quyidagi jadval bir muassasadagi xonalarning o'tirish sig'imi bo'yicha taqsimotini
ko'rsatadi:

| O'tirish sig'imi | Ulush |
|---|---|
| $18$ dan kichik | $26\%$ |
| $18$–$40$ | $21\%$ |
| $41$–$65$ | $29\%$ |
| $65$ dan katta | $24\%$ |

Shu muassasadan tasodifan bir xona tanlansa, uning sig'imi **kamida $18$ ta o'rindiq**
bo'lgani sharti bilan, sig'imi **$65$ dan katta** bo'lish ehtimoli nechaga teng?

**Yechish:** Shart — "kamida $18$" — bu **uchta** toifani birlashtiradi: $18$–$40$,
$41$–$65$, va $65$ dan katta. Demak maxraj — bu uchtasining yig'indisi, faqat bitta
qatorning o'zi emas: $21\%+29\%+24\%=74\%$.

So'ralgan hodisa ($65$ dan katta) — bu uchtadan faqat bittasi: $24\%$.

$$P(65\text{ dan katta}\mid\text{kamida }18)=\frac{24\%}{74\%}=\frac{24}{74}=\frac{12}{37}\approx0.324$$

**Javob:** $\dfrac{12}{37}\approx0.324$

### Your-Turn Example (O'zingiz bajaring)

Bir universitet talabalari sinf bo'yicha quyidagicha taqsimlangan: Birinchi kurs $22\%$,
Ikkinchi kurs $28\%$, Uchinchi kurs $24\%$, To'rtinchi kurs $26\%$. Tasodifan tanlangan
talaba **birinchi kurs emasligi** sharti bilan, uning **to'rtinchi kurs** bo'lish ehtimoli
$=\underline{\hspace{20mm}}$

### Common Mistake Box (real CB wrong-answer rationale)

**Noto'g'ri yondashuv:** Shartli ehtimollikning maxraji sifatida **jami populyatsiyaning
o'zini** ishlatish — ya'ni shartni ("kamida $18$", "birinchi kurs emas") maxrajga
qo'shishni butunlay unutish.

**To'g'ri qoida:** Real test materialida aynan shu xato nomlangan: *"bu — shartsiz, barcha
xonalar orasidan tanlash ehtimoli, faqat shartga mos keladigan xonalar orasidan emas."*
"Berilgan ... sharti bilan" so'zlarini ko'rgan zahoti, maxrajni albatta **faqat o'sha
shartga mos keladigan guruh(lar)** bilan cheklang — butun jadvalning yig'indisi bilan emas.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Conditional probability | Shartli ehtimollik |
| Category / row / column | Toifa / qator / ustun |
| Combine (several categories) | Birlashtirish |
| Restrict the denominator | Maxrajni cheklash |

---

## Concept 4 — Ikki O'zgaruvchili Ma'lumotni Masshtablashtirish va Eng Mos Chiziq (Scaling Two-Variable Data and the Line of Best Fit)

### Definition

*Agar bir ma'lumotlar to'plamining har bir $y$ qiymati bitta doimiy songa ko'paytirilsa,
shu to'plam uchun eng mos chiziq tenglamasi $y=a+bx$ bo'lsa, yangi (masshtablashtirilgan)
to'plam uchun eng mos chiziq — **ikkala koeffitsient ham** ($a$ ham, $b$ ham) o'sha doimiy
songa ko'paytirilgan $y=(a\cdot k)+(b\cdot k)x$ tenglamasi bo'ladi.*

<small>(If every $y$-value of a data set is multiplied by a constant, and the original
line of best fit is $y = a + bx$, the new (scaled) data set's line of best fit is
$y = (a \cdot k) + (b \cdot k)x$ — both the intercept AND the slope get multiplied by that
same constant.)</small>

**Why this is new material, not in Book 2 L16:** Book 2 taught reading a scatterplot and
describing a trend. This teaches a specific **algebraic transformation rule** — scaling
every $y$-value scales the entire line (intercept and slope alike) by the same factor —
which lets you answer the question without re-plotting anything.

### Model Example (4-misol) — Real SAT Hard Question

$E$ ma'lumotlar to'plami uchun eng mos chiziq tenglamasi $y=12+1.5x$ (ya'ni $y$-kesishma
$12$, burchak koeffitsienti $1.5$). $F$ to'plami $E$ ning har bir $y$ qiymatini $3.9$ ga
ko'paytirish orqali hosil qilinadi. $F$ uchun eng mos chiziq tenglamasi qanday bo'ladi?

**Yechish:** $E$ ning tenglamasi $y=a+bx$ ko'rinishida, $a=12$, $b=1.5$. $F$ — bu $E$ ning
har bir $y$ qiymati $3.9$ ga ko'paytirilgan holati, demak $F$ ning eng mos chizig'i ham
**ikkala koeffitsientni** $3.9$ ga ko'paytirish orqali topiladi:

$$a_{\text{new}}=12\times3.9=46.8 \qquad b_{\text{new}}=1.5\times3.9=5.85\approx5.9$$

**Javob:** $y=46.8+5.9x$ (taxminan)

*(E'tibor bering: faqat $b$ ni yoki faqat $a$ ni ko'paytirish — bu keng tarqalgan xato.
$y$ ning HAR BIR qiymati ko'paytirilgani uchun, chiziqning HAR IKKI qismi — boshlang'ich
nuqtasi ham, burchagi ham — bir xil koeffitsientga ko'payadi.)*

### Your-Turn Example (O'zingiz bajaring)

$G$ to'plami uchun eng mos chiziq $y=5+2x$. $H$ to'plami $G$ ning har bir $y$ qiymatini
$2.5$ ga ko'paytirish orqali hosil qilingan. $H$ uchun eng mos chiziq tenglamasi
$=\underline{\hspace{30mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** Faqat burchak koeffitsientini ($b$) ko'paytirish, $y$-kesishmani
($a$) o'zgarishsiz qoldirish — yoki aksincha.

**To'g'ri qoida:** $y$ ning har bir qiymati ko'paytirilgani — bu butun chiziqning
vertikal ravishda "cho'zilishi" degani. Chiziqning istalgan nuqtasi $(x,y)$ endi
$(x, ky)$ ga aylanadi, bu esa ham boshlang'ich nuqtani ($x=0$ dagi qiymat, ya'ni $a$), ham
burchak koeffitsientini ($b$) bir xil $k$ ga ko'paytiradi. Faqat bittasini ko'paytirish —
chiziqni noto'g'ri "egadi", to'g'ri "cho'zmaydi".

### Vocabulary

| English | O'zbekcha |
|---|---|
| Line of best fit | Eng mos chiziq |
| Scale (multiply every value) | Masshtablashtirish |
| Intercept / slope | $y$-kesishma / burchak koeffitsienti |

---

## Concept 5 — Vakillik Namunasidan Populyatsiya Sonini Baholash (Estimating a Population Count from a Representative Sample)

### Definition

*Agar bir namuna (masalan, bitta sinf) butun populyatsiyaning (masalan, shtatdagi barcha
shunga o'xshash sinflarning) **vakili** deb berilgan bo'lsa, namunadagi foiz yoki nisbatni
har bir shunga o'xshash guruhga qo'llab, so'ngra guruhlar sonига ko'paytirish orqali butun
populyatsiya uchun sonli baho olish mumkin.*

<small>(If a sample — e.g., one class — is stated to be representative of a larger
population — e.g., every similar class in the state — you can apply the sample's
percentage to each similar group, then multiply by the number of groups, to get a numeric
estimate for the whole population.)</small>

**This connects directly to Book 2 L18's random-sample framework** — "representative"
here plays the same role "randomly sampled" did there — but goes one step further by
asking for an actual **numeric estimate**, not just a judgment about whether
generalizing is valid.

### Model Example (5-misol) — Real SAT Hard Question

$X$ shtatida, janob Kempning $26$ nafar o'quvchidan iborat $8$-sinfi so'rovdan o'tkazildi,
va o'quvchilarning $34.6\%$ i kamida ikkita aka-uka/opa-singilga ega ekanini aytdi.
Shtatdagi o'rtacha $8$-sinf hajmi $26$ ga teng. Agar janob Kempning sinfi shtatdagi barcha
$8$-sinflarning vakili bo'lsa va shtatda $1{,}800$ ta $8$-sinf bo'lsa, shtatdagi
**ikkitadan kam** aka-uka/opa-singilga ega $8$-sinf o'quvchilarining sonini eng yaxshi
baholang.

**Yechish:** $34.6\%$ dan $26$ ta o'quvchining soni: $0.346\times26=8.996\approx9$ nafar
o'quvchi kamida ikkitaga ega — demak $26-9=17$ nafari **ikkitadan kam**ga ega.

Janob Kempning sinfi vakillik qilgani uchun, shtatdagi har bir $8$-sinfda taxminan $17$
nafar o'quvchi ikkitadan kamga ega deb hisoblash mumkin. Shtatda $1{,}800$ ta sinf
borligi uchun:

$$17\times1{,}800=30{,}600$$

**Javob:** $\approx30{,}600$ o'quvchi

### Your-Turn Example (O'zingiz bajaring)

Bir shaharda $25$ nafar o'quvchidan iborat vakillik namunasida, o'quvchilarning $28\%$ i
bir uy hayvoniga ega ekanini aytdi. Shaharda shunga o'xshash $2{,}200$ ta sinf bor. Shahar
bo'yicha **uy hayvoniga ega bo'lmagan** o'quvchilar sonini baholang:
$\underline{\hspace{25mm}}$

### Common Mistake Box (real CB wrong-answer rationale)

**Noto'g'ri yondashuv:** Berilgan foizni e'tiborsiz qoldirib, taxminiy javobni shunchaki
**umumiy sonning yarmi** deb hisoblash (go'yo har doim $50\%-50\%$ bo'linish bordek).

**To'g'ri qoida:** Real test materialida aynan shu xato nomlangan: bu "umumiy sonning
yarmi, ammo berilgan foiz $50\%$ dan farq qilgani uchun" noto'g'ri javob. Har doim
**aniq berilgan foiz/nisbatdan** boshlang, hech qachon "balki yarmidir" deb taxmin
qilmang — savol sizga aniq foizni shu uchun bergan.

### Vocabulary

| English | O'zbekcha |
|---|---|
| Representative (of a population) | Vakillik qiluvchi |
| Estimate | Baholash |
| Apply the sample rate to each group | Namunadagi nisbatni har bir guruhga qo'llash |

---

## Notes for the problems file (Sets 1–8)

1. Grouped-data min/max mean — including a reversed-direction variant.
2. Added-value effect on mean/median — deliberate mix of "median doesn't move" and
   "median DOES move" cases, so students can't pattern-match one rule blindly.
3. Multi-category conditional probability from tables (row/column combos).
4. Two-variable data scaling / line of best fit transformation.
5. Population estimate from a representative sample.
6. Mixed — combining two of the above skills in one problem.
7. Spot the error — each item targets one of this lesson's real CB-documented wrong-answer
   traps (range-vs-mean confusion, forgetting to restrict the conditional denominator,
   assuming a 50/50 split instead of using the given percentage).
8. Bonus/Mastery Check — hardest, multi-step.
