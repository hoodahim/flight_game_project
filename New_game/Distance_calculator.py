import mysql.connector
from geopy import distance


def distance_calculator(current_location, next_location):
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
    distance_between_locations = round(distance.distance(tuple(current_coordinate), tuple(next_coordinate)).km, 2)
    return distance_between_locations


def CO2_emmision_calculator(kilometers):
    CO2_emission = round(kilometers * 0.156, 2)
    return CO2_emission


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='CamdenTown',
    autocommit=True
)

current_place = input("current").upper()
next_place = input("next").upper()
kilometers = distance_calculator(current_place, next_place)
print(kilometers)

change_of_emission = CO2_emmision_calculator(kilometers)
print(change_of_emission)