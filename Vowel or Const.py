# Input a character
character = input("Enter a character: ").lower()

# Check if the input is a single alphabet character
if len(character) == 1 and character.isalpha():
    # Check if the character is a vowel
    if character in "aeiou":
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    print("Please enter a single alphabet character.")