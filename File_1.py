import mysql.connector
import sys
import random

def randomizer():
    random.randrange(1, 1000000)  # replace with real numbers
    # use database position numbers choose the airport
    return ()


start = randomizer()
final = randomizer()

while start != final:
    confirm = "n"
    change = input("Enter airport to fly to")
    # check if name or other data entered is in database
    # if in print out airport info
    # if no re-loop

    confirm = input("Are you sure (y/n)")
    if confirm == "y":
        start = change
    else:
        print("")

print("You have reached your destination.")