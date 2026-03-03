char = input("enter a single character:") #this just requestion sometime to choose a character
if len(char) == 1:                             #if someone slected a signle char then it will say its a vowel
    if char.lower() in ['a','e','i','o','u']:
        print("this is a vowel")
    else:
        print("this aint a vowel") #code provides results if a single character of a non-vowel is inputed
else: 
    print("pls enter only one character")