# Mock Test 7 — Source of truth (Book 3, ≈800)

All 44 problems are original. Math is written in LaTeX (`$...$`), money as `\$`, percent as `\%`.
`\dsp{...}` = centered display line. Figures/tables are raw LaTeX in a ```latex block.
Solutions are for the author only; they are not printed in the book.
Domains: ALG = Algebra, ADV = Advanced Math, PSDA = Problem-Solving and Data Analysis, GT = Geometry and Trigonometry.
Difficulty: E / M / H. Type: MC or GRID.

# MODULE 1 (22 questions; Easy Q1–8, Medium Q9–19, Hard Q20–22)

## M1-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: A diner charges \$8.50 for the lunch special plus \$1.25 for each extra topping. Ravi paid \$13.50 for a lunch special with extra toppings and nothing else. How many extra toppings did he order?
- A: $5$
- B: $10.8$
- C: $4$
- D: $17.6$
- Answer: C
- Solution: $8.50+1.25t=13.50$, so $1.25t=5$ and $t=4$ (5 forgets to divide by 1.25; 10.8 forgets the \$8.50 base price; 17.6 adds the base price instead of subtracting).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $(2x+5)^2$?
- A: $4x^2+20x+25$
- B: $4x^2+25$
- C: $4x^2+10x+25$
- D: $2x^2+20x+25$
- Answer: A
- Solution: $(2x)^2+2(2x)(5)+25=4x^2+20x+25$ (B drops the middle term; C halves it; D forgets to square the 2).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: A restaurant sold 480 pizzas last week, and $\frac{3}{8}$ of them were pepperoni. How many of the pizzas sold were not pepperoni?
- Answer: 300
- Solution: $\frac{5}{8}\cdot480=300$ (the pepperoni pizzas number 180).

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A circle has a circumference of $14\pi$. What is the area of the circle?
- A: $7\pi$
- B: $98\pi$
- C: $196\pi$
- D: $49\pi$
- Answer: D
- Solution: $2\pi r=14\pi$ gives $r=7$, so $A=49\pi$ (7π is the radius; 196π treats 14 as the radius; 98π multiplies the circumference by the radius).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: In the $xy$-plane, a line passes through the points $(1,4)$ and $(5,12)$. What is the slope of the line?
- A: $\frac{1}{2}$
- B: $2$
- C: $4$
- D: $8$
- Answer: B
- Solution: $\frac{12-4}{5-1}=2$ ($\frac12$ inverts the ratio; 8 and 4 use only the rise or only the run).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The functions $f$ and $g$ are defined by $f(x)=x+3$ and $g(x)=x^2$. What is the value of $f(g(4))$?
- A: $19$
- B: $49$
- C: $16$
- D: $7$
- Answer: A
- Solution: $g(4)=16$ and $f(16)=19$ (49 is $g(f(4))$, the composition in the wrong order; 16 is only $g(4)$; 7 is only $f(4)$).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: The length of a rectangular stage is 3 meters more than twice its width. The perimeter of the stage is 36 meters. What is the width, in meters, of the stage?
- Answer: 5
- Solution: $\ell=2w+3$ and $\ell+w=18$, so $3w+3=18$ and $w=5$.

## M1-Q8
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $(3x^2y)(4xy^3)$?
- A: $12x^2y^3$
- B: $7x^3y^4$
- C: $12x^3y^4$
- D: $12x^3y^3$
- Answer: C
- Solution: Multiply the coefficients and add the exponents: $12x^{2+1}y^{1+3}=12x^3y^4$ (A multiplies the exponents; B adds the coefficients; D drops one power of $y$).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A city planner surveyed two independent random samples of residents about a proposed bike lane. Sample 1 estimated that 52\% of all residents support the lane, with a margin of error of 4 percentage points. Sample 2 estimated that 47\% support it, with a margin of error of 3 percentage points. Which of the following is the most appropriate conclusion?
- A: The percent of all residents who support the bike lane is exactly 49\%.
- B: Sample 1 is more reliable than Sample 2 because its estimate is greater.
- C: At least one of the samples was not random, because the two estimates are different.
- D: It is plausible that between 48\% and 50\% of all residents support the bike lane.
- Answer: D
- Solution: The plausible values are 48\% to 56\% from Sample 1 and 44\% to 50\% from Sample 2; values consistent with both are 48\% to 50\%. (Margins of error never pin down an exact value; different estimates are expected from different random samples; a larger estimate says nothing about reliability.)

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: At a restaurant, every entr\'ee costs \$9 more than every side dish. A table orders 3 entr\'ees and 4 side dishes for \$65.50 before tax. What is the price of one side dish?
- A: $\$9.36$
- B: $\$5.50$
- C: $\$13.21$
- D: $\$14.50$
- Answer: B
- Solution: $3(s+9)+4s=65.50$ gives $7s=38.50$, so $s=5.50$ (9.36 divides 65.50 by 7 and ignores the \$9 difference; 14.50 is the entr\'ee price; 13.21 subtracts \$9 instead of adding).

## M1-Q11
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The polynomial $p(x)=x^3-4x^2-11x+30$ has $x=2$ as a zero. What is the greatest zero of $p$?
- Answer: 5
- Solution: $p(x)=(x-2)(x^2-2x-15)=(x-2)(x-5)(x+3)$, so the zeros are $2$, $5$, $-3$.

## M1-Q12
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A running track encloses a region made of a rectangle that is 30 meters long and 14 meters wide, with a semicircle attached to each of the two 14-meter ends, as shown. What is the area, in square meters, of the region enclosed by the track?
- Figure:
```latex
\begin{tikzpicture}[scale=0.14]
\draw[line width=0.7pt] (0,0)--(30,0) arc(-90:90:7)--(0,14) arc(90:270:7)--cycle;
\draw[line width=0.5pt,dashed] (0,0)--(0,14); \draw[line width=0.5pt,dashed] (30,0)--(30,14);
\node[font=\small] at (15,-2.2) {30};
\node[font=\small] at (31.8,7) {14};
\end{tikzpicture}
```
- A: $420+14\pi$
- B: $420+\frac{49}{2}\pi$
- C: $420+49\pi$
- D: $420+196\pi$
- Answer: C
- Solution: The two semicircles of radius 7 make one circle: $420+\pi(7)^2=420+49\pi$ (B counts one semicircle; D uses the diameter 14 as the radius; 14π is the circumference of the circle).

## M1-Q13
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A 20-question quiz awards 5 points for each correct answer and subtracts 2 points for each incorrect answer. Dana answered all 20 questions and needs at least 58 points. What is the least number of questions she must answer correctly?
- A: $14$
- B: $9$
- C: $12$
- D: $20$
- Answer: A
- Solution: $5c-2(20-c)\ge58$ gives $7c\ge98$ and $c\ge14$ (12 ignores the penalty, $5c\ge58$; 9 uses $7c\ge58$ and forgets the 40; 20 uses $5c-2c\ge58$).

## M1-Q14
- Domain: PSDA
- Difficulty: M
- Type: GRID
- Stem: A museum builds a scale model of the Sun and Earth using one scale for all sizes. In the model, Earth, whose diameter is 12,800 kilometers, is a sphere 4 centimeters in diameter. The Sun's diameter is 1,392,000 kilometers. What is the diameter, in meters, of the model Sun?
- Answer: 4.35
- Solution: The Sun is $\frac{1{,}392{,}000}{12{,}800}=108.75$ times Earth's diameter, so the model Sun is $108.75\cdot4=435$ cm $=4.35$ m (435 is in centimeters).

## M1-Q15
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Two streaming services opened in the same month. After $t$ months, Service A has $A(t)=800+60t$ thousand subscribers and Service B has $B(t)=500(1.12)^{t}$ thousand subscribers. For the least whole number of months $t$ for which $B(t)>A(t)$, what is the value of $t$?
- A: $8$
- B: $10$
- C: $13$
- D: $9$
- Answer: D
- Solution: $t=8$: $B\approx1238<1280=A$. $t=9$: $B\approx1386.5>1340=A$. So $t=9$ (8 is the nearest miss; 10 and 13 are later months, when $B$ is already ahead).

## M1-Q16
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A candle burns at a constant rate. The graph of its height $h$, in centimeters, $t$ hours after it was lit passes through the points $(2,21)$ and $(6,15)$. Which of the following is the best interpretation of the $t$-intercept of the graph?
- A: The candle was 24 centimeters tall when it was lit.
- B: The candle burns completely 16 hours after it was lit.
- C: The candle burns 1.5 centimeters every hour.
- D: The candle is 16 centimeters tall after 24 hours.
- Answer: B
- Solution: The slope is $-1.5$, so $h=24-1.5t$; $h=0$ at $t=16$ (A is the $h$-intercept; C is the slope; D swaps the two intercepts).

## M1-Q17
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: A cubic polynomial $p$ has a negative leading coefficient. Its graph crosses the $x$-axis at $x=-1$ and touches the $x$-axis at $x=2$ without crossing it. Which of the following could define $p(x)$?
- A: $-(x+1)^2(x-2)$
- B: $(x+1)(x-2)^2$
- C: $-(x+1)(x-2)^2$
- D: $-(x-1)(x+2)^2$
- Answer: C
- Solution: A squared factor gives a touch point, so $(x-2)^2$ and a single $(x+1)$; the negative sign gives the negative leading coefficient (A touches at $-1$; B has a positive leading coefficient; D has zeros $1$ and $-2$).

## M1-Q18
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A restaurant adds an 8\% sales tax and a 15\% service charge to the food total, both computed on the food total. A party's final bill was \$61.50. What was the food total, in dollars?
- Answer: 50
- Solution: $f(1+0.08+0.15)=1.23f=61.50$, so $f=50$.

## M1-Q19
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following functions has the greatest maximum value?
- A: $p(x)=-(x-1)(x+5)$
- B: $q(x)=-3(x-1)^2+4$
- C: $r(x)=-x^2+6x-2$
- D: $s(x)=-\frac{1}{2}x^2+2x+6$
- Answer: A
- Solution: Maxima: $p$ at $x=-2$ gives $9$; $q$ gives $4$; $r$ at $x=3$ gives $7$; $s$ at $x=2$ gives $8$. The greatest is $9$ (B reads the 4 in vertex form as a maximum without comparing; the factored form hides its vertex).

## M1-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The quadratic function $f$ has a maximum value of 19. The graph of $y=f(x)$ in the $xy$-plane passes through the points $(1,10)$ and $(7,10)$. What is the value of $f(-1)$?
- A: $6$
- B: $14$
- C: $44$
- D: $-6$
- Answer: D
- Solution: The axis of symmetry is $x=4$, so $f(x)=a(x-4)^2+19$ and $9a+19=10$ gives $a=-1$. Then $f(-1)=-25+19=-6$ (44 uses $a=+1$; 14 subtracts the distance 5 without squaring; 6 loses the sign).

## M1-Q21
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: A restaurant sells 120 lunch specials per day at a price of $p$ dollars each. When it raises the price by \$1.50, it sells 15 fewer lunch specials per day, and the daily revenue from lunch specials stays exactly the same. What is the daily revenue, in dollars, from lunch specials?
- Answer: 1260
- Solution: $120p=(p+1.5)(105)$ gives $15p=157.5$, $p=10.5$; revenue $=120(10.5)=1260$ (10.5 is the price, not the revenue).

## M1-Q22
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: For $0<x<20$, the equation below is true.\dsp{$\sin\left((4x+7)^{\circ}\right)=\cos\left((2x-1)^{\circ}\right)$}What is the value of $x$?
- A: $29$
- B: $14$
- C: $41$
- D: $84$
- Answer: B
- Solution: $\sin\theta=\cos\varphi$ when $\theta+\varphi=90$, so $6x+6=90$ and $x=14$ (29 uses a sum of $180^{\circ}$; 41 is the other solution of the sine equation, but it is outside $0<x<20$; 84 forgets to divide by 6).

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $5-2x=3x-15$, what is the value of $x$?
- A: $-10$
- B: $4$
- C: $-2$
- D: $20$
- Answer: B
- Solution: $20=5x$, so $x=4$ ($-2$ subtracts 15 from 5; $-10$ moves $3x$ with the wrong sign; 20 forgets to divide by 5).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $f$ is defined by $f(x)=x^2-3x+5$. What is the value of $f(-2)$?
- A: $3$
- B: $7$
- C: $-5$
- D: $15$
- Answer: D
- Solution: $4+6+5=15$ (3 uses $-6$ for $-3x$; 7 squares as $-4$; $-5$ does both).

## M2-Q3
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: On an excavation plan, 1 centimeter represents 0.5 meter. A rectangular trench appears on the plan as 6 centimeters by 4.5 centimeters. What is the actual area, in square meters, of the trench?
- A: $6.75$
- B: $10.5$
- C: $13.5$
- D: $27$
- Answer: A
- Solution: The trench is $3\text{ m}\times2.25\text{ m}=6.75\text{ m}^2$ (areas scale by the square of 0.5; 13.5 scales the area by 0.5 only; 27 is the plan area; 10.5 is the real perimeter).

## M2-Q4
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: The graph of $5x+ky=20$ in the $xy$-plane, where $k$ is a constant, passes through the point $(2,5)$. What is the $y$-coordinate of the $y$-intercept of the graph?
- Answer: 10
- Solution: $10+5k=20$ gives $k=2$; then $2y=20$ at $x=0$, so $y=10$.

## M2-Q5
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The graph of the quadratic function $f$ in the $xy$-plane opens upward, has its vertex at $(3,-4)$, and passes through the point $(5,4)$. Which of the following defines $f$?
- A: $2(x+3)^2-4$
- B: $4(x-3)^2-4$
- C: $2(x-3)^2-4$
- D: $2(x-3)^2+4$
- Answer: C
- Solution: $f(x)=a(x-3)^2-4$ and $f(5)=4a-4=4$ gives $a=2$ (A flips the sign of $h$; B forgets to square the 2 and uses $2a=8$; D flips the sign of $k$).

## M2-Q6
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: Triangles $X$, $Y$, and $Z$ are similar. Every side of $Y$ is 3 times as long as the corresponding side of $X$, and every side of $Z$ is $\frac{2}{3}$ as long as the corresponding side of $Y$. The area of triangle $Z$ is 100 square units. What is the area of triangle $X$?
- A: $50$
- B: $200$
- C: $400$
- D: $25$
- Answer: D
- Solution: Each side of $Z$ is $3\cdot\frac23=2$ times the side of $X$, so the area of $Z$ is 4 times the area of $X$: $100/4=25$ (50 uses the side ratio as the area ratio; 200 and 400 invert the direction).

## M2-Q7
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: If $3x+5y=17$ and $2x-y=7$, what is the value of $5x+4y$?
- A: $24$
- B: $7$
- C: $10$
- D: $17$
- Answer: A
- Solution: Add the equations: $5x+4y=17+7=24$ (no need to solve; $x=4$, $y=1$; 17 and 7 are given right sides; 10 subtracts them).

## M2-Q8
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The function $f$ is defined by $f(x)=a\cdot b^{x}$, where $a$ and $b$ are positive constants. If $f(1)=12$ and $f(3)=48$, what is the value of $f(0)$?
- Answer: 6
- Solution: $f(3)/f(1)=b^2=4$, so $b=2$ and $a=6$; $f(0)=a=6$.

## M2-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The table shows two data sets, $P$ and $Q$, each with six values. Which of the following statements is true?
- Figure:
```latex
\begin{tabular}{|l|c|c|c|c|c|c|}
\hline
Set $P$ & 8 & 8 & 8 & 14 & 14 & 14\\\hline
Set $Q$ & 8 & 9 & 10 & 12 & 13 & 14\\\hline
\end{tabular}
```
- A: The two sets have the same mean and the same median, and Set $Q$ has the greater standard deviation.
- B: The two sets have the same mean and the same median, and Set $P$ has the greater standard deviation.
- C: The two sets have the same mean, but Set $P$ has the greater median.
- D: The two sets have the same median, but Set $Q$ has the greater mean.
- Answer: B
- Solution: Both means are 11 and both medians are 11. The values of $P$ sit farther from 11 (SD $=3$ versus about $2.16$), so $P$ has the greater standard deviation.

## M2-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A glass supplier accepts a pane if its thickness $t$, in millimeters, satisfies $|t-6.4|\le0.15$. What is the difference, in millimeters, between the greatest and the least acceptable thickness?
- A: $0.15$
- B: $6.25$
- C: $0.30$
- D: $6.55$
- Answer: C
- Solution: The acceptable thicknesses run from $6.25$ to $6.55$, a spread of $0.30$ (0.15 is only the half-width; 6.25 and 6.55 are the endpoints).

## M2-Q11
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: For all values of $x$, $(x+3)(x^2-2x+k)=x^3+x^2-2x+c$, where $k$ and $c$ are constants. What is the value of $c$?
- Answer: 12
- Solution: Expanding gives $x^3+x^2+(k-6)x+3k$. Matching the $x$-terms, $k-6=-2$ so $k=4$, and $c=3k=12$.

## M2-Q12
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A survey drone's height above an archaeological site, in meters, $t$ minutes after launch is $h=40+12t$. What is the height of the drone, in meters, 150 seconds after launch?
- A: $58$
- B: $70$
- C: $190$
- D: $1{,}840$
- Answer: B
- Solution: 150 seconds is 2.5 minutes, so $h=40+30=70$ (58 uses $t=1.5$; 190 adds 150; 1,840 uses $t=150$ minutes).

## M2-Q13
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: Kepler's third law states that for planets orbiting the same star, the square of a planet's orbital period is proportional to the cube of its average distance from the star. Planet $Y$ has an orbital period 8 times that of Planet $X$. Assume both planets move in circular orbits at constant speeds. Planet $Y$'s orbital speed is how many times Planet $X$'s orbital speed?
- A: $\frac{1}{2}$
- B: $\frac{1}{8}$
- C: $2$
- D: $4$
- Answer: A
- Solution: $P^2\propto a^3$ gives $64=(a_Y/a_X)^3$, so $a_Y=4a_X$. Speed $=\frac{2\pi a}{P}$, so the ratio is $\frac{4}{8}=\frac12$ (4 is the distance ratio alone; $\frac18$ is the period ratio inverted; 2 inverts the final ratio).

## M2-Q14
- Domain: PSDA
- Difficulty: H
- Type: GRID
- Stem: An archaeologist counted the pottery fragments in each of five trenches. Each count is a positive integer, the mean of the five counts is 14, and the median is 12. What is the greatest possible number of fragments in the trench with the most fragments?
- Answer: 44
- Solution: Order the counts $a\le b\le12\le d\le e$ with sum 70. To make $e$ largest, make the others as small as allowed: $a=b=1$ and $d=12$ (not 13: the median only forces $d\ge12$). Then $e=70-1-1-12-12=44$.

## M2-Q15
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: For how many integer values of $k$ does the equation $(k-3)x=12$ have an integer solution $x$?
- A: $6$
- B: $11$
- C: $13$
- D: $12$
- Answer: D
- Solution: $x=\frac{12}{k-3}$ is an integer exactly when $k-3$ is a divisor of 12, positive or negative: $\pm1,\pm2,\pm3,\pm4,\pm6,\pm12$, which is 12 values (6 counts only positive divisors; 13 counts $k=3$, which gives $0=12$, no solution; 11 drops one divisor).

## M2-Q16
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The table gives four values of the quadratic function $f$. The function $g$ is defined by $g(x)=f(2x-1)+8$. What is the greatest value of $x$ for which $g(x)=0$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|c|}
\hline
$x$ & 0 & 1 & 3 & 5\\\hline
$f(x)$ & $-5$ & $-8$ & $-8$ & 0\\\hline
\end{tabular}
```
- A: $1$
- B: $3$
- C: $2$
- D: $7$
- Answer: C
- Solution: $g(x)=0$ means $f(2x-1)=-8$. A quadratic takes the value $-8$ at most twice, and the table shows $f(1)=f(3)=-8$, so $2x-1=1$ or $3$, giving $x=1$ or $x=2$. The greatest is 2 (3 is the largest input $u$ itself, or ignores the $+8$; 1 is the smaller solution; 7 solves $x=2u+1$, the inverse of the wrong direction).

## M2-Q17
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the circle with equation $x^2+y^2-4x+6y-212=0$ and the point $P(26,4)$ are given. The two lines through $P$ that are tangent to the circle touch it at points $T_1$ and $T_2$. What is the length of $\overline{T_1T_2}$?
- A: $12$
- B: $24$
- C: $20$
- D: $30$
- Answer: B
- Solution: Completing the squares: $(x-2)^2+(y+3)^2=225$, center $O(2,-3)$, $r=15$. $OP=\sqrt{24^2+7^2}=25$, so the tangent length is $\sqrt{625-225}=20$. In right triangle $OT_1P$ the altitude from $T_1$ to $OP$ is $\frac{15\cdot20}{25}=12$, and $T_1T_2$ is twice that: 24 (12 is half the chord; 20 is the tangent length $PT_1$; 30 is the diameter).

## M2-Q18
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: What is the sum of all real solutions of the equation $x^{2/3}-5x^{1/3}+6=0$?
- Answer: 35
- Solution: Let $u=x^{1/3}$: $u^2-5u+6=0$, so $u=2$ or $3$ and $x=u^3=8$ or $27$. The sum is 35 (5 is the sum of the $u$-values, not of $x$).

## M2-Q19
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: Two cell towers are located at mile markers 4 and 10 along a straight highway. A driver at mile marker $x$ has a combined distance to the two towers that is less than 10 miles. For how many integer values of $x$ is this possible?
- A: $7$
- B: $11$
- C: $13$
- D: $9$
- Answer: D
- Solution: $|x-4|+|x-10|<10$. Between the towers the sum is 6; beyond a tower it grows by 2 per mile, so the sum equals 10 at $x=2$ and $x=12$. Thus $2<x<12$ and $x=3,\dots,11$: 9 values (7 only counts markers between the towers; 11 uses $\le$; 13 requires each distance to be less than 10 separately).

## M2-Q20
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, lines $\ell$ and $n$ are perpendicular and intersect at the point $(2,5)$. The $y$-intercept of $n$ is 5 greater than the $y$-intercept of $\ell$. If the slope of $\ell$ is positive and greater than 1, what is the slope of $\ell$?
- A: $-\frac{1}{2}$
- B: $\frac{1}{2}$
- C: $2$
- D: $5$
- Answer: C
- Solution: $\ell$: $y=m(x-2)+5$ has intercept $5-2m$; $n$ has slope $-\frac1m$ and intercept $5+\frac2m$. Then $\frac2m+2m=5$, so $2m^2-5m+2=0$ and $m=2$ or $\frac12$; only $2$ exceeds 1 ($\frac12$ is the other root; $-\frac12$ is the slope of $n$; 5 is the intercept difference).

## M2-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: In the figure, triangle $ABC$ has a right angle at $C$, with $CA=8$ and $CB=6$. Semicircles are drawn outward on legs $\overline{CA}$ and $\overline{CB}$, and the circle with diameter $\overline{AB}$ is drawn through $C$. The two shaded crescents lie inside the semicircles but outside the large circle. What is the total area of the two shaded regions?
- Figure:
```latex
\begin{tikzpicture}[scale=0.38]
\coordinate (C) at (0,0); \coordinate (A) at (8,0); \coordinate (B) at (0,6);
\fill[badge] (0,0) arc(180:360:4)--cycle;
\fill[badge] (0,6) arc(90:270:3)--cycle;
\fill[white] (4,3) circle (5);
\draw[line width=0.6pt] (0,0) arc(180:360:4);
\draw[line width=0.6pt] (0,6) arc(90:270:3);
\draw[line width=0.6pt] (4,3) circle (5);
\draw[line width=0.8pt] (C)--(A)--(B)--cycle;
\draw[line width=0.5pt] (0,0.7)--(0.7,0.7)--(0.7,0);
\node[font=\small] at (-0.6,-0.5) {$C$}; \node[right,font=\small] at (A) {$A$}; \node[above,font=\small] at (B) {$B$};
\node[above,font=\small] at (4,0) {8}; \node[right,font=\small] at (0,3) {6};
\end{tikzpicture}
```
- Answer: 24
- Solution: Area of the two leg semicircles $=\frac{\pi}{8}(8^2+6^2)=12.5\pi$, which equals the semicircle on the hypotenuse ($\frac{\pi}{8}\cdot10^2$). The crescents are (leg semicircles) $-$ (the parts of the large circle outside the triangle) $=$ (leg semicircles) $+$ triangle $-$ (large semicircle) $=$ the triangle: $\frac12(8)(6)=24$.

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: For how many integer values of $p$ does the equation $x^2-px+24=0$ have two integer solutions?
- A: $8$
- B: $4$
- C: $16$
- D: $12$
- Answer: A
- Solution: The solutions $r,s$ are integers with $rs=24$ and $p=r+s$. The factor pairs $(1,24),(2,12),(3,8),(4,6)$ and their negatives give $p=\pm25,\pm14,\pm11,\pm10$: 8 values (4 forgets the negative pairs; 16 counts each value of $r$ separately, i.e. ordered pairs of both signs).
