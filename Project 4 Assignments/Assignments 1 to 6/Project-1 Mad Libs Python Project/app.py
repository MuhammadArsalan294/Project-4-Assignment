 # Mad Libs Game in Python

print("Welcome to Mad Libs!")
print("Please provide the following inputs:")

# Get user inputs for the different parts of speech
noun1 = input("Noun (place): ")                       # place = input("Koi jagah ka naam do: ")
noun2 = input("Noun (object): ")                      # object_name = input("Koi cheez ka naam do: ")
verb1 = input("Verb (action): ")                      # action1 = input("Koi kaam batayein (verb): ")
verb2 = input("Verb (action): ")                      # action2 = input("Dusra kaam (verb): ")
adjective1 = input("Adjective (descriptive word): ")  # descriptive1 = input("Koi sifat (adjective): ")
adjective2 = input("Adjective (descriptive word): ")  # descriptive2 = input("Dusri sifat (adjective): ")
adverb1 = input("Adverb (how something is done): ")   # how1 = input("Kaise kiya? (adverb): ")
adverb2 = input("Adverb (how something is done): ")   # how2 = input("Phir kaise kiya? (adverb): ")
color = input("Color: ")                              # color = input("Koi color ka naam: ")

# Create the story using the inputs
story = f"""
Once upon a time, in a {adjective1} {noun1}, there was a {noun2} that loved to {verb1}.
One day, it {verb2} {adverb1} into the {adjective2} forest, looking for something {adjective1}.
It found a {color} {noun2} and decided to {verb1} it {adverb2} for the rest of its life.
"""

# Print the final story
print("\nHere is your Mad Libs story:\n")
print(story)


