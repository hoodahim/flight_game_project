# Gets the weather with latitude and longitude.

import requests
import json
import math


def get_weather(api, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    response = requests.get(url).json()
#    print(response)
    temperature_celsius = response['main']['temp'] - 273.25            # converting it to celsius
    rounded_celsius = math.floor(temperature_celsius + 0.5)            # rounding
#    print(rounded_celsius)
    weather_condition = {
        "main": response['weather'][0]['main'],
        "description": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon'],
        "temp": rounded_celsius,
        "wind": response['wind']['speed']
    }
    json.dumps(response, default=lambda o: o.__dict__, indent=4)
    return weather_condition


api_key = "628dc836c467279560786b9ec5b2a731"
longitude = -0.36833301186561584    # long., lat. example from our own DB
latitude = 51.874698638916016
weather_of_current = get_weather(api_key, latitude, longitude)
print(weather_of_current)
