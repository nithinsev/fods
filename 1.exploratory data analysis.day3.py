import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
num_samples = 100
sales = np.random.normal(loc=1000, scale=200, size=num_samples)
advertising_expenditure = np.random.normal(loc=500, scale=100, size=num_samples)
data = pd.DataFrame({'Sales': sales, 'Advertising_Expenditure': advertising_expenditure})
print(data.head())
summary_stats = data.describe()
print("\nSummary Statistics:\n", summary_stats)
plt.figure(figsize=(10, 6))
plt.hist(data['Sales'], bins=20, color='skyblue', alpha=0.7, label='Sales')
plt.hist(data['Advertising_Expenditure'], bins=20, color='salmon', alpha=0.7, label='Advertising Expenditure')
plt.title('Distribution of Sales and Advertising Expenditure')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
mean_sales = data['Sales'].mean()
variance_sales = data['Sales'].var()
mean_advertising = data['Advertising_Expenditure'].mean()
variance_advertising = data['Advertising_Expenditure'].var()
covariance = data.cov().iloc[0, 1]
correlation = data.corr().iloc[0, 1]
print("\nMean of Sales:", mean_sales)
print("Variance of Sales:", variance_sales)
print("Mean of Advertising Expenditure:", mean_advertising)
print("Variance of Advertising Expenditure:", variance_advertising)
print("Covariance between Sales and Advertising Expenditure:", covariance)
print("Correlation between Sales and Advertising Expenditure:", correlation)
from scipy.stats import zscore
data['Sales_Zscore'] = zscore(data['Sales'])
data['Advertising_Expenditure_Zscore'] = zscore(data['Advertising_Expenditure'])
outliers_sales = data[data['Sales_Zscore'].abs() > 3]
outliers_advertising = data[data['Advertising_Expenditure_Zscore'].abs() > 3]
print("\nNumber of outliers in Sales:", len(outliers_sales))
print("Number of outliers in Advertising Expenditure:", len(outliers_advertising))
plt.figure(figsize=(10, 6))
plt.scatter(data['Sales'], data['Advertising_Expenditure'], color='skyblue', label='Data')
plt.scatter(outliers_sales['Sales'], outliers_sales['Advertising_Expenditure'], color='red', label='Outliers (Sales)')
plt.scatter(outliers_advertising['Sales'], outliers_advertising['Advertising_Expenditure'], color='green', label='Outliers (Advertising)')
plt.title('Scatter Plot with Outliers')
plt.xlabel('Sales')
plt.ylabel('Advertising Expenditure')
plt.legend()
plt.grid(True)
plt.show()
