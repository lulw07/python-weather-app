import tkinter as tk
import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api-key").read()

def get_weather():
    city = city_entry.get()
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

        result_label.config(text="-------------------------------------------------------------\n"
                                 f"Weather stats for {city_name}, {country} | {datetime}\n"
                                 "-------------------------------------------------------------\n"
                                 f"Current weather: {weather}\n"
                                 f"Temperature: {temp_celsius}°C\n"
                                 f"Feels like: {feel_like}°C\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Wind speed: {wind_speed} km/h\n"
                                 "-------------------------------------------------------------\n"
                                 f"Sunrise: {dt.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M:%S')}\n"
                                 f"Sunset: {dt.datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M:%S')}\n"
                                 "-------------------------------------------------------------")
    else:
        result_label.config(text="City not found.")


window = tk.Tk()
window.title("Weather Forecast")

city_label = tk.Label(window, text="Enter city:")
city_label.pack(pady=10)

city_entry = tk.Entry(window)
city_entry.pack(pady=5)

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(window, wraplength=400)
result_label.pack(padx=20, pady=10)

window.mainloop()
