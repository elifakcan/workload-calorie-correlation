# workload-calorie-correlation
# Impact of Daily Academic Intensity on Dietary Deviation

## 1. Project Proposal
This project aims to investigate the relationship between **daily academic/workload intensity** and **unplanned high-calorie food consumption**.  
The hypothesis is that on days with higher academic or personal workload (e.g., multiple classes, exams, projects, or gym sessions), individuals are more likely to deviate from their planned diet or consume higher-calorie meals.

**Hypothesis (H₁):** As the daily workload intensity increases, the number of unplanned or high-calorie meals consumed also increases.  
**Null hypothesis (H₀):** There is no relationship between daily workload intensity and unplanned meal consumption.

---

## 2. Variables and Data Description
| Variable | Type | Description |
|-----------|------|-------------|
| `Academic_Load` | Numerical | The **actual daily workload**, measured by the total number of homework, quizzes, or project deadlines assigned in SUCourse+ (or similar academic platforms). For example, if 2 homework and 1 project deliverable are due on the same day, the `Academic_Load` value = 3. |
| `Unplanned_Meals` | Numerical | The count of meals/snacks that exceed the planned calorie intake or deviate from the daily diet plan. |
| `Calories_Total` | Numerical | Total calories consumed during the day (recorded for additional analysis and validation). |

Optional supporting variables:  
- `Sleep_Hours`, `Stress_Level`, or `Day_Type (Weekday/Weekend)` may be added later to test control effects.

---

## 3. Data Collection Plan
- The data will be **self-collected over a 20-day period**.  
- Each day, the participant (the researcher) will:
  1. Assign a **Workload_Score (0–5)** based on daily activities (lessons, exams, meetings, gym, etc.).
  2. Record all meals and their estimated **calorie values** using a calorie-tracking app or online database.
  3. Mark each meal as **planned** (fits the diet plan) or **unplanned** (extra snack, high-calorie, or impulse food).  
- The dataset will therefore contain approximately **20 rows (days)** and **3–5 columns** (depending on added variables).

Example daily entry:

| Date | Workload_Score | Unplanned_Meals | Calories_Total | Notes |
|------|----------------|-----------------|----------------|-------|
| 2025-11-01 | 4 | 2 | 2350 | Exam + gym + late-night snack |
| 2025-11-02 | 2 | 0 | 1800 | Light day |

---

## 4. Analysis Plan
- **Descriptive statistics** to observe trends (mean, variance, etc.).
- **Correlation analysis** between `Workload_Score` and `Unplanned_Meals`.
- **Group comparison:** Independent samples t-test between “High workload (≥3)” and “Low workload (<3)” groups.
- Visualization: Scatter plot and regression line to illustrate the relationship.

---

## 5. Expected Outcome
It is expected that days with higher workload intensity will show **a positive correlation** with the number of unplanned/high-calorie meals.  
The findings could provide insight into how academic or professional stress influences dietary discipline and decision-making.

---

## 6. Tools and Timeline
- **Tools:** Excel or Google Sheets for data entry, Python (pandas, matplotlib, scipy) or Excel functions for analysis.  
- **Timeline:**  
  - Week 1–3 → Data collection (20 days)  
  - Week 4 → Data cleaning and analysis  
---
