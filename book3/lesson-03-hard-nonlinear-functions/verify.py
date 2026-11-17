#!/usr/bin/env python3
"""Book 3, Lesson 3 "Hard nonlinear functions": the problem bank AND its verifier.

Every problem is registered with its stem and choices (LaTeX), a worked solution that uses
the SHORTCUT (what students see), and a `calc` function that recomputes the answer the LONG
way (solve / expand / scan with sympy), independent of the shortcut and of the letter shown.

Running `python3 verify.py` recomputes every answer, checks that exactly one choice is correct
(and that all choices are distinct), balances the correct letters, and prints OK / FAIL per item.
`build.py` imports PROBLEMS from this file to write problems.md and lesson03-typeset.tex.
"""
import sys
import random
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, expand, factor, Poly,
                   diff, Eq, S, log, N as numeric, Abs, oo, sympify, roots, interpolate, limit, Float)

x, y, a, b, c, k, h, p, q, r, s = symbols('x y a b c k h p q r s', real=True)
t = Symbol('t', real=True)
w = Symbol('w', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: read the function before you compute", "Medium and Hard"),
    2: ("Set 2", "Quadratic models, symmetry and equivalent forms", "Hard"),
    3: ("Set 3", "Exponential models: factors, rates and two-point rebuilds", "Hard"),
    4: ("Set 4", "Composition, transformations, polynomials and piecewise rules", "Hard"),
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
    d = sympify(u) - sympify(v)
    fs = d.free_symbols
    if not fs:
        return abs(complex(numeric(d, 30))) < 1e-9
    pts = [Rational(37, 100), Rational(191, 100), Rational(263, 100), Rational(-141, 100)]
    for pv in pts:
        if abs(complex(numeric(d.subs({s_: pv for s_ in fs}), 30))) > 1e-9:
            return False
    return True

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='sort', **kw):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, **kw))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol, **kw):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol, **kw))

def vertex(expr):
    """(h, k) of a parabola by calculus."""
    hh = solve(diff(expr, x), x)[0]
    return hh, simplify(expr.subs(x, hh))

def vtx_str(expr):
    hh, kk = vertex(expr)
    return "(%s,%s)" % (hh, kk)

def fit_quadratic(points):
    return expand(interpolate(points, x))


def must_be_true_26():
    """S2.6: opens downward (a<0), f(-2)=f(6), f(0)=c>0.  Which of I: b>0, II: c>b hold in every sample?"""
    rows = []
    for av in (-3, -1, Rational(-1, 2)):
        bv = solve(Eq(av*4 - 2*b, av*36 + 6*b), b)[0]          # f(-2)=f(6)
        for cv in (Rational(1, 100), 1, 5, 100):               # any c>0
            rows.append((bv > 0, cv > bv))
    keep = [name for name, i in (("I", 0), ("II", 1)) if all(r_[i] for r_ in rows)]
    if not keep:
        return "Neither I nor II"
    return "%s only" % keep[0] if len(keep) == 1 else "I and II"

def must_be_true_51():
    """S5.1: a>0, vertex (h,k) with k<0, f(-5)=f(1).  Which of I: b>0, II: c<0, III: two real zeros hold always?"""
    rows = []
    for av in (Rational(1, 3), 1, 5):
        for kv in (-1, -9):
            hv = Rational(-5 + 1, 2)                              # axis from symmetry
            f = expand(av*(x - hv)**2 + kv)
            bv, cv = f.coeff(x, 1), f.coeff(x, 0)
            rows.append((bv > 0, cv < 0, len(solve(f, x)) == 2))
    keep = [n for n, i in (("I", 0), ("II", 1), ("III", 2)) if all(r_[i] for r_ in rows)]
    return {"I": "I only", "I,III": "I and III only", "II,III": "II and III only", "I,II,III": "I, II and III"}.get(",".join(keep), "other")

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"The function $g$ is defined by $g(x)=-2(x+4)^2+9$. What is the maximum value of $g$?",
   C(9), [C(-4), C(-2), C(4)],
   lambda: vertex(-2*(x + 4)**2 + 9)[1],
   "Vertex form reads h and k",
   r"In $a(x-h)^2+k$ with $a<0$ the maximum value is $k=9$ (it happens at $x=-4$). The traps: $-4$ is where the maximum happens, $4$ is the sign slip on $h$, and $-2$ is just $a$.")

mc(1, 'M',
   r"The value $V$, in dollars, of a car $t$ years after it was bought is modeled by $V(t)=24{,}000(0.85)^t$. Which is the best interpretation of the number $0.85$ in this model?",
   T(r"The car's value drops by $15\%$ each year."),
   [T(r"The car's value drops by $85\%$ each year."), T(r"The car's value drops by $0.85\%$ each year."), T(r"The car's value drops by \$0.85 each year.")],
   lambda: r"The car's value drops by $%d\%%$ each year." % round(100 * (1 - Rational(85, 100))),
   "Growth factor = 1 ± rate",
   r"Each year the value is multiplied by $0.85=1-0.15$, so it drops by $15\%$. (Choice $85\%$ confuses the factor with the rate; $0.85\%$ forgets to convert a decimal to a percent.)", order='free')

gi(1, 'M',
   r"The functions $f$ and $g$ are defined by $f(x)=x^2-4x-5$ and $g(x)=2x+1$. What is the value of $f(g(1))$?",
   "-8", Integer(-8),
   lambda: (lambda f, g: f(g(1)))(lambda u: u**2 - 4*u - 5, lambda u: 2*u + 1),
   "Compose inside-out",
   r"Inside first: $g(1)=3$. Then $f(3)=9-12-5=-8$. (Doing $g(f(1))$ instead gives $-15$.)")

mc(1, 'M',
   r"The polynomial $p(x)=(x-3)^2(x+1)(x-6)$ is graphed in the $xy$-plane. How many distinct $x$-intercepts does the graph have?",
   C(3), [C(1), C(2), C(4)],
   lambda: Integer(len(set(solve((x - 3)**2*(x + 1)*(x - 6), x)))),
   "Zeros and multiplicity",
   r"The zeros are $3$ (double), $-1$ and $6$. Distinct intercepts: $3$. (Choice 4 counts the double root twice; choice 2 counts only the places where the graph crosses.)")

mc(1, 'M',
   r"The graph of $g$ is the graph of $f(x)=x^2$ shifted $3$ units to the left and $2$ units down. Which equation defines $g$?",
   C(r"g(x)=(x+3)^2-2", (x + 3)**2 - 2),
   [C(r"g(x)=(x-3)^2-2", (x - 3)**2 - 2), C(r"g(x)=(x+3)^2+2", (x + 3)**2 + 2), C(r"g(x)=(x-3)^2+2", (x - 3)**2 + 2)],
   lambda: (lambda f: f(x + 3) - 2)(lambda u: u**2),
   "Shift rules (x → x − h)",
   r"Left $3$ means $f(x+3)$ (inside, opposite sign); down $2$ means $-2$ outside. So $g(x)=(x+3)^2-2$.", order='free')

gi(1, 'H',
   r"A bakery's daily profit, in dollars, from selling $x$ trays is $P(x)=-2x^2+60x-200$. What is the greatest possible daily profit, in dollars?",
   "250", Integer(250),
   lambda: vertex(-2*x**2 + 60*x - 200)[1],
   "Vertex = max/min",
   r"The axis is $x=-\dfrac{60}{2(-2)}=15$. Then $P(15)=-450+900-200=250$.")

mc(1, 'H',
   r"The function $f$ is defined by $f(x)=a(x-1)(x-5)$, where $a$ is a constant. The graph of $y=f(x)$ passes through $(0,-15)$. What is the maximum value of $f$?",
   C(12), [C(-15), C(-12), C(3)],
   lambda: (lambda av: vertex(av*(x - 1)*(x - 5))[1])(solve(a*(0 - 1)*(0 - 5) + 15, a)[0]),
   "Axis = midpoint of the zeros",
   r"$f(0)=5a=-15$, so $a=-3$. The axis is $x=\frac{1+5}2=3$ and $f(3)=-3(2)(-2)=12$. (Traps: $-15$ is $f(0)$, $3$ is where the maximum happens, $-12$ is a sign slip.)")

mc(1, 'H',
   r"The amount $A$, in milligrams, of a medicine in a patient's blood $t$ hours after a dose is modeled by $A(t)=400\left(\dfrac12\right)^{t/6}$. Which statement is true?",
   T(r"The amount is cut in half every $6$ hours."),
   [T(r"The amount drops by $6$ milligrams every hour."), T(r"The amount is cut in half every hour."), T(r"The initial amount is $200$ milligrams.")],
   lambda: r"The amount is cut in half every $%d$ hours." % solve(Eq(Rational(1, 2)**(x/6), Rational(1, 2)), x)[0],
   "Per-period exponent",
   r"$\left(\frac12\right)^{t/6}$ multiplies by $\frac12$ each time $t$ grows by $6$: a half-life of $6$ hours. The initial amount is $A(0)=400$.", order='free')

mc(1, 'H',
   r"The function $f$ is defined by $f(x)=2x^2-12x+c$, where $c$ is a constant. The minimum value of $f$ is $3$. What is the value of $c$?",
   C(21), [C(3), C(12), C(18)],
   lambda: solve(Eq(vertex(2*x**2 - 12*x + c)[1], 3), c)[0],
   "Vertex = max/min",
   r"The axis is $x=3$, so the minimum is $f(3)=18-36+c=c-18=3$ and $c=21$. (Traps: $12$ forgets the factor $2$, $18$ is just the constant part, $3$ is the minimum itself.)")

mc(1, 'H',
   r"What is the sum of all values of $x$ that satisfy $|x-4|-3=2$?",
   C(8), [C(4), C(5), C(10)],
   lambda: sum(solve(Abs(x - 4) - 3 - 2, x)),
   "Absolute value: two cases",
   r"$|x-4|=5$, so $x=9$ or $x=-1$, and the sum is $8$. (Traps: $5$ is only $|x-4|$, $10$ is the difference of the solutions, $4$ is the center.)")

mc(1, 'H',
   r"The functions $f$ and $g$ are defined by $f(x)=2x+3$ and $g(x)=x^2-1$. Which expression is equivalent to $g(f(x))$?",
   C(r"4x^2+12x+8", 4*x**2 + 12*x + 8),
   [C(r"2x^2+1", 2*x**2 + 1), C(r"4x^2+8", 4*x**2 + 8), C(r"4x^2+12x+9", 4*x**2 + 12*x + 9)],
   lambda: expand((2*x + 3)**2 - 1),
   "Compose inside-out",
   r"Put $f(x)$ inside $g$: $(2x+3)^2-1=4x^2+12x+9-1$. (Traps: $2x^2+1$ is $f(g(x))$; $4x^2+8$ squares the terms one by one; $4x^2+12x+9$ forgets the $-1$.)", order='free')

gi(1, 'H',
   r"The polynomial $p$ is defined by $p(x)=a(x+2)(x-1)(x-4)$, where $a$ is a constant. The graph of $y=p(x)$ passes through $(0,16)$. What is the value of $p(3)$?",
   "-20", Integer(-20),
   lambda: (lambda av: (av*(x + 2)*(x - 1)*(x - 4)).subs(x, 3))(solve(a*2*(-1)*(-4) - 16, a)[0]),
   "Zeros and multiplicity",
   r"$p(0)=a(2)(-1)(-4)=8a=16$, so $a=2$. Then $p(3)=2(5)(2)(-1)=-20$.")

# ============================================================ SET 2  (Hard, 14)  quadratic models, symmetry, forms
mc(2, 'H',
   r"The height, in feet, of a ball $t$ seconds after it is thrown is modeled by $h(t)=-4t^2+24t+10$. Which of the following is the best interpretation of the point $(3,46)$ on the graph of $y=h(t)$?",
   T(r"The ball reaches its greatest height, $46$ feet, $3$ seconds after it is thrown."),
   [T(r"The ball reaches its greatest height, $3$ feet, $46$ seconds after it is thrown."),
    T(r"The ball is $46$ feet above the ground when it lands, $3$ seconds after it is thrown."),
    T(r"The ball is thrown from a height of $46$ feet and is rising at $3$ feet per second.")],
   lambda: (lambda hh, kk: r"The ball reaches its greatest height, $%d$ feet, $%d$ seconds after it is thrown." % (kk, hh))(*[v for v in vertex(-4*x**2 + 24*x + 10)]),
   "Interpret the model",
   r"The axis is $t=-\frac{24}{2(-4)}=3$ and $h(3)=-36+72+10=46$, so $(3,46)$ is the vertex: the maximum height is $46$ ft at $t=3$. (The other choices swap the coordinates, call the vertex the landing point, or call $46$ the starting height; the starting height is $h(0)=10$.)", order='free')

gi(2, 'H',
   r"A theater sells $300-12p$ tickets per show when the ticket price is $p$ dollars, where $p$ can be any amount from $0$ to $25$. The revenue is the price times the number of tickets sold. What is the greatest possible revenue per show, in dollars?",
   "1875", Integer(1875),
   lambda: max((300 - 12*Rational(n, 4))*Rational(n, 4) for n in range(0, 101)),
   "Optimize: vertex of the product",
   r"$R(p)=p(300-12p)$ has zeros $p=0$ and $p=25$, so its maximum is halfway at $p=12.5$: $R=12.5(300-150)=12.5\cdot150=1875$.")

mc(2, 'H',
   r"A farmer has $80$ meters of fencing for three sides of a rectangular pen; the fourth side is a barn wall that needs no fence. The two sides perpendicular to the barn each have length $w$ meters. What is the greatest possible area, in square meters, of the pen?",
   C(800), [C(20), C(400), C(1600)],
   lambda: max(n*(80 - 2*n) for n in range(0, 41)),
   "Optimize: vertex of the product",
   r"The side along the wall is $80-2w$, so $A=w(80-2w)$ with zeros $0$ and $40$. The maximum is at $w=20$: $A=20\cdot40=800$. (Traps: $20$ is $w$; $400$ treats the pen as a square with 4 fenced sides; $1600$ is $40^2$.)")

mc(2, 'H',
   r"Which of the following is equivalent to $f(x)=3x^2+18x+20$ and shows the minimum value of $f$ as a constant?",
   C(r"3(x+3)^2-7", 3*(x + 3)**2 - 7),
   [C(r"3(x+3)^2+11", 3*(x + 3)**2 + 11), C(r"3(x-3)^2-7", 3*(x - 3)**2 - 7), C(r"3(x+3)^2+20", 3*(x + 3)**2 + 20)],
   lambda: expand(3*x**2 + 18*x + 20),
   "Complete the square",
   r"$3(x^2+6x)+20=3\big[(x+3)^2-9\big]+20=3(x+3)^2-27+20=3(x+3)^2-7$. (Forgetting to multiply the $9$ by $3$ gives $+11$; skipping the correction gives $+20$.)", order='free')

gi(2, 'H',
   r"The function $g(x)=ax^2+bx+c$ has a minimum value of $-18$, and $g(1)=g(7)$. The graph of $y=g(x)$ passes through $(0,14)$. What is the value of $g(-1)$?",
   "32", Integer(32),
   lambda: (lambda sol: (sol[a]*x**2 + sol[b]*x + sol[c]).subs(x, -1))(solve([a + b + c - (49*a + 7*b + c), a*16 + 4*b + c + 18, c - 14], [a, b, c])),
   "Symmetry about the axis",
   r"$g(1)=g(7)$ puts the axis at $x=4$, so $g(x)=a(x-4)^2-18$. Then $g(0)=16a-18=14$ gives $a=2$, and $g(-1)=2(25)-18=32$.")

mc(2, 'H',
   r"The function $f(x)=ax^2+bx+c$ has constants $a$, $b$ and $c$. The graph of $y=f(x)$ opens downward, $f(-2)=f(6)$, and $f(0)>0$. Which of the following must be true?"
   "\n" r"I. $b>0$" "\n" r"II. $c>b$",
   T(r"I only"), [T(r"II only"), T(r"I and II"), T(r"Neither I nor II")],
   lambda: must_be_true_26(),
   "Symmetry about the axis",
   r"$f(-2)=f(6)$ puts the axis at $x=2$, so $-\frac b{2a}=2$ and $b=-4a$. With $a<0$ that gives $b>0$: I is true. Only $c=f(0)>0$ is known, so $c>b$ can fail (take $a=-3$, $b=12$, $c=1$): II is not forced.", order=0)

mc(2, 'H',
   r"The table shows values of the quadratic function $f$, whose graph opens upward. [[TABLE]] What is the minimum value of $f$?",
   C(-3), [C(-1), C(-2), C(2)],
   lambda: (lambda f: vertex(f)[1])(fit_quadratic([(0, 5), (1, -1), (3, -1)])),
   "Symmetry about the axis",
   r"$f(1)=f(3)$, so the axis is $x=2$. With $f(x)=a(x-2)^2+k$: $f(1)=a+k=-1$ and $f(0)=4a+k=5$, so $a=2$, $k=-3$. The minimum is $-3$. (The table's $-1$ is not the lowest point; $2$ is where the minimum happens.)",
   table=[[r"$x$", "0", "1", "3"], [r"$f(x)$", "5", r"$-1$", r"$-1$"]])

mc(2, 'H',
   r"A company's monthly profit, in thousands of dollars, from producing $x$ thousand units is $P(x)=-0.5x^2+40x-350$. What is the greatest number of thousands of units that the company can produce and still make a profit of at least $0$?",
   C(70), [C(10), C(40), C(80)],
   lambda: max(solve(-Rational(1, 2)*x**2 + 40*x - 350, x)),
   "Axis = midpoint of the zeros",
   r"Solve $-0.5x^2+40x-350=0$: $x^2-80x+700=0$, so $x=10$ or $x=70$. Profit is $\ge0$ for $10\le x\le70$, so the largest output is $70$. (Traps: $10$ is the smaller zero, $40$ the vertex, $80$ the sum of the zeros.)")

mc(2, 'H',
   r"The function $f$ is defined by $f(x)=-(x-4)^2+9$. For how many integer values of $x$ is $f(x)>0$?",
   C(5), [C(3), C(7), C(9)],
   lambda: Integer(len([n for n in range(-40, 40) if -(n - 4)**2 + 9 > 0])),
   "Vertex form reads h and k",
   r"$f(x)>0$ means $(x-4)^2<9$, so $1<x<7$: the integers $2,3,4,5,6$ give $5$. (Counting $\ge0$ gives $7$; $3$ is the half-width; $9$ is $k$.)")

mc(2, 'H',
   r"A parabola has its vertex at $(-2,5)$ and passes through $(0,13)$. Which equation defines the parabola?",
   C(r"y=2(x+2)^2+5", 2*(x + 2)**2 + 5),
   [C(r"y=2(x-2)^2+5", 2*(x - 2)**2 + 5), C(r"y=(x+2)^2+9", (x + 2)**2 + 9), C(r"y=2(x+2)^2+13", 2*(x + 2)**2 + 13)],
   lambda: (lambda av: av*(x + 2)**2 + 5)(solve(a*(0 + 2)**2 + 5 - 13, a)[0]),
   "Vertex form reads h and k",
   r"$y=a(x+2)^2+5$ and $y(0)=4a+5=13$ give $a=2$. (Check the vertex, not only the point: $2(x-2)^2+5$ also passes through $(0,13)$ but has vertex $(2,5)$; $(x+2)^2+9$ has vertex $(-2,9)$.)", order='free')

gi(2, 'H',
   r"A ball is thrown upward from a height of $2$ meters. Its height after $t$ seconds is $h(t)=-5t^2+bt+2$ meters, where $b$ is a positive constant. The ball's maximum height is $22$ meters. What is the value of $b$?",
   "20", Integer(20),
   lambda: [v for v in solve(Eq(vertex(-5*x**2 + b*x + 2)[1], 22), b) if v > 0][0],
   "Vertex = max/min",
   r"The vertex is at $t=\frac b{10}$, so the maximum is $2+\frac{b^2}{20}=22$. Then $b^2=400$ and $b=20$ (positive).")

mc(2, 'H',
   r"The function $f$ is defined by $f(x)=x^2-6x+k$, where $k$ is a constant. The graph of $y=f(x)$ does not intersect the line $y=-2$. Which of the following could be the value of $k$?",
   C(10), [C(4), C(6), C(7)],
   lambda: [kv for kv in (4, 6, 7, 10) if vertex(x**2 - 6*x + kv)[1] > -2][0],
   "Vertex = max/min",
   r"The minimum of $f$ is $f(3)=k-9$. The graph stays above $y=-2$ only if $k-9>-2$, i.e. $k>7$. Only $10$ works. ($k=7$ makes the vertex touch the line.)")

mc(2, 'H',
   r"For which values of $x$ is $-3x^2+12x-9>0$?",
   T(r"$1<x<3$"), [T(r"$x<1$ or $x>3$"), T(r"$-3<x<-1$"), T(r"$x<-3$ or $x>-1$")],
   lambda: (lambda zs, f: "$%d<x<%d$" % (zs[0], zs[1]) if f((zs[0] + zs[1])/2) > 0 else "outside")(sorted(solve(-3*x**2 + 12*x - 9, x)), lambda v: -3*v**2 + 12*v - 9),
   "Factor and sketch",
   r"$-3(x-1)(x-3)>0$. The parabola opens downward, so it is above the axis between the zeros: $1<x<3$. (The outside-the-zeros choice is for an upward parabola.)", order='free')

gi(2, 'H',
   r"A parabola passes through $(0,6)$, $(2,6)$ and $(5,-9)$ and opens downward. What is the maximum value of the function?",
   "7", Integer(7),
   lambda: vertex(fit_quadratic([(0, 6), (2, 6), (5, -9)]))[1],
   "Symmetry about the axis",
   r"Equal outputs at $x=0$ and $x=2$ put the axis at $x=1$. Write $y=a(x-1)^2+k$: $a+k=6$ and $16a+k=-9$, so $a=-1$ and $k=7$.")

# ============================================================ SET 3  (Hard, 14)  exponential models
mc(3, 'H',
   r"The population of a town $t$ years after 2020 is modeled by $P(t)=1200(1.2)^t$. By approximately what percent does the population grow each month?",
   C(r"1.5\%", 1.5), [C(r"1.7\%", 1.7), C(r"20\%", 20), C(r"240\%", 240)],
   lambda: round(float((Rational(12, 10)**Rational(1, 12) - 1)*100), 1),
   "Unit change: t = m/12",
   r"Each month multiplies by $1.2^{1/12}\approx1.0153$, about $1.5\%$ growth. (Dividing $20\%$ by $12$ gives the trap $1.7\%$; $20\%$ is the yearly rate; $240\%$ multiplies by $12$.)")

mc(3, 'H',
   r"A culture of bacteria doubles every $5$ hours. By approximately what factor does the culture grow in $12$ hours?",
   C(5.3), [C(2.4), C(4.0), C(24.0)],
   lambda: round(float(2**Rational(12, 5)), 1),
   "Per-period exponent",
   r"In $12$ hours there are $\frac{12}5=2.4$ doubling periods, so the factor is $2^{2.4}\approx5.3$. (Traps: $2.4$ is the number of periods; $4.0$ rounds the periods down to $2$; $24$ is $12\cdot2$.)")

gi(3, 'H',
   r"A population grows exponentially. It was $3000$ at time $t=2$ hours and $12{,}000$ at time $t=6$ hours. What was the population at time $t=0$?",
   "1500", Integer(1500),
   lambda: (lambda sol: sol[0][a])([d for d in solve([a*b**2 - 3000, a*b**6 - 12000], [a, b], dict=True) if d[b] > 0]),
   "Two points: divide to get b",
   r"From $t=2$ to $t=6$ the population is multiplied by $4$ in $4$ hours, so $b^4=4$ and $b^2=2$. Going back from $t=2$ to $t=0$ divides by $b^2=2$: $3000\div2=1500$.")

mc(3, 'H',
   r"The table shows two values of the exponential function $f(x)=ab^x$, where $a$ and $b$ are positive constants. [[TABLE]] Which equation defines $f$?",
   C(r"f(x)=2(3)^x", 2*3**x), [C(r"f(x)=2(27)^x", 2*27**x), C(r"f(x)=18(3)^x", 18*3**x), C(r"f(x)=6(3)^x", 6*3**x)],
   lambda: (lambda d: d[a]*d[b]**x)([d for d in solve([a*b**2 - 18, a*b**5 - 486], [a, b], dict=True) if d[b] > 0][0]),
   "Two points: divide to get b",
   r"Divide: $\frac{ab^5}{ab^2}=b^3=\frac{486}{18}=27$, so $b=3$. Then $a\cdot3^2=18$ gives $a=2$. (Choice 27 is $b^3$, not $b$; $18$ is $f(2)$, not $f(0)$; $6$ divides by $b$ only once.)",
   table=[[r"$x$", "2", "5"], [r"$f(x)$", "18", "486"]], order='free')

mc(3, 'H',
   r"The number of bacteria $N$ in a culture $t$ years after it was started is modeled by $N(t)=250(1.5)^{t/3}$. Which statement is true?",
   T(r"The number of bacteria increases by $50\%$ every $3$ years."),
   [T(r"The number of bacteria increases by $50\%$ every year."), T(r"The number of bacteria increases by $150\%$ every $3$ years."),
    T(r"The number of bacteria increases by exactly $\frac{50}{3}\%$ every year.")],
   lambda: r"The number of bacteria increases by $%d\%%$ every $%d$ years." % (round((Rational(3, 2) - 1)*100), 3),
   "Per-period exponent",
   r"The exponent $\frac t3$ counts blocks of $3$ years; each block multiplies by $1.5$, i.e. a $50\%$ increase. (The yearly factor is $1.5^{1/3}\approx1.145$, not $1+\frac{0.5}3$.)", order='free')

mc(3, 'H',
   r"The function $f$ is defined by $f(x)=50-6(2)^x$. For how many positive integer values of $x$ is $f(x)>0$?",
   C(3), [C(2), C(4), C(8)],
   lambda: Integer(len([n for n in range(1, 60) if 50 - 6*2**n > 0])),
   "Graph it (Desmos)",
   r"$f(x)>0$ means $2^x<\frac{50}6\approx8.33$, so $x\le3$ (since $2^3=8$). The positive integers $1,2,3$ give $3$. (Counting $x=0$ gives $4$; using $2^x<8$ strictly gives $2$; $8$ is a value of $2^x$.)")

gi(3, 'H',
   r"An account earns interest so that its balance after $t$ years is $P(1.05)^t$ dollars, where $P$ is the amount first deposited. What is the least whole number of years after which the balance is more than double the amount first deposited?",
   "15", Integer(15),
   lambda: [n for n in range(1, 100) if Rational(105, 100)**n > 2][0],
   "Graph it (Desmos)",
   r"Solve $1.05^t>2$: graph $y=1.05^t$ and $y=2$; they cross near $t\approx14.2$. Since $1.05^{14}\approx1.98<2$ and $1.05^{15}\approx2.08$, the answer is $15$.")

mc(3, 'H',
   r"The function $f$ is defined by $f(x)=40(0.5)^x$, and $g(x)=f(x-3)$. Which of the following is equivalent to $g(x)$ and shows the value of $g(0)$ as the coefficient?",
   C(r"320(0.5)^x", 320*Rational(1, 2)**x),
   [C(r"5(0.5)^x", 5*Rational(1, 2)**x), C(r"40(0.5)^x-3", 40*Rational(1, 2)**x - 3), C(r"40(0.125)^x", 40*Rational(125, 1000)**x)],
   lambda: 40*Rational(1, 2)**(x - 3),
   "Shift rules (x → x − h)",
   r"$g(x)=40(0.5)^{x-3}=40(0.5)^{-3}(0.5)^x=40\cdot8\,(0.5)^x=320(0.5)^x$. (Using $0.5^{+3}$ gives $5$; $-3$ outside is a vertical shift; $0.125$ is $0.5^3$, a changed base.)", order='free')

mc(3, 'H',
   r"A town had $8000$ residents in $2020$ and $12{,}500$ residents in $2024$. Assuming exponential growth, about how many residents will the town have in $2026$?",
   C(r"15{,}625", 15625), [C(r"14{,}750", 14750), C(r"19{,}531", 19531), C(r"30{,}518", 30518)],
   lambda: 8000*(Rational(12500, 8000))**Rational(6, 4),
   "Two points: divide to get b",
   r"Over $4$ years the factor is $\frac{12500}{8000}=\frac{25}{16}$, so $b^4=\frac{25}{16}$ and $b^2=\frac54$. In $6$ years (three blocks of $2$): $8000\left(\frac54\right)^3=15{,}625$. (Traps: $14{,}750$ is linear growth; $19{,}531$ applies the 4-year factor again; $30{,}518$ uses $25\%$ per year.)")

mc(3, 'H',
   r"Which of the following is equivalent to $5000\cdot2^{t/3}$?",
   C(r"5000\left(\sqrt[3]{2}\right)^t", 5000*(2**Rational(1, 3))**t),
   [C(r"5000\cdot8^t", 5000*8**t), C(r"5000\left(\dfrac23\right)^t", 5000*Rational(2, 3)**t), C(r"5000\cdot6^t", 5000*6**t)],
   lambda: 5000*2**(t/3),
   "Per-period exponent",
   r"$2^{t/3}=\left(2^{1/3}\right)^t$: the base becomes the cube root of $2$. (Traps: $8=2^3$, $\frac23$ and $6$ come from mishandling the exponent $\frac t3$.)", order='free')

gi(3, 'H',
   r"A radioactive sample has a half-life of $8$ days. After $20$ days, the mass left is what percent of the original mass? Round to the nearest whole percent and enter only the number.",
   "18", Integer(18),
   lambda: round(float(100*Rational(1, 2)**Rational(20, 8))),
   "Per-period exponent",
   r"There are $\frac{20}8=2.5$ half-life periods, so the fraction left is $\left(\frac12\right)^{2.5}\approx0.1768$, i.e. about $18\%$.")

mc(3, 'H',
   r"The graph of $g(x)=3(2)^x-12$ crosses the $x$-axis at $(p,0)$ and the $y$-axis at $(0,q)$. What is the value of $p-q$?",
   C(11), [C(-11), C(-7), C(9)],
   lambda: (lambda pv, qv: pv - qv)(solve(3*2**x - 12, x)[0], (3*2**x - 12).subs(x, 0)),
   "Intercepts: set x = 0 or y = 0",
   r"$3(2)^x=12$ gives $2^x=4$, so $p=2$. $q=g(0)=3-12=-9$. Then $p-q=2+9=11$. (Traps: $-7$ is $p+q$, $-11$ is $q-p$, $9$ is $|q|$.)")

mc(3, 'H',
   r"A cup of coffee cools so that its temperature, in degrees Celsius, $t$ minutes after it is poured is $T(t)=a\left(\dfrac12\right)^{t}+20$, where $a$ is a constant. The coffee was $100^\circ$ when it was poured. What is the temperature after $3$ minutes?",
   C(30), [C(12.5), C(32.5), C(60)],
   lambda: (lambda av: av*Rational(1, 2)**3 + 20)(solve(a + 20 - 100, a)[0]),
   "Intercepts: set x = 0 or y = 0",
   r"$T(0)=a+20=100$, so $a=80$ (the room temperature $20$ is the floor, not part of $a$). Then $T(3)=80\cdot\frac18+20=30$. (Traps: $12.5=100\cdot\frac18$; $32.5$ uses $a=100$; $60$ halves only once.)")

gi(3, 'H',
   r"The graphs of $f(x)=5(2)^x$ and $g(x)=c\left(\dfrac12\right)^x$, where $c$ is a constant, intersect at the point where $x=2$. What is the value of $c$?",
   "80", Integer(80),
   lambda: solve(Eq(5*2**2, c*Rational(1, 2)**2), c)[0],
   "Substitute the point",
   r"At $x=2$: $5\cdot4=20$ and $c\left(\frac12\right)^2=\frac c4$. Setting $20=\frac c4$ gives $c=80$.")

# ============================================================ SET 4  (Hard, 14)  composition, transformations, polynomials, piecewise
gi(4, 'H',
   r"The functions $f$ and $g$ are defined by $f(x)=2x+3$ and $g(x)=x^2-4x$. What is the sum of all values of $x$ for which $f(g(x))=g(f(x))$?",
   "-6", Integer(-6),
   lambda: sum(solve((2*(x**2 - 4*x) + 3) - ((2*x + 3)**2 - 4*(2*x + 3)), x)),
   "Compose inside-out",
   r"$f(g(x))=2x^2-8x+3$ and $g(f(x))=(2x+3)^2-4(2x+3)=4x^2+4x-3$. Setting them equal: $2x^2+12x-6=0$, so the sum of the solutions is $-\frac{12}2=-6$.")

mc(4, 'H',
   r"The tables define the functions $f$ and $g$ on the values $1,2,3,4$. [[TABLE]] For how many of the values $x=1,2,3,4$ is $f(g(x))=g(f(x))$?",
   C(1), [C(0), C(2), C(4)],
   lambda: Integer(len([v for v in (1, 2, 3, 4) if {1: 3, 2: 1, 3: 4, 4: 2}[{1: 2, 2: 4, 3: 3, 4: 1}[v]] == {1: 2, 2: 4, 3: 3, 4: 1}[{1: 3, 2: 1, 3: 4, 4: 2}[v]]])),
   "Compose inside-out",
   r"Compute both orders. $x=1$: $f(g(1))=f(2)=1$, $g(f(1))=g(3)=3$. $x=2$: $f(g(2))=f(4)=2$, $g(f(2))=g(1)=2$ (equal). $x=3$: $f(3)=4$ but $g(4)=1$. $x=4$: $f(1)=3$ but $g(2)=4$. Only $x=2$ works. (Choice 4 assumes the order does not matter.)",
   table=[[r"$x$", "1", "2", "3", "4"], [r"$f(x)$", "3", "1", "4", "2"], [r"$g(x)$", "2", "4", "3", "1"]])

mc(4, 'H',
   r"The function $f$ is defined by $f(x)=x^2-4x+1$, and $g(x)=-2f(x+1)+5$. What are the coordinates of the vertex of the graph of $y=g(x)$?",
   T(r"$(1,11)$"), [T(r"$(3,11)$"), T(r"$(1,2)$"), T(r"$(1,1)$")],
   lambda: "$%s$" % vtx_str(-2*((x + 1)**2 - 4*(x + 1) + 1) + 5),
   "Shift rules (x → x − h)",
   r"$f$ has vertex $(2,-3)$. $f(x+1)$ moves it left $1$: $(1,-3)$. Multiplying by $-2$ gives $y=6$, and adding $5$ gives $11$: vertex $(1,11)$. (Traps: $(3,11)$ shifts right; $(1,2)$ forgets the $-2$; $(1,1)$ subtracts the $5$.)", order='free')

mc(4, 'H',
   r"The function $f$ has exactly two zeros, $-2$ and $5$. The function $g$ is defined by $g(x)=f(2x-4)$. What is the sum of the zeros of $g$?",
   C(5.5), [C(-2), C(3), C(11)],
   lambda: sum(solve(((2*x - 4) + 2)*((2*x - 4) - 5), x)),
   "Shift rules (x → x − h)",
   r"$g(x)=0$ when $2x-4=-2$ or $2x-4=5$, so $x=1$ or $x=4.5$ and the sum is $5.5$. (Plugging the zeros forward, $2(-2)-4$ and $2(5)-4$, gives the trap $-2$; ignoring the factor $2$ gives $11$; $3$ is the sum of the zeros of $f$.)")

gi(4, 'H',
   r"The function $f$ has a maximum value of $7$ at $x=3$. The function $g$ is defined by $g(x)=2-3f(x-5)$ and has an absolute minimum at the point $(h,k)$. What is the value of $h+k$?",
   "-11", Integer(-11),
   lambda: (lambda g: sum(vertex(g)))(2 - 3*(-((x - 5) - 3)**2 + 7)),
   "Shift rules (x → x − h)",
   r"$f(x-5)$ moves the maximum point to $(8,7)$. Multiplying by $-3$ turns it into a minimum at $y=-21$, and adding $2$ gives $y=-19$. So $(h,k)=(8,-19)$ and $h+k=-11$.")

mc(4, 'H',
   r"The function $p$ is defined by [[D:p(x)=-2(x-3)^2(x+1)(x+4):D]] Which statement about the graph of $y=p(x)$ is true?",
   T(r"It touches the $x$-axis at $x=3$, and $p(x)\to-\infty$ as $x\to\infty$ and as $x\to-\infty$.", "touch,-,-"),
   [T(r"It crosses the $x$-axis at $x=3$, and $p(x)\to-\infty$ as $x\to\infty$ and as $x\to-\infty$.", "cross,-,-"),
    T(r"It touches the $x$-axis at $x=3$, and $p(x)\to+\infty$ as $x\to\infty$ and as $x\to-\infty$.", "touch,+,+"),
    T(r"It touches the $x$-axis at $x=3$, $p(x)\to-\infty$ as $x\to\infty$, and $p(x)\to+\infty$ as $x\to-\infty$.", "touch,-,+")],
   lambda: (lambda P: "%s,%s,%s" % ("touch" if roots(P, x)[3] % 2 == 0 else "cross",
                                      "+" if Poly(P, x).LC() > 0 else "-",
                                      "+" if Poly(P, x).LC()*(-1)**Poly(P, x).degree() > 0 else "-"))(-2*(x - 3)**2*(x + 1)*(x + 4)),
   "Leading coefficient and ends",
   r"The factor $(x-3)^2$ has an even exponent, so the graph touches the axis at $3$ without crossing. The degree is $4$ (even) and the leading coefficient $-2$ is negative, so both ends point down.", order='free')

mc(4, 'H',
   r"The graph of the cubic function $p$ is shown. [[FIG]] The graph crosses the $x$-axis at $x=-3$, touches the $x$-axis at $x=1$, and passes through $(-1,-2)$. Which equation could define $p$?",
   C(r"p(x)=-\dfrac14(x+3)(x-1)^2", -Rational(1, 4)*(x + 3)*(x - 1)**2),
   [C(r"p(x)=\dfrac14(x+3)(x-1)^2", Rational(1, 4)*(x + 3)*(x - 1)**2),
    C(r"p(x)=-\dfrac14(x-3)(x+1)^2", -Rational(1, 4)*(x - 3)*(x + 1)**2),
    C(r"p(x)=-\dfrac14(x+3)^2(x-1)", -Rational(1, 4)*(x + 3)**2*(x - 1))],
   lambda: (lambda av: av*(x + 3)*(x - 1)**2)(solve(a*(-1 + 3)*(-1 - 1)**2 - (-2), a)[0]),
   "Zeros and multiplicity",
   r"A crossing at $-3$ is a single factor and a touch at $1$ is a squared factor: $p(x)=a(x+3)(x-1)^2$. Using $p(-1)=a(2)(4)=-2$ gives $a=-\frac14$. (The other choices have the signs or the double root in the wrong place, or give $p(-1)=+2$.)",
   order='free', fig='cubic')

mc(4, 'H',
   r"The function $f$ is defined by [[D:f(x)=\begin{cases}-2x+9 & \text{if } x<3\\[1mm] (x-5)^2+1 & \text{if } x\ge3\end{cases}:D]] How many values of $a$ satisfy $f(a)=5$?",
   C(3), [C(1), C(2), C(4)],
   lambda: Integer(len(set([v for v in solve(-2*x + 9 - 5, x) if v < 3] + [v for v in solve((x - 5)**2 + 1 - 5, x) if v >= 3]))),
   "Pick the branch",
   r"Branch 1 ($a<3$): $-2a+9=5$ gives $a=2$, valid. Branch 2 ($a\ge3$): $(a-5)^2=4$ gives $a=3$ or $a=7$, both valid ($a=3$ belongs to this branch). Three values: $2,3,7$.")

mc(4, 'H',
   r"What is the sum of the zeros of $g(x)=-|x+3|+8$?",
   C(-6), [C(-11), C(5), C(6)],
   lambda: sum(solve(-Abs(x + 3) + 8, x)),
   "Absolute value: two cases",
   r"$|x+3|=8$ gives $x=5$ or $x=-11$, and the sum is $-6$ (it is twice the center $-3$). (Traps: $5$ or $-11$ is a single zero; $6$ comes from using the center $+3$.)")

mc(4, 'H',
   r"The function $f$ is defined by $f(x)=x^2-6x$. What is the sum of all values of $k$ for which $f(2k)=f(k+3)$?",
   C(4), [C(1), C(3), C(6)],
   lambda: sum(solve(Eq((2*k)**2 - 6*(2*k), (k + 3)**2 - 6*(k + 3)), k)),
   "Symmetry about the axis",
   r"Equal outputs happen when the inputs are equal ($2k=k+3$, so $k=3$) or symmetric about the axis $x=3$ ($2k+k+3=6$, so $k=1$). The sum is $4$. (Choices $3$ and $1$ each find only one of the two cases; $6$ is the sum of the symmetric inputs.)")

gi(4, 'H',
   r"The function $g$ is defined by $g(x)=-3x^2+18x-5$. For a real number $a\ne-1$, $g(a)=g(-1)$. What is the value of $a$?",
   "7", Integer(7),
   lambda: [v for v in solve(Eq(-3*k**2 + 18*k - 5, -3*(-1)**2 + 18*(-1) - 5), k) if v != -1][0],
   "Symmetry about the axis",
   r"The axis is $x=-\frac{18}{2(-3)}=3$. The point symmetric to $x=-1$ is $2(3)-(-1)=7$.")

mc(4, 'H',
   r"The function $f$ is defined by $f(x)=x^2-2x$, and $g(x)=f(x-2)+3$. How many $x$-intercepts does the graph of $y=g(x)$ have?",
   C(0), [C(1), C(2), C(3)],
   lambda: Integer(len(solve(((x - 2)**2 - 2*(x - 2)) + 3, x))),
   "Shift rules (x → x − h)",
   r"$g(x)=(x-2)^2-2(x-2)+3=x^2-6x+11$, with discriminant $36-44<0$. (Also: $f$ has vertex $(1,-1)$, so $g$ has vertex $(3,2)$, above the axis and opening up: no intercepts. Choice 2 assumes $g$ keeps the zeros of $f$.)")

mc(4, 'H',
   r"A parabola opens upward, has $x$-intercepts at $(-2,0)$ and $(6,0)$, and has $y$-intercept $(0,-24)$. Which equation defines the parabola?",
   C(r"y=2(x+2)(x-6)", 2*(x + 2)*(x - 6)),
   [C(r"y=2(x-2)(x+6)", 2*(x - 2)*(x + 6)), C(r"y=-2(x+2)(x-6)", -2*(x + 2)*(x - 6)), C(r"y=(x+2)(x-6)-24", (x + 2)*(x - 6) - 24)],
   lambda: (lambda av: av*(x + 2)*(x - 6))(solve(a*(0 + 2)*(0 - 6) + 24, a)[0]),
   "Test the points",
   r"$y=a(x+2)(x-6)$ and $y(0)=-12a=-24$ give $a=2>0$. (Traps: $(x-2)(x+6)$ has the zeros at the wrong signs; $-2(\ldots)$ opens downward; subtracting $24$ shifts the whole graph instead of scaling it.)", order='free')

gi(4, 'H',
   r"The function $f$ is defined by $f(x)=x^2+bx+c$, where $b$ and $c$ are constants. The function $g$ is defined by $g(x)=f(x-4)$ and its zeros are $1$ and $9$. What is the minimum value of $f$?",
   "-16", Integer(-16),
   lambda: vertex((x + 3)*(x - 5))[1],
   "Shift rules (x → x − h)",
   r"$g(x)=f(x-4)=0$ at $x=1,9$ means $f(-3)=f(5)=0$ (subtract $4$ from each zero). So $f(x)=(x+3)(x-5)$, the axis is $x=1$ and the minimum is $f(1)=4(-4)=-16$.")

# ============================================================ SET 5  (Summit, 20)
mc(5, 'H',
   r"The function $f(x)=ax^2+bx+c$ has constants $a$, $b$ and $c$. The graph of $y=f(x)$ is a parabola that opens upward and has vertex $(h,k)$ with $k<0$. Also, $f(-5)=f(1)$. Which of the following must be true?"
   "\n" r"I. $b>0$" "\n" r"II. $c<0$" "\n" r"III. The equation $f(x)=0$ has two distinct real solutions",
   T(r"I and III only"), [T(r"I only"), T(r"II and III only"), T(r"I, II and III")],
   lambda: must_be_true_51(),
   "Symmetry about the axis",
   r"$f(-5)=f(1)$ puts the axis at $x=-2$, so $-\frac b{2a}=-2$ and $b=4a>0$ (I is true). The vertex is below the axis and the parabola opens up, so it crosses the axis twice (III is true). But $c=f(0)=4a+k$ can be positive (try $a=5$, $k=-1$), so II is not forced.", order=1)

gi(5, 'H',
   r"A concert hall sells $1200-30p$ tickets per show when the ticket price is $p$ dollars. The revenue is the price times the number of tickets sold. The owner will not charge less than $\$25$. What is the greatest possible revenue per show, in dollars?",
   "11250", Integer(11250),
   lambda: max(Rational(n, 4)*(1200 - 30*Rational(n, 4)) for n in range(100, 161)),
   "Domain limit: check the vertex",
   r"$R(p)=p(1200-30p)$ has zeros $0$ and $40$, so its vertex is $p=20$, which is below the allowed minimum $25$. For $p\ge25$ the revenue only falls, so the best price is $25$: $R=25(450)=11{,}250$. (The vertex value $12{,}000$ is not allowed.)")

mc(5, 'H',
   r"Town A's population $t$ years from now is modeled by $A(t)=12{,}000(1.10)^t$, and town B's is modeled by $B(t)=18{,}000(1.04)^t$. For what least whole number of years $t$ does town A's population first exceed town B's?",
   C(8), [C(6), C(7), C(13)],
   lambda: [n for n in range(0, 100) if 12000*Rational(11, 10)**n > 18000*Rational(104, 100)**n][0],
   "Graph it (Desmos)",
   r"Graph both curves: they cross where $\left(\frac{1.10}{1.04}\right)^t=1.5$, near $t\approx7.2$. At $t=7$, $A\approx23{,}385<B\approx23{,}687$; at $t=8$, $A\approx25{,}723>B\approx24{,}634$. So $t=8$. (Traps: $6$ is the gap $10-4$; $7$ rounds $7.2$ down; $13$ is $\frac{50}{4}$.)")

mc(5, 'H',
   r"The number of views $V$ of a video $d$ days after it is posted is modeled by $V(d)=500\cdot2^{d/3}$. Which function gives the number of views $w$ weeks after it is posted?",
   C(r"V(w)=500\cdot2^{7w/3}", 500*2**(7*w/3)),
   [C(r"V(w)=500\cdot2^{w/3}", 500*2**(w/3)), C(r"V(w)=500\cdot2^{3w/7}", 500*2**(3*w/7)), C(r"V(w)=500\cdot2^{21w}", 500*2**(21*w))],
   lambda: 500*2**((7*w)/3),
   "Unit change: t = m/12",
   r"$w$ weeks is $d=7w$ days. Substitute: $500\cdot2^{7w/3}$. (Traps: leaving $d=w$; inverting $7$ and $3$; multiplying $3\cdot7$.)", order='free')

gi(5, 'H',
   r"The table shows values of the quadratic function $f$. [[TABLE]] What is the value of $f(4)$?",
   "-9", Integer(-9),
   lambda: fit_quadratic([(0, 7), (1, -3), (6, 7)]).subs(x, 4),
   "Symmetry about the axis",
   r"$f(0)=f(6)$ puts the axis at $x=3$. Write $f(x)=a(x-3)^2+k$: $9a+k=7$ and $4a+k=-3$, so $a=2$, $k=-11$. Then $f(4)=2(1)-11=-9$.",
   table=[[r"$x$", "0", "1", "6"], [r"$f(x)$", "7", r"$-3$", "7"]])

mc(5, 'H',
   r"The graph of $y=g(x)$ is the graph of $y=3^x$ reflected over the $x$-axis, stretched vertically by a factor of $2$, shifted $1$ unit right, and shifted $5$ units up. For what value of $x$ is $g(x)=-49$?",
   C(4), [C(3), C(5), C(28)],
   lambda: round(float(numeric(solve(Eq(-2*3**(x - 1) + 5, -49), x)[0]))),
   "Shift rules (x → x − h)",
   r"The transformations give $g(x)=-2\cdot3^{x-1}+5$. Then $-2\cdot3^{x-1}=-54$, so $3^{x-1}=27=3^3$ and $x-1=3$, $x=4$. (Traps: $3$ forgets the right shift; $5$ shifts the wrong way; $28$ treats $3^{x-1}$ as $x-1$ added to $27$.)")

gi(5, 'H',
   r"The function $f$ is defined by $f(x)=3x+k$, where $k$ is a constant. If $f(f(x))=9x+20$ for all $x$, what is the value of $k$?",
   "5", Integer(5),
   lambda: solve(expand((3*(3*x + k) + k) - (9*x + 20)), k)[0],
   "Compose inside-out",
   r"$f(f(x))=3(3x+k)+k=9x+4k$. Then $4k=20$ and $k=5$. (Squaring $f$ or adding $k$ only once are the usual slips.)")

mc(5, 'H',
   r"The polynomial $p$ is defined by $p(x)=(x-2)(x^2+kx+9)$, where $k$ is a constant. The graph of $y=p(x)$ has exactly two distinct $x$-intercepts. Which of the following could be the value of $k$?",
   C(6), [C(0), C(5), C(10)],
   lambda: [kv for kv in (0, 5, 6, 10) if len(set(solve((x - 2)*(x**2 + kv*x + 9), x))) == 2][0],
   "Zeros and multiplicity",
   r"The quadratic factor must add exactly one new zero: a double root ($D=k^2-36=0$, so $k=\pm6$; for $k=6$ the root is $-3$). For $k=0$ or $5$ it has no real zeros (one intercept in all); for $k=10$ it has two new zeros (three intercepts).", order='free')

mc(5, 'H',
   r"The function $f$ is defined by $f(x)=ab^x$, where $a$ and $b$ are constants and $b>0$. If $f(1)=-12$ and $f(3)=-48$, what is the value of $f(0)$?",
   C(-6), [C(-24), C(-3), C(6)],
   lambda: [d[a] for d in solve([a*b - (-12), a*b**3 - (-48)], [a, b], dict=True) if d[b] > 0][0],
   "Two points: divide to get b",
   r"$b^2=\frac{-48}{-12}=4$, so $b=2$. Going back one step from $f(1)$ divides by $b$: $f(0)=\frac{-12}2=-6$. (Traps: $-24$ multiplies by $b$; $-3$ divides by $b^2$; $6$ loses the sign.)")

gi(5, 'H',
   r"A rancher uses $240$ meters of fencing to build a rectangular field and one dividing fence parallel to the field's width. The fencing consists of three pieces of length $W$ meters (the width) and two pieces of length $L$ meters (the length). What is the greatest possible area of the field, in square meters?",
   "2400", Integer(2400),
   lambda: max(n*Rational(240 - 3*n, 2) for n in range(1, 80)),
   "Optimize: vertex of the product",
   r"With width $W$, $3W+2L=240$, so $L=\frac{240-3W}2$ and $A=\frac{W(240-3W)}2$. The zeros are $W=0$ and $W=80$, so the maximum is at $W=40$: $L=60$ and $A=2400$.")

mc(5, 'H',
   r"A parabola passes through $(-1,10)$, $(0,4)$ and $(3,10)$. Which equation defines it in vertex form?",
   C(r"y=2(x-1)^2+2", 2*(x - 1)**2 + 2),
   [C(r"y=2(x+1)^2+2", 2*(x + 1)**2 + 2), C(r"y=2(x-1)^2+4", 2*(x - 1)**2 + 4), C(r"y=6(x-1)^2+4", 6*(x - 1)**2 + 4)],
   lambda: (lambda f: (lambda hh, kk: f.coeff(x, 2)*(x - hh)**2 + kk)(*vertex(f)))(fit_quadratic([(-1, 10), (0, 4), (3, 10)])),
   "Vertex form reads h and k",
   r"Equal outputs at $x=-1$ and $x=3$ put the axis at $x=1$. Then $y=a(x-1)^2+k$: $a+k=4$ and $4a+k=10$, so $a=2$, $k=2$. (Sign slip on $h$ gives $2(x+1)^2$; the others fail $(0,4)$.)", order='free')

mc(5, 'H',
   r"The functions $f$ and $g$ are defined by $f(x)=|x-3|$ and $g(x)=2x-5$. For how many values of $x$ is $g(f(x))=f(g(x))$?",
   C(0), [C(1), C(2), C(3)],
   lambda: Integer(len(set(
       [v for v in solve((2*(3 - x) - 5) - (8 - 2*x), x) if v < 3] +
       [v for v in solve((2*(x - 3) - 5) - (8 - 2*x), x) if 3 <= v < 4] +
       [v for v in solve((2*(x - 3) - 5) - (2*x - 8), x) if v >= 4]))),
   "Graph it (Desmos)",
   r"$g(f(x))=2|x-3|-5$ and $f(g(x))=|2x-8|=2|x-4|$. The equation becomes $|x-3|-|x-4|=2.5$, but the left side always lies between $-1$ and $1$. Graphing $y=2|x-3|-5$ and $y=2|x-4|$ shows two V shapes with the second always at least $3$ units above the first: they never meet, so there are $0$ solutions.")

gi(5, 'H',
   r"The number of bacteria in a sample grows by $40\%$ every $2$ hours. After $6$ hours, the number of bacteria is what percent greater than the starting number? Enter only the number.",
   "174.4", Rational(1744, 10),
   lambda: round(float(100*(Rational(14, 10)**3 - 1)), 1),
   "Growth factor = 1 ± rate",
   r"$6$ hours is $3$ periods of $2$ hours: $1.4^3=2.744$, which is $174.4\%$ greater. (Not $3\cdot40=120\%$: growth compounds.)")

mc(5, 'H',
   r"The polynomial $p(x)=a(x+2)(x-3)^2$, where $a>0$, is graphed in the $xy$-plane. For which values of $x$ is $p(x)<0$?",
   T(r"$x<-2$", "x<-2"), [T(r"$x>3$", "x>3"), T(r"$-2<x<3$", "-2<x<3"), T(r"$x<-2$ or $x>3$", "x<-2 or x>3")],
   lambda: " or ".join(lab for lab, tp in (("x<-2", -3), ("-2<x<3", 0), ("x>3", 4)) if (1*(tp + 2)*(tp - 3)**2) < 0),
   "Zeros and multiplicity",
   r"The factor $(x-3)^2$ is never negative, so the sign is the sign of $(x+2)$ (with $a>0$), except at the touching zero $x=3$. So $p<0$ only for $x<-2$. (The graph does not change sign at $x=3$.)", order='free')

gi(5, 'H',
   r"A fish population in a pond is modeled by $P(t)=-2(t-6)^2+130$, where $t$ is the number of months after January 1. For how many months is the population at least $112$ fish?",
   "6", Integer(6),
   lambda: (lambda zs: max(zs) - min(zs))(solve(-2*(t - 6)**2 + 130 - 112, t)),
   "Vertex form reads h and k",
   r"$-2(t-6)^2+130\ge112$ gives $(t-6)^2\le9$, so $3\le t\le9$. By symmetry the period is $2\cdot3=6$ months long.")

mc(5, 'H',
   r"The graph of $f(x)=2(x-1)^2+3$ is translated $4$ units to the right and then reflected across the $y$-axis to make the graph of $g$. What are the coordinates of the vertex of the graph of $g$?",
   T(r"$(-5,3)$"), [T(r"$(3,3)$"), T(r"$(5,3)$"), T(r"$(-3,3)$")],
   lambda: "$%s$" % vtx_str((lambda f: f(-x - 4))(lambda u: 2*(u - 1)**2 + 3)),
   "Shift rules (x → x − h)",
   r"Vertex $(1,3)$; right $4$: $(5,3)$; reflect across the $y$-axis: $(-5,3)$. (Reflecting first and then shifting right gives $(-1+4,3)=(3,3)$, the order trap.)", order='free')

mc(5, 'H',
   r"The number of members $N$ of a club $t$ years after it was founded is modeled by $N(t)=800(1.44)^{t/2}$. The number of members grows by what percent each year?",
   C(r"20\%", 20), [C(r"22\%", 22), C(r"44\%", 44), C(r"120\%", 120)],
   lambda: round(float((Rational(144, 100)**Rational(1, 2) - 1)*100)),
   "Per-period exponent",
   r"$1.44^{t/2}=\left(\sqrt{1.44}\right)^t=1.2^t$, so the yearly factor is $1.2$: a $20\%$ increase. (Traps: $44\%$ is the growth per $2$ years; $22\%$ halves it; $120\%$ is the factor, not the increase.)")

mc(5, 'H',
   r"The table shows values of a function $f$. [[TABLE]] Which of the following equations defines $f$?",
   C(r"f(x)=3x^2-3", 3*x**2 - 3), [C(r"f(x)=9x-9", 9*x - 9), C(r"f(x)=3x^2-3x", 3*x**2 - 3*x), C(r"f(x)=3^{x+1}-9", 3**(x + 1) - 9)],
   lambda: fit_quadratic([(1, 0), (2, 9), (4, 45)]),
   "Test the points",
   r"Test each equation at all four points. $3x^2-3$ gives $0,9,45,72$ at $x=1,2,4,5$. (The linear choice fits only $x=1,2$; $3x^2-3x$ fails at $x=2$; the exponential fails at $x=2$.)",
   table=[[r"$x$", "1", "2", "4", "5"], [r"$f(x)$", "0", "9", "45", "72"]], order='free')

mc(5, 'H',
   r"The function $f$ is defined by $f(x)=2x^2-3x$, and $g(x)=x-2$. For what value of $x$ is $f(g(x))=f(x)$?",
   C(r"\dfrac74", Rational(7, 4)), [C(1), C(r"\dfrac72", Rational(7, 2)), C(7)],
   lambda: solve(Eq(2*(x - 2)**2 - 3*(x - 2), 2*x**2 - 3*x), x)[0],
   "Symmetry about the axis",
   r"$f$ has axis $x=\frac34$. $f(x-2)=f(x)$ means $x-2$ and $x$ are symmetric about it: $(x-2)+x=\frac32$, so $x=\frac74$. (Or expand: $-8x+14=0$.) (Traps: $\frac72$ forgets to halve; $7$ drops the denominator.)")

mc(5, 'H',
   r"The functions $f$ and $g$ are defined by $f(x)=-(x-2)^2+9$ and $g(x)=2x-4$. At what value of $x$ does $f(g(x))$ reach its maximum?",
   C(3), [C(-1), C(2), C(9)],
   lambda: vertex(-((2*x - 4) - 2)**2 + 9)[0],
   "Compose inside-out",
   r"$f(g(x))=-(2x-6)^2+9$ is maximal when $2x-6=0$, i.e. $g(x)=2$ (the input where $f$ peaks), so $x=3$. (Traps: $2$ is where $f$ peaks; $9$ is the maximum value; $-1$ solves $2x+4=2$.)")

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
