# This is the main file were I will the 
# write the code of AFFINE CYPHER.


def alphabet():
    alphabet = []

    for i in range(65,91):
        alphabet.append(chr(i))

    return alphabet

alph = alphabet()

print("Enter Text...")
text = input("> ")

# Function that ask user to enter keys
def enterKey():
    '''Ask user to enter key's'''
    print("Enter keys:")
    print('For Example: 4, 5')
    keys = input('> ')
    keyA, keyB = keys.split(',')

    return keyA,keyB

# Function to check if the entee key's are VAILD
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
    '''ask user to ncrypt or decrypt a message'''
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
def encryptText(message,keyA,keyB):
    '''To encrypt the plane text'''

    encrypt_txt = []
      
    for i in message.split():
        word = ''
        for j in i:
            
            letter_index = alph.index(j.upper())
            keyA,keyB=int(keyA),int(keyB)

            new_index = ((keyA * letter_index) + keyB) % 26

            word += alph[new_index]

        encrypt_txt.append(word)

    return (' '.join(encrypt_txt))  

# Function to decrypt text
def decryptText(message,keyA,keyB):
    '''To decrypt the encrypted test'''
    
    decrypt_txt = []

# Function to find the HCF
def HCF(a,b):
    '''To find the HCF of given two(2) number's'''

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

