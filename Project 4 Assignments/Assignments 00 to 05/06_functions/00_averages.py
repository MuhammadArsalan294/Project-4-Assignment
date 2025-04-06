"""
Write a function that takes two numbers and finds the average between the two.

"""

# 1
def average(a, b):
    return (a + b) / 2
    # 1. Function Definition
    # def keyword ka matlab hai ke hum ek function bana rahe hain.
    # average(a, b): Yeh function do arguments (a aur b) ko accept karta hai.
    # (a + b) / 2: Dono numbers ka sum karta hai aur phir 2 se divide karke average return karta hai.

def main():
# Example usage:
    num1 = 10
    num2 = 20
    print("Average:", average(num1, num2))
# 2. Function Call (Example Usage)
# num1 = 10 aur num2 = 20 set kiya.
# average(num1, num2) ko call kiya, jisme a = 10 aur b = 20 pass ho gaye.
# print statement output dikhayega.

if __name__ == '__main__':
    main()



# 2
def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

