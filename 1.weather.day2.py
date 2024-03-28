import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = {
    'date': ['2019-01-01', '2019-01-02', '2019-01-03'],
    'temperature': [25.2, 27.1, 24.8],
    'precipitation': [0.3, 0.0, 0.1], 
    'humidity': [72, 68, 75],
     'wind_speed': [5.1, 4.8, 6.2]
}
df = pd.DataFrame(data)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Set 'date' column as the index
df.set_index('date', inplace=True)

# Visualize the average temperature trends over different seasons
df.resample('M')['temperature'].mean().plot(title='Average Temperature Trends (Monthly)')
plt.ylabel('Temperature (°C)')
plt.xlabel('Date')
plt.show()

# Identify and visualize any patterns or anomalies in precipitation
df['precipitation'].plot(title='Precipitation Trends')
plt.ylabel('Precipitation (mm)')
plt.xlabel('Date')
plt.show()

# Plot temperature distributions and highlight extreme weather events
sns.histplot(df['temperature'], bins=10, kde=True)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()
