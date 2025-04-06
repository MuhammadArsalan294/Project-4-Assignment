"""
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. 

Do no write twenty print statements The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

"""

# 1
def main():
    for num in range(0, 40, 2):  # Start from 0, go up to 38, step by 2
        print(num, end=" ")  # Print numbers on the same line with space

if __name__ == "__main__":
    main()
    # Yeh check karega ke script direct run ho rahi hai ya import ki gayi hai.
    # Agar script direct run ho rahi hai, toh main() function execute hoga.
    # Agar script kisi aur file me import ho, toh main() run nahi hoga.



# 2
def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop
   
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()