"""
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

"""

# 1
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
# Constants
# Constants ka matlab yeh hai ke yeh values program mein change nahi hoti.
# 🔹 Hum ek saal ke total seconds calculate karne ke liye ye values use karenge:

def main():
# Yeh ek function define karta hai jo program ka main logic handle karega.

    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    # Calculation
    # 🔹 Yahaan hum multiply kar rahe hain:

    print(f"There are {seconds_in_year} seconds in a year!")
    # Output
    # 🔹 f-string ka istemal kiya gaya hai taake variable ka value statement ke andar asani se likh sakein.

if __name__ == '__main__':
    main()
# Yeh ensure karta hai ke jab program run ho, toh main() function execute ho.



# 2 
# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # We can get the number of seconds per year by multiplying the handy constants above!
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()