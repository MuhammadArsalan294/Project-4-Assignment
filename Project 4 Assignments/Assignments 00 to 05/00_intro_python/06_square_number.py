"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0

"""

# 1 
def main():
    
    num = float(input("Type a number to see its square: "))
    # User se input lena
    # input() function user se number input lene ke liye use hota hai. float() ka use decimal numbers allow karne ke liye kiya gaya hai.
   
    square = num * num
    # Square calculate karna
    # Formula: square = number × number
    
    print(f"{num} squared is {square}")
    # Output print karna
    # f-string ka use kiya gaya hai taake output formatted ho.


if __name__ == "__main__":
    main()
# Program run karna
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho.




# 2 
def main():
    num: float = float(input("Type a number to see its square: ")) # Make sure to cast the input to a float so we can do math with it!
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

