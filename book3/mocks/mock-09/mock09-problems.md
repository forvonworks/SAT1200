# Mock Test 9 — Source of truth (Book 3, ≈800)

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
- Stem: An event planner charges a flat fee of \$180 plus \$12 for each guest. A client paid a total of \$540. How many guests were there?
- A: $45$
- B: $30$
- C: $60$
- D: $360$
- Answer: B
- Solution: $180+12g=540$ gives $12g=360$ and $g=30$ (45 divides the whole bill by 12 and ignores the fee; 60 adds the fee instead of subtracting it; 360 subtracts the fee but forgets to divide by 12).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $(x-3)(x+8)$?
- A: $x^{2}+11x-24$
- B: $x^{2}-5x-24$
- C: $x^{2}-24$
- D: $x^{2}+5x-24$
- Answer: D
- Solution: $(x-3)(x+8)=x^2+8x-3x-24=x^2+5x-24$ ($11x$ adds 3 and 8 instead of subtracting; $-5x$ has the wrong sign; $x^2-24$ drops the middle term).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: A clothing store has 480 jackets in stock at the start of a clearance sale. By the end of the sale, 35\% of the jackets have been sold. How many jackets are left in stock?
- Answer: 312
- Solution: $480(1-0.35)=480(0.65)=312$ (168 is the number sold, not the number left).

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A rectangular loading dock has a perimeter of 62 meters and a width of 11 meters. What is the area of the dock, in square meters?
- A: $220$
- B: $341$
- C: $440$
- D: $682$
- Answer: A
- Solution: The length is $\frac{62}{2}-11=20$, so the area is $20\cdot11=220$ (341 uses the half-perimeter 31 as the length; 440 uses $62-22=40$ as the length; 682 multiplies the perimeter by the width).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: The temperature in degrees Fahrenheit, $F$, is related to the temperature in degrees Celsius, $C$, by the equation $F=1.8C+32$. A greenhouse is kept at $86^{\circ}$F. What is this temperature in degrees Celsius?
- A: $54$
- B: $65.6$
- C: $30$
- D: $79.8$
- Answer: C
- Solution: $86=1.8C+32$ gives $1.8C=54$ and $C=30$ (54 stops before dividing by 1.8; 65.6 adds 32 instead of subtracting it; 79.8 is $\frac{86}{1.8}+32$, which applies the conversion in the wrong direction).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: If $2^{x}=32$, what is the value of $2^{x-2}$?
- A: $8$
- B: $30$
- C: $16$
- D: $3$
- Answer: A
- Solution: $2^x=32$ means $x=5$, so $2^{x-2}=2^3=8$ (30 subtracts 2 from 32; 16 divides by 2 once; 3 is $x-2$).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: A delivery van leaves the depot carrying 240 packages. At each stop it drops off 8 packages and picks up none. After how many stops will exactly 72 packages remain on the van?
- Answer: 21
- Solution: $240-8s=72$ gives $8s=168$ and $s=21$.

## M1-Q8
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: For $x>0$, which of the following is equivalent to $\sqrt{x}\cdot x^{3/2}$?
- A: $x^{3/4}$
- B: $x^{2}$
- C: $x^{5/2}$
- D: $x$
- Answer: B
- Solution: $x^{1/2}\cdot x^{3/2}=x^{1/2+3/2}=x^2$ ($x^{3/4}$ multiplies the exponents; $x^{5/2}$ treats $\sqrt x$ as $x^1$; $x$ subtracts the exponents).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The ages of the 7 members of a hiking club are 24, 27, 31, 35, 39, 41, and 48. A new member who is 35 years old joins the club. Which of the following statements about the new set of 8 ages, compared with the original set of 7 ages, is true?
- A: The mean is unchanged and the standard deviation is the same.
- B: The mean is unchanged and the standard deviation is larger.
- C: The mean is unchanged and the standard deviation is smaller.
- D: The mean is larger and the standard deviation is smaller.
- Answer: C
- Solution: The original mean is $\frac{245}{7}=35$, so a new value of 35 leaves the mean at 35. The new value is exactly at the mean, so it adds nothing to the sum of squared deviations but increases the number of values; the standard deviation therefore gets smaller (the other choices ignore this, or change the mean).

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A warehouse packs mugs in small boxes that hold 6 mugs each and large boxes that hold 15 mugs each. A shipment consists of 30 boxes holding a total of 306 mugs. How many of the boxes are large boxes?
- Answer: 14
- Solution: With $s$ small and $\ell$ large boxes, $s+\ell=30$ and $6s+15\ell=306$. Substituting $s=30-\ell$ gives $180+9\ell=306$, so $\ell=14$.

## M1-Q11
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following is equivalent to $(2x-3)^{2}-(x+1)^{2}$?
- A: $3x^{2}-12x+8$
- B: $3x^{2}+8$
- C: $3x^{2}-10x+8$
- D: $3x^{2}-14x+8$
- Answer: D
- Solution: $(4x^2-12x+9)-(x^2+2x+1)=3x^2-14x+8$ ($3x^2-12x+8$ drops the middle term of $(x+1)^2$; $3x^2+8$ drops both middle terms; $3x^2-10x+8$ forgets to distribute the minus sign onto $2x$).

## M1-Q12
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: On a map grid whose units are kilometers, a delivery drone flies in a straight line from depot $A(-2,5)$ to depot $B(10,-3)$. A checkpoint $C$ lies on $\overline{AB}$, three-fourths of the way from $A$ to $B$. What are the coordinates of $C$?
- A: $(7,-1)$
- B: $(4,1)$
- C: $(1,3)$
- D: $(5.5,2.75)$
- Answer: A
- Solution: From $A$, move $\frac34$ of the way: $x=-2+\frac34(12)=7$ and $y=5+\frac34(-8)=-1$ ($(4,1)$ is the midpoint; $(1,3)$ is one-fourth of the way; $(5.5,2.75)$ adds three-fourths of $B$'s coordinates to $A$).

## M1-Q13
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A community theater needs to raise at least \$6,000 from a performance. Adult tickets cost \$30 each and student tickets cost \$18 each. Exactly 100 student tickets were sold. What is the least number of adult tickets that must be sold to reach the goal?
- A: $200$
- B: $234$
- C: $140$
- D: $4{,}200$
- Answer: C
- Solution: $30a+18(100)\ge6000$ gives $30a\ge4200$ and $a\ge140$ (200 ignores the student revenue; 234 divides the remaining \$4,200 by the student price; 4,200 stops before dividing).

## M1-Q14
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: Two accounts each start with \$2,000 and earn 10\% interest per year. Account A pays simple interest, so each year's interest is 10\% of the original \$2,000. Account B pays interest compounded annually. After 3 years, how many more dollars of interest has Account B earned than Account A?
- Answer: 62
- Solution: Account A earns $3(200)=600$. Account B grows to $2000(1.1)^3=2662$, so it earns $662$. The difference is $662-600=62$.

## M1-Q15
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A soccer team has played 20 league matches and lost 3 of them. A win earns 3 points, a draw earns 1 point, and a loss earns 0 points. The team has 41 points. How many of the 20 matches did the team win?
- A: $14$
- B: $12$
- C: $5$
- D: $24$
- Answer: B
- Solution: With $w$ wins and $d$ draws, $w+d=17$ and $3w+d=41$. Subtracting gives $2w=24$, so $w=12$ (14 is $41\div3$ rounded; 5 is the number of draws; 24 is $2w$).

## M1-Q16
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: A charity concert's profit, in dollars, when each ticket is sold for $p$ dollars is modeled by $P(p)=-120(p-25)^{2}+9{,}000$. Which of the following statements is true?
- A: The maximum possible profit is \$25, and it occurs when the ticket price is \$9,000.
- B: The maximum possible profit is \$120, and it occurs when the ticket price is \$25.
- C: The profit is \$9,000 when tickets are free, and it decreases as the ticket price rises.
- D: The maximum possible profit is \$9,000, and it occurs when the ticket price is \$25.
- Answer: D
- Solution: The square is never negative and $-120$ makes it a loss, so $P$ is largest when $p-25=0$: the maximum profit is 9,000 at $p=25$ (the second choice swaps the two numbers; 120 is only the stretch factor; $P(0)=-66{,}000$, not 9,000).

## M1-Q17
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: If $a^{2}-b^{2}=63$ and $a+b=9$, what is the value of $a$?
- Answer: 8
- Solution: $a^2-b^2=(a+b)(a-b)$, so $a-b=\frac{63}{9}=7$. Adding $a+b=9$ gives $2a=16$ and $a=8$ (7 is only $a-b$).

## M1-Q18
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: In a genetics experiment, 320 pea plants were grown, and the ratio of tall plants to short plants was 3 to 1. Some tall plants, and no short plants, were then removed so that the ratio of tall plants to short plants became 5 to 2. How many tall plants were removed?
- A: $200$
- B: $40$
- C: $80$
- D: $16$
- Answer: B
- Solution: At first there are 240 tall and 80 short plants. The short plants stay at 80, so the tall plants must drop to $80\cdot\frac52=200$; $240-200=40$ were removed (200 is the number left; 80 is the number of short plants; 16 is $240\div15$).

## M1-Q19
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A retailer ordered cartons of two products. Each carton of product A costs \$14 and each carton of product B costs \$22. The retailer ordered 10 more cartons of A than of B and spent exactly \$680 in all. How many cartons did the retailer order in total?
- A: $40$
- B: $15$
- C: $25$
- D: $34$
- Answer: A
- Solution: With $b$ cartons of B, $14(b+10)+22b=680$ gives $36b=540$ and $b=15$. Then A is 25 and the total is 40 (15 and 25 are the counts of one product; 34 is $680\div20$).

## M1-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The function $f$ is defined by $f(x)=2x^{2}+bx+c$, where $b$ and $c$ are constants. The graph of $f$ in the $xy$-plane passes through $(0,3)$, and $f(1)=f(5)$. What is the value of $f(3)$?
- A: $57$
- B: $3$
- C: $-15$
- D: $-12$
- Answer: C
- Solution: $f(0)=3$ gives $c=3$. Equal outputs at $x=1$ and $x=5$ put the axis of symmetry at $x=3$, so $-\frac{b}{4}=3$ and $b=-12$. Then $f(3)=18-36+3=-15$ (57 uses $b=12$; 3 is $f(0)$; $-12$ is $b$).

## M1-Q21
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: A retailer buys a jacket from a wholesaler, marks the price up by 40\% of the wholesale price, and later sells it during a sale at 25\% off the marked-up price. The sale price is \$63. What did the retailer pay the wholesaler for the jacket, in dollars?
- Answer: 60
- Solution: If the wholesale price is $w$, the sale price is $w(1.40)(0.75)=1.05w=63$, so $w=60$ (treating the two changes as a net $+15\%$ would give $63\div1.15\approx54.8$).

## M1-Q22
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: An isosceles trapezoid has parallel sides of lengths 12 and 30 and a perimeter of 72, as shown. What is the area of the trapezoid?
- Figure:
```latex
\begin{tikzpicture}[x=0.12cm,y=0.12cm]
\fill[badge!45] (0,0)--(30,0)--(21,12)--(9,12)--cycle;
\draw[line width=0.7pt] (0,0)--(30,0)--(21,12)--(9,12)--cycle;
\node[above,font=\small] at (15,12) {12};
\node[below,font=\small] at (15,0) {30};
\draw[line width=0.6pt] (3.9,6.5)--(5.1,5.5); \draw[line width=0.6pt] (24.9,6.5)--(26.1,5.5);
\end{tikzpicture}
```
- A: $315$
- B: $504$
- C: $189$
- D: $252$
- Answer: D
- Solution: The two equal legs are $\frac{72-42}{2}=15$. Each leg extends $\frac{30-12}{2}=9$ beyond the top base, so the height is $\sqrt{15^2-9^2}=12$ and the area is $\frac12(12+30)(12)=252$ (315 uses the leg as the height; 504 forgets the $\frac12$; 189 uses 9 as the height).

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: A theater manager packs 5 identical boxes of programs and also adds 12 loose programs, for a total of 112 programs. How many programs are in each box?
- A: $24.8$
- B: $22.4$
- C: $20$
- D: $100$
- Answer: C
- Solution: $5p+12=112$ gives $5p=100$ and $p=20$ (24.8 adds the 12 before dividing; 22.4 ignores the loose programs; 100 stops before dividing).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $g$ is defined by $g(x)=3\cdot2^{x}$. What is the value of $g(4)-g(2)$?
- A: $36$
- B: $12$
- C: $24$
- D: $48$
- Answer: A
- Solution: $g(4)=48$ and $g(2)=12$, so the difference is 36 (12 is $g(2)$ alone; 24 is $g(3)$; 48 is $g(4)$ alone).

## M2-Q3
- Domain: PSDA
- Difficulty: M
- Type: GRID
- Stem: A shipping container can hold at most 26.5 metric tons of cargo. Each crate weighs 1,250 pounds. If 1 metric ton is 1,000 kilograms and 1 kilogram is 2.2 pounds, what is the greatest number of crates that can be loaded without exceeding the weight limit?
- Answer: 46
- Solution: The limit is $26.5\cdot1000\cdot2.2=58{,}300$ pounds. $\frac{58300}{1250}=46.64$, and only whole crates fit, so the greatest number is 46 (rounding to 47 would exceed the limit).

## M2-Q4
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following is equivalent to $\frac{1}{4}x^{2}-3x+9$?
- A: $\left(\frac{1}{2}x+3\right)^{2}$
- B: $\left(\frac{1}{4}x-3\right)^{2}$
- C: $\left(\frac{1}{2}x-9\right)^{2}$
- D: $\left(\frac{1}{2}x-3\right)^{2}$
- Answer: D
- Solution: The first term is $(\frac12x)^2$, the last is $3^2$, and the middle term is $-2(\frac12x)(3)=-3x$, so the expression is $(\frac12x-3)^2$ ($(\frac12x+3)^2$ has the wrong middle sign; $(\frac14x-3)^2$ squares the coefficient incorrectly; $(\frac12x-9)^2$ uses 9 instead of its square root).

## M2-Q5
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: A rectangular lawn measures 18 meters by 12 meters. A path of uniform width is built around the lawn, so the lawn and the path together form a larger rectangle. The area of the path alone equals the area of the lawn. What is the width of the path, in meters?
- A: $6$
- B: $3$
- C: $18$
- D: $1.5$
- Answer: B
- Solution: The larger rectangle has area $2(216)=432$: $(18+2w)(12+2w)=432$ gives $w^2+15w-54=0$, so $(w+18)(w-3)=0$ and $w=3$ (6 adds $w$, not $2w$, to each side; 18 is the rejected negative root; 1.5 halves the width twice).

## M2-Q6
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A map uses a coordinate grid whose units are kilometers. A survey drone flies in a straight line at a constant speed. At 2:00 p.m. it is at $(3,-1)$, and at 2:30 p.m. it is at $(9,3)$. At the moment the drone's $x$-coordinate is 21, what is its $y$-coordinate?
- A: $11$
- B: $15$
- C: $7$
- D: $14$
- Answer: A
- Solution: Every 30 minutes $x$ grows by 6 and $y$ by 4. To go from $x=3$ to $x=21$ takes 3 half-hours, so $y=-1+3(4)=11$ (15 starts from $(9,3)$ but takes three steps; 7 takes only two steps from the first point; 14 treats $y$ as proportional to $x$).

## M2-Q7
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A wildlife biologist tags 80 fish in a lake and releases them. Several days later she catches a random sample of 150 fish from the lake and finds that 12 of them are tagged. Assuming the proportion of tagged fish in the sample equals the proportion of tagged fish in the whole lake, about how many fish are in the lake?
- A: $960$
- B: $1{,}800$
- C: $1{,}000$
- D: $218$
- Answer: C
- Solution: $\frac{12}{150}=\frac{80}{N}$ gives $N=\frac{80\cdot150}{12}=1000$ (960 is $80\cdot12$; 1,800 is $12\cdot150$; 218 is $80+150-12$).

## M2-Q8
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A research thermometer uses a new scale $T$ that is a linear function of the Fahrenheit scale. Water freezes at $32^{\circ}$F, which reads $20^{\circ}$T, and boils at $212^{\circ}$F, which reads $220^{\circ}$T. What is the reading, in degrees T, when the temperature is $98.6^{\circ}$F?
- Answer: 94
- Solution: The slope is $\frac{220-20}{212-32}=\frac{10}{9}$ degrees T per degree F. $T=20+\frac{10}{9}(98.6-32)=20+74=94$.

## M2-Q9
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Plant A is 10 centimeters tall today and grows 4 centimeters each month. Plant B is also 10 centimeters tall today, and its height increases by 20\% each month. At the end of which month is Plant B first taller than Plant A?
- A: Month 6
- B: Month 8
- C: Month 7
- D: Month 9
- Answer: B
- Solution: After $t$ months, $A=10+4t$ and $B=10(1.2)^t$. At $t=7$: $A=38$, $B\approx35.8$. At $t=8$: $A=42$, $B\approx43.0$. So B first passes A at month 8 (6 and 7 are too early; 9 is the month after the first crossing).

## M2-Q10
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: In the figure, two circles share center $O$. A chord of the larger circle is tangent to the smaller circle. The chord has length 24, and the radius of the smaller circle is 5. What is the area of the region between the two circles?
- Figure:
```latex
\begin{tikzpicture}[scale=0.165]
\draw[line width=0.7pt] (0,0) circle (13);
\fill[badge!45] (0,0) circle (5);
\draw[line width=0.7pt] (0,0) circle (5);
\draw[line width=0.7pt] (-12,5)--(12,5);
\fill (0,0) circle (0.25); \node[below left,font=\small] at (0,0) {$O$};
\draw[line width=0.5pt] (0,0)--(0,5);
\node[right,font=\small] at (0,2.2) {5};
\draw[line width=0.4pt,<->] (-12,6.8)--(12,6.8);
\node[above,font=\small] at (0,6.8) {24};
\end{tikzpicture}
```
- A: $169\pi$
- B: $576\pi$
- C: $119\pi$
- D: $144\pi$
- Answer: D
- Solution: The radius to the tangent point is perpendicular to the chord and bisects it, so $R^2=5^2+12^2=169$. The ring area is $\pi(R^2-r^2)=\pi(169-25)=144\pi$ (169$\pi$ is the whole large disk; $576\pi$ uses the chord as a radius; $119\pi$ subtracts 25 a second time).

## M2-Q11
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A theater sold 200 tickets for a show: adult tickets at \$18, student tickets at \$12, and senior tickets at \$10. The theater sold the same number of student tickets as senior tickets and collected \$3,320 in all. How many adult tickets were sold?
- A: $160$
- B: $20$
- C: $180$
- D: $40$
- Answer: A
- Solution: With $s$ student and $s$ senior tickets, there are $200-2s$ adult tickets: $18(200-2s)+22s=3320$ gives $3600-14s=3320$, so $s=20$ and the adult tickets number 160 (20 is $s$; 180 is the adult count if only one of the two other groups is subtracted; 40 is $2s$).

## M2-Q12
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: Three-fourths of a number is 15 more than one-third of the same number. What is one-half of the number?
- Answer: 18
- Solution: $\frac34n=\frac13n+15$ gives $\frac{5}{12}n=15$, so $n=36$ and half of it is 18 (36 is $n$ itself).

## M2-Q13
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: For the equation $(k^{2}-k-6)x=k^{2}-9$, where $k$ is a constant, for which value of $k$ does the equation have no solution?
- A: $3$
- B: $-2$
- C: $-3$
- D: $2$
- Answer: B
- Solution: The coefficient $(k-3)(k+2)$ is zero at $k=3$ and $k=-2$. At $k=3$ the right side is $0$ too, so $0\cdot x=0$ has infinitely many solutions. At $k=-2$ the right side is $-5$, so $0\cdot x=-5$ has no solution. ($k=3$ gives infinitely many solutions; $-3$ makes only the right side zero; $2$ makes neither zero.)

## M2-Q14
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the graph of $y=x^{2}+2$ and the graph of $x^{2}+y^{2}=k$, where $k$ is a positive constant, have exactly one point in common. What is the value of $k$?
- A: $2$
- B: $\frac{9}{4}$
- C: $4$
- D: $8$
- Answer: C
- Solution: Substituting $x^2=y-2$ gives $y^2+y-2-k=0$ with the extra condition $y\ge2$. A double root would need $9+4k=0$, which is impossible for $k>0$, so tangency in the usual sense never happens. Instead the circle must touch the parabola at its vertex $(0,2)$, the point nearest the origin, so $k=2^2=4$ (2 is the radius; $\frac94$ is the discriminant condition with its sign dropped; 8 doubles the squared radius).

## M2-Q15
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: In the figure, line $PT$ is tangent at $T$ to a circle with center $O$. Segment $PO$ meets the circle at $A$. If $PT=24$ and $PA=16$, what is the radius of the circle?
- Figure:
```latex
\begin{tikzpicture}[scale=0.125]
\draw[line width=0.7pt] (0,0) circle (10);
\coordinate (O) at (0,0); \coordinate (P) at (26,0); \coordinate (T) at (3.846,9.231); \coordinate (A) at (10,0);
\draw[line width=0.7pt] (P)--(T); \draw[line width=0.7pt] (O)--(P); \draw[line width=0.5pt,dashed] (O)--(T);
\fill (O) circle (0.45); \fill (A) circle (0.45); \fill (T) circle (0.45); \fill (P) circle (0.45);
\node[below left,font=\small] at (O) {$O$}; \node[below,font=\small] at (A) {$A$}; \node[above,font=\small] at (T) {$T$}; \node[right,font=\small] at (P) {$P$};
\node[above right,font=\small] at (15,5.2) {24}; \node[below,font=\small] at (18,0) {16};
\draw[line width=0.4pt] ($(T)+(0.85,-0.35)$)--($(T)+(1.2,0.5)$)--($(T)+(0.35,0.85)$);
\end{tikzpicture}
```
- Answer: 10
- Solution: Let the radius be $r$. The radius $OT$ is perpendicular to the tangent, so triangle $PTO$ is right-angled at $T$ with $OP=16+r$: $r^2+24^2=(16+r)^2$ gives $576=256+32r$, so $r=10$.

## M2-Q16
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A set of 7 positive integers has a mean of 10, a median of 9, and a unique mode of 8. What is the greatest possible value of the largest integer in the set?
- A: $26$
- B: $18$
- C: $40$
- D: $23$
- Answer: D
- Solution: The sum is 70 and the fourth number is 9. Two 8s must appear, and the smallest possible lower three are $1,8,8$ (sum 17). The numbers above the median cannot repeat 9 (that would tie 8 as the mode), so they are at least $10$ and $11$. The largest number is then $70-17-9-10-11=23$ (26 lets 9 appear three times; 18 uses three 8s; 40 ignores the mode condition).

## M2-Q17
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the line $y=2x-3$ intersects the parabola $y=x^{2}-5x+k$, where $k$ is a constant, at two points. The $x$-coordinates of these two points differ by 5. What is the value of $k$?
- A: $3$
- B: $6$
- C: $-3$
- D: $8$
- Answer: A
- Solution: Setting the $y$-values equal: $x^2-7x+(k+3)=0$. The roots differ by $\sqrt{49-4(k+3)}=5$, so $37-4k=25$ and $k=3$ (6 forgets the $+3$ from the line; $-3$ uses the slope $-5$ alone; 8 sets the discriminant, not its square root, equal to 5).

## M2-Q18
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: In a league of 10 teams, every team plays every other team exactly once. A win earns a team 3 points, a draw earns each of the two teams 1 point, and a loss earns 0 points. When all games have been played, the mean number of points per team is 12.5. How many of the games ended in a draw?
- A: $5$
- B: $20$
- C: $10$
- D: $35$
- Answer: C
- Solution: There are $\binom{10}{2}=45$ games and $10(12.5)=125$ points. A decisive game gives out 3 points and a draw gives out 2, so $3(45)-d=125$ and $d=10$ (5 treats a draw as worth 1 point in total; 20 is the points handed out in draws; 35 is the number of decisive games).

## M2-Q19
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: Two delivery drones leave depots at opposite ends of a straight route at the same moment, each flying at its own constant speed toward the other depot. After passing each other, drone A needs 9 more minutes to reach the far depot and drone B needs 4 more minutes. How many minutes after takeoff did the drones pass each other?
- Answer: 6
- Solution: Let them pass after $t$ minutes, with speeds $a$ and $b$. After passing, A covers B's first part: $9a=bt$; B covers A's first part: $4b=at$. Multiplying, $36ab=abt^2$, so $t^2=36$ and $t=6$ (6.5 would be the average of 9 and 4).

## M2-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The table gives three values of the quadratic function $f$. The function $g$ is defined by $g(x)=f\left(\dfrac{x-3}{2}\right)$. What is the sum of the zeros of $g$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|}
\hline
$x$ & 0 & 1 & 3\\\hline
$f(x)$ & 16 & 7 & $-5$\\\hline
\end{tabular}
```
- A: $20$
- B: $26$
- C: $16$
- D: $11$
- Answer: B
- Solution: Through $(0,16),(1,7),(3,-5)$ the quadratic is $f(x)=x^2-10x+16=(x-2)(x-8)$, with zeros 2 and 8. $g(x)=0$ when $\frac{x-3}{2}=2$ or $8$, so $x=7$ or $19$, and the sum is 26 (20 forgets the shift; 16 forgets the stretch; 11 applies the inverse operations backwards).

## M2-Q21
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In the figure, a chord is 5 units from the center $O$ of a circle with radius 10. What is the area of the shaded region, which lies on the side of the chord away from $O$?
- Figure:
```latex
\begin{tikzpicture}[scale=0.155]
\fill[badge!55] (-8.66,-5) arc (210:330:10) -- cycle;
\draw[line width=0.7pt] (0,0) circle (10);
\draw[line width=0.7pt] (-8.66,-5)--(8.66,-5);
\fill (0,0) circle (0.3); \node[above,font=\small] at (0,0.2) {$O$};
\draw[line width=0.5pt] (0,0)--(0,-5); \node[right,font=\small] at (0,-2.5) {5};
\draw[line width=0.5pt] (0,0)--(8.66,-5); \node[above right,font=\small] at (4.3,-2.9) {10};
\end{tikzpicture}
```
- A: $\frac{100\pi}{3}-50\sqrt{3}$
- B: $\frac{50\pi}{3}-25\sqrt{3}$
- C: $\frac{100\pi}{3}+25\sqrt{3}$
- D: $\frac{100\pi}{3}-25\sqrt{3}$
- Answer: D
- Solution: The distance 5 is half the radius, so each half of the chord subtends $60^\circ$ at $O$ and the central angle is $120^\circ$. The sector has area $\frac13(100\pi)=\frac{100\pi}{3}$. The triangle has base $2\cdot5\sqrt3=10\sqrt3$ and height 5, so its area is $25\sqrt3$. The segment is sector minus triangle (the second choice forgets the $\frac12$; the third uses $60^\circ$; the fourth adds the triangle).

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: For how many integer values of $k$ does the equation $|x^{2}-4x-5|=k$ have exactly four distinct real solutions?
- Answer: 8
- Solution: $x^2-4x-5=(x-5)(x+1)$ has its minimum $-9$ at $x=2$. For $k>0$ the equation $x^2-4x-5=k$ always has two solutions. The equation $x^2-4x-5=-k$ has two solutions only when $-k>-9$, that is $k<9$. So four distinct solutions need $0<k<9$, i.e. $k=1,2,\dots,8$: 8 values ($k=9$ gives only 3 solutions because $-k=-9$ is the vertex, a double root; $k=0$ gives only 2).
