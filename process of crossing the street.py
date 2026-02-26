print("Start")

while True:
    print("Look left")
    left = input("Are cars coming from the left? (Yes/No): ").strip().lower()

    if left == "yes":
        print("Wait")
        continue
    elif left != "no":
        print("Please type Yes or No")
        continue

    print("Look right")
    right = input("Are cars coming from the right? (Yes/No): ").strip().lower()

    if right == "yes":
        print("Wait")
        continue
    elif right != "no":
        print("Please type Yes or No")
        continue

    print("Cross the street")
    break

print("End")