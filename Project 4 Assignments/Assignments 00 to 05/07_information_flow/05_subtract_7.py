"""
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, 

revisit the add_five example from lecture.

"""

# 1
def subtract_seven(num):
    return num - 7
    # 1. subtract_seven(num) function:
    # Ye function ek num argument leta hai, jo kisi number ko represent karta hai.
    # Phir ye function num - 7 ke result ko return karta hai, matlab jo number diya gaya hai usmein se 7 subtract kar ke.
    

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)
    # 2. main() function:
    # input("Enter a number: ") se program user se ek number input karta hai.
    # int() function ka use kiya jaata hai taake jo string input hoti hai, usay integer mein convert kiya ja sake.
    # Phir subtract_seven(number) function ko call karke us number se 7 subtract kiya jaata hai aur result result variable mein store hota hai.
    # print("Result after subtracting 7:", result) se result print hota hai.


if __name__ == '__main__':
    main()
    # 3. if __name__ == '__main__': 
    # block:Ye line ensure karti hai ke main() function sirf tab run ho jab aap script ko directly run kar rahe hain, na ke kisi aur program mein import kar rahe ho.





# 2
def main():
	num: int = 7
	num = subtract_seven(num)
	print("this should be zero: ", num)

def subtract_seven(num):
	num = num - 7
	return num


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()