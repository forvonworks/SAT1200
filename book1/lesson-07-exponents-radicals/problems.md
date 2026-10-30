# Book 1 — Lesson 7: Exponents & Radicals (Basic) — Practice Sets

**Source content file**, paired with `concepts.md`. Sets build in the order
specified at the bottom of `concepts.md`: pure rule drill → zero/negative
exponents → mixed exponents → simplifying radicals → combining radicals →
spot-the-error → bonus challenge. Every answer below verified by script
(Python, exact fraction/symbolic arithmetic, not floats) — see the lesson's
commit message for confirmation.

All expressions use SAT-standard notation (fraction bar for division,
juxtaposition/$\times$ for multiplication, $\sqrt{\ }$ for square roots).

---

## Set 1 — Exponent Rules Drill (no zero/negative exponents yet)

1. $2^2 \times 2^3$
2. $\dfrac{3^4}{3^2}$
3. $(2^2)^3$
4. $5^3 \times 5^2$
5. $\dfrac{4^5}{4^3}$
6. $(3^2)^2$
7. $2^3 \times 2^3$
8. $(2^3)^3$

*(Items 7 and 8 are a deliberate pair — same numbers, different structure.
Students should get different answers and be able to explain why, per the
Common Mistake box in `concepts.md`.)*

## Set 2 — Zero and Negative Exponents

1. $5^0$
2. $2^{-3}$
3. $4^{-2}$
4. $2^0 \times 2^{-2}$
5. $3^{-2} \times 3^4$
6. $5^2 \times 5^{-2}$
7. $10^{-1} \times 100$
8. $2^{-1} + 2^{-2}$

## Set 3 — Mixed, Real-Test Density

1. $\dfrac{(2^2 \times 2^3)^2}{2^4}$
2. $(3 \times 3^2)^2$
3. $\dfrac{5^3}{5^2 \times 5^{-1}}$
4. $(2^{-1})^{-3}$
5. $(4^2)^0$
6. $\dfrac{2^5}{2^{-2}}$
7. $\dfrac{(3^2)^2}{3^3}$
8. $10^3 \times 10^{-1} \div 10$

## Set 4 — Simplifying Square Roots

1. $\sqrt{16}$
2. $\sqrt{49}$
3. $\sqrt{18}$
4. $\sqrt{50}$
5. $\sqrt{72}$
6. $\sqrt{20}$
7. $\sqrt{45}$
8. $\sqrt{8}$

## Set 5 — Combining Radicals

1. $\sqrt{8} + \sqrt{2}$
2. $\sqrt{18} - \sqrt{2}$
3. $\sqrt{12} + \sqrt{27}$
4. $\sqrt{50} - \sqrt{8}$
5. $2\sqrt{3} \times \sqrt{3}$
6. $\sqrt{2} \times \sqrt{8}$
7. $3\sqrt{5} + 2\sqrt{5}$
8. $\sqrt{45} - \sqrt{20}$

## Set 6 — Spot the Error

Each item shows a solution with exactly one broken step. Name the step, say
what rule it breaks, and give the correct final answer.

1. $2^3 \times 2^3$ — *"Noto'g'ri yechim: $2^3 \times 2^3 = 2^9 = 512$."*
2. $(2^2)^3$ — *"Noto'g'ri yechim: $(2^2)^3 = 2^{2+3} = 2^5 = 32$."*
3. $2^{-3}$ — *"Noto'g'ri yechim: $2^{-3} = -8$."*
4. $\sqrt{16+9}$ — *"Noto'g'ri yechim: $\sqrt{16}+\sqrt{9} = 4+3 = 7$."*
5. $\sqrt{32}$ — *"Noto'g'ri yechim: $32 = 16 \times 2$ deb to'g'ri
   ajratilgan, lekin javobda $16\sqrt{2}$ deb yozilgan."*

## Set 7 — Bonus / Challenge (timed, ~90 seconds each)

1. $\dfrac{(2^3)^2}{2^4} + \sqrt{16}$
2. $\sqrt{3^2 \times 2^2}$
3. $2^{-2} \times 4^2 + \sqrt{9}$
4. $(\sqrt{2})^4$
5. $1 + \sqrt{5^2 - 3^2}$

---

## Answer Key

**Set 1:** 1) 32  2) 9  3) 64  4) 3125  5) 16  6) 81  7) 64  8) 512

**Set 2:** 1) 1  2) $\frac{1}{8}$  3) $\frac{1}{16}$  4) $\frac{1}{4}$
5) 9  6) 1  7) 10  8) $\frac{3}{4}$

**Set 3:** 1) 64  2) 729  3) 25  4) 8  5) 1  6) 128  7) 3  8) 10

**Set 4:** 1) 4  2) 7  3) $3\sqrt{2}$  4) $5\sqrt{2}$  5) $6\sqrt{2}$
6) $2\sqrt{5}$  7) $3\sqrt{5}$  8) $2\sqrt{2}$

**Set 5:** 1) $3\sqrt{2}$  2) $2\sqrt{2}$  3) $5\sqrt{3}$  4) $3\sqrt{2}$
5) 6  6) 4  7) $5\sqrt{5}$  8) $\sqrt{5}$

**Set 6:**
1. Error — multiplied the exponents instead of adding them (this is the
   product rule, $a^p \times a^p = a^{2p}$, not the power rule). Correct:
   $2^{3+3} = 2^6 = 64$.
2. Error — added the exponents instead of multiplying them (this is a power
   raised to a power, $(a^p)^q = a^{pq}$, not the product rule). Correct:
   $2^{2 \times 3} = 2^6 = 64$.
3. Error — treated the negative exponent as making the base negative instead
   of taking the reciprocal. Correct: $2^{-3} = \frac{1}{2^3} = \frac{1}{8}$.
4. Error — split the square root of a sum into a sum of square roots, which
   is never valid. Correct: $\sqrt{16+9} = \sqrt{25} = 5$.
5. Error — factored out $16$ correctly but forgot to take $16$'s own square
   root before pulling it outside the radical. Correct:
   $\sqrt{32} = \sqrt{16 \times 2} = \sqrt{16}\times\sqrt{2} = 4\sqrt{2}$.

**Set 7:** 1) 8  2) 6  3) 7  4) 4  5) 5
