"""
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high)  Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. 
"""

# 1
def in_range(n, low, high):
# 1. in_range function:
# Yeh function 3 cheezon ko check karta hai:
# n: Number jo aap check karna chahte hain.
# low: Lower boundary (shuru ka point).
# high: Upper boundary (aakhri point).
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    return False
    # 2. Condition (if n >= low and n <= high):
    # Yeh condition check karti hai agar n low se bara ya barabar hai aur n high se chhota ya barabar hai.
    # Agar yeh dono cheezein sach hain, toh function True return karta hai. Matlab n range ke andar hai.
    # Agar yeh condition fail hoti hai, toh function False return karta hai. Matlab n range ke bahar hai.

# Taking input from the user
n = int(input("Enter a number: "))
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
# 3. Input: 
# Jab program start hota hai, yeh user se 3 cheezein input maangta hai:
# Ek number (n) jo user check karna chahta hai.
# Ek lower boundary (low).
# Ek upper boundary (high).


# Printing the result of the in_range function
print(in_range(n, low, high))
# 4. Condition Check:
# Uske baad, program in_range function ko call karta hai aur input ke saath check karta hai:
# Agar n dono boundaries ke beech aata hai, toh function True return karta hai.
# Agar n range ke bahar hai, toh function False return karta hai.
# True ya False print hota hai, jo batata hai ki n range ke andar hai ya nahi.




# 2
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # We could have also included an else statement, but since we are returning, it's fine without!
    return False

