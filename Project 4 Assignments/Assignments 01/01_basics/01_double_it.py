"""
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until 

the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128

Note that:

2 doubled is 4

4 doubled is 8

8 doubled is 16

and so on.

We stop at 128 because that value is greater than 100.

Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double 

the value of curr_value using a line like:

curr_value = curr_value * 2

This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

while curr_value < 100:
    
"""

# 1
def main():
    curr_value = int(input("Enter a number: "))  # User input
    # 1. User Input
    # User ek number enter karega.
    # int(input(...)): Input ko integer me convert karega.
    # Invalid input (e.g., "hello") dene par program crash ho sakta hai.

    
    while curr_value < 100: # Loop to double the value until it reaches 100 or more
    # 2. Doubling Loop
    # Jab tak curr_value 100 se chhota hai, loop chalega.
    # Jaise hi curr_value >= 100 hoga, loop band ho jayega.

        curr_value *= 2
        print(curr_value, end=" ")
        # 3. Doubling and Printing
        # curr_value *= 2: Har baar number 2 se multiply hoga.
        # print(curr_value, end=" "): Ek hi line me values print hongi (space ke saath).

if __name__ == "__main__":
    main()
