
# **Workload–Calorie Correlation Analysis**

This project investigates how **daily academic workload** influences **daily calorie intake** by combining **custom workload modeling**, **statistical hypothesis testing**, and **machine learning techniques**.

The analysis integrates **interpretability-focused machine learning models** to uncover both **linear trends** and **nonlinear threshold effects** in stress-related eating behavior.

---

## **1. Research Question**

**Does a higher academic workload lead to increased daily calorie intake?**
If so:

* Is the effect limited to exam days, or does it extend across exam weeks?
* Is there a workload threshold after which calorie intake increases sharply?

---

## **2. Hypotheses**

### **H₁ – Alternative Hypothesis**

Higher academic workload leads to higher daily calorie intake.

### **H₀ – Null Hypothesis**

Academic workload and daily calorie intake are not related.

---

## **3. Dataset Description**

Daily observations were collected from **September 22 to the end of November** from two sources:

1. **Academic workload data (SUCourse+)**
2. **Calorie intake data (Yazıo nutrition tracking app)**

The datasets were merged using a common `Date` column.

---

### **3.1 Academic Workload Variables**

| Variable           | Description                    |
| ------------------ | ------------------------------ |
| `Course_Load_Min`  | Lecture minutes attended       |
| `Homework_Count`   | Number of homework assignments |
| `Project_Count`    | Number of project tasks        |
| `Exam_Count`       | Number of exams taken          |
| `Exam_Number_Week` | Weekly exam intensity          |

---

### **3.2 Nutrition Variable**

| Variable   | Description                 |
| ---------- | --------------------------- |
| `Calories` | Total daily calories logged |

---

## **4. Workload Score Model**

A **custom workload score** was designed to aggregate daily academic intensity into a single interpretable metric.

[
\text{Workload Score} = \text{Daily Base Workload} \times \text{Weekly Fatigue Factor}
]

### Components:

* Lecture attendance
* Homework and project load
* Exam intensity
* Combo bonus (Homework + Project + Exam on same day)
* Weekly fatigue accumulation

This structure captures **both daily stressors and cumulative weekly pressure**.

---

## **5. Exploratory Data Analysis (EDA)**

Key visualizations include:

* Workload vs calorie scatter and regression plots
* Workload distribution
* Weekday vs weekend calorie comparison
* Daily and weekly calorie time series
* Correlation heatmap

These analyses suggest a **positive but noisy relationship** between workload and calorie intake.

---

## **6. Statistical Hypothesis Testing**

### **6.1 Independent Samples t-Test**

* Comparison: Low (≤3) vs High (≥8) workload
* Result: Not statistically significant (p = 0.1209)
* Interpretation: Limited power due to small high-workload sample size

### **6.2 One-Way ANOVA**

* Groups: Low, Medium, High workload
* Result: Statistically significant (p = 0.0043)
* Interpretation: Calorie intake differs meaningfully across workload categories

---

## **7. Temporal Analysis: Exam Weeks & Pre–Post Exam Patterns**

To address feedback beyond single exam days:

### **Exam Week Analysis**

* A binary `Is_Exam_Week` variable was created
* Exam weeks exhibit **higher average calorie intake**, indicating sustained stress effects

### **Pre–Post Exam Analysis**

* Days were labeled relative to the nearest exam (−3 to +3)
* Calories tend to **increase before exams** and decline afterward
* This pattern suggests **anticipatory stress-related eating**

---

## **8. Machine Learning Analysis**

### **8.1 Multiple Linear Regression**

A regression model was trained using:

* Academic workload components
* Exam intensity
* Exam week indicator

**Purpose:** Interpretability rather than high-accuracy prediction.

Key findings:

* Exam-related variables are the strongest predictors
* Lecture load has a comparatively smaller effect
* Exam week effect remains significant even after controlling for daily workload

---

### **8.2 Decision Tree Regression (Threshold Detection)**

A shallow decision tree was used to detect **nonlinear workload thresholds**.

**Finding:**
Calorie intake increases sharply once workload exceeds a critical threshold, confirming that the relationship is **not purely linear**.

---

### **8.3 Random Forest Regression**

A Random Forest model was applied to:

* Validate feature importance rankings
* Confirm robustness across ML techniques

**Result:**
Exam-related features consistently rank highest in importance.

---

### **8.4 K-Means Clustering (Unsupervised Learning)**

Using workload score and calories:

* Days were clustered into three distinct groups
* Clusters align closely with low, medium, and high workload categories
* Provides unsupervised validation of workload classification

---

## **9. Summary of Findings**

* Academic workload and calorie intake are positively related
* Exam-related stress is the dominant driver
* Calorie intake increases **before exams**, not just on exam days
* A clear workload threshold exists beyond which calorie intake rises sharply
* Results are consistent across statistical tests and ML models

---

## **10. Tools & Technologies**

* **Python**: pandas, numpy, matplotlib, seaborn
* **Statistics**: scipy
* **Machine Learning**: scikit-learn
* **Preprocessing**: Excel

---

## **11. Conclusion**

> **Higher academic workload is associated with increased calorie intake**,
> particularly during exam weeks and beyond a critical workload threshold.

By combining **statistical inference** with **interpretable machine learning models**, this project provides a robust, data-driven understanding of stress-related eating behavior in academic settings.

---
