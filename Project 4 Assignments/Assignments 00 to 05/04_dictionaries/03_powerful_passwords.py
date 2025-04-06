"""
You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)

"""

import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()
    # hashlib.sha256() ka use kiya gaya hai jo ek one-way encryption technique hai.
    # .encode() password ko bytes me convert karta hai kyunki SHA-256 hashing ko bytes format chahiye hota hai.
    # .hexdigest() se hashed output hexadecimal format me convert hota hai.

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email exists in stored_logins and verifies 
    if the hashed password matches the stored hash.
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False
    # Pehle check karta hai ki email stored_logins me mojood hai ya nahi.
    # Agar email exist karti hai, to entered password ko hash karta hai aur stored hash se compare karta hai.
    # Agar match ho jaye, to True return hota hai, warna False.

def main():
# Example stored logins (passwords are stored as hashes)
    stored_logins = {
        "user1@example.com": hash_password("mypassword123"),
        "user2@example.com": hash_password("securepass456"),
        "user3@example.com": hash_password("hello_world!")
}

    # Example login attempts
    print(login("user1@example.com", "mypassword123", stored_logins))  # ✅ True
    print(login("user2@example.com", "wrongpassword", stored_logins))  # ❌ False
    print(login("unknown@example.com", "randompass", stored_logins))   # ❌ False
    # Stored passwords hash form me save kiye gaye hain taki security barqarar rahe.
    # Login attempts ko test kiya gaya hai:
    # Sahi credentials → True
    # Galat password → False
    # Agar email register nahi hai → False

if __name__ == '__main__':
    main()



# 2
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

# There is no need to edit code beyond this point

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()