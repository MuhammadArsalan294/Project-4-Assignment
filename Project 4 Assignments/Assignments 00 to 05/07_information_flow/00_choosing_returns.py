"""
There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check 

if someone is an adult. We might check their age and return different things depending on how old they are!

We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) 

function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, 

return False instead.

Here are two sample runs of the program, one for each return option (user input in bold italics):

(Entered age is an adult age)

How old is this person?: 35

True

(Entered age is not an adult age)

How old is this person?: 7

False

"""


# 1
ADULT_AGE = 18  # Adult age in the United States
# 1. ADULT_AGE = 18
# Ye ek constant variable hai jisme 18 set kiya gaya hai, jo United States mein adult hone ki age hai.

def is_adult(age):
    return age >= ADULT_AGE
    # 2. is_adult(age) function:
    # Ye function age ko argument ke roop mein leta hai.
    # Agar age 18 ya usse zyada hai, to ye True return karega (matlab wo adult hai).
    # Agar age 18 se kam hai, to False return karega (matlab wo adult nahi hai).

def main():
# Taking user input
    age = int(input("How old is this person?: "))
    print(is_adult(age))
    # 3. main() function:
    # Yahan, input() function ke zariye user se age input li jaati hai.
    # input() se jo value milti hai, wo hamesha string hoti hai. Isliye, humne int() function use kiya hai taake us string ko integer mein convert kiya ja sake.
    # Phir is_adult(age) function ko call karke, result print kiya jaata hai.

if __name__ == "__main__":
    main()
    # 4. if __name__ == "__main__": block:
    # Ye ensure karta hai ke main() function sirf tab execute ho jab aap script ko directly run kar rahe ho. Agar aap is file ko kisi aur program mein import karte hain, to main() function automatically execute nahi hoga.


# 2
ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()