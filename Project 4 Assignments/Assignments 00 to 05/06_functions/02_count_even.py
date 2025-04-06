"""
Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

"""

# 1
def main():
    """
    Prompts the user for integers until they press enter.
    Counts and prints the number of even numbers in the list.
    """
    numbers = []
    # 1. main() Function
    # numbers = [] ek empty list hai jo user ke input store karegi.
    # Yeh function user se numbers lega aur even numbers ka count karega.
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop when the user presses enter without input
        # 2. User Input Handling (Loop)
        # Infinite while True loop chalayega jab tak user manually enter na dabaye.
        # Agar user khaali enter dabaye ("") to break ho jayega aur loop ruk jayega.

        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            # 3. Input Validation (try-except)
            # try block me user ka input integer me convert karne ki koshish karta hai.
            # Agar conversion fail ho (e.g., user ne "abc" likha ho) to except ValueError block chalega aur error message print karega.
            # Agar input valid integer ho to numbers list me add ho jayega.
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    # 4. Even Numbers Count
    # Yeh ek Python generator expression hai jo list ke andar even numbers count karta hai.
    # num % 2 == 0 condition check karti hai ke number even hai ya nahi.
    # Agar even ho to sum(1 ...) uska count badhata hai.
    
    print("Number of even numbers:", even_count)
    # 5. Print the Result
    # Final result print karta hai ke kitne even numbers enter kiye gaye the.

# Run the function

if __name__ == '__main__':
    main()
    # 6. if __name__ == '__main__':
    # Script jab direct run hogi, tabhi main() chalega.
    # Agar script import ho jaye kisi aur file me, to main() function automatically execute nahi hoga.







# 2

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    # Here's another way to do this same thing, with a different kind of for-loop:
    # for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #         count += 1

    print(count)  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()