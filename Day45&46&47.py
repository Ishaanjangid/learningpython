
# Function that return a string of ALPHABET [a~z]
def alphabet():
    alphabet = ''

    for i in range(65,91):
        alphabet += chr(i)

    return alphabet
alph = alphabet()

print("Enter Text...")
text = input("> ")

print("Enter keys:")
keys = input('> ')
keyA, keyB = keys.split()

# Function to ask user to (e)ncrypt or (d)ecrypt the message.
def encryptOrDecryptMessage():
    '''ask user to encrypt or decrypt a message'''
    while True:
        print('''Type (e) to 'encrypt' or,
              (d) to 'decrypt'.''')

        mode = input('> ')

        if mode.lower().startswith('e'):
            # User want to encrypt the message
            myMode = 'encrypt'
        
        elif mode.lower().startswith('d'):
            # User want to dcrypt the message
            myMode = 'decrypt'

        else:
            print("INVALID INPUT!!!")
            continue

        return myMode

# Function to encrypt text
def encryptText(message,keyA,keyB):
    encryptic_txt = []

    for i in message.split():
        word = ''
        for j in i:
            
            letter_index = alph.index(j.upper())
            keyA,keyB=int(keyA),int(keyB)

            new_index = ((keyA * letter_index) + keyB) % 26

            word += alph[new_index]

        encryptic_txt.append(word)

    return (' '.join(encryptic_txt))

# Function to decrypt text
def decryptText(message,keyA,keyB):
    '''To decrypt the, encrypt text'''
    pass



# Function to find the HCF
def HCF(a,b):

    factor_a = []
    factor_b = []

    # Calculating factor of 'a'

    i = 2
    while i <= a:

        if a % i == 0:
            factor_a.append(i)
            a //= i
        else:
            i += 1


    # Calculating factor of 'b'
    
    i = 2

    while i <= b:
        if b % i == 0:
            factor_b.append(i)
            b //= i
        else:
            i += 1

    # Collecting the common factors

    common_factor = set(factor_a) & set(factor_b)

    hcf = 1

    for factor in common_factor:
        hcf *= factor

    
    return hcf

