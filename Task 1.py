import matplotlib.pyplot as plt
import pandas as pd

# Data for Age Distribution
age_distribution = pd.DataFrame({
    "Age Group": ["0-14 years", "15-24 years", "25-44 years", "45-64 years", "65+ years", "Total"],
    "Population": [2100, 1700, 3500, 2800, 1900, 12000]
})

# Create a bar chart for Age Distribution
plt.figure(figsize=(10, 6))
plt.bar(age_distribution["Age Group"][:-1], age_distribution["Population"][:-1], color="skyblue")
plt.title("Age Distribution in Greenfield")
plt.xlabel("Age Group")
plt.ylabel("Population")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the chart
plt.savefig("age_distribution_chart.png")
plt.show()
