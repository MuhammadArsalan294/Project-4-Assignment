"""
Print 10 random numbers in the range 1 to 100.

Here is an example run:

45 79 61 47 52 10 16 83 19 12

Each time you run your program you should get different numbers

81 76 70 1 27 63 96 100 32 92

Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would 

produce a random integer between 1 and 6, which could include 1 and could include 6:

value = random.randint(1, 6)

"""

# 1
import random
# 1. Importing Required Module
# random module use kiya gaya hai taake random numbers generate kar sakein.

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100
# 2. Constants Define Karna
# N_NUMBERS = 10 → Total 10 random numbers generate honge.
# MIN_VALUE = 1 → Random numbers ka minimum value 1 hoga.
# MAX_VALUE = 100 → Random numbers ka maximum value 100 hoga.

def main():
# 3. Main Function
# main() function define kiya jo random numbers print karega.
    
    for _ in range(N_NUMBERS):  # 10 random numbers generate karna aur ek hi line mein print karna
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")
        # 4. Generating and Printing Random Numbers
        # range(N_NUMBERS): Loop 10 baar chalega.
        # random.randint(MIN_VALUE, MAX_VALUE): Ek random number 1 se 100 ke beech generate karega.
        # end=" " → Ek hi line me saare numbers print honge.

if __name__ == '__main__':
    main()



# 2
import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    pass

if __name__ == '__main__':
    main()
