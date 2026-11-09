# Book 3 — Lesson 5: Bonus Insight — Logarithms & Unit Circle

**Source content file**, paired with `problems.md`. Unlike every other lesson in this
series, this one has **zero grounding in the official College Board Question Bank** — the
real-data analysis in `research/15-question-bank-analysis.md` and the official skill list in
`research/01-official-sat-math-spec.md` both confirm logarithms and the unit circle are
simply not named anywhere in the SAT's Algebra/Advanced Math/Geometry & Trigonometry skill
tags. This lesson is not test prep. It exists because a student who has finished Books 1–2
and all of Book 3's hard-tier lessons has earned a look at where the math they already know
leads next — and because seeing the "why" behind a tool makes the tool feel less arbitrary,
even when the tool itself won't be graded.

> **MUHIM OGOHLANTIRISH — bu dars SAT'da sinalmaydi.**
> **IMPORTANT WARNING — this lesson is not tested on the SAT.**
>
> *Quyidagi mavzular — logarifmlar va birlik aylana — rasmiy SAT Matematika dasturida
> (`research/01`) umuman tilga olinmaydi. Bu darsni SAT tayyorgarligining bir qismi sifatida
> emas, balki mukofot sifatida o'qing: Kitob 1-2 va shu kitobning qolgan barcha darslarini
> tugatgan talaba uchun qiziqarli bonus tushuncha. Bu yerda vaqtingizni sarflashdan oldin,
> SAT'da haqiqatan sinaladigan barcha mavzularni mustahkamlab bo'lganingizga ishonch hosil
> qiling.*
>
> *(The topics below — logarithms and the unit circle — are not mentioned anywhere in the
> official SAT Math specification. Read this lesson not as SAT preparation, but as a reward:
> an interesting bonus concept for a student who has finished Books 1–2 and every other
> lesson in this book. Before spending time here, make sure every topic that IS actually
> tested on the SAT is solid.)*
>
> One precise exception worth knowing: the **special right-triangle ratios** (30-60-90 and
> 45-45-90) from Book 2 Lesson 22 ARE testable — they're on the SAT's built-in reference
> sheet. What's not tested is the *unit-circle framing* itself (angles beyond 90°, full
> 360° rotation, radian measure) — Concept 2 below shows how that framing connects to the
> triangle ratios you already know, as a bonus perspective, not new testable material.

---

## Concept 1 — Logarithms: Undoing an Exponential

### Definition

*Agar $b^y = x$ bo'lsa, u holda $y$ ni $x$ ning $b$ asosiga ko'ra **logarifmi** deb ataladi
va $y = \log_b(x)$ deb yoziladi; boshqacha aytganda, logarifm — ko'rsatkichli amalni
teskari yo'nalishda bajarish, ya'ni "$b$ ni qaysi darajaga ko'tarsam $x$ chiqadi?" degan
savolga javob beradi.*

<small>(If $b^y = x$, then $y$ is called the logarithm of $x$ to base $b$, written
$y = \log_b(x)$ — in other words, a logarithm answers "to what power must I raise $b$ to
get $x$?")</small>

**Nega bu kerak bo'ladi — Book 2 Lesson 8'ga qaytish:** o'sha darsda $y = a(1+r)^x$
formulasi bilan, $x$ (vaqt) berilganda $y$ (miqdor) ni topish o'rgatilgan edi. Lekin
teskarisi-chi — $y$ berilib, $x$ ni topish kerak bo'lsa (masalan, "miqdor qachon $100$ ga
yetadi?")? Book 2'ning vositalari (ko'paytirish, daraja) buni to'g'ridan-to'g'ri yecha
olmaydi — aynan shu yerda logarifm kerak bo'ladi.

$$\log_2(8) = 3 \quad \text{chunki} \quad 2^3 = 8 \qquad\qquad
\log_{10}(1000) = 3 \quad \text{chunki} \quad 10^3 = 1000$$

### Model Example (1-misol)

$2^x = 100$ tenglamasini yeching (aniq, kasr son javob bilan).

**Yechish:** Bu tenglamani Book 2'ning vositalari bilan to'g'ridan-to'g'ri yechib
bo'lmaydi — $2^6=64$ va $2^7=128$, demak $x$ $6$ va $7$ orasida, lekin butun son emas.
Logarifm ta'rifiga ko'ra, agar $2^x=100$ bo'lsa, $x = \log_2(100)$. Kalkulyatordan:
$x = \log_2(100) \approx 6.644$.

**Javob:** $x \approx 6.644$

*(E'tibor bering: $2^{6.644}$ ni hisoblab ko'rsangiz, haqiqatan ham taxminan $100$ chiqadi —
logarifm shunchaki "qaysi daraja" savoliga sonli javob beradi.)*

### Logarithm Properties (intuitive level — not exhaustive)

| Qoida (Rule) | Ma'no |
|---|---|
| $\log_b(mn) = \log_b(m) + \log_b(n)$ | Ko'paytmaning logarifmi — logarifmlar yig'indisi |
| $\log_b\left(\dfrac{m}{n}\right) = \log_b(m) - \log_b(n)$ | Bo'linmaning logarifmi — logarifmlar ayirmasi |
| $\log_b(m^k) = k\log_b(m)$ | Darajaning logarifmi — ko'rsatkich oldinga chiqadi |

**Intuitive aloqasi:** bular — darajalar qoidalarining (Book 1 Lesson 7) "teskari tomondan"
ko'rinishi. Darajalarda ko'paytirish — ko'rsatkichlarni qo'shish edi ($a^m \times a^n =
a^{m+n}$); logarifmda esa ko'paytmaning logarifmi — logarifmlarning qo'shilishi. Bir xil
g'oya, ikki yo'nalishda.

### Your-Turn Example (O'zingiz bajaring)

$5^x = 3$ tenglamasini yeching: $x = \log_5(3) = \underline{\hspace{25mm}}$
*(Kalkulyatordan taxminiy qiymat toping.)*

---

## Concept 2 — The Unit Circle: Trigonometry Beyond 90°

### Definition

*Markazi koordinata boshida va radiusi $1$ ga teng bo'lgan aylana **birlik aylana** deb
ataladi; bu aylana ustidagi, musbat $x$ o'qidan $\theta$ burchak masofasida joylashgan
nuqtaning koordinatalari aynan $(\cos\theta, \sin\theta)$ ga teng bo'ladi.*

<small>(A circle of radius 1 centered at the origin is called the unit circle; the point on
this circle at angle $\theta$ from the positive $x$-axis has coordinates exactly
$(\cos\theta, \sin\theta)$.)</small>

**Book 2 Lesson 22'ga bog'lanish:** o'sha darsda $\sin$ va $\cos$ faqat to'g'ri burchakli
uchburchakning **o'tkir** burchaklari ($0°$ dan $90°$ gacha) uchun ta'riflangan edi — katet
va gipotenuza nisbati sifatida. Birlik aylana esa xuddi shu $\sin$ va $\cos$ tushunchalarini
**har qanday** burchak uchun — $90°$ dan katta, hatto manfiy yoki $360°$ dan katta
burchaklar uchun ham — kengaytiradi. Uchburchak endi kerak emas: burchak shunchaki aylana
bo'ylab qancha "aylanganini" ko'rsatadi.

| $\theta$ | Nuqta $(\cos\theta, \sin\theta)$ |
|---|---|
| $0°$ | $(1, 0)$ |
| $90°$ | $(0, 1)$ |
| $180°$ | $(-1, 0)$ |
| $270°$ | $(0, -1)$ |
| $360°$ | $(1, 0)$ — boshlang'ich nuqtaga qaytadi |

### Model Example (2-misol)

$30°$-$60°$-$90°$ maxsus uchburchagining nisbatlarini (Book 2 Lesson 22, SAT ma'lumot
varag'ida berilgan) ishlatib, birlik aylanadagi $\theta=30°$ nuqtasining koordinatalarini
toping.

**Yechish:** $30°$-$60°$-$90°$ uchburchakda (gipotenuza $=1$ bo'lganda) $30°$ burchakka
qarama-qarshi katet $=\frac12$, qo'shni katet $=\frac{\sqrt3}{2}$. Birlik aylanada bu
to'g'ridan-to'g'ri koordinatalarga aylanadi: $\cos30° = \frac{\sqrt3}{2} \approx 0.866$
(qo'shni/gipotenuza), $\sin30° = \frac12 = 0.5$ (qarama-qarshi/gipotenuza).

**Javob:** $\left(\dfrac{\sqrt3}{2}, \dfrac12\right) \approx (0.866,\ 0.5)$

*(Bu — Book 2 Lesson 22'dagi SOH-CAH-TOA bilan bir xil hisob, faqat endi natija "uchburchak
nisbati" emas, "aylana ustidagi nuqta" sifatida talqin qilinmoqda. SAT bu talqinni so'ramaydi
— lekin maxsus uchburchak nisbatlarining o'zi, yuqorida eslatilganidek, ma'lumot varag'ida
berilgani uchun sinaladi.)*

### Your-Turn Example (O'zingiz bajaring)

$45°$-$45°$-$90°$ maxsus uchburchak nisbatlaridan foydalanib, $\theta=45°$ uchun
$(\cos45°, \sin45°)$ nuqtasini toping: $\underline{\hspace{35mm}}$

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Logarithm | Logarifm |
| Base (of a logarithm) | Asos |
| Inverse operation | Teskari amal |
| Unit circle | Birlik aylana |
| Radian | Radian |
| Full rotation | To'liq aylanish |

---

## Notes for the problems file

Short — this is bonus material, not a tested skill, so it gets 2-3 light sets rather than
the usual 6-7:

1. Evaluate simple logarithms directly from the definition (no calculator needed —
   designed to come out to clean integers).
2. Convert between exponential and logarithmic form; solve simple equations both ways
   (including one or two needing a calculator for a non-integer answer).
3. Bonus: unit-circle coordinates at the "axis" angles (0°/90°/180°/270°/360°) and the
   three special angles (30°/45°/60°), reusing Book 2 Lesson 22's special-triangle ratios.
