# Program to remove non-letter prefix and suffix. 

# name = input("Enter: ")

# for i in range(len(name)):
#     prefixNonLetter = ''

#     while len(name) > 0 and not name.isalpha():
#         prefixNonLetter += name[0]
#         # print(letter)
#         # print(name)
#         name = name[1:]
    
#     print(prefixNonLetter)
#     print(name)

import random

def main():
    print("Bagels, a deductive logic game.")
    print('By Ishaan Jangid \'ishaanjangid035@gmail.com\'')
    print()
    print('when I say:\tThat means')
    print('Pico\tOne Digit is correct but in the wrong place.')
    print('Fermi\tOne Digit is correct and in the right place.')
    print('Bagels\tNo digit is correct.')
    print()
    print('For example, if the number is 248 and you guess 843.')
    print("the clues would be Fermi Pico.")

    # Make the secrate number the player needs to guess:
    numbers = list('0123456789')
    random.shuffle(numbers)

    # Get the first 3 digit in the list for the secrate number:
    secretNum = f"{numbers[0]}{numbers[1]}{numbers[2]}"
    
    print('I have thought up a 3-digit number.')
    print('You have 10 guesses to get it.')

    numGuesses = 1

    while numGuesses <= 10:
        print('Guess #',numGuesses)
        guess = input('> ')

        clues = getClues()


def getClues(guess,secretNum):
    """Returns a string with the pico, fermi, bagels clues for
    a guess and secret number pair."""

    if guess == secretNum:
        return 'you got it!'
    
    
main()


