#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 10, 2022
# Number guessing program, this random numbers being generated.
import random


def main():

    # Spacer
    print("")

    # Obtain user guess for the correct answer
    print("This is a number guessing game, choose a number between 1-10")
    guess_answer = int(input("Insert your guess (0 - 9): "))

    # Spacer
    print("")

    # Generates the random number
    guess_generated = random.randint(0, 9)

    # Answer checking, seeing if user input is correct
    if guess_answer == random.randint:
        print("Your guess is correct!")

    else:
        print(f"Your answer is incorrect! the correct answer was:{guess_generated}")


if "__main__" == __name__:
    main()
