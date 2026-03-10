side1 = float(input("Enter side 1: "))          #these next three lines request user input for the three sides of the triangle.
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")               #All three user inputs are anaylized and if they are all the same, it is an equilateral triangle.
else:
    print("The triangle is not equilateral.")               #prints that the triangle is not equilateral if any of the sides are different.