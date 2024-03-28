import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
np.random.seed(0)
exam_scores = np.random.randint(40, 101, size=50)
plt.figure(figsize=(8, 6))
plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Exam Scores')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
skewness = skew(exam_scores)
print("Skewness Coefficient:", skewness)
