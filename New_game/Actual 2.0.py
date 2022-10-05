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
         password='MariaDb', # NOTE: IT'S DIFFERENT FOR EVERYONE (Now it's Vlad's version)
         autocommit=True
         )


screen_name = input("Please choose a username: ")
print(f"Hello, {screen_name}, and welcome to \033[1m" + "Fairweather Tourist" + "\033[0m. It looks like you are currently in Helsinki, Finland.\n")
print("""Let me tell you a bit more about the game: \n
You have had this bucket list for a while now and you it's time to put things finally into motion!
- Based on your estimation you have overall €1200 to visit 5 locations in Europe.
- You wish that all these 5 locations would have a different weather condition compared to the ones you have already visited. 
- Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
  and plan to minimalize CO2 emission.
- I will be your conscience and not allow you to travel further once emission reaches ...... 
- ADD INFO ABOUT SCORING SYSTEM
""")

answer_rules = input(f"Are the rules clear and you are ready to see the goals, {screen_name}, (yes/no)? ").lower()

while answer_rules != "yes":
    if answer_rules == "no":
        print("Let me tell you part with slight change: \nMORE DETAILED DESCRIPTION")
        answer_rules = input("Are you ready to see the goals? ").lower()
    else:
        print("Invalid input, are you ready to see the goals? ").lower()
        answer_rules = input("").lower()

print("HERE ARE THE GOALS OF THE GAME:")
answer_firstlocation = input(f"Are the rules clear now and you are ready to choose your first location, {screen_name}, (yes/no)? ").lower()

while answer_firstlocation != "yes":
    if answer_firstlocation == "no":
        print("Here are the goals of the game: \nMORE DETAILED GOALS")
        answer_firstlocation = input("Are you now ready to choose your first location? ").lower()
    else:
        print("Invalid input, are you ready to choose your first location? ").lower()
        answer_firstlocation = input("").lower()

print("""Here are the game's goals:
- "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty" /Weather: rainy
- “Endless White Nights”: finally meeting Santa /Goal: snow
- Add goal
- Add goal
- “We’re Going to Ibiza!”: does it need an explanation? /Goal: sunny
- "Easter Egg": “I was once called an old dame. In daylight I’m proudly wearing my scars of history, 
                but when the night falls I put on my jewels to mesmerise you with my thousand sparks.”

""")

# Initial score is always 0, base score is subject to change since we will complicate the game with API
total_score = 0
base_score = 500
bonus_score = 800

# All of the correct answers:
airports = {"EGKK": "London Gatwick Airport",
            "EGSS": "London Stansted Airport",
            "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport",
            "EFRO": "Rovaniemi", #does not work yet (not printed because it is not large airport)
            "LPPT": "Humberto Delgado Airport (Lisbon Portela)",
            "LKPR": "V?clav Havel Airport Prague",
            "LEIB": "Ibiza Airport"}

# List of correct countries:
countries = {"GB": "Great Britain",
            "FI": "Finland",
            "PT": "Portugal",
            "CZ": "Czech Republic",
            "ES": "Spain",
            "HU": "Hungary"}

while total_score < 2500:
    Country_code_input = input("Enter country's code: ").upper() # asks user for a country code where player wants to go
    while Country_code_input not in countries: # if the country is not on our list, it asks to try again until user guesses it
        print("Ooops, wrong country, try again!")
        Country_code_input = input("Enter country's code: ").upper()
    airport_printer(Country_code_input) #all LARGE airports in that country are printed
    ICAO_code_input = input("Please, write down the preferred ICAO code: ").upper() #ask to write the preferred icao code
    location_finder(ICAO_code_input)
    if ICAO_code_input in airports:
        total_score += base_score
        print(f"Your current score is {total_score}") #Just for testing, can be deleted later
        if ICAO_code_input == "LEIB":
            print(f'''{screen_name}, you guessed the 5st location and in Ibiza. Here is a funfact as reward:
                    This warm and beautiful mediterranean island, is known as a popular tourist destination, 
                    with a highly active nightlife.''')  # add fun fact
        elif ICAO_code_input == "EFRO":
            print(f'''{screen_name}, you guessed the 2st location in Rovaniemi. Here is a funfact as reward:
                    Santa Claus village is in Rovaniemi, where you can meet Santa, and his reindeer. 
                    If you can't make it there every year to make your wish, don't worry you can just mail him, 
                    just like thousands of children every year.''')  # add fun fact
        elif ICAO_code_input == "LPPT":
            print(f'''{screen_name}, you guessed the 3st location and in Caparica. Here is a funfact as reward:
                    This beautiful beach area hosts many different festivals, 
                    so don't be surprised to see people gathered here, especially on the weekends.''')  # add fun fact
        elif ICAO_code_input == "LKPR":
            print(f'''{screen_name}, you guessed the 4st location and in Prague. Here is a funfact as reward:
                    This historical city is filled with many beautiful landmarks 
                    and traditional arts like opera and theatre thrive here. 
                    Still the city has a modern side to this artistic talent, 
                    as it makes numerous appearances in movies, mainly due to the city's major film studios.''')  # add fun fact
        else: # this "else" in practice means that ICAO_code_input == "EGKK": or "EGSS" or "EGGW" or "EGLL":
            print(f'''{screen_name}, you guessed the 1st location and in London. Here is a funfact as reward: 
                    The guards of the tower of London are called “Meat Eaters”. 
                    This is due to their historical role as the most important royal guards, 
                    as they were promised a proper meal, containing meat, even if the rest of the nation had a food crisis.''')
    elif ICAO_code_input == "LHBP":
        total_score += bonus_score
        print(f"Your current score is {total_score}")  # Just for testing, can be deleted later
        print(f'''{screen_name}, you guessed the "Easter Egg" location. Here is the explanation as reward:
        If you ever visit Budapest, pay attention to the buildings. 
        They are old, a lot of their frontage is deteriorating and a lot of them have bullet marks from WWII 
        and the Hungarian Revolution of 1956. When it gets dark, make sure you stroll at the bank of the Danube
        too see it lit up beautifully.''') # add fun fact
    else:
        print("Unfortunately, it's not that airport, let's try again!")

print(f"""
			.:''':.           .            * * *        .::::.         '
		   :__\ /__:	   __\(/__   . : .*__\/__*      ::::::      .  '  .
    . ' ' .:  / \.... 		 /)\     ' : '*  /\  *        ...      * \ * / *
   :__\ /__:' . :::::: .    | '            * * * '      *_\(/_* -= : = o = : =- 
   :  / \  :  : :::::: :    =      .******.    '.\./.'  *./)\.*    *:/ * \:*
	' . . '     '::::'    =====   * __\/__ *  --= o =--   '''       '  '  '
		  *                 |     *   /\   *   .'/.\.            ._____'___.
Congratulations, {screen_name}. You won \033[1mFairweather Tourist\033[0m! Your final score was: {total_score}.  
			  *             |    .-' -|				   .---_..   |  .      |
		------------        |    | '  |           __   |     |   |  |   ¤  |   .
	  *	 ¤	¤  ¤  ¤  *		|    |  ¤ |   |  |   |  |_ |  ¤  | _ |         |   |
_____'	¤  ¤  ¤  ¤	¤ '   / " \  |    |-. "  "   | ¤         |   |      ¤  |___|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")  #player won the game, finish

sys.exit