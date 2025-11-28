
---

# **Workload–Calorie Correlation Analysis**

This project analyzes how **daily academic workload** affects **calorie intake** using a custom workload scoring model and statistical hypothesis testing.

---

# **1. Research Question**

**Does a higher academic workload lead to increased daily calorie intake?**

---

# **2. Hypotheses**

### **H₁ – Alternative Hypothesis**

Higher workload → higher daily calorie intake.

### **H₀ – Null Hypothesis**

Workload and daily calorie intake are not related.

---

# **3. Dataset Description**

Daily data collected throughout November, containing workload activities and calorie intake.

| Variable           | Description                    |
| ------------------ | ------------------------------ |
| `Date`             | Daily entry                    |
| `Course_Load_Min`  | Lecture minutes attended       |
| `Homework_Count`   | Number of homework assignments |
| `Project_Count`    | Number of project tasks        |
| `Exam_Count`       | Number of exams taken          |
| `Exam_Number_Week` | Weekly exam intensity          |
| `Calories`         | Total daily calories           |

---

# **4. Workload Score Model**

Daily workload is computed via a custom formula combining:

* Lecture attendance
* Homework weight
* Project weight
* Exam intensity
* Combo bonus (HW + Project + Exam same day)
* Weekly Fatigue Factor (based on weekly workload)

**Final Formula:**

[
\text{Workload Score} = \text{Daily Base Workload} \times \text{Weekly Fatigue Factor}
]

---

# **5. Visualization**

## **5.1 Scatter: Workload Score vs Calories**

![Scatter Workload vs Calories](scatter_workload_calories.png)

---

## **5.2 Regression: Workload Score vs Calories**

![Regression Workload vs Calories](regression_workload_calories.png)

---

## **5.3 Workload Score Distribution**

![Workload Distribution](workload_distribution.png)

---

## **5.4 Weekday vs Weekend Calories**

![Calories Weekday Weekend](weekday_weekend_calories.png)

---

## **5.5 Average Calories by Day of Week**

![Calories by Day](calories_by_dayofweek.png)

---

## **5.6 Average Workload by Day of Week**

![Workload by Day](workload_by_dayofweek.png)

---

## **5.7 Daily Calories Over Time (Exam Days Highlighted)**

![Daily Calories Over Time](calories_timeseries_exam.png)

---

## **5.8 Weekly Average Calories**

![Weekly Calories](weekly_calories.png)

---

## **5.9 Correlation Heatmap**

![Correlation Heatmap](correlation_heatmap.png)

---

# **6. Hypothesis Testing Results **

## **6.1 Independent Samples t-Test**

### **Research Question:**

Do I consume significantly different calories on **low-workload** vs **high-workload** days?

### **Groups**

* **Low Workload:** Workload ≤ 3 → *47 days*
* **High Workload:** Workload ≥ 8 → *10 days*

### **Method:** Welch's t-test (unequal variance)

### **Results**

* **t-statistic:** −1.7000
* **p-value:** 0.1209

### **Interpretation**

* p > 0.05 → **Not statistically significant**
* High-workload days appear slightly higher in descriptive plots, but:

  * Sample size of high-workload days is very small (n = 10)
  * Not enough statistical power

### **Conclusion**

There is **no statistically significant difference** in calorie intake between low and high workload days.

---

## **6.2 One-Way ANOVA (Low vs Medium vs High Workload)**

### **Research Question:**

Does calorie intake differ across workload categories?

### **Groups**

* Low
* Medium
* High

### **Results**

* **F-statistic:** 5.9362
* **p-value:** 0.0043

### **Interpretation**

* p < 0.01 → **Highly significant**
* Strong evidence that calorie intake varies based on workload level

### **Which groups differ?**

Descriptive trends indicate:

* **Medium workload** → highest calories
* **High workload** → elevated
* **Low workload** → lowest

### **Conclusion**

Workload intensity significantly affects calorie consumption across categories.

---

# **7. Summary of Findings**

* **t-test:** Low vs High → Not significant
* **ANOVA:** Low vs Medium vs High → ✔ Significant

This suggests:

* Extreme low–high comparison lacks statistical power
* But overall calorie patterns **do change meaningfully** with workload level

---

# **8. Tools Used**

* **Python:** pandas, numpy, seaborn, matplotlib, scipy
* **Excel:** preprocessing

---

# **9. Conclusion**

Overall:

> **Higher workload generally leads to higher calorie intake**,
> although the difference between only low and high days is not strong enough to be statistically significant.

The broader workload categories tell a clearer story:
**workload intensity does influence calorie consumption.**

---
