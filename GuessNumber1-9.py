import random

number = random.randint(1, 9)       #generates a random number between 1 and 9 and stores it in the variable number.

while True:
    guess = int(input("Guess a number between 1 and 9: "))      #requests user input for a guess and stores it as an integer in the variable guess. The loop continues until the user guesses the correct number.

    if guess == number:
        print("Well guessed!")      #if the user's guess is correct, it will print "Well guessed!" and the loop will break, ending the program.
        break
    else:
        print("Try again.")