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
# random module import karte hain jo random numbers generate karne ke liye use hota hai.

def main():
    secret_number = random.randint(1, 99)  # 1 se 99 tak random number generate karo
    print("I am thinking of a number between 1 and 99...")
    # secret_number = random.randint(1, 99)
    # Yeh ek random number generate karta hai jo 1 se 99 ke beech hoga.
    # print() statement
    # User ko batata hai ke ek number socha gaya hai, jo usko guess karna hai.

    while True:
        try:
            guess = int(input("Enter a guess: "))  # User input
            # while True:
            # Yeh loop tab tak chalta rahega jab tak user sahi number guess nahi kar leta.
            # try:
            # Yeh error handling ke liye hai. Agar user number ke bajaye koi aur cheez (e.g., text) likhta hai to program crash nahi hoga.
            # int(input("Enter a guess: "))
            # Yeh user se number input leta hai aur integer me convert karta hai.
            
            if guess < 1 or guess > 99:
                print("Please enter a number between 1 and 99.")
                continue  # Invalid input, dobara input lo
                #  Agar user 1 se chhota ya 99 se bada number likhe, to program usko dobara puchhega.

            if guess < secret_number:
                print("Your guess is too low\n")
            elif guess > secret_number:
                print("Your guess is too high\n")
                # Agar user ka guess chhota ho → "Your guess is too low"
                # Agar user ka guess bada ho → "Your guess is too high"
                # Agar guess barabar ho to next step chalay ga

            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break  # Sahi guess hone par loop exit
                # Agar guess sahi ho to
                # Program user ko mubarakbad deta hai 🎉
                # Loop exit ho jata hai (break) aur game khatam ho jata hai.

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            # Agar user koi ghalat input dale (jaise abc, hello), to
            # Program crash nahi hoga
            # Balki user ko message dega ke "Invalid input! Please enter a valid number."
            # Loop wapis chalega aur user se dobara number pucha jayega

if __name__ == '__main__':
    main()
    # Yeh line Python ka standard tareeqa hai ensure karne ka ke jab script run ho to main() function execute ho.




# 2
import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
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
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()