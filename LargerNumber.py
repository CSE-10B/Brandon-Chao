num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))        #requests user input for two numbers and stores them as num1 and num2

if num1 > num2:
    print("The larger number is:", num1) #compares the two numbers and prints out which one is larger. If num1 is larger than num2, it will print num1 as the larger number.
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal") #if both prevous conditions are false, it means the numbers are equal and it will print that both numbers are equal.