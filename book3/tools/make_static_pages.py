#!/usr/bin/env python3
"""Generate Book 3 front matter, section openers, back cover and green dedication (tex) from Book 2 templates."""
import re, os
os.chdir('/home/user/SAT1200/book3')

def bulletize(tex):
    """Turn the 2-column bullet tabulars into hanging-indent paragraphs (aligned bullets)."""
    def conv(m):
        body = m.group(1)
        rows = [r.strip() for r in re.split(r'\\\\(?:\[[^\]]*\])?', body) if r.strip()]
        out = []
        for r in rows:
            r = re.sub(r'^\{\\color\{accent\}\\Large\\textbullet\}\s*&\s*', '', r)
            out.append(r'\par\vspace{2.2mm}\noindent\hangindent=7mm\hangafter=1 \hspace{1mm}{\color{accent}\textbullet}\hspace{3.5mm}' + r)
        return '\n'.join(out) + r'\par'
    return re.sub(r'\\begin\{tabular\}\{@\{\}p\{5mm\}p\{150mm\}@\{\}\}(.*?)\\end\{tabular\}', conv, tex, flags=re.S)

def recolor(s):
    return (s.replace('602785','0F6A52').replace('B8A0C8','A9CFC2').replace('F5F0F9','EDF5F2'))
# ---- front matter (title, copyright, about) ----
f = recolor(open('../book2/front-matter.tex').read())
f = f.replace("2-KITOB \\textperiodcentered\\ ASOSIY MAVZULAR", "3-KITOB \\textperiodcentered\\ \\textapprox800")
f = f.replace("SAT matematikasining asosiy mavzulari to'liq ingliz tilida", "Master SAT tricks for perfect score")
f = f.replace(r"\textapprox", r"$\approx$")
a = f.index(r'\textbf{SAT 1200+} --- Digital'); e = f.index('}\n\\end{textblock*}', a)
about = r"""\textbf{SAT 1200+} --- Digital SAT imtihonining matematika bo'limiga tayyorlanish uchun yozilgan uch kitoblik seriya. \textbf{3-kitob} --- seriyaning cho'qqisi: eng qiyin savollarni yechish, vaqtni tejaydigan usullar va to'liq hajmli mock testlar orqali \textbf{≈800} ballga tayyorlanish.

\vspace{4mm}
Bu kitobda yangi mavzu emas, balki \emph{tanish mavzularning qiyin ko'rinishi} o'rgatiladi: qiyin SAT savollari odatda siz biladigan 2--3 qoidani zanjirga ulaydi yoki oddiy masalani g'ayrioddiy shaklda yashiradi. Barcha masalalar original, javoblari esa tekshirilgan; ular College Board'ning rasmiy savollar bazasi \emph{usullari} tahlili asosida yozilgan.

\vspace{4mm}
\textbf{Har bir darsning tuzilishi:}

\vspace{2mm}
\begin{tabular}{@{}p{10mm}p{150mm}@{}}
1. & \textbf{Qoida/Formula sahifasi (Rules sheet)} --- eng muhim qoidalar va usullar, qisqa misollar bilan; oxirida 10--15 ta yangi so'z (New words). QR kod orqali video darsni ko'ring. \\[3mm]
2. & \textbf{Mashqlar (Problems)} --- 5 ta to'plam: bosqichma-bosqich qiyinlashib, "Summit" to'plamida eng qiyin masalalar. \\[3mm]
3. & \textbf{Qaydlar uchun} --- har bir darsdan keyin o'zingiz yozib borishingiz uchun bo'sh sahifa. \\[3mm]
4. & \textbf{Javoblar (Answer key)} --- har bir masala uchun qisqa yechim va qo'llanilgan usul nomi. \\
\end{tabular}

\vspace{4mm}
Kitob oxirida \textbf{10 ta to'liq mock test} (har biri: 1-modul va qiyinroq 2-modul, 22 savoldan, 35 daqiqadan) berilgan. Mock testlarning javoblari testdan keyin emas, kitobning eng oxirida, \textbf{Answer sheets} bo'limida beriladi.

"""
f = f[:a] + about + f[e:]
open('front-matter.tex', 'w').write(f)
# ---- back cover ----
b = recolor(open('../book2/back-cover.tex').read())
a = b.index(r"\textbf{SAT 1200+} seriyasining"); e = b.index('}\n\\end{textblock*}', a)
b = b[:a] + r"""\textbf{SAT 1200+} seriyasining \textbf{3-kitobi} sizni qiyin savollar bilan ishlashga, vaqtni tejaydigan usullarga va haqiqiy imtihon tuzilishidagi to'liq mock testlarga tayyorlaydi --- maqsad \textbf{≈800}."""+"\n" + b[e:]
a = b.index(r"23 ta dars"); e = b.index('\\\\\n\\end{tabular}', a)
b = b[:a] + r"""9 ta dars, har biri \textbf{qoida sahifasi}, \textbf{yangi so'zlar} va QR kod orqali \textbf{video dars} bilan \\[3mm]
{\color{accent}\Large\textbullet} & Har bir darsda 5 ta qiyin mashq to'plami va \textbf{har bir masalaga to'liq yechim} \\[3mm]
{\color{accent}\Large\textbullet} & \textbf{10 ta to'liq mock test}: 1-modul va qiyinroq 2-modul, javoblar kitob oxirida \\[3mm]
{\color{accent}\Large\textbullet} & Original masalalar, tekshirilgan javoblar --- rasmiy savollar bazasining \emph{usullari} asosida""" + b[e:]
b = b.replace(r"\textbf{2-kitob} (Asosiy mavzular)", r"\textbf{2-kitob} (Asosiy mavzular)")
b = bulletize(b)
open('back-cover.tex', 'w').write(b)
# ---- dedication green ----
d = open('../dedication/dedication-page.tex').read().replace('602785','0F6A52').replace('B8A0C8','A9CFC2')
open('dedication-page.tex', 'w').write(d)
# ---- section openers (mock tests / answer sheets) from the dedication preamble ----
pre = d[:d.index(r'\begin{document}')]
pre += r'''
\newcommand{\pagefooter}[1]{%
\begin{textblock*}{194mm}(8mm,286.41mm)
  \begin{tikzpicture}\fill[accent] (0,0) rectangle (194mm,0.6mm);\end{tikzpicture}
\end{textblock*}
\begin{textblock*}{63.59mm}(8mm,288.27mm)
  {\sffamily\bfseries\color{accent}\fontsize{13}{16}\selectfont SAT 1200+}
\end{textblock*}
\begin{textblock*}{10mm}(188mm,288.27mm)
  \centering{\sffamily\color{accent}\fontsize{14}{16}\selectfont #1}
\end{textblock*}}
\newcommand{\frontheader}[1]{%
\begin{textblock*}{194mm}(16mm,16mm)
\begin{tikzpicture}\node[font=\sffamily\bfseries\fontsize{15}{16}\selectfont,text=ink,anchor=west] at (0,0) {#1};\end{tikzpicture}
\end{textblock*}
\begin{textblock*}{194mm}(16mm,22.5mm)
\begin{tikzpicture}\fill[accent] (0,0) rectangle (194mm,0.5mm);\end{tikzpicture}
\end{textblock*}}
'''
pre = pre.replace(r'\usepackage[absolute]{textpos}', r'\usepackage[absolute]{textpos}' + '\n\\usepackage{array}')
mocks = pre + r'''
\begin{document}
\frontheader{Mock Tests}
\pagefooter{@@PAGE@@}
\mbox{}
\begin{textblock*}{170mm}(20mm,40mm)
{\fontsize{11}{17}\selectfont\color{ink}
\textbf{10 ta to'liq mock test.} Har bir mock --- haqiqiy Digital SAT Math tuzilishi: ikki modul, har biri 22 savol, 35 daqiqa.

\vspace{4mm}
\textbf{1-modul} --- hamma uchun bir xil, oson, o'rta va qiyin savollar aralashmasi (taxminan 8 oson, 11 o'rta, 3 qiyin). Haqiqiy testda 1-moduldagi natijangiz 2-modulning qaysi versiyasini olishingizni belgilaydi.

\vspace{2mm}
\textbf{2-modul} --- bu kitobda doim \emph{qiyinroq yo'nalish} (taxminan 2 oson, 10 o'rta, 10 qiyin). Chunki yuqori ballga faqat shu yo'l olib boradi.

\vspace{4mm}
\textbf{Vaqt rejasi (har bir modulda):}

\vspace{1mm}
\begin{tabular}{@{}p{5mm}p{150mm}@{}}
{\color{accent}\Large\textbullet} & 1--15-savollar: taxminan 18 daqiqa --- tez va aniq, shubhali savolni belgilab keting. \\[2mm]
{\color{accent}\Large\textbullet} & 16--22-savollar: taxminan 17 daqiqa --- eng qiyin savollar oxirida joylashgan. \\[2mm]
{\color{accent}\Large\textbullet} & So'nggi 2--3 daqiqa: belgilangan savollarga qaytish va barcha bo'sh javoblarni to'ldirish --- bo'sh javob nol ball, taxmin esa yo'q. \\
\end{tabular}

\vspace{4mm}
\textbf{Qanday ishlash kerak:} har bir modulni o'z vaqtida, kalkulyator bilan (Desmos) bajaring. Modullar orasida 5--10 daqiqa dam oling. Javoblarni \textbf{tekshirmang} --- ikkala modulni tugatgach, kitob oxiridagi \textbf{Answer sheets} bo'limida (Mock Test raqami bo'yicha) javoblarni solishtiring. Har bir xato savol uchun uning sohasi (ALG, ADV, PSDA, GT) va darajasini belgilab boring --- shu ro'yxat sizga qaysi darsga qaytish kerakligini aytadi.

\vspace{4mm}
\textit{Haftasiga 1--2 ta mock yetarli: hammasini bir haftada ishlash shoshqaloqlikka va noto'g'ri xulosalarga olib keladi.}
}
\end{textblock*}
\end{document}
'''
open('mocks-opener.tex', 'w').write(bulletize(mocks))
answers = pre + r'''
\begin{document}
\frontheader{Answer Sheets}
\pagefooter{@@PAGE@@}
\mbox{}
\begin{textblock*}{170mm}(20mm,40mm)
{\fontsize{11}{17}\selectfont\color{ink}
Bu bo'limda 10 ta mock testning javoblari berilgan --- har bir mock uchun bitta sahifa. Faqat ikkala modulni ham tugatgandan keyin oching.

\vspace{4mm}
\textbf{Har bir sahifada:} har bir savol uchun javob, soha (\textbf{ALG} --- Algebra, \textbf{ADV} --- Advanced Math, \textbf{PSDA} --- Problem-Solving \& Data Analysis, \textbf{GT} --- Geometry \& Trigonometry) va daraja (\textbf{E} --- oson, \textbf{M} --- o'rta, \textbf{H} --- qiyin). Yulduzcha (*) bilan belgilangan savollar --- javobni o'zingiz yozadigan (grid-in) savollar.

\vspace{4mm}
\textbf{Xatolar bilan ishlash:}

\vspace{1mm}
\begin{tabular}{@{}p{5mm}p{150mm}@{}}
{\color{accent}\Large\textbullet} & Xato qilgan savollaringizning sohasini sanang: bitta sohada ko'p xato bo'lsa, tegishli darsga qayting. \\[2mm]
{\color{accent}\Large\textbullet} & 1-modulda oson (E) savolda xato qilgan bo'lsangiz --- bu bilim emas, e'tibor muammosi; sekinroq va aniqroq ishlang. \\[2mm]
{\color{accent}\Large\textbullet} & 2-moduldagi qiyin (H) savollarni yecha olmagan bo'lsangiz --- tegishli darsdagi "Summit" to'plamini qayta ishlang. \\[2mm]
{\color{accent}\Large\textbullet} & Vaqt yetmagan bo'lsa --- bu tezlik muammosi: 5-dars (Speed Tricks) ni takrorlang. \\
\end{tabular}
}
\end{textblock*}
\end{document}
'''
open('answers-opener.tex', 'w').write(bulletize(answers))
print('ok')
