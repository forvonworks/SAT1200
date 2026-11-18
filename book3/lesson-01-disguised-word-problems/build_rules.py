#!/usr/bin/env python3
"""Generator for rules-sheet.tex (Book 3 Lesson 1). Cards are stacked automatically; python3 build_rules.py"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

# (title, [(kind, tex)])   kind: f = 15pt formula, e = 13pt line, x = 13pt example
CARDS = [
 ("Read the last sentence first; define variables", [
   ("f", r"underline what is asked: a total, a difference, a rate, \ ``how many more''"),
   ("e", r"$x$ = number of adult tickets \ (tickets): write a unit beside every symbol"),
   ("x", r"$s=75$ and $a=45$, but the question asks for $s-a=30$")]),
 ("Words to symbols", [
   ("f", r"$a$ more than $b\ \to\ b+a$ \qquad $a$ less than $b\ \to\ b-a$"),
   ("e", r"$a$ times as many as $b\ \to\ a\cdot b$ \qquad $x$ exceeds $y$ by $k\ \to\ x=y+k$"),
   ("x", r"5 less than twice $n$: \ $2n-5$ \ (not $5-2n$)")]),
 ("Inequality words", [
   ("f", r"at least $\ge$ \quad at most, no more than $\le$ \quad more than $>$ \quad fewer than $<$"),
   ("e", r"minimum count: round UP \qquad maximum count: round DOWN"),
   ("x", r"$14a\ge890\ \Rightarrow\ a\ge63.6\ \Rightarrow\ 64$ tickets")]),
 ("Hidden given information", [
   ("f", r"mean $\times$ count $=$ sum \qquad total $=$ part $+$ part \qquad ratio $3{:}5$: $3k,\ 5k$"),
   ("e", r"a total can be hidden in a difference, a mean, or a ratio: rewrite it as an equation"),
   ("x", r"mean 18 of 5 numbers: sum 90; mean 20 of 6 numbers: sum 120; sixth number $30$")]),
 ("Consecutive integers, ages, coins", [
   ("f", r"$n,\ n+1,\ n+2$ \qquad even or odd: $n,\ n+2,\ n+4$"),
   ("e", r"coins: value $=$ coin value $\times$ count \qquad ages: the age gap never changes"),
   ("x", r"three consecutive odd integers with sum 111: the middle one is $111\div3=37$")]),
 ("Chains and extra information", [
   ("f", r"find the intermediate quantity, then answer the quantity asked"),
   ("e", r"cross out every number that no equation uses (fees, distances, prices not asked about)"),
   ("x", r"35 scones $\to$ scone sales $35\times4.50$")]),
 ("Rate, time, distance and work", [
   ("f", r"$d=rt$ \qquad job rates add: $\dfrac1{t_1}+\dfrac1{t_2}=\dfrac1{t}$"),
   ("e", r"average speed $=\dfrac{\text{total distance}}{\text{total time}}$, never the mean of the two speeds"),
   ("x", r"24 km at 12 km/h and back at 8 km/h: $\dfrac{48}{2+3}=9.6$ km/h")]),
 ("Mixtures", [
   ("f", r"amount $\times$ concentration adds: \ $c_1v_1+c_2v_2=c_3(v_1+v_2)$"),
   ("e", r"draining $x$ of a mixture removes $x\times$ its concentration, not $x$"),
   ("x", r"50 L at $20\%$, drain $x$, add $x$ pure: $10-0.2x+x=18$")]),
 ("Units hidden in context", [
   ("f", r"convert first: min $\to$ h $(\div60)$ \quad W $\to$ kW $(\div1000)$ \quad week $\to$ days"),
   ("e", r"per-day rate $\times$ days, per-hour rate $\times$ hours: the units must cancel"),
   ("x", r"1.5 kW for 40 min a day for 30 days: $1.5\times\tfrac{40}{60}\times30=30$ kWh")]),
 ("Invented notation", [
   ("f", r"$a\star b=2a-b^2$: first symbol $\to a$, second symbol $\to b$"),
   ("e", r"nested operations: inside first \qquad simplify the definition if you can"),
   ("x", r"$(3\star4)\star2=(-10)\star2=-24$ \qquad $(a+b)^2-(a-b)^2=4ab$")]),
 ("Which model?", [
   ("f", r"constant difference: linear \qquad constant ratio: exponential"),
   ("e", r"two linear parts multiplied: quadratic \qquad doubling differences: exponential"),
   ("x", r"$5,8,14,26$: differences $3,6,12$, so $N=2+3\cdot2^t$")]),
 ("What does it represent?", [
   ("f", r"$y=mx+b$: \ $m$ = change in $y$ per 1 unit of $x$ \qquad $b$ = value at $x=0$"),
   ("e", r"an intercept is where the other variable is $0$ \qquad $a\,b^{t/n}$: factor $b$ every $n$ units"),
   ("x", r"$L=46-2t$: 2 cm lost per minute; empty at $t=23$")]),
 ("Plug in the answer choices", [
   ("f", r"test a middle choice first; a wrong choice must fail one condition"),
   ("e", r"use it when the algebra is long or the asked quantity is hard to isolate"),
   ("x", r"digit sum 11, reversing adds 27: $47\to74$ works")]),
 ("Patterns and counting", [
   ("f", r"linear: $a_n=a_1+(n-1)d$ \qquad exponential: $a_n=a_1r^{\,n-1}$"),
   ("e", r"recursive rule: generate terms \qquad counting: multiply choices, subtract forbidden"),
   ("x", r"border of an $n\times n$ square: $4n-4$ \qquad $4\cdot5\cdot4-4=76$ meals")]),
]

WORDS = [
 ("variable", "o'zgaruvchi"), ("unit", "o'lchov birligi"), ("rate", "tezlik, me'yor"), ("ratio", "nisbat"),
 ("mean (average)", "o'rtacha qiymat"), ("consecutive", "ketma-ket"), ("at least", "kamida"), ("at most", "ko'pi bilan"),
 ("mixture", "aralashma"), ("concentration", "konsentratsiya"), ("sequence", "ketma-ketlik"), ("model", "model"),
 ("intercept", "o'q bilan kesishish nuqtasi"), ("total", "jami"), ("difference", "ayirma, farq"),
]

SIZES = {"f": (15, 18), "e": (13, 16), "x": (13, 16)}

def lh(kind, tex):
    base = 8.6 if kind == "f" else 7.4
    return base + (3.5 if re.search(r"dfrac|frac", tex) else 0)

PRE = open(os.path.join(HERE, "..", "lesson-05-speed-tricks", "rules-sheet.tex"), encoding="utf-8").read()
PRE = PRE[:PRE.index(r"\begin{document}")]
PRE = PRE.replace(r"\newcommand{\pill}[3]", r"\newcommand{\pill}[3]")

def card_height(lines):
    return 10.5 + (1.5 if re.search(r"frac", lines[0][1]) else 0) + sum(lh(k, t) for k, t in lines) + 2.0

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
        out.append(r"\topicheader{1}{Disguised Word Problems}")
        if i == 0:
            out.append(r"\videobanner{Lesson 1}")
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
