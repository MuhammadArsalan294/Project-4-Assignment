"""
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48

"""

# 1
import random
# 1. Importing Required Module
#  random module use kiya gaya hai taake ek random number generate kar sakein.

def main():
    secret_number = random.randint(0, 99) # Random number generate karein (0 se 99 ke darmiyan)
    # 2. Generating a Secret Number
    #  random.randint(0, 99): Ek random number 0 se 99 ke darmiyan choose karega.

    print("I am thinking of a number between 0 and 99...")
    # 3. Printing Instructions
    #  User ko bataya jayega ke ek number guess karna hai jo 0 aur 99 ke beech hai.
    
    guess = int(input("Enter a guess: ")) # User se pehli guess lein
    # 4. Taking the First Guess
    # User se ek number input liya jata hai.
    # int(input(...)): Input ko integer me convert kiya jata hai.
    # Agar user koi invalid input de (jaise "hello"), to program crash ho sakta hai. Isko handle karne ke liye try-except ka use kar sakte hain.
    
    while guess != secret_number: # Jab tak user sahi number guess na kare, loop chalay
    # 5. Loop to Keep Asking Until the Correct Guess
    #  Jab tak user ka guess sahi nahi hota, loop chalta rahega.

        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
            # 6. Giving Hints
            # Agar guess zyada ho to "Your guess is too high" print hoga.
            # Agar guess kam ho to "Your guess is too low" print hoga.
        
       
        guess = int(input("Enter a new number: "))  # Naya number guess karne ko kahe
        # 7. Taking a New Guess
        #  User se dubara naya number manga jayega jab tak sahi na ho.

    print(f"Congrats! The number was: {secret_number}")   # Sahi guess par message dikhaye
    # 8. Congratulating the User
    # Jab user sahi number guess kar lega, usko "Congrats!" wala message milega.

if __name__ == "__main__":
    main()




# 2
import random

def main():
    # Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        if guess < secret_number:  # If-statement is True if guess is less than secret number
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() # Print an empty line to tidy up the console for new guesses
        guess: int = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()
