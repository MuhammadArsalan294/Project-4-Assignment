"""
Write a program to print terms in the Fibonacci sequence up to a maximum value.

In the 13th century, the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population of rabbits, 

devised a mathematical sequence that now bears his name. The first two terms in this sequence, Fib(0) and Fib(1), are 0 and 1, and every subsequent term 

is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:

Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 

(you should store this value as a constant!). Thus, your program should produce the following sample run:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

"""

# 1
MAX_VALUE = 10000  # Maximum limit
# Ek constant variable jo maximum value ko store karta hai (10,000 tak values print hongi).

def main():
    a, b = 0, 1  # Pehle do numbers set karna
    # Fibonacci series ke pehle do numbers 0 aur 1 hotay hain, isliye a = 0, b = 1 rakha hai.

    while a < MAX_VALUE:
    # Jab tak a (Fibonacci number) 10,000 se chhota hai, tab tak loop chalay ga.

        print(a, end=" ")  # Print number
        # Har Fibonacci number ek line me space ke saath print hoga
        
        a, b = b, a + b  # Agle numbers update karna
        # Naya Fibonacci number generate karne ka formula
        # a ka naya value b ban jaye ga
        # b ka naya value a + b (sum of last two numbers) ho jaye ga

if __name__ == '__main__':
    main()




# 2 
MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()