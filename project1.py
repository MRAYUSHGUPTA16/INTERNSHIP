import random

def guessing_game():

    number = random.randint(1, 100)

    print("Welcome to Number Guessing Game")
    print("I have selected a number between 1 and 100.")

    while True:

        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too Low! Try Again.")

        elif guess > number:
            print("Too High! Try Again.")

        else:
            print("Congratulations! You guessed the correct number.")
            break


guessing_game()