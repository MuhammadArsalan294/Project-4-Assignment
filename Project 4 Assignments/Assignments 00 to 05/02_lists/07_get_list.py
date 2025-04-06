"""
Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything,

print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']
"""


# 1
def main():
    values = []  # Empty list to store user inputs             
    # values = [] ek khaali list banayi jisme user ke inputs store honge.

    while True:                                                  
    # while True: ek infinite loop hai jo bar bar user se input lega.
        value = input("Enter a value: ")  # User input           
        # input("Enter a value: ") user se ek value maangta hai.
        if value == "":  # If input is empty, break the loop    
        # Agar user sirf enter press kare (khaali input de), toh if value == "" condition True ho jayegi. break statement loop ko rok dega.
            break
        values.append(value)  # Add value to the list            
        # Agar user ne koi value di hai, toh values.append(value) usko list me add kar dega.

    print("Here's the list:", values)  
    # Print the final list  # Jab loop band hoga, toh list print kar di jayegi.


if __name__ == '__main__':
    main()    
    # Yeh standard Python syntax hai jo program ko execute karta hai. Jab yeh script run hogi, toh main() function execute hoga.




# 2
def main():
    lst = []  # Make an empty list to store things in

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()