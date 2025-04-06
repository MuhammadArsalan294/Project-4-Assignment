"""
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

"""

# 1
def main():
    for num in range(10, 20):  # 10 se 19 tak
    # 1. main() Function
    # range(10, 20) ek loop chalata hai 10 se lekar 19 tak (kyunki range() ka upper limit exclude hota hai).
    # Har number num ko check karega aur print karega

        if num % 2 == 0:
            print(num, "even")
        else:
            print(num, "odd")
            # 2. Even-Odd Check
            # num % 2 == 0 ka matlab hai agar number 2 se divide ho jaye bina remainder ke, to yeh even hai.
            # Agar num % 2 != 0 ho to yeh odd hai.
            # Output me likh diya jayega even ya odd.

if __name__ == '__main__':
    main()
    # 3. if __name__ == '__main__':
    # Script jab direct run hogi, tabhi main() function execute hoga.
    # Agar script import ho jaye kisi aur file me, to automatically execute nahi hogi.


# 2
def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()