# Fetches all the EU large_airports and compares it to the parameter (ICAO code).
# Calls function weather_fetcher with the latitude and longitude of ICAO code, which returns current weather.
# For the rest of the large airports, function distance_emission_calculator is called for distance and CO2 emission data.
# Returns data to function new_game and fly_to.

import mysql.connector
import json
from icao_weather_fetcher import weather_fetcher
from distance_co2_calculator import distance_emission_calculator


def airport_fetcher(icao):
    list_of_big_european_airports = []             # For storing the fetched data.
    cursor = connection.cursor()
    cursor.execute(
        "SELECT airport.ident, airport.name, airport.municipality, country.name, airport.latitude_deg, airport.longitude_deg "
        "FROM airport, country WHERE airport.iso_country = country.iso_country AND airport.type = '" + "large_airport" + "'"
        "AND country.continent = '" + "EU" + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            if icao == row[0]:              # Checks if given parameter matches with ident of fetched data.
                active = True                   # If it does, becomes the active new airport
                weather = weather_fetcher(row[4], row[5])     # and calls function weather_fetcher, which returns its current weather.
                response = {
                    "ident": row[0],
                    "active": active,
                    "name": row[1],
                    "location": row[2],
                    "country": row[3],
                    "latitude": row[4],
                    "longitude": row[5],
                    "weather": weather,
                }
                json.dumps(response, default=lambda o: o.__dict__, indent=4)
                list_of_big_european_airports.insert(0, response)                       # Insert it to first place for more convenient use.
            else:
                active = False
                distance, co2_consumption = distance_emission_calculator(icao, row[0])      # Calls function that calculates in advance the distance and CO2 emission from parameter.
                response = {
                    "ident": row[0],
                    "active": active,
                    "name": row[1],
                    "location": row[2],
                    "country": row[3],
                    "latitude": row[4],
                    "longitude": row[5],
                    "distance": distance,
                    "co2_consumption": co2_consumption,
                }
                json.dumps(response, default=lambda o: o.__dict__, indent=4)
                list_of_big_european_airports.append(response)
    return list_of_big_european_airports


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )
