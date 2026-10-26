# Book 1 — Lesson 1: Basic Arithmetic & Order of Operations

**Source content file.** This is the authored content, not the final page — it gets
typeset against `research/14-design-spec.md`. Structure follows that spec's
content-block pattern exactly (§6): Definition → Model example → Your-turn →
common-mistake box → Vocabulary, repeated per concept on this lesson.

**Research grounding:** `research/02-topic-difficulty-taxonomy.md` (order of
operations named explicitly as a top-3 pre-SAT gap, alongside fractions and
decimals) and `research/04-common-student-mistakes.md`. Checked against the
official College Board Question Bank export in `Materials/`: order of
operations is **not** a tagged SAT skill in its own right — every question is
tagged under Algebra/Advanced Math/etc. — confirming it's treated as assumed
prior knowledge the real test never re-teaches. That's exactly why it's Book 1,
Lesson 1: get it automatic before anything else depends on it.

---

## Concept 1 — Arithmetic Operations & Their Names

### Definition

*Qo'shish, ayirish, ko'paytirish va bo'lish kabi sonlar ustida bajariladigan
harakatlar arifmetik amallar deb ataladi. Har bir amalning natijasi ham o'z
nomiga ega: qo'shishning natijasi — yig'indi, ayirishniki — ayirma,
ko'paytirishniki — ko'paytma, bo'lishniki — bo'linma deb ataladi.*

<small>(Addition, subtraction, multiplication, and division are called
arithmetic operations. Each operation's result also has its own name: a sum,
a difference, a product, a quotient.)</small>

**Why this matters for the SAT, not just as a definition:** these result-names
are exactly the words SAT word problems use instead of symbols — "the sum of
x and 7," "the product of two consecutive integers," "a quotient of 4" — so
this isn't a vocabulary formality, it's the first step of translating English
into an equation (the skill Book 2 Lesson 4 builds on directly).

### Quick reference table

| Amal (Operation) | Belgi (Symbol) | Natija nomi (Result name) | English |
|---|---|---|---|
| Qo'shish | $+$ | Yig'indi | Sum |
| Ayirish | $-$ | Ayirma | Difference |
| Ko'paytirish | $\times$ (or juxtaposition: $ab$) | Ko'paytma | Product |
| Bo'lish | $\div$ or $\dfrac{a}{b}$ | Bo'linma | Quotient |

*Note on notation:* SAT materials almost never use $\div$ or a middle dot for
multiplication — division is written as a fraction ($\frac{a}{b}$), and
multiplication is written by juxtaposition ($3x$, $(x+1)(x-2)$) or $\times$
only when both are numerals ($3 \times 4$). Students used to seeing $\div$ and
$\cdot$ constantly in local textbooks should expect fraction and juxtaposition
notation to dominate on the actual test.

*(No model/your-turn pair here — this is a fluency check, not new material.
Moving straight to the lesson's real content.)*

---

## Concept 2 — Order of Operations (Amallar Bajarish Tartibi)

### Definition

*Bir nechta amalni o'z ichiga olgan ifodani hisoblashda, amallarning qat'iy
belgilangan ketma-ketlikda bajarilishini talab qiluvchi qoida amallar bajarish
tartibi deb ataladi. Bu tartibga ko'ra, amallar quyidagi izchillikda
bajariladi: avval qavs ichidagi amallar, so'ngra daraja va ildiz, keyin II
bosqich amallari — ko'paytirish va bo'lish (chapdan o'ngga), va eng oxirida I
bosqich amallari — qo'shish va ayirish (chapdan o'ngga).*

<small>(When an expression contains more than one operation, a fixed order
decides what gets computed first: parentheses, then exponents/roots, then
Stage II operations — multiplication and division, left to right — then Stage
I operations — addition and subtraction, left to right.)</small>

**Note on framing — do this in class, not just on the page:** Uzbek curriculum
teaches this as *I bosqich amallari* (addition/subtraction) and *II bosqich
amallari* (multiplication/division) rather than an English mnemonic like
PEMDAS. Keep that native framing — it's not a simplification, it's how
students already learned it, and research on PEMDAS specifically shows the
*mnemonic itself* is a common source of error (see Common Mistake box below).
Introduce "PEMDAS" only as a side-note — students will see it used in
imported materials and should recognize it, but it should not replace the
bosqich framing as the primary mental model.

$$\text{Qavs} \rightarrow \text{Daraja / ildiz} \rightarrow \text{II bosqich (} \times, \div \text{)} \rightarrow \text{I bosqich (} +, - \text{)}$$

**Two groupings the "qavs" step must also catch, not just visible
parentheses** — this is the single highest-value SAT-specific extension of a
rule students already know:

- **Kasr chizig'i (the fraction bar) groups everything above it and
  everything below it**, as if each were in its own parentheses — even with
  no parentheses drawn. $\dfrac{3+5}{2 \times 2}$ means
  $\dfrac{(3+5)}{(2\times2)}$, not $3 + \dfrac{5}{2} \times 2$.
- **Modul belgisi (absolute value bars, $|\ |$) also group their contents**
  before the absolute value itself is applied: everything inside $|\ |$ is
  computed first, then the result is made non-negative.

### Model Example (1-misol)

$$5 + 2 \times (8 - 3)^2 \div 5 = ?$$

**Yechish:**
Avval qavs ichidagi amal bajariladi: $8 - 3 = 5$. Ifoda quyidagi ko'rinishni
oladi: $5 + 2 \times 5^2 \div 5$.

Keyin daraja hisoblanadi: $5^2 = 25$. Ifoda: $5 + 2 \times 25 \div 5$.

Endi II bosqich amallari chapdan o'ngga bajariladi: avval $2 \times 25 = 50$,
so'ngra $50 \div 5 = 10$. Ifoda: $5 + 10$.

Eng oxirida I bosqich amali bajariladi: $5 + 10 = 15$.

**Javob:** $15$

### Your-Turn Example (O'zingiz bajaring)

$$12 - 3 \times (1 + 3)^2 \div 6 = \underline{\hspace{25mm}}$$

*(Student works all four stages; space provided for working, not just the
final blank — matches the step-by-step shown in the model.)*

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** Ko'paytirishni har doim bo'lishdan oldin, qo'shishni
esa har doim ayirishdan oldin bajarish kerak deb o'ylash.

**To'g'ri qoida:** Ko'paytirish va bo'lish bir xil bosqichga tegishli — ular
ifodada qaysi tartibda uchrasa, **chapdan o'ngga** shu tartibda bajariladi
(xuddi shunday, qo'shish va ayirish ham bir xil bosqich). $20 \div 4 \times 5$
ifodasida avval bo'lish emas, chapda turgan amal — ya'ni bo'lish — bajariladi
chunki u chapda: $20 \div 4 = 5$, so'ng $5 \times 5 = 25$. Agar
"ko'paytirish har doim birinchi" degan noto'g'ri qoida qo'llansa, natija
noto'g'ri — $20 \div 20 = 1$ — chiqib ketadi.

*(Research basis: this exact confusion — treating × as always preceding ÷, and
+ as always preceding −, rather than recognizing them as equal-priority,
left-to-right pairs — is the most consistently documented PEMDAS
misconception across multiple independent studies, including one reporting
roughly 70% of a preservice-teacher sample holding this exact
misconception. See `research/02` and session research notes.)*

**Second common mistake, SAT-specific:** treating "qavs" as meaning only
*explicitly drawn* parentheses, and missing that a fraction bar or absolute
value bars group their contents the same way. This mirrors a real error
pattern seen in official SAT material: substituting a negative value into an
expression and misapplying order of operations around the implied grouping
is explicitly named as a wrong-answer trap in official answer rationales
(general pattern — not reproducing any specific test question here).

$$\frac{10 - 4}{2 \times 3} \quad \ne \quad 10 - \frac{4}{2} \times 3$$

The left side treats top and bottom as grouped ($= 1$); the right side wrongly
applies order of operations as if there were no fraction bar at all ($= 4$).

### Vocabulary

| English | O'zbekcha |
|---|---|
| Arithmetic operation | Arifmetik amal |
| Sum / Difference / Product / Quotient | Yig'indi / Ayirma / Ko'paytma / Bo'linma |
| Order of operations | Amallar bajarish tartibi |
| Parentheses | Qavs |
| Exponent | Daraja |
| Stage I operations (+, −) | I bosqich amallari |
| Stage II operations (×, ÷) | II bosqich amallari |
| Left to right | Chapdan o'ngga |
| Fraction bar | Kasr chizig'i |
| Absolute value bars | Modul belgisi |

---

## Notes for the problems file (Sets 1–6/7)

- Set 1: pure numeric PEMDAS drills, no negatives, building the 4-stage habit.
- Set 2: add negative numbers inside the expression (bridges toward Lesson 4,
  without requiring signed-number rules not yet taught — keep negatives as
  given values being substituted, not operations the student must derive).
- Set 3: fraction-bar-as-grouping drills specifically (the highest-value
  SAT-specific extension identified above).
- Set 4: absolute-value-bars-as-grouping drills.
- Set 5: mixed — exponents + fraction bar + parentheses combined, closer to
  real test density.
- Set 6: "spot the error" format — given a wrong worked solution using the
  documented misconception (× before ÷ regardless of position), student
  identifies which step broke the rule. Directly targets the common mistake
  from pedagogy research (erroneous-examples effect — conditional use,
  exactly the documented-common-error case `06-concept-explanation-pedagogy.md`
  calls this technique appropriate for).
- Set 7 (bonus/challenge): multi-layer nested parentheses + fraction bar +
  absolute value combined in one expression, timed.
