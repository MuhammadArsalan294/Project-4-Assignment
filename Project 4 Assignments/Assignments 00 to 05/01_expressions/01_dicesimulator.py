"""
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

"""
# 1
import random  # Random numbers generate karne ke liye
# Python ka random module use kiya gaya hai random numbers generate karne ke liye.

def roll_dice():
    return random.randint(1, 6)  # 1 se 6 ke beech ka random number return karega
# randint(1, 6) ek random number generate karega jo 1 se 6 tak hoga (jaise ek asli dice).
# Function return karega ek random dice value.

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    for i in range(3):  # Loop chalega 3 times (3 rolls)
    # Loop 3 times chalega (0, 1, 2) yani 3 rolls honge.

        die1 = roll_dice()  # Pehla dice roll karna
        die2 = roll_dice()  # Dusra dice roll karna
        # 2 dice roll ho rahe hain, har ek roll_dice() function se random value le raha hai.

        print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}")
        # i+1 ka use ho raha hai taake roll counting 1 se start ho (1, 2, 3).

# Program run karna
if __name__ == "__main__":
    main()
# Ensure karta hai ke jab program run ho, toh main() function execute ho.




#2
"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""



import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


