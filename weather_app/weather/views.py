from django.shortcuts import render
import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "295ebf1613d08e1db3962513565fa710"
CITY = "Berlin"

def index(request):
    weather_data = get_weather()
    return render(request, 'weather/index.html', {'weather_data': weather_data})

def get_weather():
    city = CITY
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url).json()

    if response["cod"] != "404":
        city_name = response["name"]
        country = response["sys"]["country"]
        weather = response["weather"][0]["description"]
        temp_celsius = response["main"]["temp"]
        feel_like = response["main"]["feels_like"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        datetime = dt.datetime.fromtimestamp(response["dt"]).strftime("%d-%m-%Y %H:%M:%S")

        weather_data = {
            'city_name': city_name,
            'country': country,
            'weather': weather,
            'temp_celsius': temp_celsius,
            'feel_like': feel_like,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'datetime': datetime,
        }

        return weather_data
    else:
        return None