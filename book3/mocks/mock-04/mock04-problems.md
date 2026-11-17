# Mock Test 4 — Source of truth (Book 3, ≈800)

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
- Stem: If $\dfrac{x}{4}+9=17$, what is the value of $x$?
- A: $8$
- B: $26$
- C: $32$
- D: $104$
- Answer: C
- Solution: $\frac{x}{4}=8$, so $x=32$ (8 stops one step early; 26 adds 9 instead of subtracting; 104 adds 9, then multiplies by 4).

## M1-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: The function $h$ is defined by $h(x)=x^{2}-5$. What is the value of $h(6)-h(2)$?
- A: $11$
- B: $30$
- C: $31$
- D: $32$
- Answer: D
- Solution: $h(6)=31$ and $h(2)=-1$, so the difference is $32$ (11 is $h(6-2)$; 30 adds the two values; 31 is only $h(6)$).

## M1-Q3
- Domain: PSDA
- Difficulty: E
- Type: GRID
- Stem: A recipe uses 3 cups of broth for every 2 cups of rice. How many cups of broth are needed for 14 cups of rice?
- Answer: 21
- Solution: $14\cdot\frac32=21$.

## M1-Q4
- Domain: GT
- Difficulty: E
- Type: MC
- Stem: A circular tabletop has an area of $81\pi$ square inches. What is the circumference, in inches, of the tabletop?
- A: $9\pi$
- B: $18\pi$
- C: $36\pi$
- D: $81\pi$
- Answer: B
- Solution: $\pi r^2=81\pi$ gives $r=9$, so $C=2\pi r=18\pi$ (36$\pi$ uses the diameter in $2\pi r$; 81$\pi$ is the area).

## M1-Q5
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: What is the slope of the line in the $xy$-plane with equation $4x-2y=10$?
- A: $-5$
- B: $-2$
- C: $2$
- D: $4$
- Answer: C
- Solution: $y=2x-5$, so the slope is $2$ (-5 is the $y$-intercept, -2 is a sign slip, 4 is the coefficient of $x$).

## M1-Q6
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: Which of the following is a factor of $x^{2}+2x-24$?
- A: $x-6$
- B: $x-4$
- C: $x+4$
- D: $x+8$
- Answer: B
- Solution: $x^2+2x-24=(x+6)(x-4)$ (the signs are swapped in A and C).

## M1-Q7
- Domain: ALG
- Difficulty: E
- Type: GRID
- Stem: In the $xy$-plane, a line has slope 3 and passes through the point $(2,5)$. The line crosses the $y$-axis at the point $(0,b)$. What is the value of $b$?
- Answer: -1
- Solution: $y-5=3(x-2)$, so $y=3x-1$ and $b=-1$.

## M1-Q8
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: A baker's sourdough starter doubles in mass every 6 hours. If the starter has a mass of 30 grams now, what will its mass be, in grams, 18 hours from now?
- A: $60$
- B: $90$
- C: $240$
- D: $540$
- Answer: C
- Solution: Three doublings: $30\cdot2^3=240$ (60 doubles once; 90 triples; 540 multiplies by 18).

## M1-Q9
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A scatterplot of 40 vineyards shows the annual rainfall $x$, in inches, and the grape yield $y$, in tons per acre. The line of best fit passes through the points $(20,3.1)$ and $(36,4.7)$. According to the line of best fit, what is the predicted yield, in tons per acre, of a vineyard that receives 30 inches of rainfall?
- A: $3.0$
- B: $4.1$
- C: $4.7$
- D: $5.3$
- Answer: B
- Solution: Slope $=\frac{1.6}{16}=0.1$; $y=3.1+0.1(30-20)=4.1$ (3.0 is $0.1\cdot30$ with no intercept; 4.7 reads the nearer given point; 5.3 moves the wrong way from $(36,4.7)$).

## M1-Q10
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A greenhouse uses large trays that hold 24 seedlings each and small trays that hold 15 seedlings each. A total of 40 trays hold 762 seedlings. How many large trays are there?
- A: $18$
- B: $20$
- C: $22$
- D: $32$
- Answer: A
- Solution: $L+S=40$ and $24L+15S=762$ give $9L=162$, $L=18$ (22 is the number of small trays; 20 is $762/39$ rounded; 32 is $762/24$ rounded).

## M1-Q11
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: What is the greatest integer $x$ that satisfies the inequality $4-3(x-2)>-14$?
- Answer: 7
- Solution: $10-3x>-14$, so $x<8$; the greatest integer is $7$ (8 would make the inequality an equality, not strict).

## M1-Q12
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The table shows four values of the function $f$. Which of the following equations defines $f$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|c|}
\hline
$x$ & 0 & 1 & 2 & 3\\\hline
$f(x)$ & 6 & 9 & 13.5 & 20.25\\\hline
\end{tabular}
```
- A: $f(x)=6(1.5)^{x}$
- B: $f(x)=6+3x$
- C: $f(x)=9(1.5)^{x}$
- D: $f(x)=6(3)^{x}$
- Answer: A
- Solution: Each value is $1.5$ times the one before and $f(0)=6$. (B is linear but $f(2)\ne12$; C has $f(0)=9$; D grows too fast.)

## M1-Q13
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A rectangular fish tank is 60 centimeters long, 30 centimeters wide, and 40 centimeters tall. The tank is filled with water to $\frac34$ of its height. How many liters of water are in the tank? (1 liter $=1{,}000$ cubic centimeters)
- A: $54$
- B: $72$
- C: $540$
- D: $54{,}000$
- Answer: A
- Solution: $60\cdot30\cdot30=54{,}000$ cm$^3=54$ L (72 is the full tank; 54,000 is not converted to liters; 540 is a decimal-place slip).

## M1-Q14
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The table gives three values of the quadratic function $g$. What is the value of $g(7)$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|}
\hline
$x$ & 1 & 3 & 5\\\hline
$g(x)$ & 11 & 3 & 11\\\hline
\end{tabular}
```
- Answer: 35
- Solution: $g(1)=g(5)$, so the axis is $x=3$ and the vertex is $(3,3)$. $g(x)=a(x-3)^2+3$ with $4a+3=11$, $a=2$; $g(7)=2\cdot16+3=35$.

## M1-Q15
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A farmer recorded the wheat yield, in bushels per acre, of each of 12 fields. The mean yield was 31, the median yield was 29, and the two highest yields were 80 and 44. The farmer then found that the 80 was a recording error and that the correct yield for that field was 50. What are the mean and the median of the corrected data?
- A: Mean 31, median 29
- B: Mean 28.5, median 26.5
- C: Mean 33.5, median 29
- D: Mean 28.5, median 29
- Answer: D
- Solution: The total drops by 30, so the mean drops by $30/12=2.5$ to $28.5$. The new value 50 is still the highest (above 44), so the middle two values, and the median, do not change. (A forgets to recompute the mean; B moves the median too; C moves the mean the wrong way.)

## M1-Q16
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: In the $xy$-plane, the line $y=ax+b$ passes through the points $(-1,7)$ and $(3,-5)$, where $a$ and $b$ are constants. What is the value of $a-b$?
- A: $-12$
- B: $-7$
- C: $1$
- D: $7$
- Answer: B
- Solution: $a=\frac{-5-7}{3-(-1)}=-3$; then $7=-3(-1)+b$ gives $b=4$, so $a-b=-7$ ($-12=ab$, $1=a+b$, $7=b-a$).

## M1-Q17
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: Which of the following is equivalent to $\dfrac{x}{x+2}+\dfrac{3}{x-1}$, where $x\ne-2$ and $x\ne1$?
- A: $\dfrac{x+3}{2x+1}$
- B: $\dfrac{x^{2}-x+3}{x^{2}+x-2}$
- C: $\dfrac{x^{2}+5x-3}{x^{2}+x-2}$
- D: $\dfrac{x^{2}+2x+6}{x^{2}+x-2}$
- Answer: D
- Solution: Common denominator $(x+2)(x-1)$: numerator $x(x-1)+3(x+2)=x^2+2x+6$. (A adds tops and bottoms; B forgets to multiply the 3 by $x+2$; C multiplies by the wrong factors.)

## M1-Q18
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: The intensity $I$ of the sound from a speaker, in watts per square meter, is inversely proportional to the square of the distance $d$, in meters, from the speaker. At a distance of 4 meters the intensity is 0.09. At what distance, in meters, is the intensity 0.01?
- Answer: 12
- Solution: $I=k/d^2$, $k=0.09\cdot16=1.44$; $1.44/d^2=0.01$ gives $d^2=144$, $d=12$.

## M1-Q19
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A pottery kiln starts at 600 degrees Fahrenheit. For its first 150 minutes it heats at a constant 4 degrees per minute, and after that it heats at a constant 3 degrees per minute. How many minutes after the kiln starts does it first reach 1,800 degrees?
- A: $200$
- B: $300$
- C: $350$
- D: $400$
- Answer: C
- Solution: After 150 minutes: $600+600=1200$. The remaining $600$ degrees at 3 per minute take $200$ minutes, so $350$ in all (300 uses 4 per minute all the way; 400 uses 3 all the way; 200 counts only the second stage).

## M1-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The function $f$ is defined by $f(x)=x^{2}-6x$. For what value of $x$ is $f(x+2)-f(x)=16$?
- A: $2$
- B: $4$
- C: $6$
- D: $8$
- Answer: C
- Solution: $f(x+2)=x^2-2x-8$, so $f(x+2)-f(x)=4x-8=16$ and $x=6$ (4 drops the $-8$; 2 has a sign slip; 8 doubles the answer).

## M1-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: A sector of a circle has radius 10 and a central angle of $216^{\circ}$. Its two straight edges are brought together, with no overlap, to form the lateral surface of a cone. What is the height of the cone?
- Answer: 8
- Solution: The arc length $\frac{216}{360}\cdot2\pi\cdot10=12\pi$ becomes the base circumference, so the base radius is 6. The slant height is 10, so $h=\sqrt{100-36}=8$.

## M1-Q22
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: A rectangular room is 5 feet longer than it is wide. In a renovation, 3 feet are added to both the length and the width, and the floor area increases by 66 square feet. What is the perimeter, in feet, of the original room?
- A: $7$
- B: $12$
- C: $19$
- D: $38$
- Answer: D
- Solution: $(w+3)(w+8)-w(w+5)=6w+24=66$, $w=7$, length 12, perimeter $38$ (7 is the width, 12 the length, 19 the half-perimeter).

# MODULE 2 — harder route (22 questions; Easy Q1–2, Medium Q3–12, Hard Q13–22)

## M2-Q1
- Domain: ALG
- Difficulty: E
- Type: MC
- Stem: Which of the following is the solution to the inequality $6-3x\ge21$?
- A: $x\ge-5$
- B: $x\ge5$
- C: $x\le5$
- D: $x\le-5$
- Answer: D
- Solution: $-3x\ge15$; dividing by $-3$ reverses the inequality: $x\le-5$ (A forgets to reverse; B, C lose the sign).

## M2-Q2
- Domain: ADV
- Difficulty: E
- Type: MC
- Stem: For $x>0$, which of the following is equivalent to $\sqrt{49x^{8}}$?
- A: $49x^{4}$
- B: $7x^{6}$
- C: $7x^{16}$
- D: $7x^{4}$
- Answer: D
- Solution: $\sqrt{49}=7$ and $\sqrt{x^8}=x^4$ (A leaves the 49; B subtracts 2 from the exponent; C squares instead of taking the root).

## M2-Q3
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: The population of a small farming town has changed at a constant rate. It was 14,200 in 2010 and 12,700 in 2020. According to this linear model, in what year will the population reach 10,000?
- A: $2028$
- B: $2038$
- C: $2048$
- D: $2066$
- Answer: B
- Solution: The population falls 150 per year; $14{,}200-150t=10{,}000$ gives $t=28$, so the year is $2038$ (2028 counts 18 years from 2010; 2048 counts 28 years from 2020; 2066 uses the slope $1500/20=75$).

## M2-Q4
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: In the $xy$-plane, the line $kx+3y=12$ is perpendicular to the line $2x-5y=7$, where $k$ is a constant. What is the value of $k$?
- Answer: 7.5
- Solution: Slopes are $-\frac k3$ and $\frac25$. Perpendicular: $-\frac k3\cdot\frac25=-1$, so $k=\frac{15}{2}=7.5$.

## M2-Q5
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The table gives four values of the quadratic function $f$. What is the value of $f(10)$?
- Figure:
```latex
\begin{tabular}{|c|c|c|c|c|}
\hline
$x$ & 1 & 2 & 3 & 4\\\hline
$f(x)$ & 7 & 13 & 25 & 43\\\hline
\end{tabular}
```
- A: $61$
- B: $270$
- C: $277$
- D: $337$
- Answer: C
- Solution: The second differences are constant ($6, 12, 18$ gives 6), so $a=3$. $f(x)=3x^2-3x+7$ and $f(10)=277$ (61 continues the first difference of 6 as if the table were linear; 270 drops the constant 7; 337 has the sign of $b$ wrong).

## M2-Q6
- Domain: PSDA
- Difficulty: M
- Type: MC
- Stem: A museum builds a model of a cylindrical water tower at a scale of 1 to 50, so every length on the real tower is 50 times the corresponding length on the model. The model's tank holds 2.4 liters when full. How many cubic meters does the real tower's tank hold when full? (1 cubic meter $=1{,}000$ liters)
- A: $6$
- B: $300$
- C: $6{,}000$
- D: $300{,}000$
- Answer: B
- Solution: Volume scales by $50^3=125{,}000$: $2.4\cdot125{,}000=300{,}000$ L $=300$ m$^3$ (300,000 is not converted; 6 and 6,000 scale the volume by $50^2$).

## M2-Q7
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A storage tank holds 900 liters of irrigation water. A pump drains it at a constant 18 liters per minute. Fifteen minutes after the first pump starts, a second pump that drains 12 liters per minute is also switched on, and both pumps keep running. How many minutes after the second pump is switched on will the tank be empty?
- A: $21$
- B: $30$
- C: $36$
- D: $50$
- Answer: A
- Solution: After 15 minutes, $900-270=630$ L remain; both pumps drain $30$ L/min, so $630/30=21$ min (36 is the time since the first pump started; 30 treats both pumps as running from the start; 50 is $900/18$).

## M2-Q8
- Domain: ALG
- Difficulty: M
- Type: GRID
- Stem: A beekeeper sells honey for \$12 per jar at a weekend market. She pays a \$150 booth fee, and 20\% of her sales revenue goes to the market organizers. Her profit is her revenue minus the booth fee minus the organizers' 20\% share. What is the least number of jars she must sell so that her profit is at least \$400?
- Answer: 58
- Solution: Profit $=0.8(12n)-150=9.6n-150\ge400$, so $n\ge57.3$; the least whole number is 58.

## M2-Q9
- Domain: GT
- Difficulty: M
- Type: MC
- Stem: A gable roof covers a rectangular building that is 32 feet wide and 40 feet long. The two sloped faces of the roof are congruent rectangles, and the roof has a pitch of 9 to 12, meaning it rises 9 feet for every 12 feet of horizontal run. Ignoring any overhang, what is the total area, in square feet, of the two sloped faces?
- A: $960$
- B: $1280$
- C: $1600$
- D: $2240$
- Answer: C
- Solution: Each face spans a horizontal run of 16 ft, so the rise is 12 ft and the slope length is $\sqrt{16^2+12^2}=20$ ft; area $=2\cdot20\cdot40=1600$ (960 uses the rise 12; 1280 uses the run 16; 2240 adds run and rise).

## M2-Q10
- Domain: ADV
- Difficulty: M
- Type: MC
- Stem: The frequency, in hertz, of a musical note that is $n$ semitones above a reference note of 440 hertz is $f(n)=440\cdot2^{n/12}$. A certain note has a frequency of 1,320 hertz. Which of the following is closest to the number of semitones that note is above the reference note?
- A: $3$
- B: $19$
- C: $24$
- D: $36$
- Answer: B
- Solution: $2^{n/12}=3$, so $n=12\log_2 3\approx19.02$ (3 is the frequency ratio; 36 is $12\cdot3$; 24 is two octaves, a ratio of 4).

## M2-Q11
- Domain: ALG
- Difficulty: M
- Type: MC
- Stem: A farmer borrows $P$ dollars at a simple annual interest rate $r$ (written as a decimal). After $t$ years the total amount owed is $A=P(1+rt)$. Which of the following expresses $r$ in terms of $A$, $P$, and $t$?
- A: $r=\dfrac{A}{Pt}-1$
- B: $r=\dfrac{A-P}{t}$
- C: $r=\dfrac{A}{P}-t$
- D: $r=\dfrac{A-P}{Pt}$
- Answer: D
- Solution: $A-P=Prt$, so $r=\frac{A-P}{Pt}$ (A subtracts 1 from the wrong quantity; B drops $P$; C subtracts $t$ instead of dividing).

## M2-Q12
- Domain: ADV
- Difficulty: M
- Type: GRID
- Stem: If $x>0$ and $\dfrac{\sqrt[3]{x^{2}}\cdot x^{3/4}}{\sqrt{x}}=x^{p}$, what is the value of $p$?
- Answer: 11/12
- Solution: $p=\frac23+\frac34-\frac12=\frac{8+9-6}{12}=\frac{11}{12}$.

## M2-Q13
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: An orchard has 500 apple trees of two varieties, Gala and Fuji. The partially completed table classifies the trees by variety and by whether the tree has fire blight. Exactly 25\% of the Gala trees have fire blight. If one tree is selected at random from the trees that do not have fire blight, what is the probability that it is a Fuji tree?
- Figure:
```latex
\begin{tabular}{|l|c|c|c|}
\hline
 & Blight & No blight & Total\\\hline
Gala & & & 200\\\hline
Fuji & & & 300\\\hline
Total & 140 & & 500\\\hline
\end{tabular}
```
- A: $\frac{7}{12}$
- B: $\frac{3}{5}$
- C: $\frac{9}{14}$
- D: $\frac{7}{10}$
- Answer: A
- Solution: Gala with blight $=50$, so Fuji with blight $=90$ and Fuji without blight $=210$. Trees without blight $=500-140=360$; $\frac{210}{360}=\frac7{12}$. (3/5 is the share of Fuji among all trees; 9/14 is $\frac{90}{140}$, Fuji among blighted trees; 7/10 is $\frac{210}{300}$, the share of Fuji trees that are healthy.)

## M2-Q14
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: The graph of $y=x^{2}-4x+9$ in the $xy$-plane is translated 5 units to the left and 2 units down. The resulting graph is then reflected across the vertical line $x=2$. The final graph has equation $y=x^{2}+bx+c$, where $b$ and $c$ are constants. What is the value of $b+c$?
- A: $6$
- B: $18$
- C: $38$
- D: $52$
- Answer: C
- Solution: The vertex $(2,5)$ moves to $(-3,3)$, then reflects across $x=2$ to $(7,3)$. The parabola still opens upward: $y=(x-7)^2+3=x^2-14x+52$, so $b+c=38$. (6 reflects across the $y$-axis instead, giving vertex $(3,3)$; 18 skips the reflection; 52 is only $c$.)

## M2-Q15
- Domain: ADV
- Difficulty: H
- Type: GRID
- Stem: The graph of $y=-x^{2}+6x+c$ lies on or below the line $y=2x-5$ for every value of $x$ in the $xy$-plane, where $c$ is a constant. What is the greatest possible value of $c$?
- Answer: -9
- Solution: Need $-x^2+6x+c\le2x-5$ for all $x$, i.e. $-x^2+4x+c+5\le0$. The left side has maximum value $c+9$ (at $x=2$), so $c\le-9$; the greatest value is $-9$.

## M2-Q16
- Domain: GT
- Difficulty: H
- Type: MC
- Stem: A right square pyramid has a base with edge length 12, and each of its four lateral edges has length 11. What is the volume of the pyramid?
- A: $336$
- B: $48\sqrt{85}$
- C: $528$
- D: $1008$
- Answer: A
- Solution: The center of the base is $6\sqrt2$ from each base vertex, so $h^2=121-72=49$, $h=7$ and $V=\frac13\cdot144\cdot7=336$. (48$\sqrt{85}$ uses half the base edge, 6, instead of half the diagonal; 528 uses the lateral edge as the height; 1008 forgets the $\frac13$.)

## M2-Q17
- Domain: ALG
- Difficulty: H
- Type: MC
- Stem: A cook has 50 liters of syrup that is 20\% sugar by volume. She boils off water until the syrup is 25\% sugar. She then stirs in $y$ liters of a 10\% sugar syrup, and the final mixture has the same sugar concentration as the original 50 liters. What is the total volume, in liters, of the final mixture?
- A: $20$
- B: $40$
- C: $60$
- D: $70$
- Answer: C
- Solution: The sugar is $10$ L; after boiling the volume is $40$ L. Then $10+0.1y=0.2(40+y)$ gives $y=20$ and the total is $60$ L. (20 is $y$; 40 is the volume after boiling; 70 forgets the boiled-off water.)

## M2-Q18
- Domain: ALG
- Difficulty: H
- Type: GRID
- Stem: The graph of the linear function $f$ passes through the points $(2,5)$ and $(6,17)$. The linear function $g$ is defined so that $g(f(x))=4x-3$ for all $x$. For what value of $x$ does $g(x)=f(x)$?
- Answer: -2/5
- Solution: $f(x)=3x-1$. With $u=3x-1$, $x=\frac{u+1}{3}$, so $g(u)=\frac{4(u+1)}{3}-3=\frac{4u-5}{3}$. Setting $\frac{4x-5}{3}=3x-1$ gives $4x-5=9x-3$, $x=-\frac25$.

## M2-Q19
- Domain: PSDA
- Difficulty: H
- Type: MC
- Stem: A music teacher records how the number of errors $E$ in a piece depends on the number of rehearsals $r$. The scatterplot shows the errors falling quickly at first and then more slowly, and the teacher models the data with the exponential function $E=a\cdot b^{r}$, whose graph passes through the points $(1,72)$ and $(4,36.864)$. According to the model, what is the least whole number of rehearsals after which the predicted number of errors is below 10?
- A: $4$
- B: $7$
- C: $9$
- D: $10$
- Answer: D
- Solution: $b^3=\frac{36.864}{72}=0.512$, so $b=0.8$ and $a=90$. $90(0.8)^r<10$ needs $r>9.85$, so $r=10$. (4 uses $b=0.512$ for one rehearsal; 7 uses a straight line through the two points; 9 rounds $9.85$ down, but $90(0.8)^9\approx12.1$.)

## M2-Q20
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: What is the sum of all real solutions of the equation below?\dsp{$\sqrt{2x+3}+\sqrt{x-2}=\sqrt{5x+1}$}
- A: $-2$
- B: $1$
- C: $3$
- D: $4$
- Answer: C
- Solution: Squaring gives $3x+1+2\sqrt{(2x+3)(x-2)}=5x+1$, so $\sqrt{(2x+3)(x-2)}=x$ and $2x^2-x-6=x^2$, i.e. $x=3$ or $x=-2$. At $x=-2$ the radicands are negative, so only $x=3$ works ($\sqrt9+\sqrt1=4=\sqrt{16}$). (1 is the sum of both roots; $-2$ is the extraneous root; 4 is the common value of the two sides.)

## M2-Q21
- Domain: GT
- Difficulty: H
- Type: GRID
- Stem: In the figure, two circles with radii 4 and 9 are externally tangent to each other, and a line is tangent to the smaller circle at $P$ and to the larger circle at $Q$. What is the area of the shaded quadrilateral, whose vertices are $P$, $Q$, and the centers of the two circles?
- Figure:
```latex
\begin{tikzpicture}[scale=0.26]
\coordinate (P) at (0,0); \coordinate (Q) at (12,0);
\coordinate (A) at (0,4); \coordinate (B) at (12,9);
\fill[ink!20] (P)--(Q)--(B)--(A)--cycle;
\draw[line width=0.7pt] (A) circle (4); \draw[line width=0.7pt] (B) circle (9);
\draw[line width=0.7pt] (-6,0)--(22,0);
\draw[line width=0.7pt] (P)--(A)--(B)--(Q)--cycle;
\draw[line width=0.5pt] (0,1)--(1,1)--(1,0); \draw[line width=0.5pt] (12,1)--(11,1)--(11,0);
\fill[ink] (A) circle (0.4); \fill[ink] (B) circle (0.4);
\node[below left,font=\small] at (P) {$P$}; \node[below right,font=\small] at (Q) {$Q$};
\node[left,font=\small] at (0,2) {4}; \node[right,font=\small] at (12,4.5) {9};
\end{tikzpicture}
```
- Answer: 78
- Solution: The centers are 13 apart. The radii to $P$ and $Q$ are parallel (both perpendicular to the line), so the quadrilateral is a right trapezoid with parallel sides 4 and 9 and height $PQ$. Dropping a perpendicular: $PQ^2+(9-4)^2=13^2$, $PQ=12$. Area $=\frac12(4+9)(12)=78$.

## M2-Q22
- Domain: ADV
- Difficulty: H
- Type: MC
- Stem: For how many integer values of $k$ does the line $y=x+k$ intersect the circle $x^{2}+y^{2}=50$ at exactly two points?
- A: $9$
- B: $19$
- C: $21$
- D: $29$
- Answer: B
- Solution: Substituting gives $2x^2+2kx+k^2-50=0$ with discriminant $400-4k^2>0$, so $|k|<10$: the integers $-9$ through $9$, 19 values. (21 wrongly includes $k=\pm10$, where the line is tangent; 29 uses a wrong distance $|k|/2$; 9 counts only positive $k$.)
