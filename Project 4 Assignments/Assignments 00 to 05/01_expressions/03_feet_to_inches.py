"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

"""

# 1
INCHES_PER_FOOT = 12  
# Ek foot mein 12 inches hote hain

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    feet = float(input("Enter length in feet: "))
    # User se feet input lena

    inches = feet * INCHES_PER_FOOT  
    # Feet ko inches mein convert karna

    print(f"{feet} feet is equal to {inches} inches.")
    # Output print karna

if __name__ == '__main__':
    main()
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho



# 2
"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
