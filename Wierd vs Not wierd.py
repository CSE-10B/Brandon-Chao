n = int(input("Enter an integer: "))     #requests user input for an integer and stores it as n

if n % 2 == 1:
    print("Weird")          #if n is odd, it is weird.
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:          #if n is even and in the inclusive range of 2 to 5, print Not Weird. If n is even and in the inclusive range of 6 to 20, print Weird.
    print("Weird")
else:
    print("Not Weird")
