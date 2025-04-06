"""
Write a function that takes a list of numbers and returns the sum of those numbers.
"""

# 1
def sum_of_numbers(numbers):
    return sum(numbers)  # Yeh sum() function list ke tamam numbers ka sum karega.
    # sum_of_numbers(numbers) ek function hai jo ek list ko input leta hai. 
    # sum(numbers) ek built-in function hai jo list ke tamam elements ka sum calculate karta hai.
    # Phir ye function calculated sum ko return karta hai.

def main():
    numbers_list = [1, 2, 3, 4, 5]  # Ek list jisme numbers hain
    # numbers_list = [1, 2, 3, 4, 5] → Humne ek list banayi.

    result = sum_of_numbers(numbers_list)  # Function ko call kar rahe hain
    # sum_of_numbers(numbers_list) → Is function ko call kiya jo list ke numbers ka sum karega.
    # sum([1, 2, 3, 4, 5]) → sum() function kaam karega aur 1+2+3+4+5 = 15 return karega.

    print(result)  # Output: 15
    # print(result) → Ye 15 print karega.

if __name__ == '__main__':
    main()
    # Yeh line ensure karti hai ke jab script direct run ho, tab main() function execute ho.


# 2 
def add_many_numbers(numbers)-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()