import random


def guess_the_number():
    end_game = False
    number = random.randint(1, 100)
    while end_game != True:
        guess = input("Guess the number: ")
        try:
            guess_by_number = int(guess)
        except ValueError:
            print("It's not a number! Try again.")
            continue
        if guess_by_number > number:
            print("To big!")
            continue
        elif guess_by_number < number:
            print("To small!")
            continue
        else:
            print("You win! Congratulations!")
            end_game = True
            break

guess_the_number()


