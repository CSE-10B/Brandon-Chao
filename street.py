print("Start")
print("Follow Liberty Avenue")

while True:
    answer = input("Have you gone 2 miles yet? Yes or No?")
    if answer == "Yes":
        break 
    elif answer == "No":
        print("keep walking on Liberty Ave")
    else:
        print("please type Yes or No")
print("turn left onto 40th street")

while True:
    answer = input("did you reach the bridge? Yes or No?:")
    
    if answer == "Yes":
        print("stop at the bridge (Do Not cross)")
        break
    elif answer == "No":
        print("keep walking on 40th street")
    else: 
        print("listen to the directions provided")

print("turn Right onto Foster Street")

while True:
    answer = input("Is this the first left turn Yes or No?:")

    if answer == "Yes":
        print("turn left")
        break
    elif answer == "No":
        print("keep walking on foster street")
    else: 
        print("listen to the directions provided")

while True: 
    answer = input("Have you reached the NREC building? Yes or No?:")

    if answer == "Yes":
        print("you arrived at NREC")
        break
    elif answer == "No":
        print("keep following the road")
    else: 
        print("listen to the directions provided")

print("END")









