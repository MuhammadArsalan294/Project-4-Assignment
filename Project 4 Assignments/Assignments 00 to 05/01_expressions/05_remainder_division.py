"""

Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2

"""

# 1 
def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    num1 = int(input("Please enter an integer to be divided: "))  
    # User se pehla number lena (dividend)
    # int(input()) → User se integer values input lene ke liye

    num2 = int(input("Please enter an integer to divide by: "))  
    # User se doosra number lena (divisor)

    quotient = num1 // num2 
    # // (floor division) → Quotient (bina decimal ka result) nikalne ke liye 
 
    remainder = num1 % num2  
   # Division ka result aur remainder calculate karna
   #  % (modulus operator) → Remainder nikalne ke liye

    print(f"The result of this division is {quotient} with a remainder of {remainder}")
    # Result print karna
    # Formatted output (f"") → Clear aur readable output ke liye

if __name__ == '__main__':
    main()
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho.



# 2
def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
