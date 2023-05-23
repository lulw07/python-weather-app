import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api-key").read()
CITY = "Berlin"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=metric"

response = requests.get(url).json()

city = response["name"]
country = response["sys"]["country"]
weather = response["weather"][0]["description"]
temp_celsius = response["main"]["temp"]
feel_like = response["main"]["feels_like"]
humidity = response["main"]["humidity"]
wind_speed = response["wind"]["speed"]
datetime = dt.datetime.fromtimestamp(response["dt"]).strftime("%d-%m-%Y %H:%M:%S")

print("-------------------------------------------------------------")
print(f"Weather stats for {city}, {country} | {datetime}")
print("-------------------------------------------------------------")
print(f"Current weather: {weather}")
print(f"Temperature: {temp_celsius}°C")
print(f"Feels like: {feel_like}°C")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} km/h")
print("-------------------------------------------------------------")
print(f"Sunrise: {dt.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M:%S')}")
print(f"Sunset: {dt.datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M:%S')}")
print("-------------------------------------------------------------")