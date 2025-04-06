"""
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. 

Do no write twenty print statements

The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

"""


# 1
def main():
    for i in range(20):  # 20 numbers generate karna
    # Yeh loop 0 se 19 tak chalega (total 20 iterations).

        print(i * 2, end=" ")  # Even number print karna
        # Har i ko 2 se multiply karna → Even number milega
        # i = 0 → 0
        # i = 1 → 2
        # i = 2 → 4 ...
        # end=" " → Yeh ensure karega ke numbers ek hi line me print hon.

if __name__ == "__main__":
    main()





# 2
def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop
   
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()