"""
Simulate rolling two dice, and prints results of each roll as well as the total.

"""

# 1
import random
# Yeh random module ko import karta hai jo random numbers generate karne ke liye use hota hai.

NUM_SIDES: int = 6
# NUM_SIDES ek constant variable hai jo bata raha hai ke har dice ke 6 sides hain (1 se 6 tak).

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Yeh random.randint(1, 6) ka use karke do dice ka random number generate karta hai.

    total = die1 + die2
    # Yeh die1 aur die2 ko add karta hai total sum nikalne ke liye.

    print("Dice have", NUM_SIDES, "sides each.")
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")
    # Pehli line bata rahi hai ke dice ke 6 sides hain.
    # Dusri line die1, die2, aur total ki random values print karegi.

if __name__ == '__main__':
    main()
# Yeh program ko execute karne ka standard tarika hai. Jab aap is file ko run karenge, to main() function call ho jayega.



# 2
"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

