import sys
import random
import mysql.connector
from geopy.distance import geodesic

# functions


def location_finder(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + icao + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            return airport, municipality


def list_of_airports_based_on_country_code(country_code):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, type, name, iso_country FROM airport "
                   "WHERE iso_country='" + country_code + "' ORDER BY type DESC")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[2]} is a {row[1]} type of airport which icao code is {row[0]}.")
    return

def random_location_generator():
    pass

def distance_calculator():
    pass

# main programme:
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name}. Welcome to theNameOfTheGame.")

initial_location = input("""
Let's start by choosing you location. 
Please enter A, if you have an airport already in your mind
or enter B, if you want me to print the airports of a certain country
or enter C, if you like surprises.
Your preference: """).upper()

while initial_location != "A" and initial_location != "B" and initial_location != "C":
    initial_location = input("Please answer with a valid letter. ").upper()

if initial_location == "A":
    airport_code = input("Please enter the icao code of the airport: ").upper()
    name_of_airport, name_of_municipality = location_finder(airport_code)
    print("The airport of your choice is: " + name_of_airport + " which locates in: " + name_of_municipality + ".")

elif initial_location == "B":
    country_name = input("Please enter the country code of the country: ").upper()
    list_of_airports_based_on_country_code(country_name)
    airport_code = input("Please enter the icao code of the airport, you wish to choose from the list: ").upper()
    name_of_airport, name_of_municipality = location_finder(airport_code)
    print("The airport of your choice is: " + name_of_airport + " which locates in: " + name_of_municipality + ".")

# elif initial_location == "C":
#    ("How ")


mean_of_transportation = input("""
Now let's choose your mean of transportation. 
You can either travel with helicopter by entering A
or enter B, if you'd rather fly an airplane. 
Your preference: """).upper()

while mean_of_transportation != "A" and mean_of_transportation != "B":
    mean_of_transportation = input("Please answer with a valid letter. ").upper()

if mean_of_transportation == "A":
    specification = input("""
    There are two types of helicopters: normal (xxx CO2 emission, yyy range)
    and electronic helicopter (xxx CO2 emission, yyy range).
    Please choose either the normal by entering C or the electronic by entering D.
    Your preference: """).upper()
    while specification != "C" and specification != "D":
        specification = input("Please answer with a valid letter. ").upper()
    if specification == "C":
        print("You chose the normal helicopter.")
    elif specification == "D":
        print("You chose the electronic helicopter.")

elif mean_of_transportation == "B":
    specification = input("""
    There are two types of airplanes: normal (xxx CO2 emission, yyy range)
    and electronic airport (xxx CO2 emission, yyy range).
    Please choose either the normal by entering E or the electronic by entering F.
    Your preference: """).upper()
    while specification != "E" and specification != "F":
        specification = input("Please answer with a valid letter. ").upper()
    if specification == "E":
        print("You chose the normal airplane.")
    elif specification == "F":
        print("You chose the electronic airplane.")
