import random

def guess_the_number():
    print("🎉 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set number of attempts
    attempts = 10
    
    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Take a guess: "))
        except ValueError:
            print("⛔ Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Your guess must be between 1 and 100.")
            continue
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
            break
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
        
        attempts -= 1

    if attempts == 0:
        print(f"\n😢 Game Over! The number was {secret_number}.")

# Run the game
guess_the_number()
