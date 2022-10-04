import sys
import mysql.connector


# Function to find the airport based on entered ICAO code (by user) and provide with airport's name & municipality
def location_finder(ICAO):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + ICAO + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            return airport, municipality


# Function to print the airport's information based on country code entered by user
def airport_printer(country_code):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, type, name, iso_country FROM airport "
                   "WHERE iso_country='" + country_code + "' ORDER BY type DESC")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[2]} is a {row[1]} type of airport which ICAO code is {row[0]}.")
    return


# main game
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='cars', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         user='root', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         password='MariaDB', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         autocommit=True
         )

ICAO_code_input = input("Enter ICAO code of an airport: ")
location_finder(ICAO_code_input)

Country_code_input = input("Enter country's code: ")
airport_printer(Country_code_input)

screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name}, and welcome to \033[1m" + "theNameOfTheGame" + "\033[0m. It looks like you are currently in Helsinki, Finland.\n")
print("""Let me tell you a bit more about the game: \n
You have had this bucket list for a while now and you decided it's time to put things finally into motion!
- Based on your calculation you have overall 1200 EUR to visit 5 locations in Europe.
- You wish that all these 5 locations will each have a different weather condition compared to the ones you have already visited. 
- Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
  and plan your trip ahead to minimalize unnecessary CO2 emission.
""")

# print(f"Are the rules clear to you and you are ready to see the goals, {screen_name} (yes/no)?")
answer = input(f"Are the rules clear to you, and you are ready to see the goals, {screen_name} (yes/no)? ").lower()

while answer != "yes":
    if answer == "no":
        print("Let me tell you part with slight change: \nMORE DETAILED DESCRIPTION")
        answer = input("").lower()
    else:
        print("Invalid input, are you ready to see the goals?")
        answer = input("").lower()

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