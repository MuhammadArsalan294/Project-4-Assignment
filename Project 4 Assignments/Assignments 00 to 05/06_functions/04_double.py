"""
Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, 

calls your code for double(num) , and prints the result.

Here's a sample run of the program (user input in bold italics):

Enter a number: 2 Double that is 4

"""

# 1
def double(num):
    return num * 2
    # 1. double() Function
    # Yeh ek function hai jo ek argument (num) leta hai.
    # Us number ko 2 se multiply karke return karta hai.
    # Example: Agar num = 5 ho, to
    # 5×2=10
    # return karega.

def main():
    num = int(input("Enter a number: "))
    print(f"Double that is {double(num)}")
    # 2. main() Function
    # input() function user se number input lene ke liye use hota hai.
    # int() ka istemal is input ko integer me convert karne ke liye hota hai.
    # double(num) function call karta hai jo input ka double return karega.
    # Final output print karega using f-string (formatted string).

if __name__ == '__main__':
    main()
    # 3. if __name__ == '__main__':
    # Script jab direct run hogi, tabhi main() function execute hoga.\Agar script kisi aur file me import ho jaye, to automatically execute nahi hogi.


# 2
def double(num: int):
    return num * 2

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()