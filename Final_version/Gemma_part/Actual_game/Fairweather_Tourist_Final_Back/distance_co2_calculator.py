# Called by function airport_fetcher, parameters: ICAO code of current and possible new location.
# Based on ICAO code, fetches latitude and longitude,
# geopy calculates the distance,
# CO2 emission also calculated.
# Returns distance and CO2.

import mysql.connector
from geopy import distance


def distance_emission_calculator(current_location, next_location):
    current_coordinate = []                                          # Fetching and storing of longitude and latitude for both locations.
    next_coordinate = []
    cursor1 = connection.cursor()
    cursor1.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + current_location + "'")
    current_icao = cursor1.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + next_location + "'")
    next_icao = cursor2.fetchall()
    for coordinate in current_icao:
        current_coordinate.append(coordinate)
    for coordinate in next_icao:
        next_coordinate.append(coordinate)
    distance_between_locations = round(distance.distance(tuple(current_coordinate), tuple(next_coordinate)).km)     # Calculation of distance.
    additional_emission = round(distance_between_locations * 0.156)                             # Calculation and rounding of CO2 emission.
    return distance_between_locations, additional_emission


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )
