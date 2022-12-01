import sys
import mysql.connector
from geopy import distance


def distance_calculator(current_location, next_location):
    current_coordinate = []
    next_coordinate = []
    cursor1 = connection.cursor()
    cursor1.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + current_location + "'")
    current_icao = cursor1.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + next_location + "'")
    next_icao = cursor2.fetchall()
    for coordinate in current_icao:
        current_coordinate.append(coordinate)
    for coordinate in next_icao:
        next_coordinate.append(coordinate)
    distance_between_locations = round(distance.distance(tuple(current_coordinate), tuple(next_coordinate)).km, 2)
    return distance_between_locations


def emission_calculator(kilometers):
    additional_emission = round(kilometers * 0.156, 2)
    return additional_emission


def location_finder(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident='" + icao + "'")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport = row[1]
            municipality = row[2]
            print(f"\nCongratulations, you have arrived at {row[1]} located in {row[2]}.")
            return airport, municipality


def airport_printer(country):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT airport.ident, airport.name, airport.municipality, airport.iso_country, airport.type, "
        "country.iso_country, country.name, country.continent FROM airport, country "
        "WHERE airport.iso_country = country.iso_country AND country.name ='" + country + "' "
        "AND airport.type = '" + "large_airport" + "' AND country.continent = '" + "EU" + "'")
    result = cursor.fetchall()
    if cursor.rowcount < 0:
        print("None")
    else:
        for row in result:
            print(f"{row[1]} is located in {row[2]} and the ICAO code is {row[0]}.")
    return


def country_checker(country):
    country_list = ["Albania", "Andorra", "Armenia", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
                    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Faroe Island", "Finland",
                    "France", "Georgia", "Germany", "Gibraltar", "Greece", "Hungary", "Iceland", "Ireland",
                    "Isle of Man", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia",
                    "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal",
                    "Romania", "Russian Federation", "San Marino", "Serbia", "Slovakia", "Spain", "Sweden",
                    "Switzerland", "Turkey", "United Kingdom", "Vatican City State"]
    while country not in country_list:
        country = input("\nPlease enter a valid country: ")
    return country


def icao_checker(icao):
    icao_list = ["LATI", "UDYZ", "LOWW", "UMMS", "EBBR", "LBBG", "LBSF", "LBWN", "LDZA", "LCLK", "LKPR", "EKBI", "EKCH",
                 "EETN", "LFBD", "LFBO", "LFLL", "LFML", "LFMN", "LFPG", "LFPO", "LFSB", "BIKF", "UGTB", "LGAV",
                 "LGIR", "LGTS", "EIDW", "EINN", "EFHK", "EDDB", "EDDF", "EDDH", "EDDK", "EDDL", "EDDM", "EDDN", "EDDP",
                 "EDDS", "EDDV", "LHBP", "LICC", "LICJ", "LIEE", "LIMC", "LIME", "LIMF", "LIPE", "LIPX", "LIPZ", "LIRF",
                 "LIRN", "LIRN", "LIRP", "EVRA", "EYVI", "ELLX", "LWSK", "LMML", "LYPG", "EHAM", "EHEH", "ENBR", "ENGM",
                 "ENTC", "ENVA", "ENZV", "EPGD", "EPKK", "EPWA", "LPFR", "LPPD", "LPPR", "LPPT", "LROP", "RU-0016",
                 "RU-0035", "RU-4464", "UHWW", "ULLI", "UNKL", "UNNT", "URRP", "URSS", "USSS", "UUBW", "UUDD", "UUEE",
                 "UUWW", "UWSG", "UWUU", "UWWW", "LYBE", "LZIB", "GCFV", "GCLP", "GCRR", "GCTS", "LEAL", "LEBL", "LEIB",
                 "LEMD", "LEMG", "LEPA", "LEST", "ESGG", "ESSA", "LSGG", "LSZH", "LTAC", "LTAI", "LTBA", "LTBJ", "LTBS",
                 "LTFE", "LTFJ", "LTFM", "EGAA", "EGBB", "EGCC", "EGGW", "EGKK", "EGLL", "EGPF", "EGPH", "EGSS"]
    while icao not in icao_list:
        icao = input("\nPlease enter a valid ICAO code: ").upper()
    return icao


def rule_printer():
    print("""\nYou have had this bucket list for a while now and it's time to put things finally into motion!
    - You wish to visit 5 locations in Europe. (List appears soon.)
    - Before flying off to your first adventure, I ask you kindly to take into consideration sustainability 
      and plan to minimalize CO2 emission.
    - As a matter of fact I will be your conscience and not allow you to travel further if CO2 emission reaches 3,75 tonnes. 
\nThe scoring system works the following way:
    - You need to score 2500 points to win.
    - If you guess one of the location: +500 points
    - If you guess "Easter Egg" location: +800 points
    - If target score is not reached, but allowed CO2 emission exceeded, the game ends.""")
    return


def second_rule_printer():
    print('''
        - 5 locations need to be visited in Europe. (List appears soon.)
        - Protecting our planet is important so please minimalize CO2 emission.
        - Game ends if CO2 emission reaches 3,75 tonnes. 
        - In order to win, you need 2500 points.
        - If you guess one of the location: +500 points
        - If you guess "Easter Egg": +800 points
        - If target score is not reached, but allowed CO2 emission exceeded, the game ends.''')
    return


def goal_printer():
    print('''\nHere are the 5 locations:\n
    (1) "Fancying a Pint?”: learning that “bangers” do not necessarily mean something dirty"
    (2) “Waves of South”: surfing lessons for the fainthearted
    (3) “Charles' Eastern Comfort”: heavy food today, cholesterol tomorrow
    (4) “Fjordes and Riches”: old home of great sailor warriors and grand mountains
    (5) “We’re Going to Ibiza!”: does it need more explanation?
    (+1) "Easter Egg": “I was once called an old dame. In daylight I’m proudly wearing my scars of history, 
                       but when the night falls I put on my jewels to mesmerise you with my thousand sparks.”''')
    return


def country_code_printer():
    print("""\nHere are the European countries as help:
    Albania, Andorra, Armenia, Austria, Belarus, Belgium, Bosnia and Herzegovina, 
    Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Faroe Island, Finland, 
    France, Georgia, Germany, Gibraltar, Greece, Hungary, Iceland, Ireland, Isle of Man, 
    Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Macedonia, Malta, 
    Moldova, Monaco, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, 
    Russian Federation, San Marino, Serbia, Slovakia, Spain, Sweden, Switzerland, 
    Turkey, United Kingdom, Vatican City State.""")


def london_funfact():
    print(f'''\n{screen_name}, you arrived in London and you guessed the 1st location. Here is a fun fact as reward: 
        The guards of the tower of London are called “Meat Eaters”. 
        This is due to their historical role as the most important royal guards, 
        as they were promised a proper meal, containing meat, even if the rest of the nation had a food crisis.''')


def prague_funfact():
    print(f'''\n{screen_name}, you arrived in Prague and you guessed the 3rd location. Here is a fun fact as reward:
        This historical city is filled with many beautiful landmarks and traditional arts 
        like opera and theatre thrive here. Still the city has a modern side to this artistic talent, 
        as it makes numerous appearances in movies, mainly due to the city's major film studios.''')


def oslo_funfact():
    print(f'''\n{screen_name}, you arrived in Oslo and you guessed 4th location. Here is a fun fact as reward:
        Dublin was founded by the Vikings, who were first spotted off the coast of Ireland in AD 792. 
        In the 9th century, the Vikings invaded the region and established the Norse Kingdom of Dublin.''')


def ibiza_funfact():
    print(f'''\n{screen_name}, you arrived in Ibiza and you guessed the 5th location. Here is a fun fact as reward:
        This warm and beautiful mediterranean island, is known as a popular tourist destination, 
        with a highly active nightlife.''')


def caparica_funfact():
    print(f'''\n{screen_name}, you arrived in Caparica and you guessed the 2nd location. Here is a fun fact as reward:
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
    password='CamdenTown',
    autocommit=True
)

screen_name = input("Hello, please enter your name: ")
print(f"""\nWelcome {screen_name} to \033[1mFairweather Tourist\033[0m. It looks like you are currently in Helsinki, Finland.
Let me tell you a bit more about the game: """)

rule_printer()
answer_rules = input(f"\n{screen_name}, are the rules clear and are you ready to see the goals(yes/no)? ").lower()
while answer_rules != "yes":
    if answer_rules == "no":
        second_rule_printer()
        answer_rules = input("\nAre you ready now to see the goals(yes/no)? ").lower()
    else:
        answer_rules = input("\nInvalid input, are you ready to see the goals(yes/no)? ").lower()

goal_printer()
answer_first_location = input(
    f"\n{screen_name}, are the goals clear and are you ready to choose your first location(yes/no)? ").lower()
while answer_first_location != "yes":
    if answer_first_location == "no":
        goal_printer()
        answer_first_location = input("\nAre you now ready to choose your first location(yes/no)? ").lower()
    else:
        answer_first_location = input("\nInvalid input, are you ready to choose your first location(yes/no)? ").lower()

country_code_printer()
airports = {"EGKK": "London Gatwick Airport", "EGSS": "London Stansted Airport", "EGGW": "London Luton Airport",
            "EGLL": "London Heathrow Airport", "ENGM": "Oslo Airport",
            "LPPT": "Humberto Delgado Airport (Lisbon Portela)",
            "LKPR": "V?clav Havel Airport Prague", "LEIB": "Ibiza Airport"}
countries = ["United Kingdom", "Norway", "Portugal","Czech Republic", "Spain", "Hungary"]

total_score = CO2_emission = total_distance = 0
base_score = 500
bonus_score = 800
answer_list = ["EFHK"]
while total_score < 2500 and CO2_emission < 3750:
    # print(answer_list)
    country_input = input("\nEnter country: ")
    country_confirmed = country_checker(country_input)
    airport_printer(country_confirmed)
    ICAO_code_input = input("\nEnter ICAO code: ").upper()
    ICAO_confirmed = icao_checker(ICAO_code_input)
    if ICAO_confirmed in answer_list:
        print("\nYou have already visited that location, try another one!")
    else:
        answer_list.append(ICAO_confirmed)
        location_finder(ICAO_confirmed)
        current_location = answer_list[-2]
        odometer = distance_calculator(current_location, ICAO_confirmed)
        total_distance += odometer
        change_of_CO2 = emission_calculator(odometer)
        CO2_emission += change_of_CO2
        if ICAO_confirmed in airports:
            total_score += base_score
            if ICAO_confirmed == "LEIB":
                ibiza_funfact()
            elif ICAO_confirmed == "ENGM":
                oslo_funfact()
            elif ICAO_confirmed == "LPPT":
                caparica_funfact()
            elif ICAO_confirmed == "LKPR":
                prague_funfact()
            else:
                london_funfact()
                answer_list.append("EGKK")
                answer_list.append("EGSS")
                answer_list.append("EGGW")
                answer_list.append("EGLL")
        elif ICAO_confirmed == "LHBP":
            total_score += bonus_score
            budapest_funfact()
        elif ICAO_confirmed not in airports and country_confirmed in countries:
            print("\nUnfortunately, the airport is not right, but you guessed the country right!")
        else:
            print("\nUnfortunately, the location is not in this country, try another one!")
        print(f"Your current score is {total_score} points, CO2 emission is {CO2_emission:6.2f}kg and travelled distance is {total_distance:6.2f}km.")

if total_score >= 2500:
    print(f"""
    			.:''':.           .            * * *        .::::.         '    .*   .            . '  ' .   *\./*
    		   :__\ /__:	   __\(/__   . : .*__\/__*      ::::::      .  '  .   __\(/__        :__\ /__:   */'\*
        . ' ' .:  / \.... 		 /)\     ' : '*  /\  *        ...      * \ * / *    /)\   '*'    :  / \  :     .
       :__\ /__:' . :::::: .    | '            * * * '      *_\(/_* -= : = o = : =-  . '\*\./*./' ' . . '    .:::.
       :  / \  :  : :::::: :    =      .******.    '.\./.'  *./)\.*    *:/ * \:*    -=-=-= o =-=-=-   .***.  ':::'
    	' . . '     '::::'    =====   * __\/__ *  --= o =--   '''       '  '  '       ./.*/.\*.\.    *_\(/_*   '
    		  *                 |     *   /\   *   .'/.\.       *    ._____'___. .::.     '*'       :*./)\.*:
                        Congratulations, {screen_name}. You won \033[1mFairweather Tourist\033[0m! 
        Your final score is: {total_score} points, your CO2 emission is: {CO2_emission:6.2f}kg and distance is: {total_distance:6.2f}km.
    			  *             |    .-' -|				   .---_..   |  .      |                 *       .------.
    		------------        |    | '  |           __   |     |   |  |   ¤  |   ._____.  *   ***      | ¤  ¤ |
    	  *	 ¤	¤  ¤  ¤  *		|    |  ¤ |   |  |   |  |_ |  ¤  | _ |         |   |  ¤  | *** *****     | ¤  ¤ |
    _____'	¤  ¤  ¤  ¤	¤ '   / " \  |    |-. "  "   | ¤         |   |      ¤  |___|     |  |____|,,__,,_|      |__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
else:
    print(
        f"\nUnfortunately {screen_name}, you have exceeded the maximum allowed value of CO2 emission, "
        f"your final score is {total_score} with {CO2_emission:6.2f}kg CO2 emission and {total_distance:6.2f} km as travelled distance.")

sys.exit
