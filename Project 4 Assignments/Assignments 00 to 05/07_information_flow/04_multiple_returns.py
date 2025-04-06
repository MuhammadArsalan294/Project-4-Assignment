"""
There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

Asks the user for their first name and stores it in a variable

Asks the user for their last name and stores it in a variable

Asks the user for their email address and stores it in a variable

Returns all three of these pieces of data in the order it was asked

You can return multiple pieces of data by separating each piece with a comma in the return line.

Here is an example run of the program:

What is your first name?: Jane

What is your last name?: Stanford

What is your email address?: janestanford@stanford.edu

Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

(Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)

"""

# 1
def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email
    # 1. get_user_data() function:
    # Ye function user se unka first_name, last_name, aur email input leta hai.
    # Har input ke baad, input() function user se value leta hai aur usay respective variable mein store karta hai.
    # Phir ye 3 values (first_name, last_name, email) ek tuple ke roop mein return hoti hain.
    
def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)
    # 2. main() function:
    # Is function mein, get_user_data() function ko call kiya jaata hai aur jo data return hota hai, usay user_data variable mein store kiya jaata hai.
    # Phir print() ke through wo user data print hota hai. Ye data ek tuple ki form mein dikhega.

if __name__ == "__main__":
    main()
    # 3. if __name__ == "__main__": block:
    # Ye line ensure karti hai ke main() function sirf tab execute ho jab aap script ko directly run kar rahe hain (na ke usse kisi aur program mein import kar rahe ho).



# 2
def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
