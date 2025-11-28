
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

# **5. Visualizations**

Below are the final graphs used in the analysis.

Each image will be uploaded to GitHub as:
`images/<filename>.png`

---

## **5.1 Scatter: Workload Score vs Calories**

Shows raw relationship and spread.

```
![Scatter Workload vs Calories](images/scatter_workload_calories.png)
```

---

## **5.2 Regression: Workload Score vs Calories**

Positive trend → supports H₁.

```
![Regression Workload vs Calories](images/regression_workload_calories.png)
```

---

## **5.3 Workload Score Distribution**

Shows skew toward low workload days.

```
![Workload Distribution](images/workload_distribution.png)
```

---

## **5.4 Weekday vs Weekend Calories**

Weekdays (higher workload) → higher calorie intake.

```
![Calories Weekday Weekend](images/weekday_weekend_calories.png)
```

---

## **5.5 Average Calories by Day of Week**

```
![Calories by Day](images/calories_by_dayofweek.png)
```

---

## **5.6 Average Workload by Day of Week**

```
![Workload by Day](images/workload_by_dayofweek.png)
```

---

## **5.7 Daily Calories Over Time (Exam Days Highlighted)**

```
![Daily Calories Over Time](images/calories_timeseries_exam.png)
```

---

## **5.8 Weekly Average Calories**

```
![Weekly Calories](images/weekly_calories.png)
```

---

## **5.9 Correlation Heatmap**

```
![Correlation Heatmap](images/correlation_heatmap.png)
```

---

# **6. Hypothesis Testing Results (Ready for Report)**

## **6.1 Independent Samples t-Test**

### **Research Question:**

Do I consume significantly different calories on **low-workload** vs **high-workload** days?

### **Groups**

* **Low Workload:** Workload ≤ 3 → *47 days*
* **High Workload:** Workload ≥ 8 → *10 days*

### **Method:**

**Welch’s t-test** (assumes unequal variance)

### **Results**

* **t-statistic:** −1.7000
* **p-value:** 0.1209

### **Interpretation**

* p > 0.05 → **not statistically significant**
* High-workload days *appear* higher in plots, but the difference is not strong enough to be statistically significant.
* Main reason: **only 10 high-workload days**, lowering statistical power.

### **Conclusion**

There is **no statistically significant difference** in calorie intake between low-workload and high-workload days.

---

## **6.2 One-Way ANOVA (Low vs Medium vs High Workload)**

### **Research Question:**

Does calorie intake differ across **all workload levels**?

### **Groups:**

* Low
* Medium
* High

### **Results**

* **F-statistic:** 5.9362
* **p-value:** 0.0043

### **Interpretation**

* p < 0.01 → **statistically significant**
* Calorie consumption **depends on workload category**.
* Descriptive patterns indicate:

  * Medium workload → highest calories
  * High workload → also elevated
  * Low workload → lowest

### **Conclusion**

There is **strong statistical evidence** that workload level affects calorie intake.

---

# **7. Summary of Findings**

* **t-test:** Low vs High → Not significant
* **ANOVA:** Low vs Medium vs High → ✔ Significant
* Interpretation:

  * Extreme low–high comparison lacks enough data
  * But overall calorie patterns **do change** with workload intensity

---

# **8. Tools Used**

* **Python**

  * pandas
  * numpy
  * seaborn
  * matplotlib
  * scipy
* **Excel** for preprocessing

---

# **9. Conclusion**

The overall evidence suggests:

> **Higher workload generally leads to higher calorie intake**,
> **even though the Low–High difference alone isn’t large enough to be statistically significant.**

This supports the **trend-level relationship** hypothesized.

---
