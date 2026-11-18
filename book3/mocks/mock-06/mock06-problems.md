# Mock Test 6 — Source of truth (Book 3, ≈800)

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
- Stem: If $\dfrac{2}{3}x-5=7$, what is the value of $x$?
- A: $8$
- B: $13$
- C: $18$
- D: $36$
- Answer: C
- Solution: $\frac23x=12$, so $x=18$ (8 multiplies 12 by $\frac23$ instead of $\frac32$; 13 clears the fraction but forgets to multiply the 5 by 3; 36 multiplies by 3 and forgets to divide by 2).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The graph of $y=(x-4)(x+2)$ in the $xy$-plane crosses the $x$-axis at two points. What is the distance between these two points?
- A: $2$
- B: $6$
- C: $8$
- D: $12$
- Answer: B
- Solution: The zeros are $4$ and $-2$, so the distance is $4-(-2)=6$ (2 is the sum of the zeros, 8 is the size of their product, 12 doubles the distance).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: A clinic has 1,600 patients enrolled. Exactly 45\% of them received a flu vaccination this season. How many of the enrolled patients did not receive a flu vaccination?
- Answer: 880
- Solution: $55\%$ were not vaccinated: $0.55\cdot1600=880$ (720 is the vaccinated count).

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: In right triangle $ABC$, the right angle is at $C$, $AC=8$, and $BC=15$. What is the value of $\sin A$?
- A: $\frac{8}{15}$
- B: $\frac{8}{17}$
- C: $\frac{15}{8}$
- D: $\frac{15}{17}$
- Answer: D
- Solution: $AB=\sqrt{8^2+15^2}=17$ and $\sin A=\frac{\text{opposite}}{\text{hypotenuse}}=\frac{BC}{AB}=\frac{15}{17}$ (8/17 is $\cos A$, 15/8 is $\tan A$, 8/15 is $\tan B$).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $y=3x$ and $x+y=20$, what is the value of $x$?
- A: $5$
- B: $10$
- C: $15$
- D: $60$
- Answer: A
- Solution: $x+3x=20$, so $x=5$ (10 divides 20 by 2, 15 is the value of $y$, 60 is $3\cdot20$).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $4x^{2}-25$?
- A: $(2x-5)(2x+5)$
- B: $(2x-5)^{2}$
- C: $(2x+5)^{2}$
- D: $(4x-5)(x+5)$
- Answer: A
- Solution: Difference of squares: $(2x)^2-5^2=(2x-5)(2x+5)$ (B and C are perfect squares with a middle term; D expands to $4x^2+15x-25$).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: The length of a rectangle is 4 inches more than twice its width. The perimeter of the rectangle is 44 inches. What is the width, in inches, of the rectangle?
- Answer: 6
- Solution: $w+(2w+4)=22$, so $3w=18$ and $w=6$.

## M1-Q8
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: For $x>0$, which of the following is equivalent to $3x^{2}\cdot4x^{5}$?
- A: $7x^{7}$
- B: $7x^{10}$
- C: $12x^{10}$
- D: $12x^{7}$
- Answer: D
- Solution: Multiply the coefficients and add the exponents: $12x^{7}$ (A adds the coefficients, B adds the coefficients and multiplies the exponents, C multiplies the exponents).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The scatterplot shows data for 12 basketball players. For each player, $x$ is the average number of minutes played per game and $y$ is the average number of points scored per game. The line of best fit shown has equation $y=0.62x-3.4$. Which of the following is the best interpretation of the number 0.62 in this context?
- Figure:
```latex
\begin{tikzpicture}[x=2.1mm,y=1.7mm]
\draw[->,ink,line width=0.6pt] (10,0)--(40.5,0);
\draw[->,ink,line width=0.6pt] (10,0)--(10,21.5);
\foreach \a in {10,20,30,40}{\draw[ink,line width=0.5pt] (\a,0)--(\a,-0.8); \node[below,font=\scriptsize] at (\a,-0.8) {\a};}
\foreach \b in {5,10,15,20}{\draw[ink,line width=0.5pt] (10,\b)--(9.4,\b); \node[left,font=\scriptsize] at (9.4,\b) {\b};}
\node[below,font=\scriptsize] at (25,-3.2) {Minutes played per game};
\node[above,font=\scriptsize] at (10,21.5) {Points per game};
\foreach \a/\b in {12/5.0,15/5.2,18/8.5,20/8.3,22/11.4,24/10.6,26/13.9,28/12.8,30/16.3,32/15.6,34/18.6,36/17.9}{\fill[ink] (\a,\b) circle (0.55);}
\draw[line width=0.8pt] (11,3.42)--(37,19.54);
\end{tikzpicture}
```
- A: A player who plays 0 minutes per game is predicted to score 0.62 points per game.
- B: The players in the data set scored 0.62 points per game on average.
- C: For each additional minute played per game, the predicted number of points scored per game increases by 0.62.
- D: For each additional point scored per game, the predicted number of minutes played per game increases by 0.62.
- Answer: C
- Solution: 0.62 is the slope: points per game per minute per game. (A describes the intercept, which is $-3.4$; B confuses the slope with a mean; D reverses the roles of $x$ and $y$.)

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A homebuyer makes a down payment of \$24,000 and then pays \$1,350 each month. What is the least whole number of months after which the total amount paid, including the down payment, will exceed \$90,000?
- A: $48$
- B: $49$
- C: $66$
- D: $67$
- Answer: B
- Solution: $24000+1350m>90000$ gives $m>48.89$, so $m=49$ (48 months total \$88,800; 66 and 67 ignore the down payment, $90000/1350\approx66.7$).

## M1-Q11
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: The lines $3x+2y=16$ and $x-y=2$ intersect at a point in the $xy$-plane. The line $y=kx+10$, where $k$ is a constant, passes through the same point. What is the value of $k$?
- Answer: -2
- Solution: From $x=y+2$: $3y+6+2y=16$, so $y=2$, $x=4$. Then $2=4k+10$ and $k=-2$.

## M1-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The phosphate level in a lake is 50 units today and decreases by 12\% every 3 years. Which of the following functions gives the phosphate level $P(t)$, in units, $t$ years from today?
- A: $P(t)=50(0.88)^{t/3}$
- B: $P(t)=50(0.88)^{3t}$
- C: $P(t)=50(0.12)^{t/3}$
- D: $P(t)=50(1.12)^{t/3}$
- Answer: A
- Solution: A 12\% decrease multiplies by $0.88$ once per 3-year period, and $t$ years contain $t/3$ periods. (B counts $3t$ periods; C uses the percent itself as the factor; D is growth.)

## M1-Q13
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A surveyor whose eyes are 1.6 meters above the ground stands on level ground 50 meters from the base of a tower. The angle of elevation from the surveyor's eyes to the top of the tower is $55^{\circ}$. To the nearest meter, what is the height of the tower?
- A: $35$
- B: $41$
- C: $71$
- D: $73$
- Answer: D
- Solution: Height above eye level $=50\tan55^\circ\approx71.4$; adding the eye height gives $73.0\approx73$ (71 forgets the eye height; 41 is $50\sin55^\circ$; 35 is $50/\tan55^\circ$).

## M1-Q14
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The functions $f$ and $g$ are defined by $f(x)=3x-2$ and $g(x)=x^{2}+1$. If $x>0$ and $f(g(x))=49$, what is the value of $x$?
- Answer: 4
- Solution: $f(g(x))=3(x^2+1)-2=3x^2+1=49$, so $x^2=16$ and $x=4$ (positive).

## M1-Q15
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A fiber-optic line transfers data at 480 megabits per second. At this rate, how many gigabytes of data can the line transfer in 10 minutes? (1 byte $=8$ bits and 1 gigabyte $=1{,}000$ megabytes.)
- A: $0.6$
- B: $3.6$
- C: $36$
- D: $288$
- Answer: C
- Solution: $480/8=60$ MB per second; in $600$ seconds that is $36{,}000$ MB $=36$ GB. (0.6 uses 10 seconds; 3.6 uses 1 minute; 288 forgets to convert bits to bytes.)

## M1-Q16
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A food truck sells tacos for \$3 each and burritos for \$7.50 each. On days when its revenue is exactly \$600, the numbers of tacos $t$ and burritos $b$ sold satisfy $3t+7.5b=600$. According to this equation, each additional burrito sold corresponds to how many fewer tacos sold?
- A: $0.4$
- B: $2.5$
- C: $4.5$
- D: $7.5$
- Answer: B
- Solution: $t=200-2.5b$, so the slope is $-2.5$: each burrito replaces 2.5 tacos (0.4 inverts the ratio; 4.5 subtracts the prices; 7.5 is the burrito price).

## M1-Q17
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The graphs of $y=x^{2}-3x-4$ and $y=2x+2$ in the $xy$-plane intersect at two points. What is the $y$-coordinate of the point of intersection with the greater $x$-coordinate?
- A: $0$
- B: $2$
- C: $6$
- D: $14$
- Answer: D
- Solution: $x^2-5x-6=0$ gives $x=6$ or $x=-1$. At $x=6$, $y=2(6)+2=14$ (0 is the $y$-coordinate at $x=-1$; 6 is the $x$-coordinate; 2 is the intercept).

## M1-Q18
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: If $x>0$, $y>0$, $x^{2}+y^{2}=52$, and $xy=24$, what is the value of $x+y$?
- Answer: 10
- Solution: $(x+y)^2=x^2+y^2+2xy=52+48=100$, so $x+y=10$ (the numbers are 4 and 6).

## M1-Q19
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the $xy$-plane, line $\ell$ passes through the points $(2,-3)$ and $(8,9)$. Line $m$ is perpendicular to $\ell$ and passes through the origin. Which of the following points lies on line $m$?
- A: $(4,-2)$
- B: $(2,-4)$
- C: $(4,2)$
- D: $(2,4)$
- Answer: A
- Solution: Slope of $\ell$ is $2$, so $m$ has slope $-\frac12$ and equation $y=-\frac12x$; $(4,-2)$ lies on it. (B is on $y=-2x$, a sign error; C is on $y=\frac12x$; D is on $y=2x$, the parallel line.)

## M1-Q20
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the line $3x+4y=36$ crosses the $x$-axis at point $A$ and the $y$-axis at point $B$. What is the shortest distance, in units, from the origin to line segment $\overline{AB}$?
- A: $\frac{36}{7}$
- B: $\frac{36}{5}$
- C: $\frac{15}{2}$
- D: $9$
- Answer: B
- Solution: $A=(12,0)$, $B=(0,9)$, $AB=15$. The right triangle's area is $\frac12\cdot12\cdot9=54=\frac12\cdot15\cdot h$, so $h=\frac{36}{5}$. (36/7 divides 36 by $3+4$; 15/2 is the distance to the midpoint of $AB$; 9 is the shorter intercept.)

## M1-Q21
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: In the equation $x^{2}-kx+18=0$, $k$ is a positive constant. The two solutions of the equation differ by 3. What is the value of $k$?
- Answer: 9
- Solution: Let the solutions be $r$ and $r+3$. Then $r(r+3)=18$, so $r=3$ or $r=-6$, and $k=r+(r+3)=9$ or $-9$. Since $k>0$, $k=9$.

## M1-Q22
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: Print Shop A charges \$0.50 per page for the first 200 pages of an order and \$0.30 for each page after the first 200. Print Shop B charges a flat \$60 plus \$0.10 per page. What is the least number of pages for which Print Shop B's total charge is strictly less than Print Shop A's?
- A: $101$
- B: $150$
- C: $151$
- D: $200$
- Answer: C
- Solution: For $n\le200$: $0.5n>60+0.1n$ gives $n>150$, so $151$ (check: A $=\$75.50$, B $=\$75.10$). (101 uses the second-tier formula $40+0.3n$, valid only past 200; 150 makes the shops equal; 200 is the tier boundary.)

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $5(x-3)=2x+9$, what is the value of $x$?
- A: $-2$
- B: $2$
- C: $4$
- D: $8$
- Answer: D
- Solution: $5x-15=2x+9$, so $3x=24$ and $x=8$ ($4$ forgets to distribute to the $-3$; $-2$ distributes $+15$; $2$ makes the right side $2x-9$).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: What is the $x$-coordinate of the vertex of the graph of $y=x^{2}-6x+11$ in the $xy$-plane?
- A: $-3$
- B: $3$
- C: $6$
- D: $11$
- Answer: B
- Solution: $x=-\frac{b}{2a}=3$ ($-3$ is a sign error; 6 is the coefficient of $x$; 11 is the $y$-intercept).

## M2-Q3
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The body mass index $B$ of a person who weighs $w$ pounds and is $h$ inches tall is given by $B=\dfrac{703w}{h^{2}}$. Which of the following expresses $h$ in terms of $B$ and $w$, for $h>0$?
- A: $h=\dfrac{\sqrt{703w}}{B}$
- B: $h=\left(\dfrac{703w}{B}\right)^{2}$
- C: $h=\dfrac{703w}{\sqrt{B}}$
- D: $h=\sqrt{\dfrac{703w}{B}}$
- Answer: D
- Solution: $h^2=\frac{703w}{B}$, so $h=\sqrt{\frac{703w}{B}}$ (A puts only the numerator under the root; B squares instead of taking a root; C takes the root of $B$ alone).

## M2-Q4
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A no-interest loan is repaid in equal monthly payments, so the remaining balance decreases by the same amount each month. After 8 months the remaining balance is \$9,360, and after 20 months it is \$7,200. What was the original loan amount, in dollars?
- Answer: 10800
- Solution: The balance falls $\frac{9360-7200}{12}=180$ per month, so the original amount is $9360+8\cdot180=10{,}800$.

## M2-Q5
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The number of reported cases of a virus in a town grew exponentially, with 250 cases in week 0 and 360 cases in week 2. By what percent did the number of reported cases grow each week?
- A: $20\%$
- B: $22\%$
- C: $44\%$
- D: $120\%$
- Answer: A
- Solution: $250b^2=360$, so $b^2=1.44$ and $b=1.2$: 20\% growth per week (44\% is the two-week growth, 22\% halves it, 120\% reads the factor $1.2$ as a percent growth).

## M2-Q6
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: Two triangular sails are similar. The smaller sail has an area of 18 square feet, and the larger sail has an area of 72 square feet. A side of the smaller sail is 5 feet long. How long, in feet, is the corresponding side of the larger sail?
- A: $10$
- B: $20$
- C: $54$
- D: $90$
- Answer: A
- Solution: The area ratio is $4$, so the scale factor is $\sqrt4=2$ and the side is $10$ (20 uses the area ratio as the scale factor; 54 subtracts the areas; 90 is $5\cdot18$).

## M2-Q7
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: The graph of $y=|3x-12|-6$ and the line $y=9$ intersect at two points in the $xy$-plane. What is the distance between these two points?
- A: $2$
- B: $9$
- C: $10$
- D: $30$
- Answer: C
- Solution: $|3x-12|=15$ gives $x=9$ or $x=-1$, so the distance is $10$ (2 solves $|3x-12|=3$, subtracting 6 instead of adding; 9 is one solution; 30 is the gap between $3x-12=15$ and $3x-12=-15$, not divided by 3).

## M2-Q8
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: What is the sum of the squares of the three real solutions of the equation $x^{3}-5x^{2}-4x+20=0$?
- Answer: 33
- Solution: $x^2(x-5)-4(x-5)=(x-5)(x-2)(x+2)$, so the solutions are $5,2,-2$ and $25+4+4=33$.

## M2-Q9
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following quadratic equations has the solutions $x=3+\sqrt{7}$ and $x=3-\sqrt{7}$?
- A: $x^{2}-6x+2=0$
- B: $x^{2}-6x-2=0$
- C: $x^{2}+6x+2=0$
- D: $x^{2}-6x+16=0$
- Answer: A
- Solution: The sum of the solutions is $6$ and the product is $9-7=2$, so $x^2-6x+2=0$ (B has the wrong sign on the product; C has the wrong sign on the sum; D uses $9+7$).

## M2-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: Glacier A is 420 meters thick and is thinning at a constant rate of 3.5 meters per decade. Glacier B is 350 meters thick and is thinning at a constant rate of 1.5 meters per decade. What is the least whole number of decades after which Glacier A will be thinner than Glacier B?
- A: $35$
- B: $36$
- C: $70$
- D: $120$
- Answer: B
- Solution: $420-3.5d<350-1.5d$ gives $d>35$, so $36$ (35 makes them equal, not thinner; 70 is the 70-meter gap, not divided by the 2 m per decade closing rate; 120 is when Glacier A reaches zero).

## M2-Q11
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A mobile plan costs \$45 per month and includes 10 gigabytes (GB) of data. Each additional whole gigabyte used costs \$8.50. Jin wants her bill for a month to be at most \$120. What is the greatest whole number of gigabytes in total that she can use in that month?
- Answer: 18
- Solution: $45+8.5g\le120$ gives $g\le8.82$, so 8 additional gigabytes; the total is $10+8=18$ (8 forgets the included 10 GB).

## M2-Q12
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: If $\dfrac{x}{2}+\dfrac{y}{3}=7$ and $\dfrac{x}{4}-\dfrac{y}{6}=\dfrac{3}{2}$, what is the value of $xy$?
- A: $4$
- B: $16$
- C: $60$
- D: $120$
- Answer: C
- Solution: Multiplying by 6 and 12: $3x+2y=42$ and $3x-2y=18$, so $x=10$, $y=6$ and $xy=60$ (4 is $x-y$, 16 is $x+y$, 120 is $x\cdot2y$).

## M2-Q13
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: Researchers wanted to know whether a new walking program lowers blood pressure in patients aged 50 to 65 at a health system. They selected 400 such patients at random and invited them to join; each patient decided whether to join. After six months, the average drop in systolic blood pressure was 9 points for the 210 patients who joined and 3 points for the 190 who did not. Which conclusion is best supported by the study?
- A: The program causes a larger drop in blood pressure for all patients aged 50 to 65 at the health system.
- B: The program causes a larger drop in blood pressure for the 400 patients selected, but this cannot be generalized to other patients.
- C: Because patients chose whether to join, nothing can be concluded about patients other than the 400 selected.
- D: Among patients aged 50 to 65 at the health system, joining is associated with a larger drop in blood pressure, but the study does not show that the program caused the larger drop.
- Answer: D
- Solution: Random selection allows generalizing the association to the whole population of patients, but without random assignment (patients chose) a cause-and-effect conclusion is not supported. (A claims both; B claims causation but denies generalization, which reverses the two ideas; C denies that a random sample generalizes.)

## M2-Q14
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The concentration of a herbicide in a pond, in micrograms per liter, $d$ days after it was applied is modeled by $C(d)=64(0.8)^{d/5}$. According to the model, the concentration decreases by 36\% every $n$ days. What is the value of $n$?
- A: $5$
- B: $10$
- C: $25$
- D: $36$
- Answer: B
- Solution: A 36\% decrease multiplies by $0.64=0.8^2$, which takes two 5-day periods: $n=10$ (5 is the period of the 20\% decrease; 25 squares the 5 instead of doubling it; 36 uses the percent as the number of days).

## M2-Q15
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A city planner surveyed two independent random samples of residents about a proposed bike lane. In the first sample, 38\% of the respondents supported the proposal, with a margin of error of 3.1 percentage points. In the second sample, 43\% supported it, with a margin of error of 3.4 percentage points. Both margins of error were calculated at the same confidence level. Which of the following percentages of all residents who support the proposal is consistent with the results of both samples?
- A: $36\%$
- B: $38\%$
- C: $40\%$
- D: $43\%$
- Answer: C
- Solution: The first interval is $34.9\%$ to $41.1\%$ and the second is $39.6\%$ to $46.4\%$; only values from $39.6\%$ to $41.1\%$ lie in both, so $40\%$. (38\% and 43\% are the two sample estimates, each outside the other interval; 36\% lies only in the first interval.)

## M2-Q16
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: In the $xy$-plane, the graph of the equation below is a circle.\dsp{$x^{2}+y^{2}-12x-16y+84=0$}What is the shortest distance, in units, from the origin to a point on the circle?
- Answer: 6
- Solution: Completing the squares: $(x-6)^2+(y-8)^2=16$, center $(6,8)$, radius $4$. The origin is $10$ from the center and outside the circle (84 > 0), so the nearest point is $10-4=6$ away. (10 is the distance to the center; 4 is the radius; 14 is the farthest point.)

## M2-Q17
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: A runner jogs the first half of a trail's length at 6 miles per hour and the second half at a constant speed of $v$ miles per hour. Her average speed for the entire trail is 8 miles per hour. What is the value of $v$?
- A: $10$
- B: $12$
- C: $14$
- D: $16$
- Answer: B
- Solution: Let each half be $d$ miles. Total time $\frac d6+\frac dv=\frac{2d}{8}$, so $\frac1v=\frac14-\frac16=\frac1{12}$ and $v=12$. (10 averages the two speeds, which is wrong because she spends more time at the slower speed; 14 is $8+6$; 16 doubles 8.)

## M2-Q18
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A screening test for a virus is given to everyone in a large population. The table shows the percent of the population in each group and the percent of each group that tests positive. Of all the people who test positive, approximately what percent are actually infected?
- Figure:
```latex
\begin{tabular}{|l|>{\centering\arraybackslash}p{22mm}|>{\centering\arraybackslash}p{27mm}|}
\hline
Group & Share of the population & Percent who test positive\\\hline
Infected & 2\% & 90\%\\\hline
Not infected & 98\% & 5\%\\\hline
\end{tabular}
```
- A: $2\%$
- B: $27\%$
- C: $90\%$
- D: $95\%$
- Answer: B
- Solution: Per 10,000 people: 200 infected, 180 of them test positive; 9,800 not infected, 490 of them test positive. Positives that are infected: $\frac{180}{670}\approx27\%$. (2\% is the base rate; 90\% is the sensitivity; 95\% is the share of healthy people who test negative.)

## M2-Q19
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: For a positive constant $k$, how many distinct real solutions does the equation $x^{2}-8x+16=k\,|x-4|$ have?
- A: $1$
- B: $2$
- C: $3$
- D: $4$
- Answer: C
- Solution: The left side is $|x-4|^2$, so $|x-4|\,(|x-4|-k)=0$: $x=4$ or $x=4\pm k$, three distinct solutions. (Dividing by $|x-4|$ loses $x=4$ and gives 2; 4 double-counts; 1 keeps only $x=4$.)

## M2-Q20
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: For a constant $k$, the vertex of the parabola $y=x^{2}-4kx+3k$ lies on the line $y=2x-5$. What is the sum of all possible values of $k$?
- Answer: -1/4
- Solution: The vertex is $(2k,\,3k-4k^2)$. Substituting into the line: $3k-4k^2=4k-5$, so $4k^2+k-5=0$, whose roots are $k=1$ and $k=-\frac54$. The sum is $-\frac14$ (also $-\frac ba$).

## M2-Q21
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: What is the sum of all real solutions of the equation $|x-2|+|x-9|=15$?
- A: $11$
- B: $13$
- C: $15$
- D: $22$
- Answer: A
- Solution: For $x\ge9$: $2x-11=15$, $x=13$. For $x\le2$: $11-2x=15$, $x=-2$. Between 2 and 9 the left side is 7, so there are no solutions. The sum is $11$. (13 is only the greater solution; 15 is the right side; 22 doubles the sum.)

## M2-Q22
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: From a point on level ground, the angle of elevation to the top of a wind turbine's tower is $28^{\circ}$. After walking 40 meters directly toward the base of the tower, the observer measures the angle of elevation to the top as $41^{\circ}$. Ignoring the observer's height, to the nearest meter, how tall is the tower?
- A: $9$
- B: $21$
- C: $35$
- D: $55$
- Answer: D
- Solution: Let $h$ be the height and $x$ the second distance to the base. Then $x=\frac{h}{\tan41^\circ}$ and $x+40=\frac{h}{\tan28^\circ}$, so $h\left(\frac1{\tan28^\circ}-\frac1{\tan41^\circ}\right)=40$ and $h\approx54.8\approx55$. (9 is $40\tan13^\circ$; 21 is $40\tan28^\circ$; 35 is $40\tan41^\circ$.)
