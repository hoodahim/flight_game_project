# Called by function airport_fetcher, parameter: latitude and longitude to call the weather API.
# Returns the current weather.

import requests
import math
import json


def weather_fetcher(latitude, longitude):
    api_key = "628dc836c467279560786b9ec5b2a731"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url).json()                         # Fetches the data based on latitude and longitude from OpenWeather API.
    temperature_celsius = response['main']['temp'] - 273.25     # Converting it to celsius.
    rounded_celsius = math.floor(temperature_celsius + 0.5)     # Rounding of celsius.
    wind_speed = response['wind']['speed']
    rounded_wind = math.floor(wind_speed + 0.5)                 # Rounding of wind speed.
    weather_condition = {
        "main": response['weather'][0]['main'],
        "temp": rounded_celsius,
        "wind": rounded_wind
    }
    json.dumps(response, default=lambda o: o.__dict__, indent=4)
    return weather_condition
