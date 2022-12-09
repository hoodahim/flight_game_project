import mysql.connector
import random


class Player:
    existing_id = []

    def __init__(self, screen_name, current_location='EFHK', c02_consumed=0, co2_budget=3500, score=0):
        self.screen_name = screen_name
        self.current_location = current_location
        self.id = random.randint(100000, 999999)
        while self.id in Player.existing_id:
            self.id = random.randint(100000, 999999)
        Player.existing_id.append(self.id)
        self.c02_consumed = c02_consumed
        self.co2_budget = co2_budget
        self.score = score

    def player_add(self):
        cursor = connection.cursor()
        sql_add = "INSERT INTO game VALUES (" + str(self.id) + ", " + str(self.c02_consumed) + ", " + str(self.co2_budget) + ", '" + self.current_location + "', '" + self.screen_name + "', " + str(self.score) + ")"
        cursor.execute(sql_add)

    def player_update(self, consumption, gained_score, new_location):
        self.c02_consumed += consumption
        self.co2_budget -= consumption
        self.score += gained_score
        cursor = connection.cursor()
        sql_update = "UPDATE Game SET co2_consumed = " + str(self.c02_consumed) + ", co2_budget = " + str(self.co2_budget) + ", location = '" + new_location + "', score = " + str(self.score) + ""
        cursor.execute(sql_update)

    def player_fetch(self, name):
        cursor = connection.cursor()
        sql_fetch = "SELECT id, co2_consumed, co2_budget, location, screen_name FROM game WHERE screen_name = '" + name + "'"
        cursor.execute(sql_fetch)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                print(row)


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='CamdenTown',
    autocommit=True
)
