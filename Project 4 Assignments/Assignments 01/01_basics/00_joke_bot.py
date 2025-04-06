"""
Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. 

Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

If the user enters anything else we print out:

Sorry I only tell jokes

You should use the three constants:

PROMPT JOKE SORRY

which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

Your program will need to use an if statement which checks if the user input is Joke:

if user_input == "Joke":

Recall that == is a comparison which tests if two values are equal to one another.

Here is a full run of the program (user input is in blue):

What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, 

and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

"""


# 1
import random
# 1. Importing Required Module
#  random module ka use kiya gaya hai random joke select karne ke liye.

PROMPT = "What do you want? "
JOKES = [
    "Here is a joke for you!\nPanaversity GPT - Sophia is heading out to the grocery store.\nA programmer tells her: get a liter of milk, and if they have eggs, get 12.\nSophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'",
    "Why do programmers prefer dark mode?\nBecause light attracts bugs!",
    "Why do Java developers wear glasses?\nBecause they don't C#!",
    "There are 10 types of people in the world: Those who understand binary and those who don’t."
]
SORRY = "Sorry, I only tell jokes."
# 2. Constants
# JOKES ek list hai jo randomly select hone wale jokes contain karti hai.
# SORRY message tab show hoga jab user "joke" ya "exit" ke ilawa kuch likhe.

def main():
# 3. Main Function
#  main() function program ka logic execute karta hai.
    while True:
    # 4. Infinite Loop for User Input
    # Loop tab tak chalta rahega jab tak user "exit" na likhe.

        user_input = input(PROMPT).strip().lower()
        # 5. Taking User Input and Handling Cases
        #input(PROMPT): User se input leta hai.
        # .strip().lower():
        # .strip() extra spaces hata deta hai (taake " joke " bhi work kare).
        # .lower() capital letters ko chhoti letters me convert karta hai ("JOKE", "Joke" etc. sab valid honge).
        
        if user_input == "joke":
            print(random.choice(JOKES))
            # 6. Checking User Input
            # Agar "joke" likha gaya ho to ek random joke print hoga.
            # random.choice(JOKES): JOKES list se ek random item select karega.

        elif user_input == "exit":
            print("Goodbye!")
            break
            # 7. Exit Condition
            #  Agar user "exit" likhta hai, to program "Goodbye!" print karega aur loop band ho jayega (break ka use kiya hai).

        else:
            print(SORRY)
            # 8. Invalid Input Handling
            #  Agar user "joke" ya "exit" ke ilawa kuch bhi likhta hai, to "Sorry, I only tell jokes." print hoga.

if __name__ == "__main__":
    main()



# 2
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
  
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
    