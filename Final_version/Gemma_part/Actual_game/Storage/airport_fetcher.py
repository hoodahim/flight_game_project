# Fetches all the big European airports and "json"-ed it.

import mysql.connector
import json


def airport_fetcher():
    list_of_big_european_airports = []
    cursor = connection.cursor()
    cursor.execute(
        "SELECT airport.ident, airport.name, airport.municipality, country.name, airport.latitude_deg, airport.longitude_deg "
        "FROM airport, country WHERE airport.iso_country = country.iso_country AND airport.type = '" + "large_airport" + "'"
        "AND country.continent = '" + "EU" + "'")
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for row in result:
            response = {
                "ident": row[0],
                "name": row[1],
                "location": row[2],
                "country": row[3],
                "latitude": row[4],
                "longitude": row[5],
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

list_of_airports = airport_fetcher()
print(list_of_airports)
