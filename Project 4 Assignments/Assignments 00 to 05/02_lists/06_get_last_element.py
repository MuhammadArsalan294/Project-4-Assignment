"""
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty,

but there are no guarantees on its length.
"""


# 1
def get_last_element(lst):
    print("Last element:", lst[-1])  # Last element print karega

def main():
    user_list = input("Enter elements separated by space: ").split()
    # 🔹 User se list input lena
    # User ek hi line me elements enter karega
    # Example: "Apple Banana Cherry Mango"
    # .split() ka use hoke list banegi
    # Output: ['Apple', 'Banana', 'Cherry', 'Mango']

    get_last_element(user_list)  # Function call
    # Function lst[-1] se last element print karega
    # Output: "Last element: Mango" 

if __name__ == '__main__':
    main()
    # Yeh line ensure karti hai ke jab script direct run ho, tab main() function execute ho.



# 2
def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[-1])  # List ka last element print karega

def get_lst():
    """Prompts the user to enter one element at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    
    return lst

def main():
    lst = get_lst()  # User se list lena
    get_last_element(lst)  # Last element print karna

if __name__ == "__main__":
    main()
