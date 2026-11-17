# Book 3 — Lesson 1: Multi-Step & Disguised Word Problems (Challenge)

**Source content file**, paired with `problems.md`. Opens Book 3 — the 800+ tier, the final
book of the series. Book 3 does **not** introduce new topics: research confirms calculus,
matrices, complex numbers, formal trig identities, and the unit circle are all out of SAT
scope (`research/02-topic-difficulty-taxonomy.md`). The single most consistent finding
across every source checked is that top-tier difficulty comes from **unfamiliar framing of
standard content, not new content** — and that most points lost at the top of the score
range come from *setup* errors (solving for the wrong quantity, missing the real structure
under a costume of unfamiliar notation), not computation errors.

**Research grounding:** every Model Example and Your-Turn in this lesson is built directly
from a real, official, Hard-tagged College Board SAT Math question — rendered from the
actual Question Bank PDF in `Materials/` and read page-by-page (see
`research/15-question-bank-analysis.md` for the extraction method), not invented. The
numbers, structure, and even the wrong-answer traps are real test material. This is the
hardest tier the real SAT gives — treat it that way.

**A note on register:** this book assumes Book 1 and Book 2's mechanics are already
automatic. The job here isn't re-explaining how to factor or complete the square — it's
training *pattern recognition under time pressure*. Read each concept as a coach pointing
out "this is the move," not a teacher re-deriving a rule from scratch.

---

## Concept 1 — Kvadrat funksiya niqob ostida (The Parabola Hiding Under a Word Problem)

### Ta'rif

*Agar biror masalada "eng katta/eng kichik qiymat", "maksimal balandlik" yoki "bir xil
qiymatga ikki marta erishish" kabi so'zlar uchrasa va yashirin tuzilma kvadrat funksiya
bo'lsa, to'liq tenglamani qurishdan oldin **parabolaning simmetriyasi**dan foydalanish
kerakligini tekshiring — bu ko'pincha to'liq hisoblashdan 3-4 baravar tezroq yo'l.*

<small>(If a problem mentions "maximum/minimum value," "maximum height," or "reaching the
same value twice," and the hidden structure is a quadratic function, check whether the
**parabola's symmetry** gives a shortcut before building the full equation — this is often
3-4x faster than the full computation.)</small>

**The key fact:** a parabola is symmetric about its vertex. If you know the vertex's
$x$-coordinate (or time-coordinate) and one other point, you automatically know the
*mirror* point — no need to ever find $a$, $b$, or $c$.

### Model Example (1-misol) — real SAT Hard question

Kvadrat funksiya snaryadning balandligini (metrda) uchirilgandan keyingi vaqt (soniyada)
funksiyasi sifatida modellaydi. Model snaryad yerdan $7$ metr balandlikda uchirilgan va
uchirilgandan $3$ soniya o'tgach $51{,}1$ metr maksimal balandlikka yetgan, deb taxmin
qiladi. Model snaryad $7$ metr balandlikka necha soniyadan keyin qaytib tushadi, deb
taxmin qiladi?

**Sekin yo'l (ko'rsatish uchun, lekin BU yo'lni tanlamang):** $f(x)=a(x-3)^2+51{,}1$ qurib,
$f(0)=7$ dan $a=-4{,}9$ topib, so'ng $f(x)=7$ tenglamasini yechish — to'g'ri, lekin $4$-$5$
qadam va $30$+ soniya vaqt talab qiladi.

**Tez yo'l — simmetriyadan foydalaning:** Parabolaning uchi (maksimal nuqta) $x=3$ da.
Boshlang'ich balandlik ($7$ metr) uchirilishdan $3$ soniya oldin (ya'ni $x=0$ da) sodir
bo'lgan — bu uchidan $3$ soniya **oldin**. Parabola uchiga nisbatan simmetrik bo'lgani
uchun, xuddi shu $7$ metr balandlikka uchidan $3$ soniya **keyin** ham erishiladi:
$3+3=6$.

**Javob:** $6$ soniya

*(Diqqat: bu yerda $a$, $b$ yoki to'liq tenglama — umuman kerak emas edi. Faqat ikkita
narsa kerak edi: uchining joylashuvi va bitta ma'lum nuqtaning undan qancha uzoqligi.)*

### Your-Turn Example (O'zingiz bajaring) — real SAT Hard question, table-based variant

Jadvalda $x$ ning uchta qiymati va ularga mos $y$ qiymatlari ko'rsatilgan, bunda
$y=f(x)+4$ va $f$ — kvadrat funksiya:

| $x$ | $y$ |
|---|---|
| $21$ | $-8$ |
| $23$ | $8$ |
| $25$ | $-8$ |

$y=f(x)$ grafigining $y$-o'qi bilan kesishish nuqtasining $y$-koordinatasini toping.

*(Maslahat: jadvalda $x=21$ va $x=25$ uchun $y$ bir xil — $-8$. Bu simmetriya belgisi!
Uchining $x$-koordinatasi shu ikki nuqta orasidagi o'rtacha qiymat ekanini tan olishdan
boshlang, keyin $k+4=8$ dan $k$ ni toping, so'ngra $a$ ni bitta nuqta orqali toping, va
oxirida $x=0$ dagi qiymatni hisoblang — javob butun son emas, bu normal, katta son
chiqishidan qo'rqmang.)*

$\underline{\hspace{30mm}}$

### Qanday aniqlash kerak (how to spot this disguise next time)

- Masalada "maksimal/minimal", "eng baland/eng past nuqta" yoki jadvalda **bir xil $y$
  qiymatiga ega ikkita $x$** uchrasa — bu kvadrat simmetriya signalidir.
- Agar sizdan **uchning o'ziga** emas, balki undan muayyan masofadagi boshqa nuqta
  so'ralsa (masalan "qachon yana shu balandlikka yetadi"), to'liq tenglama qurishdan oldin
  doim simmetriyani tekshiring.
- Bu usul faqat **vaqtni** tejaydi, javobni o'zgartirmaydi — ikkala yo'l ham to'g'ri javobga
  olib keladi, lekin test vaqti cheklangan bo'lgani uchun tezroq yo'l qimmatlidir.

---

## Concept 2 — So'ralgan narsa — birinchi topadigan narsangiz emas (What's Asked Isn't What You'll Find First)

### Ta'rif

*Qiyin savollarda ko'pincha tenglamani yechish natijasida topilgan qiymat va savolda
so'ralgan qiymat **boshqa-boshqa** bo'ladi — masala sizni tabiiy ravishda bitta qiymatni
topishga yo'naltiradi, ammo haqiqiy javob undan **bir qadam nariroqda** turadi.*

<small>(In hard questions, the value your solving process naturally produces and the value
the question actually asks for are often **different** — the problem nudges you toward
finding one thing, but the real answer is **one more step away**.)</small>

Research bu xatoni aniq nomlaydi: testning eng yuqori qismida nuqta yo'qotishning asosiy
sababi — algebra xatosi emas, balki **noto'g'ri miqdorni hisoblash** (`research/02`,
"answering the wrong quantity" topilmasi).

### Model Example (2-misol) — real SAT Hard question

$$y=x^2+2x+1$$
$$x+y+1=0$$

Agar $(x_1,y_1)$ va $(x_2,y_2)$ yuqoridagi tenglamalar sistemasining ikkita yechimi bo'lsa,
$y_1+y_2$ ning qiymati nechaga teng?

**Yechish:** Ikkinchi tenglamadan $y=-x-1$. Birinchisiga qo'yamiz: $-x-1=x^2+2x+1$, bundan
$x^2+3x+2=0$, ya'ni $(x+1)(x+2)=0$. Demak $x=-1$ yoki $x=-2$.

**Eng ko'p uchraydigan sakrash (va aynan shu yerda ko'pchilik yo'qotib qo'yadi):** $x$
qiymatlarini topgач, ko'pchilik darhol $x_1+x_2=-1+(-2)=-3$ ni javob deb o'ylaydi — **chunki
aynan shu qiymatni birinchi bo'lib hisoblagan edi**. Lekin savol $y_1+y_2$ ni so'ramoqda,
$x_1+x_2$ ni emas!

To'g'ri davom etish: $y=-x-1$ orqali har bir $x$ uchun $y$ ni toping. $x=-1$: $y=-(-1)-1=0$.
$x=-2$: $y=-(-2)-1=1$. Demak $y_1+y_2=0+1=1$.

**Javob:** $1$

*(E'tibor bering: $-3$ variant sifatida javoblar ro'yxatida **atayin** qo'yilgan — bu
imtihon tuzuvchilari "noto'g'ri miqdorni hisoblagan" o'quvchini ushlab olish uchun qo'ygan
tuzoq. Har doim savolni ikkinchi marta o'qing: "qaysi harf so'ralmoqda?")*

### Your-Turn Example (O'zingiz bajaring) — real SAT Hard question

$xy$-tekislikda parabolaning uchi $(9,-14)$ nuqtada va u $x$-o'qni ikki nuqtada kesib
o'tadi. Agar parabola tenglamasi $y=ax^2+bx+c$ ko'rinishida yozilsa (bu yerda $a$, $b$, $c$
— konstantalar), $a+b+c$ ning qiymati quyidagilardan qaysi biri bo'lishi mumkin?

A. $-23$     B. $-19$     C. $-14$     D. $-12$

*(Maslahat — bu yerda ham "so'ralgan narsa birinchi topadiganingiz emas" tuzog'i bor, lekin
teskari yo'nalishda: $a+b+c$ ifodasiga alohida-alohida qaramang. $y=ax^2+bx+c$ da $x=1$
qo'ysangiz nima chiqadi? Shuningdek, parabola $x$-o'qni ikki nuqtada kesib o'tishi va uchi
$(9,-14)$ — ya'ni $x$-o'qdan pastda — joylashgani haqidagi shartdan $a$ ning ishorasi
haqida nima xulosa chiqarish mumkinligini o'ylab ko'ring.)*

$\underline{\hspace{30mm}}$

### Qanday aniqlash kerak

- Yechish jarayonida topilgan **birinchi** harf/qiymat ($x$, vaqt, bitta o'zgaruvchi) va
  savolda so'ralgan harf/qiymat ($y$, boshqa o'zgaruvchi, ifodaning qiymati) bir xil
  ekanini **har doim tekshiring** — ayniqsa ular o'xshash tuyulganda.
  qiymatlar ro'yxatida bo'lsa, bu signal: orqaga qaytib, savolni qayta o'qing.

---

## Concept 3 — Tartibsiz ko'rinish ortida — tanish tuzilma (A Familiar Structure Hidden Behind Messy Algebra)

### Ta'rif

*Ba'zi qiyin savollar tenglamalarni atayin "tartibsiz" — standart ko'rinishda emas —
beradi, shunday qilib ularning ortidagi tanish qoida (masalan, "yechimsiz sistema =
parallel chiziqlar") darhol ko'rinmaydi. Birinchi qadam har doim: tenglamalarni **standart
ko'rinishga** ($Ax+By=C$) keltirish.*

<small>(Some hard questions deliberately give equations in a messy, non-standard form so
that the familiar rule underneath — e.g. "no solution = parallel lines" — isn't
immediately visible. The first move is always: rearrange into standard form first.)</small>

### Model Example (3-misol) — real SAT Hard question

$$4x-6y=10y+2$$
$$ty=\frac12+2x$$

Berilgan tenglamalar sistemasida $t$ — konstanta. Agar sistema yechimga ega bo'lmasa, $t$
ning qiymati nechaga teng?

**Yechish — avval standart ko'rinishga keltiring:** Birinchi tenglama: $4x-6y=10y+2$,
bundan $4x-16y=2$, ya'ni $2x-8y=1$. Ikkinchi tenglama: $ty=\frac12+2x$, bundan
$-2x+ty=\frac12$, ya'ni $2x-ty=-\frac12$ (har ikki tomonni $-1$ ga ko'paytirib).

Endi tanish tuzilma ko'rinadi: ikkala tenglama ham $2x$ bilan boshlanadi. Yechimsiz sistema
uchun chiziqlar **parallel va har xil** bo'lishi kerak — ya'ni $x$ va $y$ koeffitsientlari
nisbati teng, lekin erkin had nisbati har xil bo'lishi kerak. $x$ koeffitsientlari allaqachon
teng ($2=2$), demak $y$ koeffitsientlari ham teng bo'lishi kerak: $-8=-t$, bundan $t=8$.

**Javob:** $t=8$

*(Tekshirish: erkin hadlar nisbati $1$ va $-\frac12$ — har xil, demak chiziqlar chindan ham
parallel va har xil, bitta ham umumiy nuqtaga ega emas. Agar bu tekshiruv o'tkazilmasa va
nisbatlar tasodifan teng chiqib qolsa, sistema cheksiz yechimga ega bo'lgan bo'lardi —
"yechimsiz" emas.)*

### Your-Turn Example (O'zingiz bajaring) — real SAT Hard question, reverse direction

$$y=6x+18$$

Ikkita chiziqli tenglamadan tashkil topgan sistemaning bitta tenglamasi yuqorida berilgan.
Sistema yechimga ega emas. Quyidagilardan qaysi biri sistemaning ikkinchi tenglamasi
bo'lishi mumkin?

A. $-6x+y=18$     B. $-6x+y=22$     C. $-12x+y=36$     D. $-12x+y=18$

*(Maslahat: bu safar yo'nalish teskari — sizga $t$ ni emas, balki **butun tenglamani**
tanlash kerak. Berilgan tenglamani avval standart ko'rinishga keltiring: $-6x+y=18$.
Qaysi variant xuddi shu chap tomonga ega, lekin **boshqa** erkin hadga ega — ya'ni parallel,
lekin bir xil chiziq emas?)*

$\underline{\hspace{30mm}}$

### Qanday aniqlash kerak

- "Yechimsiz", "cheksiz ko'p yechim" yoki "bitta yechim" so'zlari uchrasa — darhol
  tenglamalarni $Ax+By=C$ ko'rinishiga keltiring, keyin koeffitsient nisbatlarini solishtiring.
- Yechimsiz $\Rightarrow$ koeffitsient nisbatlari teng, erkin had nisbati har xil.
- Cheksiz yechim $\Rightarrow$ barcha uchta nisbat teng (bir xil chiziq).
- Bitta yechim $\Rightarrow$ koeffitsient nisbatlari har xil.

---

## Concept 4 — Almashtirish tanish ayirmani/yig'indini yashiradi (A Substitution Hides a Familiar Identity)

### Ta'rif

*Ba'zi ifodalarda berilgan almashtirish ($a=c+d$ kabi) ifodani to'g'ridan-to'g'ri ochib
tashlashga emas, balki **tanish algebraik ayniyat** (to'liq kvadrat, kvadratlar ayirmasi)ni
tanishga chaqiradi. Avval almashtirishsiz ifodaning o'zida tanish naqshni qidiring.*

<small>(Some expressions with a given substitution aren't asking you to just expand —
they're asking you to recognize a familiar algebraic identity (perfect square, difference
of squares) first. Look for the pattern in the expression itself before substituting.)</small>

### Model Example (4-misol) — real SAT Hard question

Agar $a=c+d$ bo'lsa, quyidagi ifodalardan qaysi biri $x^2-c^2-2cd-d^2$ ifodasiga teng?

A. $(x+a)^2$     B. $(x-a)^2$     C. $(x+a)(x-a)$     D. $x^2-ax-a^2$

**Yechish:** Oxirgi uchta hadni $-1$ ga ajratib chiqaramiz: $x^2-c^2-2cd-d^2 =
x^2-(c^2+2cd+d^2)$. Qavs ichidagi ifoda — tanish to'liq kvadrat: $c^2+2cd+d^2=(c+d)^2$.
Demak ifoda $x^2-(c+d)^2$ ga teng. Berilgan $a=c+d$ dan, bu $x^2-a^2$ ga teng. Va
$x^2-a^2$ — kvadratlar ayirmasi, $(x+a)(x-a)$ ko'rinishida yoziladi.

**Javob:** C

*(Almashtirishni ($a=c+d$) darhol qo'llashga urinish — ya'ni $c$ va $d$ ni $a$ orqali
ifodalashga harakat qilish — bu yerda noto'g'ri yo'nalish. Avval ifodaning o'zida
to'liq-kvadrat naqshini tanib olish kerak edi, keyingina almashtirish mantiqiy bo'ladi.)*

### Your-Turn Example (O'zingiz bajaring) — real SAT Hard question

$3(2x^2+px+8)-16x(p+4)$ ifodasida $p$ — konstanta. Bu ifoda $6x^2-155x+24$ ifodasiga teng.
$p$ ning qiymati nechaga teng?

A. $-3$     B. $7$     C. $13$     D. $155$

*(Maslahat: qavslarni oching, $x$ oldidagi barcha hadlarni $p$ orqali yig'ing — bu sizga
$x$ koeffitsienti uchun $p$ ga bog'liq bitta ifoda beradi. Keyin uni $-155$ ga tenglashtirib,
$p$ uchun oddiy chiziqli tenglama yeching. Bu "tanish tuzilma" — koeffitsientlarni
tenglashtirish — lekin tartibsiz qavslar ortida yashiringan.)*

$\underline{\hspace{30mm}}$

### Qanday aniqlash kerak

- Ifodada berilgan almashtirish ko'rinishi ($a=c+d$, $u=x^2$ kabi) darhol qo'llanishi shart
  emas — avval ifodaning o'zini tanish ayniyat (to'liq kvadrat, kvadratlar ayirmasi, umumiy
  ko'paytuvchi) nuqtai nazaridan ko'rib chiqing.
- Ko'p qavsli, ko'p hadli "tartibsiz" ifodalar deyarli har doim standart algebraik ayniyatga
  qisqaradi — maqsad sizni shu ayniyatni **tezda tanishga** o'rgatish, uzun ochish amallarini
  mashq qildirish emas.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Disguised / hidden structure | Niqoblangan / yashirin tuzilma |
| Parabola symmetry | Parabola simmetriyasi |
| Vertex | Uchi (parabolaning) |
| Standard form (of a line) | Standart ko'rinish |
| No solution (system) | Yechimsiz (sistema) |
| Infinitely many solutions | Cheksiz ko'p yechim |
| Parallel and distinct | Parallel va har xil |
| Substitution | Almashtirish |
| Perfect square (identity) | To'liq kvadrat (ayniyat) |
| Difference of squares | Kvadratlar ayirmasi |
| Setup error | Masalani noto'g'ri tuzish xatosi |

---

## Notes for the problems file (Sets 1–8)

Every real question used above is adapted from an official College Board Hard-tagged SAT
item (internal tracking only, not shown to the student). Problems.md should:

1. Set 1: parabola-symmetry shortcut drill (direct practice of Concept 1's technique).
2. Set 2: "what's actually asked" drill — each problem solves for one variable/quantity
   naturally, but asks for a different, closely related one.
3. Set 3: no-solution/infinite-solution/one-solution classification from messy (non-standard)
   equation forms.
4. Set 4: substitution-hides-an-identity drill (perfect square, difference of squares,
   coefficient matching through messy distribution).
5. Set 5: mixed — two or more of the above disguises combined in one problem.
6. Set 6: spot-the-error — a solution that fell for exactly the "wrong quantity" or
   "applied the almost-right rule" trap from one of the four concepts above.
7. Set 7: timed bonus — hardest-tier items, real test density.
8. Answer key with full reasoning for the trickier items (not just the final number).
