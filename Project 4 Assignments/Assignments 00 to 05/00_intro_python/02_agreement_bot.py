"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" 

(the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!

"""

# 1
def main():
# main() function banaya gaya hai jo poora program execute karega.

    favorite_animal = input("What's your favorite animal? ")
     # input("What's your favorite animal? ") Yeh user se input lene ke liye use hota hai. Jo bhi user likhega, woh ek string (text) ke roop mein store hoga.
    # favorite_animal Yeh ek variable hai jo user ke diye gaye input ko store karega.
    # 👀 Agar user "Lion" likhta hai, toh favorite_animal = "Lion" store ho jayega.

    print(f"My favorite animal is also {favorite_animal}!")
     # Jawab print karna
    # print(f"...") ek formatted string (f-string) hai. Yeh {favorite_animal} ki jagah user ka input print karega.


if __name__ == "__main__":
    main()
# Function ko call karna
# Yeh check karta hai ke agar program direct run ho raha hai, tabhi main() function chale. Yeh ek best practice hai Python programming mein.



# 2
def main():
    favorite_animal = input("What's your favorite animal? ").strip()  # Remove extra spaces
    
    if favorite_animal.isalpha():  # Checks if all characters are letters (A-Z/a-z)  
        print(f"My favorite animal is also {favorite_animal}!")
    else:
        print("Invalid! Please enter only letters (no numbers or symbols).")

if __name__ == '__main__':
    main()