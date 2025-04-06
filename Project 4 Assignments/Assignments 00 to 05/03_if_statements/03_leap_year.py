"""
Write a program that reads a year from the user and tells whether a given year is a leap year or not.

A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar,

a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days 

instead of 365, by extending February to 29 days rather than the common 28.

In the Gregorian calendar, three criteria must be checked to identify leap years:

1. The given year must be evenly divisible by 4;
2. If the year can also be evenly divided by 100, it is NOT a leap year; unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."

"""

# 1
def is_leap_year(year):
    """Yeh function check karega ke diya gaya year leap year hai ya nahi."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    # Yeh function 3 conditions check karta hai:
    # Agar ek saal 4 se divisible hai aur 100 se nahi hai, toh Leap Year hoga
    # Agar ek saal 400 se divisible hai, tab bhi Leap Year hoga.
    # Agar yeh conditions nahi milti toh saal Leap Year nahi hoga.

def main():
    try:
        year = int(input("Enter a year: "))  # User se input lena
        if is_leap_year(year):
            print("That's a leap year! 🎉")
        else:
            print("That's not a leap year. ❌")
    except ValueError:
        print("Invalid input! Please enter a valid year.")  # Agar user ne galat input diya toh
    # User se ek year input liya aur is_leap_year(year) function call kiya.
    # Agar function True return kare toh "That's a leap year!" print hoga.
    # Agar False return kare toh "That's not a leap year." print hoga.
    # Agar user ne number ke ilawa koi aur cheez likhi (e.g., abc ya hello), toh program crash na ho.
    # Instead, yeh error handle karega aur "Invalid input! Please enter a valid year." message dega.

if __name__ == '__main__':
    main()
    # Yeh ensure karega ke jab script direct run ho, tab main() function execute ho.



# 2 
def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                print("That's a leap year!")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()