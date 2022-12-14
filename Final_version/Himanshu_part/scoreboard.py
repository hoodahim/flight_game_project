import requests
import config
import os

from dotenv import load_dotenv
load_dotenv()

class Scoreboard:
    def __init__(self, game):
        goals_reached = []
        for goals in game.goals:
            if goals.reached == True:
                goals_reached.append(goals.goalid)

    def goal_check(self):


