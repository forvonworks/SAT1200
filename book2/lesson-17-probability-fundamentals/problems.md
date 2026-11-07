# Book 2 — Lesson 17: Probability Fundamentals — Practice Sets

**Source content file**, paired with `concepts.md`. Sets build: basic
probability → table-based probability → mutually-exclusive addition rule →
independent multiplication rule → classify-the-relationship (the core
payoff of this lesson) → spot-the-error on the independence/exclusivity
conflation → bonus. All answers verified by script (`fractions.Fraction`),
not hand-computed.

---

## Set 1 — Basic Probability (Favorable / Total)

1. A bag has 7 red and 3 blue marbles. Find $P(\text{red})$.
2. A jar has 5 green, 4 yellow, and 3 purple marbles. Find $P(\text{yellow})$.
3. A class of 25 students has 15 who play chess. Find $P(\text{plays chess})$.
4. A spinner has 8 equal sections numbered 1–8. Find $P(\text{lands on a
   number greater than 5})$.
5. A set of cards is numbered 1 through 20. Find $P(\text{card is a
   multiple of 4})$.
6. A box has 6 red pens and 9 blue pens. Find $P(\text{blue})$.

## Set 2 — Probability From a Table

A survey of 60 students gives:

| | Likes Math | Doesn't Like Math | Total |
|---|---|---|---|
| Boys | 18 | 12 | 30 |
| Girls | 22 | 8 | 30 |
| **Total** | **40** | **20** | **60** |

1. $P(\text{randomly chosen student likes math})$
2. $P(\text{randomly chosen student is a girl})$
3. $P(\text{student is a boy AND likes math})$
4. $P(\text{student is a girl who doesn't like math})$
5. $P(\text{likes math} \mid \text{student is a boy})$ — restrict the total
   to just the boys' row first.
6. $P(\text{is a girl} \mid \text{student likes math})$ — restrict the
   total to just the "Likes Math" column first.

## Set 3 — Mutually Exclusive Events & the Addition Rule

Check overlap before choosing the simple or general form of the rule.

1. A die is rolled. Find $P(\text{rolling a 2 or a 5})$.
2. A card is drawn from a standard 52-card deck. Find $P(\text{King or
   Queen})$.
3. A die is rolled. Find $P(\text{even number or a number greater than 4})$.
4. A spinner has 10 equal sections numbered 1–10. Find $P(\text{multiple of
   3 or multiple of 5})$.
5. A bag has 4 red, 5 blue, and 3 green marbles. Find $P(\text{red or
   green})$.
6. A die is rolled. Find $P(\text{number less than 3 or an odd number})$.

## Set 4 — Independent Events & the Multiplication Rule

1. A coin is flipped twice. Find $P(\text{heads, then heads})$.
2. A die is rolled twice. Find $P(\text{first roll is 6 AND second roll is
   even})$.
3. One card is drawn from each of two separate full decks. Find
   $P(\text{both are Aces})$.
4. A spinner with 4 equal sections numbered 1–4 is spun twice. Find
   $P(\text{first spin is odd AND second spin is 4})$.
5. Bag A has 3 red and 2 blue marbles. Bag B has 4 red and 6 blue marbles.
   One marble is drawn from each bag. Find $P(\text{both red})$.
6. A weighted coin lands heads with probability $0.6$ on every flip,
   flips independent of each other. Find $P(\text{heads on both of two
   flips})$.

## Set 5 — Classify the Relationship

For each pair of events, decide: **mutually exclusive only**,
**independent only**, **neither**, or **both** — and justify with the
actual probabilities, not intuition. (Hint for #6: check what happens when
one event has probability $0$.)

1. A die is rolled once. $A$ = "rolling an even number." $B$ = "rolling an
   odd number."
2. Two separate coins are flipped. $A$ = "first coin shows heads." $B$ =
   "second coin shows tails."
3. One card is drawn from a deck. $A$ = "card is a heart." $B$ = "card is
   red."
4. A red die and a blue die are rolled together. $A$ = "red die shows 1."
   $B$ = "blue die shows 6."
5. One card is drawn from a deck. $A$ = "card is a spade." $B$ = "card is a
   heart."
6. A die is rolled once. $A$ = "rolling a 7" (note: a standard die has no
   7). $B$ = "rolling an even number."

## Set 6 — Spot the Error

Each item shows a solution that conflates independence with mutual
exclusivity (or vice versa) — exactly the gap this lesson targets. Name the
error and give the correct answer (or corrected reasoning for #5).

1. Bir zar tashlanganda, $A$ = juft son tushishi, $B$ = $4$ dan katta son
   tushishi. *"Bu ikki hodisa bog'liq emas, shuning uchun
   $P(A \text{ yoki } B) = P(A)+P(B) = \frac36+\frac26=\frac56$."*
2. Tanga ikki marta tashlanadi. $A$ = birinchi tashlashda gerb, $B$ =
   ikkinchi tashlashda gerb. *"Ikkalasi ham gerb bo'lishi "g'alati"
   tuyuladi, shuning uchun bular birgalikda bo'lmaydi, demak
   $P(A \text{ va } B) = 0$."*
3. Zar tashlanadi. $A$ = $2$ tushishi, $B$ = $5$ tushishi. *"Bular
   birgalikda bo'lmaydi, demak ular mustaqil ham — shuning uchun
   $P(A \text{ va } B) = P(A)\times P(B) = \frac16\times\frac16=\frac{1}{36}$."*
4. Standart 52 ta kartadan bitta tortiladi. $A$ = karta qizil, $B$ = karta
   yurak (heart) turkumidan. *"Bular ikki xil xossa, demak mustaqil —
   shuning uchun $P(A \text{ va } B) = \frac12\times\frac14=\frac18$."*
5. Ikki xaltadan (A va B) bittadan shar tortiladi. *"Bu ikki tortish
   bog'liq emas (chunki ikki xil xalta), shuning uchun bu hodisalar bir
   vaqtda sodir bo'lolmaydi, ya'ni ular birgalikda bo'lmaydi."*

## Set 7 — Bonus / Challenge

1. A survey of 100 people finds 55 like coffee, 40 like tea, and 20 like
   both. Find $P(\text{likes coffee or tea})$.
2. $A$ and $B$ are independent events with $P(A)=0.3$ and $P(B)=0.5$. Find
   $P(A \text{ or } B)$. (First find $P(A \text{ and } B)$ using
   independence, then apply the general addition rule.)
3. A box has 3 red and 7 blue balls. Two balls are drawn **without
   replacement**. Find $P(\text{both red})$. (These draws are *not*
   independent — the first draw changes what's left for the second.)
4. A die is rolled once. $A$ = "rolling a number $\le 3$." $B$ = "rolling a
   number $\ge 4$." Are $A$ and $B$ mutually exclusive? Independent? Find
   $P(A \text{ or } B)$.
5. Two spinners, each with 5 equal sections numbered 1–5, are spun
   independently. Find the probability that the sum of the two spins is
   $8$.

---

## Answer Key

**Set 1:** 1) $\frac{7}{10}$  2) $\frac13$  3) $\frac35$  4) $\frac38$
5) $\frac14$  6) $\frac35$

**Set 2:** 1) $\frac23$  2) $\frac12$  3) $\frac{3}{10}$  4) $\frac{2}{15}$
5) $\frac35$  6) $\frac{11}{20}$

**Set 3:** 1) $\frac13$  2) $\frac{2}{13}$  3) $\frac23$  4) $\frac12$
5) $\frac{7}{12}$  6) $\frac23$

**Set 4:** 1) $\frac14$  2) $\frac{1}{12}$  3) $\frac{1}{169}$  4) $\frac18$
5) $\frac{6}{25}$  6) $\frac{9}{25}$

**Set 5:**
1. $P(A \text{ va } B)=0$ (even and odd can't both happen) → mutually
   exclusive. $P(A)\times P(B)=\frac14\ne0$ → not independent. **Mutually
   exclusive only.**
2. HT is a valid outcome, so not mutually exclusive. $P(A \text{ va } B)=
   \frac12\times\frac12=\frac14=P(A)\times P(B)$ → independent.
   **Independent only.**
3. Every heart is red, so overlap is nonzero ($\frac{13}{52}$) — not
   mutually exclusive. $P(A)\times P(B)=\frac14\times\frac12=\frac18
   \ne\frac{13}{52}=\frac14$ — not independent either. **Neither.**
4. Different dice — can both happen (not ME). $P(A \text{ va } B)=
   \frac16\times\frac16=P(A)\times P(B)$ → independent. **Independent
   only.**
5. Can't be both suits at once → mutually exclusive, $P(A\text{ va }B)=0$.
   $P(A)\times P(B)=\frac{1}{16}\ne0$ → not independent. **Mutually
   exclusive only.**
6. $P(A)=0$ (impossible event). $P(A \text{ va } B)=0$, which matches
   *both* the mutually-exclusive condition ($=0$) and the independence
   condition ($P(A)\times P(B)=0\times\frac12=0$). **Both** — this only
   happens because $P(A)=0$; it's the edge case that proves the rule
   "nonzero-probability mutually exclusive events are never independent"
   needs that "nonzero" qualifier.

**Set 6:**
1. Error — assumed mutually exclusive (no overlap) when $6$ satisfies
   both "even" and "$>4$"; the simple addition rule was used without
   checking for overlap. Correct: $P=\frac36+\frac26-\frac16=\frac23$.
2. Error — assumed mutually exclusive based on intuition ("feels
   unusual") instead of checking; HH is in fact a perfectly valid outcome,
   so these events are independent, not mutually exclusive. Correct:
   $P(A \text{ va } B)=\frac12\times\frac12=\frac14$.
3. Error — the exact backwards rule: concluded mutually exclusive implies
   independent, when it's the opposite (nonzero-probability mutually
   exclusive events are never independent). Since rolling a 2 and rolling
   a 5 can never happen together, $P(A \text{ va } B)=0$, not $\frac{1}{36}$.
4. Error — assumed independence without checking the actual overlap;
   every heart is automatically red, so knowing the card is a heart
   completely determines it's also red. Correct:
   $P(A \text{ va } B)=P(\text{heart})=\frac14$, not $\frac18$.
5. Error — confusing independence with mutual exclusivity in the other
   direction: separate bags make the two draws *independent*, but
   independent events absolutely *can* happen together — that's exactly
   what $P(A \text{ va } B)=P(A)\times P(B)$ computes (a positive number,
   not zero). Independent does not mean "can't happen together"; it means
   "one doesn't affect the other's probability."

**Set 7:** 1) $\frac34$  2) $0.65$ (or $\frac{13}{20}$)  3) $\frac{1}{15}$
4) Mutually exclusive (can't be both $\le3$ and $\ge4$); not independent
(product $\frac14\ne0$); $P(A\text{ or }B)=1$ (every roll is one or the
other — the two events cover the entire sample space). 5) $\frac{3}{25}$
