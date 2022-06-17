# This is Guessing Game 2.0. I learned more about functions and decided to
#   rewrite the code to include a counter that will print out how many times
#   you played the game when you're done.

import random

rd = random.randint(1,9)
guess = None
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()