import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Temperature': [20, 22, 25, 27, 30, 28],
    'Rainfall': [50, 40, 60, 70, 55, 45]
}
df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'], format='%B').dt.month
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature'], marker='o', linestyle='-')
plt.title('Monthly Temperature Trend')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(df['Month'], ['January', 'February', 'March', 'April', 'May', 'June'])
plt.tight_layout()
plt.show()plt.figure(figsize=(10, 6))
plt.scatter(df['Rainfall'], df['Temperature'], color='skyblue')
plt.title('Monthly Rainfall vs Temperature')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()
