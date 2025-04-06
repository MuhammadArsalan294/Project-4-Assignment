"""
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, 

should be helpful to you here. Call your function from main()!

Here's a sample run (user input is in blue):

Enter a number: 42 The ones digit is 2

"""


# 1
def print_ones_digit(num):
    print("The ones digit is", abs(num) % 10)
    # 1. print_ones_digit(num) Function
    # num ek integer hai jo function accept karega.
    # abs(num) ka use isliye kiya gaya hai taake agar number negative ho tab bhi correct
    # num % 10 ka use kiya gaya hai taake ones digit (akhri digit) mil sake.
    # Print statement output show karega.

def main():
    print_ones_digit(int(input("Enter a number: ")))
    # 2. main() Function
    # User se ek number input liya jata hai.
    # int(input(...)) se ensure kiya gaya hai ke input number format me ho.
    # Us number ko print_ones_digit() function me bhej diya jata hai.

if __name__ == "__main__":
    main()
    # 3. if __name__ == "__main__":
    # Jab script run hogi, tab main() function execute hoga.
    # Agar script kisi aur module me import ho, to yeh code automatically execute nahi hoga.






# 2 

def print_ones_digit(num): 
    print("The ones digit is", num % 10)

def main(): 
    num = int(input("Enter a number: ")) 
    print_ones_digit(num)

# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()


