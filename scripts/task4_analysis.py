import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (built-in flights dataset)
df = sns.load_dataset('flights')

# Save dataset to your project (optional but recommended)
df.to_csv("../data/flights.csv", index=False)

# Preview dataset
print("Dataset Preview:\n", df.head())

# -----------------------------
# GRAPH 1: Passengers over time
# -----------------------------
sns.lineplot(x='year', y='passengers', data=df)
plt.title("Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.savefig("../outputs/passengers_over_time.png")
plt.clf()

# -----------------------------
# GRAPH 2: Monthly distribution
# -----------------------------
sns.boxplot(x='month', y='passengers', data=df)
plt.title("Monthly Passenger Distribution")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.savefig("../outputs/monthly_distribution.png")
plt.clf()

# -----------------------------
# GRAPH 3: Heatmap (Fixed)
# -----------------------------
pivot = df.pivot(index="month", columns="year", values="passengers")

sns.heatmap(pivot, cmap="coolwarm")
plt.title("Passenger Heatmap")
plt.savefig("../outputs/passenger_heatmap.png")
plt.clf()