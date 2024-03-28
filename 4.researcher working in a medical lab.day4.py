import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
control_group = np.array([72, 68, 75, 71, 73, 70, 68, 72, 69, 70])
treatment_group = np.array([82, 78, 85, 81, 83, 80, 79, 84, 81, 82])
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
alpha = 0.05
print("Hypothesis Test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
if p_value < alpha:
    print("Reject the null hypothesis: The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant effect of the new treatment compared to the placebo.")
plt.figure(figsize=(8, 6))
plt.boxplot([control_group, treatment_group], labels=['Placebo', 'New Treatment'])
plt.title('Effectiveness of New Treatment vs Placebo')
plt.ylabel('Score')
plt.grid(True)
plt.show()
