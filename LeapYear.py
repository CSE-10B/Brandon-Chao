def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):        #a function that takes in a year as an argument and checks if it is a leap year. It uses the rules for determining leap years, which are: a year is a leap year if it is divisible by 4 but not divisible by 100, or if it is divisible by 400. If the year meets either of these conditions, the function returns True, indicating that it is a leap year. Otherwise, it returns False.
        return True
    else:   
        return False

year = int(input("Enter a year: "))     #requests user input for a year and stores it as an integer in the variable year.

if is_leap(year):
    print("this is a leap year")
else:                                   #calls the is_leap function with the user input year and prints whether it is a leap year or not based on the return value of the function. If the function returns True, it prints "this is a leap year". If it returns False, it prints "this is not a leap year".
    print("this is not a leap year")