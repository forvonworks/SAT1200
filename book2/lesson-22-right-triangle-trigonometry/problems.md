# Book 2 — Lesson 22: Right-Triangle Trigonometry — Problem Sets

**Source content file**, paired with `concepts.md`. Rounding convention used
throughout: side lengths round to the **nearest hundredth** (2 decimal
places), angles round to the **nearest tenth of a degree**. All numeric
answers verified by Python script (`math` module, degree mode via
`math.radians`/`math.degrees`) before finalizing — not hand-computed.

---

## Set 1 — Identify Opposite / Adjacent / Hypotenuse

For each triangle and angle given, name which side is the **opposite
leg**, which is the **adjacent leg**, and which is the **hypotenuse**.
Items are paired (1&2, 3&4, 5&6) — same triangle, different angle — on
purpose, so the opposite/adjacent swap is unavoidable to notice.

Right triangle $ABC$, right angle at $C$.

1. For angle $A$: name the opposite leg, adjacent leg, and hypotenuse.
2. For angle $B$ (same triangle): name the opposite leg, adjacent leg, and hypotenuse.

Right triangle $PQR$, right angle at $Q$.

3. For angle $P$: name the opposite leg, adjacent leg, and hypotenuse.
4. For angle $R$ (same triangle): name the opposite leg, adjacent leg, and hypotenuse.

Right triangle $XYZ$, right angle at $Y$, hypotenuse $XZ$.

5. For angle $X$: name the opposite leg, adjacent leg, and hypotenuse.
6. For angle $Z$ (same triangle): name the opposite leg, adjacent leg, and hypotenuse.

## Set 2 — Compute the Three Ratios (Exact Fractions)

For each right triangle, find $\sin\theta$, $\cos\theta$, $\tan\theta$ for
the specified angle. Reduce fractions to simplest form.

1. Legs $3$ and $4$, hypotenuse $5$. $\theta$ is opposite the leg of length $3$.
2. Same triangle as #1. $\theta$ is opposite the leg of length $4$.
3. Legs $5$ and $12$, hypotenuse $13$. $\theta$ is opposite the leg of length $5$.
4. Same triangle as #3. $\theta$ is opposite the leg of length $12$.
5. Legs $8$ and $15$, hypotenuse $17$. $\theta$ is opposite the leg of length $8$.
6. Legs $7$ and $24$, hypotenuse $25$. $\theta$ is opposite the leg of length $24$.

## Set 3 — Solve for a Missing Side

Round to the nearest hundredth.

1. Hypotenuse $=12$, angle $=25°$. Find the opposite side.
2. Hypotenuse $=18$, angle $=40°$. Find the adjacent side.
3. Adjacent $=10$, angle $=55°$. Find the opposite side.
4. Opposite $=9$, angle $=32°$. Find the hypotenuse.
5. Hypotenuse $=22$, angle $=63°$. Find the adjacent side.
6. Adjacent $=14$, angle $=47°$. Find the hypotenuse.

## Set 4 — Solve for a Missing Angle

Round to the nearest tenth of a degree.

1. Opposite $=6$, hypotenuse $=14$. Find the angle.
2. Adjacent $=9$, hypotenuse $=20$. Find the angle.
3. Opposite $=11$, adjacent $=15$. Find the angle.
4. Opposite $=18$, hypotenuse $=30$. Find the angle.
5. Adjacent $=21$, opposite $=25$ (relative to the same angle). Find the angle.
6. Adjacent $=13$, hypotenuse $=37$. Find the angle.

## Set 5 — Mixed Applied Problems

Round to the nearest hundredth unless stated otherwise.

1. A ladder $12$ ft long leans against a wall, making a $68°$ angle with
   the ground. How high up the wall does it reach?
2. A ramp rises over a horizontal distance of $40$ ft at an angle of $10°$.
   How long is the ramp itself (the hypotenuse)?
3. From a point $100$ m from the base of a tower, the angle of elevation
   to the top of the tower is $38°$. Find the tower's height.
4. A kite string is $65$ m long and makes a $50°$ angle with the ground.
   How far horizontally is the kite from the person holding the string?
5. A right triangle has legs $9$ and $12$. First find the hypotenuse, then
   find the angle opposite the leg of length $9$ (round the angle to the
   nearest hundredth of a degree).
6. An airplane descends at an angle of depression of $6°$ while covering
   $2000$ m of horizontal distance. By how many meters does its altitude
   decrease?

## Set 6 — Spot the Error

Each item mixes a real setup with exactly one broken step. Name the
error, say which rule it breaks, and give the correct answer.

1. Right triangle, right angle at $C$, opposite-to-$A$ leg $BC=5$,
   adjacent-to-$A$ leg $AC=12$, hypotenuse $AB=13$. Find $\sin A$.
   *Noto'g'ri yechim:* "$\sin A = \dfrac{12}{13}$, chunki $12$ — uzunroq
   katet."
2. Same triangle as #1. Find $\cos B$ (the angle at vertex $B$, not $A$).
   *Noto'g'ri yechim:* "Burchak $A$ uchun qo'shni katet $AC=12$ edi, shuning
   uchun $\cos B = \dfrac{12}{13}$ ham."
3. Find $\sin 30°$.
   *Noto'g'ri yechim:* "Kalkulyatorga $30$ ni kiritib, $\sin 30 \approx
   -0.988$ chiqdi, demak javob $-0.988$."
4. Given $\sin\theta = 0.6$, find $\theta$.
   *Noto'g'ri yechim:* "$\sin\theta=0.6$, shuning uchun $\theta = 0.6°$."
5. A right triangle has hypotenuse $10$ and one leg $6$. Find the other leg.
   *Noto'g'ri yechim:* "$10^2 + 6^2 = \text{boshqa katet}^2$, demak boshqa
   katet $= \sqrt{136} \approx 11.66$."

## Set 7 — Bonus / Challenge

1. Given $\sin 23° \approx 0.3907$, find $\cos 67°$ without recomputing
   from scratch — use the complementary-angle identity.
2. A right triangle has an acute angle of $34°$. Find the other acute
   angle, and state the relationship between $\sin 34°$ and that angle's
   cosine.
3. A right triangle has hypotenuse $26$ and one acute angle of $42°$. Find
   both legs (round each to the nearest hundredth).
4. A $20$-ft ladder reaches $16$ ft up a wall. Find (a) the angle the
   ladder makes with the ground, (b) the angle it makes with the wall, and
   (c) confirm the two angles are complementary.
5. A plane climbs at a constant angle of $15°$ along a flight path of
   $5000$ m. Find the horizontal distance covered and the altitude gained
   (each rounded to the nearest hundredth).

---

## Answer Key

**Set 1:**
1. Opposite $=BC$, adjacent $=AC$, hypotenuse $=AB$.
2. Opposite $=AC$, adjacent $=BC$, hypotenuse $=AB$ (hypotenuse never changes).
3. Opposite $=QR$, adjacent $=PQ$, hypotenuse $=PR$.
4. Opposite $=PQ$, adjacent $=QR$, hypotenuse $=PR$.
5. Opposite $=YZ$, adjacent $=XY$, hypotenuse $=XZ$.
6. Opposite $=XY$, adjacent $=YZ$, hypotenuse $=XZ$.

**Set 2:**
1. $\sin=\frac35$, $\cos=\frac45$, $\tan=\frac34$
2. $\sin=\frac45$, $\cos=\frac35$, $\tan=\frac43$
3. $\sin=\frac{5}{13}$, $\cos=\frac{12}{13}$, $\tan=\frac{5}{12}$
4. $\sin=\frac{12}{13}$, $\cos=\frac{5}{13}$, $\tan=\frac{12}{5}$
5. $\sin=\frac{8}{17}$, $\cos=\frac{15}{17}$, $\tan=\frac{8}{15}$
6. $\sin=\frac{24}{25}$, $\cos=\frac{7}{25}$, $\tan=\frac{24}{7}$

**Set 3:** 1) $5.07$  2) $13.79$  3) $14.28$  4) $16.98$  5) $9.99$  6) $20.53$

**Set 4:** 1) $25.4°$  2) $63.3°$  3) $36.3°$  4) $36.9°$  5) $50.0°$  6) $69.4°$

**Set 5:**
1. $\approx 11.13$ ft
2. $\approx 40.62$ ft
3. $\approx 78.13$ m
4. $\approx 41.78$ m
5. Hypotenuse $=15$; angle $=\arcsin\left(\frac{9}{15}\right)\approx 36.87°$
6. $\approx 210.21$ m

**Set 6:**
1. Error — picked the longer leg by size instead of identifying which leg
   is actually opposite angle $A$ (opposite/adjacent mislabeling). Correct:
   $\sin A = \frac{5}{13}$.
2. Error — reused angle $A$'s adjacent-leg label ($AC=12$) for angle $B$
   without re-identifying roles for the new angle (the "didn't re-identify
   when the reference angle changed" error). For angle $B$, $AC$ is
   actually the *opposite* leg, and $BC=5$ is adjacent. Correct:
   $\cos B = \frac{5}{13}$.
3. Error — calculator left in radian mode instead of degree mode. Correct:
   $\sin 30° = 0.5$.
4. Error — reported the ratio itself as the angle instead of applying the
   inverse sine function. Correct: $\theta = \arcsin(0.6) \approx 36.9°$.
5. Error — treated the hypotenuse as if it were a leg, adding squares
   instead of subtracting. Correct: other leg $=\sqrt{10^2-6^2}=\sqrt{64}=8$.

**Set 7:**
1. $\cos 67° = \sin 23° \approx 0.3907$ (complementary angles, no new computation needed)
2. Other acute angle $=56°$; $\cos 56° = \sin 34°$ (both $\approx 0.5592$)
3. Opposite $\approx 17.40$, adjacent $\approx 19.32$
4. (a) $\approx 53.13°$ with the ground, (b) $\approx 36.87°$ with the wall,
   (c) $53.13°+36.87°=90°$ ✓ — complementary, as expected since they're the
   two acute angles of the same right triangle.
5. Horizontal distance $\approx 4829.63$ m; altitude gained $\approx 1294.10$ m
