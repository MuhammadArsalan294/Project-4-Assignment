"""
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. 

The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

"""

# 1
def get_first_element(lst):
    print("First element:", lst[0])  # Pehla element print karega
    # lst[0] list ka pehla element print karega.
    # List non-empty hone ki guarantee hai, to IndexError nahi aayega.

def main():
    user_list = input("Enter elements separated by space: ").split()
    # User se list input lena
    # input(...) user se ek hi line me elements leta hai.
    # .split() space ke basis par list me convert karta hai.
    # User ek hi line me elements likhega → "Apple Banana Cherry"
    # split() automatically list banayega → ["Apple", "Banana", "Cherry"]

    get_first_element(user_list)  # Function call
    # get_first_element(user_list) call hoga, jo first element print karega.
    # get_first_element(user_list) function list ka pehla element print karega.

if __name__ == '__main__':
    main()
    # Yeh line ensure karti hai ke jab script direct run ho, tab main() function execute ho.



# 2
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[0])

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()


   