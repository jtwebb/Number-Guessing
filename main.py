import sys
import os
import random


def init():
    number = random.randint(0, 250)
    guess = get_number("I'm thinking of a number. Try to guess the number I'm thinking of.")
    check_guess(guess, number)


def check_guess(guess, number):
    if guess > number:
        check_guess(get_number('Too high. Guess again.'), number)
    elif guess < number:
        check_guess(get_number('Too low. Guess again.'), number)
    else:
        play_again()


def play_again():
    print(
        """
 __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
        """
    )
    answer = input("Would you like to play again? (yes/No)")
    if answer == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        init()
    else:
        print('Thanks for playing!')


def get_number(message):
    try:
        return int(input(message))
    except KeyboardInterrupt as e:
        print('Thanks for playing!')
        sys.exit(0)
    except ValueError as e:
        print('Please use whole numbers only')
        return get_number(message)


init()
