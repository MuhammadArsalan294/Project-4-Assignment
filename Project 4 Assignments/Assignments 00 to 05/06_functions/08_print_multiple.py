"""
Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. 

We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!

"""
# 1 
def print_multiple(message: str, repeats: int):
    for _ in range(repeats):
        print(message, end=' ')
        # 1. print_multiple() Function
        # message: str aur repeats: int function ke arguments hain. message wo text hai jo repeat hoga, aur repeats wo number hai jo batata hai kitni baar message repeat hoga.
        # for _ in range(repeats): loop repeats number of times chalega. Har baar message ko print karega.
        # end=' ' ka use isliye kiya gaya hai taake har message ke baad nayi line na aaye, aur sab messages ek hi line mein print ho.

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)
    # 2. main() Function
    # message = input("Please type a message: ") se user se ek message input liya jata hai.
    # repeats = int(input("Enter a number of times to repeat your message: ")) se user se ek integer input liya jata hai jo batata hai message ko kitni baar repeat karna hai.
    # print_multiple(message, repeats) ko call karke message ko repeat kiya jata hai.

if __name__ == "__main__":
    main()
    # 3. if __name__ == "__main__":
    # main() function ko execute karne ke liye is statement ka use hota hai jab script directly run ho.
    # Agar script kisi aur module me import ho, to main() function execute nahi hota.

# 2
def print_multiple(message: str, repeats: int): 
    for i in range(repeats): 
        print(message)

# There is no need to edit code beyond this point
def main(): 
    message = input("Please type a message: ") 
    repeats = int(input("Enter a number of times to repeat your message: ")) 
    print_multiple(message, repeats)

if __name__ == "__main__": 
    main()



