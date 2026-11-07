# Book 2 — Lesson 8: Exponential Functions & Growth/Decay

**Source content file.** Structure follows `research/14-design-spec.md`'s content
pattern (Definition → Model → Your-turn → conditional Common Mistake →
Vocabulary), same as every lesson so far. This lesson builds directly on
**Book 1 Lesson 7** (same-base exponent rules, zero/negative exponents — not
re-taught here) and **Book 2 Lesson 3** (linear functions, rate-of-change
framing, the f(x) bridge). Book 2 framing: more rigorous than Book 1's bare
fundamentals.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` explicitly
names "linear vs. exponential (additive vs. multiplicative) confusion" as a
documented error pattern, and separately names "percent/ratio base confusion
... additive instead of multiplicative reasoning on successive percent
changes" as arguably the single most persistent pain point across the whole
series. Both are centered in this lesson, not treated as footnotes.

---

## Concept 1 — Chiziqli va Ko'rsatkichli O'sish (Linear vs. Exponential Growth)

### Definition

*Har bir teng davrda bir xil MIQDORGA ortadigan (yoki kamayadigan) o'zgarish
chiziqli o'sish deb ataladi; har bir teng davrda bir xil KOEFFITSIENTGA
(ko'paytuvchiga) ortadigan o'zgarish esa ko'rsatkichli o'sish deb ataladi.
Birinchisi qo'shish orqali, ikkinchisi esa ko'paytirish orqali o'zgaradi —
va bu ikkisini chalkashtirib yuborish SAT'da eng ko'p uchraydigan konseptual
xatolardan biridir.*

<small>(A change that adds the same AMOUNT every period is linear growth; a
change that multiplies by the same FACTOR every period is exponential
growth. One changes by addition, the other by multiplication — and mixing
these two up is one of the most common conceptual errors on the SAT.)</small>

**Jadvaldan qanday aniqlash mumkin:** ketma-ket qiymatlar orasidagi
**AYIRMA** doim bir xil bo'lsa — chiziqli. Ketma-ket qiymatlar orasidagi
**NISBAT** (keyingisini oldingisiga bo'lish) doim bir xil bo'lsa —
ko'rsatkichli.

| $x$ | 0 | 1 | 2 | 3 | Turi |
|---|---|---|---|---|---|
| Chiziqli misol | 3 | 7 | 11 | 15 | Ayirma doim $+4$ |
| Ko'rsatkichli misol | 5 | 10 | 20 | 40 | Nisbat doim $\times2$ |

**Bu yerda e'tiborli bo'ling (keng tarqalgan "doimiy tezlik" tузоq):**
"doimiy tezlikda" degan so'z birikmasi ikki xil narsani anglatishi mumkin —
agar har safar bir xil **SON** (masalan, "har yili \$1500 ga") o'zgarsa, bu
chiziqli; agar har safar bir xil **FOIZ** (masalan, "har yili 7% ga")
o'zgarsa, bu ko'rsatkichli. "Doimiy tezlik" so'zini ko'rganda, avval "son"mi
yoki "foiz"mi ekanligini aniqlang.

### Model Example (1-misol)

Jadval berilgan: $x=0,1,2,3$ uchun $y=2,4,8,16$. Bu chiziqlimi yoki
ko'rsatkichlimi? Qoidani toping.

**Yechish:** Ayirmalarni tekshiramiz: $4-2=2$, $8-4=4$, $16-8=8$ — doim bir
xil emas, demak chiziqli emas. Nisbatlarni tekshiramiz: $\frac{4}{2}=2$,
$\frac{8}{4}=2$, $\frac{16}{8}=2$ — doim $2$, demak **ko'rsatkichli**.
Boshlang'ich qiymat $a=2$ (qachon $x=0$), koeffitsient $2$. Qoida:
$y = 2\times2^x$.

**Javob:** Ko'rsatkichli, $y=2\times2^x$

### Your-Turn Example (O'zingiz bajaring)

Jadval: $x=0,1,2,3$ uchun $y=10, 12.5, 15, 17.5$. Chiziqlimi yoki
ko'rsatkichlimi? Qoidani toping: $\underline{\hspace{40mm}}$

---

## Concept 2 — O'sish va Kamayish Formulasi: $y=a(1+r)^x$ va $y=a(1-r)^x$

### Definition

*Boshlang'ich qiymati $a$ bo'lgan miqdor har davrda $r$ ulushga (foizga)
ortsa, uning qiymati $y=a(1+r)^x$ formulasi bilan, kamaysa esa
$y=a(1-r)^x$ formulasi bilan ifodalanadi, bunda $x$ — o'tgan davrlar soni.*

<small>(A quantity starting at $a$ that grows by a fraction $r$ (a percent)
each period follows $y=a(1+r)^x$; if it shrinks by that fraction, it follows
$y=a(1-r)^x$, where $x$ is the number of periods elapsed.)</small>

**Nima so'ralmoqda tekshiruvi:** masala "necha yildan keyin" yoki "necha
davrdan keyin" deb so'raganda, bu son to'g'ridan-to'g'ri $x$ ga teng bo'ladi
— lekin masala "qancha o'sdi" yoki "farqi qancha" deb so'rasa, yakuniy
javobni boshlang'ich qiymatdan ayirish kerak bo'ladi. Har doim savolni
qayta o'qib, aynan nima so'ralayotganini aniqlang.

### Model Example (2-misol)

Shaharcha aholisi $200$ kishi bo'lib, har yili $5\%$ ga o'sadi. $4$ yildan
keyin aholi soni qancha bo'ladi?

**Yechish:** $5\% = 0.05$, demak o'sish koeffitsienti $1+0.05=1.05$.
Formula: $y=200\times1.05^x$. $x=4$ qo'yamiz: $y=200\times1.05^4 \approx
243.10$. Yaxlitlab, taxminan $243$ kishi.

**Javob:** $\approx 243$ kishi

### Your-Turn Example (O'zingiz bajaring)

Mashina narxi $\$15000$ bo'lib, har yili $12\%$ ga qadrsizlanadi (kamayadi).
$3$ yildan keyin narxi qancha bo'ladi? $\underline{\hspace{30mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv (ikkita keng tarqalgan xato):**

1. Foizni koeffitsientga aylantirishda xato qilish — $7\%$ ni $1.7$ deb olish
   ($0.07$ o'rniga, ya'ni $\div100$ qilishni unutish yoki noto'g'ri
   joylashtirish).
2. O'sish va kamayish formulasini aralashtirib yuborish — kamayuvchi miqdorga
   $(1+r)$ ni, yoki o'suvchi miqdorga $(1-r)$ ni qo'llash.

**To'g'ri qoida:** $7\%$ — bu $0.07$, shuning uchun koeffitsient $1.07$
($1.7$ emas). Va: miqdor ORTSA — $(1+r)$; miqdor KAMAYSA — $(1-r)$. Masalan,
$10000$ dan boshlanib yiliga $7\%$ ga o'sgan miqdor $2$ yildan keyin:
$10000\times1.07^2\approx11449$ — $10000\times1.7^2=28900$ EMAS.

---

## Concept 3 — Yarim Yemirilish Davri (Half-Life)

### Definition

*Ma'lum miqdorning aynan yarmigacha kamayishi uchun ketadigan doimiy vaqt
yarim yemirilish davri deb ataladi; agar bu davr $h$ ga teng bo'lsa, $t$
vaqtdan keyingi miqdor $y = a\left(\dfrac{1}{2}\right)^{t/h}$ formulasi
bilan topiladi, bunda $a$ — boshlang'ich miqdor.*

<small>(The fixed time it takes a quantity to drop to exactly half its value
is called the half-life. If that period is $h$, the amount after time $t$ is
$y=a(\frac12)^{t/h}$, where $a$ is the starting amount.)</small>

Bu — Concept 2'dagi kamayish formulasining maxsus holati, faqat bu safar
darajada $x$ emas, $\dfrac{t}{h}$ (nechta yarim davr o'tganini) yozamiz.

### Model Example (3-misol)

Radioaktiv modda $160$ gramm bo'lib, yarim yemirilish davri $4$ yil. $12$
yildan keyin necha gramm qoladi?

**Yechish:** Necha yarim davr o'tdi? $t/h = 12/4 = 3$. Formula:
$y=160\times\left(\frac12\right)^3 = 160\times\frac18 = 20$.

**Javob:** $20$ gramm

### Your-Turn Example (O'zingiz bajaring)

Dori miqdori $500$ mg bo'lib, yarim yemirilish davri $6$ soat. $18$ soatdan
keyin necha mg qoladi? $\underline{\hspace{25mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** har bir yarim davrda boshlang'ich miqdorning
yarmisini AYIRIB tashlash (qo'shish/ayirish — chiziqli fikrlash), ko'paytma
emas.

**To'g'ri qoida:** har bir yarim davrda QOLGAN miqdor yana yarmiga
KO'PAYTIRILADI (ko'paytirish — ko'rsatkichli fikrlash), umumiy miqdordan
emas. $240$ grammning $3$ yarim davridan keyingisi:
$240\times\left(\frac12\right)^3=30$ gramm — $240 - 3\times120=-120$ EMAS
(bu natija manfiy bo'lishi mumkin emasligi o'zi xato ekanini ko'rsatadi).

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Linear growth | Chiziqli o'sish |
| Exponential growth/decay | Ko'rsatkichli o'sish/kamayish |
| Growth factor | O'sish koeffitsienti |
| Common difference | Umumiy ayirma |
| Common ratio | Umumiy nisbat |
| Initial value | Boshlang'ich qiymat |
| Half-life | Yarim yemirilish davri |
| Rate (as a decimal) | Foiz ulushi (o'nli kasr ko'rinishida) |

## Notes for the problems file (Sets 1–7)

1. Identify linear vs. exponential from a table + state the rule (table test).
2. Build the growth equation from a word problem, evaluate.
3. Build the decay equation from a word problem, evaluate.
4. Mixed linear/exponential word problems — discriminate, then evaluate.
5. Half-life applications.
6. Spot the error — targeting the two documented misconceptions from the
   Common Mistake boxes above, plus the linear/exponential table-reading trap.
7. Bonus/Challenge — work backward: given two data points, find the rate $r$
   or the half-life $h$.
