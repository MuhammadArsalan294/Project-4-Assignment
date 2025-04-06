"""
We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's 

name and then greet them, being sure to call the greet(name) helper function.

Here's a sample run of the program (user input in bold italics):

What's your name? Sophia

Greetings Sophia!

"""
# 1
def greet(name):
    print(f"Greetings {name}!")
    # 1. greet(name) function:
    # Ye ek function hai jo ek name naam ka argument leta hai.
    # Jab function call hota hai, to ye name ko print karta hai.
    # Example: Agar aap greet("Arsalan") call karte hain, to output hoga: Greetings Arsalan!.
    
def main():
    name = input("What's your name? ")
    greet(name)
    # 2. main() function:
    # Ye main() function hai, jo program ka main part hai.
    # input("What's your name? ") se program user se unka naam maangta hai.
    # Phir greet(name) ko call karte hain aur user ka naam usse bhej dete hain, taake wo greeting print ho sake.

if __name__ == '__main__':
    main()
    # 3. if __name__ == '__main__': block:
    # Ye ensure karta hai ke main() function sirf tab execute ho jab aap script ko directly run kar rahe ho. Agar aap is file ko kisi aur program mein import karte hain, to main() function automatically execute nahi hoga.



# 2
def main():
    name : str = input("What's your name? ")
    print(greet(name))

# There is no need to edit code beyond this point

def greet(name):
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    main()
