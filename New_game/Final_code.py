import sys
import mysql.connector
import random


def location_finder(ICAO):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + ICAO + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            print(f"\nCongratulations, you have arrived at {row[1]} located in {row[2]}.")
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


def icao_code_checker(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT ident FROM airport WHERE ident='" + icao + "'")
    cursor.fetchall()
    if cursor.rowcount > 0:
        change = random.randint(200, 300)
        return change


def rule_printer():
    print("""\nYou have had this bucket list for a while now and it's time to put things finally into motion!
    - You wish to visit 5 locations in Europe. (List appears soon.)
    - Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
      and plan to minimalize CO2 emission.
    - As a matter of fact I will be your conscience and not allow you to travel further if CO2 emission reaches 3,75 t. 
\nThe scoring system works the following way:
    - You need to score 2500 points to win.
    - If you guess one of the location: +500 points
    - If you guess "Easter Egg" location: +800 points
    - If target score is not reached, but allowed CO2 emission exceeded, the game ends.""")
    return


def goal_printer():
    print('''\nHere are the 5 locations:\n
    (1) "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty"
    (2) “Waves of South”: surfing lessons for the fainthearted
    (3) “Charles' Eastern Comfort”: heavy food today, cholesterol tomorrow
    (4) “Endless White Nights”: finding inner peace in the valleys of glacier
    (5) “We’re Going to Ibiza!”: does it need more explanation?
    (+1) "Easter Egg": “I was once called an old dame. In daylight I’m proudly wearing my scars of history, 
                       but when the night falls I put on my jewels to mesmerise you with my thousand sparks.”''')


def country_code_printer():
    print("""\nHere are the country codes of the European countries.
Albania: AL, Andorra: AM, Armenia: AM, Austria: AT, Belarus: BY, Belgium: BE, Bosnia and Herzegovina: BA, 
Bulgaria: BG, Croatia: HR, Cyprus: CY, Czech Republic: CZ, Denmark: DK, Estonia: EE, Faroe Island: FO, Finland: FI, 
France: FR, Georgia: GE, Germany: DE, Gibraltar: GI, Greece: GR, Hungary: HU, Iceland: IS, Ireland: IE, Isle of Man: IM, 
Italy: IT, Kosovo: XK, Latvia: LV, Liechtenstein: LI, Lithuania: LT, Luxembourg: LU, Macedonia: MK, Malta: MT, 
Moldova: MD, Monaco: MC, Montenegro: ME, Netherlands: NL, Norway: NO, Poland: PL, Portugal: PT, Romania: RO, 
Russian Federation: RU, San Marino: SM, Serbia: RS, Slovakia: SK, Spain: ES, Sweden: SE, Switzerland: CH, 
Turkey: TR, United Kingdom: GB, Vatican City State, VA""")


def london_funfact():
    print(f'''\n{screen_name}, you arrived in London and you guessed the 1st location. Here is a funfact as reward: 
        The guards of the tower of London are called “Meat Eaters”. 
        This is due to their historical role as the most important royal guards, 
        as they were promised a proper meal, containing meat, even if the rest of the nation had a food crisis.''')


def prague_funfact():
    print(f'''\n{screen_name}, you arrived in Prague and you guessed the 3rd location. Here is a funfact as reward:
        This historical city is filled with many beautiful landmarks and traditional arts 
        like opera and theatre thrive here. Still the city has a modern side to this artistic talent, 
        as it makes numerous appearances in movies, mainly due to the city's major film studios.''')


def oslo_funfact():
    print(f'''\n{screen_name}, you arrived in Oslo and you guessed 4th location. Here is a funfact as reward:
        Dublin was founded by the Vikings, who were first spotted off the coast of Ireland in AD 792. 
        In the 9th century, the Vikings invaded the region and established the Norse Kingdom of Dublin.''')


def ibiza_funfact():
    print(f'''\n{screen_name}, you arrived in Ibiza and you guessed the 5th location. Here is a funfact as reward:
        This warm and beautiful mediterranean island, is known as a popular tourist destination, 
        with a highly active nightlife.''')


def caparica_funfact():
    print(f'''\n{screen_name}, you arrived in Caparica and you guessed the 2nd location. Here is a funfact as reward:
                    This beautiful beach area hosts many different festivals, 
                    so don't be surprised to see people gathered here, especially on the weekends.''')


def budapest_funfact():
    print(f'''\n{screen_name}, you guessed the "Easter Egg" location. Here is the explanation of the riddle as reward:
                    If you ever visit Budapest, pay attention to the buildings. 
                    They are old, a lot of their frontage is deteriorating and a lot of them have bullet marks from WWII 
                    and the Hungarian Revolution of 1956. When it gets dark, make sure you stroll at the bank of the Danube
                    too see it lit up beautifully.''')


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='him1234',
         autocommit=True
         )

screen_name = input("Hello, please enter your name: ")
print(f"""\nWelcome {screen_name} to \033[1mFairweather Tourist\033[0m. It looks like you are currently in Helsinki, Finland.
Let me tell you a bit more about the game: """)

rule_printer()
answer_rules = input(f"\n{screen_name}, are the rules clear and are you ready to see the goals(yes/no)? ").lower()
while answer_rules != "yes":
    if answer_rules == "no":
        rule_printer()
        answer_rules = input("\nAre you ready now to see the goals? ").lower()
    else:
        answer_rules = input("\nInvalid input, are you ready to see the goals? ").lower()

goal_printer()
answer_first_location = input(f"\n{screen_name}, are the goals clear and are you ready to choose your first location(yes/no)? ").lower()
while answer_first_location != "yes":
    if answer_first_location == "no":
        goal_printer()
        answer_first_location = input("\nAre you now ready to choose your first location? ").lower()
    else:
        answer_first_location = input("\nInvalid input, are you ready to choose your first location? ").lower()

country_code_printer()
airports = {"EGKK": "London Gatwick Airport", "EGSS": "London Stansted Airport", "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport", "ENGM": "Oslo Airport", "LPPT": "Humberto Delgado Airport (Lisbon Portela)",
            "LKPR": "V?clav Havel Airport Prague", "LEIB": "Ibiza Airport"}
countries = {"GB": "Great Britain", "NO": "Norway", "PT": "Portugal", "CZ": "Czech Republic", "ES": "Spain", "HU": "Hungary"}

total_score = CO2_emission = 0
base_score = 500
bonus_score = 800
answer_list = []
while total_score < 2500 and CO2_emission < 3750:
    # print(answer_list)
    Country_code_input = input("\nEnter country's code: ").upper()
    airport_printer(Country_code_input)
    ICAO_code_input = input("\nEnter ICAO code: ").upper()
    if ICAO_code_input in answer_list:
        print("\nYou have already visited that location, try another one!")
    else:
        answer_list.append(ICAO_code_input)
        location_finder(ICAO_code_input)
        CO2_change = random.randint(200, 300)
        CO2_emission += CO2_change
        if ICAO_code_input in airports:
            total_score += base_score
            if ICAO_code_input == "LEIB":
                ibiza_funfact()
            elif ICAO_code_input == "ENGM":
                oslo_funfact()
            elif ICAO_code_input == "LPPT":
                caparica_funfact()
            elif ICAO_code_input == "LKPR":
                prague_funfact()
            else:
                london_funfact()
                answer_list.append("EGKK")
                answer_list.append("EGSS")
                answer_list.append("EGGW")
                answer_list.append("EGLL")
        elif ICAO_code_input == "LHBP":
            total_score += bonus_score
            budapest_funfact()
        elif ICAO_code_input not in airports and Country_code_input in countries:
            print("\nUnfortunately, the airport is not right, but you guessed the country right!")
        else:
            print("\nUnfortunately, the location is not in this country, try another one!")
        print(f"Your current score is {total_score} points and CO2 emission is {CO2_emission}kg.")

if total_score >= 2500:
    print(f"""
    			.:''':.           .            * * *        .::::.         '
    		   :__\ /__:	   __\(/__   . : .*__\/__*      ::::::      .  '  .
        . ' ' .:  / \.... 		 /)\     ' : '*  /\  *        ...      * \ * / *
       :__\ /__:' . :::::: .    | '            * * * '      *_\(/_* -= : = o = : =- 
       :  / \  :  : :::::: :    =      .******.    '.\./.'  *./)\.*    *:/ * \:*
    	' . . '     '::::'    =====   * __\/__ *  --= o =--   '''       '  '  '
    		  *                 |     *   /\   *   .'/.\.       *    ._____'___.
        Congratulations, {screen_name}. You won \033[1mFairweather Tourist\033[0m! 
        Your final score is: {total_score} points and you CO2 emission is: {CO2_emission} kg.
    			  *             |    .-' -|				   .---_..   |  .      |
    		------------        |    | '  |           __   |     |   |  |   ¤  |   .
    	  *	 ¤	¤  ¤  ¤  *		|    |  ¤ |   |  |   |  |_ |  ¤  | _ |         |   |
    _____'	¤  ¤  ¤  ¤	¤ '   / " \  |    |-. "  "   | ¤         |   |      ¤  |___|
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
else:
    print(f"\nUnfortunately {screen_name}, you have exceeded the maximum allowed value of CO2 emission, your final score is {total_score} with {CO2_emission} kg CO2 emission.")

sys.exit