import random
EASY = 10
HARD = 5
from art import logo
def check_guess(user_guess,computer_guess,turns):
    if user_guess > computer_guess:
        print("You guessed too high.")
        return turns -1
    elif user_guess < computer_guess:
        print("You guessed too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {computer_guess}")
        return None
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return EASY
    else:
        return HARD
def game():
    print(logo)
    answer = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns =set_difficulty()
    gusse = 0
    while gusse!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        gusse =int(input("Guess the number: "))
        turns=check_guess(gusse,answer,turns)
        if turns==0:
            print(f"You've run out of guesses. Run Program to play again.The number was {answer}")
            return
        elif gusse!=answer:
            print("Guess again")
    return None
game()