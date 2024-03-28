import numpy as np
from scipy import stats
product1_lifespans = np.array([35, 40, 38, 42, 37])
product2_lifespans = np.array([30, 32, 34, 28, 33])
mean_product1 = np.mean(product1_lifespans)
mean_product2 = np.mean(product2_lifespans)
sem_product1 = stats.sem(product1_lifespans)
sem_product2 = stats.sem(product2_lifespans)
ci_product1 = stats.norm.interval(0.90, loc=mean_product1, scale=sem_product1)
ci_product2 = stats.norm.interval(0.90, loc=mean_product2, scale=sem_product2)

print("Product 1 Mean Lifespan:", mean_product1)
print("Product 1 90% Confidence Interval:", ci_product1)
print()
print("Product 2 Mean Lifespan:", mean_product2)
print("Product 2 90% Confidence Interval:", ci_product2)
t_stat, p_value = stats.ttest_ind(product1_lifespans, product2_lifespans)
alpha = 0.05  
print("\nHypothesis Test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in lifespans between the two products.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in lifespans between the two products.")
