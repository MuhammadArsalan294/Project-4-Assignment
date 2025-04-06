"""
Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. 

Write code in main() which will:

Prompt the user to enter a fruit ("Enter a fruit: ")

Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

Here's two sample runs of the program (user input in bold italics):

Enter a fruit: pear

This fruit is in stock! Here is how many:

1000

Enter a fruit: lychee

This fruit is not in stock.
"""
# 1
def num_in_stock(fruit):
    inventory = {
        "apple": 50,
        "banana": 30,
        "orange": 20,
        "pear": 1000,
        "grape": 200
    }
    return inventory.get(fruit, 0)
    # 1. num_in_stock(fruit) function:
	# Ye function fruit ko argument ke roop mein leta hai.
	# inventory ek dictionary hai jisme fruits ke naam keys hain aur unke stock numbers values hain.
	# inventory.get(fruit, 0) use hota hai taake agar user input kiya gaya fruit inventory mein ho, to uska stock number return ho jaye.
	# Agar fruit dictionary mein nahi hai, to default value 0 return hoti hai.

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
	 
    if count > 0:
        print("This fruit is in stock! Here is how many:\n")
        print(count)
    else:
        print("This fruit is not in stock.")
		# 2. main() function:
		# input("Enter a fruit: ") se program user se fruit ka naam input karta hai.
		# Phir num_in_stock(fruit) function ko call karke us fruit ka stock count check kiya jata hai.
		# Agar stock count 0 se zyada hai, to message dikhata hai: "This fruit is in stock!" aur count bhi print hota hai.
		# Agar stock count 0 hai, to message dikhata hai: "This fruit is not in stock."

if __name__ == '__main__':
    main()
	# 3. if __name__ == '__main__': block:
	# Ye part ensure karta hai ke main() function sirf tab run ho jab aap script ko directly run kar rahe ho, na ke usse kisi aur program mein import kar rahe ho.




# 2
def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)

# There is no need to edit code beyond this point

def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()