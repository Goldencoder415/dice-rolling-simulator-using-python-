import random
dicesides = int(input("Enter the number of sides on the dice: "))
roll = random.randint(1, dicesides)
print("You rolled a", roll)
input("Press Enter to exit...")