"""
Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True 

with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, 

we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), 

which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() 

is done with its execution.

Here's a sample run of this program:

I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

"""

# 1
import random

DONE_LIKELIHOOD = 0.3  # 30% chance of stopping
# 1. DONE_LIKELIHOOD Variable
# Yeh ek constant (badalne wala nahi) hai jo represent karta hai ke program kitni jaldi ruk sakta hai.
# 0.3 ka matlab hai 30% chance hai ke program counting beech me hi stop kar dega.



def done():
    return random.random() < DONE_LIKELIHOOD
    # 2. done() Function
    # random.random() ek random number generate karta hai (0 aur 1 ke beech me).
    # Agar yeh 0.3 se chhota hota hai, to True return karega, warna False.
    # 30% chance hai ke yeh True hoga aur counting ruk jayegi.

def chaotic_counting():
    for i in range(1, 11):  # 1 se 10 tak count karna hai
        if done():  # Agar done() True return kare to counting stop kar do
            return
        print(i, end=" ")
        # 3. chaotic_counting() Function
        # Loop chal raha hai 1 se 10 tak.
        # Har iteration pe done() function check hota hai:
        # Agar done() True return kare (30% chance) → counting ruk jayegi.
        # Agar False ho to counting continue rahegi.
        # print(i, end=" ") ka matlab hai numbers ek line me print honge.

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")
    # 4. main() Function
    # Pehle ek message print hota hai.
    # Phir chaotic_counting() function ko call kiya jata hai.
    # Jab counting rukti hai, to "\nI'm done." print hota hai.

if __name__ == '__main__':
    main()
    # 5. if __name__ == '__main__':
    # Script jab direct run hogi, tabhi main() chalega.
    # Agar script import ho jaye, to main() function automatically execute nahi hoga.



# 2
def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return # this ends the function execution, so we'll get back to the main() function!
        print(curr_num)

# There is no need to edit code beyond this point

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()