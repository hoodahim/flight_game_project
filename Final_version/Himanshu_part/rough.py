import random
import mysql.connector
import json

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='him1234',
         autocommit=True
         )

sql = "SELECT airport.ident, airport.name, airport.municipality, country.name, airport.latitude_deg, airport.longitude_deg "
sql += "FROM airport, country WHERE airport.iso_country = country.iso_country AND airport.type = '" + "large_airport" + "'"
sql += "AND country.continent = '" + "EU" + "'"
print(sql)
cursor = connection.cursor()
response = cursor.fetchall()
airport_list = []
for r in response:
    #data = {'name': r[1], 'latitude': r[4], 'longitude': r[5]}
    #print(data)
    data = json.dumps(r)
    print(data)
