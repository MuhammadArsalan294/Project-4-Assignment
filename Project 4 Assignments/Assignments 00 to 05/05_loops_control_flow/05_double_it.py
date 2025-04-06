"""
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. 

It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128

Note that:

2 doubled is 4

4 doubled is 8

8 doubled is 16

and so on.

We stop at 128 because that value is greater than 100.

Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. 

Recall that you can double the value of curr_value using a line like:

curr_value = curr_value * 2

This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

while curr_value < 100:

"""


# 1
def main():
    num = int(input("Enter a number: "))  # User se input lena
    # User se ek number lena aur integer me convert karna.

    while num < 100:  # Jab tak value 100 se choti hai, loop chalay ga
    # Loop tab tak chalega jab tak num 100 se choti ho.

        print(num, end=" ")  # Print karna
        # Ek hi line me output show karna (end=" " ka use kiya).

        num *= 2  # Value ko double karna
        # Har iteration me value ko double karna.
    
    print(num)  # Akhri value ko print karna jo 100 se zyada ho gayi
    # Jab loop khatam ho jaye, to final value print karni hai (jo 100 ya usse zyada ho chuki hogi).

if __name__ == '__main__':     
    main()  # Function call karna 






    

