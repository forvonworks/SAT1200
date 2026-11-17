# Mock Test 5 — Source of truth (Book 3, ≈800)

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
- Stem: If $11-2x=-7$, what is the value of $x$?
- A: $2$
- B: $9$
- C: $18$
- D: $-9$
- Answer: B
- Solution: $-2x=-18$, $x=9$ (D loses the sign; 18 forgets to divide by 2; 2 subtracts 11 and 7 the wrong way).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $3x(x-4)+5x$?
- A: $3x^2-17x$
- B: $3x^2-12x+5$
- C: $3x^2-7$
- D: $3x^2-7x$
- Answer: D
- Solution: $3x^2-12x+5x=3x^2-7x$ (A subtracts $5x$; B drops the $x$ from $5x$; C drops the $x$ from $-7x$).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: A landscaping crew has spread mulch over 35\% of a lawn that has an area of 240 square meters. What area, in square meters, has been covered with mulch?
- Answer: 84
- Solution: $0.35\cdot240=84$.

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: In an isosceles triangle, each of the two base angles measures $54^{\circ}$. What is the measure, in degrees, of the vertex angle?
- A: $72$
- B: $54$
- C: $108$
- D: $126$
- Answer: A
- Solution: $180-2(54)=72$ (126 is $180-54$; 108 is $2\cdot54$).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $3(x+2)=2(x+7)$, what is the value of $x$?
- A: $-20$
- B: $1$
- C: $8$
- D: $12$
- Answer: C
- Solution: $3x+6=2x+14$, $x=8$ (1 forgets to distribute the 2 over the 7; 12 forgets to distribute the 3 over the 2; $-20$ is a sign slip).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is a zero of $p(x)=(x-3)(x+5)(2x-1)$?
- A: $-3$
- B: $2$
- C: $5$
- D: $\frac{1}{2}$
- Answer: D
- Solution: $2x-1=0$ gives $x=\frac12$ (the zeros are $3$, $-5$, $\frac12$; $-3$ and $5$ are sign slips; 2 is the coefficient).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: The student council needs to raise at least \$450 by selling pennants for \$6 each. What is the least number of pennants it must sell?
- Answer: 75
- Solution: $6n\ge450$, $n\ge75$.

## M1-Q8
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: In the $xy$-plane, the graph of $y=(x-2)(x+6)$ crosses the $y$-axis at the point $(0,k)$. What is the value of $k$?
- A: $-4$
- B: $-12$
- C: $4$
- D: $12$
- Answer: B
- Solution: $y(0)=(-2)(6)=-12$ ($-4$ is the sum of the zeros; 12 loses the sign).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The table shows two data sets, $P$ and $Q$, each with five values. Which of the following statements is true?
- Figure:
```latex
\begin{tabular}{|l|c|c|c|c|c|}
\hline
Set $P$ & 12 & 14 & 16 & 18 & 20\\\hline
Set $Q$ & 14 & 15 & 16 & 17 & 18\\\hline
\end{tabular}
```
- A: The two sets have the same mean, and Set $P$ has the greater standard deviation.
- B: The two sets have the same mean, and Set $Q$ has the greater standard deviation.
- C: Set $P$ has the greater mean, and Set $P$ has the greater standard deviation.
- D: The two sets have the same mean and the same standard deviation.
- Answer: A
- Solution: Both means are 16. The values of $P$ lie farther from 16 on average (SD $\approx2.83$ versus $\approx1.41$ for $Q$), so $P$ has the greater standard deviation.

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A robotics club has a budget of \$900. It buys 10 kits at \$45 each and will spend part of the remaining budget on battery packs that cost \$12 each. What is the greatest number of battery packs the club can buy without going over its budget?
- A: $20$
- B: $36$
- C: $37$
- D: $38$
- Answer: C
- Solution: $450+12b\le900$ gives $b\le37.5$, so $b=37$ (38 rounds up and overspends; 36 wrongly treats the budget as a strict limit; 20 is the number of kits the whole budget could buy).

## M1-Q11
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A garden center sells soil by the bag and mulch by the bag. Three bags of soil and two bags of mulch cost \$38. Five bags of soil and four bags of mulch cost \$68. What is the cost, in dollars, of one bag of soil?
- Answer: 8
- Solution: $3s+2m=38$ and $5s+4m=68$; doubling the first gives $6s+4m=76$, so $s=8$ (and $m=7$).

## M1-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: What is the remainder when $p(x)=2x^3-5x^2+x-4$ is divided by $x-2$?
- A: $-42$
- B: $-6$
- C: $-4$
- D: $6$
- Answer: B
- Solution: Remainder $=p(2)=16-20+2-4=-6$ ($-42$ is $p(-2)$; $-4$ is the constant term).

## M1-Q13
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A landscaper spreads mulch 7 centimeters deep over a rectangular flower bed that is 3 meters long and 2 meters wide. Mulch is sold in bags that each hold 40 liters. What is the least number of bags needed to cover the bed? (1 cubic meter $=$ 1,000 liters.)
- A: $11$
- B: $2$
- C: $10$
- D: $105$
- Answer: A
- Solution: Volume $=3\cdot2\cdot0.07=0.42$ m$^3=420$ L, and $420/40=10.5$, so 11 bags are needed (10 leaves part of the bed uncovered; 2 uses 100 L per cubic meter; 105 uses 10,000 L per cubic meter).

## M1-Q14
- Domain: PSDA
- Difficulty: M
- Type: GRID
- Stem: A steel supplier raised its price per tonne by 20\%. A month later it lowered the new price by 20\%, to \$720 per tonne. What was the price per tonne, in dollars, before the increase?
- Answer: 750
- Solution: $1.2(0.8)p=0.96p=720$, so $p=750$ (a 20\% rise followed by a 20\% drop does not return to the starting price, so \$720 is not the answer).

## M1-Q15
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The annual energy output, in kilowatt-hours (kWh), of a solar panel is modeled by $E(t)=5400(0.992)^{t}$, where $t$ is the number of years after the panel was installed. Which of the following is the best interpretation of the number $0.992$ in this context?
- A: The panel's output decreases by 0.992\% each year.
- B: The panel's output decreases by 99.2\% each year.
- C: The panel's output decreases by 43.2 kWh each year.
- D: The panel's output decreases by 0.8\% each year.
- Answer: D
- Solution: Each year the output is multiplied by $0.992$, i.e. it keeps 99.2\% and loses 0.8\%. (C treats the change as linear: $0.8\%$ of 5400 is 43.2 only in the first year.)

## M1-Q16
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the $xy$-plane, line $\ell$ is parallel to the graph of $3x+4y=20$ and passes through the point $(4,1)$. What is the $y$-intercept of line $\ell$?
- A: $-2$
- B: $3$
- C: $4$
- D: $16$
- Answer: C
- Solution: $\ell$: $3x+4y=3(4)+4(1)=16$, so $y=4$ when $x=0$ ($-2$ uses slope $+\frac34$; 16 is the constant of the equation; 5 would be the intercept of the given line).

## M1-Q17
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: The sum of three consecutive odd integers is less than 90. What is the greatest possible value of the smallest of the three integers?
- A: $25$
- B: $27$
- C: $28$
- D: $29$
- Answer: B
- Solution: $n+(n+2)+(n+4)=3n+6<90$ gives $n<28$; $n$ is odd, so $n=27$ (28 is even and makes the sum exactly 90; 29 gives sum 93).

## M1-Q18
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The expression $(3x+2)^2-(3x-2)^2$ is equivalent to $kx$, where $k$ is a constant. What is the value of $k$?
- Answer: 24
- Solution: $(a+b)^2-(a-b)^2=4ab=4(3x)(2)=24x$.

## M1-Q19
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following quadratic equations has the solutions $x=-\dfrac{3}{2}$ and $x=4$?
- A: $2x^2-5x-12=0$
- B: $2x^2+5x-12=0$
- C: $2x^2-11x+12=0$
- D: $2x^2+2x-12=0$
- Answer: A
- Solution: $(2x+3)(x-4)=2x^2-5x-12$ (B has solutions $\frac32$ and $-4$; C has $\frac32$ and $4$; D has $-3$ and $2$).

## M1-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The function $f$ is defined by $f(x)=-2(x-3)^2+18$. For how many integer values of $x$ is $f(x)$ positive?
- A: $3$
- B: $6$
- C: $7$
- D: $5$
- Answer: D
- Solution: $f(x)>0$ means $(x-3)^2<9$, so $0<x<6$ and $x=1,2,3,4,5$ (7 includes the zeros $x=0$ and $x=6$; 6 counts one endpoint; 3 counts only values within 1 of the vertex).

## M1-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: A right circular cone has a height of 12 centimeters and a base radius of 9 centimeters. A plane parallel to the base cuts off a smaller cone at the top, and the smaller cone has a height of 4 centimeters. The volume of the remaining solid, between the base and the cutting plane, is $k\pi$ cubic centimeters. What is the value of $k$?
- Answer: 312
- Solution: The small cone is similar with ratio $\frac13$, so its radius is 3 and its volume is $\frac13\pi(9)(4)=12\pi$. The large cone has $\frac13\pi(81)(12)=324\pi$. Remaining: $324-12=312$.

## M1-Q22
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: Two hikers start at opposite ends of a 27-kilometer trail at the same time and walk toward each other at constant speeds. One hiker walks 1.5 kilometers per hour faster than the other, and they meet after exactly 3 hours. After they meet, how many minutes does it take the slower hiker to reach the far end of the trail?
- A: $129$
- B: $180$
- C: $252$
- D: $315$
- Answer: C
- Solution: $3(2s+1.5)=27$ gives $s=3.75$ (slower) and $5.25$ (faster). The slower hiker has walked $11.25$ km, so $15.75$ km remain: $15.75/3.75=4.2$ h $=252$ min (180 uses the faster speed; 129 is the faster hiker's remaining time).

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: If $5x-3=2x+18$, what is the value of $x$?
- A: $5$
- B: $\frac{15}{7}$
- C: $7$
- D: $21$
- Answer: C
- Solution: $3x=21$, $x=7$ (5 is a sign slip; 15/7 moves $2x$ with the wrong sign; 21 forgets to divide by 3).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $f$ is defined by $f(x)=x^2-4x+1$. What is the value of $f(3)$?
- A: $-2$
- B: $-4$
- C: $-20$
- D: $22$
- Answer: A
- Solution: $9-12+1=-2$ (B uses $+1$ as $-1$; C is $-9-12+1$; D is $9+12+1$).

## M2-Q3
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A driver completed a 300-mile trip. She drove the first 120 miles at a constant speed of 60 miles per hour and the remaining 180 miles at a constant speed of 45 miles per hour. What was her average speed, in miles per hour, for the entire trip?
- A: $45$
- B: $52.5$
- C: $105$
- D: $50$
- Answer: D
- Solution: Time $=\frac{120}{60}+\frac{180}{45}=2+4=6$ h, so the average is $300/6=50$ (52.5 averages the two speeds; 105 adds them).

## M2-Q4
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: In the $xy$-plane, the graph of $kx+6y=30$, where $k$ is a constant, is parallel to the graph of $2x+3y=7$. What is the $x$-coordinate of the point where the graph of $kx+6y=30$ crosses the $x$-axis?
- Answer: 7.5
- Solution: Slopes: $-\frac{k}{6}=-\frac23$, so $k=4$. Then $4x=30$ and $x=7.5$.

## M2-Q5
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The polynomial $p(x)$ has degree 2, and its zeros are $x=-3$ and $x=\frac12$. The graph of $y=p(x)$ crosses the $y$-axis at the point $(0,-9)$. Which of the following could be $p(x)$?
- A: $2x^2+5x-3$
- B: $6x^2+15x-9$
- C: $6x^2-15x-9$
- D: $6x^2+15x+9$
- Answer: B
- Solution: $p(x)=a(x+3)(x-\frac12)$ and $p(0)=-\frac32a=-9$ gives $a=6$: $6x^2+15x-9$ (A has the right zeros but $p(0)=-3$; C has zeros $3$ and $-\frac12$; D has $p(0)=9$).

## M2-Q6
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A solid right circular cylinder has a volume of $200\pi$ cubic centimeters and a height of 8 centimeters. What is the total surface area, in square centimeters, of the cylinder, including both circular bases?
- A: $80\pi$
- B: $105\pi$
- C: $130\pi$
- D: $200\pi$
- Answer: C
- Solution: $\pi r^2(8)=200\pi$, so $r=5$. Surface area $=2\pi r^2+2\pi rh=50\pi+80\pi=130\pi$ (80$\pi$ is the side only; 105$\pi$ counts one base).

## M2-Q7
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A gardener is planting a rectangular bed that has an area of 12 square meters. Each tomato plant needs 0.6 square meter and each pepper plant needs 0.4 square meter. The gardener will plant $x$ tomato plants and $y$ pepper plants, using no more than the available space, and wants at least twice as many pepper plants as tomato plants. Which of the following systems of inequalities represents these conditions?
- A: $0.4x+0.6y\le12$ and $y\ge2x$
- B: $0.6x+0.4y\ge12$ and $y\ge2x$
- C: $0.6x+0.4y\le12$ and $x\ge2y$
- D: $0.6x+0.4y\le12$ and $y\ge2x$
- Answer: D
- Solution: Space used is $0.6x+0.4y\le12$; "at least twice as many peppers as tomatoes" is $y\ge2x$ (A swaps the space per plant; B reverses the space inequality; C swaps the roles of $x$ and $y$).

## M2-Q8
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: If $2^{x+1}\cdot4^{x-2}=64$, what is the value of $x$?
- Answer: 3
- Solution: $2^{x+1}\cdot2^{2x-4}=2^{3x-3}=2^6$, so $3x-3=6$ and $x=3$.

## M2-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A data set of 12 values has a mean of 50 and a standard deviation of 8. A 13th value, equal to 50, is added to the data set. Which of the following must be true of the new data set of 13 values?
- A: The mean is 50, and the standard deviation is less than 8.
- B: The mean is 50, and the standard deviation is exactly 8.
- C: The mean is 50, and the standard deviation is greater than 8.
- D: The mean is less than 50, and the standard deviation is less than 8.
- Answer: A
- Solution: A new value equal to the mean leaves the mean at 50 and adds no squared deviation, but increases the count, so the standard deviation decreases ($\sqrt{12/13}\cdot8\approx7.69$).

## M2-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the system below, $k$ is a constant. If the system has infinitely many solutions, what is the value of $k$?\dsp{$y=2x+7$}\dsp{$4x-2y=k$}
- A: $-7$
- B: $-14$
- C: $7$
- D: $14$
- Answer: B
- Solution: Substitute: $4x-2(2x+7)=-14$, so $k=-14$ makes the second equation the same line as the first (any other $k$ gives no solution).

## M2-Q11
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The point $(4,9)$ lies on the graph of $y=f(x)$ in the $xy$-plane. The function $g$ is defined by $g(x)=2f(x-1)-5$. The point $(a,b)$ lies on the graph of $y=g(x)$ and corresponds to the point $(4,9)$ on the graph of $f$. What is the value of $a+b$?
- Answer: 18
- Solution: $x-1=4$ gives $a=5$; $b=2f(4)-5=13$; $a+b=18$.

## M2-Q12
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: How many integers $x$ satisfy both $3x-7>8$ and $2x+5\le31$?
- A: $7$
- B: $9$
- C: $8$
- D: $13$
- Answer: C
- Solution: $x>5$ and $x\le13$, so $x=6,\dots,13$: 8 integers (9 counts $x=5$; 7 drops $x=13$).

## M2-Q13
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: A shipping company charges \$9 for the first kilogram of a package and a fixed amount for each additional kilogram or fraction of a kilogram. A package weighing 6.5 kilograms costs \$39 to ship. How much would it cost, in dollars, to ship a package weighing 12.2 kilograms?
- A: $69$
- B: $64$
- C: $65$
- D: $70$
- Answer: A
- Solution: Beyond the first kilogram, 6.5 kg has 5.5 kg, which is billed as 6 units: $9+6d=39$, $d=5$. For 12.2 kg the extra 11.2 kg is billed as 12 units: $9+5(12)=69$ (70 charges 12.2 units; 65 charges 11.2 units; 64 rounds the extra weight down).

## M2-Q14
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: A triangular garden plot $ABC$ has sides $AB=13$ meters, $BC=14$ meters, and $CA=15$ meters. A circular pond inside the plot is tangent to all three sides and touches side $\overline{BC}$ at point $P$. Point $P$ divides $\overline{BC}$ into two parts. What is the length, in meters, of the longer part?
- Figure:
```latex
\begin{tikzpicture}[scale=0.3]
\coordinate (B) at (0,0); \coordinate (C) at (14,0); \coordinate (A) at (5,12);
\draw[line width=0.7pt] (A)--(B)--(C)--cycle;
\draw[line width=0.6pt] (6,4) circle (4);
\fill (6,0) circle (0.14);
\node[below left] at (B) {$B$}; \node[below right] at (C) {$C$}; \node[above] at (A) {$A$};
\node[above,font=\small] at (6,0.2) {$P$};
\node[left,font=\small] at (2.4,6.2) {13}; \node[right,font=\small] at (9.8,6.2) {15};
\node[below,font=\small] at (7,-0.2) {14};
\end{tikzpicture}
```
- A: $6$
- B: $7$
- C: $9$
- D: $8$
- Answer: D
- Solution: Tangent segments from a vertex are equal. With tangent lengths $t_A,t_B,t_C$: $t_B+t_C=14$, $t_A+t_B=13$, $t_A+t_C=15$ give $t_A=7$, $t_B=6$, $t_C=8$. So $BP=6$, $PC=8$ (6 is the shorter part; 7 is the midpoint guess and $t_A$; 9 has no basis).

## M2-Q15
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: For a real number $x$, $\sqrt{x+7}+\sqrt{x-1}=4$. What is the value of $\sqrt{x+7}-\sqrt{x-1}$?
- Answer: 2
- Solution: Let $a=\sqrt{x+7}$ and $b=\sqrt{x-1}$. Then $a+b=4$ and $a^2-b^2=(x+7)-(x-1)=8$, so $a-b=\frac{8}{4}=2$ (no need to find $x$, which is 2).

## M2-Q16
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: At a school with 240 students, 150 students are in the band, 110 students are in the chorus, and 40 students are in neither. One student is selected at random from only those students who are in exactly one of the two groups. What is the probability that the selected student is in the band?
- A: $\frac{3}{5}$
- B: $\frac{9}{14}$
- C: $\frac{15}{26}$
- D: $\frac{5}{8}$
- Answer: B
- Solution: In at least one group: $240-40=200$, so both $=150+110-200=60$. Band only $=90$, chorus only $=50$; $\frac{90}{140}=\frac9{14}$ ($\frac35$ is $90/150$; $\frac{15}{26}$ forgets the overlap; $\frac58$ is $150/240$).

## M2-Q17
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: A rectangular garden bed has an area of 11 square meters, and its length is 6 meters more than its width. What is the perimeter, in meters, of the bed?
- A: $4\sqrt{5}$
- B: $2\sqrt{47}$
- C: $8\sqrt{5}$
- D: $24$
- Answer: C
- Solution: $\ell w=11$ and $\ell-w=6$, so $(\ell+w)^2=(\ell-w)^2+4\ell w=36+44=80$ and $\ell+w=4\sqrt5$; the perimeter is $2(\ell+w)=8\sqrt5$ ($4\sqrt5$ forgets to double; $2\sqrt{47}$ uses $36+11$; 24 assumes the whole-number sides $11$ and $1$, which differ by 10, not 6).

## M2-Q18
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: In the $xy$-plane, a line with a positive $x$-intercept and a positive $y$-intercept passes through the point $(6,4)$. The $x$-intercept is twice the $y$-intercept. What is the area, in square units, of the triangle formed by this line and the two axes?
- Answer: 49
- Solution: With $y$-intercept $b$ the line is $\frac{x}{2b}+\frac{y}{b}=1$. At $(6,4)$: $\frac{3}{b}+\frac4b=1$, so $b=7$ and the $x$-intercept is 14. Area $=\frac12(14)(7)=49$.

## M2-Q19
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: What is the sum of the $y$-coordinates of all points of intersection of the graphs of $y=x^2-3$ and $x^2+y^2=9$ in the $xy$-plane?
- A: $1$
- B: $-1$
- C: $4$
- D: $7$
- Answer: A
- Solution: $x^2=y+3$ gives $y^2+y-6=0$, so $y=2$ or $y=-3$. $y=2$ gives $x=\pm\sqrt5$ (two points); $y=-3$ gives $x=0$ (one point). Sum $=2+2-3=1$ ($-1$ counts each $y$-value once; 4 drops the point $(0,-3)$).

## M2-Q20
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: Positions along a straight highway are measured in kilometers from a town. A service station is at position $-1$ and a rest area is at position $3$. A cyclist at position $x$ is exactly twice as far from the rest area as from the service station. What is the sum of all possible values of $x$?
- A: $-5$
- B: $-\frac{5}{3}$
- C: $\frac{1}{3}$
- D: $-\frac{14}{3}$
- Answer: D
- Solution: $|x-3|=2|x+1|$ gives $x-3=2x+2$ ($x=-5$) or $x-3=-2x-2$ ($x=\frac13$); both work. Sum $=-\frac{14}{3}$ ($-5$ and $\frac13$ are single solutions; $-\frac53$ is their product).

## M2-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: A circular steel disc has a radius of 25 centimeters. Two parallel straight cuts are made across the disc, one 14 centimeters long and the other 40 centimeters long, with the center of the disc between the two cuts. What is the distance, in centimeters, between the two cuts?
- Figure:
```latex
\begin{tikzpicture}[scale=0.11]
\draw[line width=0.7pt] (0,0) circle (25);
\draw[line width=0.7pt] (-7,24)--(7,24);
\draw[line width=0.7pt] (-20,-15)--(20,-15);
\fill (0,0) circle (0.9);
\node[right,font=\small] at (1.6,0.2) {$O$};
\node[below,font=\small] at (0,23.6) {14};
\node[above,font=\small] at (0,-14.6) {40};
\end{tikzpicture}
```
- Answer: 39
- Solution: Distances from the center: $\sqrt{25^2-7^2}=24$ and $\sqrt{25^2-20^2}=15$. The center lies between the cuts, so the distance is $24+15=39$ (the cuts would be 9 apart if they were on the same side).

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: When the polynomial $p(x)$ is divided by $x-2$, the remainder is 5. When $p(x)$ is divided by $x+3$, the remainder is $-15$. When $p(x)$ is divided by $x^2+x-6$, the remainder is $ax+b$, where $a$ and $b$ are constants. What is the value of $b$?
- A: $-15$
- B: $-3$
- C: $4$
- D: $5$
- Answer: B
- Solution: $x^2+x-6=(x-2)(x+3)$, so $p(x)=(x-2)(x+3)q(x)+ax+b$. Then $p(2)=2a+b=5$ and $p(-3)=-3a+b=-15$, so $a=4$, $b=-3$ ($-15$ and 5 are the given remainders; 4 is $a$).
