"""
Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") 

until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, 

capable, and strong; this little Python program may be able to help!

Here's a sample run of the program (user input is in blue):

Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: 

I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!

"""

# 1
def main():
    affirmation = "I am capable of doing anything I put my mind to." 
    # Sahi answer store kiya gaya hai taake user ka input match kiya ja sake. 
    
    while True:
    # Yeh infinite loop hai jo tab tak chalega jab tak user sahi jawab nahi deta.

        user_input = input("Please type the following affirmation: \n" + affirmation + "\n")
        # User ko prompt diya jata hai taake wo affirmation likhe.
        
        if user_input == affirmation:
            print("That's right! :)")
            break  # Loop ko end karna
            # Agar user ka input sahi hai, to "That's right! :)" print hoga aur loop break ho jaye ga.

        else:
            print("Hmmm, that was not the affirmation. Try again!")
            # Agar user galat likhta hai, to "Hmmm, that was not the affirmation. Try again!" message milega aur loop dobara chalega.

if __name__ == '__main__':
    main()  # Function call karna





# 2
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()