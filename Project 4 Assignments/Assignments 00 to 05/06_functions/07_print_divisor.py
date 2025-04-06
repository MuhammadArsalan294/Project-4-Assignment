"""
Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be 

cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

Here's a sample run (user input is in blue):

Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

"""

# 1
def print_divisors(num):
    """Prints all divisors of the given number."""
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")  # Saath saath print karne ke liye end=" " use kiya
            # 1. print_divisors() Function
            # Yeh function ek number (num) leta hai aur us number ke sab divisors print karta hai.
            # for i in range(1, num + 1) loop 1 se lekar num tak har number check karta hai.
            # Agar num % i == 0 (i.e., num ko i se divide karte waqt remainder 0 ho), to i ek divisor hai aur woh print hota hai.
            # end=" " ka use isliye kiya gaya hai taake divisors ek hi line mein print ho, har ek ke baad ek space ho.

def main():
    num = int(input("Enter a number: "))  # User se number lena
    print(f"Here are the divisors of {num}")
    print_divisors(num)  # Function call karna
    # 2. main() Function
    # input() function user se ek number input leta hai.
    # print(f"Here are the divisors of {num}") statement user ko bataata hai ki program divisors print karega.
    # print_divisors(num) function call hota hai jo input number ke divisors print karta hai.

# Run the program
if __name__ == '__main__':
    main()




# 2
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()