""""
Problem Statement
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

1. Prompt the user to enter the first number.

2. Read the input and convert it to an integer.

3. Prompt the user to enter the second number.

4. Read the input and convert it to an integer.

5. Calculate the sum of the two numbers.

6. Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering 

two numbers and displays their sum.

"""

# 1
def main():
# Prompt the user to enter the first number
# Yahan main() function define kiya gaya hai jo poore program ka kaam sambhalega.
    
    print("This program adds two numbers.")
    # ye print ho kar aye ga 

    num1 = int(input("Enter the first number: "))  
    # input("Enter the first number: ") Yeh user se input lene ke liye hai. User jo bhi type karega, woh ek string (text) hoti hai.
    # int(...)Yeh input ko integer (poora number) banane ke liye use hota hai.Agar user koi galat value enter kare (jaise abc ya 12.5), toh program error de sakta hai. (Iska solution neeche bataya gaya hai.)

 
    num2 = int(input("Enter the second number: "))
    # Prompt the user to enter the second number
    # Yeh bhi wahi kaam karega jo num1 ke liye kiya tha, sirf doosra number lene ke liye.

    
    total = num1 + num2  
    # Calculate the sum
    # Yeh dono numbers ka sum calculate karega aur total variable mein store karega.

   
    print(f"The sum of {num1} and {num2} is: {total}")
    # Display the result
    # Yeh f-string ka use karke result print karega. {num1}, {num2}, aur {total} values ko string ke andar embed kar dete hain.


if __name__ == "__main__":
    main()
# Call the main function
# Yeh check karta hai ki agar yeh script direct run ho rahi hai toh main() function execute ho.Ye Python ke standard practices mein se ek hai.


#2
"""
Program: add2numbers
--------------------
Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.

"""

def main():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()