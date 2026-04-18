import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("Loading Excel file...")

file_path = r"C:\Users\Angelique Snow\Downloads\student_scores_distributions.xlsx"
data = pd.read_excel(file_path)

print("Generating graphs...")

sns.set(style="whitegrid")

fig, axes = plt.subplots(3, 2, figsize=(14, 12))
axes = axes.flatten()

for i, col in enumerate(data.columns):
    sns.histplot(data[col], kde=True, bins=30, ax=axes[i])

    
    axes[i].set_title(col, fontsize=10)


    axes[i].tick_params(axis='both', labelsize=8)


fig.delaxes(axes[-1])

plt.tight_layout(pad=2.0)

plt.savefig("student_score_histograms.png", dpi=300, bbox_inches="tight")
plt.show()

print("All graphs generated successfully!")
print("Code execution complete.")