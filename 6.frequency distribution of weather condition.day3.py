from collections import Counter
weather_data = {
    'Sunny': 50,
    'Cloudy': 30,
    'Rainy': 20,
    'Snowy': 10
}
weather_distribution = Counter(weather_data)
print("Frequency distribution of weather conditions:")
for weather, frequency in weather_distribution.items():
    print(f"Weather: {weather}, Frequency: {frequency}")
most_common_weather = weather_distribution.most_common(1)[0][0]
print("\nThe most common weather type is:", most_common_weather)
