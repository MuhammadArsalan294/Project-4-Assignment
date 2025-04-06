"""
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5

"""

# 1
def main():
    # User se inputs lena
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    # input() ka use kiya gaya hai taake user side ki length enter kare. float() ka use kiya gaya hai taake decimal values bhi accept ho sakein.

    perimeter = side1 + side2 + side3 
    # Perimeter calculate karna
    # Formula: perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is {perimeter}")
    # Output print karna
    # f-string ka use kiya gaya hai taake value proper format mein print ho.

if __name__ == "__main__":
    main()
# Program run karna
# Ensure karta hai ke jab program run ho toh main() function execute ho. 
# Agar code kisi aur script mein import ho toh yeh main() function automatically execute nahi hoga.




# 2 
def main():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()


    