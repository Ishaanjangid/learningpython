# These are function to encrypt and decrypt a word
# Not a sentence

# from AffineCypher import *

def alphabet():
    alphabet = []

    for i in range(65,91):
        alphabet.append(chr(i))

    return alphabet

def modular_inverse(a, m):
    try:
        inverse = pow(a , -1 , m)
        return inverse
    except:
        raise ValueError("Inverse does not exist for this pair of numbers.")

alph = alphabet()

def encryptText(word,keyA,keyB):
    '''To encrypt the plane text'''

    
    keyA,keyB=int(keyA),int(keyB)
      
    new_word = ''
    for i in word:        
            
        letter_index = alph.index(i.upper())
            

        new_index = ((keyA * letter_index) + keyB) % 26

        new_word += alph[new_index]

    
    return new_word


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