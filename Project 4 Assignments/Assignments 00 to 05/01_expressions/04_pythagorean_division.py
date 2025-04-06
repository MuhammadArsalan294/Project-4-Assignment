"""
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

BC ** 2 = AB ** 2 + AC ** 2

Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

Here's a sample run of the program (user input is in bold italics):

Enter the length of AB: 3

Enter the length of AC: 4

The length of BC (the hypotenuse) is: 5.0

"""

# 1
import math 
# import math → math.sqrt() function use karne ke liye 

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    AB = float(input("Enter the length of AB: "))  
    AC = float(input("Enter the length of AC: "))  
    # User se dono perpendicular sides ka input lena
    #  User se AB aur AC ka input lena
 
    BC = math.sqrt(AB**2 + AC**2)  
    # Hypotenuse (BC) calculate karna
    # Formula BC = sqrt(AB² + AC²) lagana

    print(f"The length of BC (the hypotenuse) is: {BC}")
    # Result print karna
    # Formatted output print karna

if __name__ == '__main__':
    main()
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho




# 2
import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()