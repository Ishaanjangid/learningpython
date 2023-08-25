import pyperclip
import random

# Note the space at the front of the SYMBOLS strings:
SYMOBOLS = """" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF""" + \
""""GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    print('''Affine Cipher, a simple substitution cipher''')

    # Let the user specifey if they are encrypting or decrypting:
    while True:  # Keep asking it until the user enter e or d
        print("Do you want to (e)ncrypt or (d)ecrypt?")

        response = input('> ').lower()

        if response.startswith('e'):
            myMode = 'encrypt'
            break

        elif response.startswith('d'):
            myMode = 'decrypt'
            break

        print("Please enter the letter 'e' or 'd'")
        print()


    # Let the user specifey the key to use:
    while True: # Keep asking until enters a valid key.
        print("Please specify the key to use,")
        print('or RANDOM to have one generated for you:')

        response = input('> ').lower()

        if response.startswith('r'):
            myKey = generateRandomKey()
            print(f"The key is {myKey}. KEEP THIS SECRET!")
            break
            
        else:
            if not response.isdecimal():
                print("The key is not a number.")
                continue

            if checkKey(int(response), myMode):
                myKey = int(response)
                break
        

    # Let the user specify the message to encrypt/decrypt:

    print(f'Enter the message to {myMode}')
    myMessage = input('> ')

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrpyt':
        translated = decryptMessage(myKey,myMessage)
    
    print(f'{myMode.title()} text:')
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' %(myMode))
    except:
        pass  # Do nothing


    


def encryptMessage(key, message):
    """Encrypt the message using the key."""

    checkKey(key,'encrypt')
    keyA, keyB = getKeyPartsFromKey(key)
    ciphertext = ''   # Variable to store encrypt meassage

    for symbol in message:
        if symbol in SYMOBOLS:
            # encrypt this symbol
            sysIndex = SYMOBOLS.find(symbol)  # finding the index of the symbol in SYMBOL
            newIndex = (sysIndex * keyA + keyB) % len(SYMOBOLS)  # Formula of affine cipher
            ciphertext += SYMOBOLS[newIndex]

        else:
            ciphertext += symbol # just append this symbol unencrypted

    return ciphertext

def decryptMessage(key,message):
    """Decrypt the message using the key."""
    checkKey(key, 'decrypt')
    keyA ,keyB = getKeyPartsFromKey(key)
    plaintext = '' # variable to store decrypt message

def findModInverse(a, m):
    """"Return the modular inverse of a % m, which is the number x
    such thet a*x % m = 1"""

    if HCF(a, m) != 1 :
        # No mid inverse exixt if a & m are not reletively prime:
        return None
    
    # Calculate using Extended Euclidean Algorithm:

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator

        v1, v2, v3, u1, u2, u3 = ((u1 - q * v1),
                                  (u2 - q * v2),
                                  (u3 - q * v3),
                                  v1, v2, v3)
        
        return u1 % m
    

def HCF(a, b):
    """Return the HIGHEST COMMON FACTOR of a and b using
    Euclid's Algorithm."""

    while a != 0:
        a, b = b % a , a

    return b

def getKeyPartsFromKey(key):
    """Get the two key A and key B parts from the key."""
    keyA = key // len(SYMOBOLS)
    keyB = key % len(SYMOBOLS)
    return (keyA,keyB)

def checkKey(key,mode):
    """Return true if key is a valid encryption key for this mode.
    Otherwise return False."""

    keyA, keyB = getKeyPartsFromKey(key)
    if mode == 'encrypt' and keyA == 1 and keyB == 0:
        print("This key effectiely does not do any encryption on the")
        print('message. Choose a different key.')
        return False

    elif keyA < 0 or keyB < 0 or keyB > len(SYMOBOLS) - 1:
        print("Key A must be greater than 0and key B must be between")
        print(f'0 and {len(SYMOBOLS) - 1}')
        return False

    elif HCF(keyA, len(SYMOBOLS)) != 1:
        print(f'Key A ({keyA}) and the symbol set')
        print(f'size ({len(SYMOBOLS)})')
        print('Choose a diffenrent key.')
        return False
    
    return True


def generateRandomKey():
    """Generate ans return a random encryption Key."""

    while True:
        keyA = random.randint(2,len(SYMOBOLS))
        keyB = random.randint(2,len(SYMOBOLS))

        if HCF(keyA, len(SYMOBOLS)) == 1:
            return keyA * len(SYMOBOLS) + keyB


if __name__ == '__main__':
    main()

