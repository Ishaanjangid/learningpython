
# This file contain the program 
# To remove the extra symbol of a word 
# Like (, . ! @ # ...) and number's 


print("Enter message:")
message = input('> ')

plane_word = []
for word in message.split():

    # Seprate the non-letter at the start of the text
    prefixNonLetters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        plane_word.append(prefixNonLetters)
        continue

    # Seprate the non-letter at the end of the text
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Rembember if the word was in upperCase or title Case.

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # make the word lowercase for translation.

    # modifing the letter's
    word += 'xxx'

    # Set the word back to uppercase or title case:

    if wasUpper:
        word = word.upper()

    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.

    plane_word.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
crypto_txt = ' '.join(plane_word)