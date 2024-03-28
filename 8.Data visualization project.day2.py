import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [1000, 1500, 1200, 1800, 2000, 2500]
}
df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'], format='%B').dt.month
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(df['Month'], ['January', 'February', 'March', 'April', 'May', 'June']) 
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.title('Monthly Sales Comparison')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y') 
plt.xticks(df['Month'], ['January', 'February', 'March', 'April', 'May', 'June']) 
plt.tight_layout()
plt.show()
