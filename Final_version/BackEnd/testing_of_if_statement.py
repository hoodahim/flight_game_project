# testing of the if statement to see if does the right thing in all 8 possible variations

score = 0
base_score = 500
location_score = 300
london_airports = ['EGLL', 'EGGW', 'EGSS', 'EGKK']

new_location = 'LEIB'
weather_condition = 'Rain'
goal_rain = True

if new_location in london_airports or weather_condition == 'Rain':
    if new_location in london_airports and weather_condition == 'Rain':
        if goal_rain:                                       # EGLL, rain, True
            score += base_score * 2
            goal_rain = False
            print(f"both {score}")
            print(f"both {goal_rain}")
        else:                                               # EGLL, rain, False
            score += location_score
            print(f"only location bc goal rain false {score}")
            print(f"only location bc goal rain false {goal_rain}")

    elif new_location in london_airports:                   # EGLL, clouds, True or False
        score += location_score
        print(f"only location {score}")
        print(f"only location {goal_rain}")

    else:
        if goal_rain:                                       # LEIB, Rain, True
            score += base_score
            goal_rain = False
            print(f"only weather{score}")
            print(f"only weather{goal_rain}")

