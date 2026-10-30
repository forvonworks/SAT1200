# Book 1 — Lesson 6: One-Variable Equations

**Source content file.** This is the authored content, not the final page — it gets
typeset against `research/14-design-spec.md`. Structure follows that spec's
content-block pattern exactly (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary, repeated per concept on this lesson.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` ("Basic
linear equation solving (one-step, two-step, isolating a variable)" named as
a direct prerequisite for Algebra, the largest SAT domain at ~35%) and
`research/04-common-student-mistakes.md`'s Linear Equations section, which
documents three specific, well-attested error patterns used directly below:
sign-flip errors moving terms across the equals sign, inconsistent balancing
(an operation applied to only one side or only part of one side), and
solving for the wrong variable/expression (the single most frequently cited
"trap answer" mechanism across SAT topics, not just equations).

---

## Concept 1 — Tenglama, Yechim va Bir Qadamli Tenglamalar

### Definition

*Tarkibida noma'lum miqdor (odatda $x$ harfi bilan belgilanadi) bo'lgan va
ikki ifoda orasidagi tenglikni ifodalovchi tenglik tenglama deb ataladi.
Tenglamani to'g'ri sonli tenglikka aylantiradigan noma'lumning qiymati
tenglamaning yechimi (yoki ildizi) deb ataladi.*

<small>(An equation is a statement that two expressions are equal, containing
an unknown quantity — usually $x$. The value of the unknown that makes the
equation a true numerical statement is called its solution, or root.)</small>

**Tenglamani yechish qoidasi:** noma'lumni tenglamaning bir tomonida yolg'iz
qoldirish uchun, tenglamaning **ikkala tomoniga ham** bir xil amal
qo'llaniladi — bu amal har doim berilgan amalga **teskari amal** bo'ladi:
qo'shishga ayirish, ayirishga qo'shish, ko'paytirishga bo'lish, bo'lishga
ko'paytirish mos keladi.

### Model Example (1-misol)

$$x + 7 = 12$$

**Yechish:** Noma'lumni yolg'iz qoldirish uchun, qo'shishga teskari amal —
ayirish — ikkala tomonga ham qo'llaniladi: $x + 7 - 7 = 12 - 7$. Bundan
$x = 5$.

**Tekshirish:** $5 + 7 = 12$ — to'g'ri. (Har doim javobni original
tenglamaga qo'yib tekshiring, oraliq qatorga emas — bu ishorа xatolarini
ushlab oladi.)

**Javob:** $x = 5$

### Your-Turn Example (O'zingiz bajaring)

$$x - 9 = 4 \qquad x = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Amalni tenglamaning faqat bir tomoniga yoki bir
tomonining faqat bir qismiga qo'llash.

**To'g'ri qoida:** Tenglamaning tengligini saqlab qolish uchun, qanday amal
bajarilsa, u **ikkala tomonga to'liq** qo'llanishi shart. $x - 5 = 12$
tenglamasida ikkala tomonga $5$ qo'shilsa: $x = 12 + 5 = 17$ — to'g'ri
natija. Agar faqat chap tomonga qo'shilsa ($x = 12$), natija noto'g'ri
chiqadi.

*(Research basis: documented as "inconsistent balancing of the equation" —
performing an operation on one side only, or on only part of one side — a
recurring error type named in curriculum error-analysis guides. See
`research/04-common-student-mistakes.md`.)*

---

## Concept 2 — Ikki Qadamli Tenglamalar

### Definition

*Noma'lumni topish uchun ikkita ketma-ket teskari amal talab qiladigan
tenglama ikki qadamli tenglama deb ataladi. Bunda amallar teskari
tartibda — avval qo'shish/ayirish, so'ngra ko'paytirish/bo'lish — bekor
qilinadi, chunki bu amallar bajarish tartibining (Lesson 1) aynan teskarisi.*

<small>(A two-step equation needs two sequential inverse operations to
isolate the unknown. The operations are undone in reverse order — addition/
subtraction first, then multiplication/division — because this is exactly
the reverse of the order-of-operations sequence from Lesson 1.)</small>

### Model Example (2-misol)

$$3x - 5 = 10$$

**Yechish:** Avval qo'shish/ayirish bosqichi bekor qilinadi: ikkala tomonga
$5$ qo'shiladi: $3x = 15$. Endi ko'paytirish bosqichi bekor qilinadi:
ikkala tomon $3$ ga bo'linadi: $x = 5$.

**Tekshirish:** $3(5) - 5 = 15 - 5 = 10$ — to'g'ri.

**Javob:** $x = 5$

### Your-Turn Example (O'zingiz bajaring)

$$\dfrac{x}{2} + 4 = 9 \qquad x = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Amallarni noto'g'ri tartibda bekor qilish — masalan,
avval $3$ ga bo'lib, keyin $5$ ni qo'shish.

**To'g'ri qoida:** Amallar har doim **amallar bajarish tartibining teskarisi**
tartibida bekor qilinadi. $3x - 5 = 10$ da avval $-5$ (qo'shish/ayirish
bosqichi) bekor qilinadi, keyin $\times 3$ (ko'paytirish bosqichi) bekor
qilinadi — aksincha emas. Agar avval $3$ ga bo'linsa: $x - \frac{5}{3} =
\frac{10}{3}$ — bu ham yechiladi, lekin keraksiz kasrlar paydo bo'ladi va
xatoga olib kelish ehtimoli oshadi.

---

## Concept 3 — Ko'p Qadamli Tenglamalar: Qavs Ochish va O'xshash Hadlar

### Definition

*Qavslarni ochish va o'xshash hadlarni ixchamlashtirishni talab qiladigan
tenglama ko'p qadamli tenglama deb ataladi. Qavs ochishda, qavs oldidagi son
qavs ichidagi har bir hadga alohida ko'paytiriladi (distributiv xossa);
o'xshash hadlar deb, bir xil noma'lumga ega bo'lgan (yoki noma'lumsiz)
hadlarga aytiladi — ular birgalikda qo'shiladi yoki ayiriladi.*

<small>(A multi-step equation requires expanding parentheses and combining
like terms. Expanding a parenthesis means multiplying the number in front of
it by every term inside (the distributive property); like terms are terms
sharing the same variable (or no variable), which are added or subtracted
together.)</small>

### Model Example (3-misol)

$$2(x - 4) + 5 = 7$$

**Yechish:** Avval qavs ochiladi: $2 \times x = 2x$, $2 \times (-4) = -8$,
shuning uchun $2(x-4) = 2x - 8$. Ifoda: $2x - 8 + 5 = 7$. O'xshash hadlar
($-8$ va $5$) ixchamlashtiriladi: $2x - 3 = 7$. Endi ikki qadamli tenglama
kabi yechiladi: $2x = 10$, so'ng $x = 5$.

**Tekshirish:** $2(5-4) + 5 = 2(1) + 5 = 2 + 5 = 7$ — to'g'ri.

**Javob:** $x = 5$

### Your-Turn Example (O'zingiz bajaring)

$$4x + 2x - 3 = 15 \qquad x = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Manfiy son bilan qavs ochilganda, qavs ichidagi
hadlarning faqat biriga ishorа o'zgartiriladi. Masalan, $-2(x+3) = 10$ da
$-2x + 3 = 10$ deb yozish (ikkinchi hadning ishorаsi o'zgartirilmagan).

**To'g'ri qoida:** Qavs oldidagi son qavs ichidagi **har bir hadga**,
ishorаsi bilan birga, ko'paytiriladi: $-2(x+3) = -2 \times x + (-2) \times 3
= -2x - 6$. Xatoni oldini olish uchun, manfiy son bilan qavs ochishni alohida
qadam sifatida, qavs ichidagi har bir hadni aniq yozib chiqib bajaring —
boshqa amallar bilan birlashtirmang.

*(Research basis: a specific, commonly recommended fix for this exact error
— rewriting the negative-distributed expression explicitly as a separate
step before simplifying further. See `research/04-common-student-mistakes.md`.)*

---

## Concept 4 — Ikkala Tomonda Noma'lum Bo'lgan Tenglamalar

### Definition

*Noma'lum ($x$) tenglamaning ham chap, ham o'ng tomonida uchraydigan
tenglama ikkala tomonda noma'lum bo'lgan tenglama deb ataladi. Bunday
tenglamani yechish uchun, avval barcha noma'lumli hadlar tenglamaning bir
tomoniga, barcha sonli hadlar esa ikkinchi tomoniga yig'iladi.*

<small>(An equation with the unknown on both sides needs the variable terms
collected on one side and the constant terms on the other before it reduces
to a familiar one- or two-step equation.)</small>

### Model Example (4-misol)

$$5x - 2 = 2x + 7$$

**Yechish:** Noma'lumli hadlarni chap tomonga yig'ish uchun, ikkala tomondan
$2x$ ayiriladi: $5x - 2x - 2 = 7$, ya'ni $3x - 2 = 7$. Endi sonli hadlarni
o'ng tomonga yig'ish uchun, ikkala tomonga $2$ qo'shiladi: $3x = 9$. Nihoyat,
ikkala tomon $3$ ga bo'linadi: $x = 3$.

**Tekshirish:** Chap tomon: $5(3) - 2 = 13$. O'ng tomon: $2(3) + 7 = 13$ —
teng, demak to'g'ri.

**Javob:** $x = 3$

### Your-Turn Example (O'zingiz bajaring)

$$x + 8 = 3x - 2 \qquad x = \underline{\hspace{25mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Hadni tenglamaning bir tomonidan ikkinchi tomonga
"o'tkazishda" ishorаsini o'zgartirishni unutish.

**To'g'ri qoida:** Had tenglamaning bir tomonidan ikkinchisiga o'tganda, bu
aslida o'sha hadni ikkala tomondan ayirish (yoki qo'shish) amalining
qisqartirilgan yozuvidir — shuning uchun had **har doim ishorаsini
o'zgartiradi**. $3x + 4 = x + 10$ da $x$ ni o'ng tomondan chap tomonga
"o'tkazish" aslida ikkala tomondan $x$ ni ayirish degani: $3x - x + 4 = 10$,
ya'ni $2x + 4 = 10$ — ishorа to'g'ri o'zgardi, chunki amal aniq bajarildi,
taxmin qilinmadi.

*(Research basis: "sign flip errors when moving terms across the equals
sign" — one of the most consistently cited linear-equation mistakes across
tutoring sources. See `research/04-common-student-mistakes.md`.)*

**Ikkinchi keng tarqalgan xato, SAT uchun muhim:** savolda $x$ emas, balki
$x$ ni o'z ichiga olgan ifoda (masalan $3x$ yoki $x+4$) so'ralishi mumkin.
Tenglamani to'g'ri yechib, lekin savolda aynan nima so'ralganini
tekshirmasdan, $x$ ning qiymatini javob sifatida belgilash — barcha SAT
mavzularida eng ko'p uchraydigan "tузоq javob" mexanizmlaridan biri.

*(Research basis: named as one of the most frequently cited "trap answer"
mechanisms across all SAT topics, not just equations — students stop as
soon as they reach a familiar-looking number. See
`research/04-common-student-mistakes.md`.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Equation | Tenglama |
| Solution / Root | Yechim / Ildiz |
| Unknown / Variable | Noma'lum / O'zgaruvchi |
| Inverse operation | Teskari amal |
| Isolate (the variable) | (Noma'lumni) yolg'iz qoldirish |
| Distributive property / Expand brackets | Distributiv xossa / Qavs ochish |
| Like terms | O'xshash hadlar |
| Coefficient | Koeffitsient |
| Check (the answer) | Tekshirish |

---

## Notes for the problems file (Sets 1–7)

- Set 1: pure one-step equations (all four inverse operations).
- Set 2: two-step equations, reinforcing reverse-order undoing.
- Set 3: multi-step — distribution (including negative coefficients) +
  combining like terms.
- Set 4: variable on both sides.
- Set 5: mixed, SAT-style — several items ask for a derived expression
  (e.g. "what is $3x$?", "what is $x+4$?") rather than $x$ itself, directly
  drilling the "solve for the wrong thing" trap from Concept 4's second
  common-mistake box.
- Set 6: "spot the error" — five items, each targeting one of the
  documented misconceptions above (one-sided operation, sign-flip crossing
  the equals sign, incomplete negative distribution, combining unlike terms,
  answering $x$ instead of the asked expression).
- Set 7 (bonus/challenge): equations combining fractions and parentheses,
  timed.
