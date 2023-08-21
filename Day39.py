# My Take in making the BAGEL GAME :->
import random

def main():
    print("The is a DECTETIVE LOGIC game.")
    print("The AI will pass on a random 2-digit number.")
    print("You have to guess it ;->")
    print()
    print('Term:\tWhat they mean')
    print('YES:\tNumber is correct and is in correct Place.')
    print('NO:\tNumber is correct but in incorrect Place.')
    print('WRONG:\tNo digit is correct.')
    print()
    print('If I give 248 and you write 824...')
    print('I will say: \'YES NO\'')
    print()
    print("You have 10 Guesses to guess the Number")

    number = list('012345689')
    random.shuffle(number)
    secretNum = f"{number[0]}{number[1]}{number[2]}"


    # Main Program Loop

    for i in range(10):
        guess = input('> ')
        hint = clues(guess,secretNum)

        print(hint)

        if hint == 'you got it !'.lower():
            break
        
    print('Tnx for playing!!!')
        

def clues(guess,secretNum):
    # Check if the 'guess' == 'secretNum'
    if guess == secretNum:
        return 'you got it !'
    
    clue = ''

    for i in range(3):

        if guess[i] == secretNum[i]:
            clue += 'Yes '
        
        elif guess[i] in secretNum:
            clue += 'No '

    if len(clue) == 0:
        return 'WRONG'
    else:
        return clue
    

main()