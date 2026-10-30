# Book 1 — Lesson 3: Decimals & Percent Conversion — Practice Sets

**Source content file**, paired with `concepts.md`. Sets build in the order
specified at the bottom of `concepts.md`: decimal add/subtract → decimal
multiply/divide → decimal↔fraction → percent↔decimal → percent↔fraction/
percent-of-a-number → spot-the-error → bonus challenge. Every answer below
was verified by a Python script (`fractions.Fraction` for exact fraction
checks, explicit rounding for decimals) — none are hand-computed.

All percents/decimals/fractions use SAT-standard notation (decimal **point**,
not comma — see Concept 1's notation note).

---

## Set 1 — Decimal Addition & Subtraction

Builds the align-then-pad habit from Concept 1.

1. $3.7 + 2.45$
2. $12.6 - 4.75$
3. $0.8 + 0.09$
4. $15 - 3.25$
5. $2.05 + 1.95$
6. $100 - 0.4$
7. $0.125 + 0.875$
8. $7.3 - 2.08$

## Set 2 — Decimal Multiplication & Division

A separate skill from Set 1 — the error here is miscounting decimal places,
not misaligning them.

1. $0.3 \times 0.4$
2. $2.5 \times 1.2$
3. $0.06 \times 5$
4. $1.44 \div 1.2$
5. $0.5 \times 0.5$
6. $7.2 \div 0.4$
7. $0.02 \times 0.03$
8. $9.6 \div 2.4$

## Set 3 — Decimal ↔ Fraction Conversion

1. $0.5$ ni oddiy kasrga aylantiring.
2. $0.25$ ni oddiy kasrga aylantiring.
3. $0.75$ ni oddiy kasrga aylantiring.
4. $0.2$ ni oddiy kasrga aylantiring.
5. $\dfrac{3}{4}$ ni o'nli kasrga aylantiring.
6. $\dfrac{1}{8}$ ni o'nli kasrga aylantiring.
7. $\dfrac{7}{10}$ ni o'nli kasrga aylantiring.
8. $0.125$ ni oddiy kasrga aylantiring.

## Set 4 — Percent ↔ Decimal Conversion

Includes percents above 100% and below 1% to test the "move two places" rule
at its edges, not just the easy middle cases.

1. $45\%$ ni o'nli kasrga aylantiring.
2. $7\%$ ni o'nli kasrga aylantiring.
3. $150\%$ ni o'nli kasrga aylantiring.
4. $0.5\%$ ni o'nli kasrga aylantiring.
5. $0.6$ ni foizga aylantiring.
6. $1.25$ ni foizga aylantiring.
7. $0.03$ ni foizga aylantiring.
8. $2$ ni foizga aylantiring.

## Set 5 — Percent ↔ Fraction, Percent of a Number

1. $80$ ning $25\%$ i qanchaga teng?
2. $150$ ning $10\%$ i qanchaga teng?
3. $45$ ning $60\%$ i qanchaga teng?
4. $\dfrac{1}{4}$ ni foizga aylantiring.
5. $\dfrac{3}{5}$ ni foizga aylantiring.
6. $150\%$ ni oddiy kasrga aylantiring.
7. $50$ ning $12\%$ i qanchaga teng?
8. $20$ ning $90\%$ i qanchaga teng?

## Set 6 — Spot the Error

Each item shows a solution with exactly one broken step. Name the step, say
what rule it breaks, and give the correct final answer.

1. Hisoblang: $80$ ning $45\%$ i.
   *Noto'g'ri yechim:* "$45 \times 80 = 3600$, demak javob $3600$."
2. Hisoblang: $3.7 + 2.45$.
   *Noto'g'ri yechim:* "Vergulni tekislamasdan qo'shib, $3.7 + 2.45 = 2.82$
   deb topilgan."
3. Hisoblang: $1.44 \div 1.2$.
   *Noto'g'ri yechim:* "Kasr xonalarini noto'g'ri sanab, $1.44 \div 1.2 =
   0.12$ deb topilgan."
4. $0.2$ ni oddiy kasrga aylantiring.
   *Noto'g'ri yechim:* "$0.2$ dagi raqam yuzdan bir xonasida deb o'ylab,
   $\dfrac{2}{100} = \dfrac{1}{50}$ deb topilgan."
5. $150\%$ ni o'nli kasrga aylantiring.
   *Noto'g'ri yechim:* "Vergul faqat bir xona chapga surilib, $150\% = 15$
   deb topilgan."

## Set 7 — Bonus / Challenge (mixed conversions, ~90 seconds each)

1. $0.8$ ning $35\%$ ini toping, so'ngra natijani $100$ ga ko'paytiring.
2. $\dfrac{3}{8}$ ni foizga aylantiring.
3. $0.6$ ning necha foizi $0.3$ ga teng?
4. $1.5$ ni foizga va oddiy kasrga aylantiring.
5. $(0.25 + 0.5)$ yig'indisining $40\%$ ini toping.

---

## Answer Key

**Set 1:** 1) 6.15  2) 7.85  3) 0.89  4) 11.75  5) 4  6) 99.6  7) 1  8) 5.22

**Set 2:** 1) 0.12  2) 3  3) 0.3  4) 1.2  5) 0.25  6) 18  7) 0.0006  8) 4

**Set 3:** 1) 1/2  2) 1/4  3) 3/4  4) 1/5  5) 0.75  6) 0.125  7) 0.7  8) 1/8

**Set 4:** 1) 0.45  2) 0.07  3) 1.5  4) 0.005  5) 60%  6) 125%  7) 3%  8) 200%

**Set 5:** 1) 20  2) 15  3) 27  4) 25%  5) 60%  6) 3/2  7) 6  8) 18

**Set 6:**
1. Error — percent was multiplied directly without converting to a decimal
   first. Correct: $45\% = 0.45$, then $0.45 \times 80 = 36$.
2. Error — decimal points were not aligned before adding (0.7 was treated as
   if it were 0.07). Correct: align and pad — $3.70 + 2.45 = 6.15$.
3. Error — decimal places miscounted during division, shifting the result by
   a factor of 10. Correct: $1.44 \div 1.2 = 1.2$.
4. Error — misread which place value the digit 2 occupies (tenths, not
   hundredths). Correct: $0.2 = \dfrac{2}{10} = \dfrac{1}{5}$.
5. Error — moved the decimal point only one place instead of two. Correct:
   $150\% = 1.50 = 1.5$.

**Set 7:** 1) 28  2) 37.5%  3) 50%  4) 150% and 3/2  5) 0.3
