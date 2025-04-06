"""
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
Anton is 3

Beth is 4

Chen is 5

Drew is 6

Ethan is 7
"""
# 1
def main():  # 1️⃣ Function define kar raha hai
    # Age calculations
    Anton = 21   # 2️⃣ Anton ki age directly given hai
    Beth = Anton + 6   # 3️⃣ Beth Anton se 6 saal bada hai
    Chen = Beth + 20   # 4️⃣ Chen Beth se 20 saal bada hai
    Drew = Chen + Anton   # 5️⃣ Drew ki age = Chen + Anton
    Ethan = Chen   # 6️⃣ Ethan ki age = Chen ke barabar

    # Printing the output
    print(f"Anton is {Anton}")  # 7️⃣ Sabki ages print kar raha hai
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")

# Running the program
if __name__ == "__main__":  # 8️⃣ Program execute karne ka standard tarika
    main()


# 2
def main():
    anton : int = 21  # Anton's age is given as 21 years old
    beth : int = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew  : int= chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan : int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()