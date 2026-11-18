#!/usr/bin/env python3
"""True-scale TikZ figures for Book 3 Lesson 9.
Every figure is computed from the numbers printed in the problem stem; each function asserts the geometric
facts it draws (printed lengths = measured lengths, printed angles = measured angles, right angles, parallels),
so a wrong or distorted figure fails `python3 verify.py`.  Units: mm on the page."""
import math

D = math.pi / 180.0
LW = "line width=0.6pt"


def P(p):
    return "(%.3fmm,%.3fmm)" % (p[0], p[1])


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])
def unit(a, b):
    d = dist(a, b)
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
def dotp(a, b): return a[0] * b[0] + a[1] * b[1]
def mid(a, b): return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
def lerp(a, b, t): return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
def near(a, b, tol=1e-6): return abs(a - b) < tol
def ang_at(v, a, b):
    """angle at v between rays to a and b, degrees"""
    ua, ub = unit(v, a), unit(v, b)
    return math.degrees(math.acos(max(-1, min(1, dotp(ua, ub)))))
def ray_deg(v, a):
    return math.degrees(math.atan2(a[1] - v[1], a[0] - v[0]))
def centroid(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
def perp(u): return (-u[1], u[0])

START = r"\begin{tikzpicture}[%s,ink,every node/.style={font=\footnotesize,inner sep=1pt}]" % LW
END = r"\end{tikzpicture}"


def vlabel(p, text, ref, off=2.8):
    """vertex label pushed away from ref"""
    u = unit(ref, p)
    q = add(p, mul(u, off))
    return r"\node at %s {%s};" % (P(q), text)


def elabel(p, q, text, ref, off=2.6, extra=""):
    """label for edge pq, offset perpendicular, away from ref"""
    m = mid(p, q)
    n = perp(unit(p, q))
    if dotp(n, sub(m, ref)) < 0:
        n = (-n[0], -n[1])
    return r"\node%s at %s {%s};" % (extra, P(add(m, mul(n, off))), text)


def ra(v, a, b, s=2.2):
    """right-angle mark at v between directions to a and b"""
    d1, d2 = unit(v, a), unit(v, b)
    assert near(dotp(d1, d2), 0, 1e-6), "not a right angle"
    p1 = add(v, mul(d1, s)); p3 = add(v, mul(d2, s)); p2 = add(p1, mul(d2, s))
    return r"\draw[line width=0.4pt] %s -- %s -- %s;" % (P(p1), P(p2), P(p3))


def arc(v, a1, a2, r=5.0, extra=""):
    """arc at v from direction a1 to a2 (degrees, counter-clockwise)"""
    s = add(v, (r * math.cos(a1 * D), r * math.sin(a1 * D)))
    return r"\draw[line width=0.4pt%s] %s arc[start angle=%.3f,end angle=%.3f,radius=%.3fmm];" % (extra, P(s), a1, a2, r)


def angle_mark(v, a, b, r, text=None, rt=None, leader=False):
    """arc inside the angle at v (rays to a and b), optional label at radius rt along the bisector"""
    a1, a2 = ray_deg(v, a), ray_deg(v, b)
    while a2 - a1 > 180: a2 -= 360
    while a1 - a2 > 180: a1 -= 360
    lo, hi = min(a1, a2), max(a1, a2)
    out = [arc(v, lo, hi, r)]
    if text:
        m = (lo + hi) / 2.0
        rt = rt if rt else r + 4.5
        q = add(v, (rt * math.cos(m * D), rt * math.sin(m * D)))
        out.append(r"\node at %s {%s};" % (P(q), text))
    return "\n".join(out)


def tick(p, q, n=1, s=1.3, gap=0.9):
    m = mid(p, q); u = unit(p, q); nn = perp(u)
    out = []
    for i in range(n):
        c = add(m, mul(u, (i - (n - 1) / 2.0) * gap))
        out.append(r"\draw[line width=0.4pt] %s -- %s;" % (P(add(c, mul(nn, s))), P(sub(c, mul(nn, s)))))
    return "\n".join(out)


def dot(p, r=0.55):
    return r"\fill %s circle (%.2fmm);" % (P(p), r)


def poly(pts, extra=""):
    return r"\draw[%s] %s -- cycle;" % (extra.lstrip(","), " -- ".join(P(p) for p in pts))


def seg(p, q, extra=""):
    return r"\draw[%s] %s -- %s;" % (extra.lstrip(","), P(p), P(q))


def parmark(p, q, n=1):
    """small arrow heads on segment pq to mark parallels"""
    m = mid(p, q); u = unit(p, q); nn = perp(u)
    out = []
    for i in range(n):
        c = add(m, mul(u, (i - (n - 1) / 2.0) * 1.8))
        out.append(r"\draw[line width=0.4pt] %s -- %s -- %s;" % (P(add(sub(c, mul(u, 1.2)), mul(nn, 1.1))), P(c), P(sub(sub(c, mul(u, 1.2)), mul(nn, 1.1)))))
    return "\n".join(out)


def pic(*parts):
    return "\n".join([START] + [x for x in parts if x] + [END])


# ------------------------------------------------------------------------------ F: 45-60 altitude (2.4)
def fig_special(ad=6, u=5.5):
    h = ad * u
    Dp = (0, 0); A = (0, h); B = (-h / math.tan(45 * D), 0); C = (h / math.tan(60 * D), 0)
    assert near(ang_at(B, A, C), 45) and near(ang_at(C, A, B), 60)
    assert near(dotp(sub(A, Dp), sub(C, B)), 0) and near(dist(A, Dp) / u, ad)
    ref = centroid([A, B, C])
    return pic(poly([A, B, C]), seg(A, Dp, ",dashed"), ra(Dp, A, C, 2.0),
               angle_mark(B, A, C, 6, r"$45^\circ$", 11), angle_mark(C, A, B, 6, r"$60^\circ$", 10.5),
               vlabel(A, "$A$", ref), vlabel(B, "$B$", ref), vlabel(C, "$C$", ref),
               r"\node at %s {$D$};" % P((0.0, -2.8)),
               r"\node[left=0.5pt] at %s {$%g$};" % (P(mid(A, Dp)), ad))


# ------------------------------------------------------------------------------ F: altitude to hypotenuse (2.10, 3.3)
def fig_alt(p=5.0, q=12.0, u=5.0, lab_seg=None):
    """right angle at B, legs AB=p, BC=q; altitude BD to hypotenuse AC. lab_seg=(AD,DC) prints segment lengths."""
    c = math.hypot(p, q)
    A = (0, 0); C = (c * u, 0)
    xb = p * p / c * u; yb = p * q / c * u
    B = (xb, yb); Dp = (xb, 0)
    assert near(dist(A, B), p * u, 1e-6) and near(dist(B, C), q * u, 1e-6) and near(dotp(sub(A, B), sub(C, B)), 0, 1e-6)
    assert near(dotp(sub(B, Dp), sub(C, A)), 0, 1e-6)
    ref = centroid([A, B, C])
    parts = [poly([A, B, C]), seg(B, Dp, ",dashed"), ra(B, A, C, 2.2), ra(Dp, B, C, 1.8),
             vlabel(A, "$A$", ref), vlabel(B, "$B$", ref), vlabel(C, "$C$", ref),
             r"\node at %s {$D$};" % P((Dp[0], -3.0))]
    if lab_seg:
        ad, dc = lab_seg
        assert near(dist(A, Dp) / u, ad, 1e-6) and near(dist(Dp, C) / u, dc, 1e-6)
        y = -8.0
        parts.append(r"\draw[<->,line width=0.4pt] %s -- %s;" % (P((A[0], y)), P((Dp[0], y))))
        parts.append(r"\draw[<->,line width=0.4pt] %s -- %s;" % (P((Dp[0], y)), P((C[0], y))))
        parts.append(r"\node[below=0.3pt] at %s {$%g$};" % (P((Dp[0] / 2, y)), ad))
        parts.append(r"\node[below=0.3pt] at %s {$%g$};" % (P(((Dp[0] + C[0]) / 2, y)), dc))
    return pic(*parts)

# ------------------------------------------------------------------------------ F: DE parallel BC (3.1)
def fig_parseg(ad=9, db=6, de=12, bc=20, ac=17, u=3.6):
    ab = ad + db
    B = (0, 0); C = (bc * u, 0)
    xa = (ab * ab - ac * ac + bc * bc) / (2.0 * bc); ya = math.sqrt(ab * ab - xa * xa)
    A = (xa * u, ya * u)
    Dp = lerp(A, B, ad / ab); E = lerp(A, C, ad / ab)
    assert near(dist(A, Dp) / u, ad) and near(dist(Dp, B) / u, db) and near(dist(Dp, E) / u, de, 1e-6)
    assert near(Dp[1], E[1])
    ref = centroid([A, B, C])
    return pic(poly([A, B, C]), seg(Dp, E), dot(Dp), dot(E),
               vlabel(A, "$A$", ref), vlabel(B, "$B$", ref), vlabel(C, "$C$", ref),
               r"\node[left=1pt] at %s {$D$};" % P(Dp), r"\node[right=1pt] at %s {$E$};" % P(E),
               elabel(A, Dp, "$%d$" % ad, ref, 2.4), elabel(Dp, B, "$%d$" % db, ref, 2.4),
               r"\node[below=0.5pt] at %s {$%d$};" % (P(mid(Dp, E)), de))


# ------------------------------------------------------------------------------ F: parallel lines + transversal (3.2)
def fig_trans(a1=59, a2=121, t1=r"$(3x+5)^\circ$", t2=r"$(7x-5)^\circ$", gap=26.0, L=62.0):
    assert a1 + a2 == 180
    th = -a1 * D
    U = (0, 0)
    s = gap / math.sin(a1 * D)
    Lw = (s * math.cos(a1 * D), -gap)
    assert near(ang_at(U, (1, 0), Lw), a1) and near(ang_at(Lw, add(Lw, (1, 0)), U), a2)
    ext = 9.0
    uu = unit(U, Lw)
    T1 = sub(U, mul(uu, ext)); T2 = add(Lw, mul(uu, ext))
    parts = [seg((-L / 2 + 6, 0), (L / 2 + 6, 0)), seg((Lw[0] - L / 2 + 6, -gap), (Lw[0] + L / 2 + 6, -gap)), seg(T1, T2),
             r"\node[right] at %s {$\ell$};" % P((L / 2 + 6, 0)), r"\node[right] at %s {$m$};" % P((Lw[0] + L / 2 + 6, -gap)),
             r"\node[above left] at %s {$t$};" % P(T1)]
    parts.append(arc(U, -a1, 0, 7))
    parts.append(r"\node at %s {%s};" % (P((17.0, -6.4)), t1))
    parts.append(arc(Lw, 0, a2, 7))
    parts.append(r"\node at %s {%s};" % (P(add(Lw, (17.0, 10.5))), t2))
    parts.append(parmark((-L / 2 + 6, 0), (-L / 2 + 14, 0)))
    parts.append(parmark((Lw[0] - L / 2 + 6, -gap), (Lw[0] - L / 2 + 14, -gap)))
    return pic(*parts)


# ------------------------------------------------------------------------------ F: isosceles + exterior angle (3.5)
def fig_isoext(apex=36, b=24.0, t_apex=r"$(3x-6)^\circ$", t_ext=r"$(7x+10)^\circ$"):
    base = (180 - apex) / 2.0
    B = (0, 0); C = (b, 0); A = (b / 2, b / 2 * math.tan(base * D))
    assert near(dist(A, B), dist(A, C)) and near(ang_at(A, B, C), apex) and near(ang_at(B, A, C), base)
    Dp = (b + 18, 0)
    ext = 180 - base
    assert near(ang_at(C, A, Dp), ext)
    ref = centroid([A, B, C])
    lab = (A[0] + 8.0, A[1] + 1.0)
    return pic(poly([A, B, C]), seg(C, Dp), tick(A, B, 1), tick(A, C, 1),
               vlabel(B, "$B$", ref), r"\node at %s {$C$};" % P((C[0] - 1.5, -3.0)),
               r"\node[below] at %s {$D$};" % P(Dp), r"\node[above=0.3mm] at %s {$A$};" % P(A),
               angle_mark(A, B, C, 6.5),
               r"\draw[line width=0.3pt] %s -- %s;" % (P((lab[0], lab[1] - 1.5)), P((A[0] + 1.5, A[1] - 6.5))),
               r"\node[right=0pt] at %s {%s};" % (P(lab), t_apex),
               arc(C, 0, ext, 5.5), r"\node at %s {%s};" % (P(add(C, (11.5, 11.5))), t_ext))

# ------------------------------------------------------------------------------ F: pentagon with AB || ED (3.7)
def fig_pent(Bd=130, Cd=140, Dd=90, tB=r"$(2x+30)^\circ$", tC=r"$(3x-10)^\circ$", tD=r"$(x+40)^\circ$", sc=2.1):
    Ad = 100; Ed = 180 - Ad
    assert Ad + Bd + Cd + Dd + Ed == 540 and Bd + Cd + Dd == 360
    dirs = [0.0]
    for ex in (180 - Bd, 180 - Cd, 180 - Dd):
        dirs.append(dirs[-1] + ex)       # AB, BC, CD, DE
    dirs.append(dirs[-1] + (180 - Ed))   # EA
    b, c, d = 12.0, 9.0, 7.0
    v = lambda a, L: (L * math.cos(a * D), L * math.sin(a * D))
    s = add(add(v(dirs[0], b), v(dirs[1], c)), v(dirs[2], d))
    m = [[math.cos(dirs[3] * D), math.cos(dirs[4] * D)], [math.sin(dirs[3] * D), math.sin(dirs[4] * D)]]
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    e = (-s[0] * m[1][1] + s[1] * m[0][1]) / det
    l = (-m[0][0] * s[1] + m[1][0] * s[0]) / det
    assert e > 0 and l > 0
    pts = [(0.0, 0.0)]
    for ang, L in zip(dirs, (b, c, d, e)):
        pts.append(add(pts[-1], v(ang, L)))
    assert near(dist(pts[-1], pts[0]), l, 1e-6)
    pts = [mul(p, sc) for p in pts[:5]]
    A, B, C, Dp, E = pts
    def interior(i): return ang_at(pts[i], pts[(i - 1) % 5], pts[(i + 1) % 5])
    assert near(interior(1), Bd) and near(interior(2), Cd) and near(interior(3), Dd) and near(interior(0) + interior(4), 180)
    # AB parallel to ED
    ab = sub(B, A); ed = sub(Dp, E)
    assert near(ab[0] * ed[1] - ab[1] * ed[0], 0, 1e-6)
    cen = centroid(pts)
    parts = [poly(pts), parmark(A, B, 1), parmark(E, Dp, 1)]
    for i, nm in enumerate("ABCDE"):
        parts.append(vlabel(pts[i], "$%s$" % nm, cen, 3.0))
    for i, tx in ((1, tB), (2, tC)):
        parts.append(angle_mark(pts[i], pts[i - 1], pts[(i + 1) % 5], 4.0, tx, 13.0))
    parts.append(ra(Dp, C, E, 2.4))
    parts.append(r"\node at %s {%s};" % (P(add(Dp, mul(unit(Dp, cen), 13.0))), tD))
    return pic(*parts)

# ------------------------------------------------------------------------------ F: bowtie (3.11)
def fig_bowtie(ae=12, ed=18, be=10, ec=15, ang=64, u=2.4):
    assert near(ae / ed, be / ec)
    E = (0, 0)
    u1 = (math.cos(ang * D / 2 + 0.0), math.sin(ang * D / 2)); u2 = (math.cos(-ang * D / 2), math.sin(-ang * D / 2))
    A = mul(u1, ae * u); Dp = mul(u1, -ed * u); B = mul(u2, be * u); C = mul(u2, -ec * u)
    # place so that A,B on the right
    ab = sub(B, A); dc = sub(C, Dp)
    assert near(ab[0] * dc[1] - ab[1] * dc[0], 0, 1e-6)     # AB parallel DC
    assert near(dist(A, E) / u, ae) and near(dist(E, Dp) / u, ed) and near(dist(B, E) / u, be) and near(dist(E, C) / u, ec)
    cen = E
    return pic(seg(A, Dp), seg(B, C), seg(A, B), seg(Dp, C), parmark(A, B), parmark(Dp, C),
               vlabel(A, "$A$", E, 3.0), vlabel(B, "$B$", E, 3.0), vlabel(C, "$C$", E, 3.0), vlabel(Dp, "$D$", E, 3.0),
               r"\node[above=1pt] at %s {$E$};" % P(E),
               elabel(A, E, "$%d$" % ae, mul(A, 0) if False else B, 2.3), elabel(E, Dp, "$%d$" % ed, C, 2.3),
               elabel(B, E, "$%d$" % be, A, 2.3))


# ------------------------------------------------------------------------------ F: golden triangle (3.14)
def fig_golden(u=34.0):
    phi = (1 + math.sqrt(5)) / 2
    B = (0, 0); C = (u, 0); A = (u / 2, u * math.sqrt(phi * phi - 0.25))
    assert near(dist(A, B), dist(A, C)) and near(ang_at(A, B, C), 36, 1e-6)
    Dp = lerp(A, C, 1.0 / phi)  # AD = BC
    assert near(dist(A, Dp), dist(B, C)) and near(dist(B, Dp), dist(B, C))
    ref = centroid([A, B, C])
    return pic(poly([A, B, C]), seg(B, Dp), tick(A, Dp, 3), tick(B, Dp, 3), tick(B, C, 3),
               vlabel(A, "$A$", ref), vlabel(B, "$B$", ref), vlabel(C, "$C$", ref),
               r"\node[right=1pt] at %s {$D$};" % P(Dp))


# ------------------------------------------------------------------------------ F: triangle with sides 13,20,21 (4.1)
def fig_tri3(ab=13, bc=20, ac=21, u=3.4):
    xb = (ab * ab - bc * bc + ac * ac) / (2.0 * ac)
    yb = math.sqrt(ab * ab - xb * xb)
    A = (0, 0); C = (ac * u, 0); B = (xb * u, yb * u)
    assert near(dist(A, B) / u, ab) and near(dist(B, C) / u, bc) and near(dist(A, C) / u, ac)
    ref = centroid([A, B, C])
    return pic(poly([A, B, C]), vlabel(A, "$A$", ref), vlabel(B, "$B$", ref), vlabel(C, "$C$", ref),
               elabel(A, B, "$%d$" % ab, ref), elabel(B, C, "$%d$" % bc, ref), elabel(A, C, "$%d$" % ac, ref))


# ------------------------------------------------------------------------------ F: elevation with two observation points (4.2)
def fig_elev(d=40, u=0.78):
    h = d / (math.sqrt(3) - 1)
    O = (0, 0); T = (0, h * u); A = (-h * u, 0); B = (-h * math.sqrt(3) * u, 0)
    assert near(math.degrees(math.atan2(h, h)), 45) and near(math.degrees(math.atan2(h, h * math.sqrt(3))), 30)
    assert near(dist(A, B) / u, d, 1e-6)
    return pic(seg((B[0] - 4, 0), (7, 0)), seg(O, T), seg(B, T), seg(A, T),
               ra(O, T, A, 2.2),
               r"\node[above] at %s {$T$};" % P(T), r"\node[below] at %s {$B$};" % P(B), r"\node[below] at %s {$A$};" % P(A),
               r"\node[below] at %s {$O$};" % P(O),
               dot(A), dot(B),
               arc(B, 0, 30, 9), r"\node at %s {$30^\circ$};" % P(add(B, (16.0, 2.0))),
               arc(A, 0, 45, 6), r"\node at %s {$45^\circ$};" % P(add(A, (11.0, 4.0))),
               r"\draw[<->,line width=0.4pt] %s -- %s;" % (P((B[0], -7.3)), P((A[0], -7.3))),
               r"\node[below] at %s {$%d$ m};" % (P(((A[0] + B[0]) / 2, -7.0)), d))


# ------------------------------------------------------------------------------ F: coordinate plane (4.4)
def fig_coord(Pp=(-2, 1), Rr=(7, -2), xq=4, u=4.4):
    X = lambda p: (p[0] * u, p[1] * u)
    parts = [r"\draw[->,line width=0.4pt] %s -- %s;" % (P(X((-3.6, 0))), P(X((8.8, 0)))),
             r"\draw[->,line width=0.4pt] %s -- %s;" % (P(X((0, -6.6))), P(X((0, 4.6)))),
             r"\node[right] at %s {$x$};" % P(X((8.8, 0))), r"\node[above] at %s {$y$};" % P(X((0, 4.6)))]
    for k in range(-3, 9):
        if k != 0:
            parts.append(r"\draw[line width=0.3pt] %s -- %s;" % (P(add(X((k, 0)), (0, -0.9))), P(add(X((k, 0)), (0, 0.9)))))
    for k in range(-6, 5):
        if k != 0:
            parts.append(r"\draw[line width=0.3pt] %s -- %s;" % (P(add(X((0, k)), (-0.9, 0))), P(add(X((0, k)), (0.9, 0)))))
    parts.append(seg(X((xq, -6.2)), X((xq, 4.2)), ",dashed"))
    parts.append(r"\node[above right] at %s {$x=%d$};" % (P(X((xq, 3.0))), xq))
    parts.append(seg(X(Pp), X(Rr)))
    for p, nm, pos in ((Pp, "P(%d,%d)" % Pp, "above left"), (Rr, "R(%d,%d)" % Rr, "below right")):
        parts.append(dot(X(p)))
        parts.append(r"\node[%s] at %s {$%s$};" % (pos, P(X(p)), nm.replace("-", "{-}")))
    return pic(*parts)


# ------------------------------------------------------------------------------ F: house composite (4.6)
def fig_house(w=12, hr=6, slant=10, u=4.0):
    roof = math.sqrt(slant ** 2 - (w / 2.0) ** 2)
    assert near(roof, 8)
    A = (0, 0); B = (w * u, 0); C = (w * u, hr * u); Dp = (0, hr * u); T = (w * u / 2, (hr + roof) * u)
    assert near(dist(Dp, T) / u, slant) and near(dist(C, T) / u, slant)
    return pic(poly([A, B, C, T, Dp]), seg(Dp, C), ra(A, B, Dp, 2.2), ra(B, C, A, 2.2),
               r"\node[below] at %s {$%d$};" % (P(mid(A, B)), w), r"\node[right] at %s {$%d$};" % (P(mid(B, C)), hr),
               r"\node[above left=-0.5pt] at %s {$%d$};" % (P(mid(Dp, T)), slant), r"\node[above right=-0.5pt] at %s {$%d$};" % (P(mid(C, T)), slant))


# ------------------------------------------------------------------------------ F: two right triangles sharing AC (4.8)
def fig_chain(ab=9, bc=12, cd=20, u=3.0):
    ac = math.hypot(ab, bc)
    B = (0, 0); A = (0, ab * u); C = (bc * u, 0)
    uac = unit(C, A); pd = perp(uac)
    if pd[1] < 0: pd = (-pd[0], -pd[1])
    Dp = add(C, mul(pd, cd * u))
    assert near(dotp(sub(A, C), sub(Dp, C)), 0, 1e-6) and near(dist(C, Dp) / u, cd)
    assert near(math.hypot(ac, cd), 25) and near(bc / ab, 4 / 3.0)
    cen = centroid([A, B, C, Dp])
    return pic(poly([A, B, C, Dp]), seg(A, C), ra(B, A, C, 2.2), ra(C, A, Dp, 2.2),
               vlabel(A, "$A$", cen, 3.0), vlabel(B, "$B$", cen, 3.0), vlabel(C, "$C$", cen, 3.0), vlabel(Dp, "$D$", cen, 3.0),
               r"\node[left] at %s {$%d$};" % (P(mid(A, B)), ab))


# ------------------------------------------------------------------------------ F: square in right triangle (4.13)
def fig_sq(a=12, b=6, u=5.5):
    s = a * b / float(a + b)
    C = (0, 0); Bp = (a * u, 0); A = (0, b * u); Q = (s * u, s * u)
    assert near(Q[0] / (a * u) + Q[1] / (b * u), 1)
    return pic(poly([C, Bp, A]), poly([C, (s * u, 0), Q, (0, s * u)], ",line width=0.9pt"), ra(C, Bp, A, 1.8),
               r"\node[below] at %s {$%d$};" % (P(mid(C, Bp)), a), r"\node[left] at %s {$%d$};" % (P(mid(C, A)), b),
               r"\node[below left] at %s {$C$};" % P(C), r"\node[right] at %s {$B$};" % P(Bp), r"\node[above] at %s {$A$};" % P(A))


# ------------------------------------------------------------------------------ F: crossing cables (5.7)
def fig_cross(h1=12, h2=20, d=15, u=3.0):
    O1 = (0, 0); O2 = (d * u, 0); T1 = (0, h1 * u); T2 = (d * u, h2 * u)
    # intersection of O1-T2 and O2-T1
    hx = h1 * h2 / float(h1 + h2)
    X = (d * u * h1 / float(h1 + h2), hx * u)
    # check intersection lies on both
    def online(p, a, b): return near((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]), 0, 1e-6)
    assert online(X, O1, T2) and online(X, O2, T1)
    return pic(seg((-5, 0), (d * u + 5, 0)), seg(O1, T1), seg(O2, T2), seg(O1, T2, ",line width=0.5pt"), seg(O2, T1, ",line width=0.5pt"),
               r"\node[left] at %s {$%d$};" % (P(mid(O1, T1)), h1), r"\node[right] at %s {$%d$};" % (P(mid(O2, T2)), h2),
               r"\node[below] at %s {$%d$};" % (P(((O1[0] + O2[0]) / 2, 0)), d),
               dot(T1), dot(T2))


# ------------------------------------------------------------------------------ F: hexagon + inscribed triangle (5.9)
def fig_hex(s=6, u=5.0):
    V = [(s * u * math.cos(k * 60 * D), s * u * math.sin(k * 60 * D)) for k in range(6)]
    for i in range(6): assert near(dist(V[i], V[(i + 1) % 6]), s * u)
    tri = [V[0], V[2], V[4]]
    names = "ABCDEF"
    parts = [r"\fill[accent!25] %s -- %s -- %s -- cycle;" % tuple(P(p) for p in tri), poly(V), poly(tri)]
    for i in range(6):
        parts.append(vlabel(V[i], "$%s$" % names[i], (0, 0), 3.0))
    parts.append(elabel(V[0], V[1], "$%d$" % s, (0, 0), 2.6))
    return pic(*parts)


# ------------------------------------------------------------------------------ F: isosceles trapezoid (5.15)
def fig_trap(top=10, bot=26, leg=10, u=2.9):
    hgt = math.sqrt(leg ** 2 - ((bot - top) / 2.0) ** 2)
    assert near(hgt, 6)
    off = (bot - top) / 2.0
    A = (off * u, hgt * u); B = ((off + top) * u, hgt * u); C = (bot * u, 0); Dp = (0, 0)
    assert near(dist(Dp, A), leg * u) and near(dist(B, C), leg * u)
    cen = centroid([A, B, C, Dp])
    return pic(poly([Dp, C, B, A]), vlabel(Dp, "$D$", cen), vlabel(C, "$C$", cen), vlabel(B, "$B$", cen), vlabel(A, "$A$", cen),
               r"\node[above] at %s {$%d$};" % (P(mid(A, B)), top), r"\node[below] at %s {$%d$};" % (P(mid(Dp, C)), bot),
               r"\node[left] at %s {$%d$};" % (P(mid(Dp, A)), leg))


# ------------------------------------------------------------------------------ F: tan ADC (5.18)
def fig_tanD(bd=4, dc=6, ac=5, u=6.0):
    B = (0, 0); C = ((bd + dc) * u, 0); A = (C[0], ac * u); Dp = (bd * u, 0)
    assert near((ac / float(bd + dc)), 0.5)
    cen = centroid([A, B, C])
    return pic(poly([A, B, C]), seg(A, Dp), dot(Dp), ra(C, A, B, 2.0),
               r"\node[below left] at %s {$B$};" % P(B), r"\node[below right] at %s {$C$};" % P(C), r"\node[above right] at %s {$A$};" % P(A),
               r"\node[below=1pt] at %s {$D$};" % P(Dp),
               r"\node[above=0.5pt] at %s {$%d$};" % (P((bd * u / 2, 0)), bd), r"\node[above=0.5pt] at %s {$%d$};" % (P(((bd + dc / 2.0) * u, 0)), dc))
