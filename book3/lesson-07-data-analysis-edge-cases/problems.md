# Book 3 — Lesson 7: Data Analysis Edge Cases — Problem Sets

All problems are original. Every answer and every worked solution below is recomputed by `verify.py` (exact fractions, brute force, least-squares fits and simulated data sets), which prints OK/FAIL for each item. The digital SAT has a built-in Desmos graphing calculator, so a calculator is allowed on every problem. **Grid-in** = student-produced response: write a number (fractions and decimals are accepted; negative answers are allowed).

---

## Set 1 — Bridge: the core moves  (Medium / Hard)

1. *(Medium)* **Grid-in.** The mean of 7 numbers is 24. After one of the numbers is removed, the mean of the remaining 6 numbers is 26. What number was removed?

2. *(Medium)* A data set consists of the values $12,\ 15,\ 15,\ 18,\ 20$. The value $40$ is added to the data set. Which of the following statistics is the same for the original data set and the new data set?

   - (A) The mode
   - (B) The mean
   - (C) The median
   - (D) The range

3. *(Medium)* Data set $A$ is $10,\ 20,\ 30,\ 40,\ 50$ and data set $B$ is $28,\ 29,\ 30,\ 31,\ 32$. Which of the following is true?

   - (A) The two data sets have the same mean, and $B$ has the greater standard deviation.
   - (B) The two data sets have the same mean, and $A$ has the greater standard deviation.
   - (C) The two data sets have the same mean and the same standard deviation.
   - (D) Data set $A$ has the greater mean, and the standard deviations are equal.

4. *(Medium)* **Grid-in.** The table shows the number of points earned on a quiz by 20 students.

| Points on the quiz | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Number of students | 2 | 3 | 6 | 5 | 4 |

What is the mean number of points per student?

5. *(Medium)* A teacher uses the line of best fit $y=2.5x+41$ to predict a student's exam score $y$ from the number of hours $x$ the student studied. Which statement is the best interpretation of the number $2.5$ in this context?

   - (A) A student who does not study is predicted to score $2.5$ points.
   - (B) Each additional point on the exam requires $2.5$ more hours of study.
   - (C) For each additional hour of study, the predicted exam score increases by $2.5$ points.
   - (D) A student who studies $2.5$ hours is predicted to score $41$ points.

6. *(Medium)* The table shows the language class chosen by 180 students.

|  | Spanish | French | German | Total |
|---|---|---|---|---|
| Grade 10 | 40 | 25 | 15 | 80 |
| Grade 11 | 30 | 18 | 12 | 60 |
| Grade 12 | 20 | 12 | 8 | 40 |
| Total | 90 | 55 | 35 | 180 |

If a student who takes French is selected at random, what is the probability that the student is in grade 11?

   - (A) $\dfrac{1}{10}$
   - (B) $\dfrac{3}{10}$
   - (C) $\dfrac{11}{36}$
   - (D) $\dfrac{18}{55}$

7. *(Hard)* In a random sample of 900 adult residents of a city, 62\% said they favor extending the library's opening hours. The margin of error for this estimate is 3 percentage points. Which of the following is the most appropriate conclusion?

   - (A) It is plausible that the percent of all adult residents of the city who favor the extension is between $59\%$ and $65\%$.
   - (B) Exactly $62\%$ of all adult residents of the city favor the extension.
   - (C) Between $59\%$ and $65\%$ of the 900 adults surveyed favor the extension.
   - (D) There is only a $3\%$ chance that the survey result is wrong.

8. *(Medium)* A librarian randomly selects 120 names from the list of all 2,400 registered members of a public library and asks them about the new borrowing hours; 78 of the 120 approve. What is the largest group to which the result can reasonably be generalized?

   - (A) Only the 120 members who were surveyed
   - (B) All 2,400 registered members of the library
   - (C) All residents of the city where the library is located
   - (D) All public library members in the country

9. *(Hard)* The table shows a data set of 11 values.

| Value | 1 | 3 | 5 | 6 | 7 | 9 | 20 |
|---|---|---|---|---|---|---|---|
| Frequency | 2 | 2 | 3 | 1 | 1 | 1 | 1 |

The value $20$ is removed from the data set. Which statement is true about the new data set?

   - (A) The mean and the median both decrease.
   - (B) The mean does not change, and the median decreases.
   - (C) The mean decreases, and the median does not change.
   - (D) The mean and the median both stay the same.

10. *(Medium)* **Grid-in.** Maya's mean score on her first 4 tests is 78. What score does she need on her 5th test to raise the mean of all 5 tests to 80?

11. *(Hard)* Each of three independent safety checks on a machine passes with probability $0.9$. What is the probability that at least one of the three checks fails?

   - (A) $0.1$
   - (B) $0.271$
   - (C) $0.3$
   - (D) $0.729$

12. *(Hard)* **Grid-in.** In a random sample of 250 residents of a town, 45 said they bike to work. Based on this sample, about how many of the town's 8,000 residents bike to work?

---

## Set 2 — Center and spread by reasoning: shifts, scales, outliers, graphs  (Hard)

1. *(Hard)* The heights of the plants in a greenhouse have a mean of 30 centimeters and a standard deviation of 4 centimeters. Each height $h$ is converted to a code $c=10h-25$. What are the mean and the standard deviation of the codes?

   - (A) Mean $275$, standard deviation $15$
   - (B) Mean $300$, standard deviation $40$
   - (C) Mean $275$, standard deviation $4$
   - (D) Mean $275$, standard deviation $40$

2. *(Hard)* **Grid-in.** A data set has a standard deviation of 4. Every value in the data set is multiplied by $-3$ and then increased by 10. What is the standard deviation of the new data set?

3. *(Hard)* Each bar graph shows a data set of 20 values, each value between 1 and 5. The number above a bar is how many times that value occurs.

*[Figure: Data set A: bar graph (value: number of data values): 1: 1, 2: 3, 3: 12, 4: 3, 5: 1]*

*[Figure: Data set B: bar graph (value: number of data values): 1: 7, 2: 2, 3: 2, 4: 2, 5: 7]*

*[Figure: Data set C: bar graph (value: number of data values): 1: 4, 2: 4, 3: 4, 4: 4, 5: 4]*

Which of the following lists the data sets in order from the smallest standard deviation to the largest?

   - (A) A, C, B
   - (B) A, B, C
   - (C) B, C, A
   - (D) C, A, B

4. *(Hard)* A data set has 9 values: $4,\ 6,\ 7,\ 7,\ 8,\ 9,\ 9,\ 10,\ 12$. A tenth value, $45$, is added. Which statement is true about the effect on the mean and the median?

   - (A) The median increases by more than the mean does.
   - (B) The mean and the median increase by the same amount.
   - (C) The mean increases by more than the median does.
   - (D) The mean increases, but the median does not change.

5. *(Hard)* Data set $P$ is $10,\ 12,\ 14,\ 15,\ 15,\ 16,\ 18,\ 20$. Data set $Q$ is $3,\ 14,\ 15,\ 15,\ 15,\ 15,\ 16,\ 27$. Both have 8 values and the same mean. Which statement is true?

   - (A) $Q$ has the greater range and the greater IQR.
   - (B) $Q$ has the smaller range and the smaller IQR.
   - (C) $Q$ has the smaller range and the greater IQR.
   - (D) $Q$ has the greater range and the smaller IQR.

6. *(Hard)* The box plots summarize the masses of the animals in two groups.

*[Figure: box plots of Mass (kilograms), drawn to scale. Group X: minimum 12, first quartile 18, median 24, third quartile 30, maximum 40; Group Y: minimum 14, first quartile 20, median 22, third quartile 25, maximum 36]*

Based on the box plots, which of the following must be true?

   - (A) The mean of group X is greater than the mean of group Y.
   - (B) The IQR of group X is greater than the IQR of group Y.
   - (C) The range of group Y is greater than the range of group X.
   - (D) The median of group Y is greater than the median of group X.

7. *(Hard)* **Grid-in.** The mean annual salary of 10 employees at a small company is \$52,000. A new employee earning \$118,000 is hired. What is the mean annual salary, in dollars, of the 11 employees?

8. *(Hard)* The dot plot shows the number of deliveries an office received each day for 11 days.

*[Figure: dot plot of Number of deliveries (value: number of dots): 4: 1, 5: 2, 6: 3, 7: 3, 8: 1, 12: 1]*

The value $12$ was recorded in error and should have been $22$. Which of the following statistics changes when the data are corrected?

    I. The mean    II. The median    III. The range

   - (A) I and III only
   - (B) I only
   - (C) I and II only
   - (D) I, II and III

9. *(Hard)* A data set of 12 values has a mean of 30 and a standard deviation of 5. A 13th value, equal to 30, is added. Which statement is true about the new data set?

   - (A) The mean stays $30$, and the standard deviation does not change.
   - (B) The mean stays $30$, and the standard deviation increases.
   - (C) The mean stays $30$, and the standard deviation decreases.
   - (D) The mean decreases, and the standard deviation decreases.

10. *(Hard)* **Grid-in.** The mean of 9 recorded values is 41. One value was recorded as $7$ when it should have been $70$. What is the correct mean of the 9 values?

11. *(Hard)* A data set has 20 values. The greatest value is increased by $50$ (it remains the greatest). Which of the following statistics are unchanged?

    I. The mean    II. The median    III. The interquartile range (IQR)

   - (A) II only
   - (B) I and II only
   - (C) I, II and III
   - (D) II and III only

12. *(Hard)* The histogram summarizes the times, in minutes, that 40 students spent on an assignment. Each bar includes its left endpoint but not its right.

*[Figure: histogram. Time (minutes) on the horizontal axis, Frequency on the vertical axis. Bars (class: frequency): 0-10: 5, 10-20: 13, 20-30: 8, 30-40: 6, 40-50: 5, 50-60: 3]*

In which interval must the median time lie?

   - (A) 10 to 20
   - (B) 20 to 30
   - (C) 30 to 40
   - (D) 40 to 50

13. *(Hard)* **Grid-in.** The smallest value in a data set is 7 and the largest value is 19. Each value is multiplied by $2.5$, and then $3$ is added. What is the range of the new data set?

14. *(Hard)* Data set $A$ is $10,\ 12,\ 14,\ 16,\ 18$ and data set $B$ is $30,\ 32,\ 34,\ 36,\ 38$. The two sets are combined into one data set of 10 values. Which statement about the standard deviation of the combined set is true?

   - (A) It is greater than the standard deviation of $A$ and greater than that of $B$.
   - (B) It is equal to the standard deviation of $A$ and of $B$.
   - (C) It is less than the standard deviation of $A$ and of $B$.
   - (D) It is equal to the mean of the standard deviations of $A$ and $B$.

---

## Set 3 — Tables, bounds and two-variable models  (Hard)

1. *(Hard)* **Grid-in.** The table shows the frequency of each value in a data set. The mean of the data set is $2.5$.

| Value | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Frequency | 4 | 6 | $x$ | 2 |

What is the value of $x$?

2. *(Hard)* Twenty students recorded the time they spent on homework, rounded to a whole number of minutes, and the results were grouped as shown.

| Time (minutes) | 20--29 | 30--39 | 40--49 |
|---|---|---|---|
| Number of students | 4 | 6 | 10 |

What is the least possible value of the mean time of the 20 students?

   - (A) $42$
   - (B) $37.5$
   - (C) $33$
   - (D) $30$

3. *(Hard)* **Grid-in.** The scores of 20 students were grouped as shown. All scores are whole numbers.

| Score | 50--59 | 60--69 | 70--79 | 80--89 |
|---|---|---|---|---|
| Number of students | 6 | 4 | 6 | 4 |

What is the greatest possible value of the median score?

4. *(Hard)* Three sections of a course took the same exam. Section 1 had 10 students with a mean score of 70, and Section 2 had 20 students with a mean score of 78. Section 3 had 20 students. The mean score of all 50 students was 80. What was the mean score of Section 3?

   - (A) $92$
   - (B) $87$
   - (C) $80$
   - (D) $34.8$

5. *(Hard)* A survey reported the sizes of the households in a town, as shown in the table.

| Household size | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Percent of households | 18\% | 30\% | 22\% | 20\% | 6\% | 4\% |

What is the median household size?

   - (A) $2$
   - (B) $2.78$
   - (C) $3$
   - (D) $3.5$

6. *(Hard)* A company recorded the number of ads it ran in a week, $x$, and its sales for the week, $y$, in hundreds of dollars. The scatterplot shows 10 weeks of data.

*[Figure: scatterplot, Number of ads on the horizontal axis and Sales (hundreds of dollars) on the vertical axis. Points: (11, 52), (13, 54), (15, 68), (17, 70), (19, 82), (21, 82), (22, 91), (24, 95), (26, 98), (28, 113).]*

Which of the following could be the equation of the line of best fit?

   - (A) $y=3.5x+50$
   - (B) $y=12x+3.5$
   - (C) $y=0.29x+12$
   - (D) $y=3.5x+12$

7. *(Hard)* The line of best fit for the number of minutes of exercise $x$ and the calories burned $y$ is $y=1.8x+12$. A person exercised for 15 minutes and burned 34 calories. What is the residual for this person (actual value minus predicted value)?

   - (A) $-5$
   - (B) $5$
   - (C) $22$
   - (D) $39$

8. *(Hard)* A researcher measured the heights of trees between 5 and 20 years old and found the line of best fit $y=0.8x+14$, where $x$ is age in years and $y$ is height in feet. Which statement about using the model to estimate the height of a 50-year-old tree is best?

   - (A) The model predicts $54$ feet, and this is just as reliable as a prediction for a 12-year-old tree.
   - (B) The model cannot make any prediction because $x=0$ is not in the data.
   - (C) The model predicts $14$ feet, because the intercept is the height at any age.
   - (D) The model predicts $54$ feet, but $50$ years is far outside the ages in the data, so this prediction is an extrapolation and may be unreliable.

9. *(Hard)* The line of best fit for a data set is $y=0.5x+10$. Which of the following data points is farthest from the line, measured vertically?

   - (A) $(12,12)$
   - (B) $(6,15)$
   - (C) $(20,23)$
   - (D) $(30,26)$

10. *(Hard)* **Grid-in.** An exponential model $y=a\cdot b^{t}$, where $a$ and $b$ are positive constants, passes through the points $(1,\ 48)$ and $(3,\ 108)$. According to the model, what is the value of $y$ when $t=5$?

11. *(Hard)* A line of best fit for the fuel used, $y$ (in gallons), on trips of $x$ miles is $y=0.04x+1.2$. Which of the following is the best interpretation of the number $0.04$ in this context?

   - (A) The car travels $0.04$ mile on each gallon of fuel.
   - (B) The model predicts $0.04$ additional gallon of fuel for each additional mile driven.
   - (C) The model predicts $0.04$ gallon of fuel for a trip of $1.2$ miles.
   - (D) Every mile driven uses exactly $0.04$ gallon of fuel.

12. *(Hard)* The table gives five measurements of two variables.

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $y$ | 3 | 6 | 12 | 25 | 47 |

Which of the following equations best models the relationship?

   - (A) $y=11x+3$
   - (B) $y=3x^2+3$
   - (C) $y=3(2)^x$
   - (D) $y=3(1.5)^x$

13. *(Hard)* **Grid-in.** A line of best fit for the percent $y$ of a phone's battery remaining after $x$ hours of use passes through the points $(1,\ 78)$ and $(4,\ 33)$. According to the model, after how many hours of use will the battery reach $0\%$?

14. *(Hard)* The scatterplot shows nine data points, and a line of best fit is calculated for all nine.

*[Figure: scatterplot, $x$ on the horizontal axis and $y$ on the vertical axis. Points: (1, 7), (2, 9), (3, 12), (4, 13), (5, 16), (6, 17), (7, 20), (8, 21), (9, 4).]*

The point $(9,4)$ is removed, and the line of best fit is calculated again for the remaining eight points. Which statement describes the new line compared with the old one?

   - (A) The slope increases, and the $y$-intercept increases.
   - (B) The slope decreases, and the $y$-intercept decreases.
   - (C) The slope decreases, and the $y$-intercept increases.
   - (D) The slope increases, and the $y$-intercept decreases.

---

## Set 4 — Probability, inference and statistical claims  (Hard)

1. *(Hard)* **Grid-in.** A café asked its customers which hot drink they prefer. The results are shown in the table.

| Age group | Prefers coffee | Prefers tea |
|---|---|---|
| Under 30 | 24 | 6 |
| 30 to 59 | 40 | 14 |
| 60 or older | 21 | $x$ |

If one of the customers who prefer tea is chosen at random, the probability that the customer is 60 or older is $\dfrac13$. What is the value of $x$?

2. *(Hard)* A gym surveyed 500 adults about their age and whether they are gym members.

|  | Gym member | Not a member | Total |
|---|---|---|---|
| Under 30 | 96 | 64 | 160 |
| 30 or older | 84 | 256 | 340 |
| Total | 180 | 320 | 500 |

If one of the gym members is chosen at random, what is the probability that this person is under 30?

   - (A) $\dfrac{24}{125}$
   - (B) $\dfrac{8}{25}$
   - (C) $\dfrac{8}{15}$
   - (D) $\dfrac{3}{5}$

3. *(Hard)* **Grid-in.** A school counselor recorded whether students are seniors and whether they belong to a club.

|  | In a club | Not in a club |
|---|---|---|
| Seniors | 18 | $x$ |
| Not seniors | 42 | 140 |

For these students, being a senior and being in a club are independent. What is the value of $x$?

4. *(Hard)* A bag contains 5 red marbles and 3 blue marbles. Two marbles are drawn at random, one after the other, without replacement. What is the probability that at least one of the two marbles is blue?

   - (A) $\dfrac{5}{14}$
   - (B) $\dfrac{3}{8}$
   - (C) $\dfrac{39}{64}$
   - (D) $\dfrac{9}{14}$

5. *(Hard)* A box holds 4 red cards and 6 black cards. Two cards are drawn at random without replacement. What is the probability that the two cards are the same color?

   - (A) $\dfrac{1}{3}$
   - (B) $\dfrac{7}{15}$
   - (C) $\dfrac{13}{25}$
   - (D) $\dfrac{8}{15}$

6. *(Hard)* **Grid-in.** A quality inspector checks items one at a time. Each item independently has a $10\%$ chance of being defective. What is the least number of items the inspector must check so that the probability of finding at least one defective item is greater than $50\%$?

7. *(Hard)* At a school, $55\%$ of the students are in grades 9 and 10, and the rest are in grades 11 and 12. Of the students in grades 9 and 10, $30\%$ take an AP course; of the students in grades 11 and 12, $60\%$ take an AP course. What fraction of the students who take an AP course are in grades 9 and 10?

   - (A) $\dfrac{33}{200}$
   - (B) $\dfrac{3}{10}$
   - (C) $\dfrac{11}{29}$
   - (D) $\dfrac{11}{20}$

8. *(Hard)* In a town of 6,000 residents, $35\%$ own a bicycle. Of the residents who own a bicycle, $40\%$ also own a helmet. About how many of the residents own both a bicycle and a helmet?

   - (A) $840$
   - (B) $2100$
   - (C) $2400$
   - (D) $4500$

9. *(Hard)* Researchers recruited 120 volunteers from a town and randomly assigned 60 of them to follow a new sleep schedule and 60 to keep their usual schedule. After eight weeks the reaction times of the new-schedule group were faster, by an amount too large to be explained by chance. Which conclusion is best supported?

   - (A) The new sleep schedule caused faster reaction times for people like these volunteers, but the result cannot be generalized to all residents of the town.
   - (B) The new sleep schedule caused faster reaction times for all residents of the town.
   - (C) The new sleep schedule is associated with faster reaction times, but the study cannot show that it caused them.
   - (D) No conclusion can be drawn, because the volunteers were not a random sample of the town.

10. *(Hard)* A researcher selected a random sample of 500 adults from a city and asked each whether they eat breakfast every day. The researcher also measured each adult's body mass index (BMI) and found that the adults who eat breakfast daily had a lower mean BMI than those who do not. Which conclusion is best supported?

   - (A) Eating breakfast daily causes lower BMI among the city's adults.
   - (B) There is an association between eating breakfast daily and lower BMI among the city's adults, but the study cannot show that breakfast causes lower BMI.
   - (C) There is an association between eating breakfast and BMI among the 500 adults only, and it cannot be generalized to the city.
   - (D) Eating breakfast daily is associated with lower BMI among all adults in the country.

11. *(Hard)* A poll of a random sample of voters in a city estimated that $48\%$ support Candidate $P$ and $45\%$ support Candidate $Q$. The margin of error for each estimate is $4$ percentage points. Which of the following is best supported by these results?

   - (A) Candidate $P$ has more support than Candidate $Q$ among all voters in the city.
   - (B) Exactly $45\%$ of all voters in the city support Candidate $Q$.
   - (C) Candidate $P$ leads Candidate $Q$ by exactly $3$ percentage points among all voters in the city.
   - (D) It is plausible that Candidate $Q$ has at least as much support as Candidate $P$ among all voters in the city.

12. *(Hard)* A random sample of 400 people gives a poll a margin of error of 5 percentage points. A second poll of the same population uses a random sample of 1,600 people, with the same method and confidence level. Which is the most likely margin of error of the second poll?

   - (A) $1.25$
   - (B) $2.5$
   - (C) $5$
   - (D) $10$

13. *(Hard)* To estimate the percent of adult residents of a city who exercise regularly, a researcher posted a survey on the website of a large fitness gym in the city. Of the 1,500 visitors who responded, $81\%$ said they exercise regularly. Which is the most serious flaw in using the $81\%$ to estimate the percent for all adult residents?

   - (A) The respondents were not a random sample of the city, and visitors to a gym's website are more likely to exercise, so the estimate is probably too high.
   - (B) A sample of 1,500 is too small to estimate anything about a city.
   - (C) The result is too high to be believable, so the survey must contain errors.
   - (D) The researcher did not survey children as well as adults.

14. *(Hard)* **Grid-in.** A researcher estimated the percent of a town's residents who own a car. To estimate the margin of error, she simulated 1,000 random samples; the middle $95\%$ of the simulated sample percents ranged from $41\%$ to $55\%$. What is the margin of error, in percentage points, for her estimate?

---

## Set 5 — Summit: the hardest mixed problems  (Hard)

1. *(Hard)* Data set $P$ has 12 values: 40, 45, 50, 55, 58, 60, 60, 62, 65, 70, 75, 80. Data set $Q$ is formed by adding two more values, both equal to $60$, to data set $P$. Which statement is true?

   - (A) None of the mean, median, range or standard deviation changes.
   - (B) The mean and the standard deviation both decrease; the median and range stay the same.
   - (C) Only the standard deviation changes, and it decreases.
   - (D) The range and the standard deviation both decrease; the mean and median stay the same.

2. *(Hard)* **Grid-in.** Five positive integers have a mean of 12, a median of 10 and a unique mode of 8. What is the greatest possible value of the largest of the five integers?

3. *(Hard)* **Grid-in.** Data set $D$ consists of 8 positive integers, each less than 40. Seven of them are $12,\ 15,\ 15,\ 18,\ 22,\ 25,\ 27$. The mean of all 8 integers is an integer greater than 18. What is the greatest possible value of the eighth integer?

4. *(Hard)* **Grid-in.** A data set of 25 integers is summarized in the table, where each integer lies in the class shown.

| Value | 10--19 | 20--29 | 30--39 | 40--49 |
|---|---|---|---|---|
| Frequency | 4 | 9 | 7 | 5 |

What is the difference between the greatest possible mean and the least possible mean of the data set?

5. *(Hard)* The box plots summarize the scores of two groups of students on the same test.

*[Figure: box plots of Score, drawn to scale. Group X: minimum 10, first quartile 16, median 22, third quartile 34, maximum 52; Group Y: minimum 8, first quartile 20, median 26, third quartile 30, maximum 44]*

Based on the box plots, which of the following must be true?

   - (A) The IQR of group $Y$ is greater than the IQR of group $X$.
   - (B) More than half of the values in group $Y$ are less than $26$.
   - (C) The mean of group $X$ is greater than the mean of group $Y$.
   - (D) At least $25\%$ of the values in group $X$ are greater than or equal to $34$.

6. *(Hard)* The scatterplot shows four labeled points and the line of best fit, $y=2x+10$.

*[Figure: scatterplot, $x$ on the horizontal axis and $y$ on the vertical axis. Points: P (2, 16), Q (5, 12), R (8, 31), S (11, 28). The line of best fit shown is y = 2 x + 10.]*

For which point is the residual (actual value minus predicted value) the least?

   - (A) Point $Q$
   - (B) Point $P$
   - (C) Point $R$
   - (D) Point $S$

7. *(Hard)* **Grid-in.** Of 10,000 items produced in a factory, 200 are defective. A scanner flags 180 of the 200 defective items and also flags 490 of the 9,800 items that are not defective. Of all the items the scanner flags, what percent are defective? (Round to the nearest whole percent.)

8. *(Hard)* A college asked 230 students about their year and the class format (online, in person or hybrid) they prefer.

|  | Online | In person | Hybrid | Total |
|---|---|---|---|---|
| Freshmen | 28 | 36 | 16 | 80 |
| Sophomores | 40 | 24 | 26 | 90 |
| Juniors | 12 | 30 | 18 | 60 |
| Total | 80 | 90 | 60 | 230 |

Which of the following probabilities is the greatest?

   - (A) The probability that a randomly chosen student who prefers in-person classes is a junior
   - (B) The probability that a randomly chosen student who prefers online classes is a freshman
   - (C) The probability that a randomly chosen junior prefers online classes
   - (D) The probability that a randomly chosen sophomore prefers hybrid classes

9. *(Hard)* A bag contains 5 red, 4 blue and 3 green marbles. Two marbles are drawn at random without replacement. What is the probability that both marbles are the same color?

   - (A) $\dfrac{19}{33}$
   - (B) $\dfrac{25}{72}$
   - (C) $\dfrac{19}{66}$
   - (D) $\dfrac{5}{33}$

10. *(Hard)* A random sample of 100 voters gives a poll a margin of error of 9 percentage points. Assuming the same method and confidence level, what is the least sample size that would reduce the margin of error to 3 percentage points?

   - (A) $8100$
   - (B) $900$
   - (C) $600$
   - (D) $300$

11. *(Hard)* Researchers randomly selected 300 students from a school district of 12,000 students and randomly assigned 150 of them to tutoring method 1 and 150 to tutoring method 2. After a semester the method 1 group scored higher, by an amount too large to be explained by chance. Which conclusion is best supported?

   - (A) Method 1 caused higher scores, but only for the 300 students in the study.
   - (B) Method 1 is associated with higher scores among the students in the district, but the study cannot show a cause.
   - (C) Method 1 caused higher scores among all students in the country.
   - (D) Method 1 caused higher scores among the students in the district.

12. *(Hard)* Two independent polls used random samples. In City $A$, $58\%$ of the sample favored a proposal, with a margin of error of $4$ percentage points. In City $B$, $49\%$ of the sample favored it, with a margin of error of $3$ percentage points. Which conclusion is best supported?

   - (A) The intervals $54\%$ to $62\%$ and $46\%$ to $52\%$ do not overlap, so it is reasonable to conclude that the percent in favor is greater among all residents of City $A$ than among all residents of City $B$.
   - (B) The percent in favor among all residents of City $A$ is exactly $9$ points greater than among all residents of City $B$.
   - (C) No comparison is possible, because the two polls have different margins of error.
   - (D) It is plausible that $54\%$ of all residents of City $B$ are in favor.

13. *(Hard)* **Grid-in.** A poll of a random sample of residents estimated that $40\%$ of the town's 12,000 residents support a new park. The margin of error is 5 percentage points. Based on the estimate and the margin of error, what is the least number of the town's residents that plausibly support the new park?

14. *(Hard)* A survey asked 400 men and 600 women whether they would use a proposed bus route. Of the men, $55\%$ said yes; of the women, $45\%$ said yes. What percent of all 1,000 people surveyed said yes?

   - (A) $51\%$
   - (B) $50\%$
   - (C) $49\%$
   - (D) $45\%$

15. *(Hard)* The total cost $y$, in dollars, of a gym membership after $x$ weeks is modeled by $y=12.5x+300$. A new model uses $m$, the number of 4-week months, instead of $x$ (so $x=4m$). Which equation gives $y$ in terms of $m$?

   - (A) $y=12.5m+300$
   - (B) $y=50m+1200$
   - (C) $y=3.125m+300$
   - (D) $y=50m+300$

16. *(Hard)* A data set of 25 values is summarized in the table.

| Value | 1 | 2 | 3 | 4 | 5 | 9 |
|---|---|---|---|---|---|---|
| Frequency | 8 | 6 | 4 | 3 | 2 | 2 |

Which of the following correctly orders the mean, the median and the mode of the data set?

   - (A) mode $<$ median $<$ mean
   - (B) mean $<$ median $<$ mode
   - (C) median $<$ mode $<$ mean
   - (D) mode $<$ mean $<$ median

17. *(Hard)* **Grid-in.** The histogram shows the points a team scored in each of its 40 games. Each bar includes its left endpoint but not its right endpoint, and every score is a whole number.

*[Figure: histogram. Points scored on the horizontal axis, Number of games on the vertical axis. Bars (class: frequency): 0-10: 4, 10-20: 9, 20-30: 13, 30-40: 8, 40-50: 6]*

What is the greatest possible number of games in which the team scored fewer than 35 points?

18. *(Hard)* The scatterplot shows six data points. An exponential model for the data can be written as $y=a(b)^x$, where $a$ and $b$ are positive constants.

*[Figure: scatterplot, $x$ on the horizontal axis and $y$ on the vertical axis. Points: (0, 5), (1, 8), (2, 13), (3, 20), (4, 33), (5, 52).]*

Which of the following is closest to the value of $b$?

   - (A) $0.63$
   - (B) $1.6$
   - (C) $5$
   - (D) $8$

19. *(Hard)* A data set consists of 9 distinct positive integers. The median is 20 and the mean is 24. What is the least possible value of the greatest integer in the data set?

   - (A) $31$
   - (B) $32$
   - (C) $33$
   - (D) $36$

20. *(Hard)* A data set of 20 values is summarized in the table.

| Value | 2 | 3 | 5 | 6 | 7 | 10 |
|---|---|---|---|---|---|---|
| Frequency | 1 | 3 | 3 | 5 | 6 | 2 |

How many of the values are greater than the mean of the data set?

   - (A) $2$
   - (B) $7$
   - (C) $8$
   - (D) $13$

---

## Answer Key

Each entry: answer, a short worked solution, and the trick used.

### Set 1 — Bridge: the core moves

1. **Ans. 12** — Total of the 7 numbers: $7\cdot24=168$. Total of the remaining 6: $6\cdot26=156$. The removed number is $168-156=12$. (Subtracting the means gives 2, which is the change in the mean, not the number.)  *Trick: Work with totals, not means*

2. **A (The mode)** — Before: mean $16$, median $15$, mode $15$, range $8$. After adding $40$: mean $20$, median $\frac{15+18}{2}=16.5$, mode still $15$, range $28$. Only the mode is unchanged. (Many students pick the median because it is ``resistant,'' but with an even count it moves to the average of $15$ and $18$.)  *Trick: Which measure ignores a new extreme value?*

3. **B** — Both sets are centered at $30$ (mean $30$), but $A$ is spread from $10$ to $50$ while $B$ is packed between $28$ and $32$. More spread means a bigger standard deviation, so $A$'s is greater. (Same mean does not mean same spread.)  *Trick: Spread: how far the values sit from the center*

4. **Ans. 2.3** — Total points: $0(2)+1(3)+2(6)+3(5)+4(4)=0+3+12+15+16=46$. Mean $=46\div20=2.3$. (Averaging the five point values, $2$, ignores how many students earned each.)  *Trick: Weighted mean: multiply value by frequency*

5. **C** — The slope is the predicted change in $y$ for a one-unit increase in $x$: one more hour of study adds $2.5$ points. ($2.5$ is not the intercept, which is $41$, and it is points per hour, not hours per point.)  *Trick: Slope = change in $y$ for one more unit of $x$*

6. **D ($\dfrac{18}{55}$)** — The condition ``takes French'' restricts us to the French column, which has $25+18+12=55$ students. Of these, $18$ are in grade 11, so the probability is $\frac{18}{55}$. ($\frac{3}{10}=\frac{18}{60}$ divides by the grade 11 row instead; $\frac1{10}=\frac{18}{180}$ divides by everyone; $\frac{11}{36}=\frac{55}{180}$ is just the chance of taking French.)  *Trick: Conditional probability: the ``given'' group is the denominator*

7. **A** — The margin of error says the population percent is plausibly within $3$ points of the sample estimate: $62\pm3$, i.e. from $59\%$ to $65\%$. (The sample itself is known exactly: $62\%$ of the $900$. The margin of error is not a probability of being wrong.)  *Trick: Estimate $\pm$ margin of error gives a plausible interval for the population*

8. **B** — The sample was drawn at random from the list of registered members, so the result generalizes to those $2{,}400$ members and no further. (The $120$ is too narrow because a random sample is meant to represent the whole list; city residents or members elsewhere were never in the sampling frame.) Conceptual item.  *Trick: Random sample: generalize only to the population it was drawn from*

9. **C** — Sorted: $1,1,3,3,5,5,5,6,7,9,20$. With $11$ values the median is the 6th: $5$. After removing $20$ there are $10$ values and the median is the average of the 5th and 6th, $\frac{5+5}{2}=5$: unchanged. The mean drops from $\frac{65}{11}\approx5.9$ to $\frac{45}{10}=4.5$.  *Trick: Remove an extreme value: the mean moves, the median may not*

10. **Ans. 88** — She needs a total of $5\cdot80=400$ points. She has $4\cdot78=312$, so she needs $400-312=88$. (Using $80+2=82$ forgets that the new mean must also cancel the shortfall of the first four tests.)  *Trick: Work with totals, not means*

11. **B ($0.271$)** — The opposite of ``at least one fails'' is ``all three pass'': $0.9^3=0.729$. So the answer is $1-0.729=0.271$. ($0.729$ is the chance that all pass; $0.3=3(0.1)$ adds the failure chances, which double-counts overlaps; $0.1$ is a single check.)  *Trick: ``At least one'' = 1 minus ``none''*

12. **Ans. 1440** — The sample proportion is $\frac{45}{250}=0.18$. Apply it to the town: $0.18\cdot8000=1440$. (Equivalently, the town is $\frac{8000}{250}=32$ times as large as the sample, and $45\cdot32=1440$. Do not apply $45$ out of $8000$ directly.)  *Trick: Expected count = sample proportion $\times$ population*

### Set 2 — Center and spread by reasoning: shifts, scales, outliers, graphs

1. **D** — The mean goes through the whole formula: $10(30)-25=275$. Subtracting $25$ only slides every value, so spread is unchanged by it; multiplying by $10$ stretches the spread by $10$: $10\cdot4=40$. (SD $15$ subtracts $25$ from the SD; $300$ forgets the $-25$ for the mean; SD $4$ forgets the multiplication.)  *Trick: Linear change: the mean follows the formula, the SD only scales*

2. **Ans. 12** — Adding $10$ does not change the spread. Multiplying by $-3$ flips the data and stretches the distances between values by a factor of $3$. A standard deviation is never negative, so it is multiplied by $|-3|=3$: $3\cdot4=12$. (The answer $-12$ is impossible.)  *Trick: SD scales by $|k|$, shifts do nothing*

3. **A (A, C, B)** — All three sets have mean $3$, so compare how far the values sit from $3$. In $A$ one tall bar at the center (a ``skyrocket'') means most values equal the mean: smallest SD. In $B$ the two tall bars sit at the far ends (a ``double top''): largest SD. $C$ is flat and in between. The order is $A,C,B$. ($C,A,B$ wrongly calls the flat graph the most concentrated; $B,C,A$ is the reverse order.)  *Trick: Skyrocket bar $\Rightarrow$ small SD; double top $\Rightarrow$ large SD*

4. **C** — Before: sum $72$, mean $8$, median $8$. After: sum $117$, mean $11.7$ (up $3.7$). With $10$ values the median is the average of the 5th and 6th: $\frac{8+9}{2}=8.5$ (up only $0.5$). The extreme value pulls the mean a lot and the median a little. (The median does move, because an even count averages two middle values.)  *Trick: An outlier drags the mean far, the median barely*

5. **D** — Ranges: $P$: $20-10=10$; $Q$: $27-3=24$. For the IQR split each set into halves: $P$ has $Q_1=13$, $Q_3=17$, IQR $4$; $Q$ has $Q_1=14.5$, $Q_3=15.5$, IQR $1$. The two extreme values stretch $Q$'s range, but the middle half of $Q$ is tightly packed. Range and IQR can disagree.  *Trick: Range sees the extremes, IQR sees the middle half*

6. **B** — Read the five numbers. $X$: IQR $=30-18=12$, range $28$, median $24$. $Y$: IQR $=25-20=5$, range $22$, median $22$. So only the IQR statement is true. The range of $Y$ is smaller and the median of $Y$ is smaller. A box plot cannot give the mean, so the first statement is not guaranteed.  *Trick: Box plots show median, quartiles, range, IQR: never the mean*

7. **Ans. 58000** — The old total is $10(52{,}000)=520{,}000$. Add the new salary: $638{,}000$. Divide by $11$: $58{,}000$. (Averaging $52{,}000$ and $118{,}000$ gives $85{,}000$, which ignores that ten employees share the old mean.)  *Trick: Work with totals, not means*

8. **A (I and III only)** — Sorted: $4,5,5,6,6,6,7,7,7,8,12$. The median is the 6th value, $6$, and stays $6$ after $12\to22$ (the order of the middle values does not change). The mean rises, since the total rises by $10$. The range rises from $12-4=8$ to $22-4=18$. So I and III change; II does not.  *Trick: Which measure sees the corrected extreme value?*

9. **C** — A new value equal to the mean adds $30$ to the total and $1$ to the count, so the mean stays $30$. But this value sits exactly at the center, closer to the mean than the other values, so the data become slightly more concentrated and the standard deviation decreases. (It does not stay the same just because the mean did.)  *Trick: A value at the center adds a data point but no spread*

10. **Ans. 48** — The recorded total is $9(41)=369$. The error is $70-7=63$ too low, so the correct total is $369+63=432$. The correct mean is $432\div9=48$. (Adding $63$ to the mean itself is the usual slip; the mean rises by only $\frac{63}{9}=7$.)  *Trick: Correct the total, then divide*

11. **D (II and III only)** — The mean includes every value, so it rises by $\frac{50}{20}=2.5$. The median is the average of the 10th and 11th values and the IQR uses the middle of each half. None of those positions involve the greatest value, so II and III are unchanged. (The range would change too.)  *Trick: Resistant measures ignore the top value*

12. **B (20 to 30)** — With $40$ values the median is the average of the 20th and 21st. Running totals: $5,\ 18,\ 26,\ldots$ The first two bars hold only $18$ values, so the 20th and 21st values both fall in the third bar, $20$ to $30$. (The tallest bar, $10$ to $20$, is the mode interval, not the median interval.)  *Trick: Median bin: count up to the middle position*

13. **Ans. 30** — The original range is $19-7=12$. Adding $3$ moves everything equally, so it cancels in the range; multiplying by $2.5$ scales the range: $2.5\cdot12=30$. (Applying $2.5\cdot12+3=33$ adds the shift to a distance.)  *Trick: Range scales like SD: shifts cancel*

14. **A** — $A$ and $B$ each consist of five evenly spaced values $2$ apart, so they have the same standard deviation. In the combined set the values run from $10$ to $38$, in two clumps far from the combined mean $24$. That is far more spread than either set alone, so the combined standard deviation is greater than both (it is not an average of the two).  *Trick: Two separated clumps spread the combined data*

### Set 3 — Tables, bounds and two-variable models

1. **Ans. 12** — The sum of the values is $1(4)+2(6)+3x+4(2)=24+3x$ and there are $12+x$ values. Set $\frac{24+3x}{12+x}=2.5$: $24+3x=30+2.5x$, so $0.5x=6$ and $x=12$. (Check: total $60$, count $24$, mean $2.5$.)  *Trick: Frequency table: total $=\sum$ value $\times$ frequency*

2. **C ($33$)** — The least possible mean happens when every student is at the bottom of their class: $\frac{4(20)+6(30)+10(40)}{20}=\frac{660}{20}=33$. (Averaging the three lower ends, $30$, ignores the class sizes; $37.5$ uses class midpoints, which is an estimate rather than the least possible; $42$ is the greatest possible mean, using $29,39,49$.)  *Trick: Grouped data: least mean uses every class's lowest value*

3. **Ans. 74** — With $20$ scores the median is the average of the 10th and 11th. Running totals $6,\ 10,\ 16,\ 20$: the 10th score is the largest in the class $60$--$69$, and the 11th is the smallest position in the class $70$--$79$. Make both as large as possible: $69$ and $79$. The greatest median is $\frac{69+79}{2}=74$. (Taking class midpoints, or $79$, ignores that the two middle values sit in different classes.)  *Trick: Median of grouped data: locate the middle two positions*

4. **B ($87$)** — All $50$ students scored $50(80)=4000$ points. Section 1 scored $10(70)=700$ and Section 2 scored $20(78)=1560$. Section 3 scored $4000-700-1560=1740$, so its mean is $1740\div20=87$. ($92=3(80)-70-78$ treats the three section means as equally weighted; $34.8=1740\div50$ divides by the wrong count; $80$ assumes Section 3 matches the overall mean.)  *Trick: Combined mean: add up the totals*

5. **C ($3$)** — Add percents from the smallest size: $18\%$, then $48\%$ (still below $50\%$), then $70\%$. The $50$th percent is reached at size $3$, so the median is $3$. ($2$ is the mode, the most common size; $2.78$ is the mean; $3.5$ is the middle of the sizes $1$ to $6$, which ignores how many households have each size.)  *Trick: Relative-frequency table: find where the running percent passes 50\%*

6. **D ($y=3.5x+12$)** — The data rise about $70$ units over $20$ ads (for example from about $47$ at $x=10$ to about $117$ at $x=30$), so the slope is about $\frac{70}{20}=3.5$. The intercept is the value at $x=0$, not at the left edge of the graph: $47-3.5(10)=12$. So $y=3.5x+12$. ($y=3.5x+50$ reads the height at $x=10$ (about $50$) as the intercept; $y=12x+3.5$ swaps the coefficients; $0.29$ is run over rise.)  *Trick: Best-fit equation: slope from two spread-out points, intercept at $x=0$*

7. **A ($-5$)** — Predicted: $1.8(15)+12=39$. Residual $=34-39=-5$: the actual value is $5$ below the line. ($+5$ reverses the subtraction; $22=34-12$ ignores the slope term; $39$ is the prediction itself, not a residual.)  *Trick: Residual = actual $-$ predicted*

8. **D** — Substituting $x=50$ gives $0.8(50)+14=54$, so the model does give a number. But $50$ is far outside the observed ages ($5$ to $20$), so we cannot trust the linear pattern to continue: extrapolation. Predictions inside the data range are more trustworthy. Conceptual item (the number $54$ is checked).  *Trick: Prediction vs extrapolation*

9. **A $(12,12)$** — Predicted values: $13,\ 16,\ 20,\ 25$. Residuals (actual $-$ predicted): $+2,\ -4,\ +3,\ +1$. The largest in size is $|-4|=4$, at $(12,12)$, even though it is below the line. (Choosing the biggest positive residual gives $(20,23)$.)  *Trick: Farthest from the line: largest residual in size, either sign*

10. **Ans. 243** — Going from $t=1$ to $t=3$ (two steps) multiplies $y$ by $\frac{108}{48}=2.25=b^2$, so $b=1.5$. Going two more steps multiplies by $2.25$ again: $108\cdot2.25=243$. (Adding the same difference, $108+60=168$, treats the model as linear.)  *Trick: Exponential model: equal steps multiply by the same factor*

11. **B** — The slope is the predicted change in $y$ (gallons) for one more unit of $x$ (mile): $0.04$ gallon per mile. It is gallons per mile, not miles per gallon (that would be $\frac1{0.04}=25$), and a line of best fit gives predicted averages, not exact usage.  *Trick: Slope units: ($y$ units) per ($x$ unit)*

12. **C ($y=3(2)^x$)** — Look at consecutive ratios: $\frac63=2,\ \frac{12}6=2,\ \frac{25}{12}\approx2.1,\ \frac{47}{25}\approx1.9$. The ratios are nearly constant, so the data grow exponentially with $b=2$ and $a=3$ (the value at $x=0$). The differences $3,6,13,22$ are not constant, so it is not linear. $y=3(2)^x$ gives $3,6,12,24,48$, which is within $1$ of every value.  *Trick: Table: constant ratio means exponential, constant difference means linear*

13. **Ans. 6.2** — Slope $=\frac{33-78}{4-1}=-15$ percentage points per hour. So $y=78-15(x-1)=93-15x$. Set $y=0$: $x=\frac{93}{15}=6.2$ hours. (Dividing $78$ by $15$ forgets the offset of the first point.)  *Trick: Line through two points: slope, then solve for $y=0$*

14. **D** — Eight points climb steadily (about $2$ per unit of $x$). The last point $(9,4)$ is far to the right and far below the trend, so it drags the right end of the line down: the line with it is flatter. Removing it lets the line steepen, and a steeper line pivoting near the middle of the data must start lower: the $y$-intercept decreases. (Least-squares fits give a slope of about $0.7$ with the point and $2.0$ without it.)  *Trick: A far-away point tilts the line toward itself*

### Set 4 — Probability, inference and statistical claims

1. **Ans. 10** — Customers who prefer tea total $6+14+x=20+x$, and $x$ of them are $60$ or older: $\frac{x}{20+x}=\frac13$. Cross-multiply: $3x=20+x$, so $x=10$. (Do not use the whole table as the denominator: the condition is ``prefers tea''.)  *Trick: Reverse conditional: the ``given'' column is the denominator*

2. **C ($\dfrac{8}{15}$)** — The condition is ``is a member'', so use the member column: $96+84=180$ members, of whom $96$ are under $30$: $\frac{96}{180}=\frac8{15}$. ($\frac35=\frac{96}{160}$ is the reverse: the chance that an under-30 person is a member; $\frac{24}{125}=\frac{96}{500}$ divides by everyone; $\frac8{25}=\frac{160}{500}$ is just the share who are under $30$.)  *Trick: Reverse conditionals: $P(A\mid B)\ne P(B\mid A)$*

3. **Ans. 60** — Independent means the club rate is the same for seniors and non-seniors: $\frac{18}{18+x}=\frac{42}{42+140}=\frac{3}{13}$. Then $13(18)=3(18+x)$, so $234=54+3x$ and $x=60$. (Check: the overall club rate is $\frac{18+42}{260}=\frac3{13}$, the same as in each group.)  *Trick: Independence from a table: the conditional rates match*

4. **D ($\dfrac{9}{14}$)** — The opposite event is ``both red'': $\frac58\cdot\frac47=\frac5{14}$ (after one red is removed, $4$ red remain among $7$). So the answer is $1-\frac5{14}=\frac9{14}$. ($\frac{39}{64}=1-(\frac58)^2$ pretends the first marble is put back; $\frac3{8}$ counts only the first draw; $\frac5{14}$ is the chance of no blue.)  *Trick: At least one = 1 $-$ none (and update the bag)*

5. **B ($\dfrac{7}{15}$)** — Both red: $\frac4{10}\cdot\frac39=\frac2{15}$. Both black: $\frac6{10}\cdot\frac59=\frac13=\frac5{15}$. Add: $\frac2{15}+\frac5{15}=\frac7{15}$. ($\frac{13}{25}=0.4^2+0.6^2$ allows replacement; $\frac13$ is only the both-black case; $\frac8{15}$ is the chance the colors differ.)  *Trick: Without replacement: shrink the pool after each draw*

6. **Ans. 7** — The probability of no defective item among $n$ checks is $0.9^n$, so we need $1-0.9^n>0.5$, i.e. $0.9^n<0.5$. Try values: $0.9^6\approx0.531$ (too big) and $0.9^7\approx0.478$. So $n=7$. (A common guess is $5$, from $5\times10\%=50\%$, but chances do not simply add.)  *Trick: At least one: $1-0.9^n$*

7. **C ($\dfrac{11}{29}$)** — Out of $100$ students: AP in grades 9--10: $0.30\cdot55=16.5$; AP in grades 11--12: $0.60\cdot45=27$. AP total $=43.5$. Fraction $=\frac{16.5}{43.5}=\frac{11}{29}$. ($\frac3{10}$ is the AP rate within grades 9--10, the reverse question; $\frac{33}{200}=0.165$ is the share of all students; $\frac{11}{20}=0.55$ is the share of students in grades 9--10.)  *Trick: Reverse conditional with percents: build the two parts, divide by the AP total*

8. **A ($840$)** — The $40\%$ applies to bicycle owners, not to everyone: $0.35\cdot0.40=0.14$ of the town, and $0.14\cdot6000=840$. ($2100=0.35\cdot6000$ counts all bicycle owners; $2400=0.40\cdot6000$ applies $40\%$ to everyone; $4500=0.75\cdot6000$ adds the percents.)  *Trick: Expected count: multiply the chain of proportions*

9. **A** — Random assignment of the volunteers to the two groups makes the groups comparable, so a large difference can be attributed to the schedule (cause). But the volunteers were not randomly chosen from the town, so the result applies only to people like them. (Causation for the town needs random sampling; ``association only'' ignores the random assignment.) Conceptual item.  *Trick: Random assignment gives cause; only random sampling gives generalization*

10. **B** — The sample was random, so the finding applies to the city's adults. Nobody was randomly assigned to eat or skip breakfast, so other factors (exercise, income, sleep) could explain the difference: an association, not a cause. Conceptual item.  *Trick: Random sample generalizes; no random assignment means no cause*

11. **D** — Plausible values for $P$ are $44\%$ to $52\%$ and for $Q$ are $41\%$ to $49\%$. The intervals overlap (for example both could be $46\%$), so the poll cannot show that $P$ is ahead. The sample difference of $3$ points is real in the sample only. (Exact statements about the whole city are never justified by a sample.)  *Trick: Overlapping intervals: cannot separate the two*

12. **B ($2.5$)** — The margin of error is proportional to $\frac1{\sqrt n}$. Quadrupling the sample size ($1600=4\cdot400$) divides it by $\sqrt4=2$: $\frac52=2.5$. ($1.25$ divides by $4$, treating it as proportional to $\frac1n$; $5$ ignores the larger sample; $10$ moves the wrong way.)  *Trick: Margin of error shrinks with the square root of the sample size*

13. **A** — The flaw is how the sample was chosen: self-selected visitors of a gym site are not representative of all adults, and they tend to exercise more, so the result is biased upward. A larger sample would not fix this. $1{,}500$ is a perfectly adequate size for a random sample, and the question was about adults, so children are irrelevant. Conceptual item.  *Trick: Sampling bias: who could answer?*

14. **Ans. 7** — The interval $41\%$ to $55\%$ is centered on the estimate ($48\%$), and the margin of error is the distance from the center to either end: $\frac{55-41}{2}=7$ percentage points. (The full width, $14$, is twice the margin of error.)  *Trick: Margin of error = half the width of the interval*

### Set 5 — Summit: the hardest mixed problems

1. **C** — $P$ is symmetric about $60$: its mean and median are both $60$, and its range is $80-40=40$. The two new values equal $60$, so the mean stays $60$, the median stays $60$ (the middle of the sorted list), and the extremes $40$ and $80$ are unchanged, so the range stays $40$. The new values sit exactly at the center, so the data are more concentrated: the standard deviation decreases.  *Trick: A value at the center changes the SD but not mean, median or range*

2. **Ans. 23** — The total is $5\cdot12=60$. A mode of $8$ means $8$ appears at least twice, and with median $10$ both $8$'s are below the middle: $8,8,10,d,e$. To make $e$ as large as possible, make $d$ as small as possible. But $d\ge10$, and $d=10$ would make $10$ appear twice, tying with $8$ (the mode would not be unique), so $d=11$. Then $e=60-8-8-10-11=23$. (The tempting $d=10$ gives $24$.)  *Trick: Build the list from the constraints*

3. **Ans. 34** — The seven shown values sum to $134$. If the eighth value is $x$, the mean $\frac{134+x}{8}$ must be an integer, so $134+x$ is a multiple of $8$: $136,144,152,160,168,\ldots$, giving $x=2,10,18,26,34$. The mean must exceed $18$, so $134+x>144$, which allows $x=18,26,34$. All are below $40$; the greatest is $34$.  *Trick: Integer mean: the total must be divisible by the count*

4. **Ans. 9** — The greatest mean puts every value at the top of its class and the least puts every value at the bottom. Each value differs between the two cases by $19-10=9$ (the same for every class), so the means differ by exactly $9$, whatever the frequencies. (Using $10$, the class width, forgets that integers in $10$--$19$ span only $9$ units.)  *Trick: Grouped integers: every value can move by (class width $-1$)*

5. **D** — The third quartile is $34$, so at least a quarter of the values are at or above it: true. The IQRs are $34-16=18$ for $X$ and $30-20=10$ for $Y$, so $Y$'s is smaller. The median of $Y$ is $26$, so at most half the values are below $26$, never more than half. The means cannot be read from box plots. (The percent facts about quartiles, not the shape of the box, decide each statement.)  *Trick: Quartiles cut the data into quarters: use the percent meaning*

6. **A (Point $Q$)** — Predicted values at $x=2,5,8,11$: $14,\ 20,\ 26,\ 32$. Residuals: $P$: $16-14=+2$; $Q$: $12-20=-8$; $R$: $31-26=+5$; $S$: $28-32=-4$. The least residual is the most negative, $-8$ at $Q$. ($R$ has the greatest residual; $P$ is closest to the line.)  *Trick: Residual sign: below the line is negative*

7. **Ans. 27** — Flagged items: $180+490=670$. Defective among them: $180$. So $\frac{180}{670}\approx0.269$, about $27\%$. (The scanner catches $\frac{180}{200}=90\%$ of defective items, but that is the reverse question; most flagged items are false alarms because good items are so numerous.)  *Trick: Reverse conditional: the flagged group is the denominator*

8. **B** — Divide by the group named after ``who'' or ``given'': in person and junior: $\frac{30}{90}=\frac13$; junior and online: $\frac{12}{60}=\frac15$; sophomore and hybrid: $\frac{26}{90}=\frac{13}{45}\approx0.289$; online and freshman: $\frac{28}{80}=\frac7{20}=0.35$. The greatest is $0.35$. (The biggest cell, $40$, is not in any option; large counts do not mean large probabilities.)  *Trick: Name the ``given'' group, then divide by its total*

9. **C ($\dfrac{19}{66}$)** — Red: $\frac5{12}\cdot\frac4{11}=\frac{20}{132}$. Blue: $\frac4{12}\cdot\frac3{11}=\frac{12}{132}$. Green: $\frac3{12}\cdot\frac2{11}=\frac6{132}$. Total $\frac{38}{132}=\frac{19}{66}$. ($\frac5{33}$ counts only red; $\frac{25}{72}=\frac{50}{144}$ puts each marble back; $\frac{19}{33}$ forgets to reduce the total, i.e. doubles it.)  *Trick: Without replacement: add the color cases, each with a shrinking pool*

10. **B ($900$)** — To cut the margin of error to one third, the sample size must be multiplied by $3^2=9$: $100\cdot9=900$. ($300$ treats the margin as inversely proportional to $n$; $600$ subtracts; $8{,}100$ squares the nine.)  *Trick: Margin of error $\propto 1/\sqrt{n}$: divide by $k$, multiply $n$ by $k^2$*

11. **D** — Both features are present. Random selection from the district lets us generalize to all $12{,}000$ students; random assignment to the two methods lets us attribute the difference to the method. (Restricting to the $300$ ignores the random sample; ``association only'' ignores the random assignment; the whole country was never sampled.) Conceptual item.  *Trick: Random sample AND random assignment: cause for the whole population*

12. **A** — The intervals are $58\pm4=54$ to $62$ and $49\pm3=46$ to $52$. They do not overlap (the top of $B$'s, $52$, is below the bottom of $A$'s, $54$), so the data support a higher percent in $A$. The $9$-point gap is only a sample difference; margins of error can differ and the intervals can still be compared; $54\%$ lies outside $B$'s interval. Conceptual item (interval overlap is computed).  *Trick: Compare confidence intervals: no overlap supports a difference*

13. **Ans. 4200** — The plausible percent runs from $40-5=35\%$ to $45\%$. The least plausible number is $35\%$ of $12{,}000$: $0.35\cdot12000=4200$. (Using $40\%$ gives $4800$, the estimate itself; $5\%$ of $12{,}000$ is $600$, the margin in people, not the minimum.)  *Trick: Margin of error gives an interval; then scale to the population*

14. **C ($49\%$)** — Yes answers: $0.55(400)=220$ and $0.45(600)=270$, total $490$ out of $1000$: $49\%$. ($50\%$ averages the two percents with equal weights; $51\%$ reverses the weights; $45\%$ is the women's percent alone.)  *Trick: Weighted average: weight each percent by its group size*

15. **D ($y=50m+300$)** — Substitute $x=4m$: $y=12.5(4m)+300=50m+300$. The slope becomes the cost per month, four times the cost per week, but the intercept, the cost at the start, does not change. ($12.5m+300$ keeps the old slope; $50m+1200$ also multiplies the intercept; $3.125=12.5\div4$ divides instead of multiplies.)  *Trick: Change of units: substitute, then read slope and intercept*

16. **A (mode $<$ median $<$ mean)** — The mode is the most frequent value, $1$. With $25$ values the median is the 13th: running totals $8,\ 14,\ldots$ put it at $2$. The mean is $\frac{8+12+12+12+10+18}{25}=\frac{72}{25}=2.88$. So mode $<$ median $<$ mean. A long tail on the right pulls the mean up the most and the mode the least.  *Trick: Right-skewed data: mode $<$ median $<$ mean*

17. **Ans. 34** — All games in the bars $0$--$10$, $10$--$20$ and $20$--$30$ are below $35$: $4+9+13=26$. The bar $30$--$40$ contains $8$ games, and in the best case all $8$ scored $30$ to $34$. So the greatest possible number is $26+8=34$. (Splitting that bar in half, $30$, assumes the scores are spread evenly.)  *Trick: Histogram bounds: a split bar can all fall on one side*

18. **B ($1.6$)** — Each time $x$ increases by $1$, $y$ is multiplied by about the same factor: $\frac85=1.6,\ \frac{13}8\approx1.6,\ \frac{20}{13}\approx1.5,\ \frac{33}{20}\approx1.65,\ \frac{52}{33}\approx1.6$. So $b\approx1.6$ (and $a\approx5$, the value at $x=0$). ($0.63\approx\frac1{1.6}$ would be a decreasing model; $5$ is $a$; $8$ is just the height at $x=1$.)  *Trick: Exponential model: $b$ is the factor per unit of $x$*

19. **C ($33$)** — The total is $9\cdot24=216$. The four values below the median are distinct and less than $20$, so they sum to at most $16+17+18+19=70$. The median is $20$, so the four values above it sum to at least $216-70-20=126$. Four distinct integers above $20$ with sum $126$ and the smallest possible maximum are $30,31,32,33$. So the answer is $33$. (If repeats were allowed, $31,31,32,32$ would give $32$; the distinct requirement forces $33$.)  *Trick: Extreme cases: make some values as large as allowed to free the total*

20. **D ($13$)** — Total $=2+9+15+30+42+20=118$, so the mean is $\frac{118}{20}=5.9$. Values greater than $5.9$ are the $6$'s, $7$'s and $10$'s: $5+6+2=13$. (The $6$'s count: $6>5.9$. Counting values above the median $6$ gives $8$; values above the mode $7$ give $2$; values below the mean give $7$.)  *Trick: Compute the mean exactly, then count with care*

