import numpy as np
from scipy import stats

# Conversion rate data for each website design (A and B)
design_A_conversion_rates = np.array([0.12, 0.11, 0.09, 0.10, 0.13, 0.08, 0.11, 0.12, 0.10, 0.09])
design_B_conversion_rates = np.array([0.14, 0.15, 0.13, 0.16, 0.12, 0.11, 0.13, 0.15, 0.14, 0.13])

# Perform two-sample t-test to compare the means
t_stat, p_value = stats.ttest_ind(design_A_conversion_rates, design_B_conversion_rates)

alpha = 0.05  # significance level

print("Hypothesis Test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in mean conversion rates between the two designs.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in mean conversion rates between the two designs.")
