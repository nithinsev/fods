import numpy as np
import matplotlib.pyplot as plt
scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72]
mean_score = np.mean(scores)
print("Mean Score:", mean_score)
median_score = np.median(scores)
print("Median Score:", median_score)
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
print("Q1 (25th percentile):", q1)
print("Q3 (75th percentile):", q3)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
potential_outliers = [score for score in scores if score < lower_bound or score > upper_bound]
print("Potential Outliers:", potential_outliers)
plt.figure(figsize=(8, 6))
plt.boxplot(scores, vert=False)
plt.title('Box Plot of Scores')
plt.xlabel('Scores')
plt.grid(True)
plt.show()
