import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Sales': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200, 3500, 3800]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()
import numpy as np
np.random.seed(0)
df['Advertising_Expenditure'] = np.random.randint(100, 1000, size=len(df))
plt.figure(figsize=(10, 6))
plt.scatter(df['Advertising_Expenditure'], df['Sales'], color='skyblue')
plt.title('Sales vs Advertising Expenditure')
plt.xlabel('Advertising Expenditure')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(df['Date'], df['Sales'], color='skyblue')
plt.title('Monthly Sales Comparison')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(axis='y')  
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()
