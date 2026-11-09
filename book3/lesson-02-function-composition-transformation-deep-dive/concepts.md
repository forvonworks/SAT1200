# Book 3 — Lesson 2: Function Composition & Transformation — Deep Dive

**Source content file.** Book 3 is the 800+/hardest tier, the final book of the series.
This lesson builds directly on `book2/lesson-11-function-composition-transformation/concepts.md`
— re-read that file for the exact boundary. Book 2 L11 taught: composition evaluated at a
numeric point, the order-reversal trap ($f(g(x)) \ne g(f(x))$), vertical shift $f(x)+k$,
vertical reflection $-f(x)$, horizontal shift $f(x\pm h)$ with its counterintuitive sign
direction, and horizontal reflection $f(-x)$. **This lesson does not re-teach any of that.**

**Research grounding:** `research/15-question-bank-analysis.md` documents the real official
College Board Question Bank pipeline. Candidate Hard-tagged "Nonlinear functions" questions
were pulled and read directly (rendered to image, since the bank's PDF text layer drops all
embedded numbers — see `research/15` §4b). **Finding worth noting:** very few of the real
Hard "Nonlinear functions" questions are literal `f(g(x))`-notation composition problems —
the SAT tests the underlying *transformation reasoning* far more than the notation itself,
usually combined with another skill (optimization, table-reading, reconstructing an unknown
function). Two real official questions anchor Concepts 2 and 3 below; Concepts 1 and 4 use
original problems built to the same difficulty, since self-composition and stretch/compression
specifically weren't well-represented in the sampled Hard pool.

---

## Concept 1 — O'z-O'ziga Kompozitsiya va Ko'p Qatlamli Kompozitsiya: f(f(x))

### Definition

*Funksiyaning o'z natijasini yana o'ziga kirish qiymati sifatida qo'yish o'z-o'ziga
kompozitsiya deb ataladi va $f(f(x))$ ko'rinishida yoziladi. Uch yoki undan ortiq funksiya
ketma-ket qo'llanilsa, bu ko'p qatlamli kompozitsiya deb ataladi — baribir eng ichkaridan
boshlab, bosqichma-bosqich tashqariga qarab hisoblanadi.*

<small>(Applying a function to its own output is self-composition, $f(f(x))$. Three or
more functions chained the same way is nested composition — still evaluated strictly
inside-out, one layer at a time.)</small>

**Nega bu Book 2'dan qiyinroq:** $f(g(x))$ da ikkita turli funksiya bor — qaysi birinchi
ekanini chalkashtirish mumkin, lekin kamida ular boshqa-boshqa. $f(f(x))$ da esa **bir xil
qoidani ikki marta** qo'llash kerak, va har bir bosqichda butunlay yangi kirish qiymati bilan
ishlash kerak — birinchi $f(x)$ ning natijasi ikkinchi $f$ ning kirish qiymatiga aylanadi,
asl $x$ ga emas.

### Model Example (1-misol)

$f(x) = 2x+1$ berilgan. $f(f(2))$ ni toping.

**Yechish:** Avval ichkarisini hisoblaymiz: $f(2) = 2(2)+1 = 5$. Bu natija endi $f$ ning yangi
kirish qiymati: $f(5) = 2(5)+1 = 11$.

**Javob:** $f(f(2)) = 11$

*(Keng tarqalgan xato: $f(2)$ ni hisoblab, so'ngra uni $2$ ga qaytadan ko'paytirib yuborish —
ya'ni asl $x=2$ni ikkinchi marta ham ishlatish. To'g'ri yo'l: ikkinchi bosqichda kirish
qiymati endi $5$, $2$ emas.)*

### Your-Turn Example (O'zingiz bajaring)

$f(x) = 3x-1$ berilgan. $f(f(1)) = \underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** $f(f(x))$ ni $[f(x)]^2$ yoki $f(x)\times f(x)$ deb o'ylash — ya'ni
kompozitsiyani ko'paytirish bilan aralashtirish.

**To'g'ri:** $f(f(x))$ — bu $f$ ni ikki marta **ketma-ket qo'llash**, ko'paytirish emas.
Model misolda $f(2)=5$ edi; $f(f(2))$ bu $f(5)$, $f(2)\times f(2) = 25$ emas, $11$ bo'ladi.
Ikkalasi butunlay boshqa amal va boshqa javob beradi.

---

## Concept 2 — Transformatsiya Boshqa Ko'nikma Bilan Birga: Siljigan Funksiyaning Maksimumi

### Definition

*Agar $g(t) = f(t) + c$ bo'lsa va $f$ kvadrat funksiya bo'lsa, $g$ ning maksimal (yoki
minimal) qiymati $f$ ning maksimal qiymatiga $c$ ni qo'shish orqali topiladi — chunki
vertikal siljish grafikning balandligini o'zgartiradi, lekin uning qayerda maksimumga
yetishini (ya'ni $t$ ning qiymatini) o'zgartirmaydi.*

<small>(If $g(t)=f(t)+c$ and $f$ is quadratic, $g$'s max/min is $f$'s max/min plus $c$ —
a vertical shift changes the height of the peak, not where it occurs.)</small>

**Bu yerda qiyinchilik:** Book 2 L11 faqat $f(x)+k$ ni **bitta nuqtada baholash**ni o'rgatgan
edi. Bu yerda transformatsiya **optimallashtirish** (kvadrat to'ldirish orqali maksimum/
minimum topish) bilan birga keladi — ikkita ko'nikmani ketma-ket, bitta masalada qo'llash
kerak.

### Model Example (2-misol) — haqiqiy College Board savoli asosida

$f(t) = 55t - 2t^2$ berilgan. $g(t) = f(t)+3$. $g(t)$ ning maksimal qiymatini toping.

**Yechish:** Avval $f(t)$ ning maksimumini topamiz — kvadrat to'ldirish yoki uchi
formulasidan foydalanib: $f(t) = -2t^2+55t$ uchun uchi $t = \dfrac{55}{2(2)} = \dfrac{55}{4}$
da joylashgan. Bu nuqtada: $f\left(\dfrac{55}{4}\right) = 55\left(\dfrac{55}{4}\right) -
2\left(\dfrac{55}{4}\right)^2 = \dfrac{3025}{4} - \dfrac{3025}{8} = \dfrac{3025}{8}$.
$g(t) = f(t)+3$ bo'lgani uchun, $g$ ning maksimumi shunchaki $f$ ning maksimumiga $3$
qo'shilgani: $\dfrac{3025}{8}+3 = \dfrac{3049}{8} = 381.125$.

**Javob:** $g(t)$ ning maksimal qiymati $\dfrac{3049}{8} = 381.125$

*(E'tibor bering: $g(t)$ ning o'zini to'liq ochib, qaytadan kvadrat to'ldirish shart emas —
vertikal siljish qoidasini bilgan holda, faqat $f$ ning maksimumini topib, ustiga $c$ ni
qo'shish yetarli. Bu vaqtni tejaydigan "speed technique" — Lesson 4 bilan bog'liq.)*

### Your-Turn Example (O'zingiz bajaring)

$f(x) = 30x - x^2$ berilgan. $g(x) = f(x) - 5$. $g(x)$ ning maksimal qiymatini toping:
$\underline{\hspace{25mm}}$

---

## Concept 3 — Jadvaldan Siljigan Funksiyani Tiklash

### Definition

*Agar jadvalda $y = f(x) + c$ ning qiymatlari berilgan bo'lsa (asl $f(x)$ emas), avval
siljishni hisobga olib $f(x)$ ning qoidasini (uchi shakli orqali) tiklash, so'ngra kerakli
nuqtada $f$ ni baholash kerak — bu Book 2 L11'dagi "berilgan tenglamani baholash"dan farqli
o'laroq, **teskari yo'nalishda** ishlaydigan ko'nikma.*

<small>(When a table gives values of a SHIFTED function $y=f(x)+c$, reconstruct $f(x)$'s
rule first via vertex form, then evaluate $f$ wherever asked — the reverse direction from
Book 2 L11's "evaluate the given equation.")</small>

**Bu nega qiyin:** Bu yerda tenglama berilmagan — faqat uchta $(x,y)$ juftlik. Talaba avval
$y=f(x)+c$ ekanini **tushunishi**, keyin uchi (vertex) qayerdaligini jadvaldagi simmetriyadan
topishi, so'ngra siljishni **orqaga qaytarib** asl $f(x)$ ni tiklashi kerak.

### Model Example (3-misol) — haqiqiy College Board savoli asosida

Jadvalda $x$ va $y=f(x)+4$ ning uchta qiymati berilgan, $f$ — kvadrat funksiya:

| $x$ | $21$ | $23$ | $25$ |
|---|---|---|---|
| $y$ | $-8$ | $8$ | $-8$ |

$y=f(x)$ grafigining $y$-kesishish nuqtasining $y$-koordinatasini toping.

**Yechish:** $x=21$ va $x=25$ da $y$ bir xil ($-8$) — demak uchi bu ikkisining o'rtasida,
ya'ni $x=23$ da. $y=f(x)+4 = a(x-23)^2+(k+4)$ ko'rinishida yoziladi, bunda $k+4$ — uchidagi
maksimal $y$ qiymati, ya'ni $k+4=8$. $x=25$ ni qo'yamiz: $-8 = a(25-23)^2+8$, ya'ni
$-8=4a+8$, bundan $4a=-16$, $a=-4$. Demak $k=8-4=4$, va asl funksiya: $f(x)=-4(x-23)^2+4$.
$y$-kesishish nuqtasi $x=0$ da: $f(0) = -4(0-23)^2+4 = -4(529)+4 = -2116+4=-2112$.

**Javob:** $y$-kesishish nuqtasining $y$-koordinatasi $-2112$

### Your-Turn Example (O'zingiz bajaring)

Jadvalda $x$ va $y=f(x)+3$ ning uchta qiymati berilgan, $f$ — kvadrat funksiya:

| $x$ | $3$ | $5$ | $7$ |
|---|---|---|---|
| $y$ | $15$ | $23$ | $15$ |

$y=f(x)$ grafigining $y$-kesishish nuqtasining $y$-koordinatasini toping:
$\underline{\hspace{25mm}}$

### Common Mistake Box

**Noto'g'ri:** Jadvaldagi $y$ qiymatlaridan to'g'ridan-to'g'ri $f(0)$ ni topish — ya'ni
siljishni ($+4$ yoki $+3$) hisobga olmaslik, go'yoki jadvaldagi $y$ allaqachon $f(x)$ ning
o'zi ekanidek ishlash.

**To'g'ri:** Jadvaldagi $y$ — bu $f(x)$ emas, balki $f(x)+c$. Avval $a$ va uchi $(h,k)$ ni
**siljishni hisobga olib** topish kerak (uchidagi $y$ qiymati $k$ emas, $k+c$ ekanini
unutmang), so'ngra $f(x)=a(x-h)^2+k$ formulasidan foydalanib so'ralgan nuqtani hisoblash
kerak — hech qachon siljigan $y=f(x)+c$ formulasining o'zini javob deb bermang.

---

## Concept 4 — Cho'zish va Siqish: $a \cdot f(x)$ va $f(bx)$

### Definition

*Funksiyaning natijasi songa ko'paytirilsa ($a\cdot f(x)$), grafik vertikal cho'ziladi
($|a|>1$ bo'lsa) yoki siqiladi ($0<|a|<1$ bo'lsa). Funksiyaning kirish qiymati ($x$)
songa ko'paytirilsa ($f(bx)$), grafik gorizontal siqiladi ($|b|>1$ bo'lsa) yoki cho'ziladi
($0<|b|<1$ bo'lsa) — bu Book 2 L11'da o'rgatilmagan, siljish/aks ettirishdan butunlay
boshqa transformatsiya turi.*

<small>($a\cdot f(x)$ stretches/compresses the graph VERTICALLY — scaling the output.
$f(bx)$ stretches/compresses it HORIZONTALLY — scaling the input, which (like the
horizontal-shift sign trap) behaves "backwards": multiplying $x$ by a number bigger than 1
actually *compresses* the graph, it doesn't stretch it.)</small>

**Taqqoslash uchun diqqat:** $a\cdot f(x)$ va $f(bx)$ bir xil songa qarasa ham, mutlaqo
boshqa natija beradi, chunki biri natijani, ikkinchisi kirish qiymatini o'zgartiradi.

### Model Example (4-misol)

$f(x) = x^2$ berilgan. $3f(2)$ va $f(3\times2)=f(6)$ ni toping va taqqoslang.

**Yechish:** $3f(2) = 3(2^2) = 3(4) = 12$ — bu $f(2)$ ning natijasini $3$ ga ko'paytirish
(vertikal cho'zish). $f(6) = 6^2 = 36$ — bu kirish qiymatini avval $3$ ga ko'paytirib, so'ngra
funksiyaga qo'yish (gorizontal siqish). Ikkisi butunlay boshqa javob: $12 \ne 36$.

**Javob:** $3f(2)=12$; $f(6)=36$

*(Nega bunchalik katta farq: gorizontal siqishda $x$ ning o'zi kattalashadi, va $f(x)=x^2$
tez o'sadigani uchun, kirish qiymatini kattalashtirish natijani ko'paytirishdan ko'ra ancha
kuchliroq ta'sir qiladi.)*

### Your-Turn Example (O'zingiz bajaring)

$f(x) = x^2-1$ berilgan. $\dfrac12 f(4) = \underline{\hspace{15mm}}$,
$f\left(\dfrac12 \times 4\right) = \underline{\hspace{15mm}}$

### Common Mistake Box

**Noto'g'ri:** $f(bx)$ ni $b\cdot f(x)$ bilan bir xil deb hisoblash — ya'ni kirish qiymatini
o'zgartirishni natijani o'zgartirish bilan aralashtirish (xuddi Book 2 L11'dagi gorizontal/
vertikal siljishni aralashtirish xatosining cho'zish-siqish versiyasi).

**To'g'ri:** $a\cdot f(x)$ — natijani ko'paytiradi (vertikal). $f(bx)$ — kirish qiymatini
ko'paytirib, so'ngra funksiyaga qo'yadi (gorizontal, va samarasi songa teskari — $b$ katta
bo'lsa, grafik siqiladi, cho'zilmaydi). Model misoldagi kabi, bu ikkisi deyarli har doim
boshqa-boshqa son beradi.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Self-composition | O'z-o'ziga kompozitsiya |
| Nested composition | Ko'p qatlamli kompozitsiya |
| Vertex form | Uchi shakli |
| Reconstruct (a function) | Tiklash |
| Vertical stretch/compression | Vertikal cho'zish/siqish |
| Horizontal stretch/compression | Gorizontal cho'zish/siqish |
| Scale factor | Masshtab koeffitsienti |

## Notes for the problems file (Sets 1–8)

1. Self-composition $f(f(x))$ and triple composition — evaluate at a point.
2. Nested composition with two/three distinct functions.
3. Transformation + optimization combined (one real CB-grounded item, rest original).
4. Reconstruct $f$ from a shifted table, then evaluate — one real CB-grounded item
   (the exact Model Example question, restated), rest original with different numbers.
5. Vertical vs. horizontal stretch/compression — contrast pairs.
6. Mixed: composition THEN transformation applied to the composed result.
7. Spot the error — self-composition-as-squaring, forgetting to un-shift a
   reconstructed table answer, and $f(bx)$ vs. $b\cdot f(x)$ confusion.
8. Bonus/challenge — multi-layer composition combined with a transformation twist.
