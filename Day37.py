# English - PIG-Latin (will follow source code)

# English to pig Latin
message = input("English message: ")

VOWELS = tuple('aeiouy')  # Constant value

piglatin = []  # list to store translated words

# main program loop

for word in message.split():

    
    # Seprate the non-letters at the start of the word:
    prefixNonLetters = '' # variable to store non-letters at the start of the word

    # Check if the start of the word is non-letter 
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0] # add that word to 'prefixNonLetter'
        word = word[1:]  

    if len(word) == 0:
        
        piglatin.append(prefixNonLetters)
        continue

    
    # Seprate the non-letters at the end of the word:
    suffixNonLetters = ''

    while not word[-1].isalpha():
        suffixNonLetters +=  word[-1]
        word = word[:-1]

    # Rembember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lower case for translation


    # Seprate the consonants at the start of this word:

    prefixConsonants = ''

    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]

        word = word[1:]

    # Add the Pig Latin ending to the word:

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add the non-letters back to the start or end of the word.

    piglatin.append(prefixNonLetters+word+suffixNonLetters)


# joining th word

print(' '.join(piglatin))








     


