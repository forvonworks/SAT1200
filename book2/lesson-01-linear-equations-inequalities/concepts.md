# Book 2 — Lesson 1: Linear Equations & Inequalities

**Source content file.** Structure follows `research/14-design-spec.md` §6 and
mirrors `book1/lesson-01-basic-arithmetic-order-of-operations/concepts.md`.

**Framing note:** Book 2 is "every SAT topic taught beyond the SAT's own
ceiling" — not a repeat of Book 1 Lesson 6 (one-variable equations) at the
same depth. This lesson assumes that fluency and pushes further: equations
with fraction coefficients and the variable on both sides, the full
inequality sign-flip rule, and compound inequalities, none of which Book 1
covered. Per the annotated TOC, every Book 2 lesson also carries three
threads: a "what is actually being asked" check (the single most-cited SAT
trap across all topics — see `research/04`), sign-error awareness, and a
notation-translation callout where relevant. All three appear below.

**Research grounding:** `research/01-official-sat-math-spec.md` (Algebra
domain, ~35% of SAT Math — linear equations/inequalities named explicitly in
the official domain description), `research/04-common-student-mistakes.md`
("Linear Equations" and "Word Problems" sections), `research/05-uzbek-student-considerations.md`
(interval-notation semicolon-vs-comma gap), plus a targeted web search on
inequality-specific errors (forgetting to flip on a negative multiply/divide —
named "the single most common error" on these questions across multiple prep
sources; the reverse error of flipping when *not* needed, e.g. on addition/
subtraction; open-vs-closed endpoint confusion; compound-inequality direction
errors).

---

## Concept 1 — Multi-Step Linear Equations (Book 2 Depth)

### Definition

*Bir nechta amalni — qavs ochish, o'xshash hadlarni qo'shish, kasrli
koeffitsientlarni tozalashni — talab qiluvchi, noma'lum ikkala tomonda ham
uchrashi mumkin bo'lgan tenglama ko'p qadamli chiziqli tenglama deb ataladi.*

<small>(A linear equation that needs several steps — clearing parentheses,
combining like terms, clearing fraction coefficients — and may have the
variable on both sides.)</small>

### Doim So'ralayotgan Narsani Tekshiring (Always Check What's Actually Asked)

**Bu eslatma shu yerda bir marta emas — har safar eslab turing:** SAT'da eng
ko'p uchraydigan xato — bu matematik xato emas, **e'tibor xatosi**: tenglamani
to'g'ri yechib, $x$ ni topib, lekin savol $x$ ni emas, $2x+1$ yoki boshqa
ifodani so'rayotganini payqamay, $x$ ning qiymatini javob sifatida kiritish.

**Misol:** $3x+5=20$ berilgan. $6x+10$ ning qiymati nechaga teng?

Ko'pchilik $x=5$ ni topadi-yu, shu yerda to'xtaydi va $5$ ni javob deb
kiritadi. Lekin savol $x$ ni emas, $6x+10$ ni so'ragan: $6(5)+10=40$. **Har
safar tenglamani yechgandan so'ng, savolni qaytadan o'qing — aynan nima
so'ralgan?**

### Model Example (1-misol)

$$\frac{2}{3}(x+3) = x - 1$$

**Yechish:** Avval ikkala tomonni $3$ ga ko'paytirib kasrdan qutulamiz:
$2(x+3) = 3(x-1)$. Qavslarni ochamiz: $2x+6 = 3x-3$. Noma'lumni bir tomonga
yig'amiz: $6+3 = 3x-2x$, ya'ni $x=9$.

**Javob:** $x=9$

### Your-Turn Example (O'zingiz bajaring)

$3(x-2) = 2(x+1)$ tenglamasini yeching: $x = \underline{\hspace{25mm}}$

*(Ikkinchi savol, "nima so'ralgan" ko'nikmasini mustahkamlash uchun:)*
Agar $2(x+5)=18$ bo'lsa, $x+5$ ning qiymati nechaga teng?
$x+5 = \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** Tenglamani to'g'ri yechib, $x$ ning qiymatini topib, savol
nimani so'raganini tekshirmasdan o'sha sonni javob deb yozish.

**To'g'ri:** Yuqoridagi "Doim So'ralayotgan Narsani Tekshiring" bo'limiga
qarang — bu Book 2'ning eng ko'p takrorlanadigan ogohlantirishi, chunki bu
xato matematik bilim yetishmasligidan emas, e'tiborsizlikdan kelib chiqadi.

---

## Concept 2 — Chiziqli Tengsizliklar va Ishorani Almashtirish Qoidasi (Linear Inequalities & the Sign-Flip Rule)

### Definition

*Ikki ifoda orasidagi $<,\ >,\ \le,\ \ge$ munosabatlardan birini ifodalovchi
va yechimi bitta son emas, sonlar to'plami bo'lgan ifoda tengsizlik deb
ataladi. Tengsizlik tenglama kabi yechiladi — bitta muhim farq bilan: agar
ikkala tomon manfiy songa ko'paytirilsa yoki bo'linsa, tengsizlik belgisi
teskarisiga almashtiriladi.*

<small>(An inequality is solved like an equation, with one critical
difference: multiplying or dividing both sides by a negative number flips
the inequality sign.)</small>

### Model Example (2-misol)

$$-3x + 5 \le 20$$

**Yechish:** Ikkala tomondan $5$ ni ayiramiz: $-3x \le 15$. Endi ikkala
tomonni $-3$ ga bo'lamiz — **manfiy songa bo'linyapti, shuning uchun belgi
almashadi**: $x \ge -5$.

**Javob:** $x \ge -5$

### Your-Turn Example (O'zingiz bajaring)

$4 - 2x > 10$ tengsizligini yeching: $x \underline{\hspace{25mm}}$

### Common Mistake Box

**Birinchi xato — belgini almashtirishni unutish:** $-2x > 8$ ni $-2$ ga
bo'lganda, $x > -4$ deb yozish. **To'g'ri:** manfiy songa bo'lingani uchun
belgi almashadi: $x < -4$.

**Ikkinchi xato — kerak bo'lmagan joyda almashtirish:** ko'pchilik "manfiy son
ko'rsam, albatta belgi almashadi" deb noto'g'ri umumlashtiradi. Agar manfiy
son faqat **qo'shiladi yoki ayiriladi** (ko'paytirilmaydi/bo'linmaydi), belgi
almashmaydi: masalan $x - 5 > 2$ ni yechishda $x > 7$ bo'ladi, belgi
o'zgarmaydi — chunki bu yerda $5$ ayirilmoqda, ko'paytirilmayapti.
**Qoida faqat ko'paytirish va bo'lishga tegishli, qo'shish/ayirishga emas.**

---

## Concept 3 — Yechimni Sonlar O'qida Ko'rsatish (Graphing the Solution)

### Definition

*Tengsizlik yechimini sonlar o'qida ko'rsatishda, chegara nuqtasi
tengsizlikka kiritilsa (ya'ni $\le$ yoki $\ge$ bo'lsa) **to'la (yopiq) doira**,
kiritilmasa (ya'ni $<$ yoki $>$ bo'lsa) **bo'sh (ochiq) doira** bilan
belgilanadi, so'ngra yechim tomoniga qarab chiziq tortiladi.*

| Belgi | Doira turi | English |
|---|---|---|
| $<$ yoki $>$ | Ochiq (bo'sh) doira — chegara kiritilmaydi | Open circle — boundary excluded |
| $\le$ yoki $\ge$ | Yopiq (to'la) doira — chegara kiritiladi | Closed circle — boundary included |

*(Model/Your-turn pattern skipped here — bu qoida tushuncha emas, shunchaki
belgilash konventsiyasi, Concept 2'ning yechimlariga qo'llanadi.)*

---

## Concept 4 — Qo'shma Tengsizliklar (Compound Inequalities)

### Definition

*Ikki tengsizlikning "va" (bir vaqtda ikkalasi ham to'g'ri) yoki "yoki"
(kamida bittasi to'g'ri) bog'lovchisi bilan birlashtirilgan ko'rinishi
qo'shma tengsizlik deb ataladi.*

<small>("And"-type compound inequalities require both conditions true at
once (often written as one three-part inequality); "or"-type require at
least one condition true, and are solved as two separate inequalities.)</small>

### Model Example (3-misol)

**"Va" turi:** $-3 < x+1 \le 5$ tengsizligini yeching.

**Yechish:** Uch qismning har biriga bir xil amal qo'llanadi — bu yerda
hammasidan $1$ ni ayiramiz: $-3-1 < x \le 5-1$, ya'ni $-4 < x \le 4$.

**"Yoki" turi:** $2x+1 < -3$ **yoki** $2x+1 > 7$.

**Yechish:** Har bir qismni alohida yechamiz. Birinchisi: $2x < -4$, ya'ni
$x < -2$. Ikkinchisi: $2x > 6$, ya'ni $x > 3$. Ikkala yechim "yoki" bilan
birlashtiriladi: $x < -2$ **yoki** $x > 3$.

**Javob:** $-4 < x \le 4$ ; va $x<-2$ yoki $x>3$

### Your-Turn Example (O'zingiz bajaring)

$-5 \le 2x+1 < 9$ tengsizligini yeching: $\underline{\hspace{30mm}}$

### Common Mistake Box

**Noto'g'ri:** Uch qismli tengsizlikni yechishda amalni faqat o'rtadagi va
bitta tomonga qo'llab, ikkinchi tomonni unutish. Masalan $-4 < 2x < 8$ ni
$2$ ga bo'lishda $-4 < x < 8$ deb yozish (chap tomon bo'linmagan).
**To'g'ri:** amal **barcha uchta qismga** qo'llanadi: $-2 < x < 4$.

### Notation Callout — Interval Notation (Semicolon vs. Comma)

Rus/O'zbek an'anaviy darsliklarida interval ko'pincha **nuqtali vergul**
bilan yoziladi: $(2;\ 5]$. SAT va ingliz tilidagi materiallarda esa **oddiy
vergul** ishlatiladi: $(2, 5]$. Ma'no bir xil — faqat belgi farq qiladi.
SAT'da nuqtali vergul ko'rsangiz, bu matn boshqa manbadan ekanini bilib
oling; o'zingiz yozganda doim vergul ishlating.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Linear equation | Chiziqli tenglama |
| Linear inequality | Chiziqli tengsizlik |
| Sign-flip rule | Ishorani almashtirish qoidasi |
| Open circle / Closed circle | Ochiq doira / Yopiq doira |
| Compound inequality | Qo'shma tengsizlik |
| And / Or (logical) | Va / Yoki |
| Interval notation | Interval (oraliq) belgilash |
| Boundary (of an inequality) | Chegara |

## Notes for the problems file (Sets 1–7)

1. Pure multi-step equation drill (fraction coefficients, both-sides variable).
2. "What's actually being asked" trap set — every item asks for an expression, not $x$ itself.
3. Inequality solving — mix of sign-flip-needed and sign-flip-not-needed cases.
4. Compound inequalities — both "and" and "or" types.
5. Word-phrase → inequality translation ("at least," "no more than," etc.).
6. Spot the error — five items, each targeting one documented misconception above.
7. Bonus/Challenge — combines fractions, compound inequalities, and the asked-for-wrong-thing trap, timed.
