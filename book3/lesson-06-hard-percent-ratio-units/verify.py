#!/usr/bin/env python3
"""Book 3, Lesson 6 "Hard percentages, ratios & units": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX),
  * a worked solution (this is what students see),
  * a `calc` function (or an `each` predicate for "which option ..." items) that recomputes the
    answer independently of the printed solution (exact rational arithmetic / brute force loops).

Running `python3 verify.py` recomputes every answer, checks that exactly one MC choice is correct
and that choices are distinct, balances the correct letters, and prints ALL OK / FAIL.
(`build.py` imports PROBLEMS from this file to write problems.md and the .tex files.)
"""
import sys
from fractions import Fraction
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, S, sympify, latex, floor, ceiling)

x, y, z, k, p, q, r, s, t, w, n, N = symbols('x y z k p q r s t w n N', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "Percent change: chains, reversals and wording traps", "Hard"),
    3: ("Set 3", "Interest, mixtures, weighted averages and tables", "Hard"),
    4: ("Set 4", "Ratios, rates, units and similar figures", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- helpers
def C(tex_or_val, val=None):
    """Numeric choice: C(66) or C(r"\\dfrac14", Rational(1,4)) or C("5.5", Rational(11,2)) -> (latex, value)."""
    if val is None:
        v = tex_or_val
        return ("$%s$" % latex(sympify(v)), sympify(v))
    return ("$%s$" % tex_or_val, val)

def T(text, val=None):
    """Text choice. Value defaults to the text itself; pass a value for ordering/keys."""
    return (text, text if val is None else val)

def same(u, v):
    try:
        if sympify(u) == sympify(v):
            return True
    except Exception:
        pass
    if isinstance(u, (tuple, str, list)) or isinstance(v, (tuple, str, list)) or callable(u) or callable(v):
        return u == v
    return simplify(sympify(u) - sympify(v)) == 0

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='auto', each=None, md=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, each=each, md=md))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol, md=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol, md=md))

def R(a, b=1):
    return Rational(a, b)

def rnd(v, d=0):
    """Round an exact value to d decimals (half up) and return an exact Rational."""
    sc = 10 ** d
    return Rational(int(floor(Rational(v) * sc + Rational(1, 2))), sc)

def pct(v):
    return Rational(v) * 100

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"A price is increased by $20\%$, and then the new price is decreased by $20\%$. The final price is what percent of the original price?",
   C(r"96\%", 96), [C(r"80\%", 80), C(r"100\%", 100), C(r"104\%", 104)],
   lambda: pct(R(6, 5) * R(4, 5)),
   "Multipliers, not addition",
   r"Multiply the factors: $1.20\times0.80=0.96$, so the final price is $96\%$ of the original. The $20\%$ drop is taken from the larger new price, so the changes do not cancel. ($100\%$ assumes they cancel; $104\%$ flips the sign of the net change; $80\%$ uses only the decrease.)")

mc(1, 'M',
   r"After a $15\%$ discount, a jacket sells for \$102. What was the price of the jacket before the discount?",
   C(r"\$120.00", 120), [C(r"\$86.70", R(867, 10)), C(r"\$117.00", 117), C(r"\$117.30", R(11730, 100))],
   lambda: Rational(102) / (1 - R(15, 100)),
   "Reverse percent: divide by the multiplier",
   r"The sale price is $85\%$ of the original: $0.85p=102$, so $p=120$. (\$117.30 multiplies by $1.15$; \$117 adds $15$; \$86.70 takes $85\%$ of \$102 instead of dividing.)")

gi(1, 'M',
   r"The unemployment rate in a town rose from $4\%$ to $5\%$. By what percent did the unemployment rate increase?",
   "25", Integer(25),
   lambda: pct(R(5 - 4, 4)),
   "Percent change vs percentage points",
   r"Percent change $=\dfrac{\text{change}}{\text{original}}=\dfrac{1}{4}=25\%$. The rate rose by $1$ \emph{percentage point}, but the rate itself grew by $25\%$.")

mc(1, 'M',
   r"A rug has an area of $3$ square feet. What is its area in square inches? ($1$ foot $=12$ inches)",
   C(432), [C(36), C(144), C("1{,}728", 1728)],
   lambda: 3 * (12 * 12),
   "Squared units: square the factor",
   r"$1\ \text{ft}^2=12\times12=144\ \text{in}^2$, so $3\times144=432$. (Choice $36$ multiplies by $12$ only; $144$ forgets the $3$; $1{,}728$ cubes the $12$.)")

mc(1, 'M',
   r"The ratio of cats to dogs at a shelter is $3:5$. After $6$ more cats arrive, the number of cats equals the number of dogs. How many animals were at the shelter at first?",
   C(24), [C(8), C(15), C(30)],
   lambda: next(8 * kk for kk in range(1, 100) if 3 * kk + 6 == 5 * kk),
   "Ratio changes: use $3k$ and $5k$",
   r"Let the animals be $3k$ cats and $5k$ dogs. $3k+6=5k$ gives $k=3$: $9$ cats, $15$ dogs, $24$ in all. ($8$ is one ``set'' $3+5$; $15$ is the dogs; $30$ counts the new cats too.)")

mc(1, 'M',
   r"Apples, pears and plums are mixed in the ratio $2:3:6$ by count. There are $36$ more plums than apples. How many pears are there?",
   C(27), [C(9), C(18), C(54)],
   lambda: next(3 * kk for kk in range(1, 200) if 6 * kk - 2 * kk == 36),
   "Part-to-part ratio: find one part",
   r"Plums minus apples is $6k-2k=4k=36$, so $k=9$ and pears are $3k=27$. ($9$ is one part; $18$ is the apples; $54$ is the plums.)")

mc(1, 'M',
   r"Of $800$ people surveyed, $60\%$ own a car. Of the car owners, $35\%$ drive an electric car. How many of the $800$ people are car owners who drive an electric car?",
   C(168), [C(280), C(480), C(760)],
   lambda: 800 * R(60, 100) * R(35, 100),
   "Percent of a percent: multiply the factors",
   r"The $35\%$ applies to car owners, not to everyone: $0.60(800)=480$ owners, then $0.35(480)=168$. ($280$ is $35\%$ of all $800$; $480$ is the number of owners; $760$ adds $60+35=95$ percent.)")

mc(1, 'H',
   r"A deposit of \$2,000 earns $5\%$ interest per year, compounded annually, with nothing else added or withdrawn. To the nearest dollar, what is the balance after $3$ years?",
   C(r"\$2{,}315", 2315), [C(r"\$2{,}100", 2100), C(r"\$2{,}300", 2300), C(r"\$6{,}300", 6300)],
   lambda: rnd(2000 * R(105, 100) ** 3),
   "Compound = multiply by $1+r$ each period",
   r"Each year multiplies by $1.05$: $2000(1.05)^3=2315.25\approx2315$. (\$2,300 is simple interest, $3\times\$100$ added; \$6,300 is $2000\times1.05\times3$; \$2,100 is one year only.)")

gi(1, 'M',
   r"A car travels at $72$ kilometers per hour. How many meters does the car travel each second?",
   "20", Integer(20),
   lambda: R(72 * 1000, 3600),
   "Unit conversion chain",
   r"$72\ \dfrac{\text{km}}{\text{h}}\cdot\dfrac{1000\ \text{m}}{1\ \text{km}}\cdot\dfrac{1\ \text{h}}{3600\ \text{s}}=\dfrac{72{,}000}{3600}=20$ meters per second. (Shortcut: divide km/h by $3.6$.)")

mc(1, 'H',
   r"A cyclist rides $12$ km uphill at $12$ km/h and then rides back down the same $12$ km at $24$ km/h. What is the cyclist's average speed, in km/h, for the whole trip?",
   C(16), [C(8), C(18), C(24)],
   lambda: R(24) / (R(12, 12) + R(12, 24)),
   "Average speed = total distance $\\div$ total time",
   r"Total distance $=24$ km. Total time $=\frac{12}{12}+\frac{12}{24}=1.5$ h. Average speed $=24\div1.5=16$ km/h. ($18$ averages the two speeds, but more time is spent at the slower one; $8$ is product over sum, half the answer; $24$ is the return speed alone.)")

mc(1, 'M',
   r"Every length of a figure is multiplied by $4$ to make a similar, larger figure. The original figure has an area of $12$ square centimeters. What is the area of the larger figure, in square centimeters?",
   C(192), [C(16), C(48), C(768)],
   lambda: 12 * 4 ** 2,
   "Scale factor $k$: area scales by $k^2$",
   r"Lengths scale by $k=4$, so area scales by $k^2=16$: $12\times16=192$. ($48$ scales area by $4$; $768$ uses $k^3$, the rule for volume; $16$ forgets the $12$.)")

gi(1, 'H',
   r"Store A's price for a camera is $150\%$ more than Store B's price. Store A's price is how many times Store B's price?",
   "2.5", R(5, 2),
   lambda: 1 + R(150, 100),
   "``$n\\%$ more'' vs ``$n$ times as much''",
   r"$150\%$ \emph{more} means $B+1.5B=2.5B$. So A's price is $2.5$ times B's. (``$150\%$ of'' would be $1.5$ times; ``$150\%$ more than'' is $1+1.5$.)")

# ============================================================ SET 2  (percent change, 14)
mc(2, 'H',
   r"A customer buys a tablet after a $20\%$ store discount, and then uses a coupon that takes an additional $15\%$ off the already discounted price. She pays \$204. What was the original price of the tablet?",
   C(r"\$300.00", 300), [C(r"\$240.00", 240), C(r"\$275.40", R(27540, 100)), C(r"\$313.85", R(31385, 100))],
   lambda: Rational(204) / ((1 - R(20, 100)) * (1 - R(15, 100))),
   "Chain of multipliers, then divide",
   r"The discounts multiply: $0.80\times0.85=0.68$, so $0.68p=204$ and $p=300$. (Adding the discounts to $35\%$ gives $204\div0.65\approx\$313.85$; \$240 undoes only the coupon; \$275.40 multiplies by $1.35$.)")

mc(2, 'H',
   r"In a poll, the share of voters who support a measure rose from $40\%$ to $46\%$. Which statement is true?",
   T(r"The share rose by $6$ percentage points, which is a $15\%$ increase.", (6, 15)),
   [T(r"The share rose by $6\%$.", (None, 6)),
    T(r"The share rose by $15$ percentage points.", (15, None)),
    T(r"The share rose by $6$ percentage points, which is a $13\%$ increase.", (6, 13))],
   None,
   "Percentage points vs percent change",
   r"Percentage points are the difference of the two rates: $46-40=6$. Percent change compares with the starting rate: $\frac{6}{40}=15\%$. ($13\%$ divides by the new rate, $46$; ``$6\%$'' mixes the two ideas; ``$15$ points'' confuses them.)",
   order='free',
   each=lambda v: v == (46 - 40, pct(R(46 - 40, 40))))

gi(2, 'H',
   r"A price is increased by $x\%$, and then the new price is decreased by $x\%$. The final price is $91\%$ of the original price. What is the value of $x$?",
   "30", Integer(30),
   lambda: [v for v in range(1, 100) if (1 + R(v, 100)) * (1 - R(v, 100)) == R(91, 100)][0],
   "Up $x\\%$ then down $x\\%$ loses $x^2/100$ percent",
   r"$\left(1+\frac{x}{100}\right)\left(1-\frac{x}{100}\right)=1-\frac{x^2}{10{,}000}=0.91$, so $\frac{x^2}{10{,}000}=0.09$ and $x=30$. (Check: $1.3\times0.7=0.91$.)")

mc(2, 'H',
   r"Machine A produces $75\%$ more widgets per hour than machine B. Machine A produces $210$ widgets per hour. How many widgets per hour does machine B produce?",
   C(120), [C(135), C("157.5", R(315, 2)), C(280)],
   lambda: Rational(210) / (1 + R(75, 100)),
   "``$n\\%$ more than $B$'' means $B(1+n\\%)$",
   r"A is $B$ plus $75\%$ of $B$: $1.75B=210$, so $B=120$. ($135$ subtracts $75$; $157.5$ takes $75\%$ of $210$; $280$ divides by $0.75$.)")

mc(2, 'H',
   r"In a survey of $500$ customers, $30\%$ are under $25$ years old. Of the customers under $25$, $40\%$ prefer streaming; of the customers who are $25$ or older, $20\%$ prefer streaming. How many of the $500$ customers prefer streaming?",
   C(130), [C(60), C(150), C(200)],
   lambda: 500 * R(30, 100) * R(40, 100) + 500 * (1 - R(30, 100)) * R(20, 100),
   "Percent of a percent for each group, then add",
   r"Under $25$: $0.30(500)=150$ people and $0.40(150)=60$. Age $25$ or older: $350$ people and $0.20(350)=70$. Total $60+70=130$. ($60$ forgets the older group; $150$ averages $40\%$ and $20\%$ to $30\%$ of $500$; $200$ applies $40\%$ to everyone.)")

mc(2, 'H',
   r"A diner's bill before tax is $x$ dollars. A $10\%$ tax is added to the bill, and then the diner leaves a $20\%$ tip on the amount that includes tax. The diner pays \$198 in all. What is $x$?",
   C(r"\$150.00", 150), [C(r"\$152.31", R(15231, 100)), C(r"\$165.00", 165), C(r"\$180.00", 180)],
   lambda: Rational(198) / (R(11, 10) * R(12, 10)),
   "Stacked percents multiply",
   r"Tax then tip on the taxed amount: $1.10\times1.20=1.32$, so $1.32x=198$ and $x=150$. (\$152.31 adds the rates, $198\div1.30$; \$165 ignores the tax; \$180 ignores the tip.)")

mc(2, 'H',
   r"An investment grew by $25\%$ during its first year. In the second year it fell by $p\%$, and after the two years it was $12.5\%$ above its starting value. What is $p$?",
   C(10), [C("12.5", R(25, 2)), C(20), C(25)],
   lambda: pct(1 - (1 + R(125, 1000)) / (1 + R(25, 100))),
   "Unknown factor in a chain",
   r"$1.25(1-\frac{p}{100})=1.125$, so $1-\frac{p}{100}=0.9$ and $p=10$. ($12.5$ subtracts $25-12.5$; $20$ is the drop that would return it exactly to the start; $25$ assumes the second change mirrors the first.)")

gi(2, 'H',
   r"A price rises by $60\%$. By what percent must the new price fall to return to the original price?",
   "37.5", R(75, 2),
   lambda: pct(1 - 1 / (1 + R(60, 100))),
   "Undo a percent with the reciprocal factor",
   r"The new price is $1.6p$. To get back to $p$ the multiplier is $\frac1{1.6}=0.625$, a drop of $1-0.625=0.375=37.5\%$. (Not $60\%$: the drop is taken from the larger new price, so a smaller percent is enough.)")

mc(2, 'H',
   r"The positive number $x$ is $30\%$ less than $y$, and $y$ is $20\%$ greater than $z$. The number $x$ is what percent of $z$?",
   C(r"84\%", 84), [C(r"70\%", 70), C(r"90\%", 90), C(r"120\%", 120)],
   lambda: pct(R(7, 10) * R(12, 10)),
   "Percent of a percent",
   r"$x=0.70y$ and $y=1.20z$, so $x=0.70\times1.20z=0.84z$, which is $84\%$ of $z$. ($90\%$ adds $-30+20$; $70\%$ and $120\%$ use only one of the two steps.)")

mc(2, 'H',
   r"A company's revenue in 2021 was $40\%$ greater than its revenue in 2020. Revenue in 2022 was $1.5$ times the revenue in 2021. Revenue in 2022 was what percent greater than revenue in 2020?",
   C(r"110\%", 110), [C(r"90\%", 90), C(r"150\%", 150), C(r"210\%", 210)],
   lambda: pct(R(14, 10) * R(15, 10) - 1),
   "``$n$ times as much'' vs ``$n\\%$ greater''",
   r"Multiply: $1.4\times1.5=2.1$, so 2022 revenue is $2.1$ times 2020 revenue, which is $110\%$ \emph{greater}. ($210\%$ is ``$\%$ of'', not ``$\%$ greater''; $90\%$ adds $40+50$; $150\%$ uses only the last step.)")

gi(2, 'H',
   r"A store buys a jacket for \$80 and marks the price up by $60\%$. Later the store sells the jacket for $25\%$ off the marked price. The store's profit is what percent of its cost?",
   "20", Integer(20),
   lambda: pct((80 * R(16, 10) * R(75, 100) - 80) / 80),
   "Markup then discount: chain the multipliers",
   r"Marked price: $80(1.6)=128$. Sale price: $0.75(128)=96$. Profit $=96-80=16$, and $\frac{16}{80}=20\%$. (Not $35\%$: the discount is taken from the marked price.)")

mc(2, 'H',
   r"A student measures a rod and gets $144$ cm, which is $4\%$ below the rod's true length. What is the true length of the rod, in centimeters?",
   C(150), [C("138.24", R(13824, 100)), C(148), C("149.76", R(14976, 100))],
   lambda: Rational(144) / R(96, 100),
   "Percent error: the base is the true value",
   r"The measured value is $96\%$ of the true value $L$: $0.96L=144$, so $L=150$. (Percent error is measured against the true length. $144\times0.96=138.24$ goes the wrong way; $144\times1.04=149.76$ takes $4\%$ of the measurement; $148$ adds $4$.)")

mc(2, 'H',
   r"A store raises the price of an item by $25\%$. After the increase, the number of units sold falls by $20\%$. By what percent does the store's revenue from this item change?",
   T(r"It does not change.", 0),
   [T(r"It decreases by $5\%$.", -5), T(r"It increases by $5\%$.", 5), T(r"It increases by $45\%$.", 45)],
   lambda: pct(R(125, 100) * R(80, 100) - 1),
   "Revenue = price $\\times$ quantity: multiply the factors",
   r"Revenue is price $\times$ units, so the factors multiply: $1.25\times0.80=1.00$. Revenue does not change. (An increase of $5\%$ subtracts $25-20$; a decrease of $5\%$ flips that; an increase of $45\%$ adds $25+20$.)")

gi(2, 'H',
   r"A jar contains only red and blue marbles, and $40\%$ of the marbles are red. After $20$ blue marbles are removed, $50\%$ of the marbles in the jar are red. How many marbles were in the jar originally?",
   "100", Integer(100),
   lambda: next(m for m in range(1, 1000) if R(40 * m, 100) == R(1, 2) * (m - 20)),
   "Fixed part: the red count never changes",
   r"The red count stays the same. Let $N$ be the original total: $0.40N=0.50(N-20)$, so $0.10N=10$ and $N=100$. (Check: $40$ red, $60$ blue; remove $20$ blue and $40$ of $80$ are red.)")

# ============================================================ SET 3  (interest, mixtures, averages, tables; 14)
def _bal_monthly(P, tt):
    return P * (1 + R(12, 100) / 12) ** (12 * tt)

def _agree(f, g):
    return all(abs(float(f(1000, tt)) - float(g(1000, tt))) < 1e-6 for tt in (1, 2, 3, 5))

mc(3, 'H',
   r"An account pays interest at an annual rate of $12\%$, compounded monthly (that is, $1\%$ each month). If $P$ is the initial deposit, which function gives the balance after $t$ years?",
   T(r"$P(1.01)^{12t}$", lambda P, tt: P * Rational(101, 100) ** (12 * tt)),
   [T(r"$P(1.12)^{t}$", lambda P, tt: P * Rational(112, 100) ** tt),
    T(r"$P(1.12)^{12t}$", lambda P, tt: P * Rational(112, 100) ** (12 * tt)),
    T(r"$P(1.01)^{t}$", lambda P, tt: P * Rational(101, 100) ** tt)],
   None,
   "Per-period rate and number of periods",
   r"Each month multiplies the balance by $1+\frac{0.12}{12}=1.01$, and $t$ years contain $12t$ months, so $B=P(1.01)^{12t}$. (The other choices use the yearly rate $1.12$ once a year, the yearly rate every month, or only $t$ monthly periods.)",
   order='free',
   each=lambda f: _agree(f, _bal_monthly))

gi(3, 'H',
   r"Two accounts each start with \$10,000. Account A earns $5\%$ simple interest per year. Account B earns $5\%$ interest per year, compounded annually. After $3$ years, how many more dollars does Account B hold than Account A?",
   "76.25", R(7625, 100),
   lambda: 10000 * (R(21, 20) ** 3 - (1 + 3 * R(5, 100))),
   "Simple = add $rP$; compound = multiply by $1+r$",
   r"A: $10{,}000(1+3\cdot0.05)=11{,}500$. B: $10{,}000(1.05)^3=11{,}576.25$. Difference $=76.25$.")

mc(3, 'H',
   r"The balance of a loan grows by $1.5\%$ each month with no payments. Which is closest to the percent by which the balance grows in one year?",
   C(r"19.6\%", R(196, 10)), [C(r"18.0\%", R(180, 10)), C(r"119.6\%", R(1196, 10)), C(r"180\%", 180)],
   lambda: rnd(pct(R(1015, 1000) ** 12 - 1), 1),
   "Monthly growth compounds: $(1+r)^{12}-1$",
   r"One year is $12$ months: $(1.015)^{12}\approx1.196$, a growth of $19.6\%$. ($18.0\%$ is simple, $12\times1.5$; $119.6\%$ is the new amount as a percent of the old, not the growth; $180\%$ multiplies $1.5\times12$ and slips a decimal.)")

mc(3, 'H',
   r"How many liters of a $10\%$ acid solution must be added to $6$ liters of a $40\%$ acid solution to make a $30\%$ acid solution?",
   C(3), [C(6), C(9), C(12)],
   lambda: solve(R(1, 10) * w + R(4, 10) * 6 - R(3, 10) * (w + 6), w)[0],
   "Mixture: acid in = acid out",
   r"Acid: $0.10x+0.40(6)=0.30(x+6)$, so $2.4+0.1x=1.8+0.3x$ and $x=3$. (Check: $0.3+2.4=2.7$ in $9$ liters is $30\%$. $6$ assumes equal amounts; $9$ is the final volume; $12$ flips the ratio.)")

gi(3, 'H',
   r"A $12$-liter solution is $35\%$ salt by volume. How many liters of water must evaporate so that the remaining solution is $60\%$ salt by volume?",
   "5", Integer(5),
   lambda: next(e for e in range(0, 12) if R(35 * 12, 100) == R(60, 100) * (12 - e)),
   "Evaporation: the salt amount stays fixed",
   r"Salt: $0.35(12)=4.2$ liters never changes. The new volume is $4.2\div0.60=7$ liters, so $12-7=5$ liters evaporate. (Only water leaves; the salt amount is the invariant.)")

mc(3, 'H',
   r"A teacher records the mean score for three sections of a course. $$\begin{tabular}{|c|c|c|}\hline Section & Students & Mean score\\\hline I & 20 & 80\\ II & 30 & 70\\ III & 50 & 90\\\hline\end{tabular}$$ What is the mean score of all $100$ students?",
   C(82), [C(79), C(80), C(90)],
   lambda: R(20 * 80 + 30 * 70 + 50 * 90, 100),
   "Weighted average: use totals",
   r"Total points: $20(80)+30(70)+50(90)=1600+2100+4500=8200$, and $8200\div100=82$. ($80$ is the unweighted mean of the three means; $79$ pairs the means with the sizes in reverse order; $90$ is the largest section's mean.)",
   md="A teacher records the mean score for three sections of a course.\n\n   | Section | Students | Mean score |\n   |---|---|---|\n   | I | 20 | 80 |\n   | II | 30 | 70 |\n   | III | 50 | 90 |\n\n   What is the mean score of all $100$ students?")

gi(3, 'H',
   r"A class has $30$ students with a mean test score of $72$. The $18$ girls in the class have a mean score of $78$. What is the mean score of the boys?",
   "63", Integer(63),
   lambda: (30 * 72 - 18 * 78) / Integer(30 - 18),
   "Weighted average: subtract the known group's total",
   r"Total points: $30(72)=2160$. Girls: $18(78)=1404$. Boys: $2160-1404=756$ points among $12$ boys, so the mean is $756\div12=63$.")

mc(3, 'H',
   r"Employees at a company are classified by shift and by employment status. $$\begin{tabular}{|c|c|c|}\hline & Day shift & Night shift\\\hline Full-time & 180 & 120\\ Part-time & 90 & 110\\\hline\end{tabular}$$ Which is closest to the percent of night-shift employees who are full-time?",
   C(r"52\%", 52), [C(r"24\%", 24), C(r"40\%", 40), C(r"67\%", 67)],
   lambda: rnd(pct(R(120, 120 + 110)), 0),
   "Percent of a column: pick the right denominator",
   r"The group asked about is the night shift: $120+110=230$ employees. Full-time among them: $\frac{120}{230}\approx52\%$. ($24\%$ divides by all $500$; $40\%$ divides by the $300$ full-time employees; $67\%$ is $\frac{120}{180}$, night over day.)",
   md="Employees at a company are classified by shift and by employment status.\n\n   | | Day shift | Night shift |\n   |---|---|---|\n   | Full-time | 180 | 120 |\n   | Part-time | 90 | 110 |\n\n   Which is closest to the percent of night-shift employees who are full-time?")

gi(3, 'H',
   r"Solution X is $20\%$ alcohol and solution Y is $50\%$ alcohol, both by volume. A mixture of only X and Y is $38\%$ alcohol by volume. What fraction of the mixture's volume is solution Y? (Enter a fraction or a decimal.)",
   "0.6", R(3, 5),
   lambda: solve(R(2, 10) * (1 - t) + R(5, 10) * t - R(38, 100), t)[0],
   "Weighted average gives the fraction directly",
   r"Let $f$ be the fraction that is Y. Then $0.20(1-f)+0.50f=0.38$, so $0.20+0.30f=0.38$ and $f=0.6$. (Shortcut: $38$ sits $18$ of the $30$ points from $20$ to $50$, and $\frac{18}{30}=0.6$.)")

_TBL10 = {'A': (75, 60), 'B': (250, 200), 'C': (195, 150), 'D': (27, 20)}
mc(3, 'M',
   r"Annual sales of four product lines, in thousands of dollars: $$\begin{tabular}{|c|c|c|}\hline Line & 2020 & 2023\\\hline A & 60 & 75\\ B & 200 & 250\\ C & 150 & 195\\ D & 20 & 27\\\hline\end{tabular}$$ Which line had the greatest percent increase in sales from 2020 to 2023?",
   T("Line D", 'D'), [T("Line A", 'A'), T("Line B", 'B'), T("Line C", 'C')],
   None,
   "Percent change needs the starting value",
   r"Percent increases: A $\frac{15}{60}=25\%$, B $\frac{50}{200}=25\%$, C $\frac{45}{150}=30\%$, D $\frac{7}{20}=35\%$. D is greatest. (B has the greatest \emph{dollar} increase, $50$, but only $25\%$; A ties it at $25\%$; C is the runner-up at $30\%$.)",
   order='free',
   each=lambda v: v == max(_TBL10, key=lambda kk: R(_TBL10[kk][0] - _TBL10[kk][1], _TBL10[kk][1])),
   md="Annual sales of four product lines, in thousands of dollars:\n\n   | Line | 2020 | 2023 |\n   |---|---|---|\n   | A | 60 | 75 |\n   | B | 200 | 250 |\n   | C | 150 | 195 |\n   | D | 20 | 27 |\n\n   Which line had the greatest percent increase in sales from 2020 to 2023?")

mc(3, 'H',
   r"What initial deposit, to the nearest dollar, grows to exactly \$3,000 in $2$ years at $10\%$ interest per year, compounded annually?",
   C(r"\$2{,}479", 2479), [C(r"\$2{,}500", 2500), C(r"\$2{,}727", 2727), C(r"\$3{,}630", 3630)],
   lambda: rnd(Rational(3000) / R(11, 10) ** 2),
   "Reverse compound growth: divide by $(1+r)^t$",
   r"$P(1.10)^2=3000$, so $P=\frac{3000}{1.21}\approx2479$. (\$2,500 divides by $1.2$, simple interest; \$2,727 divides by $1.1$ once; \$3,630 multiplies instead of dividing.)")

mc(3, 'H',
   r"A car bought for \$24,000 loses $15\%$ of its value each year. After how many whole years is the car's value first below \$12,000?",
   C(5), [C(3), C(4), C(6)],
   lambda: next(yr for yr in range(1, 50) if 24000 * R(85, 100) ** yr < 12000),
   "Exponential decay is not linear",
   r"Value $=24000(0.85)^t<12000$ means $0.85^t<0.5$. $0.85^4\approx0.522$ is not enough and $0.85^5\approx0.444$ is, so $t=5$. ($3$ is the linear guess $50\div15\approx3.3$ rounded down; $4$ rounds $4.27$ down; $6$ overshoots.)")

mc(3, 'H',
   r"An account pays $4\%$ simple interest per year on the original deposit. After $5$ years the balance is \$6,300. What was the original deposit?",
   C(r"\$5{,}250", 5250), [C(r"\$5{,}040", 5040), C(r"\$5{,}178", 5178), C(r"\$6{,}058", 6058)],
   lambda: Rational(6300) / (1 + 5 * R(4, 100)),
   "Simple interest: $A=P(1+rt)$",
   r"Simple interest adds $4\%$ of $P$ each year, so $A=P(1+0.04\cdot5)=1.2P$ and $P=\frac{6300}{1.2}=5250$. (\$5,040 takes $80\%$ of the balance; \$5,178 divides by $1.04^5$, compound; \$6,058 divides by $1.04$ once.)")

mc(3, 'H',
   r"A $20$-liter tank holds a $15\%$ antifreeze solution. A technician drains $x$ liters of the mixture and replaces it with pure antifreeze, making the $20$ liters a $32\%$ antifreeze solution. What is $x$?",
   C(4), [C("3.4", R(34, 10)), C(5), C("6.4", R(64, 10))],
   lambda: solve(R(15, 100) * (20 - x) + x - R(32, 100) * 20, x)[0],
   "Replace-and-refill: remove antifreeze too",
   r"Antifreeze left: $0.15(20-x)$; add $x$ pure: $0.15(20-x)+x=0.32(20)=6.4$, so $3+0.85x=6.4$ and $x=4$. ($3.4$ forgets that the drained liquid carried antifreeze; $5$ adds $x$ liters instead of replacing; $6.4$ is the antifreeze amount, not the volume.)")

# ============================================================ SET 4  (ratios, rates, units, similar figures; 14)
mc(4, 'H',
   r"The ratio of blue marbles to red marbles in a bag is $3:7$. After $8$ red marbles are removed, the ratio of blue to red is $3:5$. How many blue marbles are in the bag?",
   C(12), [C(4), C(20), C(28)],
   lambda: next(3 * kk for kk in range(1, 200) if R(3 * kk, 7 * kk - 8) == R(3, 5)),
   "Ratio after a change: $3k$ and $7k$",
   r"Blue $=3k$, red $=7k$. After the change $\frac{3k}{7k-8}=\frac35$, so $15k=21k-24$ and $k=4$. Blue $=3k=12$. (Check: $12:20=3:5$. $4$ is $k$; $20$ is the red marbles after removal; $28$ is the red marbles before.)")

gi(4, 'H',
   r"In a club, the ratio of juniors to non-juniors is $3$ to $5$. Among the non-juniors, the ratio of seniors to sophomores is $2$ to $3$. The club has $96$ members. How many sophomores are in the club?",
   "36", Integer(36),
   lambda: 96 * R(5, 3 + 5) * R(3, 2 + 3),
   "Part-to-part ratios: convert to part-to-whole",
   r"Non-juniors are $\frac58$ of the club: $\frac58(96)=60$. Sophomores are $\frac35$ of the non-juniors: $\frac35(60)=36$. (The second ratio, $2:3$, splits the $60$ non-juniors, not the whole club of $96$.)")

mc(4, 'H',
   r"A tank has a volume of $2.5$ cubic meters. How many liters does it hold? ($1$ liter $=1000$ cubic centimeters and $1$ meter $=100$ centimeters)",
   C("2{,}500", 2500), [C("2.5", R(5, 2)), C(250), C("2{,}500{,}000", 2500000)],
   lambda: R(5, 2) * 100 ** 3 / 1000,
   "Cubed units: cube the factor",
   r"$1\ \text{m}^3=100^3=1{,}000{,}000\ \text{cm}^3$, so the tank holds $2.5\times10^6\ \text{cm}^3$, and dividing by $1000$ gives $2{,}500$ liters. ($250$ uses $100$ for the cubic factor; $2{,}500{,}000$ is the volume in $\text{cm}^3$, not liters; $2.5$ does no conversion.)")

mc(4, 'H',
   r"Floor tile costs \$4.50 per square foot. A rectangular floor measures $3$ yards by $4$ yards. What is the cost of tiling the floor? ($1$ yard $=3$ feet)",
   C(r"\$486.00", 486), [C(r"\$54.00", 54), C(r"\$162.00", 162), C(r"\$1{,}458.00", 1458)],
   lambda: (3 * 3) * (4 * 3) * R(9, 2),
   "Squared units: convert each side first",
   r"The floor is $9\ \text{ft}\times12\ \text{ft}=108\ \text{ft}^2$, and $108\times4.50=486$. (\$54 uses $12$ square \emph{yards}; \$162 multiplies the area by $3$ instead of $9$; \$1,458 multiplies by $27$.)")

gi(4, 'H',
   r"Pump A can fill an empty tank in $6$ hours working alone, and pump B can fill it in $12$ hours working alone. Drain C can empty a full tank in $9$ hours. If both pumps and the drain all run together, how many hours does it take to fill the empty tank?",
   "7.2", R(36, 5),
   lambda: 1 / (R(1, 6) + R(1, 12) - R(1, 9)),
   "Rates add: tank per hour",
   r"Rates (tank per hour): $\frac16+\frac1{12}-\frac19=\frac{6+3-4}{36}=\frac5{36}$. Time $=\frac{36}{5}=7.2$ hours. (Add \emph{rates}, never times.)")

mc(4, 'H',
   r"A runner runs for $2$ hours at $10$ km/h and then for $3$ hours at $15$ km/h. What is the runner's average speed, in km/h, for the whole run?",
   C(13), [C(12), C("12.5", R(25, 2)), C(65)],
   lambda: R(2 * 10 + 3 * 15, 2 + 3),
   "Equal times: average speed is a weighted average",
   r"Distance $=2(10)+3(15)=65$ km in $5$ hours, so the average speed is $13$ km/h. ($12.5$ averages the speeds without weighting; $12$ is $\frac{2\cdot10\cdot15}{10+15}$, the formula for \emph{equal distances}; $65$ is the distance, not the speed.)")

mc(4, 'H',
   r"On a map, $2.5$ centimeters represent $8$ kilometers. A lake is shown on the map with an area of $30$ square centimeters. What is the actual area of the lake, in square kilometers?",
   C("307.2", R(3072, 10)), [C(96), C(240), C("983.04", R(98304, 100))],
   lambda: 30 * (R(8) / R(5, 2)) ** 2,
   "Scale drawing: area scales by $k^2$",
   r"$1$ cm on the map is $\frac{8}{2.5}=3.2$ km, so $1\ \text{cm}^2$ is $3.2^2=10.24\ \text{km}^2$. Then $30\times10.24=307.2$. ($96$ multiplies by $3.2$ only; $240$ treats $1\ \text{cm}^2$ as $8\ \text{km}^2$; $983.04$ uses $3.2^3$.)")

gi(4, 'H',
   r"Two similar solids have surface areas of $50$ square centimeters and $450$ square centimeters. The smaller solid has a volume of $40$ cubic centimeters. What is the volume, in cubic centimeters, of the larger solid?",
   "1080", Integer(1080),
   lambda: 40 * sqrt(R(450, 50)) ** 3,
   "Similar solids: area $k^2$, volume $k^3$",
   r"The area ratio is $\frac{450}{50}=9=k^2$, so the scale factor is $k=3$. Volume scales by $k^3=27$: $40\times27=1080$.")

mc(4, 'H',
   r"Two triangles are similar. Their areas are $20$ square centimeters and $45$ square centimeters. The perimeter of the smaller triangle is $24$ centimeters. What is the perimeter of the larger triangle, in centimeters?",
   C(36), [C(49), C(54), C(81)],
   lambda: 24 * sqrt(R(45, 20)),
   "Perimeter scales by $k$, area by $k^2$",
   r"$k^2=\frac{45}{20}=\frac94$, so $k=\frac32$. Perimeter scales by $k$: $24\times\frac32=36$. ($54$ multiplies by the area ratio $\frac94$; $49$ adds the area difference; $81$ multiplies by $k^3$.)")

gi(4, 'H',
   r"A metal cube with edges of $4$ centimeters has a mass of $512$ grams. A second cube is made of the same metal and has edges of $6$ centimeters. What is the mass of the second cube, in kilograms?",
   "1.728", R(1728, 1000),
   lambda: (R(512, 4 ** 3) * 6 ** 3) / 1000,
   "Density is constant; volume scales by $k^3$",
   r"Density $=\frac{512}{64}=8$ g/cm$^3$. The second cube has volume $6^3=216$ cm$^3$, so its mass is $8\times216=1728$ g $=1.728$ kg. (Shortcut: $k=1.5$, $k^3=3.375$, and $512\times3.375=1728$.)")

mc(4, 'H',
   r"A rock sample has a density of $2.7$ grams per cubic centimeter. What is the mass, in kilograms, of $2$ cubic meters of this rock?",
   C("5{,}400", 5400), [C("5.4", R(27, 5)), C(540), C("5{,}400{,}000", 5400000)],
   lambda: R(27, 10) * 2 * 100 ** 3 / 1000,
   "Density with cubed units",
   r"$2\ \text{m}^3=2\times10^6\ \text{cm}^3$, so the mass is $2.7\times2\times10^6=5.4\times10^6$ g $=5{,}400$ kg. ($5{,}400{,}000$ is the mass in grams; $540$ uses $100^2$-type scaling; $5.4$ multiplies $2\times2.7$ with no conversion.)")

mc(4, 'H',
   r"A faucet adds water to an empty tank at $12$ liters per minute. A leak removes water at $0.15$ liter per second. How many minutes does it take to fill a $450$-liter tank?",
   C(150), [C("21.4", R(214, 10)), C("37.5", R(75, 2)), C("38.0", R(38))],
   lambda: rnd(Rational(450) / (12 - R(15, 100) * 60)),
   "Rates in the same units, then subtract",
   r"The leak is $0.15\times60=9$ liters per minute. Net rate $=12-9=3$ L/min, so $450\div3=150$ minutes. ($38.0$ subtracts $0.15$ from $12$ without converting seconds to minutes; $37.5$ ignores the leak; $21.4$ adds the leak.)")

mc(4, 'H',
   r"A scale model of a ship is built with a length scale of $1:40$ (every length on the model is $\frac1{40}$ of the real length). The real ship's deck has an area of $2{,}560$ square meters. What is the area of the deck on the model, in square meters?",
   C("1.6", R(8, 5)), [C("6.4", R(32, 5)), C(64), C("102{,}400", 102400)],
   lambda: R(2560) / 40 ** 2,
   "Scale model: area scales by $k^2$",
   r"Lengths shrink by $40$, so areas shrink by $40^2=1600$: $2560\div1600=1.6$. ($64$ divides by $40$ only; $6.4$ divides by $400$; $102{,}400$ multiplies by $1600$ instead of dividing.)")

mc(4, 'H',
   r"Four workers paint $3$ identical houses in $9$ days, all working at the same steady pace. At this pace, how many days will $8$ workers take to paint $10$ identical houses?",
   C(15), [C("4.5", R(9, 2)), C(30), C(60)],
   lambda: R(10) * (R(4 * 9, 3)) / 8,
   "Worker-days per job",
   r"One house takes $\frac{4\times9}{3}=12$ worker-days. Ten houses take $120$ worker-days, and $8$ workers need $\frac{120}{8}=15$ days. ($4.5$ halves the time for double the workers but ignores the extra houses; $30$ scales for the houses but ignores the workers; $60$ makes more workers take longer.)")

# ============================================================ SET 5  (Summit, 20)
mc(5, 'H',
   r"At a school, the ratio of boys to girls is $4:5$. Next year the number of boys will increase by $25\%$ and the number of girls will decrease by $20\%$. What will the ratio of boys to girls be next year?",
   C(r"5:4", R(5, 4)), [C(r"4:5", R(4, 5)), C(r"1:1", 1), C(r"25:16", R(25, 16))],
   lambda: R(4 * 125, 5 * 80),
   "Ratio after percent changes: multiply each part",
   r"Take $4k$ boys and $5k$ girls. Next year: $1.25(4k)=5k$ boys and $0.80(5k)=4k$ girls, so the ratio is $5:4$. ($4:5$ is the old ratio; $1:1$ treats $+25\%$ and $-20\%$ as cancelling; $25:16$ is $1.25:0.80$ alone, forgetting the old ratio.)")

mc(5, 'H',
   r"Town A has $20\%$ more residents than Town B. Then the population of A falls by $10\%$ while the population of B grows by $5\%$. After these changes, the population of A is closest to what percent of the population of B?",
   C(r"103\%", 103), [C(r"108\%", 108), C(r"115\%", 115), C(r"126\%", 126)],
   lambda: rnd(pct(R(12, 10) * R(9, 10) / R(105, 100))),
   "Compare two chains: divide the factors",
   r"Take $B=100$, so $A=120$. After the changes: $A=0.90(120)=108$ and $B=1.05(100)=105$. Then $\frac{108}{105}\approx1.03$, or $103\%$. ($108\%$ ignores B's growth; $115\%$ adds $20-10+5$; $126\%$ multiplies by $1.05$ instead of dividing.)")

mc(5, 'H',
   r"During a sale, a store takes $25\%$ off every marked price. At the sale price the store still earns a $20\%$ profit on its cost. The marked price was what percent above the store's cost?",
   C(r"60\%", 60), [C(r"45\%", 45), C(r"50\%", 50), C(r"80\%", 80)],
   lambda: pct(R(12, 10) / R(75, 100) - 1),
   "Work backwards through the chain",
   r"Let the cost be $100$. The sale price is $120$, which is $75\%$ of the marked price $M$: $M=\frac{120}{0.75}=160$. The marked price is $60\%$ above cost. ($45\%$ adds $20+25$; $50\%$ adds $25\%$ to the sale price instead of dividing by $0.75$; $80\%$ divides $20$ by $0.25$.)")

gi(5, 'H',
   r"A chemist mixes solution P ($10\%$ salt) with solution Q ($40\%$ salt) to make $30$ liters of a $22\%$ salt solution. She then adds $w$ liters of pure water, and the diluted solution is $15\%$ salt. What is $w$?",
   "14", Integer(14),
   lambda: (lambda qq: (R(1, 10) * (30 - qq) + R(4, 10) * qq) / R(15, 100) - 30)(solve(R(1, 10) * (30 - q) + R(4, 10) * q - R(22, 100) * 30, q)[0]),
   "Dilution: the salt amount is fixed",
   r"The mixture has $0.22(30)=6.6$ liters of salt, and you never need P or Q separately. Water adds no salt: $\frac{6.6}{30+w}=0.15$, so $30+w=44$ and $w=14$.")

gi(5, 'H',
   r"Account A pays $6\%$ simple interest per year on its initial deposit. Account B pays $5\%$ interest per year, compounded annually. Both start with the same deposit. After how many whole years does Account B first hold more than Account A?",
   "9", Integer(9),
   lambda: next(yr for yr in range(1, 100) if R(105, 100) ** yr > 1 + R(6, 100) * yr),
   "Linear vs exponential: compare factors year by year",
   r"Compare the multipliers: A is $1+0.06t$, B is $1.05^t$. At $t=8$: B $\approx1.4775$ and A $=1.48$, so A is still ahead. At $t=9$: B $\approx1.5513$, A $=1.54$. B first leads after $9$ years. (Or graph both in Desmos.)")

mc(5, 'H',
   r"Machine A alone can finish a job in $8$ hours, and machine B alone can finish it in $24$ hours. They work together for $3$ hours; then A stops and B finishes the rest alone. How many hours does the whole job take, counting from the start?",
   C(15), [C(6), C(12), C(27)],
   lambda: 3 + (1 - 3 * (R(1, 8) + R(1, 24))) / R(1, 24),
   "Rates: part done, then part left",
   r"Together: $\frac18+\frac1{24}=\frac16$ per hour, so $3$ hours finish $\frac12$ of the job. B does the other half at $\frac1{24}$ per hour: $12$ hours. Total $3+12=15$. ($6$ is the time if both worked the whole job; $12$ is B's time alone after A stops; $27$ adds B's full $24$ hours to the $3$.)")

mc(5, 'H',
   r"A car uses $7.5$ liters of fuel per $100$ kilometers. Which is closest to the car's fuel economy in miles per gallon? ($1$ mile $=1.6$ kilometers and $1$ gallon $=3.8$ liters)",
   C(32), [C(2), C(13), C(81)],
   lambda: rnd((R(100) / R(16, 10)) / (R(75, 10) / R(38, 10))),
   "Unit chain: miles over gallons",
   r"$100$ km $=\frac{100}{1.6}=62.5$ miles and $7.5$ L $=\frac{7.5}{3.8}\approx1.97$ gallons, so $\frac{62.5}{1.97}\approx32$ mpg. ($81$ multiplies km by $1.6$; $2$ multiplies liters by $3.8$; $13$ is $\frac{100}{7.5}$, km per liter, with no conversion.)")

gi(5, 'H',
   r"A cube-shaped tank has an inside edge length of $1.2$ meters. Water flows into the empty tank at $0.5$ liter per second. How many minutes does it take to fill the tank? ($1$ cubic meter $=1000$ liters)",
   "57.6", R(288, 5),
   lambda: (R(12, 10) ** 3 * 1000 / R(1, 2)) / 60,
   "Cubed length, then liters, then seconds to minutes",
   r"Volume $=1.2^3=1.728\ \text{m}^3=1728$ L. Time $=\frac{1728}{0.5}=3456$ s, and $\frac{3456}{60}=57.6$ minutes.")

mc(5, 'H',
   r"The radius and the height of a cone are each increased by $20\%$. By what percent does the volume of the cone increase?",
   C(r"72.8\%", R(728, 10)), [C(r"20\%", 20), C(r"44\%", 44), C(r"60\%", 60)],
   lambda: pct(R(12, 10) ** 2 * R(12, 10) - 1),
   "Volume scales by $k^3$",
   r"$V=\frac13\pi r^2h$ uses two factors of $r$ and one of $h$: $1.2\times1.2\times1.2=1.728$, an increase of $72.8\%$. ($20\%$ ignores the powers; $44\%$ uses $1.2^2$ only; $60\%$ is $3\times20\%$.)")

mc(5, 'H',
   r"Last year, $80\%$ of a school's seniors graduated. This year the number of seniors increased by $25\%$ and the number of graduates increased by $30\%$. By how many percentage points did the graduation rate change?",
   C("3.2", R(16, 5)), [C(4), C(5), C("83.2", R(832, 10))],
   lambda: pct(R(80, 100) * R(130, 100) / R(125, 100)) - 80,
   "Rate = part $\\div$ whole; percentage points",
   r"New rate $=\frac{0.80\times1.30}{1.25}=0.832=83.2\%$, which is $3.2$ points above $80\%$. ($83.2$ is the new rate, not the change; $5$ is $30-25$; $4$ is the $4\%$ \emph{percent} change, $\frac{1.30}{1.25}-1$, reported as points.)")

mc(5, 'H',
   r"A company has $2{,}000$ customers in three age groups. $${\small\setlength{\tabcolsep}{4pt}\begin{tabular}{|c|c|c|}\hline Age group & \% of customers & \% who subscribe\\\hline Under 30 & 45\% & 60\%\\ 30 to 49 & 35\% & 40\%\\ 50 and over & 20\% & 15\%\\\hline\end{tabular}}$$ Of all the customers who subscribe, which is closest to the percent who are under $30$?",
   C(r"61\%", 61), [C(r"27\%", 27), C(r"45\%", 45), C(r"60\%", 60)],
   lambda: rnd(pct((R(45, 100) * R(60, 100)) / (R(45, 100) * R(60, 100) + R(35, 100) * R(40, 100) + R(20, 100) * R(15, 100)))),
   "Conditional share: part of the subscribers, not of the customers",
   r"Subscribers as a share of all customers: $0.45(0.60)=0.27$, $0.35(0.40)=0.14$, $0.20(0.15)=0.03$, total $0.44$. Under $30$: $\frac{0.27}{0.44}\approx61\%$. ($27\%$ divides by all customers; $45\%$ is the group's share of customers; $60\%$ is the group's subscription rate.)",
   md="A company has $2{,}000$ customers in three age groups.\n\n   | Age group | Share of customers | Percent who subscribe |\n   |---|---|---|\n   | Under 30 | 45% | 60% |\n   | 30 to 49 | 35% | 40% |\n   | 50 and over | 20% | 15% |\n\n   Of all the customers who subscribe, which is closest to the percent who are under $30$?")

mc(5, 'H',
   r"A tub holds $120$ liters. A faucet adds water at $12$ liters per minute. After $5$ minutes of faucet alone, the drain is opened; it removes $8$ liters per minute while the faucet keeps running. How many more minutes pass until the tub is full?",
   C(15), [C(5), C(20), C(30)],
   lambda: R(120 - 5 * 12, 12 - 8),
   "Two-phase rate: leftover volume $\\div$ net rate",
   r"After $5$ minutes the tub holds $60$ liters, so $60$ more are needed at a net rate of $12-8=4$ L/min: $15$ minutes. ($5$ ignores the drain; $20$ is the total time, not the additional time; $30$ is $\frac{120}{4}$, ignoring the first $5$ minutes.)")

mc(5, 'H',
   r"A bacteria culture quadruples every $6$ hours. Which is closest to the percent by which the culture grows each hour?",
   C(r"26\%", 26), [C(r"50\%", 50), C(r"67\%", 67), C(r"300\%", 300)],
   lambda: Rational(round((4 ** (1 / 6) - 1) * 100)),
   "Equal-period growth: $(1+r)^6=4$",
   r"Let the hourly factor be $b$: $b^6=4$, so $b=4^{1/6}\approx1.26$, a growth of about $26\%$ per hour. ($300\%$ is the growth per $6$ hours; $50\%$ is $\frac{300}{6}$; $67\%$ is $\frac{400}{6}$.)")

mc(5, 'H',
   r"Brand X costs $40\%$ less per ounce than Brand Y. A $12$-ounce package of Brand X costs \$5.40. How much does a $16$-ounce package of Brand Y cost?",
   C(r"\$12.00", 12), [C(r"\$7.20", R(72, 10)), C(r"\$10.08", R(1008, 100)), C(r"\$18.00", 18)],
   lambda: (R(540, 100) / 12) / (1 - R(40, 100)) * 16,
   "``$n\\%$ less than $Y$'' means $0.6Y$, not $Y=1.4X$",
   r"X costs $\frac{5.40}{12}=0.45$ per ounce, and $0.45=0.60\,y$, so Y costs $0.75$ per ounce and $16(0.75)=12.00$. (\$7.20 gives Y the same unit price; \$10.08 uses $y=1.4x$; \$18.00 uses $y=\frac{x}{0.4}$.)")

mc(5, 'H',
   r"If $30\%$ of $P$ equals $45\%$ of $Q$, where $P$ and $Q$ are positive, then $P$ is what percent of $Q$?",
   C(r"150\%", 150), [C(r"15\%", 15), C(r"66\tfrac23\%", R(200, 3)), C(r"75\%", 75)],
   lambda: pct(R(45, 100) / R(30, 100)),
   "Set up $0.30P=0.45Q$ and divide",
   r"$0.30P=0.45Q$ gives $\frac PQ=\frac{0.45}{0.30}=1.5$, so $P$ is $150\%$ of $Q$. ($66\frac23\%$ is $Q$ as a percent of $P$; $15\%$ is $45-30$; $75\%$ is $30+45$.)")

gi(5, 'H',
   r"A company's profit rose $20\%$ from Year 1 to Year 2, fell $25\%$ from Year 2 to Year 3, and rose $40\%$ from Year 3 to Year 4. The Year 4 profit was \$63,000. What was the profit, in dollars, in Year 1?",
   "50000", Integer(50000),
   lambda: Rational(63000) / (R(12, 10) * R(75, 100) * R(14, 10)),
   "Reverse a chain: divide by the product of factors",
   r"The factors multiply: $1.20\times0.75\times1.40=1.26$. So Year 1 $=\frac{63{,}000}{1.26}=50{,}000$. (Adding the changes gives $46{,}667$.)")

gi(5, 'H',
   r"In a class, the mean score of the girls is $12$ points higher than the mean score of the boys. The mean score of the whole class is $3$ points higher than the boys' mean. What percent of the class is girls?",
   "25", Integer(25),
   lambda: pct(solve(12 * q - 3, q)[0]),
   "Weighted average: the gap splits in proportion",
   r"Let the girls be a fraction $f$ of the class and the boys' mean be $b$. The class mean is $b+12f$, so $12f=3$ and $f=\frac14=25\%$. (No actual scores are needed.)")

gi(5, 'H',
   r"Each edge of a cube is decreased by $10\%$. The surface area of the cube decreases by $a\%$ and the volume decreases by $b\%$. What is the value of $b-a$?",
   "8.1", R(81, 10),
   lambda: pct(1 - R(9, 10) ** 3) - pct(1 - R(9, 10) ** 2),
   "Area $k^2$, volume $k^3$ with $k=0.9$",
   r"Edges scale by $k=0.9$. Area: $0.9^2=0.81$, a decrease of $a=19$. Volume: $0.9^3=0.729$, a decrease of $b=27.1$. So $b-a=27.1-19=8.1$.")

mc(5, 'H',
   r"A rectangular field of $2$ hectares receives $25$ millimeters of rain, spread evenly over the field. How many liters of water fall on the field? ($1$ hectare $=10{,}000$ square meters and $1$ cubic meter $=1000$ liters)",
   C("500{,}000", 500000), [C(500), C("50{,}000", 50000), C("5{,}000{,}000", 5000000)],
   lambda: 2 * 10000 * R(25, 1000) * 1000,
   "Area $\\times$ depth, then liters",
   r"Area $=20{,}000\ \text{m}^2$ and depth $=25\ \text{mm}=0.025$ m, so the volume is $500\ \text{m}^3=500{,}000$ L. ($500$ is in cubic meters; $50{,}000$ uses $0.0025$ m; $5{,}000{,}000$ uses $0.25$ m.)")

mc(5, 'H',
   r"The radius of a circle is measured as $5\%$ greater than its true value. The area computed from the measured radius is what percent greater than the true area?",
   C(r"10.25\%", R(1025, 100)), [C(r"5\%", 5), C(r"10\%", 10), C(r"25\%", 25)],
   lambda: pct(R(105, 100) ** 2 - 1),
   "Relative error squares: $(1+e)^2-1$",
   r"Area $\propto r^2$, so the factor is $1.05^2=1.1025$, an increase of $10.25\%$. ($5\%$ copies the radius error; $10\%$ doubles it; $25\%$ squares the $5$.)")

# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(sympify(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
    except Exception:
        return None

def arrange_all():
    """Choose the print order of every MC problem and balance the correct letter globally.
    Numeric choices are normally printed in ascending or descending order; when a letter is already
    used more than its share, the right answer is instead placed first/last with the wrong choices sorted."""
    glob = [0, 0, 0, 0]
    perset = {}
    total_mc = sum(1 for p_ in PROBLEMS if p_['kind'] == 'mc')
    cap = -(-total_mc // 4)
    for p_ in PROBLEMS:
        if p_['kind'] != 'mc':
            continue
        ps = perset.setdefault(p_['set'], [0, 0, 0, 0])
        items = [p_['right']] + list(p_['wrongs'])
        numeric = all(_num(it[1]) is not None for it in items)
        order = p_['order']
        if isinstance(order, int):
            pos = order
            wr = list(p_['wrongs'])
            out = wr[:pos] + [p_['right']] + wr[pos:]
        elif order in ('a', 'd') or (order == 'auto' and numeric):
            asc = sorted(items, key=lambda it: float(sympify(it[1])))
            wsort = sorted(p_['wrongs'], key=lambda it: float(sympify(it[1])))
            pa = [i for i, it in enumerate(asc) if it is p_['right']][0]
            if order == 'a':
                pos, out = pa, asc
            elif order == 'd':
                pos, out = 3 - pa, asc[::-1]
            else:
                cands = []
                for out_, pos_, unsorted in ((asc, pa, 0), (asc[::-1], 3 - pa, 0),
                                              ([p_['right']] + wsort, 0, 1), (wsort + [p_['right']], 3, 1),
                                              ([p_['right']] + wsort[::-1], 0, 1), (wsort[::-1] + [p_['right']], 3, 1)):
                    over = 20 if glob[pos_] >= cap else 0
                    cands.append((over + unsorted * 2 + glob[pos_] * 0.5 + ps[pos_] * 0.3, pos_, out_))
                _, pos, out = min(cands, key=lambda c: c[0])
        else:  # free: wrongs keep listed order, right goes to the least used letter
            wr = list(p_['wrongs'])
            pos = min(range(4), key=lambda i: (glob[i], ps[i], i))
            out = wr[:pos] + [p_['right']] + wr[pos:]
        p_['choices'], p_['pos'] = out, pos
        p_['letter'] = LETTERS[pos]
        p_['answer'] = p_['letter']
        glob[pos] += 1
        ps[pos] += 1

def prepare():
    for i, p_ in enumerate(PROBLEMS):
        p_['n'] = sum(1 for q_ in PROBLEMS[:i] if q_['set'] == p_['set']) + 1
        if p_['kind'] == 'gi':
            p_['answer'] = p_['ans_tex']
    arrange_all()

def check(p_):
    if p_['kind'] == 'gi':
        got = p_['calc']()
        return (got is not None and same(got, p_['ans_val'])), got
    vals = [c_[1] for c_ in p_['choices']]
    distinct = all(not same(vals[i], vals[j]) for i in range(4) for j in range(i + 1, 4))
    if len(p_['choices']) != 4:
        return False, 'not 4 choices'
    if p_.get('each') is not None:
        truth = [bool(p_['each'](v)) for v in vals]
        ok = sum(truth) == 1 and truth[p_['pos']] and distinct
        return ok, p_['choices'][truth.index(True)][0] if any(truth) else 'none'
    got = p_['calc']()
    if isinstance(got, list):
        got = got[0] if len(got) == 1 else tuple(got)
    n_correct = sum(1 for v in vals if same(got, v))
    ok = same(got, p_['right'][1]) and n_correct == 1 and distinct and p_['choices'][p_['pos']][1] is p_['right'][1]
    return ok, got

def main():
    from collections import Counter
    prepare()
    fails = 0
    for p_ in PROBLEMS:
        ok, got = check(p_)
        tag = "S%d.%-2d" % (p_['set'], p_['n'])
        shown = p_['answer'] if p_['kind'] == 'gi' else "%s = %s" % (p_['letter'], p_['right'][0])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, got))
        if not ok:
            fails += 1
    print()
    print("problems:", len(PROBLEMS), " FAIL:", fails)
    for sn in range(1, 6):
        ps = [p_ for p_ in PROBLEMS if p_['set'] == sn]
        mcs = [p_ for p_ in ps if p_['kind'] == 'mc']
        print("Set %d: %d problems (%d MC, %d grid-in); correct-letter counts %s; difficulty %s" %
              (sn, len(ps), len(mcs), len(ps) - len(mcs),
               dict(sorted(Counter(p_['letter'] for p_ in mcs).items())),
               dict(Counter(p_['diff'] for p_ in ps))))
    allmc = [p_ for p_ in PROBLEMS if p_['kind'] == 'mc']
    print("All MC letter counts:", dict(sorted(Counter(p_['letter'] for p_ in allmc).items())))
    gcount = len(PROBLEMS) - len(allmc)
    print("grid-ins: %d of %d (%.0f%%)" % (gcount, len(PROBLEMS), 100.0*gcount/len(PROBLEMS)))
    print("ALL OK" if not fails else "SOME FAILED")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
