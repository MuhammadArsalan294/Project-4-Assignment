"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]

"""


# 1
def double_numbers(numbers):
    return [num * 2 for num in numbers]
    # Yeh function numbers naam ki list ko input leta hai.
    # num * 2 for num in numbers → Har number ka double karega aur ek nayi list banayega. 
    # Phir updated list return karega.

def main():
    numbers = [1, 2, 3, 4]
    # Input List → [1, 2, 3, 4] 

    numbers = double_numbers(numbers)  # Har element ko 2 se multiply karenge
    # num * 2 apply hoga
    # Nayi list return hogi → [2, 4, 6, 8]

    print(numbers)  # Output: [2, 4, 6, 8]
    #Print karega

if __name__ == '__main__':
    main()
    # Yeh line ensure karti hai ke jab script direct run ho, tab main() function execute ho.



# 2
def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2

    print(numbers)  # This should print the doubled list


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()