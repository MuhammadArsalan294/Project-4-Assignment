"""
Problem #2: Index Game
As a warmup, read this code and play the game a few times. Use this mental model of the list:

Objective:
Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, 
and modifying list elements.

Instructions:
Initialize a List:
Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

Accessing Elements:
Write a function that:

Accepts a list and an index as inputs.
Returns the element at the specified index.
If the index is out of range, return an appropriate message.
Modifying Elements:
Write a function that:

Accepts a list, an index, and a new value as inputs.
Replaces the element at the specified index with the new value.
If the index is out of range, return an appropriate message.
Slicing the List:
Write a function that:

Accepts a list, a start index, and an end index as inputs.
Returns a new list containing the elements from the start index up to (but not including) the end index.
Handles cases where the indices are out of range.
Game Interaction:
Create a simple text-based game that:

Prompts the user to select an operation (access, modify, slice).
Asks for the necessary inputs (index, new value, etc.).
Displays the result and the updated list.

"""

def access_element(lst, index):
    """Returns the element at the specified index."""
    if index < 0 or index >= len(lst):
        return "Index out of range!"
    return lst[index]
    #  Is function ka kaam hai ki jo index user input kare us index pe jo element ho, usse return kare.
    # Agar user invalid index (jaise negative ya list ke length se bada index) input karta hai, toh error message return hota hai: "Index out of range!"
    # Valid index hone par wo element return ho jata hai jo us index pe list mein hota hai.

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with the new value."""
    if index < 0 or index >= len(lst):
        return "Index out of range!"
    lst[index] = new_value
    return lst
    # Is function mein user jo index aur new value dega, wo list ke us index pe value ko update kar dega.
    # Agar user invalid index provide karta hai, toh "Index out of range!" return hota hai.
    # Agar index valid hai, toh wo list ko modify karke updated list return karta hai.

def slice_list(lst, start_index, end_index):
    """Returns a new list containing elements from start_index to end_index."""
    if start_index < 0 or end_index > len(lst) or start_index >= end_index:
        return "Invalid range!"
    return lst[start_index:end_index]
    # Slicing operation se user list ka ek specific part (subset) le sakta hai.
    # start_index se lekar end_index tak ke elements ko naya list banakar return kiya jata hai.
    # Agar start aur end index invalid hain (jaise start index greater hai end index se, ya indexes list ke range ke bahar hain), 
    # toh "Invalid range!" return hota hai.

def play_game():
#  play_game() function ek interactive loop hai jisme user ko multiple operations perform karne ka option diya jata hai.

    my_list = ['apple', 'banana', 'orange', 42, 'pineapple']
    
    
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        # Access an element — user ek index input karta hai aur us index pe jo element hota hai, wo dikhaya jata hai.
        # Modify an element — user ek index aur new value input karta hai, aur wo value list mein update hoti hai.
        # Slice the list — user start aur end index provide karke list ka ek hissa extract karta hai.
        # Exit — program ko exit karne ke liye option diya gaya hai.
        
        operation = input("Enter the number of the operation you want to perform: ")

        if operation == '1':
            index = int(input("Enter the index of the element to access: "))
            result = access_element(my_list, index)
            print(f"Element at index {index}: {result}")
        
        elif operation == '2':
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Updated list: {result}")
        
        elif operation == '3':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            result = slice_list(my_list, start_index, end_index)
            print(f"Sliced list: {result}")
        
        elif operation == '4':
            print("Thanks for playing! Exiting...")
            break
        
        else:
            print("Invalid option, please choose a valid operation.")


if __name__ == "__main__":
    play_game() 
    #  ensure karta hai ke play_game() function sirf tab run ho jab yeh script directly execute ho. Agar yeh code kisi aur module ke through import ho,
    #  toh yeh function automatically execute nahi hoga.
