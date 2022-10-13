mean_of_transportation = input("""
Now let's choose your mean of transportation. 
You can either travel with helicopter by entering A
or enter B, if you'd rather fly an airplane. 
Your preference: """).upper()

while mean_of_transportation != "A" and mean_of_transportation != "B":
    mean_of_transportation = input("Please answer with a valid letter. ").upper()

if mean_of_transportation == "A":
    specification = input("""
    There are two types of helicopters: normal (xxx CO2 emission, yyy range)
    and electronic helicopter (xxx CO2 emission, yyy range).
    Please choose either the normal by entering C or the electronic by entering D.
    Your preference: """).upper()
    while specification != "C" and specification != "D":
        specification = input("Please answer with a valid letter. ").upper()
    if specification == "C":
        print("You chose the normal helicopter.")
    elif specification == "D":
        print("You chose the electronic helicopter.")

elif mean_of_transportation == "B":
    specification = input("""
    There are two types of airplanes: normal (xxx CO2 emission, yyy range)
    and electronic airport (xxx CO2 emission, yyy range).
    Please choose either the normal by entering E or the electronic by entering F.
    Your preference: """).upper()
    while specification != "E" and specification != "F":
        specification = input("Please answer with a valid letter. ").upper()
    if specification == "E":
        print("You chose the normal airplane.")
    elif specification == "F":
        print("You chose the electronic airplane.")
