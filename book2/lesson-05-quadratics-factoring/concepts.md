# Book 2 — Lesson 5: Quadratics I — Factoring & Solving

**Source content file.** Advanced Math domain (~35% of SAT Math per
`research/01-official-sat-math-spec.md`). Book 2 goes beyond the SAT's own
ceiling — more rigorous than Book 1's pure fundamentals — but this lesson
stays strictly to factoring. Completing the square and the quadratic formula
are Lesson 6; graphing and the discriminant are Lesson 7. Don't reach ahead.

**Research grounding:** `research/04-common-student-mistakes.md` names
"stopping after finding one root" as a documented SAT error (quadratics have
up to two solutions, and time pressure makes students quit after the first).
A targeted web search surfaced the single highest-value factoring-specific
error: misapplying the zero-product property when the equation isn't actually
set to zero — e.g. treating $(x+2)(x-1)=6$ as if $x+2=6$ or $x-1=6$, which is
simply false; the property only works when a product equals exactly zero.

---

## Concept 1 — Kvadrat Tenglama va Yechim Nima Ekanligi

### Definition

*$ax^2+bx+c=0$ ($a\neq0$) ko'rinishidagi tenglama kvadrat tenglama deb
ataladi. Bu tenglamani yechish — uni to'g'ri qiluvchi $x$ qiymatlarini
(ildizlarni) topish demakdir. Kvadrat tenglama ko'pi bilan ikkita ildizga ega
bo'ladi — shuning uchun ikkalasini ham topib, ikkalasini ham javobga yozish
kerak.*

<small>(A quadratic equation has the form $ax^2+bx+c=0$. Solving it means
finding the values of $x$ that make it true — up to two of them.)</small>

| Tenglama | $a$ | $b$ | $c$ |
|---|---|---|---|
| $x^2+5x+6=0$ | $1$ | $5$ | $6$ |
| $3x^2-2x+1=0$ | $3$ | $-2$ | $1$ |
| $x^2-9=0$ | $1$ | $0$ | $-9$ |

*(No model/your-turn pair here — this is orientation, not a new skill yet.)*

---

## Concept 2 — $a=1$ Bo'lganda Ko'paytuvchilarga Ajratish

### Definition

*$x^2+bx+c$ ko'rinishidagi ifodani ko'paytuvchilarga ajratish uchun
ko'paytmasi $c$ ga, yig'indisi $b$ ga teng bo'lgan ikkita son topiladi.*

<small>(To factor $x^2+bx+c$, find two numbers that multiply to $c$ and add
to $b$.)</small>

### Model Example (1-misol)

$$x^2+5x+6=0$$

**Yechish:** Ko'paytmasi $6$ ga, yig'indisi $5$ ga teng ikkita son kerak:
$2$ va $3$ ($2\times3=6$, $2+3=5$). Shuning uchun:
$(x+2)(x+3)=0$. Nolga teng ko'paytma xossasiga ko'ra: $x+2=0$ yoki $x+3=0$.

**Javob:** $x=-2$ yoki $x=-3$ *(ikkala ildiz ham yozilishi shart)*

### Your-Turn Example (O'zingiz bajaring)

$$x^2+7x+12=0 \quad\Rightarrow\quad x=\underline{\hspace{15mm}} \text{ yoki } x=\underline{\hspace{15mm}}$$

---

## Concept 3 — GCF va $a\neq1$ Bo'lganda Ko'paytuvchilarga Ajratish

### Definition

*Ko'paytuvchilarga ajratishdan oldin, barcha hadlarga umumiy bo'luvchi (GCF —
Greatest Common Factor) bo'lsa, u avval qavsdan tashqariga chiqariladi;
shundan keyingina qolgan ifoda Concept 2 usuli bilan ajratiladi.*

<small>(Factor out any GCF first, then factor what's left using Concept 2's
method.)</small>

### Model Example (2-misol)

$$2x^2+8x+6=0$$

**Yechish:** Barcha hadlarda $2$ umumiy ko'paytuvchi: $2(x^2+4x+3)=0$. Endi
qavs ichini ajratamiz: ko'paytmasi $3$, yig'indisi $4$ bo'lgan sonlar — $1$ va
$3$. $2(x+1)(x+3)=0$. $2\neq0$ bo'lgani uchun: $x+1=0$ yoki $x+3=0$.

**Javob:** $x=-1$ yoki $x=-3$

### Your-Turn Example (O'zingiz bajaring)

$$3x^2-x-2=0 \quad\Rightarrow\quad x=\underline{\hspace{15mm}} \text{ yoki } x=\underline{\hspace{15mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** GCF ni e'tiborsiz qoldirib, to'g'ridan-to'g'ri $a\neq1$ holatini
murakkab usulda ajratishga urinish — yoki manfiy GCF chiqarilganda ichkaridagi
har bir hadning ishorasini o'zgartirishni unutish.

**To'g'ri:** Har doim avval GCF bor-yo'qligini tekshiring. Manfiy son chiqarsangiz
(masalan $-2$), qavs ichidagi HAR BIR hadning ishorasi teskariga aylanadi:
$-2x^2-6x = -2(x^2+3x)$, *emas* $-2(x^2-3x)$.

---

## Concept 4 — Nolga Teng Ko'paytma Xossasi va "Nima So'ralmoqda?"

### Definition

*Agar ikki yoki undan ortiq ifodaning ko'paytmasi nolga teng bo'lsa, ulardan
kamida bittasi nolga teng bo'ladi — bu nolga teng ko'paytma xossasi (zero-product
property) deb ataladi. Bu xossadan foydalanish uchun tenglama albatta
"ifoda $\times$ ifoda $=0$" ko'rinishida bo'lishi SHART — agar o'ng tomonda
nol emas, boshqa son tursa, avval hammasini bir tomonga yig'ib, nolga
tenglashtirish kerak.*

<small>(The zero-product property only works when a product equals exactly
zero. If the equation isn't already in that form, rearrange it to equal zero
first — you cannot set each factor equal to some other number.)</small>

### Model Example (3-misol)

$$(x-3)(x+1)=5$$

**Yechish:** Bu yerda o'ng tomon $0$ emas, $5$ — shuning uchun hali
ko'paytuvchilarni alohida $5$ ga tenglashtirib bo'lmaydi. Avval qavsni
ochamiz: $x^2-2x-3=5$. Ikkala tomondan $5$ ni ayiramiz: $x^2-2x-8=0$. Endi
ko'paytuvchilarga ajratamiz: ko'paytmasi $-8$, yig'indisi $-2$ bo'lgan sonlar
— $-4$ va $2$. $(x-4)(x+2)=0$. Shunda $x-4=0$ yoki $x+2=0$.

**Javob:** $x=4$ yoki $x=-2$

### "Nima So'ralmoqda?" — SAT uchun muhim eslatma

Ildizlarni topgandan so'ng, savolni qaytadan o'qing — SAT ko'pincha ildizlarning
o'zini emas, ulardan hosil bo'lgan boshqa qiymatni so'raydi: ildizlar
yig'indisini, ko'paytmasini, yoki kattasi bilan kichigi orasidagi farqni.
Masalan, yuqoridagi misolda savol "ildizlar yig'indisi nechaga teng?" deb
so'ralsa, javob $4+(-2)=2$ bo'ladi — ildizlarning o'zi emas.

### Your-Turn Example (O'zingiz bajaring)

$$(x+2)(x-1)=4 \quad\Rightarrow\quad x=\underline{\hspace{15mm}} \text{ yoki } x=\underline{\hspace{15mm}}$$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri:** $(x+2)(x-1)=6$ tenglamasini $x+2=6$ yoki $x-1=6$ deb yechishga
urinish.

**To'g'ri:** Nolga teng ko'paytma xossasi FAQAT ko'paytma nolga teng bo'lganda
ishlaydi. $(x+2)(x-1)=6$ da avval qavsni ochib, hammasini bir tomonga
yig'ib, nolga tenglashtirish kerak — keyingina ajratish mumkin.

**Ikkinchi keng tarqalgan xato:** Ikkita ildizdan faqat bittasini topib
to'xtash. Kvadrat tenglama ko'pi bilan ikkita ildizga ega — ikkalasini ham
toping va ikkalasini ham javobga yozing, ayniqsa vaqt tig'iz bo'lganda bu
xato tez-tez uchraydi.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Quadratic equation | Kvadrat tenglama |
| Standard form | Standart ko'rinish |
| Root / Solution | Ildiz / Yechim |
| Factor (verb) | Ko'paytuvchilarga ajratish |
| GCF (Greatest Common Factor) | Eng katta umumiy bo'luvchi |
| Zero-product property | Nolga teng ko'paytma xossasi |
| Sum of the roots | Ildizlar yig'indisi |
| Product of the roots | Ildizlar ko'paytmasi |

## Notes for the problems file (Sets 1–7)

- Set 1: $a=1$, all-positive $b$ and $c$ — easiest entry point.
- Set 2: $a=1$, negative $b$ and/or $c$ — sign-pair selection practice.
- Set 3: GCF extraction + $a\neq1$ factoring.
- Set 4: equations not yet set to zero — the rearrange-first skill, directly
  targeting the documented zero-product misapplication.
- Set 5: "what's actually being asked" — compute the sum, product, or
  difference of the roots, not just the roots themselves.
- Set 6: spot-the-error — four items, each a distinct documented mistake
  (stopping at one root; wrong sign pair; zero-product misapplied; dividing
  by a variable and losing a root).
- Set 7: bonus/challenge — difference-of-squares, fraction roots, and two
  more rearrange-first items at higher difficulty.
