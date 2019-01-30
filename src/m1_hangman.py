"""
Hangman.

Authors: Parker Jordan and Colin Browne.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# : 2.Done Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random
import time

def main():
    secret_word = pick_secret_word()
   #print(secret_word)                #Prints the word for testing
    number_incorrect_guesses = game_rules()
    game_board = make_game_board(secret_word)
    current_guess = user_guess()
    #test_guess_against_word(secret_word, current_guess, number_incorrect_guesses)
    game_loop(secret_word, current_guess, number_incorrect_guesses, game_board)


def pick_secret_word():
    with open('words.txt') as f:
        f.readline()
        string =f.read()
        words = string.split()

    r = random.randrange(0, len(words))
    secret_word = words[r]
    while True:
        if len(secret_word) <= 4:
            r = random.randrange(0, len(words))
            secret_word = words[r]
        else:
            return secret_word


def game_rules():
    print('Welcome to Hangman/woman!!!!! We have selected a secret word for your game.')
    incorrect_guesses = int(input('How many incorrect guesses do you want to allow? (A standard game of Hangman would have 6 incorrect guesses): '))
    return incorrect_guesses


def make_game_board(secret_word):
    string_ = '_ ' * len(secret_word)
    print(string_)
    return string_


def user_guess():
    guess = input('What letter would you like to try?: ')
    return guess


def test_guess_against_word(secret_word, current_guess, number_incorrect_guesses, game_board):
    factor = 1
    new_game_board = ''
    for k in range(len(secret_word)):
        if current_guess == secret_word[k]:
            new_game_board = new_game_board + secret_word[k] + ' '
            factor = factor * 0
        else:
            new_game_board = new_game_board + game_board[2*k] + ' '
            factor = factor * 1

    number_incorrect_guesses = number_incorrect_guesses - factor
    print('You have',number_incorrect_guesses, 'remaining incorrect guess(es).')
    print(new_game_board)
    _tuple = (new_game_board, number_incorrect_guesses)
    return _tuple


def game_loop(secret_word, current_guess, number_incorrect_guesses, game_board):

    while number_incorrect_guesses != 0:
        _tuple = test_guess_against_word(secret_word, current_guess, number_incorrect_guesses, game_board)
        number_incorrect_guesses = _tuple[1]
        game_board = _tuple[0]
        spaced_secret_word = ''
        for k in range(len(secret_word)):
            spaced_secret_word = spaced_secret_word + secret_word[k] + ' '
        if spaced_secret_word == game_board:
            print()
            print("Congradulations!!! You didn't kill a man/woman!!" )
            break
        if number_incorrect_guesses == 0:
            print()
            print()
            print('The word was:', secret_word)
            print()
            print('Welp, you killed a man/woman...')
            break
        current_guess = user_guess()
    replay = input('Would you like to play again?(y/n): ')
    if replay == 'n':
        print()
        print()
        print('What, is our game not good enough for you???')
        time.sleep(2)
        print()
        print()
        print("Too bad, you're playing again, and this time you're going to LIKE IT!!!")
        time.sleep(2)
        print()
        print()
        main()
    if replay == 'y':
        print()
        print()
        print('Well then, I guess you had better rerun the program ya dingus')
        print()
        print()
        time.sleep(2.5)
        print("JK, we'll do it for you. :)")
        time.sleep(2)
        main()
# To end the game type in anything but a 'y' or an 'n' when prompted to. Both of those answers will continue into another round of the game. (purposely)

main()