# Book 2 — Lesson 14: Percentages in Context

**Source content file**, paired with `problems.md`. This lesson assumes Book 1
Lesson 3 (Decimals & Percent Conversion) is already solid — converting a
percent to a decimal or fraction is prior knowledge here, not re-taught.
Book 2's job is to apply that conversion skill to real percent-change
situations, at the rigor level the actual SAT (and sometimes a notch beyond
it) demands.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` lists
"Percentages in context (percent change, percent of, successive percent
changes)" directly under the Problem-Solving & Data Analysis domain, flagging
it explicitly as a **recurring error zone** — and separately names successive/
compound percent-change chains as an error that "correlates with score band"
all the way up to the 800-level tier: lower/mid scorers add percentages,
higher scorers compound them correctly. `research/04-common-student-mistakes.md`
names three specific, documented percent errors this lesson targets directly:
dividing by the *new* value instead of the *original* value when computing
percent change; forgetting to convert a percent to a decimal before
calculating; and the additive-instead-of-multiplicative error on successive
changes. Given how consistently this exact family of mistakes is named at
every tier, Concept 3 (successive changes) gets real dedicated weight, not a
quick mention.

---

## Concept 1 — Percent Change (Foiz O'zgarishi)

### Definition

*Bir miqdorning dastlabki — ya'ni asl — qiymatidan qancha foizga ortishi yoki
kamayishini ko'rsatuvchi nisbat foiz o'zgarishi deb ataladi. Foiz o'zgarishi
har doim **asl qiymatga** nisbatan hisoblanadi, yangi qiymatga nisbatan emas —
bu qoidaning buzilishi eng ko'p uchraydigan xatolardan biridir.*

<small>(The ratio showing how much a quantity has increased or decreased from
its starting — original — value is called percent change. Percent change is
always calculated relative to the **original** value, never the new value —
breaking this rule is one of the most common errors.)</small>

$$\text{Foiz o'zgarishi} = \frac{\text{Yangi qiymat} - \text{Asl qiymat}}{\text{Asl qiymat}} \times 100\%$$

Natija **musbat** bo'lsa — foiz oshishi (percent increase); natija **manfiy**
bo'lsa — foiz kamayishi (percent decrease).

**Doim So'ralayotgan Narsani Tekshiring:** savol "necha foizga oshdi/kamaydi"
deb so'raganda, javob — foiz o'zgarishining o'zi, yangi qiymat ham, farq
(differences, dollar/son ko'rinishida) ham emas. $40$ dan $52$ ga o'sish —
javob $12$ emas, $30\%$.

### Model Example (1-misol)

Bir ko'ylakning narxi $\$40$ dan $\$52$ ga oshdi. Necha foizga oshganini
toping.

**Yechish:** Avval farqni topamiz: $52-40=12$. Bu farqni **asl qiymatga**
($40$ ga) bo'lamiz, yangi qiymatga ($52$ ga) emas: $\frac{12}{40}=0.30$.
O'nli kasrni foizga aylantiramiz: $0.30=30\%$.

**Javob:** $30\%$ ga oshdi.

### Your-Turn Example (O'zingiz bajaring)

Bir shahar aholisi $2{,}500$ kishidan $2{,}125$ kishiga kamaydi. Necha
foizga kamaygan? $\underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** Farqni **yangi** qiymatga bo'lish. Misolda:
$\frac{12}{52}\approx0.231=23.1\%$ — bu noto'g'ri javob, chunki o'zgarish
har doim *nimadan boshlangan* bo'lsa, o'shanga nisbatan o'lchanadi.

**To'g'ri qoida:** Maxrajda doim **asl (dastlabki) qiymat** turadi — savolda
qaysi qiymat oldin berilgan bo'lsa, o'sha maxrajga tushadi.

*(Research basis: dividing by the new value instead of the original value is
named directly in `research/04-common-student-mistakes.md` as "one of the
most common percent errors cited.")*

---

## Concept 2 — The Multiplier Method (Ko'paytuvchi Usuli)

### Definition

*Foiz o'zgarishini bitta amalda qo'llash uchun asl qiymatni $(1+r)$ yoki
$(1-r)$ ko'paytuvchisiga ko'paytirish usuli ko'paytuvchi usuli deb ataladi,
bu yerda $r$ — foizning o'nli kasr ko'rinishi. Oshish uchun $(1+r)$,
kamayish uchun $(1-r)$ qo'llaniladi.*

<small>(Applying a percent change in a single step by multiplying the
original value by $(1+r)$ for an increase or $(1-r)$ for a decrease, where
$r$ is the percent written as a decimal, is called the multiplier method.)</small>

$$\text{Yangi qiymat} = \text{Asl qiymat} \times (1 \pm r)$$

Masalan, $20\%$ oshish — ko'paytuvchi $1.20$; $20\%$ kamayish — ko'paytuvchi
$0.80$. Bu usul Konsept 1 formulasidan tezroq, chunki yangi qiymatni to'g'ridan
to'g'ri beradi — oldin farqni topib, keyin asl qiymatga qo'shish/ayirish shart
emas.

**Oldinga bog'lanish:** bu xuddi shu $(1\pm r)^x$ tuzilishi Book 2 Lesson 8'da
(Exponential Functions) takrorlanadi — u yerda bir martalik emas, har bir
davrda qayta-qayta qo'llaniladigan o'sish/kamayish modeli sifatida chiqadi.
Shu ko'paytuvchi mantig'ini hozir mustahkamlash o'sha darsni osonlashtiradi.

### Model Example (2-misol)

$\$150$ ga $20\%$ qo'shilsa, yangi qiymat nechaga teng bo'ladi?

**Yechish:** $20\%=0.20$, demak ko'paytuvchi $1+0.20=1.20$.
$150 \times 1.20 = 180$.

**Javob:** $\$180$

### Your-Turn Example (O'zingiz bajaring)

$\$200$ dan $15\%$ ayirilsa (kamaytirilsa), yangi qiymat nechaga teng?
$\underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** Foizni o'nli kasrga aylantirmasdan to'g'ridan-to'g'ri
sonning o'ziga ko'paytirish — masalan $25\%$ ni $0.25$ emas, $25$ deb olish,
natijada javob $100$ marta katta chiqadi.

**To'g'ri qoida:** Ko'paytuvchini yozishdan oldin har doim foizni $100$ ga
bo'lib, o'nli kasrga aylantiring: $25\% \rightarrow 0.25 \rightarrow$
ko'paytuvchi $1.25$ (oshish) yoki $0.75$ (kamayish).

*(Research basis: "forgetting to convert a percent to a decimal before using
it in a calculation... listed repeatedly as one of the single most common
'silly' SAT percent errors" — `research/04-common-student-mistakes.md`.)*

---

## Concept 3 — Successive Percent Changes (Ketma-ket Foiz O'zgarishi)

### Definition

*Bir miqdorga ketma-ket ikki (yoki undan ortiq) marta foiz o'zgarishi
qo'llanilganda, har bir keyingi o'zgarish **oldingi natijaga** nisbatan
hisoblanadi, **asl qiymatga** emas. Shu sababli foiz o'zgarishlarini
to'g'ridan-to'g'ri qo'shish yoki ayirish — umuman noto'g'ri natija beradi.*

<small>(When a quantity undergoes two or more percent changes one after
another, each later change is calculated relative to the **result of the
previous step**, not the original value. This is exactly why adding or
subtracting the percentages directly gives the wrong answer — almost always.)</small>

**Eng muhim ko'rsatma sifatida — bu butun kontseptning yuragi:** $r_1\%$
oshish, keyin $r_2\%$ kamayish ketma-ket qo'llanilsa, natija $r_1\% - r_2\%$
emas — ko'paytuvchilarni ketma-ket ko'paytirish kerak:

$$\text{Yakuniy qiymat} = \text{Asl qiymat} \times (1+r_1) \times (1-r_2)$$

### Model Example (3-misol) — The Classic Trap

Bir mahsulotning narxi avval $20\%$ ga oshdi, keyin yangi narxdan $10\%$
chegirma qilindi. Asl narx $\$500$ bo'lsa, bu ikki o'zgarishdan keyingi
**sof (net) foiz o'zgarishi** nechaga teng? ($20\%-10\%=10\%$ oshish deb
**javob bermang** — buni isbotlab ko'rsating.)

**Yechish:** Ko'paytuvchi usulini ketma-ket qo'llaymiz. Birinchi qadam —
$20\%$ oshish: ko'paytuvchi $1.20$. Ikkinchi qadam — bu yangi (oshgan)
qiymatdan $10\%$ chegirma: ko'paytuvchi $0.90$. Ikki ko'paytuvchini
ko'paytiramiz: $1.20 \times 0.90 = 1.08$.

Bu $1.08$ ko'paytuvchi — asl qiymatdan $8\%$ ko'proq degani, $10\%$ emas.
Tekshiramiz: $500 \times 1.08 = 540$. Agar $20\%-10\%=10\%$ deb hisoblasak,
$500\times1.10=550$ chiqardi — bu **noto'g'ri**, chunki $10\%$ chegirma
asl $\$500$ ga emas, oshgan $\$600$ ga qo'llanilgan, va $10\%$ of $600$
($=60$) $10\%$ of $500$ dan ($=50$) katta.

**Javob:** Sof o'zgarish $+8\%$ (yakuniy narx $\$540$), $+10\%$ emas.

*(Bu yerda yana ham ko'rsatkichliroq misol: agar narx $20\%$ ga oshib,
so'ngra $20\%$ ga (bir xil foizga) kamaysa — ko'pchilik "bir-birini
yo'q qiladi, $0\%$ net o'zgarish" deb o'ylaydi. Haqiqatda: $1.20\times0.80=0.96$,
ya'ni asl qiymatning $96\%$i — $4\%$ kamayish, $0\%$ emas! Buning sababi
oddiy: $20\%$ kamayish endi kattaroq (oshgan) qiymatdan olinadi, shuning
uchun dollar/so'm miqdorida ko'proq "yo'qotadi" nisbatan ko'proq, va ikkala
o'zgarish teng foizda bo'lsa ham, natija hech qachon asl qiymatga teng
bo'lmaydi — faqat foiz $0\%$ bo'lgandagina teng bo'ladi.)*

### Your-Turn Example (O'zingiz bajaring)

Bir mahsulot narxi avval $20\%$ ga kamaydi, keyin yangi (kamaygan)
narxdan $15\%$ ga yana kamaydi. Agar asl narx $\$400$ bo'lsa, yakuniy narxni
va sof foiz o'zgarishini toping. $\underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** Ikki foiz o'zgarishini to'g'ridan-to'g'ri qo'shish
yoki ayirish — masalan "narx $30\%$ oshdi, keyin $20\%$ kamaydi, demak sof
o'zgarish $30\%-20\%=10\%$ oshish."

**To'g'ri qoida:** Har bir qadam uchun alohida ko'paytuvchi yozib, ularni
ketma-ket ko'paytiring: $(1+0.30)\times(1-0.20)=1.30\times0.80=1.04$ — sof
o'zgarish atigi $+4\%$, $+10\%$ emas (Set 6'da bu xato batafsil ko'riladi).

*(Research basis: "the additive-instead-of-multiplicative error on
successive percent changes" is named across the fundamentals, core, and
advanced-tier sources in `research/02-topic-difficulty-taxonomy.md` as
arguably the single most persistent percent-related pain point in the
entire series — not a one-lesson quirk, but worth permanent vigilance.)*

### Vocabulary

| English | O'zbekcha |
|---|---|
| Percent change | Foiz o'zgarishi |
| Percent increase | Foiz oshishi |
| Percent decrease | Foiz kamayishi |
| Original value | Asl qiymat |
| New value | Yangi qiymat |
| Multiplier method | Ko'paytuvchi usuli |
| Successive percent change | Ketma-ket foiz o'zgarishi |
| Net change | Sof o'zgarish |

---

## Notes for the problems file (Sets 1–7)

1. Basic percent change — pure drill, find % increase/decrease from old/new.
2. Multiplier method — single-step, find new value from old + % change.
3. Successive changes, **same** % up then down (or vice versa) — reinforces
   the classic trap's generality.
4. Successive changes, **different** %s, including same-% compounded twice.
5. Mixed word problems — discount+tax, population, salary, markup/markdown,
   compound interest context.
6. Spot the error — each targets the additive/subtractive trap directly.
7. Bonus/challenge — three successive changes, and working backward from a
   final value to find the original (reverse-multiplier problems).
