"""
Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

Here's a sample run (user input is in bold italics):

Please type an adjective and press enter. tiny

Please type a noun and press enter. plant

Please type a verb and press enter. fly

Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

"""

# 1
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
# Constant sentence start
# SENTENCE_START variable stores the fixed starting part of the sentence.

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    # Getting user inputs
    # input() function takes three words from the user

    mad_libs_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    # Creating the sentence
    # f-string is used to combine everything into a complete sentence.

    print(mad_libs_sentence)
    # Printing the fun sentence
    # print() function displays the final Mad Libs-style sentence.

if __name__ == '__main__':
    main()
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho.



# 2
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()