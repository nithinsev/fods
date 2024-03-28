weather_data = {
    'Sunny': 50,
    'Rainy': 30,
    'Cloudy': 40,
    'Snowy': 10,
    'Foggy': 20
}
weather_distribution = {}

for weather, frequency in weather_data.items():
    if frequency in weather_distribution:
        weather_distribution[frequency].append(weather)
    else:
        weather_distribution[frequency] = [weather]
most_common_frequency = max(weather_distribution.keys())
most_common_weather = weather_distribution[most_common_frequency]
print("The most common weather type(s) is/are:", most_common_weather, "with a frequency of", most_common_frequency)
