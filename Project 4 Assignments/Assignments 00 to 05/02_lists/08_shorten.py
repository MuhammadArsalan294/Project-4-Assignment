"""
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 

If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function

once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

"""


# 1
MAX_LENGTH = 3  # Required max length
# Yeh define karta hai ke maximum sirf 3 elements list mein reh sakte hain.

def shorten(lst):
    """List ko MAX_LENGTH tak chhota karega aur remove hone wale elements print karega."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Last element hatao
        print("Removing:", removed_item)
    # Yeh function list ko check karta hai.
    # Agar list ki length MAX_LENGTH se zyada ho, toh last element hata diya jata hai (pop()).
    # Har removed element ko print bhi karta hai.

# 🔹 Main function
def main():
    user_list = input("Enter elements separated by space: ").split()
    shorten(user_list)  # List ko shorten karna
    print("Final list:", user_list)  # Updated list print karna
    # User se input leta hai, jisme wo space-separate elements enter karega.
    # Yeh input ek list ban jata hai (split() ki wajah se).
    # shorten() function call karta hai, jo list ko MAX_LENGTH tak chhota karega.
    # Final list print karta hai.

if __name__ == "__main__":
    main()
    # Yeh ensure karta hai ke jab script run ho, toh main() function execute ho.



# 2
MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()