import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# Sample data
data = {
    'Age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'BodyFat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_bodyfat = df['BodyFat'].mean()
median_bodyfat = df['BodyFat'].median()
std_bodyfat = df['BodyFat'].std()

print("Age:")
print("Mean:", mean_age)
print("Median:", median_age)
print("Standard Deviation:", std_age)

print("\nBody Fat (%):")
print("Mean:", mean_bodyfat)
print("Median:", median_bodyfat)
print("Standard Deviation:", std_bodyfat)

# Draw boxplots
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y='Age', data=df)
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y='BodyFat', data=df)
plt.title('Boxplot of Body Fat (%)')

plt.tight_layout()
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['BodyFat'])
plt.title('Scatter Plot of Age vs Body Fat')
plt.xlabel('Age')
plt.ylabel('Body Fat (%)')
plt.grid(True)
plt.show()

# Draw Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
stats.probplot(df['BodyFat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat (%)')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()
