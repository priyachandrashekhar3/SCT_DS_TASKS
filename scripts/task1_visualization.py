import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [18,19,20,21,22,23,24,25,26,27,28,29,
            22,23,24,25,26,27,28,29]
}

df = pd.DataFrame(data)

plt.hist(df['Age'], bins=6, edgecolor='black')

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.savefig("../outputs/age_distribution.png")

plt.show()