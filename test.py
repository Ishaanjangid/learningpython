
# Testing for removing (, . ! @) 
# Extra symbol from the start and end of the message

print("Enter message:")
message = input('> ')

plane_word = []
for word in message.split():
    # Seprate the non-letter at the start of the text
    prefixNonLetters = ''

    while len() > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(wor)