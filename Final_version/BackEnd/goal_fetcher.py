# Fetches the goal table.

import mysql.connector
import json


def goal_fetcher():
    list_of_goals = []
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, description, icon, target, target_minvalue, target_maxvalue, target_text FROM goal ")
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for row in result:
            goal = {
                "goalID": row[0],
                "name": row[1],
                "description": row[2],
                "icon": row[3],
                "reached": False,
                "target": row[4],
                "target_minvalue": row[5],
                "target_maxvalue": row[6],
                "target_text": row[7],
            }
            json.dumps(goal, default=lambda o: o.__dict__, indent=4)
            list_of_goals.append(goal)
    print(list_of_goals)
    return list_of_goals


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='CamdenTown',
         autocommit=True
         )

array_of_goals = goal_fetcher()
