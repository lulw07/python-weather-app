import tkinter as tk
import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api-key").read()
CITY = "Berlin"


def get_weather():
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

    result_label.config(text="-------------------------------------------------------------\n"
                             f"Weather stats for {city}, {country} | {datetime}\n"
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


# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Wettervorhersage")

# Erstelle ein Label für den Ergebnisbereich
result_label = tk.Label(window, wraplength=400)
result_label.pack(padx=20, pady=10)

# Erstelle einen Button, um die Wetterdaten abzurufen
get_weather_button = tk.Button(window, text="Wetter abrufen", command=get_weather)
get_weather_button.pack(pady=10)

# Starte die Hauptereignisschleife des Fensters
window.mainloop()
