# This is the main file were I will the 
# write the code of AFFINE CYPHER.

# Name = Day45,46,47,48,50.py


def alphabet():
    alphabet = []

    for i in range(65,91):
        alphabet.append(chr(i))

    return alphabet

alph = alphabet()

# Function that ask user to enter keys
def enterKey():
    '''Ask user to enter key's'''
    print("Enter keys:")
    print('For Example: 4, 5')
    keys = input('> ')
    keyA, keyB = keys.split(',')

    return int(keyA),int(keyB)

# Function to check if the enter key's are VAILD
def checkKey(keyA,keyB,mode):
    '''Check if the entered KEY's are valid or not'''

    if mode == 'encrypt' and keyA == 1 and keyB == 0:
        print("This key effectively does not do any encrypt on the")
        print("message. Choose a different key.")
        return False
    
    elif keyA < 0 or keyB < 0 or keyB > len(alph) - 1:
        print('Key A must be greater than 0 and key B must be between')
        print(f'0 and {len(alph-1)}')
        return False

    elif HCF(keyA,len(alph)) != 1:
        print(f'Key A ({keyA}) and the symbol set')
        print(f'size ({len(alph)}) are not relatively prime.')
        print('Choose a different key.')
        return False

    return True

# Function to ask user to (e)ncrypt or (d)ecrypt text
def encryptOrDecryptMessage():
    '''ask user to encrypt or decrypt a message'''
    while True:       
        print()
        print("Type (e) to 'encrypt' or,")
        print("(d) to 'decrypt'.")
        
        mode = input('> ')

        if mode.lower().startswith('e'):
            # User want to encrypt the message
            myMode = 'encrypt'
            return myMode
        
        elif mode.lower().startswith('d'):
            # User want to decrypt the message
            myMode = 'decrypt'
            return myMode

        
        print('INVALID INPUT!!!')
            
# Function to encrypt text
def encryptText(word,keyA,keyB):
    '''To encrypt the plane text'''

    
    keyA,keyB=int(keyA),int(keyB)
      
    new_word = ''
    for i in word:        
            
        letter_index = alph.index(i.upper())
            

        new_index = ((keyA * letter_index) + keyB) % 26

        new_word += alph[new_index]

    
    return new_word

# Function to decrypt text
def decryptText(word,keyA,keyB):
    '''TO decrypt the encrypt text.'''

    keyA,keyB=int(keyA),int(keyB)
    new_word = ''
    
    # Finding the inverse of KeyA
    inverseKeyA = modular_inverse(keyA,len(alph))

    for i in word:
        
        letter_index = alph.index(i.upper())
        new_index = (letter_index - keyB) * inverseKeyA  % len(alph) 

        new_word += alph[new_index]

    return new_word

# Function to find the HCF
def HCF(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find modular Inverse
def modular_inverse(a, m):
    try:
        inverse = pow(a , -1 , m)
        return inverse
    except:
        raise ValueError("Inverse does not exist for this pair of numbers.")

# Function to ask user to PLAY AGAIN!
def playAgain():
    print("Do you want to play Again?[y, n]")

    option = input('> ')
    
    if option.lower().startswith('y'):
        return True
    else:
        return False

# Main Loop
while True:

    # Asking user to enter the message
    print("Enter message...")
    message = input('> ')

    # Asking user to encrypt or decrypt the message
    myMode = encryptOrDecryptMessage()
    
    # Asking user to enter key's
    while True:
        # Enter key
        keyA,KeyB = enterKey()

        if checkKey(keyA,KeyB,myMode):
            # if True mean VALID KEY'S
            break

        print('INVALID KEYS')
        print()
            
    # encrypting the message
    plane_word = []
    
    for word in message.split():
        crypto_txt = ''

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
        if myMode.lower().startswith('e'):
            # Then encrypt the message
            crypto_txt += encryptText(word,keyA,KeyB)
        else:
            # Then decrypt the message
            crypto_txt += decryptText(word,keyA,KeyB)

        # Set the word back to uppercase or title case:

        if wasUpper:
            word = crypto_txt.upper()

        if wasTitle:
            word = crypto_txt.title()

        # Add the non-letters back to the start or end of the word.

        plane_word.append(prefixNonLetters + crypto_txt + suffixNonLetters)

    # Join all the words back together into a single string:
    sentence = ' '.join(plane_word)

    print(sentence)
    
    if playAgain():
        continue

    break


    