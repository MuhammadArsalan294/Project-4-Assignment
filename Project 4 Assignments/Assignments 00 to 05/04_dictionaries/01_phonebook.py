"""
In this program we show an example of using dictionaries to keep track of information in a phonebook.

"""

# 1
def main():
    phonebook = {}  # Empty dictionary to store contacts
    # Yahaan phonebook ek dictionary hai jisme names (keys) aur phone numbers (values) store hote hain.

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        # Yeh menu options dikhata hai aur user se choice input leta hai.

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Contact {name} added successfully!")
        # User name aur phone number enter karta hai
        # Dictionary me store hota hai
        # Success message print hota hai

        elif choice == "2":
            name = input("Enter name to search: ")
            if name in phonebook:
                print(f"{name}'s number: {phonebook[name]}")
            else:
                print(f"Contact {name} not found!")
        # User name enter karta hai
        # Agar dictionary me hai to number print hota hai
        # Agar nahi mila to "not found" message show hota hai

        elif choice == "3":
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully!")
            else:
                print(f"Contact {name} not found!")
        # Agar name mil jaye to contact delete hota hai
        # Agar nahi mila to error message show hota hai

        elif choice == "4":
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty!")
        # Agar dictionary me contacts hain, to sab print honge
        # Agar empty hai, to "Phonebook is empty!" message show hoga

        elif choice == "5":
            print("Exiting Phonebook. Goodbye!")
            break
        # Agar user "5" choose kare to program band ho jaye
        else:
            print("Invalid choice! Please select a valid option.")
        # Agar user galat option dale to error message show ho
        
if __name__ == "__main__":
    main()




# 2
def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()