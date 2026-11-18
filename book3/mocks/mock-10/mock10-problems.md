# Mock Test 10 — Source of truth (Book 3, ≈800, the capstone mock)

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
- Stem: A trail runner starts a climb at an elevation of 1,200 feet and gains 400 feet of elevation each hour. After how many hours will the runner reach an elevation of 3,200 feet?
- A: $8$
- B: $11$
- C: $5$
- D: $2{,}000$
- Answer: C
- Solution: $1200+400h=3200$ gives $h=5$ (8 divides 3,200 by 400 and ignores the starting elevation; 11 divides $3200+1200$ by 400; 2,000 is the elevation to be gained, not the time).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is equivalent to $(3x^{4})^{2}$?
- A: $9x^{8}$
- B: $3x^{8}$
- C: $9x^{6}$
- D: $6x^{8}$
- Answer: A
- Solution: Square both factors: $3^2x^{4\cdot2}=9x^8$ (3x⁸ forgets to square the 3; 9x⁶ adds the exponents; 6x⁸ doubles the 3).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: The lengths, in minutes, of six songs on a playlist are 3, 5, 4, 8, 6, and 4. What is the median length, in minutes, of the six songs?
- Answer: 4.5
- Solution: In order the lengths are 3, 4, 4, 5, 6, 8, so the median is the mean of 4 and 5, which is 4.5 (the mean is 5 and the mode is 4).

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A cube-shaped planter has a volume of 343 cubic inches. What is the length, in inches, of one edge of the planter?
- A: $\frac{343}{3}$
- B: $49$
- C: $14$
- D: $7$
- Answer: D
- Solution: $s^3=343$ gives $s=7$ (343/3 divides the volume by 3 as if it were $3s$; 49 is $s^2$; 14 doubles the edge).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: A charity needs 600 meal boxes packed. Volunteers have already packed 150 boxes and can pack 30 more boxes each hour. How many more hours will the volunteers need to reach 600 boxes?
- A: $5$
- B: $15$
- C: $20$
- D: $25$
- Answer: B
- Solution: $150+30h=600$ gives $30h=450$ and $h=15$ (5 divides the boxes already packed; 20 ignores the 150 already packed; 25 adds them).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The number of bacteria in a science-fair culture is modeled by $N(t)=40\cdot3^{t}$, where $t$ is the number of hours since the culture was started. According to the model, how many bacteria are in the culture at $t=2$?
- A: $240$
- B: $80$
- C: $360$
- D: $1{,}080$
- Answer: C
- Solution: $N(2)=40\cdot3^2=360$ (240 multiplies by $3\cdot2$; 80 uses $40\cdot2$; 1,080 is the value at $t=3$).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: A music streaming plan costs \$9 per month plus \$1.25 for each album downloaded that month. Lin's bill for one month was \$24. How many albums did she download that month?
- Answer: 12
- Solution: $9+1.25a=24$ gives $1.25a=15$ and $a=12$.

## M1-Q8
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A city is building a wheelchair ramp that rises 0.9 meter over a horizontal distance of 1.2 meters. What is the length, in meters, of the sloped surface of the ramp?
- A: $1.5$
- B: $2.1$
- C: $0.3$
- D: $2.25$
- Answer: A
- Solution: $\sqrt{0.9^2+1.2^2}=\sqrt{2.25}=1.5$ (2.1 adds the two legs; 0.3 subtracts them; 2.25 forgets the square root).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A science-fair team recorded the light exposure $x$, in minutes, and the height $y$, in millimeters, of 15 seedlings. The line of best fit is $y=6.4+0.38x$. One seedling had 50 minutes of exposure and a measured height of 27.1 millimeters. What is the residual for this seedling (measured height minus predicted height), in millimeters?
- A: $25.4$
- B: $-1.7$
- C: $20.7$
- D: $1.7$
- Answer: D
- Solution: The predicted height is $6.4+0.38(50)=25.4$, so the residual is $27.1-25.4=1.7$ (25.4 is the prediction itself; $-1.7$ subtracts in the wrong order; 20.7 subtracts only the intercept).

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A gardener has 18 square meters of bed space for tomatoes and peppers. Each square meter of tomatoes yields 9 kilograms, and each square meter of peppers yields 5 kilograms. All of the bed space is planted, and the total yield is 130 kilograms. How many square meters are planted with tomatoes?
- Answer: 10
- Solution: $t+p=18$ and $9t+5p=130$. Substituting $p=18-t$ gives $4t+90=130$, so $t=10$.

## M1-Q11
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: How many real solutions does the equation $\dfrac{x}{x-3}=2+\dfrac{3}{x-3}$ have?
- A: $1$
- B: $0$
- C: $2$
- D: $3$
- Answer: B
- Solution: Multiplying by $x-3$ gives $x=2(x-3)+3=2x-3$, so $x=3$. But $x=3$ makes the denominators zero, so it is extraneous and there are no solutions (1 keeps the extraneous root).

## M1-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The height, in meters, of a suspension-bridge cable above the deck is modeled by $h(x)=0.02x^{2}-1.2x+25$, where $x$ is the distance, in meters, from the left tower and $0\le x\le60$. What is the minimum height, in meters, of the cable above the deck?
- A: $25$
- B: $30$
- C: $7$
- D: $18$
- Answer: C
- Solution: The vertex is at $x=\frac{1.2}{0.04}=30$, and $h(30)=18-36+25=7$ (25 is the height at the tower; 30 is where the minimum occurs; 18 is only $0.02\cdot30^2$).

## M1-Q13
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A museum sells adult tickets for \$18 and child tickets for \$11. On one day the museum wants to collect at least \$900 and sell no more than 70 tickets in all. Which ordered pair $(a,c)$, where $a$ is the number of adult tickets and $c$ is the number of child tickets, satisfies both conditions?
- A: $(30,35)$
- B: $(20,40)$
- C: $(45,35)$
- D: $(25,30)$
- Answer: A
- Solution: Test $18a+11c\ge900$ and $a+c\le70$. For $(30,35)$: $925\ge900$ and $65\le70$. $(20,40)$ collects only \$800; $(45,35)$ sells 80 tickets; $(25,30)$ collects only \$780.

## M1-Q14
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: If $2^{a}=3$ and $2^{b}=5$, what is the value of $2^{3a-b}$?
- Answer: 5.4
- Solution: $2^{3a-b}=\dfrac{(2^a)^3}{2^b}=\dfrac{27}{5}=5.4$.

## M1-Q15
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The function $f$ is defined by $f(x)=x^{2}-8x+3$. If $f(a)=f(11)$ and $a\ne11$, what is the value of $a$?
- A: $3$
- B: $5$
- C: $8$
- D: $-3$
- Answer: D
- Solution: The graph is symmetric about $x=4$, so equal outputs come from $x=11$ and $x=8-11=-3$ (3 and 5 mirror the wrong axis; 8 is twice the axis value).

## M1-Q16
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: The table shows how 300 travelers booked a trip, by booking method and purpose of the trip. One traveler who booked on the website is chosen at random. What is the probability that the traveler's trip is for business?
- Figure:
```latex
\begin{tabular}{|l|c|c|}
\hline
 & Business & Leisure\\\hline
App & 54 & 96\\\hline
Website & 66 & 48\\\hline
Travel agent & 18 & 18\\\hline
\end{tabular}
```
- A: $\frac{11}{50}$
- B: $\frac{11}{19}$
- C: $\frac{11}{23}$
- D: $\frac{8}{19}$
- Answer: B
- Solution: 114 travelers booked on the website and 66 of them were traveling for business: $\frac{66}{114}=\frac{11}{19}$ ($\frac{11}{50}=\frac{66}{300}$ divides by all travelers; $\frac{11}{23}=\frac{66}{138}$ divides by all business trips; $\frac{8}{19}$ is the leisure share).

## M1-Q17
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A travel site charges a fixed booking fee plus the same nightly rate for every night of a hotel stay. A 3-night stay costs \$472 and a 5-night stay costs \$748. What is the booking fee, in dollars?
- Answer: 58
- Solution: The nightly rate is $\frac{748-472}{2}=138$, so the fee is $472-3(138)=58$.

## M1-Q18
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following is equivalent to $(3x-2)^{2}-(x+4)^{2}$?
- A: $8x^{2}-12$
- B: $8x^{2}-4x+20$
- C: $8x^{2}-20x-12$
- D: $4x^{2}-24x+36$
- Answer: C
- Solution: $(9x^2-12x+4)-(x^2+8x+16)=8x^2-20x-12$ (A squares each term separately, losing the middle terms; B forgets to distribute the minus sign to $8x+16$; D squares the difference $(3x-2)-(x+4)$).

## M1-Q19
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: Maya is 4 years older than twice Leo's age. In 6 years, the sum of their ages will be 49. How old is Maya now?
- A: $26$
- B: $32$
- C: $11$
- D: $37$
- Answer: A
- Solution: With Leo's age $L$, Maya is $2L+4$. Then $(L+6)+(2L+10)=49$ gives $L=11$, so Maya is 26 (32 is her age in 6 years; 11 is Leo's age; 37 is the sum of their current ages).

## M1-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: What is the sum of all solutions of the equation $(x-4)^{2}=3(x-4)$?
- A: $3$
- B: $7$
- C: $28$
- D: $11$
- Answer: D
- Solution: $(x-4)^2-3(x-4)=0$ gives $(x-4)(x-7)=0$, so $x=4$ or $x=7$ and the sum is 11 (7 divides both sides by $x-4$ and loses the solution $x=4$; 3 is the right side's constant; 28 is the product).

## M1-Q21
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: The two distinct lines $2x+ky=10$ and $kx+8y=20$ in the $xy$-plane are parallel, where $k$ is a constant. What is the value of $k$?
- Answer: -4
- Solution: Parallel lines have equal slopes: $-\frac2k=-\frac k8$, so $k^2=16$. For $k=4$ the lines are $2x+4y=10$ and $4x+8y=20$, which are the same line, not distinct parallel lines. For $k=-4$ they are $x-2y=5$ and $x-2y=-5$, which are distinct and parallel. So $k=-4$.

## M1-Q22
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: A regular hexagon is inscribed in a circle of radius 10, so all six vertices of the hexagon lie on the circle, as shown. What is the area of the region inside the circle and outside the hexagon?
- Figure:
```latex
\begin{tikzpicture}[scale=0.22]
\fill[badge!60] (0,0) circle (10);
\fill[white] (10,0)--(5,8.660254)--(-5,8.660254)--(-10,0)--(-5,-8.660254)--(5,-8.660254)--cycle;
\draw[line width=0.7pt] (0,0) circle (10);
\draw[line width=0.7pt] (10,0)--(5,8.660254)--(-5,8.660254)--(-10,0)--(-5,-8.660254)--(5,-8.660254)--cycle;
\draw[line width=0.5pt] (0,0)--(10,0); \fill (0,0) circle (0.25);
\node[above,font=\small] at (5,0) {10};
\end{tikzpicture}
```
- A: $100\pi-100\sqrt{3}$
- B: $100\pi-150\sqrt{3}$
- C: $100\pi-75\sqrt{3}$
- D: $100\pi-150$
- Answer: B
- Solution: The hexagon is six equilateral triangles of side 10, each with area $\frac{\sqrt3}{4}\cdot100=25\sqrt3$, so the hexagon has area $150\sqrt3$ and the region has area $100\pi-150\sqrt3$ (A and C count 4 or 3 triangles; D drops the $\sqrt3$).

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: A booking site charges a \$40 service fee plus \$85 for each ticket. Marta's total was \$380. How many tickets did she buy?
- A: $3$
- B: $4$
- C: $5$
- D: $340$
- Answer: B
- Solution: $40+85t=380$ gives $t=4$ (3 treats the fee as a second per-ticket charge, $380/125\approx3$; 5 adds the fee instead of subtracting it; 340 is the cost of the tickets, not their number).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $h$ is defined by $h(x)=3x^{2}-x+4$. What is the value of $h(-1)$?
- A: $8$
- B: $6$
- C: $14$
- D: $2$
- Answer: A
- Solution: $h(-1)=3(1)-(-1)+4=8$ (6 drops the sign change on $-x$; 14 squares $3\cdot(-1)$; 2 makes the squared term negative).

## M2-Q3
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: A rectangular herb garden measures 20 feet by 14 feet. A walkway of uniform width $w$ feet surrounds the garden, and the walkway alone has an area of 152 square feet. What is the value of $w$?
- A: $4$
- B: $19$
- C: $2$
- D: $76$
- Answer: C
- Solution: The outer rectangle is $(20+2w)$ by $(14+2w)$, so $(20+2w)(14+2w)-280=152$. This gives $w^2+17w-38=0$, so $(w+19)(w-2)=0$ and $w=2$ (4 adds $w$ instead of $2w$ to each side; 19 is the negative root with its sign dropped; 76 is half the area).

## M2-Q4
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A volunteer group assembles two kinds of kits for a shelter. Each type A kit holds 3 blankets and 2 bottles of water, and each type B kit holds 2 blankets and 5 bottles of water. The group uses exactly 62 blankets and exactly 100 bottles of water. How many kits did it assemble in all?
- Answer: 26
- Solution: $3a+2b=62$ and $2a+5b=100$. Eliminating $b$: $15a+10b=310$ and $4a+10b=200$, so $11a=110$, $a=10$ and $b=16$. In all there are $10+16=26$ kits.

## M2-Q5
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A recording studio charges \$55 per hour for the first 10 hours of a booking and \$40 per hour for each additional hour. A band has a budget of \$1,000. What is the greatest whole number of hours the band can book?
- A: $18$
- B: $22$
- C: $25$
- D: $21$
- Answer: D
- Solution: $550+40(h-10)\le1000$ gives $h\le21.25$, so 21 hours (18 charges every hour at \$55; 25 charges every hour at \$40; 22 rounds 21.25 up, which would cost \$1,030).

## M2-Q6
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A streaming service surveyed 40 subscribers about the number of playlists each one created last month. The table shows the results. How much greater is the median number of playlists than the mean number of playlists?
- Figure:
```latex
\begin{tabular}{|l|c|c|c|c|c|}
\hline
Playlists created & 0 & 1 & 2 & 3 & 4\\\hline
Subscribers & 5 & 8 & 7 & 12 & 8\\\hline
\end{tabular}
```
- A: $0.5$
- B: $0.25$
- C: $0.75$
- D: $2.5$
- Answer: B
- Solution: The mean is $\frac{0+8+14+36+32}{40}=2.25$. The 20th and 21st values are 2 and 3, so the median is 2.5, and $2.5-2.25=0.25$ (0.75 takes the median to be 3; 2.5 is the median itself; 0.5 compares it with a mean of 2).

## M2-Q7
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: At 10:00 a.m. a hiker is at an elevation of 2,400 feet, and at 12:30 p.m. she is at 3,000 feet. She climbs at a constant rate the whole time, starting at the trailhead, which has an elevation of 1,800 feet. At what time did she start?
- A: $7{:}30$ a.m.
- B: $7{:}00$ a.m.
- C: $8{:}00$ a.m.
- D: $8{:}30$ a.m.
- Answer: A
- Solution: She climbs $3000-2400=600$ feet in 2.5 hours, which is 240 feet per hour. Going from 1,800 to 2,400 feet is also 600 feet, so it took 2.5 hours and she started at 7:30 a.m. (8:00 a.m. and 8:30 a.m. come from assuming rates of 300 or 400 feet per hour; 7:00 a.m. from 200).

## M2-Q8
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: At a science fair, a team's profit, in dollars, from selling $x$ kits is $P(x)=-x^{2}+14x-24$, where $x$ is a whole number. For how many values of $x$ is the profit positive?
- A: $13$
- B: $11$
- C: $9$
- D: $10$
- Answer: C
- Solution: $P(x)=-(x-2)(x-12)>0$ exactly for $2<x<12$, so $x=3,4,\dots,11$, which is 9 values (11 counts the break-even values 2 and 12; 13 counts $x=0,\dots,12$; 10 includes one endpoint).

## M2-Q9
- Domain: GT
- Difficulty: M
- Type: GRID
- Stem: Dana is 1.5 meters tall. She stands 6 meters from the base of a lamppost on level ground, and her shadow is 3 meters long. She then walks 4 meters directly away from the lamppost. How long, in meters, is her shadow now?
- Answer: 5
- Solution: The lamp height $H$ satisfies $\frac{H}{6+3}=\frac{1.5}{3}$, so $H=4.5$. After walking, with shadow length $s$: $\frac{4.5}{10+s}=\frac{1.5}{s}$, so $4.5s=15+1.5s$ and $s=5$ (the shadow does not stay 3 m long, and it does not grow in proportion to the distance).

## M2-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A volunteer spends exactly \$100 on notebooks at \$7 each and pens at \$4 each, and she buys at least one of each item. In how many different ways can she make the purchase so that she buys more pens than notebooks?
- A: $1$
- B: $3$
- C: $4$
- D: $2$
- Answer: D
- Solution: $7n+4p=100$ needs $n$ to be a multiple of 4: $(n,p)=(4,18),(8,11),(12,4)$. Pens exceed notebooks in the first two only, so 2 (3 forgets the condition on pens; 4 includes $n=0$).

## M2-Q11
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A charity gala sells corporate tables for \$480 and individual tickets for \$45. The gala needs to collect at least \$6,000, and the hall holds at most 120 guests. Each table seats 8 guests and each individual ticket admits 1 guest. Which ordered pair $(t,i)$, where $t$ is the number of tables and $i$ is the number of individual tickets, satisfies both conditions?
- A: $(6,60)$
- B: $(12,30)$
- C: $(10,30)$
- D: $(8,40)$
- Answer: C
- Solution: Test $480t+45i\ge6000$ and $8t+i\le120$. $(10,30)$ gives \$6,150 and 110 guests. $(6,60)$ and $(8,40)$ seat 108 and 104 guests but collect only \$5,580 and \$5,640; $(12,30)$ collects \$7,110 but seats 126 guests.

## M2-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The graph of $y=x^{2}-4x+1$ crosses the $x$-axis at $x=r$ and $x=s$. What is the value of $(r+3)(s+3)$?
- A: $22$
- B: $13$
- C: $10$
- D: $16$
- Answer: A
- Solution: $r+s=4$ and $rs=1$, so $(r+3)(s+3)=rs+3(r+s)+9=1+12+9=22$ (13 forgets the +9; 10 is $(r+s)+6$; 16 is $rs+3(r+s)+3$).

## M2-Q13
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The functions $f$ and $g$ are defined by $f(x)=x^{2}-6x+14$ and $g(x)=x^{2}-4x+1$. What is the minimum value of $g(f(x))$?
- A: $-3$
- B: $5$
- C: $41$
- D: $6$
- Answer: D
- Solution: $f(x)=(x-3)^2+5\ge5$, so the inputs to $g$ are all at least 5. On $[5,\infty)$ the function $g$ is increasing (its vertex is at 2), so the minimum is $g(5)=25-20+1=6$, reached at $x=3$ ($-3$ is the minimum of $g$ alone, which $g(f(x))$ never reaches; 5 is the minimum of $f$; 41 is $f(g(2))$).

## M2-Q14
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A greenhouse harvests only tomatoes and peppers. From Year 1 to Year 2 the tomato harvest rose 20\%, the pepper harvest fell 10\%, and the total harvest rose 6\% to 1,590 kilograms. How many kilograms of peppers were harvested in Year 2?
- A: $700$
- B: $630$
- C: $800$
- D: $960$
- Answer: B
- Solution: The Year 1 total was $1590/1.06=1500$. With $t$ kg of tomatoes in Year 1, $1.2t+0.9(1500-t)=1590$, so $0.3t=240$ and $t=800$. Year 1 peppers were 700, so Year 2 peppers were $0.9(700)=630$ (700 and 800 are the Year 1 pepper and tomato amounts; 960 is the Year 2 tomato amount).

## M2-Q15
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: A cubic polynomial $p$ satisfies $p(1)=p(3)=p(5)=7$ and $p(0)=-8$. What is the value of $p(6)$?
- Answer: 22
- Solution: $p(x)-7$ has zeros at 1, 3 and 5, so $p(x)-7=a(x-1)(x-3)(x-5)$. At $x=0$: $-15a=-15$, so $a=1$. Then $p(6)=7+5\cdot3\cdot1=22$.

## M2-Q16
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: Under a health plan, a patient whose bill $B$ is at least the deductible $d$ owes $P=d+r(B-d)$ dollars, where $r$ is the patient's share, as a decimal, of the amount above the deductible. A \$3,000 bill left a patient owing \$1,100, and a \$7,000 bill left a patient owing \$1,900. The plan also stops the patient's cost at \$2,000 per bill. What is the least bill, in dollars, for which the patient owes the full \$2,000?
- A: $6{,}875$
- B: $9{,}375$
- C: $7{,}500$
- D: $10{,}000$
- Answer: C
- Solution: The slope gives $r=\frac{1900-1100}{4000}=0.2$. Then $1100=d+0.2(3000-d)=0.8d+600$, so $d=625$. Setting $625+0.2(B-625)=2000$ gives $B=7500$ (6,875 is $B-d$; 9,375 is $2000/0.2-625$; 10,000 ignores the deductible, $2000/0.2$).

## M2-Q17
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In right triangle $ABC$, the right angle is at $C$, the hypotenuse $AB$ has length 25, and the area of the triangle is 84. A circle with its center $P$ on $\overline{AB}$ is tangent to both $\overline{AC}$ and $\overline{BC}$, as shown. What is the radius of the circle?
- Figure:
```latex
\begin{tikzpicture}[scale=0.14]
\draw[line width=0.7pt] (0,0)--(24,0)--(0,7)--cycle;
\draw[line width=0.5pt] (0,1.2)--(1.2,1.2)--(1.2,0);
\draw[line width=0.6pt,fill=badge!50,fill opacity=0.6] (5.419355,5.419355) circle (5.419355);
\fill (5.419355,5.419355) circle (0.35);
\node[below left,font=\small] at (0,0) {$C$};
\node[below right,font=\small] at (24,0) {$A$};
\node[above left,font=\small] at (0,7) {$B$};
\node[above right,font=\small,inner sep=1pt] at (5.6,5.6) {$P$};
\end{tikzpicture}
```
- A: $\frac{168}{31}$
- B: $\frac{168}{25}$
- C: $3$
- D: $\frac{84}{31}$
- Answer: A
- Solution: With legs $a,b$: $a^2+b^2=625$ and $ab=168$, so $(a+b)^2=625+336=961$ and $a+b=31$. The radius $r$ splits the area: $\frac12ar+\frac12br=84$, so $r=\frac{168}{31}$ ($\frac{168}{25}$ is the altitude to the hypotenuse; 3 is the radius of the inscribed circle; $\frac{84}{31}$ forgets the factor $\frac12$ on both legs).

## M2-Q18
- Domain: PSDA
- Difficulty: H
- Type: GRID
- Stem: A city surveyed residents about a proposed pedestrian plaza. Of the residents surveyed, 40\% commute by car, 35\% commute by transit, and 25\% commute by bike or on foot. Among car commuters, 30\% support the plaza, and among transit commuters, 60\% support it. A supporter of the plaza is selected at random, and the probability that this supporter commutes by car is $4/15$. What percent of the bike-or-foot commuters support the plaza? (Enter the number only.)
- Answer: 48
- Solution: Car supporters are $0.4\cdot0.3=0.12$ of all residents. Since this is $\frac4{15}$ of all supporters, supporters are $0.45$ of all residents. Transit supporters are $0.35\cdot0.6=0.21$, so bike-or-foot supporters are $0.45-0.12-0.21=0.12$, and $\frac{0.12}{0.25}=0.48$, or 48\%.

## M2-Q19
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: What is the sum of all real solutions of the equation $|x^{2}-2x-8|=4x$?
- A: $4$
- B: $5+\sqrt{17}$
- C: $1+\sqrt{17}$
- D: $3+\sqrt{17}$
- Answer: B
- Solution: Since $|\cdot|\ge0$, solutions need $x\ge0$. $x^2-2x-8=4x$ gives $x=3\pm\sqrt{17}$, and only $3+\sqrt{17}$ is non-negative. $x^2-2x-8=-4x$ gives $x=2$ or $x=-4$, and only $2$ works. The sum is $5+\sqrt{17}$ (4 sums all four candidates; $1+\sqrt{17}$ keeps $-4$ and drops $3-\sqrt{17}$; $3+\sqrt{17}$ uses only the first case).

## M2-Q20
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the graph of $x^{2}+y^{2}-10x+4y+k=0$, where $k$ is an integer, is a circle that intersects the $x$-axis at two points and does not intersect the $y$-axis at all. How many integer values of $k$ are possible?
- A: $19$
- B: $21$
- C: $25$
- D: $20$
- Answer: D
- Solution: Completing squares, $(x-5)^2+(y+2)^2=29-k$. The center is 2 units from the $x$-axis and 5 units from the $y$-axis. Two points on the $x$-axis need $r>2$, so $k<25$; missing the $y$-axis needs $r<5$, so $k>4$ (tangent cases are excluded). The integers $5,\dots,24$ give 20 values (21 includes a tangent value; 19 drops one end; 25 counts from 0).

## M2-Q21
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: For how many real values of $m$ does the system below have exactly one solution $(x,y)$ in the $xy$-plane?\dsp{$|x-3|=|y+2|$}\dsp{$y=mx-8$}
- Answer: 3
- Solution: $|x-3|=|y+2|$ is the pair of lines $y=x-5$ and $y=1-x$, crossing at $(3,-2)$. The line $y=mx-8$ meets the pair exactly once if it passes through the crossing point ($-2=3m-8$, so $m=2$) or is parallel to one of the two lines ($m=1$ or $m=-1$). Otherwise it meets each line once, giving two solutions. So there are 3 values.

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: In the $xy$-plane, the system below has exactly three distinct solutions $(x,y)$, where $k$ is a constant. What is the value of $k$?\dsp{$y=x^{2}-4$}\dsp{$x^{2}+y^{2}=k$}
- A: $4$
- B: $\frac{15}{4}$
- C: $16$
- D: $20$
- Answer: C
- Solution: Substituting $x^2=y+4$ gives $y^2+y+4-k=0$, and each root $y>-4$ gives two values of $x$, while $y=-4$ gives only $x=0$. Three solutions need $y=-4$ to be a root: $16-4+4-k=0$, so $k=16$. The other root is $y=3$ (the roots sum to $-1$), giving $(0,-4)$ and $(\pm\sqrt7,3)$ (15/4 makes the discriminant zero, which gives only two solutions; $k=4$ gives four solutions; $k=20$ gives two).
