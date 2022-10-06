import sys
import mysql.connector
import random

# Function to find the airport based on entered ICAO code (by user) and provide with airport's name & municipality
def location_finder(ICAO):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + ICAO + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            print(f"Congratulations, you have arrived at {row[1]} located in {row[2]}")
            return airport, municipality

# Function to print the airport's information based on country code entered by user (ONLY large airports are considered)

def airport_printer(country_code):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality, iso_country FROM airport "
                   "WHERE iso_country='" + country_code + "' AND type = '" + "large_airport" + "'"
                   "ORDER BY type DESC")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[1]} is located in {row[2]} and the ICAO code is {row[0]}.")
    return


# main game START
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         user='root', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         password='him1234', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         autocommit=True
         )

screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name}, and welcome to \033[1m" + "Fairweather Tourist" + "\033[0m. It looks like you are currently in Helsinki, Finland.\n")
print("""Let me tell you a bit more about the game: \n
You have had this bucket list for a while now and you decided it's time to put things finally into motion!
- Based on your calculation you have overall 1200 EUR to visit 5 locations in Europe.
- You wish that all these 5 locations will each have a different weather condition compared to the ones you have already visited. 
- Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
  and plan your trip ahead to minimalize unnecessary CO2 emission.
- ADD INFO ABOUT SCORING SYSTEM
""")

answer_rules = input(f"Are the rules clear to you, and you are ready to see the goals, {screen_name}, (yes/no)? ").lower()

while answer_rules != "yes":
    if answer_rules == "no":
        print("Let me tell you part with slight change: \nMORE DETAILED DESCRIPTION")
        answer_rules = input("Are you ready to see the goals? ").lower()
    else:
        print("Invalid input, are you ready to see the goals? ")
        answer_rules = input("").lower()

print("HERE ARE THE GOALS OF THE GAME:")
answer_firstlocation = input(f"Are the rules clear to you now, and you are ready to choose your first location, {screen_name}, (yes/no)? ").lower()

while answer_firstlocation != "yes":
    if answer_firstlocation == "no":
        print("Here are the goals of the game: \nMORE DETAILED GOALS")
        answer_firstlocation = input("Are you now ready to choose your first location? ").lower()
    else:
        print("Invalid input, are you ready to choose your first location? ")
        answer_firstlocation = input("").lower()

print("""Here are the game's goals:
- "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty"
- Goal: rainy, (12-18 C?)
- Add goal
- Add goal
- Add goal
- Add goal
""")

# Initial score is always 0, base score is subject to change since we will complicate the game with API
total_score = 0
base_score = 500
bonus_score = 800

# Initial CO2 value is 0
CO2_emission = 0

# All of the correct answers:
airports = {"EGKK": "London Gatwick Airport",
            "EGSS": "London Stansted Airport",
            "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport",
            "ENGM": "Oslo",  # CHANGED LOCATION
            "LPPT": "Humberto Delgado Airport (Lisbon Portela)",
            "LKPR": "V?clav Havel Airport Prague",
            "LEIB": "Ibiza Airport"}

# List of correct countries:
countries = {"GB": "Great Britain",
             "NO": "Norway",
             "PT": "Portugal",
             "CZ": "Czech Republic",
             "ES": "Spain",
             "HU": "Hungary"}

answer_list = []  # the ICAO_code_input answers are saved to this list so they cannot be replicated
ICAO_code_input=""
# absolute CO2 emission limit is set to 300 * 15 = 4500 (so once this value is reached (or score achieved) the game will finish)

while total_score < 2500 and CO2_emission < 4500:
    Country_code_input = input(
        "Enter country's code: ").upper()  # asks user for a country code where player wants to go
    airport_printer(Country_code_input)  # all LARGE airports in that country are printed
    ICAO_code_input = input(
        "Please, write down the preferred ICAO code: ").upper()  # ask to write the preferred icao code

    if ICAO_code_input in answer_list:
        print("You have already entered this location, try another one!")
    else:
        answer_list.append(ICAO_code_input)
        location_finder(ICAO_code_input)
    # Below I tried to restrict user input to the same airport multiple times, but failed

    # answer_list.append(ICAO_code_input)  # adds a new ICAO code once the user types it in

    # if ICAO_code_input in answer_list:
    # print("You have already entered this location, try another one!")
    # ICAO_code_input = input("Please, write down the preferred ICAO code: ").upper()  # ask to write AGAIN the preferred icao code
    # answer_list.append(ICAO_code_input)  # adds a new ICAO code once the user types it in

    # print(answer_list) #just to check what ICAO codes are saved

        if ICAO_code_input in airports:
            total_score = total_score + base_score
            CO2_emission = CO2_emission + random.randint(250, 350)
            print(
            f"Your current score is {total_score}, and CO2 emission is {CO2_emission}")  # Just for testing, can be deleted later
            if ICAO_code_input == "LEIB":
                print("You guessed in right, now you are in Ibiza!")  # add fun fact
            elif ICAO_code_input == "ENGM":
                print("You guessed in right, now you are in Oslo!")  # add fun fact
            elif ICAO_code_input == "LPPT":
                print("You guessed in right, now you are in Lisbon!")  # add fun fact
            elif ICAO_code_input == "LKPR":
                print("You guessed in right, now you are in Prague!")  # add fun fact
            else:  # this "else" in practice means that ICAO_code_input == "EGKK": or "EGSS" or "EGGW" or "EGLL":
                print("You guessed it right, now you are in London! Here is fun fact about it:")
        elif ICAO_code_input == "LHBP":
            total_score = total_score + bonus_score
            CO2_emission = CO2_emission + random.randint(250, 350)
            print(
            f"Your current score is {total_score} and CO2 emission is {CO2_emission}")  # Just for testing, can be deleted later
            print("You guessed in right, now you are in Budapest!")  # add fun fact
        elif ICAO_code_input not in airports and Country_code_input in countries:
            CO2_emission = CO2_emission + random.randint(250, 350)
            print(CO2_emission)  # Just for check
            print("Unfortunately, the airport is not right, but you guessed the country right!")
        else:
            CO2_emission = CO2_emission + random.randint(250, 350)
            print(CO2_emission)  # Just for check
            print("Unfortunately, the location is not in this country, try another one!")

if total_score >= 2500:
    print(
        f"Congratulations, {screen_name}, you have won the game! You final score is {total_score} and CO2 emission is {CO2_emission}.")  # player won the game, finish
else:
    print(
        f"Unfortunately, {screen_name}, you have exceeded the maximum allowed value of CO2 emission, your final score is {total_score} with {CO2_emission} CO2 emission.")  # player lost the game

# if you want, you can look for some python firework drawing and print it along with the text

sys.exit