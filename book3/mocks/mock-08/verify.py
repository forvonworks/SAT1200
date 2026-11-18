#!/usr/bin/env python3
"""Independent verification of every answer in mock08-problems.md (Mock Test 8, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force) -- NOT read from the .md.  Tables printed in figures are parsed from
the .md so the check uses the very numbers the student sees.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts, letter balance) is asserted.
Run:  python3 verify.py      (exit code 0 = ALL OK)
"""
import itertools
import math
import os
import random
import re
import sys
from collections import Counter
from fractions import Fraction

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock08-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
R = sp.Rational
x, y = sp.symbols("x y", positive=True)
a_, b_ = sp.symbols("a b", positive=True)
k_ = sp.symbols("k", real=True)
m_ = sp.symbols("m", positive=True)
SYMS = {"x": x, "y": y, "a": a_, "b": b_, "k": k_, "m": m_, "sqrt": sp.sqrt, "pi": sp.pi}


# --------------------------------------------------------------------------- parsing md
def parse_md(path):
    qs, cur, fig = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"## (M[12])-Q(\d+)$", line)
        if m:
            cur = {"mod": int(m.group(1)[1]), "n": int(m.group(2)), "choices": {}, "figure": ""}
            qs[(cur["mod"], cur["n"])] = cur
            continue
        if cur is None:
            continue
        if line.startswith("```latex"):
            fig = []
            continue
        if fig is not None:
            if line.startswith("```"):
                cur["figure"] = "\n".join(fig)
                fig = None
            else:
                fig.append(line)
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


def tex_to_expr(s):
    s = s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = s.replace("{,}", "").replace("\\pi", "pi").replace("\\sqrt", "sqrt").replace("\\cdot", "*")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    return parse_expr(s, local_dict=SYMS, transformations=TRANS)


def same(a, b):
    """numeric equality; for expressions with free symbols, equality at random sample points."""
    a, b = sp.sympify(a), sp.sympify(b)
    fs = (a.free_symbols | b.free_symbols)
    if not fs:
        return abs(float(sp.N(a)) - float(sp.N(b))) < 1e-9
    rnd = random.Random(12345)
    for _ in range(8):
        sub = {s: sp.Float(rnd.uniform(1.1, 9.7)) for s in fs}
        va, vb = complex(sp.N(a.subs(sub))), complex(sp.N(b.subs(sub)))
        if abs(va - vb) > 1e-9 * max(1.0, abs(va)):
            return False
    return True


# ------------------------------------------------------------------ helpers for predicates
def table_rows(fig):
    """parse a tabular: returns list of rows (list of cell strings) without hlines."""
    body = fig.split("\\hline")
    rows = []
    for chunk in body:
        chunk = chunk.replace("\\end{tabular}", "").strip()
        chunk = re.sub(r"\\begin\{tabular\}\{[^}]*\}", "", chunk).strip()
        if not chunk:
            continue
        for r in chunk.split("\\\\"):
            r = r.strip()
            if r:
                rows.append([c.strip() for c in r.split("&")])
    return rows


def pred_tangent_origin(txt):
    """M1-Q22: line y = f(x) must pass through the origin and meet x^2+y^2-6x+8y=0 in exactly one point."""
    rhs = tex_to_expr(txt.split("=", 1)[1])
    X = sp.symbols("X", real=True)
    f = rhs.subs(x, X)
    if sp.simplify(f.subs(X, 0)) != 0:
        return False
    g = sp.expand(X ** 2 + f ** 2 - 6 * X + 8 * f)
    P = sp.Poly(g, X)
    A, B, C = (P.coeff_monomial(X ** 2), P.coeff_monomial(X), P.coeff_monomial(1))
    return sp.simplify(B ** 2 - 4 * A * C) == 0


def line_fn(txt):
    rhs = tex_to_expr(txt.split("=", 1)[1])
    return lambda v: sp.nsimplify(rhs.subs(x, v))


def make_pred_bond(f_true):
    def pred(txt):
        e = tex_to_expr(txt)
        for mv in list(range(1, 41)):
            if abs(float(e.subs(m_, mv)) - f_true(mv)) > 1e-6 * f_true(mv):
                return False
        return True
    return pred


def make_pred_vertexform(fexpr, minval):
    def pred(txt):
        e = tex_to_expr(txt)
        if not same(e, fexpr):
            raise AssertionError("choice not an equivalent form of f: " + txt)
        t = txt.replace("$", "").replace(" ", "")
        m = re.fullmatch(r"(\d*)\(x([+-]\d+)\)\^\{2\}([+-]\d+)", t)
        if not m:
            return False
        return int(m.group(3)) == minval
    return pred


def make_pred_programs(fig):
    rows = table_rows(fig)
    data = {}
    for r in rows[1:]:
        grp = r[0]
        for prog, cell in zip("AB", r[1:]):
            mm = re.match(r"(\d+) of (\d+)", cell)
            data[(grp, prog)] = (int(mm.group(1)), int(mm.group(2)))
    groups = sorted({g for g, _ in data})
    rate = {k: Fraction(v[0], v[1]) for k, v in data.items()}
    tot = {p: Fraction(sum(data[(g, p)][0] for g in groups), sum(data[(g, p)][1] for g in groups)) for p in "AB"}

    def pred(txt):
        clauses = []
        m = re.search(r"Program ([AB]) had the higher improvement rate in each group", txt)
        assert m, txt
        w = m.group(1); l = "B" if w == "A" else "A"
        clauses.append(all(rate[(g, w)] > rate[(g, l)] for g in groups))
        m2 = re.search(r"Program ([AB])'s overall improvement rate was also higher", txt)
        if m2:
            clauses.append(tot[m2.group(1)] > tot[("B" if m2.group(1) == "A" else "A")])
        m3 = re.search(r"Program ([AB])'s overall improvement rate was (more|less) than (\d+) percentage points higher", txt)
        if m3:
            p = m3.group(1); q = "B" if p == "A" else "A"
            gap = (tot[p] - tot[q]) * 100
            clauses.append(gap > int(m3.group(3)) if m3.group(2) == "more" else (0 < gap < int(m3.group(3))))
        assert m2 or m3, txt
        return all(clauses)
    return pred


# ------------------------------------------------------------------ independent solvers
def solve_all(qs):
    A = {}
    t = sp.symbols("t")
    X, Y = sp.symbols("X Y")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(30 + 15 * t, 150), t)[0]
    A[(1, 2)] = sp.sqrt(50)
    A[(1, 3)] = R(126) / R(30, 100)
    A[(1, 4)] = R(2) * 15 / 3                         # similar triangles: h/15 = 2/3
    A[(1, 5)] = sp.solve(sp.Eq(3 * (t + 4), 2 * t + 19), t)[0]
    A[(1, 6)] = sum(sp.solve((t - 4) * (t + 9), t))
    A[(1, 7)] = R(12) + R(5, 2) * 6
    A[(1, 8)] = 15 * x ** 7 / (3 * x ** 4)
    seniors = [1] * 5 + [0] * 7
    pairs = list(itertools.combinations(range(12), 2))
    A[(1, 9)] = Fraction(sum(1 for p in pairs if all(seniors[i] for i in p)), len(pairs))
    b10, s10 = sp.symbols("b10 s10")
    A[(1, 10)] = sp.solve([20 * b10 + 30 * s10 - 130, 250 * b10 + 180 * s10 - 1040], [b10, s10], dict=True)[0][s10]
    A[(1, 11)] = sp.sqrt(18 * x ** 5)
    Mx, My = R(-2 + 6, 2), R(1 + 7, 2)
    A[(1, 12)] = sp.sqrt(Mx ** 2 + My ** 2)
    A[(1, 13)] = min(r for r in range(0, 61) if 11 * r + 8 * (60 - r) >= 600)
    A[(1, 14)] = R(15000) * (1 - R(20, 100)) ** 3
    s_of_c = sp.solve(sp.Eq(R(12, 5) * sp.Symbol("c") + R(3, 2) * sp.Symbol("s"), 18), sp.Symbol("s"))[0]
    A[(1, 15)] = -sp.diff(s_of_c, sp.Symbol("c"))
    A[(1, 16)] = (2 * a_ ** -1 * b_ ** 2) ** 3 / (4 * a_ ** -5 * b_)
    A[(1, 17)] = sum(sp.Poly(sp.expand((2 * x - 1) * (x + 3) * (x - 4)), x).all_coeffs())
    # Q18: table from the figure; P(10th grader | vote for Walsh)
    rows = table_rows(qs[(1, 18)]["figure"])
    tab = {r[0]: [int(v) for v in r[1:]] for r in rows[1:]}
    A[(1, 18)] = Fraction(tab["Walsh"][1], sum(tab["Walsh"]))
    slope19 = R(450 - 120) / R(2) / (R(3, 2) / R(2)) if False else (R(450) - R(120)) / (R(2) - R(1, 2))
    A[(1, 19)] = 120 + slope19 * (R(7, 2) - R(1, 2))
    A[(1, 20)] = ("pred", make_pred_bond(lambda mv: 25000 * 0.82 ** (mv / 12)))
    r21 = sp.symbols("r21")
    A[(1, 21)] = sp.solve(sp.Eq((5 * r21 + 1), 4 * (2 * r21 - 1)), r21)[0]   # x = r*y, divide through by y
    A[(1, 22)] = ("pred", pred_tangent_origin)

    # ================= MODULE 2 =================
    first = sp.solve(sp.Eq(t + 2 * t + 3 * t, 90), t)[0]
    A[(2, 1)] = 3 * first
    A[(2, 2)] = (lambda z: z ** 3 - 2 * z)(-2)
    A[(2, 3)] = sp.cancel((6 * x ** 2 - 5 * x - 4) / (2 * x + 1))
    need = R(11, 10) * 72 * R(9, 2)
    A[(2, 4)] = int(math.ceil(need / 24))
    assert need / 24 != int(need / 24)
    w5 = sp.symbols("w5")
    wind = sp.solve(sp.Eq((270 + w5) * 4, (270 - w5) * 5), w5)[0]
    A[(2, 5)] = (270 + wind) * 4
    cos6 = sp.sqrt(1 - R(28, 100) ** 2)
    A[(2, 6)] = 7500 * cos6
    xs7 = sp.solve(sp.Eq(20 - R(5, 100) * t ** 2, 15), t)
    A[(2, 7)] = max(xs7) - min(xs7)
    k8 = sp.symbols("k8", real=True)
    A[(2, 8)] = sp.solve(sp.Eq((0 - 2) ** 2 + (k8 + 3) ** 2, (0 - 10) ** 2 + (k8 - 9) ** 2), k8)[0]
    f9 = 2 * x ** 2 - 12 * x + 7
    min9 = sp.minimum(f9, x, sp.S.Reals) if False else f9.subs(x, sp.solve(sp.diff(f9, x), x)[0])
    A[(2, 9)] = ("pred", make_pred_vertexform(f9, int(min9)))
    A[(2, 10)] = sp.simplify(((2 * k_) - (k_ + 3)) / ((k_ + 3) - (2 * k_)))
    cap = lambda r: 20 + R(12 - 20, 26 - 10) * (r - 10)
    r11 = sp.symbols("r11")
    A[(2, 11)] = sp.solve(sp.Eq(cap(r11), 15), r11)[0]
    pts = [(0, -4), (2, 0)]                                  # points of y = 2x - 4
    new = [(-px, py + 3) for px, py in pts]                  # reflect over y-axis, then up 3

    def pred12(txt):
        f = line_fn(txt)
        return all(f(px) == py for px, py in new)
    A[(2, 12)] = ("pred", pred12)
    b13 = sp.symbols("b13", positive=True)
    A[(2, 13)] = sp.solve(sp.Eq(b13 + R(4, 3) * b13 + sp.sqrt(b13 ** 2 + (R(4, 3) * b13) ** 2), 36), b13)[0]
    xr = sp.solve(sp.Eq(sp.sqrt(x) + 1 / sp.sqrt(x), 4), x)
    assert len(xr) == 2
    vals14 = {sp.nsimplify(sp.simplify(v ** 2 + 1 / v ** 2)) for v in xr}
    assert len(vals14) == 1
    A[(2, 14)] = vals14.pop()
    rows15 = table_rows(qs[(2, 15)]["figure"])
    xs15 = [int(re.sub(r"[^\d]", "", c)) for c in rows15[0][1:]]
    ys15 = [int(c) for c in rows15[1][1:]]
    aa, bb, cc = sp.symbols("aa bb cc", positive=True)
    cc = sp.symbols("cc", real=True)
    sol15 = sp.solve([aa * bb ** xi + cc - yi for xi, yi in zip(xs15, ys15)], [aa, bb, cc], dict=True)
    sol15 = [s for s in sol15 if s[bb] > 0 and s[aa] != 0]
    assert len(sol15) == 1
    A[(2, 15)] = (sol15[0][aa] * sol15[0][bb] ** 4 + sol15[0][cc])
    Rr, H, dep, rg = 9, 12, 8, 4
    rw = R(Rr * dep, H)
    A[(2, 16)] = (R(1, 3) * sp.pi * rw ** 2 * dep) / (sp.pi * rg ** 2)
    sols17 = []
    for n in range(1, 600):
        tot = 5 + n
        same_c = math.comb(5, 2) + math.comb(n, 2)
        if Fraction(same_c, math.comb(tot, 2)) == Fraction(4, 9):
            sols17.append(n)
    A[(2, 17)] = sum(sols17)
    u, v = sp.symbols("u v")
    s18 = sp.solve([u + 6 * v - 4, 4 * u - 3 * v - 7], [u, v], dict=True)[0]
    A[(2, 18)] = 1 / s18[u] + 1 / s18[v]
    A[(2, 19)] = ("pred", make_pred_programs(qs[(2, 19)]["figure"]))
    A[(2, 20)] = sum(kk for kk in range(-1000, 1001) if 4 * kk * kk - 4 * (kk + 12) < 0)
    k21 = sp.symbols("k21", real=True)
    cx, cy = R(-1 + 7, 2), (2 + k21) / 2
    rad_sq = ((7 + 1) ** 2 + (k21 - 2) ** 2) / 4
    sol21 = sp.solve(sp.Eq(cy ** 2, rad_sq), k21)
    assert len(sol21) == 1
    A[(2, 21)] = sol21[0]
    ff = lambda z: z ** 2 - 6 * z + 5
    sol22 = sp.solve(sp.Eq(ff(ff(x)).subs(x, x), 0), x) if False else None
    Xr = sp.symbols("Xr", real=True)
    roots22 = sp.Poly(sp.expand(ff(ff(Xr))), Xr).nroots(n=30)
    reals22 = [r for r in roots22 if abs(sp.im(r)) < 1e-15]
    A[(2, 22)] = sp.nsimplify(sum(sp.re(r) for r in reals22), rational=True, tolerance=1e-12)
    assert len(reals22) == 4
    return A


# ------------------------------------------------------------------------------ driver
def main():
    qs = parse_md(MD)
    A = solve_all(qs)
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
                for L in "ABCD":
                    txt = q["choices"][L]
                    if isinstance(val, tuple) and val[0] == "pred":
                        match = val[1](txt)
                    else:
                        c = tex_to_expr(txt)
                        match = same(c, val)
                    if match:
                        hits.append(L)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {'predicate' if isinstance(val, tuple) else sp.N(val, 6)})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"])
                assert abs(float(sp.N(keyed)) - float(sp.N(val))) < 1e-9, f"computed {val} != keyed {q['answer']}"
                lim = 6 if q["answer"].startswith("-") else 5
                assert len(q["answer"]) <= lim, "too many characters for a grid-in"
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
        print(f"{name:76s} {'OK' if cond else 'FAIL'}")
        fails += (not cond)

    chk("44 questions present", len(qs) == 44)
    for mod, spec in ((1, dict(E=range(1, 9), M=range(9, 20), H=range(20, 23))),
                      (2, dict(E=range(1, 3), M=range(3, 13), H=range(13, 23)))):
        qq = [qs[(mod, n)] for n in range(1, 23)]
        chk(f"M{mod}: 22 questions", len(qq) == 22)
        for d in "EMH":
            want = list(spec[d])
            got = [q["n"] for q in qq if q["difficulty"] == d]
            chk(f"M{mod}: difficulty {d} at Q{want[0]}-Q{want[-1]} ({len(want)})", got == want)
        for dname, cnt in dict(ALG=8, ADV=8, PSDA=3, GT=3).items():
            chk(f"M{mod}: domain {dname} = {cnt}", sum(q["domain"] == dname for q in qq) == cnt)
        g = [q["n"] for q in qq if q["type"] == "GRID"]
        chk(f"M{mod}: grid-ins {len(g)} in 5-6 -> Q{g}", 5 <= len(g) <= 6)
        chk(f"M{mod}: grid-ins spread (no two adjacent, first<=Q4, last>=Q17)",
            all(b - a >= 2 for a, b in zip(g, g[1:])) and g[0] <= 4 and g[-1] >= 17)
        c = Counter(letters[mod])
        print(f"   M{mod} MC answer-letter distribution: {dict(sorted(c.items()))}")
        chk(f"M{mod}: every letter used 3-5 times", all(3 <= c.get(L, 0) <= 5 for L in "ABCD"))
        seq = [qs[(mod, n)]["answer"] if qs[(mod, n)]["type"] == "MC" else None for n in range(1, 23)]
        run3 = any(seq[i] and seq[i] == seq[i + 1] == seq[i + 2] for i in range(20))
        chk(f"M{mod}: no three identical MC letters in consecutive questions", not run3)
    print()
    print("ALL OK" if fails == 0 else f"{fails} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
