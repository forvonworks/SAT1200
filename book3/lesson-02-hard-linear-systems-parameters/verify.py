#!/usr/bin/env python3
"""Book 3, Lesson 2 "Hard linear equations, systems & parameters": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX),
  * a worked solution (this is what students see),
  * a `calc` function (or an `each` predicate for "which option ..." items) that recomputes the
    answer independently of the printed solution (sympy / brute force over integer grids).

Running `python3 verify.py` recomputes every answer, checks that exactly one MC choice is correct
and that choices are distinct, balances the correct letters, and prints ALL OK / FAIL.
(`build.py` imports PROBLEMS from this file to write problems.md and the .tex files.)
"""
import sys
from fractions import Fraction
from itertools import product
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, expand, Poly, Matrix,
                   linsolve, EmptySet, floor, ceiling, Eq, S, nsimplify, Abs, oo, sympify, latex)

x, y, z, a, b, c, d, k, m, n, p, q, r, s, t = symbols('x y z a b c d k m n p q r s t', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "Systems with parameters: none, one or infinitely many solutions", "Hard"),
    3: ("Set 3", "Models in context: systems, rates, tables and interpretation", "Hard"),
    4: ("Set 4", "Inequalities, absolute value and identities", "Hard"),
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

def E(tex, aa, bb, cc):
    """Equation choice  a x + b y = c  stored as a tuple."""
    return ("$%s$" % tex, (aa, bb, cc))

def same(u, v):
    try:
        if sympify(u) == sympify(v):
            return True
    except Exception:
        pass
    if isinstance(u, (tuple, str, list)) or isinstance(v, (tuple, str, list)) or callable(u) or callable(v):
        return u == v
    return simplify(sympify(u) - sympify(v)) == 0

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='auto', each=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, each=each))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol))

def nsol(eqs, vs=(x, y)):
    """Number of solutions of a linear system (each expression = 0): 0, 1 or 'inf'."""
    s_ = linsolve(list(eqs), *vs)
    if s_ == EmptySet:
        return 0
    el = list(s_)[0]
    return 'inf' if any(e.free_symbols & set(vs) for e in el) else 1

def param_values(eq_fn, kk, kind):
    """Values of the parameter kk for which the 2x2 system eq_fn(kk)=(e1,e2) has `kind` solutions
    (0, 1 or 'inf'); candidates come from det = 0 (kind 0/'inf'), or are the complement for kind 1."""
    e1, e2 = [expand(e) for e in eq_fn(kk)]
    det = e1.coeff(x) * e2.coeff(y) - e1.coeff(y) * e2.coeff(x)
    cands = solve(det, kk)
    out = []
    for v in cands:
        if nsol([e1.subs(kk, v), e2.subs(kk, v)]) == kind:
            out.append(v)
    return sorted(out)

def tri_area(P, Q, R):
    return abs(P[0]*(Q[1] - R[1]) + Q[0]*(R[1] - P[1]) + R[0]*(P[1] - Q[1])) / 2

def lin1(expr, var=x):
    """Classify a linear equation expr = 0 in one variable: 0, 1 or 'inf'."""
    e_ = expand(expr)
    aa, bb = e_.coeff(var), e_.subs(var, 0)
    if aa != 0:
        return 1
    return 'inf' if bb == 0 else 0

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"In the system $kx+12y=9$ and $5x+4y=7$, $k$ is a constant. For which value of $k$ does the system have no solution?",
   C(15), [C(r"\dfrac53", Rational(5, 3)), C(3), C(20)],
   lambda: param_values(lambda kk: (kk*x + 12*y - 9, 5*x + 4*y - 7), k, 0),
   "Ratio test (a : b : c)",
   r"No solution means parallel, distinct lines: $\dfrac k5=\dfrac{12}{4}=3$, so $k=15$. The constants do not follow the ratio ($3\cdot7=21\ne9$), so the lines are distinct. ($\frac53$ inverts the ratio; $3$ is the ratio itself.)")

gi(1, 'M',
   r"In the system $2x+7y=b$ and $ax+21y=30$, $a$ and $b$ are constants. The system has infinitely many solutions. What is the value of $a+b$?",
   "16", Integer(16),
   lambda: (lambda lam: lam*2 + Integer(30)/lam)(Integer(21)/7) if nsol([2*x + 7*y - 10, 6*x + 21*y - 30]) == 'inf' else None,
   "Ratio test (a : b : c)",
   r"Infinitely many solutions means the equations are multiples of each other. $21=3\cdot7$, so multiply the first by $3$: $6x+21y=3b$. Then $a=6$ and $3b=30$, $b=10$, so $a+b=16$.")

mc(1, 'H',
   r"One equation of a system is $4(x-2y)=3y+10$. The system has no solution. Which could be the second equation?",
   E(r"-8x+22y=-5", -8, 22, -5),
   [E(r"8x-22y=20", 8, -22, 20), E(r"11x-4y=10", 11, -4, 10), E(r"4x+11y=10", 4, 11, 10)],
   None,
   "Which equation could be the second?",
   r"Rearrange: $4x-11y=10$. No solution needs the same slope but a different constant. $-8x+22y=-20$ would be the same line ($-2$ times everything); with $-5$ the lines are parallel. ($8x-22y=20$ is the same line; the other two cross it.)",
   order='free',
   each=lambda v: nsol([4*(x - 2*y) - 3*y - 10, v[0]*x + v[1]*y - v[2]]) == 0)

mc(1, 'M',
   r"At a bakery, 5 muffins and 4 bagels cost \$21.00, and 3 muffins and 4 bagels cost \$15.00. What is the cost of one bagel?",
   C(r"\$1.50", Rational(3, 2)), [C(r"\$3.00", 3), C(r"\$4.00", 4), C(r"\$6.00", 6)],
   lambda: solve([5*m + 4*b - 21, 3*m + 4*b - 15], [m, b])[b],
   "Subtract the equations",
   r"Subtract: $2m=6$, so a muffin is \$3.00. Then $4b=15-9=6$ and $b=\$1.50$. (\$3.00 is the muffin; \$6.00 is $4b$ before dividing by 4; \$4.00 comes from subtracting $5$ instead of $5\cdot3$.)")

mc(1, 'M',
   r"A teacher spends exactly \$600 on $x$ notebooks at \$3 each and $y$ binders at \$5 each, so $3x+5y=600$. What does the point $(0,120)$ on the graph of this equation represent?",
   T("No notebooks and 120 binders cost a total of \\$600.", (0, 120)),
   [T("120 notebooks and no binders cost a total of \\$600.", (120, 0)),
    T("The teacher can buy 120 items of either kind for \\$600.", 'either'),
    T("The teacher buys 120 binders for each notebook.", 'ratio')],
   None,
   "What does the point mean?",
   r"$x=0$ notebooks and $y=120$ binders: $5\cdot120=600$. The first coordinate is the number of notebooks. (Choice A swaps the coordinates: $3\cdot120=360\ne600$.)",
   order='free',
   each=lambda v: isinstance(v, tuple) and 3*v[0] + 5*v[1] == 600)

mc(1, 'M',
   r"Line $\ell$ passes through $(2,5)$ and $(6,13)$. Line $m$ is parallel to $\ell$ and passes through $(1,-4)$. What is the $y$-intercept of line $m$?",
   C(-6), [C(-4), C(2), C(6)],
   lambda: (lambda sl: -4 - sl*1)(Rational(13 - 5, 6 - 2)),
   "Parallel: same slope",
   r"Slope of $\ell$ is $\frac{13-5}{6-2}=2$, so $m$ is $y=2x+b$. Through $(1,-4)$: $-4=2+b$, $b=-6$. (2 is the slope; $-4$ is just the given $y$-coordinate.)")

mc(1, 'H',
   r"Line $q$ is perpendicular to the line $2x+3y=18$ and passes through $(10,6)$. What is the $x$-intercept of $q$?",
   C(6), [C(1), C(14), C(19)],
   lambda: (lambda sl: 10 - Rational(6)/sl)(-1/(Rational(-2, 3))),
   "Perpendicular: negative reciprocal",
   r"The given slope is $-\frac23$, so $q$ has slope $\frac32$. From $(10,6)$ down to $y=0$ is $6$ units, i.e. $6\div\frac32=4$ units left: $x=6$. (Slopes $\frac23$, $-\frac32$, $-\frac23$ give $1$, $14$, $19$.)")

mc(1, 'M',
   r"What is the sum of the solutions of $|4x-6|=14$?",
   C(3), [C(-2), C(5), C(7)],
   lambda: sum(solve(4*x - 6 - 14, x) + solve(4*x - 6 + 14, x)),
   "Absolute value: two cases",
   r"$4x-6=14$ gives $x=5$; $4x-6=-14$ gives $x=-2$. The sum is $3$. (Each single case, or the difference $7$, is a trap.)")

mc(1, 'H',
   r"For a constant $k$, the equation $3(2x-k)+x=7x+12$ has infinitely many solutions. What is the value of $k$?",
   C(-4), [C(-12), C(4), C(12)],
   lambda: solve(expand(3*(2*x - k) + x - (7*x + 12)).coeff(x, 0), k),
   "Identity: match the constants",
   r"The left side is $7x-3k$, so the $x$-terms already match. The constants must match too: $-3k=12$, so $k=-4$. (Forgetting to divide by $-3$ gives $-12$.)")

gi(1, 'H',
   r"What is the greatest integer $x$ that satisfies $3(2x-5)<4x+9$?",
   "11", Integer(11),
   lambda: max(v for v in range(-60, 61) if 3*(2*v - 5) < 4*v + 9),
   "Inequality: strict at the boundary",
   r"$6x-15<4x+9$, so $2x<24$ and $x<12$. The inequality is strict, so $12$ itself fails and the greatest integer is $11$.")

mc(1, 'M',
   r"Which ordered pair $(x,y)$ satisfies both $y>2x-3$ and $x+y<6$?",
   T("$(2,3)$", (2, 3)), [T("$(0,6)$", (0, 6)), T("$(4,1)$", (4, 1)), T("$(6,3)$", (6, 3))],
   None,
   "Test each point in both inequalities",
   r"$(2,3)$: $3>1$ and $5<6$, both true. $(0,6)$ fails $6<6$; $(4,1)$ fails $1>5$; $(6,3)$ fails both.",
   order='free',
   each=lambda v: v[1] > 2*v[0] - 3 and v[0] + v[1] < 6)

gi(1, 'H',
   r"A linear function $f$ has $f(-2)=19$ and $f(6)=-13$. For what value of $x$ does $f(x)=0$?",
   "11/4", Rational(11, 4),
   lambda: (lambda sl: solve(sl*(x - 6) - 13, x)[0])(Rational(-13 - 19, 6 + 2)),
   "Linear function from two points",
   r"Slope $=\frac{-13-19}{6-(-2)}=-4$, so $f(x)=-4x+11$ (using $f(-2)=8+11=19$). Then $-4x+11=0$ gives $x=\frac{11}4$. (Enter 11/4 or 2.75.)")

# ============================================================ SET 2  (Hard, 14)
mc(2, 'H',
   r"In the system $kx+9y=6$ and $4x+ky=-4$, $k$ is a constant. For which value of $k$ does the system have no solution?",
   C(6), [C(-6), C(r"\dfrac32", Rational(3, 2)), C(36)],
   lambda: param_values(lambda kk: (kk*x + 9*y - 6, 4*x + kk*y + 4), k, 0),
   "Ratio test (a : b : c)",
   r"Parallel needs $\frac k4=\frac9k$, so $k^2=36$ and $k=\pm6$. For $k=-6$ the second equation is $-\frac23$ times the first (the same line: infinitely many solutions). For $k=6$, scaling the first by $\frac23$ gives $4x+6y=4\ne-4$: parallel, no solution.")

gi(2, 'H',
   r"In the system $\dfrac13x+\dfrac45y=2$ and $px+qy=9$, $p$ and $q$ are constants and the system has infinitely many solutions. What is the value of $p+q$?",
   "5.1", Rational(51, 10),
   lambda: (lambda lam: lam*Rational(1, 3) + lam*Rational(4, 5))(Integer(9)/2)
           if nsol([x/3 + Rational(4, 5)*y - 2, Rational(3, 2)*x + Rational(18, 5)*y - 9]) == 'inf' else None,
   "Ratio test (a : b : c)",
   r"The equations must be the same line. Multiply the first by $\frac92$ so that $2$ becomes $9$: $\frac32x+\frac{18}5y=9$. Then $p+q=\frac32+\frac{18}5=\frac{51}{10}=5.1$.")

mc(2, 'H',
   r"One equation of a system is $5x-2(y+3)=2y+14$. The system has no solution. Which could be the second equation?",
   E(r"-10x+8y=-5", -10, 8, -5),
   [E(r"10x-8y=40", 10, -8, 40), E(r"4x+5y=20", 4, 5, 20), E(r"5x+4y=20", 5, 4, 20)],
   None,
   "Which equation could be the second?",
   r"Rearrange: $5x-2y-6=2y+14$ gives $5x-4y=20$. No solution needs coefficients in the ratio $5:-4$ but a different constant. $-10x+8y=-5$ is $-2$ times the left side, yet $-2\cdot20=-40\ne-5$: parallel. ($10x-8y=40$ is the same line; $4x+5y=20$ and $5x+4y=20$ cross it.)",
   order='free',
   each=lambda v: nsol([5*x - 2*(y + 3) - 2*y - 14, v[0]*x + v[1]*y - v[2]]) == 0)

mc(2, 'H',
   r"Which equation, together with $\dfrac25x-\dfrac13y=2$, forms a system with infinitely many solutions?",
   E(r"6x-5y=30", 6, -5, 30),
   [E(r"5x-6y=30", 5, -6, 30), E(r"6x-5y=15", 6, -5, 15), E(r"6x+5y=30", 6, 5, 30)],
   None,
   "Clear the fractions",
   r"Multiply by the common denominator $15$: $6x-5y=30$. That is the same line, so there are infinitely many solutions. ($5x-6y=30$ swaps the coefficients, $6x-5y=15$ is parallel, $6x+5y=30$ has a different slope.)",
   order='free',
   each=lambda v: nsol([Rational(2, 5)*x - Rational(1, 3)*y - 2, v[0]*x + v[1]*y - v[2]]) == 'inf')

mc(2, 'H',
   r"In the system $ax+by=20$ and $5x+2by=18$, $a$ and $b$ are constants. The graphs of the equations in the $xy$-plane intersect at the point $(2,y)$. What is the value of $a$?",
   C(8), [C("5.5", Rational(11, 2)), C(6), C(10)],
   lambda: solve([a*2 + c - 20, 5*2 + 2*c - 18], [a, c])[a],
   "Substitute the known coordinate",
   r"Put $x=2$ in the second equation: $10+2by=18$, so $by=4$. Then the first gives $2a+4=20$ and $a=8$. (Taking $by=9$ gives 5.5; $by=8$ gives 6; ignoring $by$ gives 10.)")

mc(2, 'H',
   r"If $5a+2b=34$ and $3a-4b=10$, what is the value of $a+3b$?",
   C(12), [C(6), C(22), C(44)],
   lambda: (lambda sl: sl[a] + 3*sl[b])(solve([5*a + 2*b - 34, 3*a - 4*b - 10], [a, b])),
   "Solve for the combination",
   r"Find $\lambda,\mu$ with $\lambda(5,2)+\mu(3,-4)=(1,3)$: $\lambda=\frac12$, $\mu=-\frac12$. So $a+3b=\frac12(34)-\frac12(10)=12$. (Adding the halves gives 22; adding the totals gives 44; $a=6$ alone is not asked.)")

mc(2, 'H',
   r"$6x+4y=50$ and $4x+6y=40$. What is the mean (average) of $x$ and $y$?",
   C("4.5", Rational(9, 2)), [C(9), C(45), C(90)],
   lambda: (lambda sl: (sl[x] + sl[y])/2)(solve([6*x + 4*y - 50, 4*x + 6*y - 40], [x, y])),
   "Add the equations",
   r"Add: $10x+10y=90$, so $x+y=9$ and the mean is $\frac92=4.5$. (9 is the sum; 90 is the sum of the right sides.)")

mc(2, 'H',
   r"For how many real values of $k$ does the system $kx+4y=7$ and $x+ky=3$ have no solution?",
   C(2), [C(0), C(1), C(4)],
   lambda: Integer(len(param_values(lambda kk: (kk*x + 4*y - 7, x + kk*y - 3), k, 0))),
   "Ratio test (a : b : c)",
   r"Parallel needs $\frac k1=\frac4k$, so $k=\pm2$. For $k=2$: $2x+4y=7$ versus $2x+4y=6$ (no solution). For $k=-2$: $-2x+4y=7$ versus $-2x+4y=-6$ (no solution). Both values work, so the answer is 2.")

gi(2, 'H',
   r"The graphs of $2x+3y=k$ and $x-y=2$ in the $xy$-plane intersect at a point on the line $y=2x$. What is the value of $k$?",
   "-16", Integer(-16),
   lambda: (lambda sl: 2*sl[x] + 3*sl[y])(solve([x - y - 2, y - 2*x], [x, y])),
   "Use the extra condition first",
   r"The two lines that do not contain $k$ meet where $x-y=2$ and $y=2x$: $x-2x=2$, so $x=-2$, $y=-4$. Then $k=2(-2)+3(-4)=-16$.")

mc(2, 'H',
   r"In the system $ax-6y=18$ and $2x+3y=b$, $a$ and $b$ are constants. The system has infinitely many solutions. What is the value of $a-b$?",
   C(5), [C(-13), C(-5), C(36)],
   lambda: (lambda lam: lam*2 - Integer(18)/lam)(Integer(-6)/3) if nsol([-4*x - 6*y - 18, 2*x + 3*y + 9]) == 'inf' else None,
   "Ratio test (a : b : c)",
   r"Multiply the second equation by $-2$ to match $-6y$: $-4x-6y=-2b$. Then $a=-4$ and $-2b=18$, so $b=-9$ and $a-b=5$. ($-13=a+b$, $-5=b-a$, $36=ab$.)")

gi(2, 'H',
   r"Line $\ell$ has equation $y=mx+b$. The system formed by $\ell$ and $3x-2y=5$ has no solution, and $\ell$ passes through $(4,7)$. What is the value of $b$?",
   "1", Integer(1),
   lambda: (lambda mm: 7 - 4*mm)(solve(3 - 2*m, m)[0]) if nsol([y - (Rational(3, 2)*x + 1), 3*x - 2*y - 5]) == 0 else None,
   "Slope-intercept comparison",
   r"$3x-2y=5$ is $y=\frac32x-\frac52$. No solution means $\ell$ has the same slope $\frac32$ and a different intercept. Through $(4,7)$: $7=6+b$, so $b=1$.")

mc(2, 'H',
   r"Which of the following systems of equations has infinitely many solutions?",
   T(r"$3x-2y=8$ and $-6x+4y=-16$", ((3, -2, 8), (-6, 4, -16))),
   [T(r"$2x+6y=10$ and $x+3y=10$", ((2, 6, 10), (1, 3, 10))),
    T(r"$5x+y=4$ and $10x+2y=6$", ((5, 1, 4), (10, 2, 6))),
    T(r"$x-4y=2$ and $4x-y=8$", ((1, -4, 2), (4, -1, 8)))],
   None,
   "Ratio test (a : b : c)",
   r"In $3x-2y=8$ and $-6x+4y=-16$ every number is multiplied by $-2$: the same line. In the first system doubling the second gives $2x+6y=20\ne10$; in the second, doubling the first gives $10x+2y=8\ne6$ (parallel); the last has different slopes.",
   order='free',
   each=lambda v: nsol([v[0][0]*x + v[0][1]*y - v[0][2], v[1][0]*x + v[1][1]*y - v[1][2]]) == 'inf')

gi(2, 'H',
   r"In the system $y=3x+k$ and $2y=6x+k+9$, $k$ is a constant. For one value of $k$ the system has infinitely many solutions. What is that value of $k$?",
   "9", Integer(9),
   lambda: solve(expand(2*(3*x + k) - (6*x + k + 9)).coeff(x, 0), k)[0],
   "Substitute and compare",
   r"Substitute $y$: $2(3x+k)=6x+k+9$, so $6x+2k=6x+k+9$. The $x$-terms cancel; $2k=k+9$ gives $k=9$. (For any other $k$ the lines are parallel and distinct.)")

mc(2, 'H',
   r"In the system $y=2x+a$ and $y=-x+b$, $a$ and $b$ are constants. The solution $(x,y)$ of the system has $x>0$. Which of the following must be true?",
   C(r"a<b", 'lt'), [C(r"a>b", 'gt'), C(r"a+b>0", 'sum'), C(r"ab>0", 'prod')],
   None,
   "Solve in terms of the constants",
   r"Set equal: $2x+a=-x+b$, so $x=\frac{b-a}3$. Then $x>0$ means $b>a$. (Try $a=-5,b=-2$ and $a=-1,b=3$ to see that $a+b>0$ and $ab>0$ can fail.)",
   order='free',
   each=lambda v: all({'lt': a_ < b_, 'gt': a_ > b_, 'sum': a_ + b_ > 0, 'prod': a_*b_ > 0}[v]
                      for a_ in range(-7, 8) for b_ in range(-7, 8) if Rational(b_ - a_, 3) > 0))

# ============================================================ SET 3  (Hard, 14)
mc(3, 'H',
   r"A chemist mixes a $20\%$ acid solution with a $50\%$ acid solution to make 90 liters of a $30\%$ acid solution. How many liters of the $50\%$ solution are used?",
   C(30), [C(27), C(45), C(60)],
   lambda: solve([p + q - 90, Rational(1, 5)*p + Rational(1, 2)*q - Rational(3, 10)*90], [p, q])[q],
   "Mixture: two equations",
   r"$p+q=90$ and $0.2p+0.5q=0.3(90)=27$. Substituting $p=90-q$: $18+0.3q=27$, so $q=30$. (60 is the $20\%$ amount; 45 assumes an even split; 27 is the liters of pure acid.)")

gi(3, 'H',
   r"A boat travels 36 kilometers upstream in 3 hours. The return trip downstream along the same route takes 2 hours. The boat's speed in still water and the speed of the current are both constant. What is the speed of the current, in kilometers per hour?",
   "3", Integer(3),
   lambda: solve([3*(p - q) - 36, 2*(p + q) - 36], [p, q])[q],
   "Rate equations (add / subtract)",
   r"Upstream speed $=36\div3=12$ and downstream speed $=36\div2=18$. With boat speed $v$ and current $c$: $v-c=12$ and $v+c=18$. Subtract: $2c=6$, so $c=3$.")

mc(3, 'H',
   r"A van carries $x$ boxes of 18 kilograms each and $y$ crates of 30 kilograms each, with a total load of exactly 450 kilograms: $18x+30y=450$. If the number of boxes increases by 5 and the total load stays 450 kilograms, how must the number of crates change?",
   T(r"It decreases by $3$.", -3),
   [T(r"It increases by $3$.", 3), T(r"It decreases by $\frac35$.", Rational(-3, 5)), T(r"It decreases by $\frac{25}{3}$.", Rational(-25, 3))],
   lambda: solve(18*5 + 30*t, t)[0],
   "Interpret the coefficients",
   r"5 more boxes add $5\cdot18=90$ kg, so the crates must remove $90$ kg: $90\div30=3$ crates. ($\frac35$ is the change per single box; $\frac{25}3$ inverts the ratio.)")

mc(3, 'H',
   r"The table gives values of the linear function $f$. $$\begin{array}{c|ccc}x&2&5&9\\\hline f(x)&9&18&30\end{array}$$ The graph of $g$ is the graph of $f$ shifted 4 units to the right. What is the $y$-intercept of the graph of $g$?",
   C(-9), [C(-1), C(7), C(15)],
   lambda: (lambda f: f.subs(x, -4))(9 + Rational(18 - 9, 5 - 2)*(x - 2)),
   "Linear function from a table, then shift",
   r"Slope $=\frac{18-9}{5-2}=3$, so $f(x)=3x+3$. Shifting right 4 gives $g(x)=f(x-4)=3x-9$, with $y$-intercept $-9$. (Shifting left gives 15; shifting up or down by 4 gives 7 or $-1$.)")

mc(3, 'H',
   r"A courier charges a flat fee for any parcel up to 2 kilograms, plus $c$ dollars for each kilogram above 2. A 4-kilogram parcel costs \$26 and a 7-kilogram parcel costs \$44. What is the cost of a 10-kilogram parcel?",
   C(r"\$62", 62), [C(r"\$56", 56), C(r"\$60", 60), C(r"\$74", 74)],
   lambda: (lambda sl: 44 + sl*3)(Rational(44 - 26, 7 - 4)),
   "Slope from two points",
   r"Each extra kilogram costs $\frac{44-26}{7-4}=\$6$, and both parcels are already above 2 kg. Ten kilograms is 3 kg more than seven: $44+3(6)=\$62$. (The flat fee is \$14, so \$74 charges all 10 kg; \$60 drops the fee; \$56 counts only 7 extra kilograms.)")

mc(3, 'H',
   r"On Monday a cafe sold 30 small and 20 large coffees for \$190. On Tuesday it sold 20 small and 30 large coffees for \$210. At these prices, how much money, in dollars, would 10 small and 10 large coffees cost?",
   C(80), [C(8), C(200), C(400)],
   lambda: (lambda sl: 10*sl[p] + 10*sl[q])(solve([30*p + 20*q - 190, 20*p + 30*q - 210], [p, q])),
   "Add the equations",
   r"Add: $50s+50l=400$, so $s+l=8$ and $10s+10l=80$. There is no need to find the prices (\$3 and \$5). (8 is one of each; 400 is the two totals added; 200 is their mean.)")

mc(3, 'H',
   r"A tank is filled by two pipes. If pipe A runs for $x$ minutes and pipe B runs for $y$ minutes, the tank is exactly full when $\dfrac{x}{12}+\dfrac{y}{20}=1$. What does the number 12 represent?",
   T(r"The number of minutes pipe A needs to fill the tank by itself.", 'alone'),
   [T(r"The number of minutes both pipes together need to fill the tank.", 'together'),
    T(r"The fraction of the tank that pipe A fills in one minute.", 'rate'),
    T(r"The number of minutes pipe B needs to fill the tank by itself.", 'Balone')],
   None,
   "Interpret by setting the other variable to 0",
   r"Turn pipe B off ($y=0$): $\frac x{12}=1$, so $x=12$ minutes. Pipe A alone needs 12 minutes. (Pipe A fills $\frac1{12}$ of the tank per minute, the reciprocal; 20 is pipe B's time.)",
   order='free',
   each=lambda v: v == ('alone' if solve(Rational(1, 12)*x - 1, x)[0] == 12 else None))

gi(3, 'H',
   r"A cyclist rides for a total of 3.5 hours, going 18 kilometers per hour on flat roads and 12 kilometers per hour uphill, and covers 54 kilometers. For how many minutes does the cyclist ride uphill?",
   "90", Integer(90),
   lambda: 60*solve(18*(Rational(7, 2) - t) + 12*t - 54, t)[0],
   "Rate equation (watch the units)",
   r"Let $u$ be the uphill hours: $18(3.5-u)+12u=54$, so $63-6u=54$ and $u=1.5$ hours. In minutes: $1.5\cdot60=90$.")

gi(3, 'H',
   r"A linear model predicts the number of subscribers, in thousands, of a streaming service $t$ months after launch. The model gives 52 thousand at 2 months and 88 thousand at 5 months. According to the model, what is the least whole number of months after launch at which the subscribers exceed 120 thousand?",
   "8", Integer(8),
   lambda: (lambda sl: int(floor((120 - (52 - 2*sl))/sl)) + 1)(Rational(88 - 52, 5 - 2)),
   "Linear model, then inequality",
   r"Slope $=\frac{88-52}{5-2}=12$ per month, so $S=12t+28$. $12t+28>120$ gives $t>7.67$, so the least whole month is $8$. (At $t=7$ the model gives 112, which is still below 120.)")

mc(3, 'H',
   r"For a linear function $f$ and a constant $a$, $f(a+3)-f(a)=12$. What is the value of $f(a+10)-f(a)$?",
   C(40), [C(4), C(22), C(120)],
   lambda: (lambda mm: 10*mm)(solve(3*m - 12, m)[0]),
   "Slope = change in output per unit input",
   r"A linear function changes by the same amount for equal steps: slope $=\frac{12}3=4$. Ten units of input change it by $4\cdot10=40$. (4 is the slope; $12+10=22$ and $12\cdot10=120$ are not proportional reasoning.)")

gi(3, 'H',
   r"On a test, each correct answer earns 4 points, each incorrect answer loses 1 point, and each unanswered question earns 0 points. Dana answered exactly 30 questions and scored 90 points. How many of her answers were incorrect?",
   "6", Integer(6),
   lambda: solve([p + q - 30, 4*p - q - 90], [p, q])[q],
   "Add the equations",
   r"With $c$ correct and $w$ incorrect: $c+w=30$ and $4c-w=90$. Add: $5c=120$, so $c=24$ and $w=30-24=6$.")

mc(3, 'H',
   r"Maya is 4 years older than twice Jon's age. In 6 years, the sum of their ages will be 52. How old is Maya now?",
   C(28), [C(12), C(34), C(36)],
   lambda: solve([m - (2*n + 4), (m + 6) + (n + 6) - 52], [m, n])[m],
   "Translate into two equations",
   r"$M=2J+4$ and $(M+6)+(J+6)=52$. Substitute: $3J+16=52$, so $J=12$ and $M=28$. (12 is Jon's age; 34 is Maya in 6 years; 36 comes from forgetting the 12 extra years.)")

mc(3, 'H',
   r"Plan A costs \$28 per month plus \$0.12 per gigabyte (GB) used. Plan B costs \$18 per month plus \$0.20 per GB used. For how many GB of monthly use do the two plans cost the same?",
   C(125), [C("12.5", Rational(25, 2)), C(50), C(575)],
   lambda: solve(28 + Rational(12, 100)*t - (18 + Rational(20, 100)*t), t)[0],
   "Set the two costs equal",
   r"$28+0.12g=18+0.20g$, so $10=0.08g$ and $g=125$. (50 divides by 0.20 only; 575 adds the fees instead of subtracting; 12.5 slips a decimal place.)")

mc(3, 'H',
   r"The linear functions $f$ and $g$ are defined by $f(x)=2x+3$ and $g(x)=-x+5$. For how many values of $x$ is $f(g(x))=g(f(x))$?",
   C(0), [C(1), C(2), ("Infinitely many", oo)],
   lambda: lin1(2*(-x + 5) + 3 - (-(2*x + 3) + 5)),
   "Compose, then compare the equation",
   r"$f(g(x))=2(-x+5)+3=-2x+13$ and $g(f(x))=-(2x+3)+5=-2x+2$. The $x$-terms match but $13\ne2$, so the equation has no solution: 0 values.")

# ============================================================ SET 4  (Hard, 14)
mc(4, 'H',
   r"What is the sum of all solutions of $|x-4|=2x-5$?",
   C(3), [C(0), C(1), C(4)],
   lambda: sum(v for v in (solve(x - 4 - (2*x - 5), x) + solve(x - 4 + (2*x - 5), x)) if Abs(v - 4) == 2*v - 5),
   "Absolute value: check each case",
   r"Case 1: $x-4=2x-5$ gives $x=1$, but then $|{-3}|=3\ne-3$: extraneous. Case 2: $x-4=-(2x-5)$ gives $x=3$, and $|{-1}|=1=2(3)-5$ works. Only $x=3$, so the sum is 3 (4 would include the fake root).")

gi(4, 'H',
   r"How many integers $x$ satisfy $|2x-7|\le9$?",
   "10", Integer(10),
   lambda: Integer(len([v for v in range(-60, 61) if abs(2*v - 7) <= 9])),
   "Absolute value inequality",
   r"$-9\le2x-7\le9$ gives $-2\le2x\le16$, so $-1\le x\le8$. The endpoints are included: $-1,0,\dots,8$ is $10$ integers.")

mc(4, 'H',
   r"A bakery bakes $x$ loaves and $y$ rolls in a batch. The oven holds at most 50 items, so $x+y\le50$. Loaves sell for \$6 and rolls for \$4, and the batch must bring in at least \$220, so $6x+4y\ge220$. Which ordered pair $(x,y)$ satisfies both inequalities?",
   T("$(30,15)$", (30, 15)), [T("$(10,35)$", (10, 35)), T("$(25,15)$", (25, 15)), T("$(35,20)$", (35, 20))],
   None,
   "Test each point in both inequalities",
   r"$(30,15)$: $45\le50$ and $180+60=240\ge220$. $(10,35)$ earns only $200$; $(25,15)$ earns only $210$; $(35,20)$ uses $55>50$ items.",
   order='free',
   each=lambda v: v[0] + v[1] <= 50 and 6*v[0] + 4*v[1] >= 220)

gi(4, 'H',
   r"A course grade is $70\%$ of the test average plus $30\%$ of the final exam score. Priya's test average is 74. What is the least final exam score that gives her a course grade of at least 80?",
   "94", Integer(94),
   lambda: solve(Rational(7, 10)*74 + Rational(3, 10)*t - 80, t)[0],
   "Weighted average inequality",
   r"$0.7(74)+0.3f\ge80$ gives $51.8+0.3f\ge80$, so $0.3f\ge28.2$ and $f\ge94$. The least score is 94.")

mc(4, 'H',
   r"The solution set of $ax-12<5x+6$ is $x>-3$, where $a$ is a constant. What is the value of $a$?",
   C(-1), [C(-11), C(7), C(11)],
   lambda: [av for av in range(-30, 31) if all((av*xv - 12 < 5*xv + 6) == (xv > -3)
                                                   for xv in [Rational(i, 42) for i in range(-420, 421)])],
   "Inequality: flip the sign when dividing by a negative",
   r"$(a-5)x<18$. The solution is $x>-3$ (the inequality flipped), so $a-5<0$ and $\frac{18}{a-5}=-3$, giving $a-5=-6$ and $a=-1$. (Ignoring the flip gives 11; adding $5x$ instead of subtracting gives $-11$; combining the constants as $-12+6$ gives 7.)")

gi(4, 'H',
   r"For constants $k$ and $m$, the equation $\dfrac{kx-9}{3}=5x+m$ has infinitely many solutions. What is the value of $k+m$?",
   "12", Integer(12),
   lambda: (lambda sl: sl[k] + sl[m])(solve([Rational(1, 3)*k - 5, Rational(-9, 3) - m], [k, m])),
   "Identity: match coefficients and constants",
   r"The left side is $\frac k3x-3$. Matching $x$-terms: $\frac k3=5$, so $k=15$. Matching constants: $-3=m$. Then $k+m=12$.")

mc(4, 'H',
   r"How many solutions does the following equation have? $$5(x-2)-3(x+4)=2x-20$$",
   T("No solution", 0), [T("Exactly one", 1), T("Exactly two", 2), T("Infinitely many", oo)],
   lambda: lin1(5*(x - 2) - 3*(x + 4) - (2*x - 20)),
   "Contradiction: variables cancel",
   r"The left side is $5x-10-3x-12=2x-22$. Then $2x-22=2x-20$ becomes $-22=-20$, which is false for every $x$: no solution.")

mc(4, 'H',
   r"In the $xy$-plane, the line $kx+3y=12$ is perpendicular to the line $4x-6y=7$, where $k$ is a constant. What is the value of $k$?",
   C("4.5", Rational(9, 2)), [C("-4.5", Rational(-9, 2)), C(-2), C(2)],
   lambda: solve((-k/3)*Rational(2, 3) + 1, k)[0],
   "Perpendicular: negative reciprocal",
   r"The slopes are $-\frac k3$ and $\frac{4}{6}=\frac23$. Perpendicular means the product is $-1$: $-\frac{2k}{9}=-1$, so $k=\frac92$. (Parallel would give $-2$; equal size of slopes gives 2.)")

mc(4, 'H',
   r"The lines $y=3x+2$ and $y=-x+10$ and the $y$-axis form a triangle. What is the area of the triangle?",
   C(8), [C(12), C(16), C(32)],
   lambda: (lambda sl: tri_area((0, 2), (0, 10), (sl[x], sl[y])))(solve([y - 3*x - 2, y + x - 10], [x, y])),
   "Triangle on the y-axis: base along the axis",
   r"The lines meet where $3x+2=-x+10$: $x=2$, $y=8$. The base on the $y$-axis runs from $2$ to $10$, so it is $8$, and the height is the $x$-coordinate $2$. Area $=\frac12(8)(2)=8$. (16 forgets the $\frac12$; 12 adds the intercepts; 32 uses the $y$-coordinate 8 as the height.)")

mc(4, 'H',
   r"A truck can carry at most 2,400 pounds. A shipment contains small crates of 30 pounds and large crates of 75 pounds, with at least twice as many small crates as large crates. What is the greatest number of large crates the truck can carry?",
   C(17), [C(18), C(24), C(32)],
   lambda: max(bb for bb in range(0, 100)
               if any(30*aa + 75*bb <= 2400 for aa in range(2*bb, 2*bb + 200))),
   "Constraints: use the boundary",
   r"With $b$ large crates, at least $2b$ small crates are needed: $30(2b)+75b=135b\le2400$, so $b\le17.8$ and $b=17$. (18 rounds up; 24 ignores the small crates; 32 is $2400\div75$.)")

gi(4, 'H',
   r"The point $(k,6)$ satisfies both $y<3x-3$ and $x+y\le13$. How many integer values of $k$ are possible?",
   "4", Integer(4),
   lambda: Integer(len([kk for kk in range(-60, 61) if 6 < 3*kk - 3 and kk + 6 <= 13])),
   "System of inequalities: intersect the ranges",
   r"$6<3k-3$ gives $k>3$ (strict), and $k+6\le13$ gives $k\le7$. So $k=4,5,6,7$: four values.")

mc(4, 'H',
   r"For real numbers $x$ and $y$, $|x-6|\le4$ and $|y+2|\le3$. What is the greatest possible value of $x-y$?",
   C(15), [C(9), C(11), C(13)],
   lambda: max(xv - yv for xv in range(2, 11) for yv in range(-5, 2)),
   "Absolute value as an interval",
   r"$|x-6|\le4$ means $2\le x\le10$; $|y+2|\le3$ means $-5\le y\le1$. To make $x-y$ largest take $x=10$ and $y=-5$: $15$. (9 uses $y=1$; 11 uses $x=6$; 13 forgets the shift in $y$.)")

mc(4, 'H',
   r"A part's diameter $d$, in millimeters, is acceptable if $14.2\le d\le14.8$. Which inequality describes exactly the acceptable diameters?",
   T(r"$|d-14.5|\le0.3$", (Rational(29, 2), Rational(3, 10))),
   [T(r"$|d-14.5|\le0.6$", (Rational(29, 2), Rational(3, 5))), T(r"$|d-14.8|\le0.3$", (Rational(74, 5), Rational(3, 10))),
    T(r"$|d-0.3|\le14.5$", (Rational(3, 10), Rational(29, 2)))],
   None,
   "Absolute value = center and half-width",
   r"The midpoint is $\frac{14.2+14.8}2=14.5$ and the half-width is $\frac{14.8-14.2}2=0.3$, so $|d-14.5|\le0.3$. (0.6 is the full width; 14.8 is an endpoint, not the center.)",
   order='free',
   each=lambda v: all((abs(dv - v[0]) <= v[1]) == (Rational(142, 10) <= dv <= Rational(148, 10))
                      for dv in [Rational(i, 20) for i in range(13*20, 16*20 + 1)]))

mc(4, 'H',
   r"How many solutions does the equation $|x+2|+|x-4|=6$ have?",
   T("Infinitely many", oo), [T("No solution", 0), T("Exactly one", 1), T("Exactly two", 2)],
   lambda: (lambda sols: oo if len(sols) > 2 else Integer(len(sols)))(
       [xv for xv in [Rational(i, 4) for i in range(-80, 81)] if abs(xv + 2) + abs(xv - 4) == 6]),
   "Absolute value: distance reading",
   r"$|x+2|+|x-4|$ is the sum of the distances from $x$ to $-2$ and to $4$. The points are 6 apart, so every $x$ between them (and including them) gives exactly 6: infinitely many solutions.")

# ============================================================ SET 5  (Hard, 20)  SUMMIT
mc(5, 'H',
   r"In the system $kx+2y=10$ and $3x+(k-1)y=10$, $k$ is a constant. For which value of $k$ does the system have no solution?",
   C(-2), [C(-3), C(2), C(3)],
   lambda: param_values(lambda kk: (kk*x + 2*y - 10, 3*x + (kk - 1)*y - 10), k, 0),
   "Ratio test (two candidates, check the constants)",
   r"Parallel needs $k(k-1)=2\cdot3$, so $k^2-k-6=0$ and $k=3$ or $-2$. At $k=3$ both equations are $3x+2y=10$ (infinitely many solutions). At $k=-2$ they are $x-y=-5$ and $x-y=\frac{10}3$: parallel and distinct, so no solution.")

gi(5, 'H',
   r"Line $\ell$ passes through $(2k,5)$ and $(6k,17)$, where $k$ is a positive constant, and $\ell$ is parallel to the line $3x-2y=8$. What is the $y$-intercept of $\ell$?",
   "-1", Integer(-1),
   lambda: (lambda kk: 5 - Rational(3, 2)*(2*kk))(solve(Rational(17 - 5)/(6*k - 2*k) - Rational(3, 2), k)[0]),
   "Slope from two points; parallel",
   r"Slope of $\ell$ is $\frac{17-5}{6k-2k}=\frac3k$; the given line has slope $\frac32$, so $k=2$. The points are $(4,5)$ and $(12,17)$: $y=\frac32x+b$ with $5=6+b$, so $b=-1$.")

mc(5, 'H',
   r"For which value of the constant $c$ does the equation $2(cx-3)=4x-c$ have no solution?",
   C(2), [C(-2), C(4), C(6)],
   lambda: [cv for cv in range(-20, 21) if lin1(2*(cv*x - 3) - (4*x - cv)) == 0],
   "Contradiction: equal x-coefficients, unequal constants",
   r"$2cx-6=4x-c$. No solution needs equal $x$-coefficients: $2c=4$, $c=2$, and then the constants $-6$ and $-2$ differ. ($c=6$ makes the constants equal but then $x=0$ is a solution.)")

gi(5, 'H',
   r"The numbers $x$ and $y$ satisfy $2x+y=3k$ and $x-2y=k+5$, where $k$ is a constant. If $x+y=7$, what is the value of $k$?",
   "5", Integer(5),
   lambda: solve([2*x + y - 3*k, x - 2*y - k - 5, x + y - 7], [x, y, k])[k],
   "Three equations, three unknowns",
   r"Double the first: $4x+2y=6k$; add the second: $5x=7k+5$. Then $y=3k-2x=\frac{k-10}5$ and $x+y=\frac{8k-5}5=7$, so $k=5$. (Check: $x=8$, $y=-1$.)")

mc(5, 'H',
   r"How many liters of pure water must be added to 40 liters of a $35\%$ salt solution to make a $28\%$ salt solution?",
   C(10), [C(7), C(8), C(14)],
   lambda: solve(Rational(35, 100)*40 - Rational(28, 100)*(40 + t), t)[0],
   "Mixture: the amount of salt does not change",
   r"Salt: $0.35(40)=14$ liters stays constant. $14=0.28(40+w)$ gives $40+w=50$ and $w=10$. (14 is the salt amount; 7 is the percent difference; 8 divides by $35\%$.)")

gi(5, 'H',
   r"How many ordered pairs $(x,y)$ of positive integers satisfy $2x+3y\le20$?",
   "27", Integer(27),
   lambda: Integer(len([(xv, yv) for xv in range(1, 30) for yv in range(1, 30) if 2*xv + 3*yv <= 20])),
   "Lattice points: count row by row",
   r"For $y=1,2,3,4,5,6$ the inequality $2x\le20-3y$ allows $x\le8,7,5,4,2,1$. That is $8+7+5+4+2+1=27$ pairs. ($y=7$ would need $x\le-0.5$.)")

mc(5, 'H',
   r"The function $f(x)=ax+b$ has $a>0$ and satisfies $f(f(x))=9x+8$. What is the value of $f(1)$?",
   C(5), [C(-7), C(3), C(11)],
   lambda: (lambda aa: aa + solve(aa*b + b - 8, b)[0])([v for v in solve(a**2 - 9, a) if v > 0][0]),
   "Compose, then match coefficients",
   r"$f(f(x))=a(ax+b)+b=a^2x+ab+b$. So $a^2=9$ with $a>0$ gives $a=3$, and $3b+b=8$ gives $b=2$. Then $f(1)=3+2=5$. ($a=-3$ would give $-7$ but is excluded; 11 takes $b=8$.)")

mc(5, 'H',
   r"How many solutions does the equation $\big||x-3|-2\big|=1$ have?",
   C(4), [C(1), C(2), C(3)],
   lambda: Integer(len([xv for xv in [Rational(i, 4) for i in range(-80, 81)] if abs(abs(xv - 3) - 2) == 1])),
   "Absolute value: peel the layers",
   r"$|x-3|-2=1$ or $-1$, so $|x-3|=3$ or $|x-3|=1$. That gives $x=0,6$ and $x=2,4$: four solutions. (Stopping after the first layer gives 2.)")

mc(5, 'H',
   r"A school orders $x$ adult tickets at \$5 each and $y$ student tickets at \$3 each. It needs at least 12 tickets in all, at least 3 adult tickets, and at most 8 student tickets. What is the least possible total cost, in dollars?",
   C(44), [C(36), C(39), C(60)],
   lambda: min(5*xv + 3*yv for xv in range(0, 40) for yv in range(0, 40) if xv + yv >= 12 and xv >= 3 and yv <= 8),
   "Constraints: spend on the cheaper item up to its limit",
   r"Student tickets are cheaper, so buy the most allowed: $y=8$. Then $x\ge4$ to reach 12 tickets: $5(4)+3(8)=44$. (36 uses 12 student tickets, ignoring the cap; 39 buys only 11 tickets; 60 is all adult.)")

gi(5, 'H',
   r"Car A leaves a rest stop at 1:00 p.m. and travels at 48 miles per hour. Car B leaves the same rest stop at 1:45 p.m. on the same road and travels at 60 miles per hour. How many miles from the rest stop is Car B when it catches up to Car A?",
   "180", Integer(180),
   lambda: 48*solve(48*t - 60*(t - Rational(3, 4)), t)[0],
   "Rate equation: equal distances",
   r"Let $t$ be Car A's hours: $48t=60\left(t-\frac34\right)$, so $12t=45$ and $t=3.75$. Distance $=48(3.75)=180$ miles. (Check: Car B drives 3 hours at 60 mph.)")

mc(5, 'H',
   r"Plan A costs $C=40+12m$ dollars after $m$ months, and Plan B costs $C=100+7m$ dollars. The system has the solution $(12,184)$. Which statement is true?",
   T(r"Plan A costs more than Plan B when $m>12$.", 'D'),
   [T(r"Plan A costs more than Plan B for every $m$.", 'A'), T(r"Plan B costs less than Plan A when $m<12$.", 'B'),
    T(r"Plan A costs less than Plan B when $m>12$.", 'C')],
   None,
   "Interpret the intersection point",
   r"The lines meet at $m=12$. Plan A starts lower (\$40 vs \$100) but grows faster (\$12 vs \$7 per month), so it is cheaper before $m=12$ and costs more after it. Only the first statement is true.",
   order='free',
   each=lambda v: {
       'A': all(40 + 12*mm > 100 + 7*mm for mm in range(0, 41)),
       'B': all(100 + 7*mm < 40 + 12*mm for mm in range(0, 12)),
       'C': all(40 + 12*mm < 100 + 7*mm for mm in range(13, 41)),
       'D': all(40 + 12*mm > 100 + 7*mm for mm in range(13, 41))}[v])

mc(5, 'H',
   r"The graphs of $y=ax+3$ and $y=bx-5$, where $a$ and $b$ are constants, intersect at the point whose $x$-coordinate is 4. What is the value of $a-b$?",
   C(-2), [C(-8), C(2), C(8)],
   lambda: simplify(solve(4*a + 3 - (4*b - 5), a)[0] - b),
   "Solve for the combination",
   r"At $x=4$ the $y$-values agree: $4a+3=4b-5$, so $4a-4b=-8$ and $a-b=-2$. (Forgetting to divide by 4 gives $-8$; $b-a$ gives 2; $4(b-a)$ gives 8.)")

mc(5, 'H',
   r"Pipe A fills an empty tank in 6 hours and pipe B fills it in 9 hours. Drain C empties a full tank in 18 hours. With all three open, how many hours does it take to fill the empty tank?",
   C("4.5", Rational(9, 2)), [C("3.6", Rational(18, 5)), C("7.5", Rational(15, 2)), C(18)],
   lambda: 1/(Rational(1, 6) + Rational(1, 9) - Rational(1, 18)),
   "Rates add (work-rate equation)",
   r"Rates per hour: $\frac16+\frac19-\frac1{18}=\frac{3+2-1}{18}=\frac29$ of the tank. Time $=\frac92=4.5$ hours. (3.6 ignores the drain; 7.5 averages 6 and 9.)")

mc(5, 'H',
   r"Line $m$ is perpendicular to the line $4x-3y=12$ and has the same $y$-intercept as the line $2x+5y=20$. Which is an equation of line $m$?",
   E(r"3x+4y=16", 3, 4, 16),
   [E(r"3x-4y=-16", 3, -4, -16), E(r"4x+3y=12", 4, 3, 12), E(r"3x+4y=-16", 3, 4, -16)],
   None,
   "Perpendicular + intercept",
   r"$4x-3y=12$ has slope $\frac43$, so $m$ has slope $-\frac34$. The line $2x+5y=20$ crosses the $y$-axis at $(0,4)$, so $y=-\frac34x+4$, i.e. $3x+4y=16$. ($3x+4y=-16$ uses $-4$, the $y$-intercept of the first line; $3x-4y=-16$ has slope $+\frac34$; $4x+3y=12$ has slope $-\frac43$.)",
   order='free',
   each=lambda v: Rational(-v[0], v[1]) == Rational(-3, 4) and Rational(v[2], v[1]) == 4)

mc(5, 'H',
   r"The equation $|3x-a|=12$ has two solutions whose sum is 10, where $a$ is a constant. What is the value of $a$?",
   C(15), [C(5), C(10), C(30)],
   lambda: [av for av in range(-60, 61) if Rational(av + 12, 3) + Rational(av - 12, 3) == 10],
   "Absolute value: two cases",
   r"$3x-a=\pm12$ gives $x=\frac{a+12}3$ and $x=\frac{a-12}3$. Their sum is $\frac{2a}3=10$, so $a=15$. (Forgetting to divide by 3 gives 5.)")

gi(5, 'H',
   r"How many integers $x$ satisfy $-7<\dfrac{5-2x}{3}\le5$?",
   "18", Integer(18),
   lambda: Integer(len([v for v in range(-80, 81) if -7 < Rational(5 - 2*v, 3) <= 5])),
   "Compound inequality: flip when dividing by a negative",
   r"Multiply by 3: $-21<5-2x\le15$. Subtract 5: $-26<-2x\le10$. Divide by $-2$ and reverse: $-5\le x<13$. The integers $-5,\dots,12$ number $18$.")

mc(5, 'H',
   r"Class A has 24 students with a mean score of 78. Class B has 36 students. The mean score of all 60 students is 84. What is the mean score of Class B?",
   C(88), [C(84), C(90), C(93)],
   lambda: solve(24*78 + 36*t - 60*84, t)[0],
   "Weighted average: use totals",
   r"Total points: $60(84)=5040$. Class A: $24(78)=1872$. Class B: $5040-1872=3168$, so its mean is $\frac{3168}{36}=88$. (90 averages 78 and 90 equally; 93 swaps the class sizes.)")

mc(5, 'H',
   r"For which values of $m$ do the graphs of $y=mx+3$ and $y=-x+9$ intersect in Quadrant I?",
   T(r"$m>-\frac13$", 'b'), [T(r"$m>-1$", 'a'), T(r"$m>0$", 'c'), T(r"$m<-1$", 'd')],
   None,
   "Solve for the intersection, then apply the signs",
   r"$mx+3=-x+9$ gives $x=\frac6{m+1}$ and $y=9-x$. $x>0$ needs $m>-1$; $y>0$ needs $x<9$, so $\frac6{m+1}<9$ and $m>-\frac13$. Both hold exactly when $m>-\frac13$. ($m>-1$ checks only $x>0$; $m>0$ is too strict; $m<-1$ makes $x$ negative.)",
   order='free',
   each=lambda v: all(
       {'a': mm > -1, 'b': mm > Rational(-1, 3), 'c': mm > 0, 'd': mm < -1}[v] ==
       (mm != -1 and Rational(6)/(mm + 1) > 0 and 9 - Rational(6)/(mm + 1) > 0)
       for mm in [Rational(i, 12) for i in range(-60, 61)]))

mc(5, 'H',
   r"If $\dfrac{2x+y}{x-3y}=\dfrac52$ and $y\ne0$, what is the value of $\dfrac xy$?",
   C(17), [C(-17), C(-13), C(r"\dfrac1{17}", Rational(1, 17))],
   lambda: simplify(solve(2*(2*x + y) - 5*(x - 3*y), x)[0] / y),
   "Cross-multiply, then compare coefficients",
   r"$2(2x+y)=5(x-3y)$ gives $4x+2y=5x-15y$, so $x=17y$ and $\frac xy=17$. (1/17 is $\frac yx$; $-13$ and $-17$ come from sign slips when moving terms.)")

gi(5, 'H',
   r"The table gives two points on a line in the $xy$-plane. $$\begin{array}{c|cc}x&p&p+4\\\hline y&2p+1&2p+17\end{array}$$ The $y$-intercept of the line is $(0,-7)$. What is the value of $p$?",
   "4", Integer(4),
   lambda: (lambda sl: solve(2*p + 1 - (sl*p - 7), p)[0])(Rational((2*p + 17 - (2*p + 1)).subs(p, 0), 4)),
   "Slope from a table with parameters",
   r"Slope $=\frac{(2p+17)-(2p+1)}{4}=4$, so $y=4x-7$. The first point gives $2p+1=4p-7$, so $p=4$. (Check: $4(8)-7=25=2(4)+17$.)")

# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(sympify(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
    except Exception:
        return None

def arrange_all():
    """Choose the print order of every MC problem; balance the correct letter globally and per set."""
    glob = [0, 0, 0, 0]
    perset = {}
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
            pa = [i for i, it in enumerate(asc) if it is p_['right']][0]
            if order == 'a':
                pos, out = pa, asc
            elif order == 'd':
                pos, out = 3 - pa, asc[::-1]
            else:
                cand = [(glob[pa], ps[pa], 0, pa), (glob[3 - pa], ps[3 - pa], 1, 3 - pa)]
                best = min(cand)
                pos = best[3]
                out = asc if best[2] == 0 else asc[::-1]
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
