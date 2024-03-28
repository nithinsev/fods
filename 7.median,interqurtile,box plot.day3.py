import numpy as np
import matplotlib.pyplot as plt
time_spent = [8, 12, 5, 15, 10, 20, 7, 18, 25, 8, 12, 22, 15, 10, 30, 7, 18, 15, 20, 12]
median_time_spent = np.median(time_spent)
print("Median time spent on the website:", median_time_spent)
q1 = np.percentile(time_spent, 25)
q3 = np.percentile(time_spent, 75)
iqr = q3 - q1
print("Interquartile Range (IQR):", iqr)
plt.figure(figsize=(8, 6))
plt.boxplot(time_spent)
plt.title('Box Plot of Time Spent on Website')
plt.ylabel('Time Spent (minutes)')
plt.grid(True)
plt.show()
