# Book 2 — Lesson 17: Probability Fundamentals

**Source content file**, paired with `problems.md`. Probability is one of the
most consistently underweighted topics in the Uzbek school curriculum — the
2025/26 Grade-10 exam specification gives "Statistika va ehtimollik" only
7.5% of items, and probability/statistics entered the post-Soviet curricular
tradition very late and thinly (`research/05-uzbek-student-considerations.md`).
Do not assume prior fluency here the way Book 2's algebra lessons can assume
Book 1 groundwork — this lesson builds probability from the actual
definition up, at Book 2's SAT-ceiling depth.

This lesson's center of gravity is Concept 3: the distinction between
**mutually exclusive** events and **independent** events. These two ideas
sound similar, get taught with similar-sounding names, and are confused
constantly — including by strong students — but they answer two completely
different questions, and (as the Model Example proves directly) a pair of
events that are mutually exclusive with nonzero probabilities can *never*
be independent. This is the lesson's documented conceptual gap and gets the
most page weight.

---

## Concept 1 — Ehtimollik: Imkoniyat / Jami nisbati (Basic Probability, Including From a Table)

**Ta'rif:** Ehtimollik (probability) — biror hodisaning yuz berish imkoniyatini
sonlar bilan o'lchash usuli bo'lib, u *qulay holatlar sonini jami holatlar
soniga nisbati* sifatida hisoblanadi:

$$P(\text{hodisa}) = \frac{\text{qulay holatlar soni}}{\text{jami holatlar soni}}$$

**English:** Probability measures how likely an event is, as a number from
$0$ (impossible) to $1$ (certain): $P(\text{event}) = \dfrac{\text{favorable
outcomes}}{\text{total outcomes}}$. It can be written as a fraction, decimal,
or percent — all three are the same number, and the SAT uses all three
freely, so don't let a format switch (e.g. an answer choice given as a
percent when you computed a fraction) throw you.

**A probability doesn't have to come from a dice/cards setup — it very
often comes from a table of data** (a frequency table, a survey result
table, a two-way table). In that case, "total outcomes" is the relevant row,
column, or grand total, and "favorable outcomes" is the count that matches
the condition. This is the single most common SAT probability format, and
table-*reading* errors (grabbing the wrong row/column total) are more common
than any probability-formula error.

*(Nima so'ralmoqda? — before dividing anything, underline exactly which
group the question is asking about: "the probability that a student is
female *and* likes basketball" uses one cell; "the probability that a
student is female" uses a row/column total; "the probability that a student
likes basketball, *given that* she is female" restricts the total itself to
just the female row. Reading the condition correctly is the whole problem —
once you know the right numerator and the right denominator, the division is
trivial.)*

### Model Example (1-misol)

Maktabda 200 o'quvchi bor. Ulardan 120 nafari futbolni, 80 nafari esa
basketbolni afzal ko'radi (har bir o'quvchi faqat bittasini tanlagan).
Tasodifan tanlangan o'quvchining basketbolni afzal ko'rish ehtimolini toping.

**Yechish:** Jami o'quvchilar soni — $200$. Basketbolni afzal ko'radiganlar
— $80$. $P(\text{basketbol}) = \dfrac{80}{200} = \dfrac{2}{5} = 0.4 = 40\%$.

**Javob:** $P = \dfrac{2}{5}$ (yoki $0.4$, yoki $40\%$ — barchasi bir xil son)

### Your-Turn Example (O'zingiz bajaring)

Sinfda 30 o'quvchi bor, ulardan 18 nafari qizlar. Tasodifan tanlangan
o'quvchining o'g'il bola bo'lish ehtimoli $= \underline{\hspace{25mm}}$

---

## Concept 2 — Birgalikda Bo'lmaydigan Hodisalar va Qo'shish Qoidasi (Mutually Exclusive Events and the Addition Rule)

**Ta'rif:** Ikki hodisa **birgalikda bo'lmaydigan** (mutually exclusive)
deb ataladi, agar ular *bir vaqtda yuz berishi mumkin bo'lmasa* — ya'ni
ularning umumiy natijasi yo'q. Masalan, bitta zar tashlanganda "3 tushishi"
va "4 tushishi" — birgalikda bo'lmaydi, chunki bir tashlashda faqat bitta
son chiqadi.

**English:** Two events are **mutually exclusive** if they share no
outcomes — they cannot both happen at the same time. "Rolling a 3" and
"rolling a 4" on one die are mutually exclusive.

**Qo'shish qoidasi (addition rule):**

- Agar $A$ va $B$ birgalikda bo'lmasa: $P(A \text{ yoki } B) = P(A) + P(B)$
- Agar $A$ va $B$ birgalikda bo'lishi mumkin bo'lsa (ustma-ust tushadigan
  qismi bor): $P(A \text{ yoki } B) = P(A) + P(B) - P(A \text{ va } B)$

The second (general) form is the one to default to — it's always correct;
the simple "just add them" version is only a special case of it, valid
*only* when $P(A \text{ va } B) = 0$. **The single most common error here is
forgetting to subtract the overlap** when the two events *can* happen
together (e.g. "rolling an even number" and "rolling greater than 3" on a
die both happen at once on a roll of 4 or 6 — subtract that double-count,
or you overestimate the probability).

### Model Example (2-misol)

Bir zar tashlanadi. Juft son tushish yoki $3$ dan katta son tushish
ehtimolini toping.

**Yechish:** $A$ = juft son $= \{2,4,6\}$, $P(A) = \frac{3}{6}$. $B$ = $3$
dan katta son $= \{4,5,6\}$, $P(B) = \frac{3}{6}$. Bu hodisalar birgalikda
bo'lmaydigan emas — $4$ va $6$ ikkalasiga ham mos keladi, ya'ni
$P(A \text{ va } B) = \frac{2}{6}$. Shuning uchun umumiy qoidani
qo'llaymiz: $P(A \text{ yoki } B) = \frac{3}{6}+\frac{3}{6}-\frac{2}{6} =
\frac{4}{6} = \frac{2}{3}$.

**Javob:** $P = \dfrac{2}{3}$

*(Tekshirish: to'g'ridan-to'g'ri sanab ko'rsak, $\{2,4,5,6\}$ — 4 ta mos son,
jami 6 tadan, demak $\frac{4}{6}=\frac{2}{3}$. Mos keladi.)*

### Your-Turn Example (O'zingiz bajaring)

Bir zar tashlanadi. $5$ dan kichik son tushish yoki toq son tushish
ehtimoli $= \underline{\hspace{25mm}}$

### Umumiy Xato (Common Mistake)

**Xato:** Ustma-ust tushadigan holatni hisobga olmaslik — ya'ni hodisalar
bir vaqtda yuz berishi mumkin bo'lganda ham oddiy $P(A)+P(B)$ formulasini
qo'llash, natijada haqiqiy ehtimoldan kattaroq (ba'zan $1$ dan ham katta!)
javob chiqishi.

**To'g'ri yondashuv:** Har doim avval so'rang: *"Bu ikki hodisa bir vaqtda
yuz berishi mumkinmi?"* Agar ha bo'lsa — albatta $P(A \text{ va } B)$ ni
ayirib tashlang.

---

## Concept 3 — Mustaqil Hodisalar vs. Birgalikda Bo'lmaydigan Hodisalar (Independence vs. Mutual Exclusivity — the Core of This Lesson)

**Ta'rif (mustaqillik):** Ikki hodisa **mustaqil** (independent) deyiladi,
agar bittasining yuz berishi ikkinchisining ehtimolligiga *hech qanday
ta'sir qilmasa*. Masalan, bir tangani ikki marta tashlashda, birinchi
tashlashda "gerb" tushishi ikkinchi tashlashning natijasiga umuman ta'sir
qilmaydi — bular mustaqil.

**English:** Two events are **independent** if the occurrence of one does
not change the probability of the other. **Multiplication rule (only valid
for independent events):** $P(A \text{ va } B) = P(A) \times P(B)$.

**This is where the two ideas get confused — and they are asking two
completely different questions:**

| | Mutually exclusive | Independent |
|---|---|---|
| Question it answers | *Can they happen together at all?* | *Does one happening change the other's probability?* |
| Condition | $P(A \text{ va } B) = 0$ | $P(A \text{ va } B) = P(A)\times P(B)$ |
| Relevant rule | Addition rule | Multiplication rule |

**They are not opposites, and they are not synonyms — and here is the
single most important fact that ties them together:** if two events are
mutually exclusive AND each has a nonzero probability, they are
**automatically NOT independent.** Why: if $A$ happens, $B$ becomes
*impossible* ($P(B\mid A) = 0$) — that is about as strong an effect on
$B$'s probability as there is. "No overlap" is itself a dependency.

### Model Example (3-misol) — Side-by-Side Contrast

**A.** Bitta zar tashlanadi. $A$ = "3 tushishi", $B$ = "4 tushishi".

- Birgalikda bo'lmaydiganmi? **Ha** — bir tashlashda faqat bitta son
  chiqadi, $3$ va $4$ bir vaqtda chiqa olmaydi: $P(A \text{ va } B)=0$.
- Mustaqilmi? **Yo'q.** Tekshiramiz: $P(A)=\frac16$, $P(B)=\frac16$, demak
  mustaqil bo'lsa $P(A \text{ va } B)$ $\frac16\times\frac16=\frac{1}{36}$
  ga teng bo'lishi kerak edi. Ammo haqiqiy qiymat $0$, $\frac{1}{36}$ ga
  teng emas. Demak **mustaqil emas** — aslida bu yerda eng kuchli bog'liqlik
  bor: $A$ yuz bersa, $B$ ning ehtimoli $\frac16$ dan $0$ ga tushadi.

**B.** Tanga ikki marta tashlanadi. $A$ = "birinchi tashlashda gerb", $B$ =
"ikkinchi tashlashda raqam".

- Birgalikda bo'lmaydiganmi? **Yo'q** — ikkalasi bir vaqtda, ya'ni bir xil
  tajribada, mustaqil ravishda yuz berishi mumkin (gerb, keyin raqam —
  bemalol bo'lishi mumkin natija).
- Mustaqilmi? **Ha.** Birinchi tashlash ikkinchisiga hech qanday ta'sir
  qilmaydi: $P(A \text{ va } B) = \frac12\times\frac12=\frac14$, va buni
  to'g'ridan-to'g'ri sanab ham tasdiqlash mumkin (GG, GR, RG, RR — 4
  natijadan 1 tasi GR).

**Javob/Xulosa:** (A) — birgalikda bo'lmaydigan, mustaqil emas. (B) —
mustaqil, birgalikda bo'lmaydigan emas. Bu ikki holat bir-birining
oynadagi aksi — va aynan shuning uchun ularni chalkashtirish oson, lekin
ular hech qachon bir xil narsani anglatmaydi.

### Your-Turn Example (O'zingiz bajaring)

Quyidagi juftlikni tekshiring: Bir xaltada 5 qizil va 5 ko'k shar bor.
Birinchi sharni tortib olib, **qaytarmay**, ikkinchi sharni tortamiz.
$A$ = "birinchi shar qizil", $B$ = "ikkinchi shar qizil". Bu hodisalar
mustaqilmi? Birgalikda bo'lmaydiganmi (ya'ni ikkalasi ham qizil bo'lishi
mumkin emasmi)? $\underline{\hspace{45mm}}$

*(Maslahat: qaytarmasdan tortish — bu "replacement"siz tanlash degani;
birinchi natija ikkinchisining shartlarini o'zgartiradi.)*

### Umumiy Xato (Common Mistake)

**Xato:** "Bu hodisalar bir-biriga bog'liq emas" degan intuitiv tuyg'uni
"demak ular ham mustaqil, ham birgalikda bo'lmaydi" deb talqin qilish —
ya'ni ikki tushunchani sinonim sifatida ishlatish, yoki birini isbotlab,
ikkinchisini ham avtomatik to'g'ri deb hisoblash.

**To'g'ri yondashuv:** Har doim ikkitasini alohida tekshiring:
(1) $P(A \text{ va } B)=0$ bo'lsa — birgalikda bo'lmaydigan;
(2) $P(A \text{ va } B)=P(A)\times P(B)$ bo'lsa — mustaqil. Agar ikkala
hodisaning ehtimolligi noldan katta bo'lsa, ular **hech qachon** bir vaqtda
ikkalasi ham to'g'ri bo'la olmaydi — mutually exclusive (nonzero) always
implies NOT independent.

---

## Lug'at (Vocabulary)

| O'zbekcha | English |
|---|---|
| Ehtimollik | Probability |
| Qulay holat | Favorable outcome |
| Jami holatlar soni | Total outcomes |
| Birgalikda bo'lmaydigan hodisalar | Mutually exclusive events |
| Mustaqil hodisalar | Independent events |
| Qo'shish qoidasi | Addition rule |
| Ko'paytirish qoidasi | Multiplication rule |
| Kesishma (A va B) | Intersection (A and B) |
| Qaytarmasdan tanlash | Selection without replacement |
| Shartli ehtimollik | Conditional probability |
