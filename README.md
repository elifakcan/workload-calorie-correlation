

## **Workload–Calorie Correlation Analysis**

### *Understanding how academic workload influences daily calorie intake*

---

## ## 1. Research Question

**Does a higher academic workload lead to an increase in daily calorie intake?**

---

## ## 2. Hypotheses

### **H₁ (Alternative Hypothesis)**

Higher workload → higher average daily calorie intake.

### **H₀ (Null Hypothesis)**

Workload and calorie intake are not related.

---

## ## 3. Dataset Description

The dataset contains **daily academic activity & calorie intake** for the month of November.
Each row represents one day.

### **Variables**

| Variable           | Description                        |
| ------------------ | ---------------------------------- |
| `Date`             | Daily record                       |
| `Course_Load_Min`  | Total minutes of lectures attended |
| `Homework_Count`   | Number of homework assignments     |
| `Project_Count`    | Number of project submissions      |
| `Exam_Count`       | Number of exams taken on that day  |
| `Exam_Number_Week` | Exam intensity for that week       |
| `Calories`         | Total calories consumed            |

---

## ## 4. Workload Model

Daily workload is calculated using the **Daily Base Workload Formula**:

### **Components:**

* **Attendance:**
  [
  \text{attendance} = \frac{\text{Course_Load_Min}}{50}
  ]

* **Homework Weight:**

  * Heavier on exam days
  * Normal weight otherwise

* **Project Weight:**

  * Higher weight on exam days

* **Exam Weight:**
  Increases based on exam intensity that week.

* **Combo Bonus:**
  Homework + Project + Exam on the same day adds extra load.

---

## ### Final Formula

[
\text{Workload Score} = \text{Daily Base Workload} \times \text{Weekly Fatigue Factor}
]

Weekly fatigue factor increases with:

* More weekly exams
* More homework
* More projects

---

## ## 5. Visualizations

Below are the **five final graphs** used in the analysis.

### ###  Average Calories by Workload Category

Higher workload categories → higher calorie averages.

![plot](Fig1.png)

---

### ###  Average Workload Score by Day of Week

Shows weekly academic intensity pattern.

![plot](Fig2.png)

---

### ###  Calories: Weekday vs Weekend

Weekdays show higher calories.

![plot](Fig3.png)

---

### ###  Regression: Workload Score vs Calories

A clear positive trend — supports H₁.

![plot](Fig4.png)

---

### ###  Scatter Plot: Workload Score vs Calories

Raw distribution of all points.

![plot](Fig5.png)

---

## ## 6. Conclusion

✔ As workload increases, **average daily calorie intake also increases**.
✔ Regression shows **strong positive association**.
✔ Weekdays (higher workload) → **higher calorie averages**.

**Therefore, the hypothesis H₁ is supported.**

---

## ## 7. Tools Used

* Python

  * pandas
  * numpy
  * seaborn
  * matplotlib
* Excel (data cleaning & preprocessing)

---
