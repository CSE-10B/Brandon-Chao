print("Start")

steps = 0

while True:
    print("Take one pace")
    steps += 1
    
    answer = input("Have you taken 20 paces yet? (Yes/No): ").strip().lower()

    if answer == "yes":
        break
    elif answer == "no":
        continue
    else:
        print("Please type Yes or No")

print("Turn")
print("Shoot")
print("End")