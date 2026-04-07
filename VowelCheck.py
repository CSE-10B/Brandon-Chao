# Ask the user to enter a single character
char = input("enter a single character:") 
if len(char) == 1:  
    # Check if the character is a vowel
    if char.lower() in ['a','e','i','o','u']:
        print("this is a vowel")
    else:
        print("this aint a vowel") 
else: 
    print("pls enter only one character")
