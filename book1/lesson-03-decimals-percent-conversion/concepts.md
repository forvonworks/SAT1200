# Book 1 — Lesson 3: Decimals & Percent Conversion

**Source content file.** This is the authored content, not the final page — it gets
typeset against `research/14-design-spec.md`. Structure follows that spec's
content-block pattern exactly (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary, repeated per concept on this lesson.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` names
"decimal operations & rounding, decimal↔fraction↔percent conversion" as a
confirmed Book 1 gap (baseline incoming-freshman standard, listed in SAT-prep
study guides as a to-know topic), and names "percent basics ... as a pure
arithmetic skill" as a distinct, earlier skill from "percent change in
context" — which is explicitly Book 2 material (percent-change word problems,
successive percent changes). This lesson stays inside that boundary: raw
conversion and computation only, no context word problems.
`research/04-common-student-mistakes.md` names forgetting to convert a
percent to a decimal before calculating as "one of the single most common
'silly' SAT percent errors," and grid-in-specific mistakes (rounding too
early, not recognizing decimal/fraction forms as interchangeable) as a
format-specific trap worth addressing directly.

---

## Concept 1 — O'nli Kasrlar va Raqamli Belgilash (Decimal Notation & Place Value)

### Definition

*Butun qism bilan kasr qismi maxsus belgi bilan ajratilgan son o'nli kasr deb
ataladi; bu belgidan keyingi har bir raqam o'ninchi, yuzdan bir, mingdan bir
ulushlarni ifodalaydi.*

<small>(A number whose whole part and fractional part are separated by a
marker is called a decimal; each digit after that marker represents tenths,
hundredths, thousandths, and so on.)</small>

**Muhim notation farqi — alohida ta'kidlang:** O'zbekiston va Rossiya
an'anasida o'nli kasrning qismlari **vergul** bilan ajratiladi (masalan,
$3{,}14$). SAT testida va boshqa inglizcha manbalarda esa **nuqta**
ishlatiladi ($3.14$). Bu shunchaki yozuv farqi emas — agar talaba bu farqni
bilmasa, test paytida sonni noto'g'ri o'qishi yoki grid-in javobini noto'g'ri
kiritishi mumkin. SAT-dagi har bir o'nli kasr nuqta bilan yoziladi deb,
boshidanoq mustahkam o'rnating.

### Model Example (1-misol)

$$3.7 + 2.45 = ?$$

**Yechish:** O'nli kasrlarni qo'shishda eng muhim qoida — vergul (yoki
nuqta)larni bir-biriga mos tekislab yozish, so'ngra yetishmayotgan xonalarni
nol bilan to'ldirish. $3.7$ sonini $3.70$ deb yozamiz, chunki $2.45$ sonida
ikkita kasr xonasi bor. Endi tekislab qo'shamiz:

$$3.70 + 2.45 = 6.15$$

**Javob:** $6.15$

### Your-Turn Example (O'zingiz bajaring)

$$12.6 - 4.75 = \underline{\hspace{25mm}}$$

*(Student aligns the decimal points, pads with a zero where needed, then
subtracts — same two-step habit shown in the model.)*

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** O'nli kasrlarni nol bilan to'ldirmasdan, raqamlarni
shunchaki eng o'ngdan boshlab tekislab qo'shish — natijada xona qiymatlari
mos kelmay qoladi.

**To'g'ri qoida:** Qo'shish yoki ayirishdan oldin har doim vergul
(nuqta)larni ustma-ust tekislang, so'ngra qisqaroq sonni nol bilan
to'ldiring. $3.7 + 2.45$ ifodasida, agar vergul tekislanmasdan $7$ va $45$
raqamlari to'g'ridan-to'g'ri qo'shilsa, natija $2.82$ kabi butunlay noto'g'ri
chiqadi — chunki $0.7$ (yetti o'ndan bir) $0.07$ (yetti yuzdan bir) bilan
adashtirilgan. To'g'ri javob — tekislab qo'shilganda — $6.15$.

*(Research basis: decimal-point misalignment during addition/subtraction is
a classic, well-documented arithmetic error — distinct from a conceptual
gap, it is a procedural habit that must be drilled explicitly. See
`research/02-topic-difficulty-taxonomy.md`.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Decimal (number) | O'nli kasr |
| Decimal point | Vergul (SAT-da: nuqta) |
| Place value | Xona qiymati |
| Tenths / Hundredths / Thousandths | O'ndan bir / Yuzdan bir / Mingdan bir |
| To align | Tekislamoq |

---

## Concept 2 — O'nli Kasr va Oddiy Kasr O'rtasida O'tish (Decimal ↔ Fraction Conversion)

### Definition

*Har qanday o'nli kasrni, uning oxirgi xona qiymatiga mos keluvchi maxrajli
oddiy kasrga aylantirish mumkin; aksincha, maxraji $10$, $100$, $1000$ kabi
sonlarga teng bo'lgan har qanday oddiy kasrni o'nli kasrga aylantirish
mumkin.*

<small>(Any decimal can be converted to a fraction whose denominator matches
its last place value; conversely, any fraction whose denominator is 10, 100,
1000, etc. can be converted to a decimal.)</small>

### Model Example (2-misol)

$$0.75 \text{ sonini oddiy kasrga aylantiring.}$$

**Yechish:** $0.75$ sonida oxirgi raqam — $5$ — yuzdan bir xonasida turibdi,
demak maxraj $100$ bo'ladi: $\dfrac{75}{100}$. Endi suratni va maxrajni
ularning eng katta umumiy bo'luvchisiga — $25$ ga — qisqartiramiz:

$$\frac{75}{100} = \frac{75 \div 25}{100 \div 25} = \frac{3}{4}$$

**Javob:** $\dfrac{3}{4}$

### Your-Turn Example (O'zingiz bajaring)

$$\frac{1}{8} \text{ kasrini o'nli kasrga aylantiring: } \underline{\hspace{25mm}}$$

*(Student divides numerator by denominator, or recognizes the common
eighths-as-decimals pattern if already taught.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Fraction | Oddiy kasr |
| Numerator / Denominator | Surat / Maxraj |
| To simplify (reduce) | Qisqartirmoq |
| Greatest common divisor | Eng katta umumiy bo'luvchi |

---

## Concept 3 — Foiz va O'nli Kasr O'rtasida O'tish (Percent ↔ Decimal Conversion)

### Definition

*Yuzdan necha ulush ekanligini ko'rsatuvchi son foiz deb ataladi va $\%$
belgisi bilan yoziladi; foizni o'nli kasrga aylantirish uchun sonni $100$ ga
bo'lish, ya'ni vergulni ikki xona chapga surish kifoya.*

<small>(A number showing how many parts out of a hundred is called a
percent, written with the % symbol; to convert a percent to a decimal,
divide by 100 — move the decimal point two places to the left.)</small>

**SAT uchun nega muhim:** hisoblashdan oldin foizni albatta o'nli kasrga
(yoki oddiy kasrga) aylantirish shart — foiz belgisi bilan to'g'ridan-to'g'ri
ko'paytirish mumkin emas. Bu qadam tez-tez tushirib qoldiriladigan, lekin
butun javobni buzadigan xato (pastdagi Keng tarqalgan xato bo'limiga
qarang).

### Model Example (3-misol)

$$45\% \text{ ni o'nli kasrga, so'ngra } 0.6 \text{ ni foizga aylantiring.}$$

**Yechish:** $45\%$ ni o'nli kasrga aylantirish uchun $100$ ga bo'lamiz (yoki
vergulni ikki xona chapga suramiz): $45\% = 0.45$.

$0.6$ ni foizga aylantirish uchun esa $100$ ga ko'paytiramiz (vergulni ikki
xona o'ngga suramiz): $0.6 = 60\%$.

**Javob:** $45\% = 0.45$; $\quad 0.6 = 60\%$

### Your-Turn Example (O'zingiz bajaring)

$$150\% \text{ ni o'nli kasrga aylantiring: } \underline{\hspace{25mm}}$$

*(Student practices a percent greater than 100% — decimal point still moves
two places left, giving a result greater than 1.)*

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Foizni o'nli kasrga aylantirmasdan, to'g'ridan-to'g'ri
butun son sifatida ko'paytirish.

**To'g'ri qoida:** Har qanday hisoblashdan oldin foiz albatta o'nli kasrga
(yoki oddiy kasrga) aylantiriladi. $45\% \text{ ning } 80 \text{ dan nechaga
tengligini}$ topishda, agar $45 \times 80 = 3600$ deb hisoblansa, natija $100$
martadan ortiq kattalashtirilgan bo'ladi. To'g'ri yechim: avval $45\% = 0.45$
ga aylantiriladi, so'ngra $0.45 \times 80 = 36$.

*(Research basis: "forgetting to convert a percent to a decimal before using
it in a calculation... is listed repeatedly as one of the single most common
'silly' SAT percent errors." See `research/04-common-student-mistakes.md`.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Percent | Foiz |
| Percent sign | Foiz belgisi (%) |
| To convert | Aylantirmoq |

---

## Concept 4 — Foiz va Oddiy Kasr, "Sonning Foizi" (Percent ↔ Fraction, Percent of a Number)

### Definition

*Biror sonning berilgan foizini topish uchun, o'sha foiz o'nli kasrga (yoki
oddiy kasrga) aylantirilib, berilgan songa ko'paytiriladi.*

<small>(To find a given percent of a number, convert that percent to a
decimal or fraction, then multiply it by the number.)</small>

**Diqqat — doiraning chegarasi:** Bu kontseptsiya faqat "sonning foizini
topish" (masalan, $80$ ning $45\%$i qancha) kabi sof hisoblash ko'nikmasini
qamrab oladi. "Foiz o'zgarishi," "ketma-ket foiz o'zgarishlari" kabi
kontekstli masalalar — bular Kitob 2'da alohida o'rganiladi.

### Model Example (4-misol)

$$80 \text{ ning } 25\% \text{ i qanchaga teng? So'ngra } \frac{3}{5} \text{ ni foizga aylantiring.}$$

**Yechish:** $25\%$ ni o'nli kasrga aylantiramiz: $25\% = 0.25$. Endi $80$ ga
ko'paytiramiz: $0.25 \times 80 = 20$.

$\dfrac{3}{5}$ ni foizga aylantirish uchun avval o'nli kasrga o'tkazamiz:
$\dfrac{3}{5} = 0.6$, so'ngra $100$ ga ko'paytiramiz: $0.6 \times 100 = 60\%$.

**Javob:** $80$ ning $25\%$ i $= 20$; $\quad \dfrac{3}{5} = 60\%$

### Your-Turn Example (O'zingiz bajaring)

$$45 \text{ ning } 60\% \text{ i qanchaga teng? } \underline{\hspace{25mm}}$$

*(Student converts 60% to a decimal, then multiplies — same two-step
sequence shown in the model.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Percent of a number | Sonning foizi |
| To multiply | Ko'paytirmoq |

---

## Notes for the problems file (Sets 1–7)

- Set 1: decimal addition/subtraction drill — place-value alignment habit.
- Set 2: decimal multiplication/division drill — decimal-place counting
  (a separate, equally common procedural slip from alignment errors).
- Set 3: decimal ↔ fraction conversion, both directions.
- Set 4: percent ↔ decimal conversion, both directions, including percents
  above 100% and below 1% to stress-test the "move two places" rule at its
  edges.
- Set 5: percent ↔ fraction conversion and "percent of a number," mixed.
- Set 6: spot-the-error — targets the documented "forgot to convert % to
  decimal" mistake plus the decimal-alignment and decimal-shift errors from
  Concepts 1 and 3 (erroneous-examples technique, per
  `06-concept-explanation-pedagogy.md`, used here because each error is a
  specifically documented common misconception, not an invented one).
- Set 7 (bonus/challenge): multi-step problems chaining a decimal operation,
  a percent conversion, and a fraction conversion in one item — closer to
  the density of an actual SAT grid-in question.
