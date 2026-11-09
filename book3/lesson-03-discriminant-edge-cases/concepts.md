# Book 3 — Lesson 3: No-Real-Solution Quadratics & Discriminant Edge Cases

**Source content file**, paired with `problems.md`. Book 3 is the 800+/hardest tier —
the final book. This lesson builds directly on Book 2 Lesson 6 (quadratic formula,
derived — $D=b^2-4ac$ is literally the piece under the radical) and Book 2 Lesson 7
(the discriminant as a solution-counter: $D>0$ two real roots, $D=0$ one, $D<0$ none).
**It does not re-teach that baseline** — it goes into the genuine edge-case territory
the real SAT tests at the Hard tier: using the discriminant *backward* to solve for an
unknown parameter, recognizing a quadratic *disguised* inside a system, a radical
equation, or a word problem, and handling the subtlety of "exactly one real solution"
when squaring an equation can introduce an extraneous root.

**Research grounding:** `research/15-question-bank-analysis.md` documents the official
College Board Question Bank pipeline. This lesson is built directly from real
Hard-tagged SAT questions in the "Nonlinear equations in one variable and systems of
equations in two variables" skill (62-question Hard pool) — rendered and read via the
vision pipeline documented there, not guessed. Model Example 3 below reproduces one of
those real questions essentially as-is (Question ID `2c288148`, SAT Question Bank,
Hard) — a genuine released-difficulty example, not an invented approximation of one.

---

## Concept 1 — Tizimni Bitta Kvadrat Tenglamaga Keltirish (Reducing a System to a Single Quadratic)

### Definition

*Chiziq va parabolaning kesishish nuqtalarini topish uchun ikkala tenglamani
tenglashtirib, bitta o'zgaruvchili kvadrat tenglama hosil qilish usuli tizimni
kvadrat tenglamaga keltirish deb ataladi; hosil bo'lgan tenglamaning diskriminanti
esa kesishish nuqtalari sonini — ularni to'liq yechmasdan turib — aniqlaydi.*

<small>(Setting a line's and a parabola's equations equal to each other reduces a
system to a single-variable quadratic — this is called reducing the system to a
quadratic. That quadratic's discriminant then tells you how many intersection points
exist, before you fully solve.)</small>

**Nima so'ralmoqda?** SAT bu texnikani ko'pincha "necha marta kesishadi" yoki "nechta
umumiy yechimi bor" tarzida so'raydi — bu savolga javob berish uchun koordinatalarning
o'zini topish shart emas, faqat diskriminantning ishorasi yetarli. Agar savol aynan
kesishish nuqtasini so'rasa, shundagina to'liq yechish kerak.

### Model Example (1-misol)

$$y = 2x^2 - 21x + 64 \qquad\qquad y = 3x + a$$

Berilgan tizimda $a$ — doimiy son. Tizimning grafiklari $xy$-tekislikda aynan bitta
$(x,y)$ nuqtada kesishadi. $x$ ning qiymatini toping. *(Real SAT Hard question, ID
`77c0cced` — $a$ ning qiymati berilmagan, lekin bitta yechim borligi orqali topish
mumkin.)*

**Yechish:** Ikkinchi tenglamani birinchisidan ayiramiz: $0 = 2x^2-21x+64-(3x+a)$,
ya'ni $0 = 2x^2-24x+(64-a)$. Tizim aynan bitta yechimga ega bo'lgani uchun, bu kvadrat
tenglama ham aynan bitta yechimga ega — demak uning diskriminanti nolga teng. $a=2$,
$b=-24$, $c=64-a$ (bu yerdagi "$a$" diskriminant formulasidagi koeffitsient, savoldagi
$a$ bilan chalkashtirmang): $D=(-24)^2-4(2)(64-a)=576-512+8a=64+8a$. $D=0$ dan: $a=-8$.

Endi $a=-8$ ni qo'yib, kvadrat tenglamani yechamiz: $0=2x^2-24x+72$, ya'ni
$0=x^2-12x+36=(x-6)^2$. Demak $x=6$.

**Javob:** $x=6$

*(Diqqat: savolda ikkita noma'lum bor edi — $a$ va $x$. Avval diskriminant orqali
$a$ ni topdik, keyingina $x$ ni topdik. Ikki bosqichli bu ketma-ketlikni SAT hard
savollarida tez-tez uchratasiz.)*

### Your-Turn Example (O'zingiz bajaring)

$y=x^2-6x+13$ va $y=4x-11$. Tizim nechta kesishish nuqtasiga ega? Agar birdan ko'p
bo'lsa, ularni toping: $\underline{\hspace{40mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Ikkala tenglamani tenglashtirishda ishorani noto'g'ri ko'chirish —
masalan $y=2x^2-21x+64$ va $y=3x+a$ ni tenglashtirib, $2x^2-21x+64-3x+a=0$ deb yozish
($-a$ o'rniga $+a$).

**To'g'ri:** Ikkinchi tenglamaning **butun o'ng tomoni** ayiriladi:
$2x^2-21x+64-(3x+a)=0$, qavsni ochganda $-3x$ **va** $-a$ chiqadi:
$2x^2-24x+(64-a)=0$. Qavs ichidagi ikkala hadni ham ishorasini o'zgartirib ochish
kerak, faqat birinchisini emas.

---

## Concept 2 — Diskriminantni Orqaga Qarab Ishlatish (Using the Discriminant Backward)

### Definition

*Tenglamaning yechimlar soni oldindan berilib, shu shart orqali noma'lum
koeffitsientni topish usuli diskriminantni orqaga qarab ishlatish deb ataladi —
odatdagi yo'nalish teskarisiga: avval $D$ ning ishorasi haqidagi shartni tenglama
yoki tengsizlik sifatida yozib, so'ngra uni noma'lum uchun yechamiz.*

<small>(Given a stated solution-count, working backward through the discriminant to
find an unknown coefficient — the reverse of the usual direction: write the condition
on $D$'s sign as an equation or inequality, then solve it for the unknown.)</small>

**Ikki holat farqlanadi:**
- **"Aynan bitta yechim"** → $D=0$, **tenglama** hosil bo'ladi, bitta (yoki ikkita)
  aniq qiymat chiqadi.
- **"Yechim yo'q"** yoki **"birdan ortiq yechim"** → $D<0$ yoki $D>0$, **tengsizlik**
  hosil bo'ladi, noma'lumning butun bir **oralig'i** javob bo'ladi — shuning uchun
  savol ko'pincha "eng kichik butun qiymat" yoki "eng katta mumkin bo'lgan qiymat"
  deb so'raydi, aniq bitta son emas.

### Model Example (2-misol)

$$y=-2.5 \qquad\qquad y=x^2+8x+k$$

Berilgan tizimda $k$ — musbat butun son. Tizim hech qanday haqiqiy yechimga ega emas.
$k$ ning eng kichik mumkin bo'lgan qiymatini toping. *(Real SAT Hard question, ID
`6aefc52b`.)*

**Yechish:** Tenglashtiramiz: $x^2+8x+k=-2.5$, ya'ni $x^2+8x+(k+2.5)=0$. Haqiqiy
yechim yo'qligi uchun $D<0$: $D=8^2-4(1)(k+2.5)=64-4k-10=54-4k$. Shart: $54-4k<0$,
bundan $k>13.5$. $k$ butun son bo'lgani uchun, shartni qanoatlantiruvchi **eng kichik**
butun son $k=14$.

**Javob:** $k=14$

*(Bu yerda javob bitta "chegaraviy" son emas — $k=13.5$ emas, chunki $k=13.5$ da
$D=0$ bo'lib, bu aynan bitta yechim degani, "yechim yo'q" emas. Tengsizlikni qat'iy
($D<0$, $D\le0$ emas) yechish va keyin "eng kichik butun" ni alohida topish kerak.)*

### Your-Turn Example (O'zingiz bajaring)

$4x^2-20x+c=0$ tenglamasi aynan bitta yechimga ega. $c$ ning qiymatini toping:
$c=\underline{\hspace{15mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** $b^2>K$ ko'rinishidagi tengsizlikni yechishda faqat $b>\sqrt K$ ni
yozib, $b<-\sqrt K$ tarmog'ini unutib qo'yish — masalan $b^2>1600$ dan faqat $b>40$
deb xulosa chiqarish.

**To'g'ri:** $b^2>K$ ($K>0$) tengsizligi **ikkita** tarmoqqa ega: $b>\sqrt K$ **yoki**
$b<-\sqrt K$. Ildiz chiqarishda ishorani unutish — bu xuddi $x^2=9$ dan faqat $x=3$
deb, $x=-3$ ni unutib qo'yishga o'xshaydi, faqat tengsizlik holatida xato yanada
ko'zga tashlanmay qoladi. To'g'ri javob: $b<-40$ yoki $b>40$.

---

## Concept 3 — Yashiringan Kvadrat Tenglamalar (Disguised Quadratics)

### Definition

*Tashqi ko'rinishidan kvadrat tenglama bo'lmagan, ammo soddalashtirish yoki ikkala
tomonni kvadratga ko'tarish orqali kvadrat tenglamaga aylanadigan tenglama yashiringan
kvadrat tenglama deb ataladi; bunday hollarda diskriminantni qo'llashdan oldin
tenglamani albatta standart ko'rinishga ($ax^2+bx+c=0$) keltirish shart.*

<small>(An equation that doesn't look quadratic on the surface, but becomes one after
simplifying or squaring both sides, is a disguised quadratic. Before the discriminant
can be applied, the equation must first be rearranged into standard form.)</small>

**Eng muhim ogohlantirish:** ildiz belgisi ($\sqrt{\ }$) ishtirok etgan tenglamani
ikkala tomonini kvadratga ko'tarsangiz, natijada hosil bo'lgan kvadrat tenglama
**qo'shimcha (begona) yechim** keltirib chiqarishi mumkin — bu yechim original
tenglamani qanoatlantirmaydi. Shuning uchun "nechta haqiqiy yechim" savoli bu yerda
ikki qatlamli: avval kvadrat tenglamaning diskriminanti bilan ishlaysiz, so'ngra har
bir topilgan yechimni **original tenglamaga** qo'yib tekshirasiz.

### Model Example (3-misol)

$$\sqrt{k-x} = 58-x$$

Berilgan tenglamada $k$ — doimiy son. Tenglama aynan bitta haqiqiy yechimga ega.
$4k$ ning eng kichik mumkin bo'lgan qiymatini toping. *(Bu — real SAT Hard savoli,
ID `2c288148`, College Board Question Bank'dan olingan — o'zgartirishsiz.)*

**Yechish:** Ildiz ostidagi ifoda manfiy bo'lmasligi va ildizning o'zi ham manfiy
bo'lmasligi kerak — demak $58-x\ge0$, ya'ni $x\le58$ bo'lishi shart (bu — **sohaviy
shart**, keyinroq tekshirish uchun eslab qoling). Ikkala tomonni kvadratga ko'taramiz:
$k-x=(58-x)^2$. O'ng tomonni ochamiz: $k-x=3364-116x+x^2$. $x$ ni chap tomonga
o'tkazamiz: $k=x^2-115x+3364$. Hammasini bir tomonga yig'amiz: $0=x^2-115x+(3364-k)$.

Bu — standart kvadrat tenglama: $a=1$, $b=-115$, $c=3364-k$.
$D=(-115)^2-4(1)(3364-k)=13225-13456+4k=4k-231$.

Agar $4k<231$ bo'lsa, $D<0$ — kvadrat tenglamaning o'zi yechimga ega emas, demak
original tenglama ham yechimga ega emas (nol yechim). Agar $4k=231$ bo'lsa, $D=0$ —
kvadrat tenglama **aynan bitta** yechimga ega, $x=57.5$. Bu yechim sohaviy shartni
tekshiramiz: $58-57.5=0.5>0$ — shart bajariladi, demak bu yechim **haqiqiy va
begona emas**. Shunday qilib, $4k=231$ bo'lganda original tenglama aynan bitta
haqiqiy yechimga ega bo'ladi, va bu — mumkin bo'lgan **eng kichik** qiymat (undan
kichik $4k$ da yechim umuman yo'q).

**Javob:** $4k$ ning eng kichik qiymati — $231$.

*(Bu masalaning chuqurligi shunda: savol "diskriminant nolga teng bo'lsin" deb
to'g'ridan-to'g'ri aytmagan — "aynan bitta haqiqiy yechim" degan, va buni $D=0$
shartiga aylantirish, PLUS topilgan yechimni sohaviy shart bilan tekshirish — ikkala
qadam ham talab qilingan. Faqat $D=0$ ni yechib, tekshirishni unutish ko'p hollarda
tasodifan to'g'ri javob beradi, lekin har doim emas — tekshirish qadamini tushirib
qoldirmang.)*

### Your-Turn Example (O'zingiz bajaring)

$\sqrt{k-x} = 40-x$ tenglamasi aynan bitta haqiqiy yechimga ega. $4k$ ning eng kichik
mumkin bo'lgan qiymatini toping (yuqoridagi usulni to'liq takrorlang — $58$ o'rniga
$40$ qo'yib): $4k=\underline{\hspace{20mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** Kvadratga ko'targandan so'ng, hosil bo'lgan kvadrat tenglamaning
yechimlarini original tenglamani tekshirmasdan, to'g'ridan-to'g'ri javob deb qabul
qilish.

**To'g'ri:** Har safar ildizli (yoki modulli) tenglamani kvadratga ko'targaningizda,
**sohaviy shartni** ($\sqrt{\ }$ belgisi ostidagi va tenglamaning ikkinchi tomonidagi
ifodalar manfiy bo'lmasligi) alohida yozib qo'ying, va topilgan har bir yechimni shu
shartga nisbatan tekshiring — qanoatlantirmasa, u **begona yechim** va rad etiladi.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Discriminant | Diskriminant |
| No real solution | Haqiqiy yechim yo'q |
| Exactly one real solution | Aynan bitta haqiqiy yechim |
| Disguised quadratic | Yashiringan kvadrat tenglama |
| Extraneous solution | Begona yechim |
| Domain condition | Sohaviy shart |
| To reduce (a system) to a quadratic | Kvadrat tenglamaga keltirish |
| Working backward (from a condition) | Orqaga qarab ishlash |

---

## Notes for the problems file (Sets 1–8)

1. Classify by discriminant alone — no solving, speed drill.
2. Systems reduced to a quadratic — classify intersection count, find points when exactly one.
3. Discriminant backward, $D=0$ (equation) — solve for the unknown parameter.
4. Discriminant backward, $D<0$/$D>0$ (inequality) — find a range or an extreme integer value.
5. Disguised quadratics (radical equations, rational equations, a tangent-style word problem) — fewer items, hardest tier.
6. Mixed — combines two techniques per problem (e.g., find the parameter, then the point; or ties into Vieta's-style root-sign reasoning as a bridge toward Lesson 4).
7. Spot the error — targets: forgetting the ± branch in an inequality, skipping the extraneous-solution check, mis-signing a,b,c after an incomplete rearrangement, confusing "no real solution" with "no solution" in a word-problem context.
8. Bonus/Challenge — two more real Hard-tagged SAT questions (unmodified) plus an original proof-style item ("show this system never intersects").
