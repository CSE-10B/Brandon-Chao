#asks the user to enter a number 
num = int(input("Enter a number: ")) 
# Use the modulus operator to divide the number by 2
# If the remainder is 0, the number is even
if num % 2 == 0:
    print("The number is even.") 
# If the remainder is not 0, the number is odd    
else:
    print("The number is odd.")
