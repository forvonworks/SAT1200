#!/usr/bin/env python3
"""Book 3, Lesson 7 "Data-analysis edge cases": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX; figures/tables are @@name@@ tokens expanded by build.py),
  * a worked solution (this is what students see),
  * a `calc` function (or an `each` predicate for "which statement ..." items) that recomputes the
    answer independently of the printed solution, from the SAME data that is drawn in the figure
    (exact Fractions, brute force, least-squares fits, random simulation of data sets).

Running `python3 verify.py` recomputes every answer, checks that exactly one MC choice is correct
and that choices are distinct, balances the correct letters, and prints ALL OK / FAIL.
(`build.py` imports PROBLEMS and FIGS from this file to write problems.md and the .tex files.)

Owner rule: the lesson never teaches or uses the sigma formula for standard deviation.  Students compare
spread by reasoning (spread, shape, skyrocket / double-top bars).  The helper `sd()` below exists only so that
this verifier can check such comparisons numerically.
"""
import sys, math, random
from fractions import Fraction
from itertools import combinations, product
from sympy import Rational, Integer, sympify, latex, S, nsimplify

PROBLEMS = []
FIGS = {}          # name -> dict(tex=..., md=...)
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "Center and spread by reasoning: shifts, scales, outliers, graphs", "Hard"),
    3: ("Set 3", "Tables, bounds and two-variable models", "Hard"),
    4: ("Set 4", "Probability, inference and statistical claims", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- statistics helpers (verification only)
def mean(l):
    return Fraction(sum(Fraction(v) for v in l), len(l))

def median(l):
    s = sorted(Fraction(v) for v in l)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

def mode_list(l):
    from collections import Counter
    c = Counter(l)
    m = max(c.values())
    return sorted(k for k, v in c.items() if v == m)

def quartiles(l):
    s = sorted(Fraction(v) for v in l)
    n = len(s)
    lo, hi = s[:n // 2], s[(n + 1) // 2:]
    return median(lo), median(hi)

def iqr(l):
    q1, q3 = quartiles(l)
    return q3 - q1

def rng(l):
    return Fraction(max(l)) - Fraction(min(l))

def sd(l):
    """Numeric spread, used ONLY to verify comparison items (never shown to students)."""
    m = float(mean(l))
    return math.sqrt(sum((float(v) - m) ** 2 for v in l) / len(l))

def expand(table):
    """{value: count} -> list of values."""
    out = []
    for v, c in table.items():
        out += [v] * c
    return out

def lsq(pts):
    """Least-squares line y = m x + b through points."""
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    m = sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts)
    return m, my - m * mx

def R(v):
    if isinstance(v, Fraction):
        return Rational(v.numerator, v.denominator)
    return sympify(v)

# ---------------------------------------------------------------- choice constructors
def C(v):
    v = R(v)
    return ("$%s$" % latex(v), v)

def FR(a, b):
    return ("$\\dfrac{%d}{%d}$" % (a, b), Rational(a, b))

def DEC(txt):
    return ("$%s$" % txt, Rational(txt))

def PCT(v):
    return ("$%s\\%%$" % (latex(R(v))), R(v))

def T(text, val=None):
    return (text, text if val is None else val)

def same(u, v):
    if isinstance(u, (tuple, str, list)) or isinstance(v, (tuple, str, list)) or callable(u) or callable(v):
        return u == v
    try:
        return R(u) == R(v)
    except Exception:
        return u == v

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='auto', each=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, each=each))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=R(ans_val),
                         calc=calc, trick=trick, sol=sol))

# ---------------------------------------------------------------- figures (true scale TikZ + markdown twin)
def _fmt(v):
    return ("%g" % v)

def reg(name, tex, md):
    FIGS[name] = dict(tex=tex, md=md)
    return "@@%s@@" % name

def tbl_fig(name, header, rows, colspec=None, first_left=True):
    k = len(header)
    spec = colspec or ("|" + ("l|" if first_left else "c|") + "c|" * (k - 1))
    t = [r"\begin{center}{\small\renewcommand{\arraystretch}{1.15}\setlength{\tabcolsep}{4.5pt}",
         r"\begin{tabular}{%s}\hline" % spec,
         " & ".join(r"\cellcolor{accent}\textcolor{white}{\bfseries %s}" % h for h in header) + r"\\ \hline"]
    for r_ in rows:
        t.append(" & ".join(str(c) for c in r_) + r"\\ \hline")
    t.append(r"\end{tabular}}\end{center}")
    md = ["| " + " | ".join(header) + " |", "|" + "---|" * k]
    for r_ in rows:
        md.append("| " + " | ".join(str(c).replace(r"\textbf{", "").replace("}", "") for c in r_) + " |")
    return reg(name, "\n".join(t), "\n".join(md))

def bars_fig(name, panels, ymax, width=78, height=19):
    """panels: list of dict(title, counts, labels). Counts printed above bars; common vertical scale."""
    n = len(panels)
    gap = 5.0
    pw = (width - gap * (n - 1)) / n
    s = [r"\begin{center}\begin{tikzpicture}[font=\sffamily\fontsize{6.5}{7}\selectfont]"]
    md = []
    for i, p in enumerate(panels):
        x0 = i * (pw + gap)
        cnt = p['counts']
        k = len(cnt)
        bw = pw / k
        s.append(r"\draw[ink!60,line width=0.4pt] (%.2fmm,0mm) -- (%.2fmm,0mm);" % (x0, x0 + pw))
        for j, c in enumerate(cnt):
            h = c * height / ymax
            cx = x0 + (j + 0.5) * bw
            if c > 0:
                s.append(r"\fill[accent!85] (%.2fmm,0mm) rectangle (%.2fmm,%.2fmm);" % (cx - 0.38 * bw, cx + 0.38 * bw, h))
                s.append(r"\node[above,inner sep=0.6pt,text=ink] at (%.2fmm,%.2fmm) {%d};" % (cx, h, c))
            s.append(r"\node[below,inner sep=1pt,text=ink!85] at (%.2fmm,0mm) {%s};" % (cx, p['labels'][j]))
        if p.get('title'):
            s.append(r"\node[inner sep=0pt,font=\sffamily\bfseries\fontsize{8}{8}\selectfont] at (%.2fmm,%.2fmm) {%s};" % (x0 + pw / 2, height + 5.5, p['title']))
        if p.get('xlabel'):
            s.append(r"\node[below,inner sep=0pt] at (%.2fmm,-4.2mm) {%s};" % (x0 + pw / 2, p['xlabel']))
        md.append("%sbar graph (value: number of data values): " % ((p['title'] + ": ") if p.get('title') else "") +
                  ", ".join("%s: %d" % (p['labels'][j], cnt[j]) for j in range(k)))
    s.append(r"\end{tikzpicture}\end{center}")
    return reg(name, "\n".join(s), "\n\n".join("*[Figure: " + m_ + "]*" for m_ in md))

def hist_fig(name, edges, counts, ymax, ystep, xlabel, ylabel, width=70, height=30):
    ne = len(counts)
    bw = width / ne
    s = [r"\begin{center}\begin{tikzpicture}[font=\sffamily\fontsize{6.5}{7}\selectfont]"]
    for yv in range(0, ymax + 1, ystep):
        yy = yv * height / ymax
        s.append(r"\draw[ink!%d,line width=0.3pt] (0mm,%.2fmm) -- (%.2fmm,%.2fmm);" % (25 if yv else 70, yy, width, yy))
        s.append(r"\node[left,inner sep=1.5pt] at (0mm,%.2fmm) {%d};" % (yy, yv))
    for j, c in enumerate(counts):
        s.append(r"\fill[accent!80] (%.2fmm,0mm) rectangle (%.2fmm,%.2fmm);" % (j * bw, (j + 1) * bw, c * height / ymax))
        s.append(r"\draw[white,line width=0.4pt] (%.2fmm,0mm) rectangle (%.2fmm,%.2fmm);" % (j * bw, (j + 1) * bw, c * height / ymax))
    s.append(r"\draw[ink!70,line width=0.4pt] (0mm,0mm) -- (0mm,%.2fmm);" % height)
    for j, e in enumerate(edges):
        s.append(r"\node[below,inner sep=1.5pt] at (%.2fmm,0mm) {%s};" % (j * bw, e))
    s.append(r"\node[below,inner sep=0pt] at (%.2fmm,-4.5mm) {%s};" % (width / 2, xlabel))
    s.append(r"\node[rotate=90,above,inner sep=5pt] at (-2.5mm,%.2fmm) {%s};" % (height / 2, ylabel))
    s.append(r"\end{tikzpicture}\end{center}")
    md = "*[Figure: histogram. %s on the horizontal axis, %s on the vertical axis. Bars (class: frequency): %s]*" % (
        xlabel, ylabel, ", ".join("%s-%s: %d" % (edges[j], edges[j + 1], counts[j]) for j in range(ne)))
    return reg(name, "\n".join(s), md)

def box_fig(name, boxes, lo, hi, step, xlabel, width=70):
    """boxes: list of (label, min, q1, med, q3, max); true scale."""
    u = width / (hi - lo)
    def X(v):
        return (v - lo) * u
    s = [r"\begin{center}\begin{tikzpicture}[font=\sffamily\fontsize{7}{8}\selectfont]"]
    md = []
    for i, (lab, mn, q1, md_, q3, mx) in enumerate(boxes):
        y = -(i * 10 + 4)
        s.append(r"\draw[ink,line width=0.5pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(mn), y, X(q1), y))
        s.append(r"\draw[ink,line width=0.5pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(q3), y, X(mx), y))
        s.append(r"\draw[ink,line width=0.5pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(mn), y - 1.5, X(mn), y + 1.5))
        s.append(r"\draw[ink,line width=0.5pt] (%.2fmm,%dmm) -- (%.2fmm,%dmm);" % (X(mx), y - 1.5, X(mx), y + 1.5))
        s.append(r"\draw[ink,fill=accent!22,line width=0.5pt] (%.2fmm,%.1fmm) rectangle (%.2fmm,%.1fmm);" % (X(q1), y - 2.8, X(q3), y + 2.8))
        s.append(r"\draw[ink,line width=0.9pt] (%.2fmm,%.1fmm) -- (%.2fmm,%.1fmm);" % (X(md_), y - 2.8, X(md_), y + 2.8))
        s.append(r"\node[left,inner sep=3pt] at (0mm,%dmm) {\bfseries %s};" % (y, lab))
        md.append("%s: minimum %s, first quartile %s, median %s, third quartile %s, maximum %s" % (lab, _fmt(mn), _fmt(q1), _fmt(md_), _fmt(q3), _fmt(mx)))
    ya = -(len(boxes) * 10 + 1)
    s.append(r"\draw[ink,line width=0.5pt] (0mm,%dmm) -- (%.2fmm,%dmm);" % (ya, width, ya))
    v = lo
    while v <= hi + 1e-9:
        s.append(r"\draw[ink,line width=0.4pt] (%.2fmm,%dmm) -- (%.2fmm,%.1fmm);" % (X(v), ya, X(v), ya - 1.4))
        s.append(r"\node[below,inner sep=1.2pt] at (%.2fmm,%.1fmm) {%s};" % (X(v), ya - 1.2, _fmt(v)))
        v += step
    s.append(r"\node[below,inner sep=0pt] at (%.2fmm,%.1fmm) {%s};" % (width / 2, ya - 6.3, xlabel))
    s.append(r"\end{tikzpicture}\end{center}")
    return reg(name, "\n".join(s), "*[Figure: box plots of %s, drawn to scale. %s]*" % (xlabel, "; ".join(md)))

def dots_fig(name, counts, lo, hi, xlabel, width=72):
    """counts: dict value -> number of dots."""
    u = width / (hi - lo)
    s = [r"\begin{center}\begin{tikzpicture}[font=\sffamily\fontsize{7}{8}\selectfont]"]
    r_ = 1.35
    for v, c in counts.items():
        for k in range(c):
            s.append(r"\fill[accent] (%.2fmm,%.2fmm) circle (%.2fmm);" % ((v - lo) * u, r_ + k * 2 * r_ * 1.05, r_))
    s.append(r"\draw[ink,line width=0.5pt] (-2mm,0mm) -- (%.2fmm,0mm);" % (width + 2))
    for v in range(int(lo), int(hi) + 1):
        s.append(r"\draw[ink,line width=0.4pt] (%.2fmm,0mm) -- (%.2fmm,-1.3mm);" % ((v - lo) * u, (v - lo) * u))
        s.append(r"\node[below,inner sep=1.2pt] at (%.2fmm,-1.2mm) {%d};" % ((v - lo) * u, v))
    s.append(r"\node[below,inner sep=0pt] at (%.2fmm,-6.3mm) {%s};" % (width / 2, xlabel))
    s.append(r"\end{tikzpicture}\end{center}")
    return reg(name, "\n".join(s), "*[Figure: dot plot of %s (value: number of dots): %s]*" % (
        xlabel, ", ".join("%s: %d" % (_fmt(v), c) for v, c in counts.items())))

def scat_fig(name, pts, xr, yr, xstep, ystep, xlab, ylab, line=None, labels=None, width=66, height=46):
    """pts: list of (x,y). xr,yr = (lo,hi). line=(m,b) drawn across the x-range. labels: letters for points."""
    ux = width / (xr[1] - xr[0])
    uy = height / (yr[1] - yr[0])
    def X(v):
        return (v - xr[0]) * ux
    def Y(v):
        return (v - yr[0]) * uy
    s = [r"\begin{center}\begin{tikzpicture}[font=\sffamily\fontsize{6.5}{7}\selectfont]"]
    v = xr[0]
    while v <= xr[1] + 1e-9:
        s.append(r"\draw[ink!22,line width=0.3pt] (%.2fmm,0mm) -- (%.2fmm,%.2fmm);" % (X(v), X(v), height))
        s.append(r"\node[below,inner sep=2.4pt] at (%.2fmm,0mm) {%s};" % (X(v), _fmt(v)))
        v += xstep
    v = yr[0]
    while v <= yr[1] + 1e-9:
        s.append(r"\draw[ink!22,line width=0.3pt] (0mm,%.2fmm) -- (%.2fmm,%.2fmm);" % (Y(v), width, Y(v)))
        s.append(r"\node[left,inner sep=2.6pt] at (0mm,%.2fmm) {%s};" % (Y(v), _fmt(v)))
        v += ystep
    s.append(r"\draw[ink,line width=0.5pt] (0mm,0mm) rectangle (%.2fmm,%.2fmm);" % (width, height))
    if line:
        m, b = line
        # clip the line to the plotting window
        xs = [xr[0], xr[1]]
        pts_l = [(x_, m * x_ + b) for x_ in xs]
        if m != 0:
            for yv in yr:
                xx = (yv - b) / m
                if xr[0] <= xx <= xr[1]:
                    pts_l.append((xx, yv))
        pts_l = sorted([p for p in pts_l if yr[0] - 1e-9 <= p[1] <= yr[1] + 1e-9])
        s.append(r"\draw[accent,line width=0.8pt] (%.2fmm,%.2fmm) -- (%.2fmm,%.2fmm);" % (X(pts_l[0][0]), Y(pts_l[0][1]), X(pts_l[-1][0]), Y(pts_l[-1][1])))
    for i, (x_, y_) in enumerate(pts):
        s.append(r"\fill[ink] (%.2fmm,%.2fmm) circle (0.95mm);" % (X(x_), Y(y_)))
        if labels:
            s.append(r"\node[inner sep=0pt,font=\sffamily\bfseries\fontsize{7.5}{8}\selectfont,text=accent] at (%.2fmm,%.2fmm) {%s};" % (X(x_) + 2.6, Y(y_) + 2.6, labels[i]))
    s.append(r"\node[below,inner sep=0pt] at (%.2fmm,-5.2mm) {%s};" % (width / 2, xlab))
    s.append(r"\node[rotate=90,above,inner sep=6pt] at (-4mm,%.2fmm) {%s};" % (height / 2, ylab))
    s.append(r"\end{tikzpicture}\end{center}")
    ptxt = ", ".join(("%s(%s, %s)" % ((labels[i] + " ") if labels else "", _fmt(p[0]), _fmt(p[1]))) for i, p in enumerate(pts))
    md = "*[Figure: scatterplot, %s on the horizontal axis and %s on the vertical axis. Points: %s.%s]*" % (
        xlab, ylab, ptxt, (" The line of best fit shown is y = %s x + %s." % (_fmt(line[0]), _fmt(line[1]))) if line else "")
    return reg(name, "\n".join(s), md)

# ---------------------------------------------------------------- random data sets with a given five-number summary
def datasets_with_summary(mn, q1, md_, q3, mx, trials=300, seed=7):
    """Random integer/half-integer data sets (n = 8, 12, 16) whose min/Q1/median/Q3/max match exactly."""
    rnd = random.Random(seed)
    out = []
    for _ in range(trials):
        n = rnd.choice([8, 12, 16])
        k = n // 4
        # quarter blocks; Q1 = mean of v_k and v_{k+1}, median = mean of v_{2k},v_{2k+1}, Q3 = mean of v_{3k}, v_{3k+1}
        def pair(c, lo_, hi_):
            d = rnd.choice([0, 0.5, 1, 2, 3, 4])
            a, b = c - d, c + d
            return (max(a, lo_), min(b, hi_)) if (a >= lo_ and b <= hi_) else (c, c)
        v = [None] * (n + 1)
        a, b = pair(q1, mn, md_); v[k], v[k + 1] = a, b
        a, b = pair(md_, mn, mx); v[2 * k], v[2 * k + 1] = a, b
        a, b = pair(q3, md_, mx); v[3 * k], v[3 * k + 1] = a, b
        if k == 1:
            # n = 4 not used; (n>=8 so k>=2)
            pass
        v[1] = mn
        v[n] = mx
        fill = rnd.choice(['uniform', 'low', 'high'])
        ok = True
        for i in range(1, n + 1):
            if v[i] is None:
                lo_ = v[i - 1] if v[i - 1] is not None else mn
                # next defined value
                j = i
                while j <= n and v[j] is None:
                    j += 1
                hi_ = v[j]
                lo_ = max(lo_, mn)
                if lo_ > hi_:
                    ok = False
                    break
                v[i] = {'low': lo_, 'high': hi_}.get(fill) if fill != 'uniform' else round(rnd.uniform(lo_, hi_) * 2) / 2
                v[i] = min(max(v[i], lo_), hi_)
        vals = v[1:]
        if ok and sorted(vals) == vals and (min(vals), max(vals)) == (mn, mx) and quartiles(vals) == (Fraction(q1), Fraction(q3)) and median(vals) == Fraction(md_):
            out.append(vals)
    assert len(out) > 50, "too few consistent data sets"
    return out

def must_be_true(stmt, summaries, pairs=300, seed=3):
    """stmt(d1, d2, ...) -> bool. True iff it holds for every sampled combination of data sets with the given summaries."""
    rnd = random.Random(seed)
    pools = [datasets_with_summary(*s_) for s_ in summaries]
    for _ in range(pairs):
        ds = [rnd.choice(p_) for p_ in pools]
        if not stmt(*ds):
            return False
    return True

# ============================================================ SET 1  (Medium/Hard, 12)
gi(1, 'M',
   r"The mean of 7 numbers is 24. After one of the numbers is removed, the mean of the remaining 6 numbers is 26. What number was removed?",
   "12", 12,
   lambda: [x_ for x_ in range(-200, 400) if Fraction(168 - x_, 6) == 26][0],
   "Work with totals, not means",
   r"Total of the 7 numbers: $7\cdot24=168$. Total of the remaining 6: $6\cdot26=156$. The removed number is $168-156=12$. (Subtracting the means gives 2, which is the change in the mean, not the number.)")

_l = [12, 15, 15, 18, 20]
_STAT = {"The mean": mean, "The median": median, "The mode": mode_list, "The range": rng}
mc(1, 'M',
   r"A data set consists of the values $12,\ 15,\ 15,\ 18,\ 20$. The value $40$ is added to the data set. Which of the following statistics is the same for the original data set and the new data set?",
   T("The mode"), [T("The mean"), T("The median"), T("The range")],
   None, "Which measure ignores a new extreme value?",
   r"Before: mean $16$, median $15$, mode $15$, range $8$. After adding $40$: mean $20$, median $\frac{15+18}{2}=16.5$, mode still $15$, range $28$. Only the mode is unchanged. (Many students pick the median because it is ``resistant,'' but with an even count it moves to the average of $15$ and $18$.)",
   order='free', each=lambda v: _STAT[v](_l) == _STAT[v](_l + [40]))

_A, _B = [10, 20, 30, 40, 50], [28, 29, 30, 31, 32]
def _rel(a, b, tol=1e-9):
    return 'same' if abs(a - b) < tol else ('A' if a > b else 'B')
mc(1, 'M',
   r"Data set $A$ is $10,\ 20,\ 30,\ 40,\ 50$ and data set $B$ is $28,\ 29,\ 30,\ 31,\ 32$. Which of the following is true?",
   T("The two data sets have the same mean, and $A$ has the greater standard deviation.", ('same', 'A')),
   [T("The two data sets have the same mean, and $B$ has the greater standard deviation.", ('same', 'B')),
    T("The two data sets have the same mean and the same standard deviation.", ('same', 'same')),
    T("Data set $A$ has the greater mean, and the standard deviations are equal.", ('A', 'same'))],
   lambda: (_rel(float(mean(_A)), float(mean(_B))), _rel(sd(_A), sd(_B))),
   "Spread: how far the values sit from the center",
   r"Both sets are centered at $30$ (mean $30$), but $A$ is spread from $10$ to $50$ while $B$ is packed between $28$ and $32$. More spread means a bigger standard deviation, so $A$'s is greater. (Same mean does not mean same spread.)",
   order='free')

_t14 = {0: 2, 1: 3, 2: 6, 3: 5, 4: 4}
_f = tbl_fig("s1_t4", ["Points on the quiz"] + [str(k) for k in _t14], [["Number of students"] + [v for v in _t14.values()]])
gi(1, 'M',
   r"The table shows the number of points earned on a quiz by 20 students." + _f + r"What is the mean number of points per student?",
   "2.3", Rational(23, 10), lambda: mean(expand(_t14)),
   "Weighted mean: multiply value by frequency",
   r"Total points: $0(2)+1(3)+2(6)+3(5)+4(4)=0+3+12+15+16=46$. Mean $=46\div20=2.3$. (Averaging the five point values, $2$, ignores how many students earned each.)")

_m5 = (2.5, 41)
mc(1, 'M',
   r"A teacher uses the line of best fit $y=2.5x+41$ to predict a student's exam score $y$ from the number of hours $x$ the student studied. Which statement is the best interpretation of the number $2.5$ in this context?",
   T("For each additional hour of study, the predicted exam score increases by $2.5$ points.", ('per hour', Rational(5, 2))),
   [T("A student who does not study is predicted to score $2.5$ points.", ('at zero', Rational(5, 2))),
    T("Each additional point on the exam requires $2.5$ more hours of study.", ('hours per point', Rational(5, 2))),
    T("A student who studies $2.5$ hours is predicted to score $41$ points.", ('at 2.5 hours', 41))],
   lambda: ('per hour', (Rational(5, 2) * 1 + 41) - (Rational(5, 2) * 0 + 41)),
   "Slope = change in $y$ for one more unit of $x$",
   r"The slope is the predicted change in $y$ for a one-unit increase in $x$: one more hour of study adds $2.5$ points. ($2.5$ is not the intercept, which is $41$, and it is points per hour, not hours per point.)",
   order='free')

_lang = {"Grade 10": (40, 25, 15), "Grade 11": (30, 18, 12), "Grade 12": (20, 12, 8)}
_f = tbl_fig("s1_t6", ["", "Spanish", "French", "German", "Total"],
             [[g] + list(v) + [sum(v)] for g, v in _lang.items()] + [["Total"] + [sum(v[i] for v in _lang.values()) for i in range(3)] + [180]])
mc(1, 'M',
   r"The table shows the language class chosen by 180 students." + _f + r"If a student who takes French is selected at random, what is the probability that the student is in grade 11?",
   FR(18, 55), [FR(1, 10), FR(3, 10), FR(11, 36)],
   lambda: Fraction(_lang["Grade 11"][1], sum(v[1] for v in _lang.values())),
   "Conditional probability: the ``given'' group is the denominator",
   r"The condition ``takes French'' restricts us to the French column, which has $25+18+12=55$ students. Of these, $18$ are in grade 11, so the probability is $\frac{18}{55}$. ($\frac{3}{10}=\frac{18}{60}$ divides by the grade 11 row instead; $\frac1{10}=\frac{18}{180}$ divides by everyone; $\frac{11}{36}=\frac{55}{180}$ is just the chance of taking French.)")

mc(1, 'H',
   r"In a random sample of 900 adult residents of a city, 62\% said they favor extending the library's opening hours. The margin of error for this estimate is 3 percentage points. Which of the following is the most appropriate conclusion?",
   T("It is plausible that the percent of all adult residents of the city who favor the extension is between $59\\%$ and $65\\%$.", ('plausible', 59, 65)),
   [T("Exactly $62\\%$ of all adult residents of the city favor the extension.", ('exact', 62)),
    T("Between $59\\%$ and $65\\%$ of the 900 adults surveyed favor the extension.", ('sample', 59, 65)),
    T("There is only a $3\\%$ chance that the survey result is wrong.", ('chance', 3))],
   lambda: ('plausible', 62 - 3, 62 + 3),
   "Estimate $\\pm$ margin of error gives a plausible interval for the population",
   r"The margin of error says the population percent is plausibly within $3$ points of the sample estimate: $62\pm3$, i.e. from $59\%$ to $65\%$. (The sample itself is known exactly: $62\%$ of the $900$. The margin of error is not a probability of being wrong.)",
   order='free')

mc(1, 'M',
   r"A librarian randomly selects 120 names from the list of all 2,400 registered members of a public library and asks them about the new borrowing hours; 78 of the 120 approve. What is the largest group to which the result can reasonably be generalized?",
   T("All 2,400 registered members of the library", ('population', 2400)),
   [T("Only the 120 members who were surveyed", ('population', 120)),
    T("All residents of the city where the library is located", ('population', 'city')),
    T("All public library members in the country", ('population', 'country'))],
   lambda: ('population', 2400),
   "Random sample: generalize only to the population it was drawn from",
   r"The sample was drawn at random from the list of registered members, so the result generalizes to those $2{,}400$ members and no further. (The $120$ is too narrow because a random sample is meant to represent the whole list; city residents or members elsewhere were never in the sampling frame.) Conceptual item.",
   order='free')

_t19 = {1: 2, 3: 2, 5: 3, 6: 1, 7: 1, 9: 1, 20: 1}
_f = tbl_fig("s1_t9", ["Value"] + [str(k) for k in _t19], [["Frequency"] + list(_t19.values())])
def _chg(a, b):
    return 'same' if a == b else ('down' if b < a else 'up')
_d9 = expand(_t19)
_d9b = [v for v in _d9 if v != 20]
mc(1, 'H',
   r"The table shows a data set of 11 values." + _f + r"The value $20$ is removed from the data set. Which statement is true about the new data set?",
   T("The mean decreases, and the median does not change.", ('down', 'same')),
   [T("The mean and the median both decrease.", ('down', 'down')),
    T("The mean does not change, and the median decreases.", ('same', 'down')),
    T("The mean and the median both stay the same.", ('same', 'same'))],
   lambda: (_chg(mean(_d9), mean(_d9b)), _chg(median(_d9), median(_d9b))),
   "Remove an extreme value: the mean moves, the median may not",
   r"Sorted: $1,1,3,3,5,5,5,6,7,9,20$. With $11$ values the median is the 6th: $5$. After removing $20$ there are $10$ values and the median is the average of the 5th and 6th, $\frac{5+5}{2}=5$: unchanged. The mean drops from $\frac{65}{11}\approx5.9$ to $\frac{45}{10}=4.5$.",
   order='free')

gi(1, 'M',
   r"Maya's mean score on her first 4 tests is 78. What score does she need on her 5th test to raise the mean of all 5 tests to 80?",
   "88", 88, lambda: [x_ for x_ in range(0, 200) if Fraction(78 * 4 + x_, 5) == 80][0],
   "Work with totals, not means",
   r"She needs a total of $5\cdot80=400$ points. She has $4\cdot78=312$, so she needs $400-312=88$. (Using $80+2=82$ forgets that the new mean must also cancel the shortfall of the first four tests.)")

mc(1, 'H',
   r"Each of three independent safety checks on a machine passes with probability $0.9$. What is the probability that at least one of the three checks fails?",
   DEC("0.271"), [DEC("0.1"), DEC("0.3"), DEC("0.729")],
   lambda: 1 - Rational(9, 10) ** 3,
   "``At least one'' = 1 minus ``none''",
   r"The opposite of ``at least one fails'' is ``all three pass'': $0.9^3=0.729$. So the answer is $1-0.729=0.271$. ($0.729$ is the chance that all pass; $0.3=3(0.1)$ adds the failure chances, which double-counts overlaps; $0.1$ is a single check.)")

gi(1, 'H',
   r"In a random sample of 250 residents of a town, 45 said they bike to work. Based on this sample, about how many of the town's 8,000 residents bike to work?",
   "1440", 1440, lambda: Fraction(45, 250) * 8000,
   "Expected count = sample proportion $\\times$ population",
   r"The sample proportion is $\frac{45}{250}=0.18$. Apply it to the town: $0.18\cdot8000=1440$. (Equivalently, the town is $\frac{8000}{250}=32$ times as large as the sample, and $45\cdot32=1440$. Do not apply $45$ out of $8000$ directly.)")

# ============================================================ SET 2  (Hard, 14)
_base = [26, 34]            # mean 30, SD 4  (the stated mean and SD are those of this data set)
def _ms(l):
    return (round(float(mean(l)), 6), round(sd(l), 6))
mc(2, 'H',
   r"The heights of the plants in a greenhouse have a mean of 30 centimeters and a standard deviation of 4 centimeters. Each height $h$ is converted to a code $c=10h-25$. What are the mean and the standard deviation of the codes?",
   T("Mean $275$, standard deviation $40$", (275, 40)),
   [T("Mean $275$, standard deviation $15$", (275, 15)), T("Mean $300$, standard deviation $40$", (300, 40)),
    T("Mean $275$, standard deviation $4$", (275, 4))],
   lambda: _ms([10 * v - 25 for v in _base]),
   "Linear change: the mean follows the formula, the SD only scales",
   r"The mean goes through the whole formula: $10(30)-25=275$. Subtracting $25$ only slides every value, so spread is unchanged by it; multiplying by $10$ stretches the spread by $10$: $10\cdot4=40$. (SD $15$ subtracts $25$ from the SD; $300$ forgets the $-25$ for the mean; SD $4$ forgets the multiplication.)",
   order='free')

gi(2, 'H',
   r"A data set has a standard deviation of 4. Every value in the data set is multiplied by $-3$ and then increased by 10. What is the standard deviation of the new data set?",
   "12", 12, lambda: round(sd([-3 * v + 10 for v in _base])),
   "SD scales by $|k|$, shifts do nothing",
   r"Adding $10$ does not change the spread. Multiplying by $-3$ flips the data and stretches the distances between values by a factor of $3$. A standard deviation is never negative, so it is multiplied by $|-3|=3$: $3\cdot4=12$. (The answer $-12$ is impossible.)")

_pa = dict(title="Data set A", counts=[1, 3, 12, 3, 1], labels=list("12345"))
_pb = dict(title="Data set B", counts=[7, 2, 2, 2, 7], labels=list("12345"))
_pc = dict(title="Data set C", counts=[4, 4, 4, 4, 4], labels=list("12345"))
_f = bars_fig("s2_bars", [_pa, _pb, _pc], 12)
def _spread_order():
    ds = {p_['title'][-1]: sum(([int(l) for _ in range(c)] for l, c in zip(p_['labels'], p_['counts'])), []) for p_ in (_pa, _pb, _pc)}
    return tuple(sorted(ds, key=lambda k: sd(ds[k])))
mc(2, 'H',
   r"Each bar graph shows a data set of 20 values, each value between 1 and 5. The number above a bar is how many times that value occurs." + _f + r"Which of the following lists the data sets in order from the smallest standard deviation to the largest?",
   T("A, C, B", ('A', 'C', 'B')), [T("A, B, C", ('A', 'B', 'C')), T("B, C, A", ('B', 'C', 'A')), T("C, A, B", ('C', 'A', 'B'))],
   _spread_order,
   "Skyrocket bar $\\Rightarrow$ small SD; double top $\\Rightarrow$ large SD",
   r"All three sets have mean $3$, so compare how far the values sit from $3$. In $A$ one tall bar at the center (a ``skyrocket'') means most values equal the mean: smallest SD. In $B$ the two tall bars sit at the far ends (a ``double top''): largest SD. $C$ is flat and in between. The order is $A,C,B$. ($C,A,B$ wrongly calls the flat graph the most concentrated; $B,C,A$ is the reverse order.)",
   order='free')

_o = [4, 6, 7, 7, 8, 9, 9, 10, 12]
_OS = {
    "The median increases by more than the mean does.": lambda d0, d1: median(d1) - median(d0) > mean(d1) - mean(d0),
    "The mean increases by more than the median does.": lambda d0, d1: mean(d1) - mean(d0) > median(d1) - median(d0),
    "The mean and the median increase by the same amount.": lambda d0, d1: mean(d1) - mean(d0) == median(d1) - median(d0),
    "The mean increases, but the median does not change.": lambda d0, d1: mean(d1) > mean(d0) and median(d1) == median(d0),
}
mc(2, 'H',
   r"A data set has 9 values: $4,\ 6,\ 7,\ 7,\ 8,\ 9,\ 9,\ 10,\ 12$. A tenth value, $45$, is added. Which statement is true about the effect on the mean and the median?",
   T("The mean increases by more than the median does."),
   [T("The median increases by more than the mean does."), T("The mean and the median increase by the same amount."), T("The mean increases, but the median does not change.")],
   None, "An outlier drags the mean far, the median barely",
   r"Before: sum $72$, mean $8$, median $8$. After: sum $117$, mean $11.7$ (up $3.7$). With $10$ values the median is the average of the 5th and 6th: $\frac{8+9}{2}=8.5$ (up only $0.5$). The extreme value pulls the mean a lot and the median a little. (The median does move, because an even count averages two middle values.)",
   order='free', each=lambda v: _OS[v](_o, _o + [45]))

_P = [10, 12, 14, 15, 15, 16, 18, 20]
_Q = [3, 14, 15, 15, 15, 15, 16, 27]
def _cmp(a, b):
    return 'greater' if a > b else ('less' if a < b else 'equal')
mc(2, 'H',
   r"Data set $P$ is $10,\ 12,\ 14,\ 15,\ 15,\ 16,\ 18,\ 20$. Data set $Q$ is $3,\ 14,\ 15,\ 15,\ 15,\ 15,\ 16,\ 27$. Both have 8 values and the same mean. Which statement is true?",
   T("$Q$ has the greater range and the smaller IQR.", ('greater', 'less')),
   [T("$Q$ has the greater range and the greater IQR.", ('greater', 'greater')), T("$Q$ has the smaller range and the smaller IQR.", ('less', 'less')),
    T("$Q$ has the smaller range and the greater IQR.", ('less', 'greater'))],
   lambda: (_cmp(rng(_Q), rng(_P)), _cmp(iqr(_Q), iqr(_P))),
   "Range sees the extremes, IQR sees the middle half",
   r"Ranges: $P$: $20-10=10$; $Q$: $27-3=24$. For the IQR split each set into halves: $P$ has $Q_1=13$, $Q_3=17$, IQR $4$; $Q$ has $Q_1=14.5$, $Q_3=15.5$, IQR $1$. The two extreme values stretch $Q$'s range, but the middle half of $Q$ is tightly packed. Range and IQR can disagree.",
   order='free')

_bx = [("Group X", 12, 18, 24, 30, 40), ("Group Y", 14, 20, 22, 25, 36)]
_f = box_fig("s2_box", _bx, 10, 40, 5, "Mass (kilograms)")
_BS = {
    "The mean of group X is greater than the mean of group Y.": lambda x_, y_: mean(x_) > mean(y_),
    "The IQR of group X is greater than the IQR of group Y.": lambda x_, y_: iqr(x_) > iqr(y_),
    "The range of group Y is greater than the range of group X.": lambda x_, y_: rng(y_) > rng(x_),
    "The median of group Y is greater than the median of group X.": lambda x_, y_: median(y_) > median(x_),
}
mc(2, 'H',
   r"The box plots summarize the masses of the animals in two groups." + _f + r"Based on the box plots, which of the following must be true?",
   T("The IQR of group X is greater than the IQR of group Y."),
   [T("The mean of group X is greater than the mean of group Y."), T("The range of group Y is greater than the range of group X."),
    T("The median of group Y is greater than the median of group X.")],
   None, "Box plots show median, quartiles, range, IQR: never the mean",
   r"Read the five numbers. $X$: IQR $=30-18=12$, range $28$, median $24$. $Y$: IQR $=25-20=5$, range $22$, median $22$. So only the IQR statement is true. The range of $Y$ is smaller and the median of $Y$ is smaller. A box plot cannot give the mean, so the first statement is not guaranteed.",
   order='free', each=lambda v: must_be_true(lambda x_, y_: _BS[v](x_, y_), [_bx[0][1:], _bx[1][1:]]))

gi(2, 'H',
   r"The mean annual salary of 10 employees at a small company is \$52,000. A new employee earning \$118,000 is hired. What is the mean annual salary, in dollars, of the 11 employees?",
   "58000", 58000, lambda: Fraction(10 * 52000 + 118000, 11),
   "Work with totals, not means",
   r"The old total is $10(52{,}000)=520{,}000$. Add the new salary: $638{,}000$. Divide by $11$: $58{,}000$. (Averaging $52{,}000$ and $118{,}000$ gives $85{,}000$, which ignores that ten employees share the old mean.)")

_dp = {4: 1, 5: 2, 6: 3, 7: 3, 8: 1, 12: 1}
_f = dots_fig("s2_dots", _dp, 3, 13, "Number of deliveries")
_dl = expand(_dp)
_dl2 = [22 if v == 12 else v for v in _dl]
def _changed():
    s_ = set()
    if mean(_dl) != mean(_dl2): s_.add('I')
    if median(_dl) != median(_dl2): s_.add('II')
    if rng(_dl) != rng(_dl2): s_.add('III')
    return s_
_CH = {"I only": {'I'}, "I and II only": {'I', 'II'}, "I and III only": {'I', 'III'}, "I, II and III": {'I', 'II', 'III'}}
mc(2, 'H',
   r"The dot plot shows the number of deliveries an office received each day for 11 days." + _f + r"The value $12$ was recorded in error and should have been $22$. Which of the following statistics changes when the data are corrected?" + "\n\n" + r"\quad I. The mean\quad II. The median\quad III. The range",
   T("I and III only"), [T("I only"), T("I and II only"), T("I, II and III")],
   None, "Which measure sees the corrected extreme value?",
   r"Sorted: $4,5,5,6,6,6,7,7,7,8,12$. The median is the 6th value, $6$, and stays $6$ after $12\to22$ (the order of the middle values does not change). The mean rises, since the total rises by $10$. The range rises from $12-4=8$ to $22-4=18$. So I and III change; II does not.",
   order='free', each=lambda v: _CH[v] == _changed())

_s9 = [25] * 6 + [35] * 6
mc(2, 'H',
   r"A data set of 12 values has a mean of 30 and a standard deviation of 5. A 13th value, equal to 30, is added. Which statement is true about the new data set?",
   T("The mean stays $30$, and the standard deviation decreases.", ('same', 'down')),
   [T("The mean stays $30$, and the standard deviation does not change.", ('same', 'same')), T("The mean stays $30$, and the standard deviation increases.", ('same', 'up')),
    T("The mean decreases, and the standard deviation decreases.", ('down', 'down'))],
   lambda: (_chg(float(mean(_s9)), float(mean(_s9 + [30]))), _chg(round(sd(_s9), 9), round(sd(_s9 + [30]), 9))),
   "A value at the center adds a data point but no spread",
   r"A new value equal to the mean adds $30$ to the total and $1$ to the count, so the mean stays $30$. But this value sits exactly at the center, closer to the mean than the other values, so the data become slightly more concentrated and the standard deviation decreases. (It does not stay the same just because the mean did.)",
   order='free')

gi(2, 'H',
   r"The mean of 9 recorded values is 41. One value was recorded as $7$ when it should have been $70$. What is the correct mean of the 9 values?",
   "48", 48, lambda: Fraction(9 * 41 - 7 + 70, 9),
   "Correct the total, then divide",
   r"The recorded total is $9(41)=369$. The error is $70-7=63$ too low, so the correct total is $369+63=432$. The correct mean is $432\div9=48$. (Adding $63$ to the mean itself is the usual slip; the mean rises by only $\frac{63}{9}=7$.)")

import random as _r
_rr = _r.Random(11)
_lists20 = [[_rr.randint(1, 60) for _ in range(20)] for _ in range(60)]
_S11 = {"II only": {'II'}, "I and II only": {'I', 'II'}, "II and III only": {'II', 'III'}, "I, II and III": {'I', 'II', 'III'}}
def _same11(d):
    d2 = sorted(d)
    d2[-1] += 50
    s_ = set()
    if mean(d) == mean(d2): s_.add('I')
    if median(d) == median(d2): s_.add('II')
    if iqr(d) == iqr(d2): s_.add('III')
    return s_
mc(2, 'H',
   r"A data set has 20 values. The greatest value is increased by $50$ (it remains the greatest). Which of the following statistics are unchanged?" + "\n\n" + r"\quad I. The mean\quad II. The median\quad III. The interquartile range (IQR)",
   T("II and III only"), [T("II only"), T("I and II only"), T("I, II and III")],
   None, "Resistant measures ignore the top value",
   r"The mean includes every value, so it rises by $\frac{50}{20}=2.5$. The median is the average of the 10th and 11th values and the IQR uses the middle of each half. None of those positions involve the greatest value, so II and III are unchanged. (The range would change too.)",
   order='free', each=lambda v: all(_S11[v] == _same11(d) for d in _lists20))

_hc = [5, 13, 8, 6, 5, 3]
_he = [0, 10, 20, 30, 40, 50, 60]
_f = hist_fig("s2_hist", _he, _hc, 15, 5, "Time (minutes)", "Frequency")
def _med_bin():
    cum, out = 0, []
    for j, c in enumerate(_hc):
        for _ in range(c): out.append(j)
    n = len(out)
    lo, hi = out[n // 2 - 1], out[n // 2]
    return "%d to %d" % (_he[lo], _he[lo + 1]) if lo == hi else None
mc(2, 'H',
   r"The histogram summarizes the times, in minutes, that 40 students spent on an assignment. Each bar includes its left endpoint but not its right." + _f + r"In which interval must the median time lie?",
   T("20 to 30", "20 to 30"), [T("10 to 20", "10 to 20"), T("30 to 40", "30 to 40"), T("40 to 50", "40 to 50")],
   _med_bin, "Median bin: count up to the middle position",
   r"With $40$ values the median is the average of the 20th and 21st. Running totals: $5,\ 18,\ 26,\ldots$ The first two bars hold only $18$ values, so the 20th and 21st values both fall in the third bar, $20$ to $30$. (The tallest bar, $10$ to $20$, is the mode interval, not the median interval.)",
   order='free')

gi(2, 'H',
   r"The smallest value in a data set is 7 and the largest value is 19. Each value is multiplied by $2.5$, and then $3$ is added. What is the range of the new data set?",
   "30", 30, lambda: (Rational(5, 2) * 19 + 3) - (Rational(5, 2) * 7 + 3),
   "Range scales like SD: shifts cancel",
   r"The original range is $19-7=12$. Adding $3$ moves everything equally, so it cancels in the range; multiplying by $2.5$ scales the range: $2.5\cdot12=30$. (Applying $2.5\cdot12+3=33$ adds the shift to a distance.)")

_A2, _B2 = [10, 12, 14, 16, 18], [30, 32, 34, 36, 38]
mc(2, 'H',
   r"Data set $A$ is $10,\ 12,\ 14,\ 16,\ 18$ and data set $B$ is $30,\ 32,\ 34,\ 36,\ 38$. The two sets are combined into one data set of 10 values. Which statement about the standard deviation of the combined set is true?",
   T("It is greater than the standard deviation of $A$ and greater than that of $B$.", 'greater'),
   [T("It is equal to the standard deviation of $A$ and of $B$.", 'equal'), T("It is less than the standard deviation of $A$ and of $B$.", 'less'),
    T("It is equal to the mean of the standard deviations of $A$ and $B$.", 'average')],
   lambda: 'greater' if sd(_A2 + _B2) > max(sd(_A2), sd(_B2)) else 'other',
   "Two separated clumps spread the combined data",
   r"$A$ and $B$ each consist of five evenly spaced values $2$ apart, so they have the same standard deviation. In the combined set the values run from $10$ to $38$, in two clumps far from the combined mean $24$. That is far more spread than either set alone, so the combined standard deviation is greater than both (it is not an average of the two).",
   order='free')

# ============================================================ SET 3  (Hard, 14)
_t31 = (4, 6, 2)
_f = tbl_fig("s3_t1", ["Value", "1", "2", "3", "4"], [["Frequency", 4, 6, "$x$", 2]])
gi(3, 'H',
   r"The table shows the frequency of each value in a data set. The mean of the data set is $2.5$." + _f + r"What is the value of $x$?",
   "12", 12,
   lambda: [x_ for x_ in range(1, 200) if mean(expand({1: 4, 2: 6, 3: x_, 4: 2})) == Rational(5, 2)][0],
   "Frequency table: total $=\\sum$ value $\\times$ frequency",
   r"The sum of the values is $1(4)+2(6)+3x+4(2)=24+3x$ and there are $12+x$ values. Set $\frac{24+3x}{12+x}=2.5$: $24+3x=30+2.5x$, so $0.5x=6$ and $x=12$. (Check: total $60$, count $24$, mean $2.5$.)")

_t32 = {"20--29": (20, 29, 4), "30--39": (30, 39, 6), "40--49": (40, 49, 10)}
_f = tbl_fig("s3_t2", ["Time (minutes)"] + list(_t32), [["Number of students"] + [v[2] for v in _t32.values()]])
def _min_mean():
    return Fraction(sum(lo * c for lo, hi, c in _t32.values()), 20)
mc(3, 'H',
   r"Twenty students recorded the time they spent on homework, rounded to a whole number of minutes, and the results were grouped as shown." + _f + r"What is the least possible value of the mean time of the 20 students?",
   C(33), [C(30), DEC("37.5"), C(42)],
   _min_mean,
   "Grouped data: least mean uses every class's lowest value",
   r"The least possible mean happens when every student is at the bottom of their class: $\frac{4(20)+6(30)+10(40)}{20}=\frac{660}{20}=33$. (Averaging the three lower ends, $30$, ignores the class sizes; $37.5$ uses class midpoints, which is an estimate rather than the least possible; $42$ is the greatest possible mean, using $29,39,49$.)")

_t33 = [(50, 59, 6), (60, 69, 4), (70, 79, 6), (80, 89, 4)]
_f = tbl_fig("s3_t3", ["Score"] + ["%d--%d" % (a, b) for a, b, c in _t33], [["Number of students"] + [c for a, b, c in _t33]])
gi(3, 'H',
   r"The scores of 20 students were grouped as shown. All scores are whole numbers." + _f + r"What is the greatest possible value of the median score?",
   "74", 74,
   lambda: median([hi for lo, hi, c in _t33 for _ in range(c)]),
   "Median of grouped data: locate the middle two positions",
   r"With $20$ scores the median is the average of the 10th and 11th. Running totals $6,\ 10,\ 16,\ 20$: the 10th score is the largest in the class $60$--$69$, and the 11th is the smallest position in the class $70$--$79$. Make both as large as possible: $69$ and $79$. The greatest median is $\frac{69+79}{2}=74$. (Taking class midpoints, or $79$, ignores that the two middle values sit in different classes.)")

mc(3, 'H',
   r"Three sections of a course took the same exam. Section 1 had 10 students with a mean score of 70, and Section 2 had 20 students with a mean score of 78. Section 3 had 20 students. The mean score of all 50 students was 80. What was the mean score of Section 3?",
   C(87), [C(92), C(80), DEC("34.8")],
   lambda: Fraction(80 * 50 - 10 * 70 - 20 * 78, 20),
   "Combined mean: add up the totals",
   r"All $50$ students scored $50(80)=4000$ points. Section 1 scored $10(70)=700$ and Section 2 scored $20(78)=1560$. Section 3 scored $4000-700-1560=1740$, so its mean is $1740\div20=87$. ($92=3(80)-70-78$ treats the three section means as equally weighted; $34.8=1740\div50$ divides by the wrong count; $80$ assumes Section 3 matches the overall mean.)")

_hh = {1: 18, 2: 30, 3: 22, 4: 20, 5: 6, 6: 4}
_f = tbl_fig("s3_t5", ["Household size"] + [str(k) for k in _hh], [["Percent of households"] + ["%d\\%%" % v for v in _hh.values()]])
def _med_pct():
    cum = 0
    for k, v in _hh.items():
        cum += v
        if cum >= 50: return k
mc(3, 'H',
   r"A survey reported the sizes of the households in a town, as shown in the table." + _f + r"What is the median household size?",
   C(3), [C(2), DEC("2.78"), DEC("3.5")],
   _med_pct,
   "Relative-frequency table: find where the running percent passes 50\\%",
   r"Add percents from the smallest size: $18\%$, then $48\%$ (still below $50\%$), then $70\%$. The $50$th percent is reached at size $3$, so the median is $3$. ($2$ is the mode, the most common size; $2.78$ is the mean; $3.5$ is the middle of the sizes $1$ to $6$, which ignores how many households have each size.)")

_xs = [11, 13, 15, 17, 19, 21, 22, 24, 26, 28]
_es = [2, -4, 3, -2, 4, -3, 2, -1, -5, 3]
_pts6 = [(x_, round(3.5 * x_ + 12 + e_)) for x_, e_ in zip(_xs, _es)]
_f = scat_fig("s3_sc6", _pts6, (10, 30), (40, 120), 5, 20, "Number of ads", "Sales (hundreds of dollars)")
_opts6 = {"$y=3.5x+12$": (3.5, 12), "$y=3.5x+50$": (3.5, 50), "$y=12x+3.5$": (12, 3.5), "$y=0.29x+12$": (0.29, 12)}
def _best_line():
    sse = {k: sum((y_ - (m_ * x_ + b_)) ** 2 for x_, y_ in _pts6) for k, (m_, b_) in _opts6.items()}
    k = min(sse, key=sse.get)
    return ('line',) + _opts6[k]
mc(3, 'H',
   r"A company recorded the number of ads it ran in a week, $x$, and its sales for the week, $y$, in hundreds of dollars. The scatterplot shows 10 weeks of data." + _f + r"Which of the following could be the equation of the line of best fit?",
   T("$y=3.5x+12$", ('line', 3.5, 12)), [T("$y=3.5x+50$", ('line', 3.5, 50)), T("$y=12x+3.5$", ('line', 12, 3.5)), T("$y=0.29x+12$", ('line', 0.29, 12))],
   _best_line,
   "Best-fit equation: slope from two spread-out points, intercept at $x=0$",
   r"The data rise about $70$ units over $20$ ads (for example from about $47$ at $x=10$ to about $117$ at $x=30$), so the slope is about $\frac{70}{20}=3.5$. The intercept is the value at $x=0$, not at the left edge of the graph: $47-3.5(10)=12$. So $y=3.5x+12$. ($y=3.5x+50$ reads the height at $x=10$ (about $50$) as the intercept; $y=12x+3.5$ swaps the coefficients; $0.29$ is run over rise.)",
   order='free')

mc(3, 'H',
   r"The line of best fit for the number of minutes of exercise $x$ and the calories burned $y$ is $y=1.8x+12$. A person exercised for 15 minutes and burned 34 calories. What is the residual for this person (actual value minus predicted value)?",
   C(-5), [C(5), C(22), C(39)],
   lambda: 34 - (Rational(9, 5) * 15 + 12),
   "Residual = actual $-$ predicted",
   r"Predicted: $1.8(15)+12=39$. Residual $=34-39=-5$: the actual value is $5$ below the line. ($+5$ reverses the subtraction; $22=34-12$ ignores the slope term; $39$ is the prediction itself, not a residual.)")

mc(3, 'H',
   r"A researcher measured the heights of trees between 5 and 20 years old and found the line of best fit $y=0.8x+14$, where $x$ is age in years and $y$ is height in feet. Which statement about using the model to estimate the height of a 50-year-old tree is best?",
   T("The model predicts $54$ feet, but $50$ years is far outside the ages in the data, so this prediction is an extrapolation and may be unreliable.", ('extrapolation', 54)),
   [T("The model predicts $54$ feet, and this is just as reliable as a prediction for a 12-year-old tree.", ('reliable', 54)),
    T("The model cannot make any prediction because $x=0$ is not in the data.", ('none', None)),
    T("The model predicts $14$ feet, because the intercept is the height at any age.", ('intercept', 14))],
   lambda: ('extrapolation', Rational(4, 5) * 50 + 14),
   "Prediction vs extrapolation",
   r"Substituting $x=50$ gives $0.8(50)+14=54$, so the model does give a number. But $50$ is far outside the observed ages ($5$ to $20$), so we cannot trust the linear pattern to continue: extrapolation. Predictions inside the data range are more trustworthy. Conceptual item (the number $54$ is checked).",
   order='free')

_pts9 = [(6, 15), (12, 12), (20, 23), (30, 26)]
mc(3, 'H',
   r"The line of best fit for a data set is $y=0.5x+10$. Which of the following data points is farthest from the line, measured vertically?",
   T("$(12,12)$", (12, 12)), [T("$(6,15)$", (6, 15)), T("$(20,23)$", (20, 23)), T("$(30,26)$", (30, 26))],
   lambda: max(_pts9, key=lambda p_: abs(p_[1] - (Rational(1, 2) * p_[0] + 10))),
   "Farthest from the line: largest residual in size, either sign",
   r"Predicted values: $13,\ 16,\ 20,\ 25$. Residuals (actual $-$ predicted): $+2,\ -4,\ +3,\ +1$. The largest in size is $|-4|=4$, at $(12,12)$, even though it is below the line. (Choosing the biggest positive residual gives $(20,23)$.)",
   order='free')

gi(3, 'H',
   r"An exponential model $y=a\cdot b^{t}$, where $a$ and $b$ are positive constants, passes through the points $(1,\ 48)$ and $(3,\ 108)$. According to the model, what is the value of $y$ when $t=5$?",
   "243", 243,
   lambda: [Rational(48) / b_ * b_ ** 5 for b_ in [Rational(3, 2), Rational(-3, 2)] if b_ > 0 and 48 / b_ * b_ ** 3 == 108][0],
   "Exponential model: equal steps multiply by the same factor",
   r"Going from $t=1$ to $t=3$ (two steps) multiplies $y$ by $\frac{108}{48}=2.25=b^2$, so $b=1.5$. Going two more steps multiplies by $2.25$ again: $108\cdot2.25=243$. (Adding the same difference, $108+60=168$, treats the model as linear.)")

mc(3, 'H',
   r"A line of best fit for the fuel used, $y$ (in gallons), on trips of $x$ miles is $y=0.04x+1.2$. Which of the following is the best interpretation of the number $0.04$ in this context?",
   T("The model predicts $0.04$ additional gallon of fuel for each additional mile driven.", ('gallons per mile', Rational(1, 25))),
   [T("The car travels $0.04$ mile on each gallon of fuel.", ('miles per gallon', Rational(1, 25))),
    T("The model predicts $0.04$ gallon of fuel for a trip of $1.2$ miles.", ('at 1.2 miles', Rational(1, 25))),
    T("Every mile driven uses exactly $0.04$ gallon of fuel.", ('exactly', Rational(1, 25)))],
   lambda: ('gallons per mile', (Rational(1, 25) * 1 + Rational(6, 5)) - (Rational(1, 25) * 0 + Rational(6, 5))),
   "Slope units: ($y$ units) per ($x$ unit)",
   r"The slope is the predicted change in $y$ (gallons) for one more unit of $x$ (mile): $0.04$ gallon per mile. It is gallons per mile, not miles per gallon (that would be $\frac1{0.04}=25$), and a line of best fit gives predicted averages, not exact usage.",
   order='free')

_t12 = [(0, 3), (1, 6), (2, 12), (3, 25), (4, 47)]
_f = tbl_fig("s3_t12", ["$x$"] + [str(a) for a, b in _t12], [["$y$"] + [b for a, b in _t12]])
_opts12 = {"$y=11x+3$": lambda x_: 11 * x_ + 3, "$y=3(2)^x$": lambda x_: 3 * 2 ** x_, "$y=3x^2+3$": lambda x_: 3 * x_ ** 2 + 3, "$y=3(1.5)^x$": lambda x_: 3 * 1.5 ** x_}
def _best12():
    sse = {k: sum((b_ - f_(a_)) ** 2 for a_, b_ in _t12) for k, f_ in _opts12.items()}
    return min(sse, key=sse.get)
mc(3, 'H',
   r"The table gives five measurements of two variables." + _f + r"Which of the following equations best models the relationship?",
   T("$y=3(2)^x$"), [T("$y=11x+3$"), T("$y=3x^2+3$"), T("$y=3(1.5)^x$")],
   _best12,
   "Table: constant ratio means exponential, constant difference means linear",
   r"Look at consecutive ratios: $\frac63=2,\ \frac{12}6=2,\ \frac{25}{12}\approx2.1,\ \frac{47}{25}\approx1.9$. The ratios are nearly constant, so the data grow exponentially with $b=2$ and $a=3$ (the value at $x=0$). The differences $3,6,13,22$ are not constant, so it is not linear. $y=3(2)^x$ gives $3,6,12,24,48$, which is within $1$ of every value.",
   order='free')

gi(3, 'H',
   r"A line of best fit for the percent $y$ of a phone's battery remaining after $x$ hours of use passes through the points $(1,\ 78)$ and $(4,\ 33)$. According to the model, after how many hours of use will the battery reach $0\%$?",
   "6.2", Rational(31, 5),
   lambda: [x_ for x_ in [Rational(k, 10) for k in range(0, 200)] if (78 + Rational(33 - 78, 4 - 1) * (x_ - 1)) == 0][0],
   "Line through two points: slope, then solve for $y=0$",
   r"Slope $=\frac{33-78}{4-1}=-15$ percentage points per hour. So $y=78-15(x-1)=93-15x$. Set $y=0$: $x=\frac{93}{15}=6.2$ hours. (Dividing $78$ by $15$ forgets the offset of the first point.)")

_pts14 = [(1, 7), (2, 9), (3, 12), (4, 13), (5, 16), (6, 17), (7, 20), (8, 21), (9, 4)]
_f = scat_fig("s3_sc14", _pts14, (0, 10), (0, 24), 1, 4, "$x$", "$y$")
def _chg14():
    m1, b1 = lsq(_pts14)
    m0, b0 = lsq(_pts14[:-1])
    return ('increases' if m0 > m1 else 'decreases', 'increases' if b0 > b1 else 'decreases')
mc(3, 'H',
   r"The scatterplot shows nine data points, and a line of best fit is calculated for all nine." + _f + r"The point $(9,4)$ is removed, and the line of best fit is calculated again for the remaining eight points. Which statement describes the new line compared with the old one?",
   T("The slope increases, and the $y$-intercept decreases.", ('increases', 'decreases')),
   [T("The slope increases, and the $y$-intercept increases.", ('increases', 'increases')), T("The slope decreases, and the $y$-intercept decreases.", ('decreases', 'decreases')),
    T("The slope decreases, and the $y$-intercept increases.", ('decreases', 'increases'))],
   _chg14,
   "A far-away point tilts the line toward itself",
   r"Eight points climb steadily (about $2$ per unit of $x$). The last point $(9,4)$ is far to the right and far below the trend, so it drags the right end of the line down: the line with it is flatter. Removing it lets the line steepen, and a steeper line pivoting near the middle of the data must start lower: the $y$-intercept decreases. (Least-squares fits give a slope of about $0.7$ with the point and $2.0$ without it.)",
   order='free')

# ============================================================ SET 4  (Hard, 14)
_f = tbl_fig("s4_t1", ["Age group", "Prefers coffee", "Prefers tea"],
             [["Under 30", 24, 6], ["30 to 59", 40, 14], ["60 or older", 21, "$x$"]])
gi(4, 'H',
   r"A café asked its customers which hot drink they prefer. The results are shown in the table." + _f + r"If one of the customers who prefer tea is chosen at random, the probability that the customer is 60 or older is $\dfrac13$. What is the value of $x$?",
   "10", 10,
   lambda: [x_ for x_ in range(1, 500) if Fraction(x_, 6 + 14 + x_) == Fraction(1, 3)][0],
   "Reverse conditional: the ``given'' column is the denominator",
   r"Customers who prefer tea total $6+14+x=20+x$, and $x$ of them are $60$ or older: $\frac{x}{20+x}=\frac13$. Cross-multiply: $3x=20+x$, so $x=10$. (Do not use the whole table as the denominator: the condition is ``prefers tea''.)")

_gym = {"Under 30": (96, 64), "30 or older": (84, 256)}
_f = tbl_fig("s4_t2", ["", "Gym member", "Not a member", "Total"],
             [[k, v[0], v[1], sum(v)] for k, v in _gym.items()] + [["Total", 180, 320, 500]])
mc(4, 'H',
   r"A gym surveyed 500 adults about their age and whether they are gym members." + _f + r"If one of the gym members is chosen at random, what is the probability that this person is under 30?",
   FR(8, 15), [FR(24, 125), FR(8, 25), FR(3, 5)],
   lambda: Fraction(96, 96 + 84),
   "Reverse conditionals: $P(A\\mid B)\\ne P(B\\mid A)$",
   r"The condition is ``is a member'', so use the member column: $96+84=180$ members, of whom $96$ are under $30$: $\frac{96}{180}=\frac8{15}$. ($\frac35=\frac{96}{160}$ is the reverse: the chance that an under-30 person is a member; $\frac{24}{125}=\frac{96}{500}$ divides by everyone; $\frac8{25}=\frac{160}{500}$ is just the share who are under $30$.)")

_f = tbl_fig("s4_t3", ["", "In a club", "Not in a club"], [["Seniors", 18, "$x$"], ["Not seniors", 42, 140]])
gi(4, 'H',
   r"A school counselor recorded whether students are seniors and whether they belong to a club." + _f + r"For these students, being a senior and being in a club are independent. What is the value of $x$?",
   "60", 60,
   lambda: [x_ for x_ in range(1, 1000) if Fraction(18, 18 + x_) == Fraction(42, 42 + 140)][0],
   "Independence from a table: the conditional rates match",
   r"Independent means the club rate is the same for seniors and non-seniors: $\frac{18}{18+x}=\frac{42}{42+140}=\frac{3}{13}$. Then $13(18)=3(18+x)$, so $234=54+3x$ and $x=60$. (Check: the overall club rate is $\frac{18+42}{260}=\frac3{13}$, the same as in each group.)")

_bag = ['R'] * 5 + ['B'] * 3
def _atleastone():
    from itertools import permutations
    prs = list(permutations(range(8), 2))
    good = sum(1 for a_, b_ in prs if _bag[a_] == 'B' or _bag[b_] == 'B')
    return Fraction(good, len(prs))
mc(4, 'H',
   r"A bag contains 5 red marbles and 3 blue marbles. Two marbles are drawn at random, one after the other, without replacement. What is the probability that at least one of the two marbles is blue?",
   FR(9, 14), [FR(39, 64), FR(3, 8), FR(5, 14)],
   _atleastone,
   "At least one = 1 $-$ none (and update the bag)",
   r"The opposite event is ``both red'': $\frac58\cdot\frac47=\frac5{14}$ (after one red is removed, $4$ red remain among $7$). So the answer is $1-\frac5{14}=\frac9{14}$. ($\frac{39}{64}=1-(\frac58)^2$ pretends the first marble is put back; $\frac3{8}$ counts only the first draw; $\frac5{14}$ is the chance of no blue.)")

_deck = ['R'] * 4 + ['K'] * 6
def _same_color():
    from itertools import permutations
    prs = list(permutations(range(10), 2))
    return Fraction(sum(1 for a_, b_ in prs if _deck[a_] == _deck[b_]), len(prs))
mc(4, 'H',
   r"A box holds 4 red cards and 6 black cards. Two cards are drawn at random without replacement. What is the probability that the two cards are the same color?",
   FR(7, 15), [FR(13, 25), FR(1, 3), FR(8, 15)],
   _same_color,
   "Without replacement: shrink the pool after each draw",
   r"Both red: $\frac4{10}\cdot\frac39=\frac2{15}$. Both black: $\frac6{10}\cdot\frac59=\frac13=\frac5{15}$. Add: $\frac2{15}+\frac5{15}=\frac7{15}$. ($\frac{13}{25}=0.4^2+0.6^2$ allows replacement; $\frac13$ is only the both-black case; $\frac8{15}$ is the chance the colors differ.)")

gi(4, 'H',
   r"A quality inspector checks items one at a time. Each item independently has a $10\%$ chance of being defective. What is the least number of items the inspector must check so that the probability of finding at least one defective item is greater than $50\%$?",
   "7", 7,
   lambda: [n_ for n_ in range(1, 100) if 1 - Rational(9, 10) ** n_ > Rational(1, 2)][0],
   "At least one: $1-0.9^n$",
   r"The probability of no defective item among $n$ checks is $0.9^n$, so we need $1-0.9^n>0.5$, i.e. $0.9^n<0.5$. Try values: $0.9^6\approx0.531$ (too big) and $0.9^7\approx0.478$. So $n=7$. (A common guess is $5$, from $5\times10\%=50\%$, but chances do not simply add.)")

mc(4, 'H',
   r"At a school, $55\%$ of the students are in grades 9 and 10, and the rest are in grades 11 and 12. Of the students in grades 9 and 10, $30\%$ take an AP course; of the students in grades 11 and 12, $60\%$ take an AP course. What fraction of the students who take an AP course are in grades 9 and 10?",
   FR(11, 29), [FR(3, 10), FR(33, 200), FR(11, 20)],
   lambda: Fraction(55 * 30, 55 * 30 + 45 * 60),
   "Reverse conditional with percents: build the two parts, divide by the AP total",
   r"Out of $100$ students: AP in grades 9--10: $0.30\cdot55=16.5$; AP in grades 11--12: $0.60\cdot45=27$. AP total $=43.5$. Fraction $=\frac{16.5}{43.5}=\frac{11}{29}$. ($\frac3{10}$ is the AP rate within grades 9--10, the reverse question; $\frac{33}{200}=0.165$ is the share of all students; $\frac{11}{20}=0.55$ is the share of students in grades 9--10.)")

mc(4, 'H',
   r"In a town of 6,000 residents, $35\%$ own a bicycle. Of the residents who own a bicycle, $40\%$ also own a helmet. About how many of the residents own both a bicycle and a helmet?",
   C(840), [C(2100), C(2400), C(4500)],
   lambda: Rational(6000) * Rational(35, 100) * Rational(40, 100),
   "Expected count: multiply the chain of proportions",
   r"The $40\%$ applies to bicycle owners, not to everyone: $0.35\cdot0.40=0.14$ of the town, and $0.14\cdot6000=840$. ($2100=0.35\cdot6000$ counts all bicycle owners; $2400=0.40\cdot6000$ applies $40\%$ to everyone; $4500=0.75\cdot6000$ adds the percents.)")

mc(4, 'H',
   r"Researchers recruited 120 volunteers from a town and randomly assigned 60 of them to follow a new sleep schedule and 60 to keep their usual schedule. After eight weeks the reaction times of the new-schedule group were faster, by an amount too large to be explained by chance. Which conclusion is best supported?",
   T("The new sleep schedule caused faster reaction times for people like these volunteers, but the result cannot be generalized to all residents of the town.", ('cause', 'volunteers')),
   [T("The new sleep schedule caused faster reaction times for all residents of the town.", ('cause', 'town')),
    T("The new sleep schedule is associated with faster reaction times, but the study cannot show that it caused them.", ('association', 'volunteers')),
    T("No conclusion can be drawn, because the volunteers were not a random sample of the town.", ('none', None))],
   lambda: ('cause', 'volunteers'),
   "Random assignment gives cause; only random sampling gives generalization",
   r"Random assignment of the volunteers to the two groups makes the groups comparable, so a large difference can be attributed to the schedule (cause). But the volunteers were not randomly chosen from the town, so the result applies only to people like them. (Causation for the town needs random sampling; ``association only'' ignores the random assignment.) Conceptual item.",
   order='free')

mc(4, 'H',
   r"A researcher selected a random sample of 500 adults from a city and asked each whether they eat breakfast every day. The researcher also measured each adult's body mass index (BMI) and found that the adults who eat breakfast daily had a lower mean BMI than those who do not. Which conclusion is best supported?",
   T("There is an association between eating breakfast daily and lower BMI among the city's adults, but the study cannot show that breakfast causes lower BMI.", ('association', 'city')),
   [T("Eating breakfast daily causes lower BMI among the city's adults.", ('cause', 'city')),
    T("There is an association between eating breakfast and BMI among the 500 adults only, and it cannot be generalized to the city.", ('association', 'sample')),
    T("Eating breakfast daily is associated with lower BMI among all adults in the country.", ('association', 'country'))],
   lambda: ('association', 'city'),
   "Random sample generalizes; no random assignment means no cause",
   r"The sample was random, so the finding applies to the city's adults. Nobody was randomly assigned to eat or skip breakfast, so other factors (exercise, income, sleep) could explain the difference: an association, not a cause. Conceptual item.",
   order='free')

_p, _q, _moe = 48, 45, 4
mc(4, 'H',
   r"A poll of a random sample of voters in a city estimated that $48\%$ support Candidate $P$ and $45\%$ support Candidate $Q$. The margin of error for each estimate is $4$ percentage points. Which of the following is best supported by these results?",
   T("It is plausible that Candidate $Q$ has at least as much support as Candidate $P$ among all voters in the city.", 'overlap'),
   [T("Candidate $P$ has more support than Candidate $Q$ among all voters in the city.", 'P ahead'),
    T("Exactly $45\\%$ of all voters in the city support Candidate $Q$.", 'exact'),
    T("Candidate $P$ leads Candidate $Q$ by exactly $3$ percentage points among all voters in the city.", 'lead')],
   lambda: 'overlap' if (_p - _moe) <= (_q + _moe) else 'P ahead',
   "Overlapping intervals: cannot separate the two",
   r"Plausible values for $P$ are $44\%$ to $52\%$ and for $Q$ are $41\%$ to $49\%$. The intervals overlap (for example both could be $46\%$), so the poll cannot show that $P$ is ahead. The sample difference of $3$ points is real in the sample only. (Exact statements about the whole city are never justified by a sample.)",
   order='free')

mc(4, 'H',
   r"A random sample of 400 people gives a poll a margin of error of 5 percentage points. A second poll of the same population uses a random sample of 1,600 people, with the same method and confidence level. Which is the most likely margin of error of the second poll?",
   DEC("2.5"), [DEC("1.25"), C(5), C(10)],
   lambda: Rational(round(5 * math.sqrt(400 / 1600) * 100), 100),
   "Margin of error shrinks with the square root of the sample size",
   r"The margin of error is proportional to $\frac1{\sqrt n}$. Quadrupling the sample size ($1600=4\cdot400$) divides it by $\sqrt4=2$: $\frac52=2.5$. ($1.25$ divides by $4$, treating it as proportional to $\frac1n$; $5$ ignores the larger sample; $10$ moves the wrong way.)")

mc(4, 'H',
   r"To estimate the percent of adult residents of a city who exercise regularly, a researcher posted a survey on the website of a large fitness gym in the city. Of the 1,500 visitors who responded, $81\%$ said they exercise regularly. Which is the most serious flaw in using the $81\%$ to estimate the percent for all adult residents?",
   T("The respondents were not a random sample of the city, and visitors to a gym's website are more likely to exercise, so the estimate is probably too high.", 'bias'),
   [T("A sample of 1,500 is too small to estimate anything about a city.", 'size'),
    T("The result is too high to be believable, so the survey must contain errors.", 'high'),
    T("The researcher did not survey children as well as adults.", 'children')],
   lambda: 'bias',
   "Sampling bias: who could answer?",
   r"The flaw is how the sample was chosen: self-selected visitors of a gym site are not representative of all adults, and they tend to exercise more, so the result is biased upward. A larger sample would not fix this. $1{,}500$ is a perfectly adequate size for a random sample, and the question was about adults, so children are irrelevant. Conceptual item.",
   order='free')

gi(4, 'H',
   r"A researcher estimated the percent of a town's residents who own a car. To estimate the margin of error, she simulated 1,000 random samples; the middle $95\%$ of the simulated sample percents ranged from $41\%$ to $55\%$. What is the margin of error, in percentage points, for her estimate?",
   "7", 7, lambda: Rational(55 - 41, 2),
   "Margin of error = half the width of the interval",
   r"The interval $41\%$ to $55\%$ is centered on the estimate ($48\%$), and the margin of error is the distance from the center to either end: $\frac{55-41}{2}=7$ percentage points. (The full width, $14$, is twice the margin of error.)")

# ============================================================ SET 5  (Summit, 20)
_P1 = [40, 45, 50, 55, 58, 60, 60, 62, 65, 70, 75, 80]
_Q1 = _P1 + [60, 60]
def _chs(a, b):
    s_ = set()
    if mean(a) != mean(b): s_.add('mean')
    if median(a) != median(b): s_.add('median')
    if rng(a) != rng(b): s_.add('range')
    if round(sd(a), 9) != round(sd(b), 9): s_.add('sd')
    return s_
_S51 = {
    "Only the standard deviation changes, and it decreases.": lambda a, b: _chs(a, b) == {'sd'} and sd(b) < sd(a),
    "None of the mean, median, range or standard deviation changes.": lambda a, b: _chs(a, b) == set(),
    "The mean and the standard deviation both decrease; the median and range stay the same.": lambda a, b: _chs(a, b) == {'mean', 'sd'},
    "The range and the standard deviation both decrease; the mean and median stay the same.": lambda a, b: _chs(a, b) == {'range', 'sd'},
}
mc(5, 'H',
   r"Data set $P$ has 12 values: 40, 45, 50, 55, 58, 60, 60, 62, 65, 70, 75, 80. Data set $Q$ is formed by adding two more values, both equal to $60$, to data set $P$. Which statement is true?",
   T("Only the standard deviation changes, and it decreases."),
   [T("None of the mean, median, range or standard deviation changes."),
    T("The mean and the standard deviation both decrease; the median and range stay the same."),
    T("The range and the standard deviation both decrease; the mean and median stay the same.")],
   None, "A value at the center changes the SD but not mean, median or range",
   r"$P$ is symmetric about $60$: its mean and median are both $60$, and its range is $80-40=40$. The two new values equal $60$, so the mean stays $60$, the median stays $60$ (the middle of the sorted list), and the extremes $40$ and $80$ are unchanged, so the range stays $40$. The new values sit exactly at the center, so the data are more concentrated: the standard deviation decreases.",
   order='free', each=lambda v: _S51[v](_P1, _Q1))

def _brute52():
    best = 0
    for a_ in range(1, 11):
        for b_ in range(a_, 11):
            for d_ in range(10, 61):
                e_ = 60 - a_ - b_ - 10 - d_
                if e_ < d_:
                    continue
                l_ = [a_, b_, 10, d_, e_]
                c_ = {v: l_.count(v) for v in set(l_)}
                top = max(c_.values())
                modes = [v for v, k in c_.items() if k == top]
                if modes == [8] and median(l_) == 10 and mean(l_) == 12:
                    best = max(best, e_)
    return best
gi(5, 'H',
   r"Five positive integers have a mean of 12, a median of 10 and a unique mode of 8. What is the greatest possible value of the largest of the five integers?",
   "23", 23, _brute52,
   "Build the list from the constraints",
   r"The total is $5\cdot12=60$. A mode of $8$ means $8$ appears at least twice, and with median $10$ both $8$'s are below the middle: $8,8,10,d,e$. To make $e$ as large as possible, make $d$ as small as possible. But $d\ge10$, and $d=10$ would make $10$ appear twice, tying with $8$ (the mode would not be unique), so $d=11$. Then $e=60-8-8-10-11=23$. (The tempting $d=10$ gives $24$.)")

_seen = [12, 15, 15, 18, 22, 25, 27]
gi(5, 'H',
   r"Data set $D$ consists of 8 positive integers, each less than 40. Seven of them are $12,\ 15,\ 15,\ 18,\ 22,\ 25,\ 27$. The mean of all 8 integers is an integer greater than 18. What is the greatest possible value of the eighth integer?",
   "34", 34,
   lambda: max(x_ for x_ in range(1, 40) if mean(_seen + [x_]).denominator == 1 and mean(_seen + [x_]) > 18),
   "Integer mean: the total must be divisible by the count",
   r"The seven shown values sum to $134$. If the eighth value is $x$, the mean $\frac{134+x}{8}$ must be an integer, so $134+x$ is a multiple of $8$: $136,144,152,160,168,\ldots$, giving $x=2,10,18,26,34$. The mean must exceed $18$, so $134+x>144$, which allows $x=18,26,34$. All are below $40$; the greatest is $34$.")

_t54 = [(10, 19, 4), (20, 29, 9), (30, 39, 7), (40, 49, 5)]
_f = tbl_fig("s5_t4", ["Value"] + ["%d--%d" % (a, b) for a, b, c in _t54], [["Frequency"] + [c for a, b, c in _t54]])
gi(5, 'H',
   r"A data set of 25 integers is summarized in the table, where each integer lies in the class shown." + _f + r"What is the difference between the greatest possible mean and the least possible mean of the data set?",
   "9", 9,
   lambda: mean([hi for lo, hi, c in _t54 for _ in range(c)]) - mean([lo for lo, hi, c in _t54 for _ in range(c)]),
   "Grouped integers: every value can move by (class width $-1$)",
   r"The greatest mean puts every value at the top of its class and the least puts every value at the bottom. Each value differs between the two cases by $19-10=9$ (the same for every class), so the means differ by exactly $9$, whatever the frequencies. (Using $10$, the class width, forgets that integers in $10$--$19$ span only $9$ units.)")

_bx5 = [("Group X", 10, 16, 22, 34, 52), ("Group Y", 8, 20, 26, 30, 44)]
_f = box_fig("s5_box", _bx5, 0, 60, 10, "Score")
_B5 = {
    "At least $25\\%$ of the values in group $X$ are greater than or equal to $34$.": lambda x_, y_: 4 * sum(1 for v in x_ if v >= 34) >= len(x_),
    "The IQR of group $Y$ is greater than the IQR of group $X$.": lambda x_, y_: iqr(y_) > iqr(x_),
    "More than half of the values in group $Y$ are less than $26$.": lambda x_, y_: 2 * sum(1 for v in y_ if v < 26) > len(y_),
    "The mean of group $X$ is greater than the mean of group $Y$.": lambda x_, y_: mean(x_) > mean(y_),
}
mc(5, 'H',
   r"The box plots summarize the scores of two groups of students on the same test." + _f + r"Based on the box plots, which of the following must be true?",
   T("At least $25\\%$ of the values in group $X$ are greater than or equal to $34$."),
   [T("The IQR of group $Y$ is greater than the IQR of group $X$."), T("More than half of the values in group $Y$ are less than $26$."),
    T("The mean of group $X$ is greater than the mean of group $Y$.")],
   None, "Quartiles cut the data into quarters: use the percent meaning",
   r"The third quartile is $34$, so at least a quarter of the values are at or above it: true. The IQRs are $34-16=18$ for $X$ and $30-20=10$ for $Y$, so $Y$'s is smaller. The median of $Y$ is $26$, so at most half the values are below $26$, never more than half. The means cannot be read from box plots. (The percent facts about quartiles, not the shape of the box, decide each statement.)",
   order='free', each=lambda v: must_be_true(lambda x_, y_: _B5[v](x_, y_), [_bx5[0][1:], _bx5[1][1:]]))

_pts56 = [(2, 16), (5, 12), (8, 31), (11, 28)]
_lab = list("PQRS")
_f = scat_fig("s5_sc6", _pts56, (0, 12), (0, 40), 2, 5, "$x$", "$y$", line=(2, 10), labels=_lab)
mc(5, 'H',
   r"The scatterplot shows four labeled points and the line of best fit, $y=2x+10$." + _f + r"For which point is the residual (actual value minus predicted value) the least?",
   T("Point $Q$", 'Q'), [T("Point $P$", 'P'), T("Point $R$", 'R'), T("Point $S$", 'S')],
   lambda: _lab[min(range(4), key=lambda i: _pts56[i][1] - (2 * _pts56[i][0] + 10))],
   "Residual sign: below the line is negative",
   r"Predicted values at $x=2,5,8,11$: $14,\ 20,\ 26,\ 32$. Residuals: $P$: $16-14=+2$; $Q$: $12-20=-8$; $R$: $31-26=+5$; $S$: $28-32=-4$. The least residual is the most negative, $-8$ at $Q$. ($R$ has the greatest residual; $P$ is closest to the line.)",
   order='free')

gi(5, 'H',
   r"Of 10,000 items produced in a factory, 200 are defective. A scanner flags 180 of the 200 defective items and also flags 490 of the 9,800 items that are not defective. Of all the items the scanner flags, what percent are defective? (Round to the nearest whole percent.)",
   "27", 27, lambda: round(Fraction(180, 180 + 490) * 100),
   "Reverse conditional: the flagged group is the denominator",
   r"Flagged items: $180+490=670$. Defective among them: $180$. So $\frac{180}{670}\approx0.269$, about $27\%$. (The scanner catches $\frac{180}{200}=90\%$ of defective items, but that is the reverse question; most flagged items are false alarms because good items are so numerous.)")

_cl = {"Freshmen": (28, 36, 16), "Sophomores": (40, 24, 26), "Juniors": (12, 30, 18)}
_cols = ["Online", "In person", "Hybrid"]
_f = tbl_fig("s5_t8", [""] + _cols + ["Total"], [[k] + list(v) + [sum(v)] for k, v in _cl.items()] + [["Total"] + [sum(v[i] for v in _cl.values()) for i in range(3)] + [230]])
def _tot(i):
    return sum(v[i] for v in _cl.values())
_P8 = {
    "The probability that a randomly chosen student who prefers in-person classes is a junior": Fraction(_cl["Juniors"][1], _tot(1)),
    "The probability that a randomly chosen junior prefers online classes": Fraction(_cl["Juniors"][0], sum(_cl["Juniors"])),
    "The probability that a randomly chosen sophomore prefers hybrid classes": Fraction(_cl["Sophomores"][2], sum(_cl["Sophomores"])),
    "The probability that a randomly chosen student who prefers online classes is a freshman": Fraction(_cl["Freshmen"][0], _tot(0)),
}
mc(5, 'H',
   r"A college asked 230 students about their year and the class format (online, in person or hybrid) they prefer." + _f + r"Which of the following probabilities is the greatest?",
   T("The probability that a randomly chosen student who prefers online classes is a freshman"),
   [T("The probability that a randomly chosen student who prefers in-person classes is a junior"), T("The probability that a randomly chosen junior prefers online classes"),
    T("The probability that a randomly chosen sophomore prefers hybrid classes")],
   None, "Name the ``given'' group, then divide by its total",
   r"Divide by the group named after ``who'' or ``given'': in person and junior: $\frac{30}{90}=\frac13$; junior and online: $\frac{12}{60}=\frac15$; sophomore and hybrid: $\frac{26}{90}=\frac{13}{45}\approx0.289$; online and freshman: $\frac{28}{80}=\frac7{20}=0.35$. The greatest is $0.35$. (The biggest cell, $40$, is not in any option; large counts do not mean large probabilities.)",
   order='free', each=lambda v: _P8[v] == max(_P8.values()))

_bag9 = ['R'] * 5 + ['B'] * 4 + ['G'] * 3
def _same9():
    from itertools import permutations
    prs = list(permutations(range(12), 2))
    return Fraction(sum(1 for a_, b_ in prs if _bag9[a_] == _bag9[b_]), len(prs))
mc(5, 'H',
   r"A bag contains 5 red, 4 blue and 3 green marbles. Two marbles are drawn at random without replacement. What is the probability that both marbles are the same color?",
   FR(19, 66), [FR(5, 33), FR(25, 72), FR(19, 33)],
   _same9,
   "Without replacement: add the color cases, each with a shrinking pool",
   r"Red: $\frac5{12}\cdot\frac4{11}=\frac{20}{132}$. Blue: $\frac4{12}\cdot\frac3{11}=\frac{12}{132}$. Green: $\frac3{12}\cdot\frac2{11}=\frac6{132}$. Total $\frac{38}{132}=\frac{19}{66}$. ($\frac5{33}$ counts only red; $\frac{25}{72}=\frac{50}{144}$ puts each marble back; $\frac{19}{33}$ forgets to reduce the total, i.e. doubles it.)")

mc(5, 'H',
   r"A random sample of 100 voters gives a poll a margin of error of 9 percentage points. Assuming the same method and confidence level, what is the least sample size that would reduce the margin of error to 3 percentage points?",
   C(900), [C(300), C(600), C(8100)],
   lambda: 100 * (9 // 3) ** 2,
   "Margin of error $\\propto 1/\\sqrt{n}$: divide by $k$, multiply $n$ by $k^2$",
   r"To cut the margin of error to one third, the sample size must be multiplied by $3^2=9$: $100\cdot9=900$. ($300$ treats the margin as inversely proportional to $n$; $600$ subtracts; $8{,}100$ squares the nine.)")

mc(5, 'H',
   r"Researchers randomly selected 300 students from a school district of 12,000 students and randomly assigned 150 of them to tutoring method 1 and 150 to tutoring method 2. After a semester the method 1 group scored higher, by an amount too large to be explained by chance. Which conclusion is best supported?",
   T("Method 1 caused higher scores among the students in the district.", ('cause', 'district')),
   [T("Method 1 caused higher scores, but only for the 300 students in the study.", ('cause', 'sample')),
    T("Method 1 is associated with higher scores among the students in the district, but the study cannot show a cause.", ('association', 'district')),
    T("Method 1 caused higher scores among all students in the country.", ('cause', 'country'))],
   lambda: ('cause', 'district'),
   "Random sample AND random assignment: cause for the whole population",
   r"Both features are present. Random selection from the district lets us generalize to all $12{,}000$ students; random assignment to the two methods lets us attribute the difference to the method. (Restricting to the $300$ ignores the random sample; ``association only'' ignores the random assignment; the whole country was never sampled.) Conceptual item.",
   order='free')

_a, _b = (58, 4), (49, 3)
mc(5, 'H',
   r"Two independent polls used random samples. In City $A$, $58\%$ of the sample favored a proposal, with a margin of error of $4$ percentage points. In City $B$, $49\%$ of the sample favored it, with a margin of error of $3$ percentage points. Which conclusion is best supported?",
   T("The intervals $54\\%$ to $62\\%$ and $46\\%$ to $52\\%$ do not overlap, so it is reasonable to conclude that the percent in favor is greater among all residents of City $A$ than among all residents of City $B$.", 'support'),
   [T("The percent in favor among all residents of City $A$ is exactly $9$ points greater than among all residents of City $B$.", 'exact'),
    T("No comparison is possible, because the two polls have different margins of error.", 'none'),
    T("It is plausible that $54\\%$ of all residents of City $B$ are in favor.", 'plausibleB')],
   lambda: 'support' if (_a[0] - _a[1]) > (_b[0] + _b[1]) else 'other',
   "Compare confidence intervals: no overlap supports a difference",
   r"The intervals are $58\pm4=54$ to $62$ and $49\pm3=46$ to $52$. They do not overlap (the top of $B$'s, $52$, is below the bottom of $A$'s, $54$), so the data support a higher percent in $A$. The $9$-point gap is only a sample difference; margins of error can differ and the intervals can still be compared; $54\%$ lies outside $B$'s interval. Conceptual item (interval overlap is computed).",
   order='free')

gi(5, 'H',
   r"A poll of a random sample of residents estimated that $40\%$ of the town's 12,000 residents support a new park. The margin of error is 5 percentage points. Based on the estimate and the margin of error, what is the least number of the town's residents that plausibly support the new park?",
   "4200", 4200, lambda: Rational(35, 100) * 12000,
   "Margin of error gives an interval; then scale to the population",
   r"The plausible percent runs from $40-5=35\%$ to $45\%$. The least plausible number is $35\%$ of $12{,}000$: $0.35\cdot12000=4200$. (Using $40\%$ gives $4800$, the estimate itself; $5\%$ of $12{,}000$ is $600$, the margin in people, not the minimum.)")

mc(5, 'H',
   r"A survey asked 400 men and 600 women whether they would use a proposed bus route. Of the men, $55\%$ said yes; of the women, $45\%$ said yes. What percent of all 1,000 people surveyed said yes?",
   PCT(49), [PCT(45), PCT(50), PCT(51)],
   lambda: Fraction(400 * 55 + 600 * 45, 1000),
   "Weighted average: weight each percent by its group size",
   r"Yes answers: $0.55(400)=220$ and $0.45(600)=270$, total $490$ out of $1000$: $49\%$. ($50\%$ averages the two percents with equal weights; $51\%$ reverses the weights; $45\%$ is the women's percent alone.)")

mc(5, 'H',
   r"The total cost $y$, in dollars, of a gym membership after $x$ weeks is modeled by $y=12.5x+300$. A new model uses $m$, the number of 4-week months, instead of $x$ (so $x=4m$). Which equation gives $y$ in terms of $m$?",
   T("$y=50m+300$", ('line', 50, 300)),
   [T("$y=12.5m+300$", ('line', 12.5, 300)), T("$y=50m+1200$", ('line', 50, 1200)), T("$y=3.125m+300$", ('line', 3.125, 300))],
   lambda: ('line', Rational(25, 2) * 4, Rational(25, 2) * 0 + 300),
   "Change of units: substitute, then read slope and intercept",
   r"Substitute $x=4m$: $y=12.5(4m)+300=50m+300$. The slope becomes the cost per month, four times the cost per week, but the intercept, the cost at the start, does not change. ($12.5m+300$ keeps the old slope; $50m+1200$ also multiplies the intercept; $3.125=12.5\div4$ divides instead of multiplies.)",
   order='free')

_t516 = {1: 8, 2: 6, 3: 4, 4: 3, 5: 2, 9: 2}
_f = tbl_fig("s5_t16", ["Value"] + [str(k) for k in _t516], [["Frequency"] + list(_t516.values())])
_d516 = expand(_t516)
def _order516():
    m_, md_, mo_ = mean(_d516), median(_d516), mode_list(_d516)[0]
    return {"mode $<$ median $<$ mean": mo_ < md_ < m_, "mean $<$ median $<$ mode": m_ < md_ < mo_,
            "median $<$ mode $<$ mean": md_ < mo_ < m_, "mode $<$ mean $<$ median": mo_ < m_ < md_}
mc(5, 'H',
   r"A data set of 25 values is summarized in the table." + _f + r"Which of the following correctly orders the mean, the median and the mode of the data set?",
   T("mode $<$ median $<$ mean"), [T("mean $<$ median $<$ mode"), T("median $<$ mode $<$ mean"), T("mode $<$ mean $<$ median")],
   None, "Right-skewed data: mode $<$ median $<$ mean",
   r"The mode is the most frequent value, $1$. With $25$ values the median is the 13th: running totals $8,\ 14,\ldots$ put it at $2$. The mean is $\frac{8+12+12+12+10+18}{25}=\frac{72}{25}=2.88$. So mode $<$ median $<$ mean. A long tail on the right pulls the mean up the most and the mode the least.",
   order='free', each=lambda v: _order516()[v])

_h17c = [4, 9, 13, 8, 6]
_h17e = [0, 10, 20, 30, 40, 50]
_f = hist_fig("s5_hist", _h17e, _h17c, 15, 5, "Points scored", "Number of games")
gi(5, 'H',
   r"The histogram shows the points a team scored in each of its 40 games. Each bar includes its left endpoint but not its right endpoint, and every score is a whole number." + _f + r"What is the greatest possible number of games in which the team scored fewer than 35 points?",
   "34", 34,
   lambda: sum(c for e0, e1, c in zip(_h17e, _h17e[1:], _h17c) if e0 < 35),
   "Histogram bounds: a split bar can all fall on one side",
   r"All games in the bars $0$--$10$, $10$--$20$ and $20$--$30$ are below $35$: $4+9+13=26$. The bar $30$--$40$ contains $8$ games, and in the best case all $8$ scored $30$ to $34$. So the greatest possible number is $26+8=34$. (Splitting that bar in half, $30$, assumes the scores are spread evenly.)")

_pts18 = [(0, 5), (1, 8), (2, 13), (3, 20), (4, 33), (5, 52)]
_f = scat_fig("s5_sc18", _pts18, (0, 6), (0, 60), 1, 10, "$x$", "$y$")
def _bfit():
    lm, lb = lsq([(x_, math.log(y_)) for x_, y_ in _pts18])
    b_ = math.exp(lm)
    opts = [Rational('0.63'), Rational('1.6'), Rational(5), Rational(8)]
    return min(opts, key=lambda o: abs(float(o) - b_))
mc(5, 'H',
   r"The scatterplot shows six data points. An exponential model for the data can be written as $y=a(b)^x$, where $a$ and $b$ are positive constants." + _f + r"Which of the following is closest to the value of $b$?",
   DEC("1.6"), [DEC("0.63"), C(5), C(8)],
   _bfit,
   "Exponential model: $b$ is the factor per unit of $x$",
   r"Each time $x$ increases by $1$, $y$ is multiplied by about the same factor: $\frac85=1.6,\ \frac{13}8\approx1.6,\ \frac{20}{13}\approx1.5,\ \frac{33}{20}\approx1.65,\ \frac{52}{33}\approx1.6$. So $b\approx1.6$ (and $a\approx5$, the value at $x=0$). ($0.63\approx\frac1{1.6}$ would be a decreasing model; $5$ is $a$; $8$ is just the height at $x=1$.)")

def _min_max9():
    from itertools import combinations
    low_sums = {sum(c_) for c_ in combinations(range(1, 20), 4)}
    for M in range(21, 200):
        for up in combinations(range(21, M), 3):
            if (216 - 20 - M - sum(up)) in low_sums:
                return M
mc(5, 'H',
   r"A data set consists of 9 distinct positive integers. The median is 20 and the mean is 24. What is the least possible value of the greatest integer in the data set?",
   C(33), [C(31), C(32), C(36)],
   _min_max9,
   "Extreme cases: make some values as large as allowed to free the total",
   r"The total is $9\cdot24=216$. The four values below the median are distinct and less than $20$, so they sum to at most $16+17+18+19=70$. The median is $20$, so the four values above it sum to at least $216-70-20=126$. Four distinct integers above $20$ with sum $126$ and the smallest possible maximum are $30,31,32,33$. So the answer is $33$. (If repeats were allowed, $31,31,32,32$ would give $32$; the distinct requirement forces $33$.)")

_t520 = {2: 1, 3: 3, 5: 3, 6: 5, 7: 6, 10: 2}
_f = tbl_fig("s5_t20", ["Value"] + [str(k) for k in _t520], [["Frequency"] + list(_t520.values())])
_d520 = expand(_t520)
mc(5, 'H',
   r"A data set of 20 values is summarized in the table." + _f + r"How many of the values are greater than the mean of the data set?",
   C(13), [C(2), C(7), C(8)],
   lambda: sum(1 for v in _d520 if v > mean(_d520)),
   "Compute the mean exactly, then count with care",
   r"Total $=2+9+15+30+42+20=118$, so the mean is $\frac{118}{20}=5.9$. Values greater than $5.9$ are the $6$'s, $7$'s and $10$'s: $5+6+2=13$. (The $6$'s count: $6>5.9$. Counting values above the median $6$ gives $8$; values above the mode $7$ give $2$; values below the mean give $7$.)")

# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(R(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
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
            asc = sorted(items, key=lambda it: float(R(it[1])))
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
        shown = p_['answer'] if p_['kind'] == 'gi' else "%s = %s" % (p_['letter'], p_['right'][0][:50])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, str(got)[:60]))
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
    print("grid-ins: %d of %d (%.0f%%)" % (gcount, len(PROBLEMS), 100.0 * gcount / len(PROBLEMS)))
    print("ALL OK" if not fails else "SOME FAILED")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
