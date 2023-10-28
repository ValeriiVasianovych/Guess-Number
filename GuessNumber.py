#!/usr/bin/env python3
import random

def main():
    random_num = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < 1 or user_guess > 10:
            print('Error. The number must be between 1 and 10.')
            continue

        attempts += 1

        if user_guess == random_num:
            print(f'Congratulations! You guessed it! The number is {random_num}. Attempts: {attempts}')
            break
        elif user_guess > random_num:
            print(f'No, {user_guess} > then hidden number.')

        elif  user_guess < random_num:
            print(f'No, {user_guess} < then hidden number.')

        if attempts >= 8:
            print(f'You lose! You have reached the maximum number of attempts. The hidden number was {random_num}. Attempts: {attempts}')
            break

if __name__ == "__main__":
    main()

