# Book 3 — Lesson 4: Speed Techniques

**Source content file**, paired with `problems.md`. Book 3 is the 800+ tier — by now every
technique in this lesson is something the student already *could* do the slow way (Book 2
Lessons 5–6: factoring, completing the square, the quadratic formula). This lesson's whole
job is **time**: on a timed adaptive test, the student who recognizes "I don't need to solve
this fully" on sight gains 60–90 seconds per question over the student who grinds through
the full method every time — and on Module 2's harder-routed form, that time difference is
often the difference between finishing the section and running out of clock.

**Research grounding:** `research/15-question-bank-analysis.md` — this lesson's worked
examples are built from real College Board Hard-tagged questions (`SAT MATH.pdf` in
`Materials/`), selected specifically because the "obvious" solving path is slow and a
specific shortcut is fast. Vieta's formulas are **entirely new material** — they appear
nowhere in Book 1 or Book 2.

---

## Nima So'ralmoqda? (What Is Actually Being Asked?)

Tezlik texnikalarining birinchi qadami — hisoblashni boshlashdan oldin, savol **aynan
nimani so'raganini** aniqlash. Agar savol ildizlarning o'zini emas, balki ularning
**yig'indisini** yoki **ko'paytmasini** so'rasa — to'liq tenglamani yechish shart emas,
Viet teoremasi to'g'ridan-to'g'ri javob beradi. Bu farqni ko'rmasdan avtomatik ravishda
to'liq yechishga kirishish — aynan shu lesson bartaraf qilishga qaratilgan vaqt yo'qotish.

---

## Concept 1 — Viet Teoremasi (Vieta's Formulas)

### Definition

*$ax^2+bx+c=0$ ($a\ne0$) tenglamaning ikkita ildizi $x_1$ va $x_2$ bo'lsa, ularning
yig'indisi va ko'paytmasini tenglamani yechmasdan, to'g'ridan-to'g'ri koeffitsientlardan
topish mumkinligini ko'rsatuvchi qoida **Viet teoremasi** deb ataladi:
$x_1+x_2=-\dfrac{b}{a}$, $x_1 \cdot x_2 = \dfrac{c}{a}$.*

<small>(For $ax^2+bx+c=0$ with roots $x_1,x_2$: the sum of the roots is $-b/a$ and the
product is $c/a$ — found directly from the coefficients, no solving required.)</small>

**Qisqacha keltirib chiqarish:** $a\ne0$ bo'lgani uchun tenglamani $a$ ga bo'lib, ildizlar
orqali faktorlab yozamiz: $x^2+\dfrac{b}{a}x+\dfrac{c}{a} = (x-x_1)(x-x_2) =
x^2-(x_1+x_2)x+x_1x_2$. Ikkala tomondagi mos koeffitsientlarni tenglashtiramiz:
$-(x_1+x_2) = \dfrac{b}{a}$, demak $x_1+x_2=-\dfrac{b}{a}$; va $x_1x_2=\dfrac{c}{a}$.

**Bu qachon ishlatiladi:** savol ildizlarning yig'indisi, ko'paytmasi, yoki ulardan
hosil bo'ladigan boshqa simmetrik ifodani ($x_1+x_2$, $x_1x_2$, $\frac{1}{x_1}+\frac{1}{x_2}
=\frac{x_1+x_2}{x_1x_2}$ kabi) so'raganda — $x_1$ va $x_2$ ning o'zini alohida topish
shart emas.

### Model Example (1-misol) — Real SAT Hard question

$$y=x^2+2x+1 \qquad x+y+1=0$$

Yuqoridagi tenglamalar sistemasining ikkita yechimi $(x_1,y_1)$ va $(x_2,y_2)$ bo'lsa,
$y_1+y_2$ ning qiymati nechaga teng?

**Sekin yo'l (ko'pchilik shunday yechadi):** Ikkinchi tenglamadan $y=-x-1$. Birinchisiga
qo'yamiz: $-x-1=x^2+2x+1$, bundan $x^2+3x+2=0$. Faktorlab: $(x+2)(x+1)=0$, demak $x=-2$
yoki $x=-1$. Har birini $y=-x-1$ ga qo'yib: $x=-2$ bo'lsa $y=1$; $x=-1$ bo'lsa $y=0$.
Demak $y_1+y_2 = 1+0=1$.

**Tez yo'l (Viet teoremasi bilan):** $x^2+3x+2=0$ tenglamasiga yetganimizdan so'ng,
ildizlarni alohida topish shart emas — bizga faqat $y_1+y_2$ kerak. Viet teoremasiga ko'ra
$x_1+x_2 = -\dfrac{3}{1}=-3$. Har bir $y=-x-1$ bo'lgani uchun, $y_1+y_2 =
-(x_1+x_2)-2 = -(-3)-2 = 3-2=1$. **Ikkita ildizni alohida hisoblamasdan, bitta qadamda
javobga keldik.**

**Javob:** $y_1+y_2=1$

*(Bu College Board'ning haqiqiy "Hard" darajali savoli — `research/15`da hujjatlashtirilgan
rasmiy savol banki asosida.)*

### Your-Turn Example (O'zingiz bajaring)

$$y = x^2 - 4x + 3 \qquad y = -2x + 11$$

Sistemaning ikkita yechimi $(x_1,y_1)$ va $(x_2,y_2)$. Viet teoremasidan foydalanib,
ildizlarni alohida topmasdan, $x_1+x_2$ ni toping: $\underline{\hspace{20mm}}$. So'ngra
$y_1+y_2$ ni toping (ildizlarni alohida hisoblamasdan): $\underline{\hspace{20mm}}$.

---

## Concept 2 — Takroriy Ildiz Yorlig'i (The Repeated-Root Shortcut)

### Definition

*Diskriminant nolga teng bo'lgan ($b^2-4ac=0$) kvadrat tenglamaning yagona (takroriy)
ildizi, kvadrat formulani to'liq qo'llamasdan, to'g'ridan-to'g'ri $x=-\dfrac{b}{2a}$
formulasi orqali topiladi.*

<small>(When the discriminant is zero, the quadratic's one repeated root is found
directly as $x=-b/(2a)$ — no need to run the full quadratic formula.)</small>

**Bu nega ishlaydi — Viet teoremasi bilan bog'liqligi:** diskriminant nolga teng bo'lsa,
$x_1=x_2=x$ (ikkala ildiz bir xil). Viet teoremasidagi yig'indi formulasi:
$x_1+x_2=-\dfrac{b}{a}$, ya'ni $2x=-\dfrac{b}{a}$, demak $x=-\dfrac{b}{2a}$. **Bu Concept
1 dagi qoidaning xususiy holi — yangi formula emas.**

### Model Example (2-misol) — Real SAT Hard question

$$y=2x^2-21x+64 \qquad y=3x+a$$

Berilgan sistemada $a$ — o'zgarmas son. Tenglamalarning grafiklari $xy$-tekislikda faqat
bitta nuqtada, $(x,y)$ da kesishadi. $x$ ning qiymatini toping.

**Sekin yo'l:** Ikkinchi tenglamani birinchisidan ayiramiz: $0=2x^2-21x+64-3x-a =
2x^2-24x+(64-a)$. Sistema faqat bitta yechimga ega bo'lgani uchun, bu tenglama ham faqat
bitta ildizga ega — demak diskriminant nolga teng: $(-24)^2-4(2)(64-a)=0$. Buni yechib
$a=-8$ topiladi, so'ngra $a=-8$ ni tenglamaga qo'yib, $0=2x^2-24x+72$, ya'ni
$0=2(x-6)^2$, demak $x=6$.

**Tez yo'l:** $a$ ning qiymatini bilish shart emas — savol faqat $x$ ni so'ramoqda, va
tenglama $0=2x^2-24x+(64-a)$ allaqachon diskriminanti nolga teng (chunki bitta yechim
berilgan). Takroriy ildiz yorlig'i: $x = -\dfrac{b}{2a_{\text{koeff}}} =
-\dfrac{-24}{2(2)} = \dfrac{24}{4}=6$. **$a$ ning qiymatini hisoblash bosqichi butunlay
tashlab yuborildi.**

**Javob:** $x=6$

### Your-Turn Example (O'zingiz bajaring)

$y=3x^2-18x+k$ va $y=0$ tenglamalari grafigi faqat bitta nuqtada kesishadi ($k$ —
o'zgarmas son). Takroriy ildiz yorlig'idan foydalanib, $x$ ni toping (avval $k$ ni
hisoblashga urinmang): $\underline{\hspace{20mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** har doim avval noma'lum koeffitsientni ($a$, $k$ kabi) to'liq
hisoblab, keyin uni tenglamaga qo'yib, to'liq kvadrat formula bilan ildizni qayta topish —
holbuki savol faqat ildizning o'zini so'ragan va diskriminant nolga teng ekani allaqachon
berilgan.

**To'g'ri qoida:** "faqat bitta yechim/kesishish nuqtasi" so'zlari diskriminant **nolga
teng** ekanini anglatadi — bu ma'lumotni darhol $x=-\frac{b}{2a}$ formulasiga qo'llang,
oraliq noma'lumni hisoblashga vaqt sarflamang, agar savol aynan shu noma'lumni so'ramasa.

---

## Concept 3 — To'liq Faktorlash Usullari (Full Factoring-Pattern Mastery)

### Reference table — darhol tanish bo'lishi kerak bo'lgan shakllar

| Shakl (Pattern) | Faktorlangan ko'rinish | Tanish belgisi |
|---|---|---|
| To'liq kvadrat yig'indisi | $a^2+2ab+b^2=(a+b)^2$ | Uchta had, chetki ikkitasi kvadrat, o'rtadagisi $2\times$ko'paytma |
| To'liq kvadrat ayirmasi | $a^2-2ab+b^2=(a-b)^2$ | Xuddi yuqoridagidek, o'rta had manfiy |
| Kvadratlar ayirmasi | $a^2-b^2=(a+b)(a-b)$ | Ikkita had, ikkalasi ham kvadrat, orasida minus |
| Kublar yig'indisi | $a^3+b^3=(a+b)(a^2-ab+b^2)$ | Ikkita had, ikkalasi ham kub, orasida plus |
| Kublar ayirmasi | $a^3-b^3=(a-b)(a^2+ab+b^2)$ | Ikkita had, ikkalasi ham kub, orasida minus |
| Guruhlash (grouping) | $4$ hadli ifodani $2+2$ ga guruhlab, umumiy ko'paytuvchi chiqarish | Oddiy umumiy ko'paytuvchi yo'q, lekin hadlar juft-juft guruhlanganda chiqadi |

*(Kublar formulalari Book 1–2 da uchramagan — bular Book 3 ning "kamdan-kam ishlatiladigan,
lekin bilish shart" formulalaridan ikkitasi.)*

### Model Example (3-misol) — Real SAT Hard question

Agar $a=c+d$ bo'lsa, $x^2-c^2-2cd-d^2$ ifodasiga teng bo'lgan ifodani toping.

**Yechish (tezkor naqsh tanish orqali):** Oxirgi uchta haddan $-1$ ni qavsga chiqaramiz:
$x^2-c^2-2cd-d^2 = x^2-(c^2+2cd+d^2)$. Qavs ichidagi ifoda — tanish naqsh, to'liq kvadrat
yig'indisi: $c^2+2cd+d^2=(c+d)^2$. Demak ifoda $x^2-(c+d)^2$ ko'rinishiga keladi. $a=c+d$
berilgan, shuning uchun bu $x^2-a^2$ — ikkinchi tanish naqsh, kvadratlar ayirmasi:
$x^2-a^2=(x+a)(x-a)$.

**Javob:** $(x+a)(x-a)$

*(Ikki naqshni ketma-ket — avval to'liq kvadrat, keyin kvadratlar ayirmasi — zanjir
sifatida tanib olish, bu savolni 10 soniyada yechadi; naqshni tanimasdan ochib-yopib
ko'paytirish esa ancha uzoq va xato ehtimoli yuqori yo'l.)*

### Your-Turn Example (O'zingiz bajaring)

Agar $m=p-q$ bo'lsa, $y^2-p^2+2pq-q^2$ ifodasiga teng bo'lgan ifodani toping (ikkita
naqshni ketma-ket qo'llang): $\underline{\hspace{30mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** naqshni tanimasdan, ifodani to'g'ridan-to'g'ri ochib-yopib
(expand qilib) qayta guruhlashga urinish — bu ham ishlaydi, lekin 3-4 baravar ko'proq
vaqt oladi va ishora xatosiga moyil.

**To'g'ri qoida:** uchta yoki to'rtta hadli ifodani ko'rganda, avval "bu reference
jadvaldagi qaysi naqshga o'xshaydi?" deb so'rang — agar javob topilsa, formulani
to'g'ridan-to'g'ri qo'llang, ochib-yopishga vaqt sarflamang.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Vieta's formulas | Viet teoremasi |
| Sum of roots | Ildizlar yig'indisi |
| Product of roots | Ildizlar ko'paytmasi |
| Repeated root | Takroriy ildiz |
| Perfect square trinomial | To'liq kvadrat uch had |
| Difference of squares | Kvadratlar ayirmasi |
| Sum/difference of cubes | Kublar yig'indisi/ayirmasi |
| Grouping (factoring technique) | Guruhlash usuli |

---

## Notes for the problems file (Sets 1–7)

1. Vieta's formulas — pure sum/product drill, given $a,b,c$ directly.
2. Vieta's formulas — applied to a system (like Model Example 1), find $y_1+y_2$ or
   similar without finding individual roots. Timed: "under 30 seconds."
3. Repeated-root shortcut — given "exactly one solution," find the root or a related
   unknown directly via $-b/2a$, timed: "under 20 seconds, no quadratic formula."
4. Factoring-pattern recognition drill — classify which of the 6 reference patterns
   applies, then factor (includes at least 2 cube-pattern items — rare but real).
5. Mixed — student chooses the fastest applicable technique (some items have no
   shortcut and genuinely need the full method — recognizing *that* is also a skill).
6. Spot the error — targets using the full quadratic formula where Vieta's/repeated-root
   would have been faster (not a wrong answer, but a wasted-time error — flag it as such),
   plus one genuine naqsh-misapplication error.
7. Bonus/Challenge — includes an adapted version of the real `00165291` grouping-method
   question (quartic-in-disguise, solved via grouping after setting up two linear
   equations in the unknown coefficients) as the hardest item, full solution shown.
