# ============================================
# Task 5 - Statistical Analysis
# SkillCraft Technology Internship
# ============================================

# Import Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# ============================================
# LOAD DATASET
# ============================================

# Load tips dataset
df = pd.read_csv("../data/tips.csv")

# Display first 5 rows
print("===================================")
print("First 5 Rows of Dataset")
print("===================================")
print(df.head())

# ============================================
# DATASET INFORMATION
# ============================================

print("\n===================================")
print("Dataset Information")
print("===================================")
print(df.info())

# ============================================
# CHECK MISSING VALUES
# ============================================

print("\n===================================")
print("Missing Values")
print("===================================")
print(df.isnull().sum())

# ============================================
# DESCRIPTIVE STATISTICS
# ============================================

print("\n===================================")
print("Descriptive Statistics")
print("===================================")
print(df.describe())

# ============================================
# CORRELATION ANALYSIS
# ============================================

print("\n===================================")
print("Correlation Matrix")
print("===================================")

correlation = df.corr(numeric_only=True)
print(correlation)

# ============================================
# T-TEST ANALYSIS
# Compare Male vs Female Total Bill
# ============================================

male_bills = df[df['sex'] == 'Male']['total_bill']
female_bills = df[df['sex'] == 'Female']['total_bill']

t_stat, p_value = ttest_ind(male_bills, female_bills)

print("\n===================================")
print("T-Test Results")
print("===================================")

print("T-Statistic :", t_stat)
print("P-Value     :", p_value)

# Interpretation
print("\n===================================")
print("Interpretation")
print("===================================")

if p_value < 0.05:
    print("There is a statistically significant difference")
    print("between male and female total bills.")
else:
    print("There is NO statistically significant difference")
    print("between male and female total bills.")

# ============================================
# VISUALIZATION 1 - HISTOGRAM
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(df['total_bill'],
             bins=20,
             kde=True)

plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.savefig("../outputs/total_bill_distribution.png")

plt.close()

# ============================================
# VISUALIZATION 2 - BOXPLOT
# ============================================

plt.figure(figsize=(8, 5))

sns.boxplot(x='sex',
            y='total_bill',
            data=df)

plt.title("Total Bill by Gender")

plt.savefig("../outputs/bill_by_gender_stats.png")

plt.close()

# ============================================
# VISUALIZATION 3 - HEATMAP
# ============================================

plt.figure(figsize=(8, 5))

sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.savefig("../outputs/statistical_heatmap.png")

plt.close()

# ============================================
# FINAL MESSAGE
# ============================================

print("\n===================================")
print("Task 5 Statistical Analysis Completed!")
print("Graphs saved inside outputs folder.")
print("===================================")