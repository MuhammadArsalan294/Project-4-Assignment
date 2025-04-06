"""
Milestone #2: Adding in All Planets
Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an 
object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

Mercury: 37.6%

Venus: 88.9%

Mars: 37.8%

Jupiter: 236.0%

Saturn: 108.1%

Uranus: 81.5%

Neptune: 114.0%

Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print 
the equivalent weight on that planet rounded to 2 decimal places if necessary.

You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something 
other than one of the above planets.

Sample Run

$ python planetaryweight.py

Enter a weight on Earth: 120

Enter a planet: Mars

The equivalent weight on Mars: 45.36

Sample Run

$ python planetaryweight.py

Enter a weight on Earth: 150

Enter a planet: Jupiter

The equivalent weight on Jupiter: 354.0

Useful Syntax

Python has an if statement! This if statement passes if the value of x is the same as the value of y. x and y can be literal numbers, strings, variables, or 
constants.

x = 42 y = 42

if x == y: print("x and y are equal!")

"""
# Program to calculate weight on different planets

def main():
 
    planet_gravity = { # Dictionary storing the gravity percentages for each planet
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    # Planet ke gravity percentage ko store karne ke liye dictionary ka use kiya gaya hai.
    # Har planet ke liye, gravity ka percentage diya gaya hai jo Earth ki gravity ke comparison me hai.

   
    earth_weight = float(input("Enter a weight on Earth: "))  # Get the user's weight on Earth
    # User se Earth pe apna weight input karne ko bola gaya hai.
    # float() use kiya gaya hai taake user decimal numbers bhi enter kar sake (jaise 70.5 kg).
    

    planet = input("Enter a planet: ")  # Get the name of the planet
    #  User se planet ka naam input liya jata hai jahan wo apne weight ka equivalent dekhna chahta hai.
    

    if planet in planet_gravity: # Check if the planet is in the dictionary
    # Yeh line check karti hai ke user jo planet enter kar raha hai wo dictionary mein available hai ya nahi.
    # Agar planet available hai toh calculation perform hoti hai. Agar available nahi hai toh error message dikhaya jata hai.  

        planet_weight = earth_weight * planet_gravity[planet]  # Calculate the weight on the chosen planet
        #  Is line mein planet ka weight calculate hota hai.
        # Earth ka weight multiply hota hai planet ke gravity percentage se.
       
        planet_weight_rounded = round(planet_weight, 2)  # Round the result to 2 decimal places
        #  round() function se weight ko 2 decimal places tak round kiya jata hai, taake result clean aur readable ho.
       
        print(f"The equivalent weight on {planet}: {planet_weight_rounded}")  # Display the result
    else:
        print("Invalid planet name. Please enter a valid planet name.")
        # Result ko display kiya jata hai.
        # Planet ka naam aur us planet pe user ka weight print hota hai.
        # Agar user koi galat planet ka naam enter karta hai, toh program error message dikhata hai:


if __name__ == "__main__": # Call the main function
    main()
    #  Is line ka matlab hai ke jab program ko run kiya jata hai, toh main() function execute hoga.



