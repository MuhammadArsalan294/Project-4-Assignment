"""
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

(Note. The .0 after the 5 and 9 matters in the line above!!!)

Here's a sample run of the program (user input is in bold italics):

Enter temperature in Fahrenheit: 76

Temperature: 76.0F = 24.444444444444443C

"""

# 1
def main():
# Yeh main() function hai jo poora program execute karega. Isme temperature input lena, conversion karna, aur output print karna shamil hai.
    
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # input(...) user se temperature lene ke liye hai. float(...) ka use isliye kiya gaya hai taake decimal values (jese 98.6) bhi allow ho sakein.

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0 
    # Yeh standard Fahrenheit → Celsius conversion formula hai: Celsius = (Fahrenheit − 32) × 5.0/9.0      5.0/9.0 likhna zaroori hai taake result decimal (float) mein aaye.
   
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
    # f-string (f"...") ka use kiya gaya hai taake values string ke andar insert ho sakein.
    # {degrees_fahrenheit} aur {degrees_celsius} dynamically replace ho jaayenge.
   

if __name__ == '__main__':
    main()
# Yeh check karta hai agar script direct run ho rahi hai, tabhi main() function execute ho.