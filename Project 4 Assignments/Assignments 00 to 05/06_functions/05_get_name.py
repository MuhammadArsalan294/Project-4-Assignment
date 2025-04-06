"""
Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and 

then prints it in a greeting.

Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects the returned name to be Sophia):

Howdy Sophia ! 🤠

"""

# 1
def get_name():
    return "Sophia"
    # 1. get_name() Function
    # Yeh function kuch bhi input nahi leta.
    # Ek fixed naam "Sophia" return karta hai.
    # Agar tum chaaho, to is function ko modify karke user se naam input le sakte ho.

def main():
    name = get_name()
    print(f"Howdy {name} ! 🤠")
    # 2. main() Function
    # get_name() function call hota hai jo "Sophia" return karega.
    # Us naam ko ek formatted string (f-string) me Howdy ke saath print kiya jata hai.
    # Output me ek cowboy emoji 🤠 bhi add kiya gaya hai.

if __name__ == '__main__':
    main()
    # 3. if __name__ == '__main__':
    # Script jab direct run hogi, tabhi main() function chalega.
    # Agar script import ho jaye, to automatically execute nahi hogi.



# 2
def get_name():
    return "Sophia"

# There is no need to edit code beyond this point

def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()