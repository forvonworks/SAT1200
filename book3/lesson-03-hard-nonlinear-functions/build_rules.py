#!/usr/bin/env python3
"""Generator for rules-sheet.tex (Book 3 Lesson 3). Cards are stacked automatically; python3 build_rules.py"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

# (title, [(kind, tex)])   kind: f = 15pt formula, e = 13pt line, x = 13pt example
CARDS = [
 ("What each form shows (equivalent forms)", [
   ("f", r"$a(x-h)^2+k$: vertex $(h,k)$ \qquad $a(x-r)(x-s)$: zeros $r,s$"),
   ("e", r"$ax^2+bx+c$: $y$-intercept $c$, axis $x=-\dfrac b{2a}$ \qquad $a<0$: maximum $k$"),
   ("x", r"$-2(x+1)^2+8$: vertex $(-1,8)$, maximum value $8$")]),
 ("Quadratic models: the vertex is the best value", [
   ("f", r"profit, area, height $\Rightarrow$ vertex \ (out of the allowed range? use the endpoint)"),
   ("e", r"price $\times$ quantity $p(c-dp)$: zeros $0$ and $\dfrac cd$, best $p=\dfrac c{2d}$"),
   ("x", r"$p(300-12p)$: best $p=12.5$, revenue $12.5\cdot150=1875$")]),
 ("Symmetry of a parabola", [
   ("f", r"$f(p)=f(q)\ \Rightarrow$ axis $x=\dfrac{p+q}2$"),
   ("e", r"the other input with the same output as $a$ is $x=2h-a$ \ ($h$ = axis)"),
   ("x", r"axis $x=3$ and $f(-1)=f(7)$: the partner of $-1$ is $2(3)-(-1)=7$")]),
 ("Exponential models $f(x)=a\\,b^x$", [
   ("f", r"$a$ = start value $(x=0)$ \qquad $b$ = growth factor, $b=1\pm\dfrac r{100}$"),
   ("e", r"$b>1$ grows, \ $0<b<1$ decays \qquad the factor $0.85$ means a $15\%$ drop"),
   ("x", r"$24{,}000(0.85)^t$: loses $15\%$ a year (not $85\%$)")]),
 ("Per-period exponent", [
   ("f", r"$a\,b^{t/n}$: multiply by $b$ every $n$ units of $t$"),
   ("e", r"doubling time $d$: $a\cdot2^{t/d}$ \qquad half-life $d$: $a\left(\tfrac12\right)^{t/d}$"),
   ("x", r"$250(1.5)^{t/3}$: $+50\%$ every $3$ years (not every year)")]),
 ("Changing units (years to months)", [
   ("f", r"put $\dfrac m{12}$ in place of $t$: \ $P_0b^t\ \Rightarrow\ P_0\,b^{m/12}$, monthly factor $b^{1/12}$"),
   ("x", r"$1.2^{1/12}\approx1.0153$: about $1.5\%$ a month (not $20\div12$)")]),
 ("Rebuild $a\\,b^x$ from two points", [
   ("f", r"$\dfrac{y_2}{y_1}=b^{\,x_2-x_1}$ \qquad then $a=\dfrac{y_1}{b^{x_1}}$"),
   ("x", r"$f(2)=18$, $f(5)=486$: $b^3=27$, $b=3$, $a=2$")]),
 ("Composition $f(g(x))$", [
   ("f", r"inside first: put $g(x)$ where $f$ has $x$ \qquad $f(g(x))\neq g(f(x))$"),
   ("e", r"$f(f(x))$: use $f$ twice, starting from the inside"),
   ("x", r"$f=2x+3$, $g=x^2-1$: \ $g(f(x))=(2x+3)^2-1=4x^2+12x+8$")]),
 ("Transformations $y=a\\,f(x-h)+k$", [
   ("f", r"right $h$, up $k$, stretch by $|a|$, flip if $a<0$ \qquad $f(x+3)$ moves LEFT"),
   ("e", r"a point $(x,y)$ on $f$ goes to $(x+h,\ ay+k)$"),
   ("x", r"$f$ has vertex $(2,-3)$: \ $-2f(x+1)+5$ has vertex $(1,11)$")]),
 ("Polynomials: zeros, multiplicity, ends", [
   ("f", r"factor $(x-r)^m$: odd $m$ crosses the axis, even $m$ touches it"),
   ("e", r"even degree: both ends alike \qquad odd degree: ends opposite"),
   ("e", r"leading coefficient $>0$: right end up \qquad $<0$: right end down"),
   ("x", r"$-2(x-3)^2(x+1)(x+4)$: touches at $3$, degree $4$, both ends down")]),
 ("Piecewise and absolute value", [
   ("f", r"pick the piece that matches $x$; keep only solutions inside that piece"),
   ("e", r"$|u|=k\ \Rightarrow\ u=k$ or $u=-k$ \qquad $-|x-h|+k$ peaks at $(h,k)$"),
   ("x", r"$|x+3|=8$: \ $x=5$ or $x=-11$")]),
 ("Which equation? Test the points", [
   ("f", r"test each choice at the given points, zeros and $y$-intercept"),
   ("e", r"count solutions: graph both sides \qquad unknown $k$: add a slider in Desmos"),
   ("x", r"vertex $(-2,5)$ and point $(0,13)$: \ $2(x+2)^2+5$ \ (one point alone is not enough)")]),
]

WORDS = [
 ("vertex", "cho'qqi"), ("axis of symmetry", "simmetriya o'qi"), ("maximum", "eng katta qiymat"), ("minimum", "eng kichik qiymat"),
 ("growth factor", "o'sish ko'paytuvchisi"), ("decay", "kamayish (so'nish)"), ("doubling time", "ikki baravar ortish vaqti"),
 ("half-life", "yarim yemirilish davri"), ("composition", "funksiyalar kompozitsiyasi"), ("shift / translation", "siljitish"),
 ("reflection", "akslantirish"), ("multiplicity", "karralilik"), ("leading coefficient", "bosh koeffitsient"),
 ("end behavior", "chetlardagi holat"), ("piecewise function", "bo'lakli funksiya"),
]

SIZES = {"f": (15, 18), "e": (13, 16), "x": (13, 16)}

def lh(kind, tex):
    base = 9.0 if kind == "f" else 8.0
    return base + (3.5 if re.search(r"dfrac|frac", tex) else 0)

PRE = open(os.path.join(HERE, "..", "lesson-05-speed-tricks", "rules-sheet.tex"), encoding="utf-8").read()
PRE = PRE[:PRE.index(r"\begin{document}")]
PRE = PRE.replace(r"\newcommand{\pill}[3]", r"\newcommand{\pill}[3]")

def card_height(lines):
    return 10.5 + (1.5 if re.search(r"frac", lines[0][1]) else 0) + sum(lh(k, t) for k, t in lines) + 4.0

def emit():
    out = [PRE, r"\begin{document}"]
    pages, cur, y = [], [], 40.0
    first = True
    limit = 281.0
    cards = []
    for title, lines in CARDS:
        cards.append(("card", title, lines, card_height(lines)))
    cards.append(("words", "NEW WORDS", None, 75.0))
    page_y0 = [40.0, 33.0, 33.0]
    pi, y = 0, page_y0[0]
    pagecards = [[]]
    for c in cards:
        h = c[3]
        if y + h > limit:
            pi += 1
            y = page_y0[min(pi, 2)]
            pagecards.append([])
        pagecards[-1].append((y, c))
        y += h + 6.0
    npages = len(pagecards)
    for i, pc in enumerate(pagecards):
        out.append(r"\topicheader{3}{Hard Nonlinear Functions}")
        if i == 0:
            out.append(r"\videobanner{Lesson 3}")
        else:
            out.append(r"\pagekicker{Rules sheet -- %d/%d}" % (i + 1, npages))
        out.append(r"\pagefooter{%d}" % (i + 1))
        out.append(r"\mbox{}%")
        for y0, c in pc:
            kind, title, lines, h = c
            out.append("")
            out.append(r"\cardbg{16}{%.1f}{178}{%.1f}" % (y0, h))
            if kind == "words":
                out.append(r"\pillw{26}{%.1f}{NEW WORDS ~\textperiodcentered~ YANGI SO'ZLAR}" % (y0 + 3))
                half = (len(WORDS) + 1) // 2
                for ci, chunk in enumerate((WORDS[:half], WORDS[half:])):
                    out.append(r"\begin{textblock*}{80mm}(%dmm,%.1fmm)" % (26 if ci == 0 else 108, y0 + 12.5))
                    out.append(r"{\fontsize{10.5}{12}\selectfont")
                    out.append(r"\begin{tabular}{@{}>{\bfseries}p{31mm}>{\raggedright\arraybackslash}p{42mm}@{}}")
                    out.append(r"\cellcolor{accent}\textcolor{white}{\sffamily English} & \cellcolor{accent}\textcolor{white}{\sffamily O'zbekcha}\\")
                    for ri, (en, uz) in enumerate(chunk):
                        out.append(r"\rowcolor{%s} %s & {\itshape %s}\\" % ("badge!45" if ri % 2 == 0 else "white", en, uz))
                    out.append(r"\end{tabular}}")
                    out.append(r"\end{textblock*}")
                continue
            out.append(r"\pill{26}{%.1f}{%s}" % (y0 + 3, title))
            yy = y0 + 10.5 + (1.5 if re.search(r"frac", lines[0][1]) else 0)
            for k, t in lines:
                sz, ld = SIZES[k]
                out.append(r"\begin{textblock*}{158mm}(26mm,%.1fmm)" % yy)
                out.append(r"{\fontsize{%d}{%d}\selectfont %s}" % (sz, ld, t))
                out.append(r"\end{textblock*}")
                yy += lh(k, t)
        out.append(r"\clearpage" if i < npages - 1 else "")
    out.append(r"\end{document}")
    open(os.path.join(HERE, "rules-sheet.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("rules pages:", npages, [len(p) for p in pagecards])

emit()
