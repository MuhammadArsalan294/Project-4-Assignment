import random

def hangman():
    words = ['python', 'programming', 'hangman', 'challenge', 'developer', 'terminal']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0 and '_' in guessed:
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("❌ Wrong guess.")
            attempts -= 1

    if '_' not in guessed:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
