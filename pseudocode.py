import mysql.connector
import sys
import random


def randomizer():
    random.randrange(1, 1000000)  # replace with real numbers
    # use database position numbers choose the airport
    return ()


valid = 0

while valid != 1:
    start = input("Enter a starting airport: ")
    if start in airports:
        valid = 1
    else:
        print("Invalid input"), print("")

final = randomizer()

while start != final:
    confirm = "n"
    change = input("Enter airport to fly to")
    # check if name or other data entered is in database
    # if in print out airport info
    # if no, give error message and re-loop

    confirm = input("Are you sure (y/n)")
    if confirm == "y":
        start = change
    else:
        print("")

print("You have reached your destination.")
