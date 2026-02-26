print("Start Reading Flowchart")

while True:
    print("Look at the current symbol")

    shape = input("Is it a Rectangle, Diamond, or Oval? pls type which one").strip().lower()

    if shape == "rectangle":
        print("Perform the action in the box")
        print("Follow the arrow to the next symbol")

    elif shape == "diamond":
        answer = input("Answer the question (Yes/No): ").strip().lower()
        
        if answer == "yes":
            print("Follow the YES arrow")
        elif answer == "no":
            print("Follow the NO arrow")
        else:
            print("Please type Yes or No")
            continue

    elif shape == "oval":
        end = input("Does it say END? (Yes/No): ").strip().lower()
        
        if end == "yes":
            print("Stop reading the flowchart")
            break
        elif end == "no":
            print("This is the START symbol")
            print("Follow the arrow")
        else:
            print("Please type Yes or No")
            continue

    else:
        print("Please type Rectangle, Diamond, or Oval")
        continue

print("End")