import sys
import mysql.connector


def location_finder(ICAO):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + ICAO + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            print(f"\nCongratulations, you arrived at {row[1]} located in {row[2]}")
            return airport, municipality


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


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )


screen_name = input("Hello, please choose a username: ")
print(f"\nWelcome {screen_name} to \033[1m" + "Fairweather Tourist" + "\033[0m. It looks like you are currently in Helsinki, Finland.\n")
print("""Let me tell you a bit more about the game: \n
You have had this bucket list for a while now and it's time to put things finally into motion!
    - You wish to visit 5 locations in Europe. (List appears soon.)
    - Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
      and plan to minimalize CO2 emission.
    - As a matter of fact I will be your conscience and not allow you to travel further if CO2 emission reaches 4,5t. 
\nThe scoring system works the following way:
    - You need to score 2500 points to win.
    - If you guess one of the location: +500 points
    - If you guess "Easter Egg" location: +800 points
    - If target score is not reached, but allowed CO2 emission exceeded, the game ends.
""")

answer_rules = input(f"\nAre the rules clear and you are ready to see the goals, {screen_name} (yes/no)? ").lower()

while answer_rules != "yes":
    if answer_rules == "no":
        print('''
    - 5 locations need to be visited in Europe. (List appears soon.)
    - Protecting our planet is important so please minimalize CO2 emission.
    - Game ends if CO2 emission reaches 4,5t. 
    - In order to win, you need 2500 points.
    - If you guess one of the location: +500 points
    - If you guess "Easter Egg": +800 points
    - If target score is not reached, but allowed CO2 emission exceeded, the game ends.''')
        answer_rules = input("\nAre you ready to see the goals? ").lower()
    else:
        print("\nInvalid input, are you ready to see the goals? ")
        answer_rules = input("").lower()

print('''\nHere are the 5 locations:\n
(1) "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty"
(2) “Waves of South”: surfing lessons for the fainthearted
(3) “Charles' Eastern Comfort”: heavy food today, cholesterol tomorrow
(4) “Endless White Nights”: finding inner peace in the valleys of glacier
(5) “We’re Going to Ibiza!”: does it need more explanation?
(+1) "Easter Egg": “I was once called an old dame. In daylight I’m proudly wearing my scars of history, 
                   but when the night falls I put on my jewels to mesmerise you with my thousand sparks.”
''')

answer_firstlocation = input(f"\nAre the rules clear now and you are ready to choose your first location, {screen_name}, (yes/no)? ").lower()

while answer_firstlocation != "yes":
    if answer_firstlocation == "no":
        print('''\nTry to guess these 5 locations:\n
(1) "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty"
(2) “Waves of South”: surfing lessons for the fainthearted
(3) “Eastern Comfort for Charles”: heavy food today, cholesterol tomorrow
(4) “Endless White Nights”: finding inner peace in the valleys of glacier
(5) “We’re Going to Ibiza!”: does it need an explanation?
(+1) "Easter Egg": “I was once called an old dame. In daylight I’m proudly wearing my scars of history, 
                    but when the night falls I put on my jewels to mesmerise you with my thousand sparks.”
        ''')
        answer_firstlocation = input("\nAre you now ready to choose your first location? ").lower()
    else:
        print("\nInvalid input, are you ready to choose your first location? ").lower()
        answer_firstlocation = input("").lower()

total_score = 0
base_score = 500
bonus_score = 800

airports = {"EGKK": "London Gatwick Airport",
            "EGSS": "London Stansted Airport",
            "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport",
            "ENGM": "Oslo Airport",
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

while total_score < 2500:
    Country_code_input = input("\nEnter country's code: ").upper()
    while Country_code_input not in countries:
        print("\nOoops, wrong country, try again!")
        Country_code_input = input("\nEnter country's code: ").upper()
    airport_printer(Country_code_input)
    ICAO_code_input = input("\nPlease, type in the preferred ICAO code: ").upper()
    location_finder(ICAO_code_input)
    if ICAO_code_input in airports:
        total_score += base_score
        print(f"Your current score is {total_score}.")
        if ICAO_code_input == "LEIB":
            print(f'''\n{screen_name}, you arrived in Ibiza and you guessed the 5th location. Here is a funfact as reward:
                    This warm and beautiful mediterranean island, is known as a popular tourist destination, 
                    with a highly active nightlife.''')
        elif ICAO_code_input == "ENGM":
            print(f'''\n{screen_name}, you arrived in Oslo and you guessed 4th location. Here is a funfact as reward:
                    Dublin was founded by the Vikings, who were first spotted off the coast of Ireland in AD 792. 
                    In the 9th century, the Vikings invaded the region and established the Norse Kingdom of Dublin.''')
        elif ICAO_code_input == "LPPT":
            print(f'''\n{screen_name}, you arrived in Caparica and you guessed the 2nd location. Here is a funfact as reward:
                    This beautiful beach area hosts many different festivals, 
                    so don't be surprised to see people gathered here, especially on the weekends.''')
        elif ICAO_code_input == "LKPR":
            print(f'''\n{screen_name}, you arrived in Prague and you guessed the 3rd location. Here is a funfact as reward:
                    This historical city is filled with many beautiful landmarks 
                    and traditional arts like opera and theatre thrive here. 
                    Still the city has a modern side to this artistic talent, 
                    as it makes numerous appearances in movies, mainly due to the city's major film studios.''')
        else:
            print(f'''\n{screen_name}, you arrived in London and you guessed the 1st location. Here is a funfact as reward: 
                    The guards of the tower of London are called “Meat Eaters”. 
                    This is due to their historical role as the most important royal guards, 
                    as they were promised a proper meal, containing meat, even if the rest of the nation had a food crisis.''')
    elif ICAO_code_input == "LHBP":
        total_score += bonus_score
        print(f"Your current score is {total_score}.")
        print(f'''\n{screen_name}, you guessed the "Easter Egg" location. Here is the explanation of the riddle as reward:
                If you ever visit Budapest, pay attention to the buildings. 
                They are old, a lot of their frontage is deteriorating and a lot of them have bullet marks from WWII 
                and the Hungarian Revolution of 1956. When it gets dark, make sure you stroll at the bank of the Danube
                too see it lit up beautifully.''')
    else:
        print("\nUnfortunately, it's not a location from the list, let's try again!")

print(f"""
			.:''':.           .            * * *        .::::.         '
		   :__\ /__:	   __\(/__   . : .*__\/__*      ::::::      .  '  .
    . ' ' .:  / \.... 		 /)\     ' : '*  /\  *        ...      * \ * / *
   :__\ /__:' . :::::: .    | '            * * * '      *_\(/_* -= : = o = : =- 
   :  / \  :  : :::::: :    =      .******.    '.\./.'  *./)\.*    *:/ * \:*
	' . . '     '::::'    =====   * __\/__ *  --= o =--   '''       '  '  '
		  *                 |     *   /\   *   .'/.\.       *    ._____'___.
    Congratulations, {screen_name}. You won \033[1mFairweather Tourist\033[0m! 
    Your final score was: {total_score} and you CO2 emission was: .
			  *             |    .-' -|				   .---_..   |  .      |
		------------        |    | '  |           __   |     |   |  |   ¤  |   .
	  *	 ¤	¤  ¤  ¤  *		|    |  ¤ |   |  |   |  |_ |  ¤  | _ |         |   |
_____'	¤  ¤  ¤  ¤	¤ '   / " \  |    |-. "  "   | ¤         |   |      ¤  |___|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

sys.exit