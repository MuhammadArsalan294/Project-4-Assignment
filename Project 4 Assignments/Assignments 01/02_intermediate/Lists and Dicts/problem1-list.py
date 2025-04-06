"""
Problem #1: List Practice
Now practice writing code with lists! Implement the functionality described in the comments below.

def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 


# Print the updated list.

"""

def main():
    
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple'] #     # Create a list called fruit_list that contains the following fruits
    #  Yeh line ek list create kar rahi hai jisme 5 fruits (apple, banana, orange, grape, pineapple) diye gaye hain.
    # List ek ordered collection hoti hai jisme aap multiple items ko store kar sakte hain.

    print(f"The length of the list is: {len(fruit_list)}")# Print the length of the list
    # len() function ka use karke list ki length (matlab kitne items hain) print kiya gaya hai.
    # Yeh line display karegi ki list mein kitne fruits hain.
    
    fruit_list.append('mango') # Add 'mango' at the end of the list
    # append() function ka use karke ‘mango’ ko list ke end mein add kiya gaya hai.
    # append() method list ke last mein ek item add karne ka kaam karta hai.

    print(f"Updated list: {fruit_list}")  # Print the updated list
    # List ko print kiya gaya hai taake user ko updated list dikhayi ja sake.

if __name__ == "__main__": # Call the main function
    main()
    #  Is line ka matlab hai ke main() function tabhi call hoga jab program ko directly run kiya jaye.
    # Isse yeh ensure hota hai ke agar yeh file kisi aur program mein import ho, toh main() function automatically run na ho.
