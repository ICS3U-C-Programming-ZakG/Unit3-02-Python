#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 13, 2023
# This program makes the user guess a number from 0-9 and says if it's correct or not.

import constants


def main():
    # Get user guess
    print("This program is a guessing game and you must guess a number from 0-9!")
    user_guess = int(input("Please guess a number from 0-9: "))

    # Check user guess if correct or incorrect
    if user_guess == constants.CORRECT_GUESS:
        print("You guessed correctly!")
    if user_guess != constants.CORRECT_GUESS:
        print("You guessed the wrong number!")


if __name__ == "__main__":
    main()
