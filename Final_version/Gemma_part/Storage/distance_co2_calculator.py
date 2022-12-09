# Takes two icao code, fetches their coordinates and calculates distance and CO2 emission.

import mysql.connector
from geopy import distance


def distance_emission_calculator(current_location, next_location):
    current_coordinate = []
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
    distance_between_locations = round(distance.distance(tuple(current_coordinate), tuple(next_coordinate)).km)
    additional_emission = round(distance_between_locations * 0.156)
    return distance_between_locations, additional_emission


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

old = 'EGKK'
new = 'LEIB'
odometer = distance_emission_calculator(old, new)
print(odometer)
print(f"They are {odometer[0]}km away and the travel generates {odometer[1]}kg")


