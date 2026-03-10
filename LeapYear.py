def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)             #this function takes a user input for a year and determines if it is a leap year or not. A leap year is defined as being divisible by 4 but not divisible by 100, unless it is also divisible by 400. The function returns True if the year is a leap year and False otherwise.

year = int(input("Enter a year: "))         #requests user input for a year and stores it as an integer in the variable year.
print(is_leap(year))