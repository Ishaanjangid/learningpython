lst = []

vowels = tuple('aeiouy')

message = input("Enter message: ")

for word in message.split():
    # Seprate the non-letters zt the start of this word:

    prefixNonLetters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0 :
        lst.append(prefixNonLetters)
        continue


    # Seprate the non-letters at the end of the word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] 
        word = word[:-1]


    # Remember if the word is uppercase or title case.

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''

    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]

    # Adding the Pig Latin ending to the word:

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    lst.append(prefixNonLetters + word +suffixNonLetters)

# Join all the words back together int a single string:
print(' '.join(lst))

    


print(lst)
print(prefixNonLetters)

