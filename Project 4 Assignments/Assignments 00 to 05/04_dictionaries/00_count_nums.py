"""
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

"""


def main():
    counts = {}  # Dictionary to store frequency of numbers
    # Dictionary ek aisi data structure hai jo key-value pairs store karti hai.
    # Yahaan keys numbers hain, aur values unki frequency.

    while True:
        num = input("Enter a number (or press Enter to stop): ")
        if num == "":  # Stop when user presses Enter without input
            break
        # while True ka matlab hai ke loop tab tak chalega jab tak hum manually stop na karein.
        # Agar user sirf Enter dabata hai bina koi number diye, to loop break ho jata hai.
        try:
            num = int(num)  # Convert input to integer
            counts[num] = counts.get(num, 0) + 1  # Update frequency
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        # int(num) se input integer me convert hota hai.
        # counts.get(num, 0) + 1 ka matlab hai:
        # Agar number pehle se hai to uska count +1 kar do.
        # Agar pehli baar aaya to uska count 1 rakho.
        # Agar user number ke ilawa koi galt cheez likhe (abc, 5.6, etc.), to error show hoga.

    # Display the frequency of each number in sorted order
    print("\nNumber Frequency:")
    for num in sorted(counts.keys()):
        print(f"{num} appears {counts[num]} times.")
    # sorted(counts.keys()) dictionary ke keys ko chhote se bade order me sort karta hai.
    # for loop har number ka count print karta hai.

if __name__ == "__main__":
    main()





# 2
def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()