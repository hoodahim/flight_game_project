import requests
import math
import mysql.connector
from geopy import distance


def coordinate_fetcher(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao + "' ")
    result = cursor.fetchall()
    return result


def weather_fetcher(lat, lon):
    api = "628dc836c467279560786b9ec5b2a731"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    response = requests.get(url).json()
    temperature_celsius = response['main']['temp'] - 273.25            # converting it to celsius
    rounded_celsius = math.floor(temperature_celsius + 0.5)            # rounding
    return [response['weather'][0]['main'], rounded_celsius, response['wind']['speed']]


def distance_emission_calculator(current_location, next_location):
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
    distance_between_locations = round(distance.distance(tuple(current_coordinate), tuple(next_coordinate)).km)
    additional_emission = round(distance_between_locations * 0.156)
    return distance_between_locations, additional_emission


# database connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='CamdenTown',
    autocommit=True
)

# MAIN:
# base variables:
visited_locations = ['EFHK']                                                           # to append all LDN airports
order_of_visits = ['EFHK']                                                             # bc of LDN airport the previous would also be LDN, if all 4 is appended
london_airports = ['EGKK', 'EGSS', 'EGGW', 'EGLL']
score = co2_consumed = travelled_distance = 0
base_score = 500
location_score = 300
goal_sun = True
goal_rain = True
goal_cloud = True
goal_wind = True
goal_snow = True

# loop:
while score < 3000 and co2_consumed < 3500:
    now_location = order_of_visits[-1]
    new_location = input("Enter icao_code: ").upper()
    while new_location in visited_locations:                                           # no visit of the same
        new_location = input("Visited. Enter another icao_code: ").upper()

    if new_location in london_airports:                                                # handling the multiply airport of London
        visited_locations.append('EGKK')
        visited_locations.append('EGSS')
        visited_locations.append('EGGW')
        visited_locations.append('EGLL')
    else:
        visited_locations.append(new_location)

    order_of_visits.append(new_location)

    coordinate_of_next = coordinate_fetcher(new_location)
    current_weather = weather_fetcher(coordinate_of_next[0][0], coordinate_of_next[0][1])
    weather_condition, weather_temperature, weather_wind = current_weather
    print(current_weather)

    if new_location == "LHBP":                                                          # Budapest
        score += base_score * 2
        print(f"Easter Egg guessed: +{base_score*2}")
        print(f"New score: {score}")

    if new_location in london_airports or weather_condition == 'Rain' or weather_condition == 'Drizzle':                  # London & rain
        if new_location in london_airports and (weather_condition == 'Rain' or weather_condition == 'Drizzle'):
            if goal_rain:
                score += base_score * 2
                goal_rain = False
                print(f"London guessed and 'Rainy' goal reached: +{base_score*2}")
                print(f"New score: {score}")
            else:
                score += location_score
                print(f"London guessed, but 'Rainy' goal reached earlier: +{location_score}")
                print(f"New score: {score}")

        elif new_location in london_airports:
            score += location_score
            print(f"London guessed, but not the weather goal: +{location_score}")
            print(f"New score: {score}")

        else:
            if goal_rain:
                score += base_score
                goal_rain = False
                print(f"'Rainy' goal reached: +{base_score}")
                print(f"New score: {score}")

    if new_location == "LPPT" or weather_wind > 10:                                     # Caparica & wind
        if new_location == "LPPT" and weather_wind > 10:
            if goal_wind:
                score += base_score * 2
                goal_wind = False
                print(f"Caparica guessed and 'Windy' goal reached: +{base_score*2}")
                print(f"New score: {score}")
            else:
                score += location_score
                print(f"Caparica guessed, but 'Windy' goal reached earlier: +{location_score}")
                print(f"New score: {score}")

        elif new_location == "LPPT":
            score += location_score
            print(f"Caparica guessed, but not the weather goal: +{location_score}")
            print(f"New score: {score}")

        else:
            if goal_wind:
                score += base_score
                goal_wind = False
                print(f"'Windy' goal reached: +{base_score}")
                print(f"New score: {score}")

    if new_location == "LKPR" or weather_condition == 'Clouds':                        # Prague & clouds
        if new_location == "LKPR" and weather_condition == 'Clouds':
            if goal_cloud:
                score += base_score * 2
                goal_cloud = False
                print(f"Prague guessed and 'Clouds' goal reached: +{base_score*2}")
                print(f"New score: {score}")
            else:
                score += location_score
                print(f"Prague guessed, but 'Cloudy' goal reached earlier: +{location_score}")
                print(f"New score: {score}")

        elif new_location == "LKPR":
            score += location_score
            print(f"Prague guessed, but not the weather goal: +{location_score}")
            print(f"New score: {score}")

        else:
            if goal_cloud:
                score += base_score
                goal_cloud = False
                print(f"'Cloudy' goal reached: +{base_score}")
                print(f"New score: {score}")

    if new_location == "LEIB" or weather_temperature > 15:                          # Ibiza & sunny
        if new_location == "LEIB" and weather_temperature > 15:
            if goal_sun:
                score += base_score * 2
                goal_sun = False
                print(f"Ibiza guessed and 'Sunny' goal reached: +{base_score*2}")
                print(f"New score: {score}")
            else:
                score += location_score
                print(f"Ibiza guessed, but 'Sunny' goal reached earlier: +{location_score}")
                print(f"New score: {score}")

        elif new_location == "LEIB":
            score += location_score
            print(f"Ibiza guessed, but not the weather goal: +{location_score}")
            print(f"New score: {score}")

        else:
            if goal_sun:
                score += base_score
                goal_sun = False
                print(f"'Sunny' goal reached: +{base_score}")
                print(f"New score: {score}")

    if new_location == "BIKF" or weather_condition == 'Snow':                         # Reykjavik & snow
        if new_location == "BIKF" and weather_condition == 'Snow':
            if goal_snow:
                score += base_score * 2
                goal_snow = False
                print(f"Reykjavik guessed and 'Sunny' goal reached: +{base_score*2}")
                print(f"New score: {score}")
            else:
                score += location_score
                print(f"Reykjavik guessed, but 'Snows' goal reached earlier: +{location_score}")
                print(f"New score: {score}")

        elif new_location == "BIKF":
            score += location_score
            print(f"Reykjavik guessed, but not the weather goal: +{location_score}")
            print(f"New score: {score}")

        else:
            if goal_snow:
                score += base_score
                goal_snow = False
                print(f"'Snows' goal reached: +{base_score}")
                print(f"New score: {score}")

    distance_and_emission = distance_emission_calculator(now_location, new_location)
    travelled_distance += distance_and_emission[0]
    co2_consumed += distance_and_emission[1]
    print(f"Score is {score} points, CO2: {co2_consumed} kg, travelled so far: {travelled_distance}km.")


# out of the loop, outcome:
if score > 3000:
    print(f"You won :), score {score} points.")
else:
    print(f"Too much emission :(, {co2_consumed} kg.")
