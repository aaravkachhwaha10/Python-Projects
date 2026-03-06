cities = []
aqi_values = []
num_cities = int(input("How many cities AQI do you wast to enter?  "))
for i in range (num_cities):
    city_name = input(f"Enter name for city {i+1}: ")
    aqi_value = int(input(f"ENter AQI value for {city_name}: "))
    cities.append(city_name)
    aqi_values.append(aqi_value)
safe_cities = ""
dangerous_cities = ""
for i in range (len(cities)):
    city = cities[i]
    aqi = aqi_values[i]
    if aqi <= 100:
        safe_cities += city + f" (Aqi: {aqi})\n"
    else:
        dangerous_cities += city + f" (AQI: {aqi})\n"
print("\n Safe Zone Cities (AQI < 100):\n" + safe_cities)
print(" Dangerous Zone Cities (AQI > 100):\n" + dangerous_cities)