# Book 2 — Lesson 17: Probability Fundamentals — Practice Sets

**Source content file**, paired with `concepts.md`. Sets build: basic
probability → table-based probability → mutually-exclusive addition rule →
independent multiplication rule → classify-the-relationship (the core
payoff of this lesson) → spot-the-error on the independence/exclusivity
conflation → bonus. All answers verified by script (`fractions.Fraction`),
not hand-computed.

---

## Set 1 — Basic Probability (Favorable / Total)

1. A bag contains $7$ red marbles and $3$ blue marbles. If one marble is
   selected at random from the bag, what is the probability that the
   marble selected is red?
2. A jar contains $5$ green marbles, $4$ yellow marbles, and $3$ purple
   marbles. If one marble is selected at random from the jar, what is the
   probability that the marble selected is yellow?
3. A class consists of $25$ students, of whom $15$ play chess. If one
   student is selected at random from the class, what is the probability
   that the student selected plays chess?
4. A spinner is divided into $8$ equal sections numbered $1$ through $8$.
   If the spinner is spun once, what is the probability that it lands on
   a number greater than $5$?
5. A set of cards is numbered $1$ through $20$. If one card is selected at
   random from the set, what is the probability that the number on the
   card selected is a multiple of $4$?
6. A box contains $6$ red pens and $9$ blue pens. If one pen is selected
   at random from the box, what is the probability that the pen selected
   is blue?

## Set 2 — Probability From a Table

The table below summarizes the results of a survey of $60$ students.

| | Likes Math | Doesn't Like Math | Total |
|---|---|---|---|
| Boys | 18 | 12 | 30 |
| Girls | 22 | 8 | 30 |
| **Total** | **40** | **20** | **60** |

1. Based on the table, if one student from the survey is selected at
   random, what is the probability that the student selected likes math?
2. Based on the table, if one student from the survey is selected at
   random, what is the probability that the student selected is a girl?
3. Based on the table, if one student from the survey is selected at
   random, what is the probability that the student selected is a boy who
   likes math?
4. Based on the table, if one student from the survey is selected at
   random, what is the probability that the student selected is a girl
   who does not like math?
5. Based on the table, if one boy from the survey is selected at random,
   what is the probability that the boy selected likes math? (Restrict
   the total to the boys' row only.)
6. Based on the table, if one student who likes math is selected at
   random from the survey, what is the probability that the student
   selected is a girl? (Restrict the total to the "Likes Math" column
   only.)

## Set 3 — Mutually Exclusive Events & the Addition Rule

Check overlap before choosing the simple or general form of the rule.

1. A fair six-sided die is rolled once. What is the probability that the
   die shows a $2$ or a $5$?
2. A card is selected at random from a standard deck of $52$ playing
   cards. What is the probability that the card selected is a king or a
   queen?
3. A fair six-sided die is rolled once. What is the probability that the
   die shows an even number or a number greater than $4$?
4. A spinner is divided into $10$ equal sections numbered $1$ through
   $10$. If the spinner is spun once, what is the probability that it
   lands on a multiple of $3$ or a multiple of $5$?
5. A bag contains $4$ red marbles, $5$ blue marbles, and $3$ green
   marbles. If one marble is selected at random from the bag, what is the
   probability that the marble selected is red or green?
6. A fair six-sided die is rolled once. What is the probability that the
   die shows a number less than $3$ or an odd number?

## Set 4 — Independent Events & the Multiplication Rule

1. A fair coin is flipped twice. What is the probability that the coin
   shows heads on both flips?
2. A fair six-sided die is rolled twice. What is the probability that the
   first roll is a $6$ and the second roll is an even number?
3. One card is selected at random from each of two separate, standard
   $52$-card decks. What is the probability that both cards selected are
   aces?
4. A spinner divided into $4$ equal sections numbered $1$ through $4$ is
   spun twice. What is the probability that the first spin results in an
   odd number and the second spin results in a $4$?
5. Bag A contains $3$ red marbles and $2$ blue marbles. Bag B contains
   $4$ red marbles and $6$ blue marbles. If one marble is selected at
   random from each bag, what is the probability that both marbles
   selected are red?
6. A weighted coin lands on heads with probability $0.6$ on each flip, and
   the outcomes of different flips are independent of each other. What is
   the probability that the coin lands on heads on both of two flips?

## Set 5 — Classify the Relationship

For each pair of events below, determine whether the events are
**mutually exclusive only**, **independent only**, **neither**, or
**both** — and justify your answer using the actual probabilities, not
intuition. (Hint for item 6: consider what happens when one event has
probability $0$.)

1. A fair six-sided die is rolled once. Let $A$ be the event that the die
   shows an even number, and let $B$ be the event that the die shows an
   odd number.
2. Two separate coins are flipped. Let $A$ be the event that the first
   coin shows heads, and let $B$ be the event that the second coin shows
   tails.
3. One card is selected at random from a standard deck of $52$ playing
   cards. Let $A$ be the event that the card is a heart, and let $B$ be
   the event that the card is red.
4. A red die and a blue die are rolled together. Let $A$ be the event
   that the red die shows a $1$, and let $B$ be the event that the blue
   die shows a $6$.
5. One card is selected at random from a standard deck of $52$ playing
   cards. Let $A$ be the event that the card is a spade, and let $B$ be
   the event that the card is a heart.
6. A fair six-sided die is rolled once. Let $A$ be the event that the die
   shows a $7$ (note that a standard die has no face showing $7$), and
   let $B$ be the event that the die shows an even number.

## Set 6 — Spot the Error

Each item shows a solution that conflates independence with mutual
exclusivity (or vice versa) — exactly the gap this lesson targets. Name
the error and give the correct answer (or corrected reasoning for item 5).

1. A fair six-sided die is rolled once. Let $A$ be the event that the die
   shows an even number, and let $B$ be the event that the die shows a
   number greater than $4$. A student reasons: *"These two events don't
   affect each other, so $P(A \text{ or } B) = P(A)+P(B) =
   \frac36+\frac26=\frac56$."*
2. A fair coin is flipped twice. Let $A$ be the event that the first flip
   shows heads, and let $B$ be the event that the second flip shows
   heads. A student reasons: *"Both flips landing on heads seems
   unlikely, so these two events can't happen together, meaning
   $P(A \text{ and } B) = 0$."*
3. A fair six-sided die is rolled once. Let $A$ be the event that the die
   shows a $2$, and let $B$ be the event that the die shows a $5$. A
   student reasons: *"These two outcomes can't happen on the same roll,
   so they must also be independent — therefore
   $P(A \text{ and } B) = P(A)\times P(B) = \frac16\times\frac16=
   \frac{1}{36}$."*
4. One card is selected at random from a standard deck of $52$ playing
   cards. Let $A$ be the event that the card is red, and let $B$ be the
   event that the card is a heart. A student reasons: *"These describe
   two different properties of the card, so the events must be
   independent — therefore $P(A \text{ and } B) = \frac12\times\frac14=
   \frac18$."*
5. One marble is selected at random from each of two separate bags, Bag
   A and Bag B. A student reasons: *"These two draws are independent of
   each other, since they come from different bags — so the two events
   can't happen at the same time, meaning they are mutually exclusive."*

## Set 7 — Bonus / Challenge

1. A survey of $100$ people finds that $55$ like coffee, $40$ like tea,
   and $20$ like both coffee and tea. If one person from the survey is
   selected at random, what is the probability that the person selected
   likes coffee or tea?
2. Events $A$ and $B$ are independent, with $P(A)=0.3$ and $P(B)=0.5$.
   What is $P(A \text{ or } B)$? (First find $P(A \text{ and } B)$ using
   independence, then apply the general addition rule.)
3. A box contains $3$ red balls and $7$ blue balls. Two balls are
   selected at random, **without replacement**. What is the probability
   that both balls selected are red? (These draws are *not* independent
   — the first draw changes what remains for the second.)
4. A fair six-sided die is rolled once. Let $A$ be the event that the die
   shows a number less than or equal to $3$, and let $B$ be the event
   that the die shows a number greater than or equal to $4$. Are $A$ and
   $B$ mutually exclusive? Are they independent? What is
   $P(A \text{ or } B)$?
5. Two spinners, each divided into $5$ equal sections numbered $1$
   through $5$, are spun independently. What is the probability that the
   sum of the two spins is $8$?

## Set 8 — Official SAT-Style Application

Multiple-choice (A–D), matching the Digital SAT's format and item design for the
skill *Probability and conditional probability*. 15 Easy / 15 Medium / 15 Hard.
Every item is **original**: numbers, names and contexts are new, and each one
needs the same method as the official items (favorable over total, restricting a
table total to the conditioned row or column, the addition rule with or without
overlap, the multiplication rule for independent events, and classifying a pair
of events).

### Easy

1. A bag contains $4$ white tiles and $9$ black tiles. If one tile is selected at random from the bag, what is the probability that the tile selected is white?
   A) $\frac{4}{13}$  B) $\frac{4}{9}$  C) $\frac{9}{13}$  D) $\frac{5}{13}$

2. A spinner is divided into $12$ equal sections numbered $1$ through $12$. If the spinner is spun once, what is the probability that it lands on a prime number?
   A) $\frac{1}{2}$  B) $\frac{7}{12}$  C) $\frac{5}{12}$  D) $\frac{1}{12}$

3. The table shows how $80$ commuters travel to work. If one commuter from the table is selected at random, what is the probability that the commuter travels by car?

   | | Men | Women | Total |
   |---|---|---|---|
   | Bus | 18 | 12 | 30 |
   | Car | 20 | 15 | 35 |
   | Bike | 7 | 8 | 15 |
   | **Total** | **45** | **35** | **80** |

   A) $\frac{7}{9}$  B) $\frac{7}{16}$  C) $\frac{3}{7}$  D) $\frac{1}{4}$

4. The table shows how $80$ commuters travel to work. If one commuter from the table is selected at random, what is the probability that the commuter is a woman who travels by bike?

   | | Men | Women | Total |
   |---|---|---|---|
   | Bus | 18 | 12 | 30 |
   | Car | 20 | 15 | 35 |
   | Bike | 7 | 8 | 15 |
   | **Total** | **45** | **35** | **80** |

   A) $\frac{8}{35}$  B) $\frac{8}{15}$  C) $\frac{3}{16}$  D) $\frac{1}{10}$

5. A fair six-sided die is rolled once. What is the probability that the die shows a number greater than $4$?
   A) $\frac{1}{3}$  B) $\frac{1}{6}$  C) $\frac{1}{2}$  D) $\frac{2}{3}$

6. A fair six-sided die is rolled once. What is the probability that the die shows a $1$ or a $6$?
   A) $\frac{1}{36}$  B) $\frac{1}{3}$  C) $\frac{1}{6}$  D) $\frac{2}{3}$

7. A box contains $5$ red marbles, $8$ green marbles, and $7$ yellow marbles. If one marble is selected at random from the box, what is the probability that the marble selected is red or yellow?
   A) $\frac{13}{20}$  B) $\frac{1}{4}$  C) $\frac{3}{5}$  D) $\frac{7}{20}$

8. A fair six-sided die is rolled twice. What is the probability that the first roll shows a $2$ and the second roll shows a $5$?
   A) $\frac{1}{12}$  B) $\frac{1}{6}$  C) $\frac{1}{3}$  D) $\frac{1}{36}$

9. A spinner is divided into $4$ equal sections colored red, blue, green, and yellow. The spinner is spun twice. What is the probability that the spinner lands on red both times?
   A) $\frac{1}{8}$  B) $\frac{1}{16}$  C) $\frac{1}{4}$  D) $\frac{1}{2}$

10. A fair six-sided die is rolled once. Let $A$ be the event that the die shows an even number, and let $B$ be the event that the die shows a $5$. Which statement is true?
   A) $A$ and $B$ are mutually exclusive, but not independent.  B) $A$ and $B$ are mutually exclusive and independent.  C) $A$ and $B$ are independent, but not mutually exclusive.  D) $A$ and $B$ are neither mutually exclusive nor independent.

11. Events $A$ and $B$ are mutually exclusive, with $P(A)=0.4$ and $P(B)=0.35$. What is $P(A \text{ or } B)$?
   A) $0.14$  B) $0.60$  C) $0.25$  D) $0.75$

12. A card is selected at random from a standard deck of $52$ playing cards. What is the probability that the card selected is a face card (a jack, queen, or king)?
   A) $\frac{1}{4}$  B) $\frac{4}{13}$  C) $\frac{3}{13}$  D) $\frac{9}{52}$

13. A bag contains $3$ blue marbles and $9$ green marbles. How many blue marbles must be added to the bag so that the probability of selecting a blue marble at random becomes $\frac{1}{2}$?
   A) $6$  B) $3$  C) $9$  D) $12$

14. A bus is late with probability $0.18$. What is the probability that the bus is on time?
   A) $0.18$  B) $0.82$  C) $0.72$  D) $0.28$

15. A fair coin is flipped twice. What is the probability that the coin shows heads on at least one of the two flips?
   A) $\frac{1}{4}$  B) $\frac{1}{2}$  C) $\frac{3}{4}$  D) $1$

### Medium

1. The table shows the membership status of $120$ students at a school. If one junior from the table is selected at random, what is the probability that the junior is a member?

   | | Member | Non-member | Total |
   |---|---|---|---|
   | Juniors | 24 | 36 | 60 |
   | Seniors | 18 | 42 | 60 |
   | **Total** | **42** | **78** | **120** |

   A) $\frac{1}{5}$  B) $\frac{2}{5}$  C) $\frac{4}{7}$  D) $\frac{7}{20}$

2. The table shows the membership status of $120$ students at a school. If one student from the table is selected at random, what is the probability that the student is a senior or a member?

   | | Member | Non-member | Total |
   |---|---|---|---|
   | Juniors | 24 | 36 | 60 |
   | Seniors | 18 | 42 | 60 |
   | **Total** | **42** | **78** | **120** |

   A) $\frac{17}{20}$  B) $\frac{3}{20}$  C) $\frac{1}{2}$  D) $\frac{7}{10}$

3. A fair six-sided die is rolled once. What is the probability that the die shows a factor of $6$ or a prime number?
   A) $\frac{7}{6}$  B) $\frac{1}{3}$  C) $\frac{5}{6}$  D) $\frac{2}{3}$

4. A fair coin is flipped three times. What is the probability that the coin shows exactly two heads?
   A) $\frac{3}{8}$  B) $\frac{1}{8}$  C) $\frac{1}{4}$  D) $\frac{1}{2}$

5. Events $A$ and $B$ are independent, with $P(A)=0.3$ and $P(B)=0.6$. What is $P(A \text{ or } B)$?
   A) $0.18$  B) $0.72$  C) $0.90$  D) $0.42$

6. Events $A$ and $B$ are independent. The probability that a student passes test 1 is $0.7$, and the probability that the same student passes test 2 is $0.8$. Assume the two results are independent. What is the probability that the student passes both tests?
   A) $0.10$  B) $0.94$  C) $0.56$  D) $1.50$

7. Events $A$ and $B$ satisfy $P(A)=0.4$, $P(B)=0.25$, and $P(A \text{ and } B)=0.1$. Which statement is true?
   A) $A$ and $B$ are independent, but not mutually exclusive.  B) $A$ and $B$ are mutually exclusive and independent.  C) $A$ and $B$ are mutually exclusive, but not independent.  D) $A$ and $B$ are neither mutually exclusive nor independent.

8. Events $A$ and $B$ satisfy $P(A)=0.2$, $P(B)=0.5$, and $P(A \text{ or } B)=0.7$. Which statement is true?
   A) $A$ and $B$ are independent, but not mutually exclusive.  B) $A$ and $B$ are mutually exclusive and independent.  C) $A$ and $B$ are neither mutually exclusive nor independent.  D) $A$ and $B$ are mutually exclusive, but not independent.

9. A bag contains $4$ red marbles and $6$ blue marbles. Two marbles are selected at random from the bag, one after the other, without replacement. What is the probability that both marbles selected are red?
   A) $\frac{4}{25}$  B) $\frac{1}{5}$  C) $\frac{2}{15}$  D) $\frac{1}{3}$

10. An integer is selected at random from the integers $1$ through $60$, inclusive. What is the probability that the integer is divisible by $4$ or by $6$?
   A) $\frac{1}{4}$  B) $\frac{1}{3}$  C) $\frac{5}{12}$  D) $\frac{1}{2}$

11. Two fair six-sided dice are rolled. What is the probability that the sum of the two numbers showing is $7$?
   A) $\frac{1}{6}$  B) $\frac{1}{12}$  C) $\frac{7}{36}$  D) $\frac{1}{36}$

12. The table shows the opinions of $120$ people about a new sports drink. If one person from the table who dislikes the drink is selected at random, what is the probability that the person is a teen?

   | | Likes | Dislikes | Total |
   |---|---|---|---|
   | Teens | 46 | 14 | 60 |
   | Adults | 30 | 30 | 60 |
   | **Total** | **76** | **44** | **120** |

   A) $\frac{7}{60}$  B) $\frac{7}{30}$  C) $\frac{11}{30}$  D) $\frac{7}{22}$

13. A fair six-sided die is rolled twice. What is the probability that the die shows a $6$ on at least one of the two rolls?
   A) $\frac{1}{36}$  B) $\frac{11}{36}$  C) $\frac{1}{3}$  D) $\frac{1}{6}$

14. A fair coin is flipped and a fair six-sided die is rolled. What is the probability that the coin shows tails and the die shows a number greater than $4$?
   A) $\frac{1}{12}$  B) $\frac{1}{3}$  C) $\frac{1}{6}$  D) $\frac{1}{2}$

15. A student computes $P(A \text{ or } B)$ for independent events with $P(A)=0.5$ and $P(B)=0.4$ as $0.5+0.4=0.9$. What is the correct value of $P(A \text{ or } B)$?
   A) $0.9$  B) $0.2$  C) $0.45$  D) $0.7$

### Hard

1. The table shows how $150$ employees of a company work. If one employee who works remotely is selected at random, what is the probability that the employee is a designer?

   | | Remote | On-site | Total |
   |---|---|---|---|
   | Engineers | 45 | 30 | 75 |
   | Designers | 25 | 20 | 45 |
   | Managers | 15 | 15 | 30 |
   | **Total** | **85** | **65** | **150** |

   A) $\frac{5}{17}$  B) $\frac{1}{6}$  C) $\frac{5}{9}$  D) $\frac{9}{17}$

2. The table shows how $150$ employees of a company work. If one employee is selected at random, what is the probability that the employee is an engineer or works on-site?

   | | Remote | On-site | Total |
   |---|---|---|---|
   | Engineers | 45 | 30 | 75 |
   | Designers | 25 | 20 | 45 |
   | Managers | 15 | 15 | 30 |
   | **Total** | **85** | **65** | **150** |

   A) $\frac{14}{15}$  B) $\frac{1}{5}$  C) $\frac{1}{2}$  D) $\frac{11}{15}$

3. Events $A$ and $B$ satisfy $P(A)=\frac{3}{8}$, $P(B)=\frac{1}{4}$, and $P(A \text{ or } B)=\frac{1}{2}$. Which statement is true?
   A) $A$ and $B$ are mutually exclusive and independent.  B) $A$ and $B$ are neither mutually exclusive nor independent.  C) $A$ and $B$ are mutually exclusive, but not independent.  D) $A$ and $B$ are independent, but not mutually exclusive.

4. A bag contains $4$ red marbles and $8$ blue marbles. Two marbles are selected at random, one after the other, without replacement. What is the probability that at least one of the two marbles selected is red?
   A) $\frac{5}{9}$  B) $\frac{14}{33}$  C) $\frac{19}{33}$  D) $\frac{1}{3}$

5. A fair coin is flipped four times. What is the probability that the coin shows exactly three heads, or the first flip shows tails?
   A) $\frac{11}{16}$  B) $\frac{3}{4}$  C) $\frac{1}{4}$  D) $\frac{1}{2}$

6. Two fair six-sided dice are rolled. What is the probability that the product of the two numbers showing is even?
   A) $\frac{1}{4}$  B) $\frac{1}{2}$  C) $\frac{3}{4}$  D) $\frac{2}{3}$

7. Events $A$ and $B$ are independent. $P(A)=0.4$ and $P(A \text{ or } B)=0.76$. What is $P(B)$?
   A) $0.36$  B) $0.9$  C) $0.4$  D) $0.6$

8. Events $A$ and $B$ are mutually exclusive, with $P(A)=\frac{x}{12}$, $P(B)=\frac{x}{8}$, and $P(A \text{ or } B)=\frac{5}{12}$. What is the value of $x$?
   A) $1$  B) $2$  C) $3$  D) $4$

9. Events $A$ and $B$ satisfy $P(A)=0.5$, $P(B)=0.3$, and $P(A \text{ and } B)=0.15$. Which statement is true?
   A) $A$ and $B$ are not independent, because the two events overlap.  B) $A$ and $B$ are mutually exclusive, because the two events are unrelated.  C) $A$ and $B$ are independent, because $P(A \text{ and } B)=P(A)\times P(B)$.  D) $A$ and $B$ are neither mutually exclusive nor independent.

10. Two cards are selected at random from a standard deck of $52$ playing cards, one after the other, without replacement. What is the probability that both cards selected are hearts?
   A) $\frac{1}{17}$  B) $\frac{1}{16}$  C) $\frac{1}{13}$  D) $\frac{4}{17}$

11. An integer is selected at random from the integers $1$ through $200$, inclusive. What is the probability that the integer is a multiple of $6$ but not a multiple of $4$?
   A) $\frac{33}{200}$  B) $\frac{17}{200}$  C) $\frac{2}{25}$  D) $\frac{49}{200}$

12. The table shows whether $200$ people own a smartphone and whether they are under $30$ years old. If one person who does not own a smartphone is selected at random, what is the probability that the person is $30$ or older?

   | | Owns a smartphone | No smartphone | Total |
   |---|---|---|---|
   | Under 30 | 70 | 30 | 100 |
   | 30 or older | 60 | 40 | 100 |
   | **Total** | **130** | **70** | **200** |

   A) $\frac{1}{5}$  B) $\frac{2}{5}$  C) $\frac{6}{13}$  D) $\frac{4}{7}$

13. A bag contains $5$ red marbles and $7$ green marbles. Two marbles are selected at random, one after the other, without replacement. Given that the first marble selected is red, what is the probability that the second marble selected is green?
   A) $\frac{7}{11}$  B) $\frac{7}{12}$  C) $\frac{4}{11}$  D) $\frac{5}{11}$

14. A fair six-sided die is rolled twice. What is the probability that the number shown on the second roll is greater than the number shown on the first roll?
   A) $\frac{1}{6}$  B) $\frac{5}{12}$  C) $\frac{7}{12}$  D) $\frac{5}{6}$

15. Events $A$ and $B$ are independent, with $P(A)=0.2$ and $P(B)=0.5$. What is the probability that exactly one of the two events occurs?
   A) $0.1$  B) $0.4$  C) $0.5$  D) $0.6$

**A note on sourcing:** the items above were checked against the method and
distractor style of official SAT Suite Question Bank items in the *Probability and
conditional probability* skill. No College Board question text, numbers or context
is reproduced. Each answer was verified with a script.

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
1. $P(A \text{ and } B)=0$ (even and odd can't both happen) → mutually
   exclusive. $P(A)\times P(B)=\frac14\ne0$ → not independent. **Mutually
   exclusive only.**
2. HT is a valid outcome, so not mutually exclusive. $P(A \text{ and } B)=
   \frac12\times\frac12=\frac14=P(A)\times P(B)$ → independent.
   **Independent only.**
3. Every heart is red, so overlap is nonzero ($\frac{13}{52}$) — not
   mutually exclusive. $P(A)\times P(B)=\frac14\times\frac12=\frac18
   \ne\frac{13}{52}=\frac14$ — not independent either. **Neither.**
4. Different dice — can both happen (not ME). $P(A \text{ and } B)=
   \frac16\times\frac16=P(A)\times P(B)$ → independent. **Independent
   only.**
5. Can't be both suits at once → mutually exclusive, $P(A\text{ and }B)=0$.
   $P(A)\times P(B)=\frac{1}{16}\ne0$ → not independent. **Mutually
   exclusive only.**
6. $P(A)=0$ (impossible event). $P(A \text{ and } B)=0$, which matches
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
   $P(A \text{ and } B)=\frac12\times\frac12=\frac14$.
3. Error — the exact backwards rule: concluded mutually exclusive implies
   independent, when it's the opposite (nonzero-probability mutually
   exclusive events are never independent). Since rolling a 2 and rolling
   a 5 can never happen together, $P(A \text{ and } B)=0$, not
   $\frac{1}{36}$.
4. Error — assumed independence without checking the actual overlap;
   every heart is automatically red, so knowing the card is a heart
   completely determines it's also red. Correct:
   $P(A \text{ and } B)=P(\text{heart})=\frac14$, not $\frac18$.
5. Error — confusing independence with mutual exclusivity in the other
   direction: separate bags make the two draws *independent*, but
   independent events absolutely *can* happen together — that's exactly
   what $P(A \text{ and } B)=P(A)\times P(B)$ computes (a positive number,
   not zero). Independent does not mean "can't happen together"; it means
   "one doesn't affect the other's probability."

**Set 7:** 1) $\frac34$  2) $0.65$ (or $\frac{13}{20}$)  3) $\frac{1}{15}$
4) Mutually exclusive (can't be both $\le3$ and $\ge4$); not independent
(product $\frac14\ne0$); $P(A\text{ or }B)=1$ (every roll is one or the
other — the two events cover the entire sample space). 5) $\frac{3}{25}$

**Set 8 — Easy:** 1) A  2) C  3) B  4) D  5) A  6) B  7) C  8) D  9) B  10) A  11) D  12) C  13) A  14) B  15) C

**Set 8 — Medium:** 1) B  2) D  3) C  4) A  5) B  6) C  7) A  8) D  9) C  10) B  11) A  12) D  13) B  14) C  15) D

**Set 8 — Hard:** 1) A  2) D  3) B  4) C  5) A  6) C  7) D  8) B  9) C  10) A  11) B  12) D  13) A  14) B  15) C
