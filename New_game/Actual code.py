import sys
import mysql.connector


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


def airport_printer(country_code):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, type, name, iso_country FROM airport "
                   "WHERE iso_country='" + country_code + "' ORDER BY type DESC")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[2]} is a {row[1]} type of airport which icao code is {row[0]}.")
    return


# main game
# NOTE: IT'S DIFFERENT FOR EVERYONE
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='cars',
         user='root',
         password='MariaDB',
         autocommit=True
         )

screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name} and welcome to theNameOfTheGame. It looks like you are currently in Helsinki, Finland.")
print(""" Let me tell you a bit more about the game:
You have had this bucket list for a while now and you decided it's time to put things finally into motion.
Based on your calculation you have overall 1200 euro to visit 5 locations in Europe.
You wish that all these 5 location will each have a different weather condition to the ones you have already visited. 
Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
and plan your trip ahead to minimalize unnecessary CO2 emission.
""")

# ask player BY NAME if all is clear and ready to see the goals use .lower() at the end
# while answer is not "yes":
    # if answer is "no":
    #   print our the let me tell you part with slight change.
    #   ask player if all is clear and ready to see the goals use .lower() at the end
    # else:
    #   print: invalid input and ask if all is clear and ready to see goals

#print(""" #put the goals here
# """)

# ask player BY NAME if all is clear and ready to choose first location, use .lower() at the end
# while answer is not "yes":
    # if answer is "no":
    #   print our to goals
    #   ask again if all is clear and ready to choose first location, use .lower() at the end
    # else:
    #   print: invalid input and ask if all is clear and ready to choose first location

total_score = 0
# while total_score < 2500:
    # variable that asks the for a country code where player wants to go
    # call the airport printer based on country code
    # print out result
    # ask to write the preferred icao code:
    # call location finder
    # print out the players new location: You have arrived to
    # if icao code == any of the stated airport of the goal:
        # base_score = 500
        # total_score += base_score
        # if icao code = e.g. prague:
        #   print out fun fact
        # elif: previous if repeats one by one with each extra until no airport left
        #   print out the fun fact
    # elif icao == budapest:
        # bonus_score = 800
        # total_score += bonus_score
        # print out explanation of the riddle and give fun fact

# when player reaches 2500 we let it know that it has won the game and congratulate
# if you want, you can look for some python firework drawing and print it along with the text

sys.exit