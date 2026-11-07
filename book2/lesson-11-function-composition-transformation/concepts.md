# Book 2 — Lesson 11: Function Notation, Composition & Transformation (Intro-Intermediate)

**Source content file.** Structure follows `research/14-design-spec.md` §10 and
mirrors `book1/lesson-01-basic-arithmetic-order-of-operations/concepts.md`
exactly: Definition → Model example → Your-turn → conditional Common Mistake
→ shared Vocabulary.

**Builds directly on:** Book 1 Lesson 8 (f(x) as another name for $y$; $f(a)$
means "substitute $x=a$") and Book 2 Lesson 3 (linear functions in depth). This
lesson does **not** re-teach the basic f(x) bridge — it assumes that fluency
and moves straight into two genuinely new ideas: composing two functions, and
transforming a function's graph. Per `research/02-topic-difficulty-taxonomy.md`,
composition/transformation items are concentrated in the SAT's harder tier
(cited at roughly 7-10% of questions, with nested composition as "the
recurring trap format") — this is Book 2 depth, past what Book 1 touched, and
is explicitly a "study a notch above the ceiling" topic that sets up Book 3's
deeper composition/transformation work. Kept intro-intermediate on purpose:
this lesson builds real intuition on the core moves, not every possible
transformation combination — Book 3 goes further.

---

## Concept 1 — Funksiyalar Kompozitsiyasi: f(g(x))

### Definition

*Bir funksiyaning natijasini ikkinchi funksiyaga kirish qiymati sifatida
qo'yish funksiyalar kompozitsiyasi deb ataladi va $f(g(x))$ ko'rinishida
yoziladi. Bu "avval $g$ ni hisobla, so'ngra natijani $f$ ga qo'y" degani —
har doim ichkaridan tashqariga qarab hisoblanadi.*

<small>(Composition means plugging one function's output in as the other
function's input, written $f(g(x))$. Always evaluate inside-out: compute the
inner function first, then feed that result into the outer one.)</small>

**E'tibor bering:** $f(g(x))$ va $g(f(x))$ odatda **bir xil emas** —
tartib muhim. Bu eng ko'p uchraydigan xato: ikkalasini aralashtirib yuborish
(`research/04-common-student-mistakes.md`'da "Reversing the order of
composition" deb aniq qayd etilgan).

### Model Example (1-misol)

$f(x)=3x-2$, $g(x)=x^2+1$ berilgan. $f(g(2))$ ni toping.

**Yechish:** Ichkaridan boshlaymiz: $g(2) = 2^2+1 = 5$. Endi bu natijani
$f$ ga qo'yamiz: $f(5) = 3(5)-2 = 13$.

**Javob:** $f(g(2)) = 13$

*(Taqqoslash uchun: $g(f(2)) = g(3\times2-2) = g(4) = 4^2+1 = 17$ — boshqa
javob chiqdi. $f(g(x)) \ne g(f(x))$ ekanini bu aniq ko'rsatadi.)*

### Your-Turn Example (O'zingiz bajaring)

$f(x)=x^2+1$, $g(x)=2x-1$ berilgan. $f(g(3)) = \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** $f(g(x))$ so'ralganda, $g(f(x))$ ni hisoblash — ya'ni tartibni
teskari qilib yuborish.

**To'g'ri:** $f(g(x))$ yozuvida **eng yaqin harf** ($g$) birinchi hisoblanadi,
chunki u $x$ ga eng yaqin turibdi — xuddi qavslarni ichkaridan ochgandek.
Model misoldagi kabi, $f(g(2))=13$ va $g(f(2))=17$ — ular har doim ham teng
emas, shuning uchun savolda qaysi tartib so'ralganini diqqat bilan o'qing.

---

## Concept 2 — Vertikal Siljish va Aks Ettirish: f(x)+k va −f(x)

### Definition

*Funksiya ifodasining o'zi emas, balki uning natijasiga son qo'shilsa yoki
natija manfiylansa, grafik vertikal (tepaga/pastga yoki x-o'qiga nisbatan)
siljiydi: $f(x)+k$ grafikni $k$ birlikka tepaga (yoki $k$ manfiy bo'lsa
pastga) ko'taradi; $-f(x)$ esa grafikni x-o'qiga nisbatan aks ettiradi.*

<small>($f(x)+k$ shifts the graph up/down by $k$ — the input is untouched,
only the output changes. $-f(x)$ flips the graph over the x-axis.)</small>

### Model Example (2-misol)

$f(x) = x^2-4$ berilgan. $f(3)+5$ va $-f(3)$ ni toping.

**Yechish:** Avval $f(3) = 3^2-4 = 5$. Endi: $f(3)+5 = 5+5 = 10$ — bu
oddiygina $f(3)$ ning natijasiga $5$ qo'shish. $-f(3) = -5$ — bu $f(3)$ ning
natijasini manfiylash.

**Javob:** $f(3)+5=10$; $-f(3)=-5$

### Your-Turn Example (O'zingiz bajaring)

$f(x)=x^2-4$ berilgan. $f(1)-3 = \underline{\hspace{15mm}}$,
$-f(2) = \underline{\hspace{15mm}}$

---

## Concept 3 — Gorizontal Siljish va Aks Ettirish: f(x+k) va f(−x)

### Definition

*Funksiyaning natijasiga emas, balki $x$ ning o'ziga son qo'shilsa yoki $x$
manfiylansa, grafik gorizontal (chapga/o'ngga yoki y-o'qiga nisbatan)
siljiydi: $f(x-h)$ grafikni $h$ birlikka **o'ngga** (ishorasiga teskari
yo'nalishda!) suradi; $f(-x)$ esa grafikni y-o'qiga nisbatan aks ettiradi.*

<small>($f(x-h)$ shifts the graph RIGHT by $h$ — despite the minus sign.
$f(x+h)$ shifts LEFT. This is the single most counterintuitive rule in this
lesson: the sign on the input does the OPPOSITE of what it looks like it
should do.)</small>

**Nega teskari ishlaydi — mantiqiy tushuntirish:** $f(x-2)$ ning $x=2$
dagi qiymati — bu aslida $f(0)$ ning qiymati (chunki $2-2=0$). Ya'ni, $f$
asliy $x=0$ da bergan natijani endi $x=2$ da ko'ryapmiz — demak, grafik
**o'ngga** siljigan, garchi ifodada **minus** bo'lsa ham.

### Model Example (3-misol)

$f(x) = x^2+2x$ berilgan. $f(x-2)$ ni $x=5$ da hisoblang va $f(-x)$ ni
$x=3$ da hisoblang.

**Yechish:** $f(x-2)$ da $x=5$ qo'yilganda, avval $x-2=5-2=3$ hisoblanadi,
so'ngra $f(3)=3^2+2(3)=9+6=15$. Boshqa tomondan, $f(-x)$ da $x=3$ qo'yilsa,
avval $-x=-3$ bo'ladi, so'ngra $f(-3)=(-3)^2+2(-3)=9-6=3$.

**Javob:** $f(x-2)$ at $x=5$ is $15$; $f(-x)$ at $x=3$ is $3$

*(Tekshiruv: $f(x-2)$ ning $x=2$ dagi qiymati $f(0)=0$ ga teng bo'lishi
kerak — chunki grafik $2$ birlikka o'ngga surilgan. Haqiqatan ham:
$f(2-2)=f(0)=0^2+2(0)=0$. To'g'ri.)*

### Your-Turn Example (O'zingiz bajaring)

$f(x)=x^2+2x$ berilgan. $f(x+1)$ ni $x=4$ da hisoblang:
$\underline{\hspace{15mm}}$. $f(-x)$ ni $x=4$ da hisoblang:
$\underline{\hspace{15mm}}$

### Common Mistake Box

**Noto'g'ri:** $f(x-h)$ grafikni **chapga** suradi deb o'ylash, chunki
ifodada minus bor (`research/04`da "Confusing $f(x+a)$ ... with $f(x)+a$"
aniq hujjatlashtirilgan konseptual chalkashlik bilan bevosita bog'liq).

**To'g'ri:** $f(x-h)$ — **o'ngga** $h$ birlikka; $f(x+h)$ — **chapga** $h$
birlikka. Ishoraning yo'nalishi doim teskari. Buni eslab qolish uchun: "ichida
qo'shish/ayirish — $x$ ga ta'sir qiladi va NATIJA teskari tomonga siljiydi";
"tashqarida qo'shish/ayirish — natijaga ta'sir qiladi va ko'rinib turgan
yo'nalishga siljiydi" (Concept 2 bilan solishtiring).

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Function composition | Funksiyalar kompozitsiyasi |
| Inner function / outer function | Ichki funksiya / tashqi funksiya |
| Vertical shift | Vertikal siljish |
| Horizontal shift | Gorizontal siljish |
| Reflection (over x-axis / y-axis) | Aks ettirish (x-o'qiga / y-o'qiga nisbatan) |
| Transformation | Almashtirish / Transformatsiya |

## Notes for the problems file (Sets 1–7)

1. Evaluate composition at a numeric point.
2. Build/simplify composition algebraically (symbolic $f(g(x))$).
3. Vertical transformation — evaluate, identify shift amount.
4. Horizontal transformation — evaluate, including the sign-direction trap.
5. Mixed — composition + transformation together.
6. Spot the error — targets composition-order reversal, $f(x)+k$ vs. $f(x+k)$
   confusion, and the horizontal-shift sign trap (3 of `research/04`'s
   documented errors, each given its own item).
7. Bonus/challenge — nested composition and combined transformation+composition.
