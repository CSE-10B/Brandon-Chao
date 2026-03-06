age = int(input("enter your age:"))         #provides input for user to put there age 
if age < 0:
    print("Please provide a valid age")
elif age >= 18:                             #categorizes code as old enough, not old enough, or invalid if its not an age.
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")