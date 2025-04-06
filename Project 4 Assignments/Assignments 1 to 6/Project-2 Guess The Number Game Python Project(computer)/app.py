import random

def guess_the_number():
    print("🎉 Welcome to the Guess the Number Game! 🎉")
    print("I have picked a number between 1 and 100.")
    print("Can you guess it?")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif user_guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"✅ Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
