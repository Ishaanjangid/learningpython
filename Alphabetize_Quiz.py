# Day 56

import random,time

# Funciton to print out a alphebet string value
def alphabet():
    alphabet = ''

    for i in range(65,91):
        alphabet += chr(i)

    return alphabet

# Function to reverse the order of the string
def rev_alph(alph):
    alph_new = ''
    for i in range(len(alph)-1,-1,-1):
        alph_new += alph[i]
    return alph_new

# Set up the constants:
QUISTION_SIZE = 5 # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30 # The quiz lastes 30 sec.

ALPHABET = alphabet()
REVERSE_ALPHABET = rev_alph(ALPHABET)


# Main loop

def main():
    # Fancy animation for the title:
    slowPrint(ALPHABET,0.05)
    slowPrint('\tAlphabetize Quiz',0.05)
    slowPrint(REVERSE_ALPHABET,0.05)
    time.sleep(0.5)

    print(f'''By Ishaan Jangid 'ishaanjangid035@gmail.com'
          Enter the alphabetical order f the letters shown as fast
          as possible. Try to alphetixe as many as possible in {QUIZ_DURATION} seconds!
          Example:
                P M O T Q <-- The letters.
                > mopqt   <-- Enter the correct alphabetical order.''')
    input("Press Enter to begin...")

    startTime = time.time() # Get the current time for the start time.
    numCorrect = 0 # Number of question answered correctly.
    
    # Main Game loop.
    while True:
        # Come up with letters for the questoin:
        quizLetters = random.sample(ALPHABET,QUISTION_SIZE)
        print(' '.join(quizLetters))
        response = input('> ').upper()
        response = response.replace(' ','') # Remove spaces.

        # Check if the quiz's time is up:
        if time.time() - 30 > startTime:
            print("TIME'S UP!")
            break

        # Check if the response is correct:
        if list(response) == sorted(quizLetters):
            print('\tCorrect!\n')
            numCorrect += 1 # Increase the sore by 1.

        else:
            print('\tSorry, worng. :(\n')

        # After the loop exits, the quiz is over. Show the final score:
        print(f"In {QUIZ_DURATION} seconds you.")
        print(f'got {numCorrect} correct!.')
        print("Tnx for playing!")
        


def slowPrint(text,pauseAmount=0.1):
    """Slowly print ou the characters in text one at a time."""
    for character in text:
        # Set flush = TRUE here do the text is immediately printed:
        print(character,flush=True,end='')
        time.sleep(pauseAmount)
    print()



if __name__ == "__main__":
    main()