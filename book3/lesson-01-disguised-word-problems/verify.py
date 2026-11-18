#!/usr/bin/env python3
"""Book 3, Lesson 1 "Disguised & multi-step word problems": the problem bank AND its verifier.

Every problem is registered with its stem and choices (LaTeX), a worked solution that uses the
SHORTCUT (what students see), and a `calc` function that recomputes the answer independently
(solve / enumerate / simulate), not using the shortcut and not using the letter shown.

Running `python3 verify.py` recomputes every answer, checks that exactly one choice is correct
(and that all choices are distinct), balances the correct letters, and prints OK / FAIL per item.
`build.py` imports PROBLEMS from this file to write problems.md and lesson01-typeset.tex.
"""
import sys
import random
import itertools
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, expand, Poly,
                   diff, Eq, S, N as numeric, sympify, interpolate, floor, ceiling)

x, y, a, b, c, d, k, m, n, p, q, r, s, t, w, v = symbols('x y a b c d k m n p q r s t w v', real=True)
Q = Rational
f, g, l, wd, J, M, nb, pn, te, co, Lo, e, kk = symbols('f g l wd J M nb pn te co Lo e kk', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: read the last sentence first", "Medium and Hard"),
    2: ("Set 2", "Translate sentence by sentence: hidden information", "Hard"),
    3: ("Set 3", "Multi-step chains: rates, work, mixtures and units", "Hard"),
    4: ("Set 4", "Unfamiliar notation, models and what they mean", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- helpers
def C(tex_or_val, val=None):
    """Choice: C(66) or C(r"\\dfrac14", Rational(1,4)) -> (latex, value)."""
    if val is None:
        from sympy import latex
        return ("$%s$" % latex(sympify(tex_or_val)), sympify(tex_or_val))
    return ("$%s$" % tex_or_val, val)

def T(text, key=None):
    return (text, text if key is None else key)

def same(u, v):
    if isinstance(u, str) or isinstance(v, str):
        return u == v
    dd = sympify(u) - sympify(v)
    fs = dd.free_symbols
    if not fs:
        return abs(complex(numeric(dd, 30))) < 1e-9
    pts = [Rational(37, 100), Rational(191, 100), Rational(263, 100), Rational(-141, 100)]
    for pv in pts:
        if abs(complex(numeric(dd.subs({s_: pv for s_ in fs}), 30))) > 1e-9:
            return False
    return True

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='sort', **kw):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, **kw))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol, **kw):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol, **kw))

def lin(eqs, syms):
    return solve(eqs, syms, dict=True)[0]

def pick(pairs, truth):
    """pairs = [(text, predicate_or_value)]; return the text whose value equals truth."""
    hits = [tx for tx, val in pairs if (val == truth if isinstance(val, tuple) else same(val, truth))]
    assert len(hits) == 1, hits
    return hits[0]


def _lift_pick():
    grid = [(i, j) for i in range(0, 45) for j in range(0, 25)]
    truth = {(i, j) for (i, j) in grid if 40 + 12*i + 25*j <= 500 and i - j >= 3}
    cands = [
        (r"$12x+25y\le460$ and $x\ge y+3$", {(i, j) for (i, j) in grid if 12*i + 25*j <= 460 and i >= j + 3}),
        (r"$12x+25y\le500$ and $x\ge y+3$", {(i, j) for (i, j) in grid if 12*i + 25*j <= 500 and i >= j + 3}),
        (r"$12x+25y\le460$ and $x\ge3y$", {(i, j) for (i, j) in grid if 12*i + 25*j <= 460 and i >= 3*j}),
        (r"$12x+25y<460$ and $x>y+3$", {(i, j) for (i, j) in grid if 12*i + 25*j < 460 and i > j + 3}),
    ]
    hits = [tx for tx, st in cands if st == truth]
    assert len(hits) == 1
    return hits[0]

cu, bt, ra, rb, mm, ll, w2, cc, bb, gg, wk, pm = symbols('cu bt ra rb mm ll w2 cc bb gg wk pm', real=True)

def _extend_table():
    seq = [5, 8, 14, 26]
    dd = 12
    while len(seq) < 7:
        dd *= 2
        seq.append(seq[-1] + dd)
    return Integer(seq[6])

def _seq():
    aa = 5
    for _ in range(4):
        aa = 2*aa - 3
    return Integer(aa)
# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"A school play sold 120 tickets. Adult tickets cost \$8 and student tickets cost \$5, and the ticket revenue was \$735. How many more student tickets than adult tickets were sold?",
   C(30), [C(15), C(45), C(75)],
   lambda: (lambda sol: sol[s] - sol[a])(lin([a + s - 120, 8*a + 5*s - 735], [a, s])),
   "Read the last sentence first",
   r"The question asks for $s-a$, not $s$. From $a+s=120$ and $8a+5s=735$: $735-5(120)=3a=135$, so $a=45$ and $s=75$. The difference is $75-45=30$. (45 and 75 are the two counts; 15 is half the difference.)")

mc(1, 'M',
   r"A taxi charges a \$3.50 starting fee plus \$2.50 per mile. A passenger's total payment was \$21.50, which included a \$3.00 tip. How many miles was the ride?",
   C(6), [C(r"7.2", Q(36, 5)), C(r"7.4", Q(37, 5)), C(r"8.6", Q(43, 5))],
   lambda: (Q(43, 2) - 3 - Q(7, 2)) / Q(5, 2),
   "Remove what is not the fare",
   r"The tip is not part of the fare: $21.50-3.00-3.50=15.00$ is the mileage charge, and $15\div2.50=6$. (7.2 forgets the tip, 7.4 forgets the starting fee, 8.6 divides the whole payment by the rate.)")

gi(1, 'M',
   r"The sum of three consecutive odd integers is 111. What is the greatest of the three integers?",
   "39", Integer(39),
   lambda: [nn + 4 for nn in range(-200, 200) if nn % 2 != 0 and nn + (nn + 2) + (nn + 4) == 111][0],
   "Middle value = mean",
   r"For three consecutive numbers the middle one is the mean: $111\div3=37$. The three integers are 35, 37, 39, and the greatest is 39. (37 is the middle one.)")

mc(1, 'M',
   r"Seven less than 5 times a number is equal to 3 times the sum of the number and 5. What is the number?",
   C(11), [C(-1), C(4), C(6)],
   lambda: solve(5*n - 7 - 3*(n + 5), n)[0],
   "Translate sentence by sentence",
   r"``Seven less than 5 times a number'' is $5n-7$, and ``3 times the sum'' is $3(n+5)$. So $5n-7=3n+15$, $2n=22$, $n=11$. (Writing $7-5n$ gives $-1$; $3n+5$ gives 6; $5n+7$ gives 4.)")

gi(1, 'M',
   r"A cart's daily profit, in dollars, is $4.5c-210$, where $c$ is the number of cups sold in a day. The cart now sells 180 cups per day. How many more cups per day must it sell to make a daily profit of \$780?",
   "40", Integer(40),
   lambda: solve(Q(9, 2)*c - 210 - 780, c)[0] - 180,
   "Read the last sentence first",
   r"Profit \$780 needs $4.5c=990$, so $c=220$ cups. The question asks for the increase: $220-180=40$. (220 is the total, not the extra.)")

mc(1, 'M',
   r"Renting a bike costs a flat fee plus a fixed charge for each hour. A 3-hour rental costs \$19 and a 5-hour rental costs \$29. What does a 2-hour rental cost?",
   T(r"\$14.00", Integer(14)), [T(r"\$9.50", Q(19, 2)), T(r"\$10.00", Integer(10)), T(r"\$24.00", Integer(24))],
   lambda: (lambda sol: sol[f] + 2*sol[g])(lin([f + 3*g - 19, f + 5*g - 29], [f, g])),
   "Define variables with units",
   r"Two extra hours cost $29-19=10$, so each hour is \$5 and the flat fee is $19-15=\$4$. Two hours cost $4+10=\$14$. (\$10 forgets the fee; \$24 is the price of a 4-hour rental; \$9.50 halves the 3-hour price.)",
   order='free')

gi(1, 'H',
   r"Jun is 4 times as old as his sister Mei. In 6 years, Jun will be twice as old as Mei. How many years older is Jun than Mei?",
   "9", Integer(9),
   lambda: (lambda sol: sol[J] - sol[M])(lin([J - 4*M, J + 6 - 2*(M + 6)], [J, M])),
   "Read the last sentence first",
   r"Let Mei be $M$ now: $4M+6=2(M+6)$, so $2M=6$, $M=3$ and Jun is 12. The question asks for the age gap: $12-3=9$. (The gap never changes, so it is also $4M-M=3M$.)")

mc(1, 'M',
   r"The length of a rectangle is 3 more than twice its width, and its perimeter is 66. What is the area of the rectangle?",
   C(230), [C(10), C(23), C(33)],
   lambda: (lambda sol: sol[l] * sol[wd])(lin([l - 2*wd - 3, 2*(l + wd) - 66], [l, wd])),
   "Read the last sentence first",
   r"Perimeter 66 gives $l+w=33$. With $l=2w+3$: $3w+3=33$, so $w=10$ and $l=23$. The area is $10\cdot23=230$. (10 and 23 are the sides; 33 is half the perimeter.)")

mc(1, 'M',
   r"Three notebooks and 2 pens cost \$11.50. Two notebooks and 3 pens cost \$9.50. How much more does one notebook cost than one pen?",
   T(r"\$2.00", Integer(2)), [T(r"\$1.10", Q(11, 10)), T(r"\$3.10", Q(31, 10)), T(r"\$4.20", Q(21, 5))],
   lambda: (lambda sol: sol[nb] - sol[pn])(lin([3*nb + 2*pn - Q(23, 2), 2*nb + 3*pn - Q(19, 2)], [nb, pn])),
   "Subtract the equations",
   r"The question asks for $n-p$, so subtract the second purchase from the first: $n-p=11.50-9.50=2.00$. No need for the separate prices (\$3.10 and \$1.10). Adding instead gives $5(n+p)=21$, so \$4.20 is the price of one of each.",
   order='free')

mc(1, 'H',
   r"The mean of five numbers is 18. When a sixth number is included, the mean of the six numbers is 20. What is the sixth number?",
   C(30), [C(2), C(20), C(38)],
   lambda: 6*20 - 5*18,
   "Average = sum divided by count",
   r"Turn each mean into a sum: $5(18)=90$ and $6(20)=120$. The sixth number is $120-90=30$. (20 is the new mean, 38 is $18+20$, and 2 is $20-18$.)")

gi(1, 'H',
   r"A 450-liter tank is full. A pump drains it at 0.8 liter per second while a hose refills it at 30 liters per minute, both running at the same time. How many minutes will it take for the tank to be empty?",
   "25", Integer(25),
   lambda: Q(450) / (Q(4, 5)*60 - 30),
   "Units first",
   r"Put both rates in liters per minute: $0.8\times60=48$ drains and $30$ refills, so the tank loses $18$ liters per minute. $450\div18=25$ minutes. (Mixing seconds with minutes is the trap.)")

mc(1, 'H',
   r"A shop makes a sandwich from one of 3 breads, one of 4 fillings and one of 2 sauces. The tuna filling is never served with the spicy sauce. How many different sandwiches are possible?",
   C(21), [C(18), C(23), C(24)],
   lambda: Integer(len([1 for br, fl, sa in itertools.product(range(3), range(4), range(2)) if not (fl == 0 and sa == 0)])),
   "Count the forbidden ones",
   r"All combinations: $3\cdot4\cdot2=24$. The forbidden ones are tuna with spicy sauce on each of the 3 breads: 3 sandwiches. $24-3=21$. (23 forgets the breads; 18 throws out tuna altogether.)")

# ============================================================ SET 2  (Hard, 14)
mc(2, 'H',
   r"In a survey, every respondent chose either tea or coffee. Tea was chosen by 56 more respondents than coffee, and the number choosing tea was 1.5 times the number choosing coffee. How many people responded?",
   C(280), [C(112), C(168), C(224)],
   lambda: (lambda sol: sol[te] + sol[co])(lin([te - co - 56, te - Q(3, 2)*co], [te, co])),
   "Hidden total: two facts, two unknowns",
   r"With $t=c+56$ and $t=1.5c$: $0.5c=56$, so $c=112$ and $t=168$. The question asks for everyone: $112+168=280$. (112 is coffee, 168 is tea, 224 is double the coffee count.)")

gi(2, 'H',
   r"A drone's battery starts at 100\%. Takeoff uses 8\% of the charge. After takeoff, flying uses 4\% of the charge per minute for the first 10 minutes and 6\% per minute after that. For safety, the pilot must land while the charge is still more than 16\%. What is the greatest whole number of minutes the drone can fly after takeoff?",
   "15", Integer(15),
   lambda: max(mm for mm in range(0, 60) if 92 - 4*min(mm, 10) - 6*max(mm - 10, 0) > 16),
   "Strict inequality: test the boundary",
   r"After takeoff the charge is 92, and after 10 minutes it is $92-40=52$. Then $52-6j>16$ gives $j<6$, and $j=6$ gives exactly 16, which is not ``more than 16''. So $j=5$ and the flight is $10+5=15$ minutes. (16 uses $\ge$.)")

mc(2, 'H',
   r"A teacher has 10 test scores. The lowest score is 52. If it is dropped, the mean of the remaining 9 scores is 3 points higher than the mean of all 10 scores. What is the mean of all 10 scores?",
   C(79), [C(52), C(55), C(82)],
   lambda: solve((10*m - 52) / 9 - m - 3, m)[0],
   "Average = sum divided by count",
   r"Let $m$ be the mean of all 10: the 10 scores sum to $10m$. Then $\dfrac{10m-52}{9}=m+3$, so $10m-52=9m+27$ and $m=79$. (82 is the mean of the other nine; 52 is the dropped score.)")

mc(2, 'H',
   r"A jar holds only nickels, dimes and quarters: 60 coins worth \$9.90 in all. The number of quarters equals the number of nickels and dimes combined. How many dimes are in the jar?",
   C(18), [C(12), C(30), C(36)],
   lambda: [dd_ for nn in range(0, 61) for dd_ in range(0, 61) for qq in [60 - nn - dd_] if qq >= 0 and qq == nn + dd_ and 5*nn + 10*dd_ + 25*qq == 990][0],
   "Hidden given: a total stated as a relation",
   r"Quarters equal the other coins, so there are 30 quarters worth \$7.50, leaving \$2.40 = 240 cents for 30 nickels and dimes: $5n+10d=240$ with $n+d=30$. Then $5d=90$, $d=18$. (12 is the nickels, 30 the quarters.)")

mc(2, 'M',
   r"The squares of two consecutive positive odd integers add to 202. What is the product of the two integers?",
   C(99), [C(11), C(20), C(202)],
   lambda: [nn * (nn + 2) for nn in range(1, 100, 2) if nn**2 + (nn + 2)**2 == 202][0],
   "Define the variable, then answer the asked quantity",
   r"Let the integers be $n$ and $n+2$: $n^2+(n+2)^2=202$ gives $n^2+2n-99=0$, so $n=9$ and the integers are 9 and 11. The product is 99. (11 is the larger integer, 20 their sum.)")

mc(2, 'H',
   r"Maria has twice as many stickers as Leo. After Maria gives Leo 18 stickers, Leo has 6 more stickers than Maria. How many stickers did Maria have at the start?",
   C(60), [C(30), C(42), C(48)],
   lambda: (lambda sol: 2*sol[Lo])(lin([(Lo + 18) - (2*Lo - 18) - 6], [Lo])),
   "Before and after: write both states",
   r"Start: Leo $\ell$, Maria $2\ell$. After the gift: Leo $\ell+18$, Maria $2\ell-18$, and $\ell+18=(2\ell-18)+6$ gives $\ell=30$. Maria started with 60. (30 is Leo's start; 42 and 48 are the final counts.)")

mc(2, 'H',
   r"A freight lift can carry at most 500 kg, and this limit includes its own 40-kg pallet. It is loaded with $x$ boxes of 12 kg and $y$ boxes of 25 kg, with at least 3 more 12-kg boxes than 25-kg boxes. Which system of inequalities describes the possible values of $x$ and $y$?",
   T(r"$12x+25y\le460$ and $x\ge y+3$"),
   [T(r"$12x+25y\le500$ and $x\ge y+3$"), T(r"$12x+25y\le460$ and $x\ge3y$"), T(r"$12x+25y<460$ and $x>y+3$")],
   lambda: _lift_pick(),
   "Hidden given: the pallet is load too",
   r"The pallet uses 40 of the 500 kg, so the boxes may weigh at most $500-40=460$: $12x+25y\le460$. ``At least 3 more'' is $x\ge y+3$ (not $3y$, and not strict). Only the first system has both.",
   order='free')

mc(2, 'H',
   r"A space heater uses 1.5 kilowatts and runs 40 minutes each day. A fan uses 75 watts and runs 8 hours each day. Electricity costs \$0.12 per kilowatt-hour. What is the total cost of running both for 30 days? (1 kilowatt = 1000 watts)",
   T(r"\$5.76", Q(144, 25)), [T(r"\$2.16", Q(54, 25)), T(r"\$3.60", Q(18, 5)), T(r"\$218.16", Q(21816, 100))],
   lambda: (Q(3, 2)*Q(40, 60)*30 + Q(75, 1000)*8*30) * Q(12, 100),
   "Units hidden in context",
   r"Heater: $1.5\times\frac{40}{60}\times30=30$ kWh. Fan: $0.075\times8\times30=18$ kWh. Total $48$ kWh, and $48\times0.12=\$5.76$. (\$3.60 is the heater alone, \$2.16 the fan alone; \$218.16 treats 40 minutes as 40 hours.)",
   order='free')

gi(2, 'H',
   r"A delivery van drives 90 miles on each weekday (Monday to Friday) at 15 miles per gallon, and 40 miles on Saturday at 10 miles per gallon. It does not run on Sunday. Fuel costs \$3.20 per gallon. How many gallons does the van use in 4 weeks?",
   "136", Integer(136),
   lambda: 4 * (5*Q(90, 15) + Q(40, 10)),
   "Per-day versus per-week; ignore the price",
   r"One week: weekdays $5\times\frac{90}{15}=30$ gallons, Saturday $\frac{40}{10}=4$ gallons, so 34 gallons. Four weeks: $4\times34=136$. The price is not needed, and one average mileage for all days would be wrong.")

mc(2, 'H',
   r"At a farmers' market, a vendor pays a \$35 stall fee and drives 22 miles to the market. She sells eggs at \$4.50 per dozen and honey at \$9 per jar. She sells 3 more jars of honey than dozens of eggs, and her total sales are \$189. How many jars of honey does she sell?",
   C(15), [C(3), C(12), C(21)],
   lambda: (lambda sol: sol[e] + 3)(lin([Q(9, 2)*e + 9*(e + 3) - 189], [e])),
   "Ignore irrelevant information",
   r"Sales are \$189, so the fee and the mileage do not matter. With $e$ dozen: $4.5e+9(e+3)=189$, so $13.5e=162$ and $e=12$. Jars: $e+3=15$. (12 is the dozens, 3 the difference, 21 is $189\div9$.)")

gi(2, 'M',
   r"A drama club sells adult tickets for \$14 and child tickets for \$9. Exactly 40 child tickets are sold. The club needs ticket sales of at least \$1,250. What is the least number of adult tickets that must be sold?",
   "64", Integer(64),
   lambda: min(aa for aa in range(0, 500) if 14*aa + 9*40 >= 1250),
   "At least: round up",
   r"$14a+360\ge1250$ gives $a\ge\frac{890}{14}\approx63.6$. Tickets are whole, and 63 would fall short (\$1,242), so round up to 64.")

mc(2, 'H',
   r"A 120-meter rope is cut into three pieces. The second piece is 6 meters longer than the first, and the third piece is twice as long as the second. If $x$ is the length, in meters, of the first piece, which equation represents this situation?",
   T(r"$x+(x+6)+2(x+6)=120$"),
   [T(r"$x+(x+6)+2x=120$"), T(r"$x+(x+6)+(2x+6)=120$"), T(r"$x+(x+6)+\dfrac{x+6}{2}=120$")],
   lambda: (lambda pieces: pick([
       (r"$x+(x+6)+2(x+6)=120$", x + (x + 6) + 2*(x + 6)),
       (r"$x+(x+6)+2x=120$", x + (x + 6) + 2*x),
       (r"$x+(x+6)+(2x+6)=120$", x + (x + 6) + (2*x + 6)),
       (r"$x+(x+6)+\dfrac{x+6}{2}=120$", x + (x + 6) + (x + 6)/2),
   ], pieces))(x + (x + 6) + 2*(x + 6)),
   "Translate sentence by sentence",
   r"Piece 1 is $x$; piece 2 is $x+6$; piece 3 is ``twice the second'', $2(x+6)$ (the parentheses matter). Their sum is 120. (The wrong equations double the first piece, add the 6 after doubling, or halve the second piece.)",
   order='free')

mc(2, 'H',
   r"The marbles in a bag are red or blue in the ratio 3 to 5. After 12 more red marbles are added, the ratio of red to blue is 3 to 4. How many marbles are in the bag now?",
   C(140), [C(48), C(80), C(128)],
   lambda: (lambda sol: 3*sol[kk] + 12 + 5*sol[kk])(lin([4*(3*kk + 12) - 3*5*kk], [kk])),
   "Ratio parts: write 3k and 5k",
   r"Red $3k$, blue $5k$. Then $\dfrac{3k+12}{5k}=\dfrac34$, so $12k+48=15k$ and $k=16$. Now: red $48+12=60$, blue 80, total 140. (48 was the red, 80 the blue, 128 the total before.)")

gi(2, 'H',
   r"A group of friends splits the \$240 rental cost of a cabin equally. If 2 more friends join the group, each person's share drops by \$4. How many friends are in the original group?",
   "10", Integer(10),
   lambda: [sol for sol in solve(240/n - 240/(n + 2) - 4, n) if sol > 0][0],
   "Share = total divided by people",
   r"$\dfrac{240}{n}-\dfrac{240}{n+2}=4$ gives $480=4n(n+2)$, so $n^2+2n-120=0$ and $n=10$ (the other root, $-12$, is impossible). Check: \$24 each becomes \$20 each.")

# ============================================================ SET 3  (Hard, 14)
mc(3, 'H',
   r"A bakery sold muffins for \$3 each and scones for \$4.50 each one morning. It sold 5 fewer scones than muffins, and its total sales were \$277.50. How many dollars of the sales came from scones?",
   T(r"\$157.50", Q(315, 2)), [T(r"\$120.00", Integer(120)), T(r"\$175.50", Q(351, 2)), T(r"\$180.00", Integer(180))],
   lambda: (lambda sol: Q(9, 2)*(sol[mm] - 5))(lin([3*mm + Q(9, 2)*(mm - 5) - Q(555, 2)], [mm])),
   "Intermediate quantity is not the answer",
   r"With $m$ muffins and $m-5$ scones: $3m+4.5(m-5)=277.50$, so $7.5m=300$ and $m=40$. Scones: $35$, worth $35\times4.50=\$157.50$. (\$120 is the muffin sales; \$175.50 uses 5 more scones, not fewer; \$180 uses 40 scones.)",
   order='free')

gi(3, 'H',
   r"A cyclist rides 24 kilometers to a lake at 12 kilometers per hour and returns by the same route at 8 kilometers per hour. What is her average speed, in kilometers per hour, for the whole round trip?",
   "9.6", Q(48, 5),
   lambda: Q(48) / (Q(24, 12) + Q(24, 8)),
   "Average speed = total distance / total time",
   r"Times: $24\div12=2$ h and $24\div8=3$ h. Total distance 48 km in 5 h gives $48\div5=9.6$ km/h. (The average of the two speeds, 10, is the trap: she spends more time at the slower speed.)")

mc(3, 'H',
   r"Pump A can fill an empty pool in 6 hours, and pump B can fill it in 12 hours. Both pumps start at noon, but pump B is shut off after 2 hours while pump A keeps running. How many hours after noon is the pool full?",
   C(5), [C(4), C(6), C(8)],
   lambda: (lambda done: 2 + (1 - done) / Q(1, 6))(2*(Q(1, 6) + Q(1, 12))),
   "Work: add rates, track the fraction done",
   r"Together the pumps do $\frac16+\frac1{12}=\frac14$ of the pool per hour, so in 2 hours they fill $\frac12$. Pump A alone does the other $\frac12$ in 3 hours. Total $2+3=5$. (4 keeps B running; 6 is A alone; 8 lets B finish alone.)")

mc(3, 'H',
   r"A 50-liter cooling system holds a mixture that is $20\%$ antifreeze. A technician drains some of the mixture and replaces it with the same volume of pure antifreeze, so that the system is $36\%$ antifreeze. How many liters were drained?",
   C(10), [C(8), C(r"12.5", Q(25, 2)), C(40)],
   lambda: solve(50*Q(1, 5) - Q(1, 5)*r + r - 50*Q(9, 25), r)[0],
   "Mixture: what leaves, what enters",
   r"Antifreeze before: 10 L. Draining $x$ L removes $0.2x$ and adding $x$ L of pure antifreeze adds $x$: $10-0.2x+x=0.36(50)=18$, so $0.8x=8$ and $x=10$. (8 forgets that the drained liquid also held antifreeze.)")

mc(3, 'H',
   r"A machine makes 240 bolts per hour while it runs. It is scheduled for 16 hours per day, 6 days per week, but it is stopped for 2 hours of maintenance each day and makes nothing during that time. Each carton holds 1,500 bolts, and only full cartons are shipped. How many full cartons can be shipped from one week's production?",
   C(13), [C(14), C(15), C(16)],
   lambda: floor(Q(240*(16 - 2)*6, 1500)),
   "Units: per hour, per day, per week; full cartons round down",
   r"Running time is $16-2=14$ hours per day, so a week's production is $240\times14\times6=20{,}160$ bolts. $20{,}160\div1{,}500=13.44$, and only full cartons ship: 13. (14 rounds up; 15 and 16 ignore the maintenance hours.)")

mc(3, 'M',
   r"A boat travels 18 kilometers upstream in 1.5 hours. The same boat returns downstream over the same 18 kilometers in 1 hour. What is the speed of the current, in kilometers per hour?",
   C(3), [C(6), C(12), C(15)],
   lambda: (lambda sol: sol[cu])(lin([bt - cu - Q(18) / Q(3, 2), bt + cu - 18], [bt, cu])),
   "Define variables with units",
   r"Upstream $18\div1.5=12$ km/h $=b-c$; downstream $18\div1=18$ km/h $=b+c$. Subtracting: $2c=6$, so $c=3$. (12 is the upstream speed, 15 the boat's own speed, 6 the difference of the two speeds.)")

gi(3, 'H',
   r"A pool holds 650 gallons. A hose adds 15 gallons per minute, but a leak removes 5 gallons per minute. After 20 minutes the leak is fixed and a second hose, identical to the first, is added. Starting from empty, how many minutes after the start is the pool full?",
   "35", Integer(35),
   lambda: 20 + (650 - 20*(15 - 5)) / Q(2*15),
   "Two phases: net rate in each",
   r"Phase 1: net $15-5=10$ gal/min for 20 min gives 200 gal. Phase 2: two hoses give 30 gal/min, and the remaining $650-200=450$ gal take 15 min. Total $20+15=35$ min.")

mc(3, 'H',
   r"Machine A makes 3 widgets in the time machine B makes 2 widgets. Working together, they made 400 widgets in 8 hours. How many widgets does machine A make per hour?",
   C(30), [C(20), C(50), C(240)],
   lambda: (lambda sol: sol[ra])(lin([ra - Q(3, 2)*rb, 8*(ra + rb) - 400], [ra, rb])),
   "Ratio of rates",
   r"Together they make $400\div8=50$ per hour, split $3:2$ between A and B. A makes $\frac35\times50=30$ per hour. (20 is B's rate; 240 is A's total over 8 hours.)")

mc(3, 'H',
   r"A train leaves a station at 8:00 a.m. traveling at 48 miles per hour. A second train leaves the same station on the same track at 8:45 a.m., traveling at 60 miles per hour in the same direction. At what time does the second train catch the first?",
   T(r"11:45 a.m.", 705), [T(r"9:05 a.m.", 545), T(r"11:00 a.m.", 660), T(r"12:45 p.m.", 765)],
   lambda: 8*60 + 45 + (Q(48)*Q(45, 60)) / (60 - 48) * 60,
   "Head start, then closing speed",
   r"At 8:45 the first train is $48\times\frac34=36$ miles ahead. The second gains $60-48=12$ mph, so it needs $36\div12=3$ hours: 11:45 a.m. (11:00 counts the 3 hours from 8:00; 9:05 adds the speeds; 12:45 uses a 1-hour head start.)",
   order='free')

mc(3, 'H',
   r"Six workers, all working at the same rate, can build a wall in 20 days. After 8 days, 3 more workers join them, each working at that same rate. How many days, counting from the start, does it take to finish the wall?",
   C(16), [C(8), C(12), C(20)],
   lambda: 8 + (6*20 - 6*8) / Q(9),
   "Work = workers x days",
   r"The wall is $6\times20=120$ worker-days. In 8 days, $48$ are done, leaving 72. Nine workers do 72 worker-days in 8 days. Total $8+8=16$. (8 is the days after the helpers arrive; 12 and 20 do not account for the first 8 days correctly.)")

gi(3, 'H',
   r"Two walkers start 21 kilometers apart and walk toward each other along a straight road at 8 and 6 kilometers per hour. A dog starts with the first walker and runs back and forth between the two walkers at 12 kilometers per hour until they meet. How many kilometers does the dog run?",
   "18", Integer(18),
   lambda: 12 * (Q(21) / (8 + 6)),
   "Find the time first",
   r"The walkers close the gap at $8+6=14$ km/h, so they meet after $21\div14=1.5$ hours. The dog runs the whole time: $12\times1.5=18$ km. (No need to add up the back-and-forth trips.)")

mc(3, 'H',
   r"The table shows two kinds of driving for a car and the miles driven on a trip. [[TABLE]] If gas costs \$3.50 per gallon, how much does the gas for the trip cost?",
   T(r"\$38.50", Q(77, 2)), [T(r"\$32.67", Q(98, 3)), T(r"\$39.20", Q(196, 5)), T(r"\$49.00", Integer(49))],
   lambda: (Q(120, 24) + Q(216, 36)) * Q(7, 2),
   "Add gallons, not mileages",
   r"City: $120\div24=5$ gallons. Highway: $216\div36=6$ gallons. Total 11 gallons, and $11\times3.50=\$38.50$. (Averaging 24 and 36 to 30 mpg gives \$39.20; using 36 mpg for all miles gives \$32.67; 24 mpg for all gives \$49.)",
   table=[["Driving", "City", "Highway"], ["Miles per gallon", "24", "36"], ["Miles driven", "120", "216"]],
   order='free')

mc(3, 'H',
   r"Dana earns \$20 per hour for her first 40 hours in a week and 1.5 times that rate for every hour after 40. Last week she earned \$970, which included a \$20 bonus that is not based on hours. How many hours did she work?",
   C(45), [C(5), C(r"48.5", Q(97, 2)), C(r"32\tfrac13", Q(97, 3))],
   lambda: 40 + (970 - 20 - 800) / (Q(3, 2)*20),
   "Piecewise rate: separate the pieces",
   r"Remove the bonus: \$950 comes from hours. The first 40 hours pay \$800, and the remaining \$150 at \$30 per hour is 5 hours. Total $40+5=45$. (5 is only the overtime; 48.5 is $970\div20$; $32\frac13$ is $970\div30$.)")

gi(3, 'H',
   r"One faucet drips 4 drops per second and a second faucet drips 6 drops per second, both into the same bottle. Twenty drops make 1 milliliter. The bottle already holds 0.15 liter. How many minutes will it take to fill the bottle to 0.9 liter?",
   "25", Integer(25),
   lambda: (Q(900) - 150) * 20 / (4 + 6) / 60,
   "Units hidden in context",
   r"Still needed: $0.9-0.15=0.75$ L $=750$ mL $=15{,}000$ drops. Both faucets give $4+6=10$ drops per second, so $1500$ s, which is $1500\div60=25$ minutes.")

# ============================================================ SET 4  (Hard, 14)
def star_op(aa, bb):
    return 2*aa - bb**2

mc(4, 'H',
   r"For all real numbers $a$ and $b$, the operation $\star$ is defined by $a\star b=2a-b^2$. What is the value of $(3\star4)\star2$?",
   C(-24), [C(-22), C(-10), C(16)],
   lambda: star_op(star_op(3, 4), 2),
   "Invented operation: substitute inside first",
   r"Inside first: $3\star4=2(3)-4^2=-10$. Then $(-10)\star2=2(-10)-2^2=-24$. (Doing the 3 and 4 only gives $-10$; dropping the square gives $-22$; losing the minus sign gives 16.)")

gi(4, 'M',
   r"The fare, in dollars, for a taxi ride of $m$ miles is $F(m)=2.5m+4$. For two rides of $a$ miles and $b$ miles, the fare for the first ride is \$15 more than the fare for the second ride. What is the value of $a-b$?",
   "6", Integer(6),
   lambda: solve((Q(5, 2)*a + 4) - (Q(5, 2)*b + 4) - 15, a)[0] - b,
   "Function notation: the constant cancels",
   r"$F(a)-F(b)=2.5(a-b)$, because the \$4 cancels. So $2.5(a-b)=15$ and $a-b=6$. (No need to find either ride.)")

mc(4, 'H',
   r"A school sells adult tickets for \$15 and child tickets for \$6. The equation $15a+6c=420$ describes the combinations of $a$ adult tickets and $c$ child tickets that bring in exactly \$420. The equation is graphed with $a$ on the horizontal axis and $c$ on the vertical axis, and the slope of the line is $-2.5$. Which statement is the best interpretation of the slope?",
   T(r"Each additional adult ticket sold means 2.5 fewer child tickets for the same \$420."),
   [T(r"Each additional child ticket sold means 2.5 fewer adult tickets for the same \$420."),
    T(r"An adult ticket costs \$2.50 more than a child ticket."),
    T(r"The school sells 2.5 child tickets for every adult ticket.")],
   lambda: (lambda slope, unit: pick([
       (r"Each additional adult ticket sold means 2.5 fewer child tickets for the same \$420.", ("a", -Q(5, 2))),
       (r"Each additional child ticket sold means 2.5 fewer adult tickets for the same \$420.", ("c", -Q(5, 2))),
       (r"An adult ticket costs \$2.50 more than a child ticket.", ("diff", Q(5, 2))),
       (r"The school sells 2.5 child tickets for every adult ticket.", ("ratio", Q(5, 2))),
   ], (unit, slope)))(solve(15*a + 6*c - 420, c)[0].coeff(a), "a"),
   "Interpret a constant: slope is per one unit of the horizontal variable",
   r"Solve for $c$: $c=70-2.5a$. The slope is the change in $c$ (vertical) for a 1-unit increase in $a$ (horizontal): $a$ goes up 1, $c$ goes down 2.5. Swapping the axes would reverse the statement; the ticket prices differ by \$9, not \$2.50.",
   order='free')

mc(4, 'H',
   r"The table shows the number of members, $N(t)$, of an online club $t$ months after it launched. [[TABLE]] If the pattern in the table continues, how many members will the club have at $t=6$?",
   C(194), [C(23), C(98), C(320)],
   lambda: _extend_table(),
   "Choose the model: differences or ratios?",
   r"The first differences $3,6,12$ double each time, so the differences themselves grow exponentially: next $24,48,96$. Then $26+24=50$, $98$, and $98+96=194$ at $t=6$. (Equivalently $N=2+3\cdot2^t$.) Not linear (23), not $5\cdot2^t$ (320); 98 is $t=5$.",
   table=[[r"$t$ (months)", "0", "1", "2", "3"], [r"$N(t)$", "5", "8", "14", "26"]])

mc(4, 'H',
   r"The graph of a linear model for the water level, in centimeters, in a tank $t$ minutes after a drain is opened passes through the points $(4,38)$ and $(10,26)$. Which of the following is the best interpretation of the $t$-intercept of the graph?",
   T(r"The tank is empty 23 minutes after the drain is opened."),
   [T(r"The tank held 46 centimeters of water when the drain was opened."),
    T(r"The water level falls by 2 centimeters each minute."),
    T(r"The tank is empty 13 minutes after the drain is opened.")],
   lambda: (lambda slope: (lambda tint, yint: pick([
       (r"The tank is empty 23 minutes after the drain is opened.", ("t", 23)),
       (r"The tank held 46 centimeters of water when the drain was opened.", ("y", 46)),
       (r"The water level falls by 2 centimeters each minute.", ("slope", 2)),
       (r"The tank is empty 13 minutes after the drain is opened.", ("t", 13)),
   ], ("t", tint)))(solve(38 + slope*(t - 4), t)[0], 38 - slope*4))(Q(26 - 38, 10 - 4)),
   "Interpret a point: set the other variable to 0",
   r"The slope is $\frac{26-38}{10-4}=-2$, so $L=38-2(t-4)=46-2t$. The $t$-intercept is where $L=0$: $t=23$ minutes. (46 is the $y$-intercept, the starting level; $-2$ is the slope; 13 is $26\div2$, using a point that is not the intercept.)",
   order='free')

mc(4, 'H',
   r"A farmer has 120 meters of fencing and will use all of it to enclose a rectangular pen along a long straight barn wall. The wall forms one side of the pen, so only the other three sides need fencing. What is the greatest possible area of the pen, in square meters?",
   C(1800), [C(900), C(1600), C(3600)],
   lambda: max(ww*(120 - 2*ww) for ww in [Q(i, 2) for i in range(0, 121)]),
   "Choose the model: it is quadratic, so use the vertex",
   r"Two widths and one length: $l=120-2w$, area $A=w(120-2w)$. Its zeros are $0$ and $60$, so the maximum is at $w=30$: $A=30\cdot60=1800$. (900 fences all four sides; 1600 is a square pen; 3600 uses $l=120-w$.)")

mc(4, 'H',
   r"The weight, in grams, of a pouch holding $n$ identical coins is $f(n)=7.5n+12$. Which of the following is the best interpretation of $f(n+10)-f(n)$ in this context?",
   T(r"The weight of 10 coins, in grams"),
   [T(r"The weight of the pouch together with 10 coins, in grams"), T(r"The weight of $n+10$ coins, in grams"), T(r"The weight of the empty pouch, in grams")],
   lambda: (lambda dif: pick([
       (r"The weight of 10 coins, in grams", Integer(75)),
       (r"The weight of the pouch together with 10 coins, in grams", Integer(87)),
       (r"The weight of $n+10$ coins, in grams", Q(15, 2)*(n + 10)),
       (r"The weight of the empty pouch, in grams", Integer(12)),
   ], dif))(simplify((Q(15, 2)*(n + 10) + 12) - (Q(15, 2)*n + 12))),
   "Interpret an expression: the constant cancels",
   r"$f(n+10)-f(n)=7.5(10)=75$: the 12 g pouch cancels. So the expression is the weight of the 10 extra coins only. (The pouch is in both terms, so it is not counted in the difference.)",
   order='free')

mc(4, 'M',
   r"The digits of a two-digit positive integer add to 11. When the digits are reversed, the new number is 27 greater than the original number. What is the original number?",
   C(47), [C(38), C(56), C(74)],
   lambda: [10*tt + uu for tt in range(1, 10) for uu in range(0, 10) if tt + uu == 11 and (10*uu + tt) - (10*tt + uu) == 27][0],
   "Backsolve: test the choices",
   r"Test the choices (digit sum 11): $38\to83$ is $+45$; $47\to74$ is $+27$ yes; $56\to65$ is $+9$; $74\to47$ is $-27$. Algebra agrees: $9(u-t)=27$, so $u-t=3$ and $t+u=11$ give $t=4$, $u=7$.")

gi(4, 'H',
   r"A gift shop sells small boxes for \$6, medium boxes for \$10 and large boxes for \$15. On Saturday it sold 80 boxes and took in \$770. It sold twice as many small boxes as large boxes. How many medium boxes were sold?",
   "50", Integer(50),
   lambda: (lambda sol: 80 - sol[ll] - 2*sol[ll])(lin([6*(2*ll) + 10*(80 - 3*ll) + 15*ll - 770], [ll])),
   "Define variables with units: three unknowns, one parameter",
   r"Let $L$ be the large boxes: small $=2L$, medium $=80-3L$. Revenue: $12L+10(80-3L)+15L=770$ gives $-3L=-30$, so $L=10$. Medium: $80-30=50$.")

mc(4, 'H',
   r"A ball is dropped from a height of 160 centimeters. After each bounce it rises to $\frac34$ of its previous peak height. How high, in centimeters, does it rise after its third bounce?",
   C(r"67.5", Q(135, 2)), [C(40), C(90), C(120)],
   lambda: Q(160) * Q(3, 4)**3,
   "Choose the model: repeated multiplication, not subtraction",
   r"Each bounce multiplies by $\frac34$, so after 3 bounces: $160\left(\frac34\right)^3=160\cdot\frac{27}{64}=67.5$. (40 subtracts 25\% of 160 three times; 90 and 120 are the second and first bounces.)")

gi(4, 'H',
   r"A diner's meal includes one of 4 appetizers, one of 5 main dishes, and either one of 3 desserts or no dessert at all. The fish main dish is never served with the cheesecake, which is one of the 3 desserts. How many different meals are possible?",
   "76", Integer(76),
   lambda: Integer(len([1 for ap, mn, ds in itertools.product(range(4), range(5), range(4)) if not (mn == 0 and ds == 0)])),
   "Count with constraints: total minus forbidden",
   r"``No dessert'' is a fourth option: $4\cdot5\cdot4=80$ meals. Forbidden: fish with cheesecake, with any of the 4 appetizers: 4 meals. $80-4=76$. (Forgetting the no-dessert option gives 60.)")

mc(4, 'H',
   r"At a meeting, every person shakes hands exactly once with every other person. The table shows the total number of handshakes for $n$ people. [[TABLE]] Which expression gives the number of handshakes for $n$ people?",
   C(r"\dfrac{n(n-1)}{2}", n*(n - 1)/2), [C(r"2n-3", 2*n - 3), C(r"\dfrac{n(n+1)}{2}", n*(n + 1)/2), C(r"\dfrac{n^2}{2}", n**2/2)],
   lambda: expand(interpolate([(2, 1), (3, 3), (4, 6)], n)),
   "Table to equation: test every point",
   r"Test all four points. $2n-3$ fits $n=2,3$ but gives 5 at $n=4$ (it is not 6). $\frac{n(n+1)}2$ gives 3 at $n=2$; $\frac{n^2}2$ gives 2. Only $\frac{n(n-1)}2$ gives $1,3,6,10$. (Each pair of people shakes once: $\binom n2$.)",
   table=[[r"$n$", "2", "3", "4", "5"], [r"Handshakes", "1", "3", "6", "10"]], order='free')

gi(4, 'M',
   r"A sequence is defined by $a_1=5$ and $a_{n+1}=2a_n-3$ for every integer $n\ge1$. What is the value of $a_5$?",
   "35", Integer(35),
   lambda: _seq(),
   "Recursive rule: generate term by term",
   r"$a_2=2(5)-3=7$, $a_3=2(7)-3=11$, $a_4=19$, $a_5=2(19)-3=35$. (There is no shortcut like $5\cdot2^4=80$: the $-3$ changes every step.)")

mc(4, 'M',
   r"On a 30-question quiz, a correct answer earns 5 points, a wrong answer loses 2 points, and an unanswered question earns 0 points. A student leaves exactly 2 questions unanswered and scores 105 points. How many questions did the student answer incorrectly?",
   C(5), [C(7), C(23), C(25)],
   lambda: (lambda sol: sol[w2])(lin([cc + w2 - 28, 5*cc - 2*w2 - 105], [cc, w2])),
   "Read the last sentence first",
   r"Only 28 questions were answered: $c+w=28$ and $5c-2w=105$. Then $7c=161$, $c=23$, and $w=28-23=5$. (23 is the number correct; 7 counts the unanswered questions as wrong; 25 is correct plus unanswered.)")

# ============================================================ SET 5  Summit (20)
mc(5, 'H',
   r"For all real numbers $a$ and $b$, define $a\ast b=(a+b)^2-(a-b)^2$. If $x\ast6=72$, what is the value of $x$?",
   C(3), [C(12), C(18), C(36)],
   lambda: solve((x + 6)**2 - (x - 6)**2 - 72, x)[0],
   "Invented operation: simplify the definition first",
   r"$(a+b)^2-(a-b)^2=4ab$, so $x\ast6=24x=72$ and $x=3$. (12 is $72\div6$, forgetting the 4; 18 is $72\div4$, forgetting the 6; 36 forgets half of the 4.)")

mc(5, 'H',
   r"One pond has 40 lily pads, and the number doubles every week. A second pond has 600 lily pads and gains 100 per week. After how many whole weeks is the first pond's count first greater than the second pond's count?",
   C(5), [C(4), C(6), C(15)],
   lambda: min(ww for ww in range(0, 40) if 40*2**ww > 600 + 100*ww),
   "Choose the model: exponential versus linear",
   r"Test the weeks: $w=4$: $640$ versus $1000$; $w=5$: $1280$ versus $1100$. The first pond is first ahead at week 5. (Beating the second pond's starting 600 happens at week 4, which is not the comparison; $600\div40=15$ is a ratio, not a time.)")

mc(5, 'H',
   r"A rectangle's length is 7 centimeters more than its width. If the width is increased by 2 centimeters and the length is decreased by 4 centimeters, the area does not change. What is the perimeter of the original rectangle, in centimeters?",
   C(26), [C(3), C(10), C(30)],
   lambda: (lambda sol: 2*(sol[wd] + sol[wd] + 7))(lin([(wd + 2)*(wd + 7 - 4) - wd*(wd + 7)], [wd])),
   "Define variables, then write the unchanged quantity",
   r"Width $w$, length $w+7$: $(w+2)(w+3)=w(w+7)$ gives $5w+6=7w$, so $w=3$ and $l=10$. Perimeter $2(3+10)=26$. (3 and 10 are the sides; 30 is the area.)")

mc(5, 'H',
   r"A courier drives a 120-kilometer route in three equal-length parts, at 24, 40 and 60 kilometers per hour, in that order. What is the courier's average speed for the whole route, in kilometers per hour?",
   C(36), [C(40), C(r"41\tfrac13", Q(124, 3)), C(42)],
   lambda: Q(120) / (Q(40, 24) + Q(40, 40) + Q(40, 60)),
   "Average speed = total distance / total time",
   r"Each part is 40 km. Times: $\frac{40}{24}+1+\frac{40}{60}=\frac53+1+\frac23=\frac{10}3$ h. Average $120\div\frac{10}3=36$ km/h. (The mean of the speeds is $41\frac13$ and the middle speed is 40; both ignore that more time is spent going slowly.)")

gi(5, 'H',
   r"A florist makes a bouquet from roses and lilies, using whole numbers of flowers. A bouquet has at most 8 flowers, at least 2 roses, and at least as many lilies as roses. How many different bouquets (counted by number of roses and number of lilies) are possible?",
   "9", Integer(9),
   lambda: Integer(len([1 for rr in range(0, 9) for li in range(0, 9) if rr + li <= 8 and rr >= 2 and li >= rr])),
   "Count with constraints: organize by one variable",
   r"Go by roses $r$: $r=2$ allows 2 to 6 lilies (5 bouquets); $r=3$ allows 3 to 5 (3 bouquets); $r=4$ allows 4 only (1); $r=5$ would need at least 5 lilies, total 10, too many. $5+3+1=9$.")

mc(5, 'H',
   r"A 25-foot ladder leans against a vertical wall with its base 7 feet from the wall on level ground. The top of the ladder slides 4 feet down the wall, and the base moves away from the wall. How many feet does the base move?",
   C(8), [C(4), C(15), C(20)],
   lambda: sqrt(25**2 - (sqrt(25**2 - 7**2) - 4)**2) - 7,
   "Chain: find the intermediate height",
   r"Start: height $\sqrt{25^2-7^2}=24$. After sliding: height 20, so the base is $\sqrt{25^2-20^2}=15$ feet out. It moved $15-7=8$ feet. (4 copies the drop; 15 and 20 are positions, not the movement.)")

mc(5, 'H',
   r"A medicine's amount in the bloodstream halves every 6 hours. A patient has 640 milligrams in the bloodstream at 8 a.m. on Monday. How many milligrams remain at 8 a.m. on Wednesday, assuming no new doses?",
   C(r"2.5", Q(5, 2)), [C(5), C(40), C(80)],
   lambda: Q(640) * Q(1, 2)**(48 // 6),
   "Units hidden in context: count the half-lives",
   r"Monday 8 a.m. to Wednesday 8 a.m. is 48 hours, which is $48\div6=8$ half-lives: $640\left(\frac12\right)^8=640\div256=2.5$. (80 divides by 8, not by $2^8$; 40 is the Tuesday amount; 5 counts 7 half-lives.)")

gi(5, 'H',
   r"A caterer's price is a fixed setup fee plus a fixed charge per guest. The price is \$1,250 for 40 guests and \$1,750 for 65 guests. A second caterer charges \$22 per guest with no setup fee. For how many guests do the two caterers charge the same total?",
   "225", Integer(225),
   lambda: (lambda sol: solve(sol[f] + sol[g]*n - 22*n, n)[0])(lin([f + 40*g - 1250, f + 65*g - 1750], [f, g])),
   "Intermediate quantity: rebuild the first line",
   r"Per guest: $\frac{1750-1250}{65-40}=20$. Setup fee: $1250-40(20)=450$. Equal totals: $450+20g=22g$, so $g=225$.")

mc(5, 'H',
   r"In a class of 27 students, the boys' scores average 74, the girls' scores average 83, and the average for the whole class is 80. How many girls are in the class?",
   C(18), [C(6), C(9), C(r"13.5", Q(27, 2))],
   lambda: (lambda sol: sol[gg])(lin([bb + gg - 27, 74*bb + 83*gg - 80*27], [bb, gg])),
   "Weighted average: sums, not means",
   r"Total of all scores $=80\cdot27=2160$. With $b+g=27$: $74b+83g=2160$ gives $9g=2160-1998=162$, so $g=18$. (Shortcut: 80 is two-thirds of the way from 74 to 83, so two-thirds are girls. The answer 9 reverses the weights; 13.5 assumes an even split.)")

mc(5, 'H',
   r"The number of subscribers to a channel is modeled by $N(t)=3000(1.5)^{t/4}$, where $t$ is the number of months since the channel launched. Which statement is the best interpretation of the number 1.5 in this model?",
   T(r"The number of subscribers is multiplied by 1.5 every 4 months, a 50\% increase."),
   [T(r"The number of subscribers increases by 50\% every month."),
    T(r"The number of subscribers increases by 1.5 every 4 months."),
    T(r"The number of subscribers increases by 37.5\% every month.")],
   lambda: (lambda Nf: pick([
       (r"The number of subscribers is multiplied by 1.5 every 4 months, a 50\% increase.", ("x4", Q(3, 2))),
       (r"The number of subscribers increases by 50\% every month.", ("x1", Q(3, 2))),
       (r"The number of subscribers increases by 1.5 every 4 months.", ("+4", Q(3, 2))),
       (r"The number of subscribers increases by 37.5\% every month.", ("x1", Q(11, 8))),
   ], ("x4", Nf(4) / Nf(0))))(lambda tt: 3000 * Q(3, 2)**Q(tt, 4)),
   "Interpret a constant: the exponent says how often",
   r"The exponent $t/4$ makes one growth step every 4 months, and the factor per step is 1.5, so $N(t+4)=1.5\,N(t)$, a $50\%$ rise per 4 months. (Monthly growth is about 10.7\%, so ``50\% each month'' and ``37.5\% each month'' are wrong.)",
   order='free')

mc(5, 'H',
   r"A hiker starts at 7:15 a.m. and walks at 4.5 kilometers per hour for 2 hours 40 minutes. She rests for 20 minutes, then walks another 7.5 kilometers at 5 kilometers per hour. At what time does she finish?",
   T(r"11:45 a.m.", 705), [T(r"11:25 a.m.", 685), T(r"11:29 a.m.", 689), T(r"11:55 a.m.", 715)],
   lambda: 7*60 + 15 + 160 + 20 + Q(15, 2) / 5 * 60,
   "Ignore irrelevant information; add the times",
   r"Only the times matter: $2\text{ h }40\text{ min}+20\text{ min}+\frac{7.5}{5}\text{ h}=2{:}40+0{:}20+1{:}30=4{:}30$. From 7:15 that is 11:45 a.m. (11:25 forgets the rest; 11:29 writes 2 h 40 min as 2.4 h; 11:55 walks the second part at 4.5 km/h.)",
   order='free')

mc(5, 'H',
   r"A rectangular pool is 12 meters by 8 meters. A walkway of uniform width surrounds the pool, and the area of the walkway alone equals the area of the pool. What is the width of the walkway, in meters?",
   C(2), [C(3), C(4), C(6)],
   lambda: [ww for ww in solve((12 + 2*w)*(8 + 2*w) - 12*8 - 12*8, w) if ww > 0][0],
   "Define the variable: the width appears on both sides",
   r"The outer rectangle is $(12+2w)(8+2w)$ and must equal pool plus walkway $=2(96)=192$. So $4w^2+40w-96=0$, $w^2+10w-24=0$, $w=2$. (Adding $w$, not $2w$, to each side gives 4.)")

gi(5, 'H',
   r"On a graph of distance remaining, in kilometers, versus time, in minutes, commuter A's line passes through $(0,30)$ and $(45,0)$, and commuter B's line passes through $(0,39)$ and $(39,0)$. At what time, in minutes, do the two commuters have the same distance remaining?",
   "27", Integer(27),
   lambda: solve((30 - Q(30, 45)*t) - (39 - t), t)[0],
   "Equation from a described graph",
   r"A: $d=30-\frac23t$ (it covers 30 km in 45 min). B: $d=39-t$. Equal when $30-\frac23t=39-t$, so $\frac13t=9$ and $t=27$ minutes (both have 12 km left).")

gi(5, 'H',
   r"A ball is thrown upward from a platform 2 meters high. Its height, in meters, $t$ seconds later is $h(t)=-5t^2+vt+2$, where $v$ is the initial speed in meters per second and $v>0$. The ball is at a height of 22 meters at exactly one moment. What is the value of $v$?",
   "20", Integer(20),
   lambda: [vv for vv in solve(Poly(-5*t**2 + v*t + 2 - 22, t).discriminant(), v) if vv > 0][0],
   "Exactly one solution: discriminant is 0",
   r"Height 22 gives $-5t^2+vt-20=0$. One moment means one solution: $v^2-4(-5)(-20)=v^2-400=0$, so $v=20$ (positive). Equivalently 22 m is the maximum height.")

mc(5, 'H',
   r"Figure $n$ in a pattern is an $n$-by-$n$ square made only of tiles along its border; the inside is empty. Figure 1 has 1 tile, Figure 2 has 4 tiles, and Figure 3 has 8 tiles. Which figure has 96 tiles?",
   C(25), [C(24), C(26), C(100)],
   lambda: [nn for nn in range(1, 200) if (nn*nn - max(nn - 2, 0)**2) == 96][0],
   "Pattern with a linear rule",
   r"The border of an $n\times n$ square has $n^2-(n-2)^2=4n-4$ tiles (check: $n=3$ gives 8). $4n-4=96$ gives $n=25$. (24 is $96\div4$, forgetting the 4 corners counted twice; 100 adds 4.)")

mc(5, 'H',
   r"Three taxi companies charge as follows for a trip of $m$ miles: Alpha, \$2 per mile; Beta, a \$4 pickup fee plus \$1.50 per mile; Gamma, a flat \$18 for any trip. For which trip length is Beta strictly cheaper than both other companies?",
   T(r"9 miles", 9), [T(r"6 miles", 6), T(r"8 miles", 8), T(r"10 miles", 10)],
   lambda: [mi for mi in (6, 8, 9, 10) if 4 + Q(3, 2)*mi < 2*mi and 4 + Q(3, 2)*mi < 18][0],
   "Plug in answer choices",
   r"Beta beats Alpha when $4+1.5m<2m$, i.e. $m>8$, and beats Gamma when $4+1.5m<18$, i.e. $m<9.33$. So $8<m<9.33$: only 9 miles. (At 8 miles Alpha and Beta tie at \$16, so Beta is not strictly cheapest.)",
   order='free')

mc(5, 'H',
   r"A rental company's price for a car is a fixed rate for each week plus a fixed charge per mile driven. A 1-week rental with 300 miles costs \$320, and a 2-week rental with 500 miles costs \$600. What is the cost of a 3-week rental with 1,200 miles?",
   T(r"\$1,080", 1080), [T(r"\$900", 900), T(r"\$960", 960), T(r"\$1,200", 1200)],
   lambda: (lambda sol: 3*sol[wk] + 1200*sol[pm])(lin([wk + 300*pm - 320, 2*wk + 500*pm - 600], [wk, pm])),
   "Verbal model with two unknown rates",
   r"Let $W$ be the weekly rate and $r$ the mile rate: $W+300r=320$ and $2W+500r=600$. Doubling the first and subtracting: $100r=40$, so $r=0.40$ and $W=200$. Then $3(200)+1200(0.40)=1080$. (Scaling the prices, as in 900, 960 or 1,200, ignores that the two parts grow at different rates.)")

gi(5, 'H',
   r"Two runners start together at the same point of a 400-meter circular track and run in the same direction, one at 5 meters per second and the other at 7 meters per second. When the faster runner first catches up with the slower runner from behind, how many meters has the slower runner run?",
   "1000", Integer(1000),
   lambda: 5 * (Q(400) / (7 - 5)),
   "Catching up = one full lap of difference",
   r"The faster runner gains $7-5=2$ m/s and must gain one full lap, 400 m. That takes $400\div2=200$ s, in which the slower runner runs $5\times200=1000$ m. (The faster runner has run 1400 m.)")

mc(5, 'H',
   r"For all real numbers $x$ and $y$, define $x\odot y=x^2-2xy$. If $a>0$ and $a\odot3=16$, what is the value of $a\odot a$?",
   C(-64), [C(-4), C(8), C(64)],
   lambda: (lambda av: av**2 - 2*av*av)([vv for vv in solve(a**2 - 6*a - 16, a) if vv > 0][0]),
   "Invented operation: use the condition on the root",
   r"$a\odot3=a^2-6a=16$ gives $(a-8)(a+2)=0$, and $a>0$ forces $a=8$. Then $8\odot8=64-128=-64$. (The root $a=-2$ would give $-4$.)")

mc(5, 'H',
   r"A region taxes income as follows: $10\%$ of the first \$20,000, plus $25\%$ of every dollar above \$20,000. A resident owed \$4,500 in tax. What was the resident's income?",
   T(r"\$30,000", 30000), [T(r"\$18,000", 18000), T(r"\$38,000", 38000), T(r"\$45,000", 45000)],
   lambda: 20000 + (4500 - Q(1, 10)*20000) / Q(1, 4),
   "Piecewise rule: separate the pieces",
   r"The first \$20,000 gives \$2,000 in tax, so \$2,500 comes from the top bracket: $2500\div0.25=10{,}000$ above \$20,000. Income $=\$30{,}000$. (45,000 uses 10\% throughout; 18,000 uses 25\% throughout; 38,000 forgets the first \$2,000.)")
# ================================================================== balanced letters
LETTERS = "ABCD"

def arrange(p, letter=None):
    """Return (list of (tex,val) in print order, index of the correct one)."""
    items = [p['right']] + list(p['wrongs'])
    order = p['order']
    if order in ('sort', 'sort_a', 'sort_d'):
        asc = sorted(items, key=lambda it: float(it[1]))
        ai = [i for i, it in enumerate(asc) if it is p['right']][0]
        if order == 'sort_d' or (order == 'sort' and letter is not None and letter == 3 - ai and letter != ai):
            desc = asc[::-1]
            return desc, [i for i, it in enumerate(desc) if it is p['right']][0]
        return asc, ai
    pos = int(order) if order != 'free' else (letter if letter is not None else 0)
    wr = list(p['wrongs'])
    return wr[:pos] + [p['right']] + wr[pos:], pos

def plan_letters():
    rnd = random.Random(7)
    counts = [0, 0, 0, 0]
    prev = []
    for p in PROBLEMS:
        if p['kind'] != 'mc':
            continue
        order = p['order']
        if order in ('sort', 'sort_a', 'sort_d'):
            items = [p['right']] + list(p['wrongs'])
            asc = sorted(items, key=lambda it: float(it[1]))
            ai = [i for i, it in enumerate(asc) if it is p['right']][0]
            cands = {ai: 'sort_a', 3 - ai: 'sort_d'}
        elif order == 'free':
            cands = {i: i for i in range(4)}
        else:
            cands = {int(order): order}
        best = None
        for L, o in cands.items():
            score = (counts[L], (L in prev[-2:]), rnd.random())
            if best is None or score < best[0]:
                best = (score, L, o)
        _, L, o = best
        p['order'] = o if order in ('sort', 'sort_a', 'sort_d') else (L if order == 'free' else order)
        counts[L] += 1
        prev.append(L)

def prepare():
    plan_letters()
    for i, p in enumerate(PROBLEMS):
        p['n'] = sum(1 for q_ in PROBLEMS[:i] if q_['set'] == p['set']) + 1
        if p['kind'] == 'mc':
            p['choices'], p['pos'] = arrange(p)
            p['letter'] = LETTERS[p['pos']]
            p['answer'] = p['letter']
        else:
            p['answer'] = p['ans_tex']

def check(p):
    got = p['calc']()
    if p['kind'] == 'gi':
        return same(got, p['ans_val']), got
    ok = same(got, p['right'][1])
    vals = [c_[1] for c_ in p['choices']]
    n_correct = sum(1 for v in vals if same(got, v))
    distinct = all(not same(vals[i], vals[j]) for i in range(4) for j in range(i + 1, 4))
    return (ok and n_correct == 1 and distinct and p['choices'][p['pos']][1] is p['right'][1]), got

def main():
    prepare()
    fails = 0
    for p in PROBLEMS:
        try:
            ok, got = check(p)
        except Exception as e:      # a crashing calc is a failure
            ok, got = False, "EXC %r" % (e,)
        tag = "S%d.%-2d" % (p['set'], p['n'])
        shown = p['answer'] if p['kind'] == 'gi' else "%s = %s" % (p['letter'], p['right'][0])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, got))
        if not ok:
            fails += 1
    from collections import Counter
    print()
    print("problems:", len(PROBLEMS), " FAIL:", fails)
    for sn in range(1, 6):
        ps = [p for p in PROBLEMS if p['set'] == sn]
        mcs = [p for p in ps if p['kind'] == 'mc']
        print("Set %d: %d problems (%d MC, %d grid-in); correct-letter counts %s; difficulty %s" %
              (sn, len(ps), len(mcs), len(ps) - len(mcs),
               dict(sorted(Counter(p['letter'] for p in mcs).items())),
               dict(Counter(p['diff'] for p in ps))))
    allmc = [p for p in PROBLEMS if p['kind'] == 'mc']
    cnt = Counter(p['letter'] for p in allmc)
    print("All MC letter counts:", dict(sorted(cnt.items())))
    ngi = len(PROBLEMS) - len(allmc)
    print("Grid-in share: %d/%d = %.0f%%" % (ngi, len(PROBLEMS), 100.0*ngi/len(PROBLEMS)))
    if max(cnt.values()) - min(cnt.values()) > 3:
        print("LETTER BALANCE: FAIL")
        fails += 1
    print("ALL OK" if not fails else "FAILURES: %d" % fails)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
