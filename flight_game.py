# python version - game inputs - screen name

#Import libraries here

import mysql.connector



# functions here





# MAIN Program starts from here

# database connection code

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='him1234',
    autocommit=True
)

#game codes here


screenname = str(input("Please enter player's name: "))
