# Mock Test 1 — Source of truth (Book 3, ≈800)

All 44 problems are original. Math is written in LaTeX (`$...$`), money as `\$`, percent as `\%`.
`\dsp{...}` = centered display line. Figures/tables are raw LaTeX in a ```latex block.
Solutions are for the author only; they are not printed in the book.
Domains: ALG = Algebra, ADV = Advanced Math, PSDA = Problem-Solving and Data Analysis, GT = Geometry and Trigonometry.
Difficulty: E / M / H. Type: MC or GRID.

# MODULE 1 (22 questions; Easy Q1–7, Medium Q8–17, Hard Q18–22)

## M1-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $3(x-4)=15$, what is the value of $x+4$?
- A: $5$
- B: $9$
- C: $13$
- D: $19$
- Answer: C
- Solution: $x-4=5$, $x=9$, so $x+4=13$.

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $f$ is defined by $f(x)=2x^2-3x+5$. What is the value of $f(-3)$?
- A: $-4$
- B: $14$
- C: $23$
- D: $32$
- Answer: D
- Solution: $2(9)-3(-3)+5=18+9+5=32$.

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: MC
- Stem: The mean of five quiz scores is 88. Four of the scores are 90, 85, 92, and 95. What is the fifth score?
- A: $78$
- B: $82$
- C: $85$
- D: $88$
- Answer: A
- Solution: Total $=5\cdot88=440$; $440-(90+85+92+95)=440-362=78$.

## M1-Q4
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: A tutoring center charges a one-time registration fee of \$24 plus \$18 per session. Sofia paid a total of \$168. How many sessions did she pay for?
- Answer: 8
- Solution: $24+18s=168 \Rightarrow s=144/18=8$.

## M1-Q5
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A rectangle has a width of 7 centimeters and a diagonal of 25 centimeters. What is the perimeter of the rectangle, in centimeters?
- A: $31$
- B: $62$
- C: $168$
- D: $175$
- Answer: B
- Solution: Length $=\sqrt{25^2-7^2}=24$; perimeter $=2(7+24)=62$.

## M1-Q6
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $x+y=14$ and $x-y=4$, what is the value of $xy$?
- A: $45$
- B: $56$
- C: $63$
- D: $70$
- Answer: A
- Solution: Add: $2x=18$, $x=9$, $y=5$, $xy=45$.

## M1-Q7
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: What is the positive solution to the equation below?\dsp{$x^2-3x-28=0$}
- A: $-4$
- B: $3$
- C: $4$
- D: $7$
- Answer: D
- Solution: $(x-7)(x+4)=0$, positive root $7$.

## M1-Q8
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A school sold two kinds of tickets to a play. Adult tickets cost \$9 each and student tickets cost \$5 each. A total of 240 tickets were sold for \$1,720. How many student tickets were sold?
- A: $110$
- B: $120$
- C: $130$
- D: $150$
- Answer: A
- Solution: $a+s=240$, $9a+5s=1720$; $2160-4s=1720 \Rightarrow s=110$ (130 are adult tickets).

## M1-Q9
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: A juice stand's daily profit, in dollars, from selling $x$ cups of juice is modeled by $P(x)=-0.05x^2+6x-40$. According to the model, what is the maximum possible daily profit, in dollars?
- Answer: 140
- Solution: Vertex at $x=-6/(2(-0.05))=60$; $P(60)=-180+360-40=140$.

## M1-Q10
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The price of a jacket was increased by 20\%. A week later, the new price was reduced by 15\%, and the final price was \$76.50. What was the price of the jacket before the increase?
- A: \$72.86
- B: \$75.00
- C: \$78.03
- D: \$90.00
- Answer: B
- Solution: Net factor $1.2\cdot0.85=1.02$; $76.50/1.02=75$.

## M1-Q11
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the $xy$-plane, a line passes through the points $(-2,7)$ and $(4,-5)$. What is the $x$-coordinate of the point where the line crosses the $x$-axis?
- A: $-\frac{3}{2}$
- B: $\frac{2}{3}$
- C: $\frac{3}{2}$
- D: $3$
- Answer: C
- Solution: Slope $-2$, $y=-2x+3$; $y=0 \Rightarrow x=3/2$ (3 is the $y$-intercept).

## M1-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: For positive $x$ and $y$, which expression is equivalent to $\dfrac{(4x^3y)^2}{2xy^2}$?
- A: $2x^5$
- B: $8x^7$
- C: $4x^5$
- D: $8x^5$
- Answer: D
- Solution: $16x^6y^2/(2xy^2)=8x^5$.

## M1-Q13
- Domain: GT
- Difficulty: M
- Type: GRID
- Stem: In right triangle $ABC$, the right angle is at $B$, $\tan A=5/12$, and $AC=39$. What is the perimeter of triangle $ABC$?
- Answer: 90
- Solution: Sides are $5k,12k,13k$ with $13k=39$, $k=3$; perimeter $=30k=90$.

## M1-Q14
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The table shows how the 200 students in the junior and senior classes at a school usually travel to school. One student who drives is selected at random. What is the probability that the student is a senior?
- Figure:
```latex
\begin{tabular}{|l|c|c|c|}
\hline
 & Walk & Bus & Drive\\\hline
Juniors & 36 & 44 & 25\\\hline
Seniors & 24 & 31 & 40\\\hline
\end{tabular}
```
- A: $\frac{1}{5}$
- B: $\frac{13}{40}$
- C: $\frac{8}{19}$
- D: $\frac{8}{13}$
- Answer: D
- Solution: Drivers $=25+40=65$; seniors among them $40$; $40/65=8/13$.

## M1-Q15
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A freight elevator can safely carry at most 900 pounds. A worker who weighs 175 pounds rides the elevator with a cart that weighs 60 pounds and is loaded with identical boxes that weigh 35 pounds each. What is the greatest number of boxes that can be on the cart without going over the limit?
- A: $18$
- B: $19$
- C: $20$
- D: $25$
- Answer: B
- Solution: $175+60+35n\le900 \Rightarrow n\le19$ (20 and 25 come from ignoring the cart or the worker).

## M1-Q16
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: What is the sum of all solutions to the equation $\sqrt{3x+10}=x+2$?
- A: $-3$
- B: $-1$
- C: $2$
- D: $5$
- Answer: C
- Solution: Square: $x^2+x-6=0$, $x=2$ or $-3$; $-3$ is extraneous ($1\ne-1$); sum $=2$.

## M1-Q17
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: In the system of equations below, $k$ is a constant. If the system has no solution, what is the value of $k$?\dsp{$6x+9y=21$}\dsp{$2x+ky=14$}
- Answer: 3
- Solution: First equation $\div3$: $2x+3y=7$; parallel lines need $k=3$, and $7\ne14$ so no solution.

## M1-Q18
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The graph of the quadratic function $f$ crosses the $x$-axis at $x=2$ and $x=-6$ and crosses the $y$-axis at $(0,-24)$. What is the minimum value of $f$?
- A: $-48$
- B: $-32$
- C: $-24$
- D: $-16$
- Answer: B
- Solution: $f=a(x-2)(x+6)$, $f(0)=-12a=-24$, $a=2$; vertex $x=-2$, $f(-2)=2(-4)(4)=-32$.

## M1-Q19
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: How many liters of a 10\% salt solution must be added to 20 liters of a 50\% salt solution to make a 20\% salt solution?
- A: $20$
- B: $40$
- C: $60$
- D: $80$
- Answer: C
- Solution: $0.10x+10=0.20(x+20) \Rightarrow x=60$.

## M1-Q20
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: Class A has 48 students and a mean test score of 72. Class B has a mean test score of 90. The mean test score of all the students in both classes combined is 78. How many students are in Class B?
- A: $24$
- B: $36$
- C: $48$
- D: $96$
- Answer: A
- Solution: $48(72)+90n=78(48+n) \Rightarrow 12n=288$, $n=24$ (weights are inversely proportional to the distances 6 and 12).

## M1-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: A solid metal sphere with a radius of 6 centimeters is melted down, and all of the metal is used to make small solid cones. Each cone has a radius of 3 centimeters and a height of 4 centimeters. How many cones can be made?
- Answer: 24
- Solution: Sphere $\frac43\pi6^3=288\pi$; cone $\frac13\pi3^2\cdot4=12\pi$; $288/12=24$.

## M1-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: A culture of bacteria is modeled by the function below, where $P$ is the number of bacteria and $t$ is the time in hours.\dsp{$P(t)=1200(1.5)^{t/4}$}Which of the following is closest to the percent increase in the population each hour?
- A: $10.7\%$
- B: $12.5\%$
- C: $37.5\%$
- D: $50\%$
- Answer: A
- Solution: Hourly factor $1.5^{1/4}\approx1.1067$, i.e. about $10.7\%$ (12.5\% is $50\%/4$).

# MODULE 2 — harder route (22 questions; Easy Q1–3, Medium Q4–9, Hard Q10–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: What is the solution to the equation below?\dsp{$2(3x-4)=5(x+1)$}
- A: $3$
- B: $5$
- C: $9$
- D: $13$
- Answer: D
- Solution: $6x-8=5x+5 \Rightarrow x=13$.

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following expressions is equivalent to $(x-5)^2-9$?
- A: $x^2-34$
- B: $x^2-10x-9$
- C: $x^2-10x+34$
- D: $x^2-10x+16$
- Answer: D
- Solution: $x^2-10x+25-9=x^2-10x+16$.

## M2-Q3
- Domain: GT
- Difficulty: E
- Type: GRID
- Stem: The measures of the three angles of a triangle are in the ratio $2:3:4$. What is the measure, in degrees, of the smallest angle?
- Answer: 40
- Solution: $2k+3k+4k=180$, $k=20$, smallest $=40$.

## M2-Q4
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The ratio of cats to dogs at an animal shelter is 5 to 3. After 14 more dogs arrive at the shelter, the number of dogs equals the number of cats. How many animals were at the shelter before the 14 dogs arrived?
- A: $21$
- B: $35$
- C: $56$
- D: $70$
- Answer: C
- Solution: Cats $5k$, dogs $3k$; $3k+14=5k$, $k=7$; total before $=8k=56$ (35 = cats, 21 = dogs).

## M2-Q5
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the $xy$-plane, line $\ell$ passes through the point $(3,-1)$ and is parallel to the line $4x-3y=9$. What is the $y$-coordinate of the point where $\ell$ crosses the $y$-axis?
- A: $-5$
- B: $-3$
- C: $-1$
- D: $5$
- Answer: A
- Solution: Slope $4/3$; $y=\frac43x+b$, $-1=4+b$, $b=-5$.

## M2-Q6
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: What is the product of the solutions to the equation $3x^2-8x-35=0$?
- A: $-\frac{35}{3}$
- B: $-\frac{8}{3}$
- C: $\frac{8}{3}$
- D: $\frac{35}{3}$
- Answer: A
- Solution: Vieta: product $=c/a=-35/3$ (roots $5$ and $-7/3$).

## M2-Q7
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A right triangle has acute angles that measure $30^\circ$ and $60^\circ$, and its hypotenuse is 12 units long. What is the area of the triangle, in square units?
- A: $18$
- B: $18\sqrt{3}$
- C: $36$
- D: $36\sqrt{3}$
- Answer: B
- Solution: Legs $6$ and $6\sqrt3$; area $\frac12(6)(6\sqrt3)=18\sqrt3$.

## M2-Q8
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The function $f$ is defined by $f(x)=3\cdot2^{x}+5$. For some constant $a$, $f(a)=101$. What is the value of $a$?
- Answer: 5
- Solution: $3\cdot2^a=96$, $2^a=32$, $a=5$.

## M2-Q9
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: If $3a-2b=10$ and $5a+2b=22$, what is the value of $a+b$?
- A: $4$
- B: $5$
- C: $8$
- D: $12$
- Answer: B
- Solution: Add: $8a=32$, $a=4$; $12-2b=10$, $b=1$; $a+b=5$.

## M2-Q10
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The table gives three values of the quadratic function $f$. The graph of $g$ is the graph of $f$ translated 3 units to the left and 10 units up. What is the value of $g(0)$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|}
\hline
$x$ & $2$ & $4$ & $6$\\\hline
$f(x)$ & $1$ & $-7$ & $1$\\\hline
\end{tabular}
```
- A: $-5$
- B: $5$
- C: $35$
- D: $101$
- Answer: B
- Solution: $f(2)=f(6)$ so the axis is $x=4$, vertex $(4,-7)$; $a=2$; $g(x)=f(x+3)+10$, $g(0)=f(3)+10=-5+10=5$.

## M2-Q11
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: In the system of equations below, $k$ is a constant. For which value of $k$ does the system have no solution?\dsp{$kx+2y=10$}\dsp{$24x+(k+2)y=40$}
- A: $-8$
- B: $-6$
- C: $6$
- D: $8$
- Answer: A
- Solution: Parallel needs $k(k+2)=48 \Rightarrow k=6$ or $-8$; $k=6$ makes the equations identical (infinitely many), $k=-8$ gives $24x-6y=-30\ne40$, so $-8$.

## M2-Q12
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: For how many integer values of $k$ does the equation $2x^2+kx+8=0$ have no real solutions?
- Answer: 15
- Solution: $k^2-64<0 \Rightarrow -8<k<8$, integers $-7,\dots,7$: 15 values.

## M2-Q13
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: Of the 800 residents surveyed about a proposed park, 55\% live in the north district and the rest live in the south district. In the north district, 40\% of the surveyed residents favor the proposal; in the south district, 65\% favor it. If one resident who favors the proposal is selected at random, which of the following is closest to the probability that the resident lives in the north district?
- A: $0.22$
- B: $0.40$
- C: $0.43$
- D: $0.55$
- Answer: C
- Solution: North favor $=440(0.4)=176$; south favor $=360(0.65)=234$; $176/410\approx0.43$.

## M2-Q14
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the graph of $x^2+y^2-10x+4y=20$ is a circle. The line $y=-8$ intersects the circle at two points. What is the distance, in units, between these two points?
- A: $\sqrt{13}$
- B: $2\sqrt{13}$
- C: $14$
- D: $2\sqrt{85}$
- Answer: B
- Solution: $(x-5)^2+(y+2)^2=49$, center $(5,-2)$, $r=7$; distance to line $=6$; chord $=2\sqrt{49-36}=2\sqrt{13}$.

## M2-Q15
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: A water tank can be filled by Pump A alone in 6 hours or by Pump B alone in 9 hours. A drain, when open, empties a full tank in 18 hours. Starting with an empty tank, both pumps are turned on and the drain is open the whole time. How many hours will it take to fill the tank? (Assume each device works at a constant rate.)
- Answer: 4.5
- Solution: Rate $=\frac16+\frac19-\frac1{18}=\frac29$ tank/hour, so $4.5$ hours.

## M2-Q16
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: A farmer has 240 meters of fencing to enclose a rectangular field along a straight river. No fence is needed along the river. The field will be divided into 3 equal plots by two additional fences, each perpendicular to the river, so the fencing consists of 4 pieces perpendicular to the river and 1 piece parallel to it. What is the maximum possible total area, in square meters, of the field?
- A: $2400$
- B: $2880$
- C: $3600$
- D: $4800$
- Answer: C
- Solution: Width $w$, length $240-4w$; $A=w(240-4w)$ peaks at $w=30$: $30\cdot120=3600$ (4800 forgets one divider).

## M2-Q17
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: The length of a rectangle is 4 more than twice its width. When the length is increased by 6 and the width is decreased by 2, the area of the new rectangle equals the area of the original rectangle. What is the perimeter of the original rectangle, in units?
- A: $34$
- B: $60$
- C: $68$
- D: $76$
- Answer: C
- Solution: $(2w+10)(w-2)=(2w+4)w \Rightarrow 2w=20$, $w=10$, $L=24$; perimeter $=68$ (76 is the new rectangle's).

## M2-Q18
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: The number of subscribers to a video channel, in thousands, is modeled by $S(t)=a\cdot b^{t}$, where $t$ is the number of weeks since the channel launched and $a$ and $b$ are positive constants. The table gives two values. According to the model, how many more thousands of subscribers will the channel have 6 weeks after launch than 5 weeks after launch?
- Figure:
```latex
\begin{tabular}{|c|c|c|}
\hline
$t$ (weeks) & $1$ & $4$\\\hline
$S(t)$ (thousands) & $6$ & $162$\\\hline
\end{tabular}
```
- Answer: 972
- Solution: $b^3=162/6=27$, $b=3$, $a=2$; $S(6)-S(5)=1458-486=972$ (1458 alone is a trap).

## M2-Q19
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: The equation $|2x-7|=k$, where $k$ is a positive constant, has two solutions that differ by 9. What is the product of the two solutions?
- A: $-8$
- B: $7$
- C: $8$
- D: $9$
- Answer: A
- Solution: Solutions $(7\pm k)/2$ differ by $k$, so $k=9$: $x=8$ and $x=-1$; product $-8$.

## M2-Q20
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A store's sales in the second quarter were 20\% greater than its sales in the first quarter. Third-quarter sales were 25\% less than second-quarter sales, and fourth-quarter sales were 40\% greater than third-quarter sales. If fourth-quarter sales were \$75,600, what were the store's total sales for all four quarters?
- A: \$186,000
- B: \$253,350
- C: \$259,200
- D: \$261,600
- Answer: D
- Solution: Q3 $=75600/1.4=54000$; Q2 $=54000/0.75=72000$; Q1 $=72000/1.2=60000$; total $=261600$.

## M2-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: In triangle $ABC$ shown, point $D$ lies on $\overline{AB}$ and point $E$ lies on $\overline{AC}$ so that $\overline{DE}$ is parallel to $\overline{BC}$. Also $AD=6$ and $DB=9$. The area of trapezoid $DBCE$ is 84 square units. What is the area, in square units, of triangle $ADE$?
- Figure:
```latex
\begin{tikzpicture}[scale=0.75,>=latex]
\coordinate (B) at (0,0); \coordinate (C) at (6.5,0); \coordinate (A) at (2.4,4.6);
\coordinate (D) at ($(A)!0.4!(B)$); \coordinate (E) at ($(A)!0.4!(C)$);
\draw[line width=0.7pt] (A)--(B)--(C)--cycle;
\draw[line width=0.7pt] (D)--(E);
\node[above] at (A) {$A$}; \node[below left] at (B) {$B$}; \node[below right] at (C) {$C$};
\node[left] at (D) {$D$}; \node[right] at (E) {$E$};
\node[left,font=\small] at ($(A)!0.2!(B)$) {6};
\node[left,font=\small] at ($(D)!0.5!(B)$) {9};
\end{tikzpicture}
```
- Answer: 16
- Solution: $AD/AB=6/15=2/5$, so area ratio $ADE:ABC=4:25$ and $ADE:DBCE=4:21$; $84\cdot4/21=16$.

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: What is the solution to the equation below?\dsp{$\sqrt{x+7}-\sqrt{x-2}=1$}
- A: $2$
- B: $7$
- C: $9$
- D: $18$
- Answer: D
- Solution: $\sqrt{x+7}=1+\sqrt{x-2}$; square: $x+7=x-1+2\sqrt{x-2}$, so $\sqrt{x-2}=4$, $x=18$ (check: $5-4=1$).
