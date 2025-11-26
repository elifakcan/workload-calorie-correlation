# -*- coding: utf-8 -*-
"""
Final Workload–Calorie Correlation System
Includes:
- Daily Base Workload
- Weekly Fatigue Factor
- Final Workload Score
- WEEKDAY/WEEKEND ANALYSIS
- ADVANCED REPORT VISUALIZATIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ----------------------------------------
# 1. LOAD DATA
# ----------------------------------------

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "merged_november.csv")

df = pd.read_csv(csv_path)

df["Date"] = pd.to_datetime(df["Date"])

numeric_cols = ["Course_Load_Min","Homework_Count","Project_Count",
                "Exam_Count","Exam_Number_Week","Calories"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

df["Calories"] = df["Calories"].fillna(df["Calories"].mean())

df["DayOfWeek"] = df["Date"].dt.day_name()
df["DayType"] = df["Date"].dt.weekday.apply(lambda x: "Weekend" if x >= 5 else "Weekday")

# ----------------------------------------
# 2. WEEKLY FATIGUE FACTOR
# ----------------------------------------

df["Week"] = df["Date"].dt.isocalendar().week

weekly_stats = df.groupby("Week")[["Exam_Count","Homework_Count","Project_Count"]].sum().reset_index()
weekly_stats["Weekly_Fatigue_Factor"] = (
    1
    + weekly_stats["Exam_Count"] * 0.15
    + weekly_stats["Homework_Count"] * 0.05
    + weekly_stats["Project_Count"] * 0.10
)

df = df.merge(weekly_stats[["Week","Weekly_Fatigue_Factor"]], on="Week", how="left")

# ----------------------------------------
# 3. DAILY BASE WORKLOAD
# ----------------------------------------

def compute_daily_load(row):

    attendance = row["Course_Load_Min"] / 50
    hw = row["Homework_Count"] * (1.5 if row["Exam_Count"] > 0 else 1)
    project = row["Project_Count"] * (2 if row["Exam_Count"] > 0 else 1.5)
    exam_weight = 2.5 + (row["Exam_Number_Week"] * 0.7)
    exam = row["Exam_Count"] * exam_weight
    combo = 2 if (row["Homework_Count"] > 0 
                  and row["Project_Count"] > 0 
                  and row["Exam_Count"] > 0) else 0

    return attendance + hw + project + exam + combo

df["Daily_Base_Workload"] = df.apply(compute_daily_load, axis=1)

# ----------------------------------------
# 4. FINAL WORKLOAD SCORE
# ----------------------------------------

df["Workload_Score"] = df["Daily_Base_Workload"] * df["Weekly_Fatigue_Factor"]

# ----------------------------------------
# 5. SUMMARY
# ----------------------------------------

print("\n=== FINAL WORKLOAD SCORE SAMPLE ===")
print(df[["Date","Daily_Base_Workload","Weekly_Fatigue_Factor","Workload_Score"]].head())

print("\n=== CORRELATION WITH CALORIES ===")
print(df[["Workload_Score","Calories"]].corr())

# ----------------------------------------
# 6. VISUALIZATIONS
# ----------------------------------------

sns.scatterplot(data=df, x="Workload_Score", y="Calories")
plt.title("Scatter: Workload Score vs Calories")
plt.show()

sns.regplot(data=df, x="Workload_Score", y="Calories", line_kws={"color":"red"})
plt.title("Regression: Workload Score vs Calories")
plt.show()

sns.histplot(df["Workload_Score"], kde=True, bins=10, color="orange")
plt.title("Workload Score Distribution")
plt.show()

sns.jointplot(data=df, x="Workload_Score", y="Calories",
              kind="kde", fill=True, cmap="magma")
plt.suptitle("2D Density: Workload Score vs Calories", y=1.02)
plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df[["Workload_Score","Calories",
                "Daily_Base_Workload","Weekly_Fatigue_Factor"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (New Workload Model)")
plt.show()

sns.pairplot(df[["Workload_Score","Calories",
                 "Homework_Count","Project_Count","Exam_Count"]])
plt.suptitle("Pairplot (Workload Score Edition)", y=1.02)
plt.show()

df["Rolling_Calories"] = df["Calories"].rolling(3).mean()
df["Rolling_Workload"] = df["Workload_Score"].rolling(3).mean()

plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Rolling_Calories"], linewidth=3, label="Calories (3-day avg)")
plt.plot(df["Date"], df["Rolling_Workload"], linewidth=3, label="Workload Score (3-day avg)")
plt.legend()
plt.xticks(rotation=45)
plt.title("Rolling Trends: Calories vs Workload Score")
plt.show()

# ==================================================
# 7. NEW — WEEKDAY / WEEKEND ANALYSIS
# ==================================================

plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="DayType", y="Calories")
plt.title("Calories by Weekday vs Weekend")
plt.show()

plt.figure(figsize=(7,5))
sns.violinplot(data=df, x="DayType", y="Workload_Score")
plt.title("Workload Distribution: Weekday vs Weekend")
plt.show()

# Average calories per weekday
plt.figure(figsize=(10,5))
sns.barplot(data=df, x="DayOfWeek", y="Calories", estimator=np.mean, ci=None)
plt.title("Average Calories by Day of Week")
plt.xticks(rotation=45)
plt.show()

# Average workload per weekday
plt.figure(figsize=(10,5))
sns.barplot(data=df, x="DayOfWeek", y="Workload_Score", estimator=np.mean, ci=None)
plt.title("Average Workload Score by Day of Week")
plt.xticks(rotation=45)
plt.show()

# ==================================================
# 8. CALORIES x WORKDAY HEATMAP
# ==================================================

pivot = df.pivot_table(values="Calories", index="DayOfWeek", columns="DayType", aggfunc=np.mean)

plt.figure(figsize=(7,5))
sns.heatmap(pivot, annot=True, cmap="viridis")
plt.title("Calories Heatmap (Weekday/Weekend Interaction)")
plt.show()

# ==================================================
# 9. WORKLOAD CATEGORIES
# ==================================================

df["Workload_Level"] = pd.cut(
    df["Workload_Score"],
    bins=[-1,5,12,30],
    labels=["Low", "Medium", "High"]
)

plt.figure(figsize=(7,5))
sns.barplot(data=df, x="Workload_Level", y="Calories", estimator=np.mean, ci=None)
plt.title("Average Calories by Workload Category")
plt.show()
