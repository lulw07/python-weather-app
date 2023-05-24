from django.shortcuts import render
import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "295ebf1613d08e1db3962513565fa710"

def index(request):
    city = get_city(request.GET.get('city', ' '))
    weather_data = get_weather(city)
    return render(request, 'weather/index.html', {'weather_data': weather_data})

def get_city(city):
    return city

def get_icon(icon):
    image = "http://openweathermap.org/img/wn/" + icon + ".png"
    return image

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url).json()

    if response["cod"] != "404":
        icon = response["weather"][0]["icon"]
        icon = get_icon(icon)
        city_name = response["name"]
        country = response["sys"]["country"]
        weather = response["weather"][0]["description"]
        temp_celsius = response["main"]["temp"]
        feel_like = response["main"]["feels_like"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        alert_wind_speed = wind_speed * 3.6
        datetime = dt.datetime.fromtimestamp(response["dt"]).strftime("%d-%m-%Y %H:%M:%S")

        weather_data = {
            'icon': icon,
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
