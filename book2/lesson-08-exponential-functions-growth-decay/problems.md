# Book 2 — Lesson 8: Exponential Functions & Growth/Decay — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by
Python script, not hand-computed. Money/charge/population answers are
rounded to 2 decimal places unless the context naturally gives a whole
number; rounding is noted inline where it matters.

---

## Set 1 — Identify Linear vs. Exponential + State the Rule

For each table ($x=0,1,2,3$), say whether it's linear or exponential, and
give the rule ($y=\ldots$).

1. $y = 5,\ 10,\ 20,\ 40$
2. $y = 3,\ 7,\ 11,\ 15$
3. $y = 100,\ 90,\ 81,\ 72.9$
4. $y = 50,\ 45,\ 40,\ 35$
5. $y = 2,\ 6,\ 18,\ 54$
6. $y = 10,\ 12.5,\ 15,\ 17.5$

## Set 2 — Growth: Build the Equation, Then Evaluate

1. A town's population is $200$ and grows $5\%$ per year. Find the
   population after $4$ years.
2. An investment of $\$1000$ grows $6\%$ per year. Find its value after $3$
   years.
3. A bacteria culture starts at $50$ and doubles every hour. Find the count
   after $5$ hours.
4. A city's population is $8000$ and grows $3\%$ per year. Find the
   population after $2$ years.
5. An item costs $\$20$ and its price increases $10\%$ per year. Find the
   price after $3$ years.
6. A quantity starts at $12$ and grows by a factor of $1.5$ each step. Find
   its value after $4$ steps.

## Set 3 — Decay: Build the Equation, Then Evaluate

1. A car worth $\$15000$ depreciates $12\%$ per year. Find its value after
   $3$ years.
2. A $200$ g sample decreases $8\%$ per year. Find the amount after $2$
   years.
3. A population of $5000$ declines $4\%$ per year. Find the population
   after $5$ years.
4. $100$ mg of medication decreases $25\%$ every hour. Find the amount
   after $3$ hours.
5. An $800$ L tank loses $10\%$ of its water each day. Find the amount
   after $2$ days.
6. A $\$2000$ value decreases by a factor of $0.8$ each year. Find the
   value after $3$ years.

## Set 4 — Mixed: Discriminate, Then Evaluate

For each, first decide linear or exponential, then evaluate.

1. A plant grows $3$ cm every week, starting at $10$ cm. Height after $6$
   weeks?
2. A savings account earns $4\%$ interest per year, starting at $\$500$.
   Value after $3$ years?
3. A phone loses $15\%$ of its charge every hour, starting at $100\%$.
   Charge after $2$ hours?
4. A pool drains at a constant rate of $50$ liters per minute, starting
   with $2000$ liters. Amount after $10$ minutes?
5. Bacteria triple every day, starting with $4$. Count after $4$ days?
6. A runner's distance increases by $2$ miles every day, starting at $1$
   mile. Distance after $5$ days?

## Set 5 — Half-Life

1. $160$ g of a substance has a half-life of $4$ years. How much remains
   after $12$ years?
2. $500$ mg of a drug has a half-life of $6$ hours. How much remains after
   $18$ hours?
3. $80$ g of an isotope has a half-life of $10$ days. How much remains
   after $30$ days?
4. A population halves every $5$ years, starting at $6400$. Find the
   population after $20$ years.
5. $1000$ bacteria die off such that the count halves every $3$ hours. Find
   the count after $9$ hours.

## Set 6 — Spot the Error

1. A city grows $7\%$ per year, starting at $10000$. Find the population
   after $2$ years — *"$10000\times(1.7)^2=28900$."*
2. A sample decreases $20\%$ per year, starting at $500$. Find the amount
   after $2$ years — *"$500\times(1+0.2)^2=720$."*
3. A table shows $y=2,4,8,16$ for $x=0,1,2,3$. A student claims: *"This is
   linear with common difference $2$, so $y=2+2x$."*
4. A car depreciates at a constant rate of $\$1500$ per year, starting at
   $\$20000$. A student claims: *"This is exponential:
   $y=20000\times(1-0.075)^t$."*
5. Find the amount remaining after $3$ half-lives, starting at $240$ g —
   *"$240 - 3\times\frac{1}{2}\times240 = 240-360=-120$."*

## Set 7 — Bonus / Challenge (work backward)

1. A population grows from $200$ to $242$ in $2$ years at a constant
   annual percent rate. Find the rate.
2. A substance decays to $\frac14$ of its original amount after $10$ days.
   Find its half-life.
3. An investment grows from $\$1000$ to $\$1331$ in $3$ years at a constant
   annual rate. Find the rate.
4. A car worth $\$25000$ depreciates to $\$20000$ after $1$ year at a
   constant percent rate. Find the rate, then predict the value after a
   total of $2$ years.
5. A quantity grows from $3$ to $48$ over $4$ equal steps. Is this linear
   or exponential? Find the rule.

---

## Answer Key

**Set 1:**
1. Exponential, $y=5\times2^x$
2. Linear, $y=3+4x$
3. Exponential, $y=100\times0.9^x$
4. Linear, $y=50-5x$
5. Exponential, $y=2\times3^x$
6. Linear, $y=10+2.5x$

**Set 2:** 1) $\approx243$  2) $\approx\$1191.02$  3) $1600$  4) $\approx8487$  5) $\approx\$26.62$  6) $60.75$

**Set 3:** 1) $\approx\$10222.08$  2) $\approx169.28$ g  3) $\approx4077$  4) $\approx42.19$ mg  5) $648$ L  6) $\$1024$

**Set 4:**
1. Linear, $28$ cm
2. Exponential, $\approx\$562.43$
3. Exponential, $\approx72.25\%$
4. Linear, $1500$ L
5. Exponential, $324$
6. Linear, $11$ miles

**Set 5:** 1) $20$ g  2) $62.5$ mg  3) $10$ g  4) $400$  5) $125$

**Set 6:**
1. Error — $7\%$ was treated as $1.7$ instead of $1.07$ (misplaced the
   decimal in the growth factor). Correct: $10000\times1.07^2\approx11449$.
2. Error — used the growth form $(1+r)$ for a decaying quantity instead of
   $(1-r)$. Correct: $500\times0.8^2=320$.
3. Error — the differences $2,4,8$ are NOT constant, so it isn't linear;
   the ratios $2,2,2$ ARE constant, so it's exponential. Correct:
   $y=2\times2^x$.
4. Error — a constant DOLLAR amount per year ($\$1500$) is linear, not
   exponential, regardless of the word "rate." Correct: $y=20000-1500t$.
5. Error — treated repeated halving as repeated subtraction (additive)
   instead of repeated multiplication (multiplicative) — the negative
   result itself is a giveaway something's wrong, since an amount can
   never go below zero this way. Correct: $240\times(\frac12)^3=30$ g.

**Set 7:**
1. $r=10\%$
2. $h=5$ days
3. $r=10\%$
4. $r=20\%$; after $2$ years, $\$16000$
5. Exponential, $y=3\times2^x$
