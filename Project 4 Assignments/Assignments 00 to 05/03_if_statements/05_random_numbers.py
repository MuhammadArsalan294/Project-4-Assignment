"""
Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92

Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call 

would produce a random integer between 1 and 6, which could include 1 and could include 6:

value = random.randint(1, 6)

"""

# 1
import random
# Random number generate karne ke liye

N_NUMBERS: int = 10    # Total 10 numbers generate karne hain
MIN_VALUE: int = 1     # Sabse chhota possible number 1 hoga.
MAX_VALUE: int = 100   # Sabse bada number 100 ho sakta hai

def main():
    """
    Generate and print 10 random numbers in the range 1 to 100.
    """
    for _ in range(N_NUMBERS): # 10 dafa loop chalega
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ") # Ek line me print karega
    print()  # Taake output naya line par move ho
    # Loop N_NUMBERS dafa chalega (yaani 10 dafa).
    # random.randint(MIN_VALUE, MAX_VALUE) ek random number generate karega (1 se 100 ke beech).
    # print(..., end=" ") numbers ko ek hi line me print karega (new line nahi lega).
    # Akhir me print() ek new line dega taake agla output sahi dikhe.

if __name__ == '__main__':
    main()
    # 🔹 Yeh ensure karega ke jab script direct run ho, tab main() function execute ho.

# 2
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    pass

if __name__ == '__main__':
    main()