import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (built-in)
df = sns.load_dataset('tips')

# Save dataset (optional, for your repo)
df.to_csv("../data/tips.csv", index=False)

# Basic info
print("Dataset Preview:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nStatistics:\n", df.describe())

# -----------------------------
# GRAPH 1: Tip vs Total Bill
# -----------------------------
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title("Tip vs Total Bill")
plt.savefig("../outputs/tip_vs_bill.png")
plt.clf()

# -----------------------------
# GRAPH 2: Total Bill Distribution
# -----------------------------
sns.histplot(df['total_bill'], bins=10)
plt.title("Total Bill Distribution")
plt.savefig("../outputs/bill_distribution.png")
plt.clf()

# -----------------------------
# GRAPH 3: Average Tip by Day
# -----------------------------
sns.barplot(x='day', y='tip', data=df)
plt.title("Average Tip by Day")
plt.savefig("../outputs/avg_tip_day.png")
plt.clf()

# -----------------------------
# GRAPH 4: Bill by Gender
# -----------------------------
sns.boxplot(x='sex', y='total_bill', data=df)
plt.title("Total Bill by Gender")
plt.savefig("../outputs/bill_by_gender.png")
plt.clf()