#!/usr/bin/env python3
"""Independent verification of every answer in mock03-problems.md (Mock Test 3, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force) -- NOT read from the .md.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts) is asserted.
Run:  python3 verify.py      (exit code 0 = all OK)
"""
import os
import re
import sys
from collections import Counter
from fractions import Fraction

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock03-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)


# --------------------------------------------------------------------------- parsing md
def parse_md(path):
    qs = {}
    cur = None
    in_fig = False
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"## (M[12])-Q(\d+)$", line)
        if m:
            cur = {"mod": int(m.group(1)[1]), "n": int(m.group(2)), "choices": {}}
            qs[(cur["mod"], cur["n"])] = cur
            continue
        if cur is None:
            continue
        if line.startswith("```latex"):
            in_fig = True
            continue
        if in_fig:
            if line.startswith("```"):
                in_fig = False
            continue
        m = re.match(r"- (\w+): ?(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if len(k) == 1 and k in "ABCD":
            cur["choices"][k] = v
        else:
            cur[k.lower()] = v
    return qs


x, y = sp.symbols("x y", positive=True)
SYMS = {"x": x, "y": y, "sqrt": sp.sqrt, "pi": sp.pi}


def tex_to_expr(s, syms=SYMS):
    """Parse a simple LaTeX math/text choice such as '\\frac{8}{13}', '108\\sqrt3\\,\\pi', '2{,}310'."""
    s = (s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "")
          .replace("\\!", "").replace("{,}", "").replace("\\dfrac", "\\frac"))
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    s = re.sub(r"\\sqrt(\d)", r"\\sqrt{\1}", s)
    s = re.sub(r"\\frac(\d)(\d)", r"\\frac{\1}{\2}", s)
    s = s.replace("\\pi", "*pi")
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"*sqrt(\1)", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    s = re.sub(r"^\*", "", s)
    s = s.replace("(*", "(")
    return parse_expr(s, local_dict=syms, transformations=TRANS)


def same(a, b):
    a, b = sp.nsimplify(a), sp.nsimplify(b)
    if a.is_number and b.is_number:
        return abs(float(a) - float(b)) < 1e-9
    return sp.simplify(a - b) == 0


R = sp.Rational
t = sp.symbols("t")
CUSTOM = {}      # key -> function(choice_text) -> bool ; used when choices are not plain numbers


def solve_all():
    A = {}
    # ================= MODULE 1 =================
    A[(1, 1)] = 2 * sp.solve(sp.Eq(4 * t + 9, 33), t)[0]
    expr2 = sp.expand((5 * x ** 2 - 3 * x + 2) - (2 * x ** 2 - 7 * x - 1)); A[(1, 2)] = expr2
    A[(1, 3)] = R(15, 100) * 240
    A[(1, 4)] = sp.pi * 3 ** 2 * 10
    a5 = sp.symbols("a5"); A[(1, 5)] = sp.solve(sp.Eq(3, -2 * a5 + 11), a5)[0]
    A[(1, 6)] = sp.simplify((x ** 5) ** 2 / x ** 3)
    A[(1, 7)] = sp.solve(sp.Eq(5 * (t + 2), 3 * t + 20), t)[0]
    f8 = (t + 4) * (t - 6)                                # zeros -4, 6
    A[(1, 8)] = sp.solve(sp.diff(f8, t), t)[0]
    # Q9: slope of C(n)=4200+26n is the answer; the correct choice must say "each additional patient" + \$slope
    n9 = sp.symbols("n9"); slope9 = sp.diff(4200 + 26 * n9, n9)
    A[(1, 9)] = slope9
    CUSTOM[(1, 9)] = lambda c: ("additional patient" in c and f"\\${slope9}" in c and "increases" in c
                               and "fixed" not in c and "4,200" not in c)
    A[(1, 10)] = 480 * R(1, 2) ** (15 // 5)
    A[(1, 11)] = min(n for n in range(0, 2000) if 38 * n > 4800 + 14 * n)
    A[(1, 12)] = 62 - (78 - R(4, 100) * 300)
    k13 = sp.symbols("k13")
    cands13 = [kk for kk in range(-100, 101) if kk < 0 and sp.Poly(4 * t ** 2 + kk * t + 25, t).discriminant() == 0]
    assert cands13 == [-20]
    A[(1, 13)] = cands13[0]
    bc = sp.sqrt(26 ** 2 - 10 ** 2); A[(1, 14)] = R(1, 2) * 10 * bc     # angle C = 90 (Thales)
    pts = [(2, 1350), (5, 1830)]
    sl = R(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0]); A[(1, 15)] = pts[1][1] + sl * (9 - 5)
    sol16 = [v for v in range(-30, 31) if sp.Integer(4) ** v == sp.Integer(8) ** (v - 2)]
    assert sol16 == [6] and sp.solve(sp.Eq(2 * t, 3 * (t - 2)), t) == [6]
    A[(1, 16)] = sol16[0]

    def c17(cstr):                                         # line through (0,-3), perpendicular to slope 2
        rhs = tex_to_expr(cstr.split("=", 1)[1])
        b = rhs.subs(x, 0); m = (rhs.subs(x, 2) - rhs.subs(x, 0)) / 2
        return b == -3 and m * 2 == -1
    CUSTOM[(1, 17)] = c17; A[(1, 17)] = "y=-x/2-3"
    p18 = [v for v in sp.solve(sp.Eq(500 * t - 10 * t ** 2, 4000), t) if 0 < v < 50]
    assert len(p18) == 2; A[(1, 18)] = min(p18)
    tab = {("V", "flu"): 18, ("V", "no"): 162, ("N", "flu"): 36, ("N", "no"): 84}
    assert sum(tab.values()) == 300
    A[(1, 19)] = R(tab[("V", "flu")], tab[("V", "flu")] + tab[("N", "flu")])
    x20 = sp.symbols("x20"); A[(1, 20)] = sp.solve(sp.Eq(R(25, 100) * (40 - x20) + x20, R(40, 100) * 40), x20)[0]
    A[(1, 21)] = sp.sqrt(10 ** 2 - (10 - 4) ** 2)
    ff = lambda u: 3 * u - 4; gg = lambda u: u ** 2 + 1
    r22 = sp.solve(sp.expand(gg(ff(t)) - ff(gg(t))), t)
    assert sorted(r22) == [1, 3]
    A[(1, 22)] = sum(r22)

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq((t + 8) / 3, 2 * t - 4), t)[0]
    A[(2, 2)] = sp.expand((3 * x - 2) * (x + 5))
    A[(2, 3)] = sp.solve(sp.Eq(18 + R(12, 100) * t, 30 + R(8, 100) * t), t)[0]
    A[(2, 4)] = [v for v in range(-10, 20) if 2 ** (v + 3) + 2 ** v == 72 if v >= 0][0]
    assert sp.nsolve(2 ** (t + 3) + 2 ** t - 72, t, 3) - 3 < 1e-9
    k5 = sp.symbols("k5"); k5v = sp.solve(sp.Eq(3 * (7 * k5 - 12), 5 * (2 * k5 + 6)), k5)[0]
    assert R(7 * k5v - 12, 2 * k5v + 6) == R(5, 3)
    A[(2, 5)] = (7 * k5v - 12) + (2 * k5v + 6)
    s = R(13 + 13 + 10, 2); A[(2, 6)] = sp.sqrt(s * (s - 13) * (s - 13) * (s - 10))
    A[(2, 7)] = sp.solve(sp.Eq(480 - 10 * t, 60 + 25 * t), t)[0]
    k8 = sp.symbols("k8"); v8 = sp.solve(sp.diff(t ** 2 - 8 * t + k8, t), t)[0]
    A[(2, 8)] = sp.solve(sp.Eq((t ** 2 - 8 * t + k8).subs(t, v8), -3), k8)[0]
    t9 = 4 * sp.log(R(6750, 250), 3); t9 = sp.simplify(t9); assert 250 * 3 ** (t9 / 4) == 6750
    A[(2, 9)] = t9

    def c10(cstr):
        a, b = [int(v) for v in re.findall(r"-?\d+", cstr)]
        return b > 2 * a - 3 and b <= -a + 6
    CUSTOM[(2, 10)] = c10; A[(2, 10)] = "(2,3)"
    sols11 = [v for v in sp.solve(sp.Eq(t ** 2, 36), t) if v != 6]   # x=6 zeroes the denominators
    assert sols11 == [-6]; A[(2, 11)] = sum(sols11)
    a12 = [a for a in range(-50, 51) if sp.Poly((a - 2) * t + 14 - 5 * t - 2 * a, t).is_zero]
    assert len(a12) == 1; A[(2, 12)] = a12[0]
    n13 = sp.symbols("n13"); i13 = sp.solve([sp.Eq(3 * n13 + n13, 360)], n13)[n13]       # not improved in drug group
    drug_imp = 360 - i13; pl_imp = 330 - drug_imp; pl_not = 240 - pl_imp
    assert drug_imp == 3 * i13
    A[(2, 13)] = R(pl_not, pl_not + i13)
    a14, b14 = sp.symbols("a14 b14")
    s14 = sp.solve([a14 * 400 + b14 - R(19) * 400, a14 * 500 + b14 - R("17.6") * 500], [a14, b14])
    A[(2, 14)] = s14[b14]

    def c15(cstr):
        rhs = sp.expand(sp.sympify(cstr.replace("$", "").split("=", 1)[1].replace("w", "*w").replace("**", "*"),
                                   locals={"w": sp.Symbol("w")}))
        w = sp.Symbol("w")
        truth = sp.expand(10 * (R("3.2") + R("0.85") * (7 * w + 14)))
        return sp.simplify(rhs - truth) == 0
    CUSTOM[(2, 15)] = c15; A[(2, 15)] = "M=151+59.5w"
    F, X = sp.symbols("F X")
    F16 = sp.solve(sp.discriminant(X * (120 - 2 * X) - 20 * X - F, X), F)
    assert len(F16) == 1
    for Fv in (F16[0],):
        assert len(sp.solve(X * (120 - 2 * X) - 20 * X - Fv, X)) == 1
    A[(2, 16)] = F16[0]
    Rr = sp.sqrt(6 ** 2 * 3) / 2; A[(2, 17)] = R(4, 3) * sp.pi * Rr ** 3
    m18 = sp.symbols("m18")
    s18 = sp.solve(sp.Eq(5 - 2 * m18, -3 + 8 / m18), m18)
    assert len(s18) == 1; A[(2, 18)] = s18[0]
    a19 = sp.symbols("a19"); a19v = sp.solve(sp.Eq(a19 * (0 - 4) ** 2 - 12, 20), a19)[0]
    assert a19v > 0
    zf = sp.solve(a19v * (t - 4) ** 2 - 12, t)                         # zeros of f
    zg = [2 * z for z in zf]                                            # g(x)=f(x/2)=0 <=> x/2 = zero of f
    gx = lambda v: (a19v * (v / 2 - 4) ** 2 - 12)
    assert all(sp.simplify(gx(z)) == 0 for z in zg)
    A[(2, 19)] = sp.simplify(abs(zg[0] - zg[1]))
    cnt = 0
    for k in range(-400, 401):
        if k + 6 == 0:
            continue                                                    # parallel lines
        xv = Fraction(27, k + 6); yv = 2 * xv - 5
        assert k * xv + 3 * yv == 12
        if xv.denominator == 1 and yv.denominator == 1:
            cnt += 1
    A[(2, 20)] = cnt
    a21, b21 = sp.symbols("a21 b21", positive=True)
    s21 = sp.solve([sp.Eq(a21 + b21, 60 - 26), sp.Eq(a21 ** 2 + b21 ** 2, 26 ** 2)], [a21, b21], dict=True)
    legs = sorted([s21[0][a21], s21[0][b21]]); assert legs == [10, 24]
    area = R(1, 2) * legs[0] * legs[1]
    A[(2, 21)] = area / R(60, 2)
    assert A[(2, 21)] == (legs[0] + legs[1] - 26) / 2
    vals22 = []
    for u in sp.solve(t + 1 / t - 7, t):                                # u = 4^x
        xv = sp.log(u, 4)
        vals22.append(sp.N(2 ** xv + 2 ** (-xv), 30))
    assert abs(vals22[0] - vals22[1]) < 1e-20
    A[(2, 22)] = sp.nsimplify(round(float(vals22[0]), 9))
    return A


def run():
    qs = parse_md(MD)
    A = solve_all()
    fails = 0
    letters = {1: [], 2: []}
    for key in sorted(qs):
        q = qs[key]
        tag = f"M{key[0]}-Q{key[1]:02d}"
        ok = True
        try:
            val = A[key]
            if q["type"] == "MC":
                assert set(q["choices"]) == set("ABCD"), "needs exactly choices A-D"
                hits = []
                for Lt in "ABCD":
                    ctext = q["choices"][Lt]
                    if key in CUSTOM:
                        match = CUSTOM[key](ctext)
                    else:
                        match = same(tex_to_expr(ctext), val)
                    if match:
                        hits.append(Lt)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                # distinct choices
                if key not in CUSTOM:
                    ex = [tex_to_expr(q["choices"][L]) for L in "ABCD"]
                    assert all(not same(ex[i], ex[j]) for i in range(4) for j in range(i)), "duplicate choices"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {val})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"])
                assert abs(float(sp.N(keyed)) - float(sp.N(val))) < 1e-9, f"computed {val} != keyed {q['answer']}"
                assert len(q["answer"]) <= 5, "answer too long for grid"
                msg = f"grid-in {q['answer']}"
        except AssertionError as e:
            ok = False
            msg = f"ASSERT: {e}"
        except Exception as e:      # noqa
            ok = False
            msg = f"ERROR {type(e).__name__}: {e}"
        print(f"{tag}  {'OK  ' if ok else 'FAIL'}  {msg}")
        fails += (not ok)

    print("\n-- blueprint --")

    def chk(name, cond):
        nonlocal fails
        print(f"{name:72s} {'OK' if cond else 'FAIL'}")
        fails += (not cond)

    chk("44 questions present", len(qs) == 44)
    dom = dict(ALG=8, ADV=8, PSDA=3, GT=3)
    for mod, spec in ((1, dict(E=range(1, 9), M=range(9, 20), H=range(20, 23))),
                      (2, dict(E=range(1, 3), M=range(3, 13), H=range(13, 23)))):
        qq = [qs[(mod, n)] for n in range(1, 23)]
        chk(f"M{mod}: 22 questions", len(qq) == 22)
        for d in "EMH":
            want = list(spec[d])
            got = [q["n"] for q in qq if q["difficulty"] == d]
            chk(f"M{mod}: difficulty {d} at Q{want[0]}-Q{want[-1]} ({len(want)})", got == want)
        for dname, cnt in dom.items():
            chk(f"M{mod}: domain {dname} = {cnt}", sum(q["domain"] == dname for q in qq) == cnt)
        g = [q["n"] for q in qq if q["type"] == "GRID"]
        chk(f"M{mod}: grid-ins {len(g)} in 5-6 -> Q{g}", 5 <= len(g) <= 6)
        chk(f"M{mod}: grid-ins spread (no two adjacent, first<=Q4, last>=Q17)",
            all(b - a >= 2 for a, b in zip(g, g[1:])) and g[0] <= 4 and g[-1] >= 17)
        c = Counter(letters[mod])
        print(f"   M{mod} MC answer-letter distribution: {dict(sorted(c.items()))}")
        chk(f"M{mod}: each letter used 3-5 times", set(c) == set("ABCD") and 3 <= min(c.values()) and max(c.values()) <= 5)
    print()
    print("ALL OK" if fails == 0 else f"{fails} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(run())
