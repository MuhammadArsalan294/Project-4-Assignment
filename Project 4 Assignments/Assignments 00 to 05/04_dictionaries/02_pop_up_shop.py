"""
Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

Here is an example run of the program (user input is in bold italics):

How many (apple) do you want?: 2

How many (durian) do you want?: 0

How many (jackfruit) do you want?: 1

How many (kiwi) do you want?: 0

How many (rambutan) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5

"""

# 1
def main():
    # Dictionary containing fruit names and their prices per unit
    fruit_prices = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 10.0,
        "kiwi": 7.5,
        "rambutan": 12.0,
        "mango": 8.5
    }
    # Yeh ek dictionary hai jisme fruit names (keys) aur unki prices per unit (values) stored hain.

    total_cost = 0  # Variable to store total cost
    # Yeh total cost store karega jo user ki purchases ka sum hoga.

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
    # Loop chalayega har fruit ke liye aur uska price access karega.
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a valid non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
            # User se fruit ki quantity input leta hai
            # Agar user negative number dale to error message dikhata hai
            # ValueError handle karta hai agar user number ke ilawa kuch aur likhe
            # total_cost update hoti hai (quantity * price) se

    # Print the total cost
    print(f"\nYour total is ${total_cost:.2f}")
    # Yeh total cost 2 decimal places tak print karega.

if __name__ == "__main__":
    main()



# 2
def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()