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
         database='cars', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         user='root', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         password='MariaDB', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         autocommit=True
         )

screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name}, and welcome to \033[1m" + "theNameOfTheGame" + "\033[0m. It looks like you are currently in Helsinki, Finland.\n")
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

# All of the correct answers:
airports = {"EGKK": "London Gatwick Airport",
            "EGSS": "London Stansted Airport",
            "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport",
            "EFRO": "Rovaniemi",
            "LPPT": "Humberto Delgado Airport (Lisbon Portela)",
            "LKPR": "V?clav Havel Airport Prague",
            "LEIB": "Ibiza Airport"}

# Countries' id: Great Britain (GB), Finland (FI), Portugal (PT), Czech Republic (CZ), Spain (ES)
# List of correct countries:
countries = {"GB": "Great Britain",
            "FI": "Finland",
            "PT": "Portugal",
            "CZ": "Czech Republic",
            "ES": "Spain"}

while total_score < 2500:
    Country_code_input = input("Enter country's code: ").upper() # asks user for a country code where player wants to go
    while Country_code_input not in countries: # if the country is not on our list, it asks to try again until user guesses it
        print("Ooops, wrong country, try again!")
        Country_code_input = input("Enter country's code: ").upper()
    airport_printer(Country_code_input) #all LARGE airports in that country are printed
    ICAO_code_input = input("Please, write down the preferred ICAO code: ").upper() #ask to write the preferred icao code
    location_finder(ICAO_code_input)
    if ICAO_code_input in airports:
        total_score = total_score + base_score
        print(f"Your current score is {total_score}") #Just for testing, needs to be deleted later
        if ICAO_code_input == "EGKK" or "EGSS" or "EGGW" or "EGLL":
            print("You guessed it right, now you are in London! Here is fun fact about it:")
        elif ICAO_code_input == "EFRO":
            print("You guessed in right, now you are in Rovaniemi!") #add fun fact
        elif ICAO_code_input == "LPPT":
            print("You guessed in right, now you are in Lisbon!")  # add fun fact
        elif ICAO_code_input == "LKPR":
            print("You guessed in right, now you are in Prague!")  # add fun fact
        elif ICAO_code_input == "LEIB":
            print("You guessed in right, now you are in Ibiza!")  # add fun fact
    else:
        print("Unfortunately, it's not that airport, let's try again!")

print(f"Congratulations, {screen_name}, you have won the game! You final score is {total_score}.")

# while total_score < 2500:
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