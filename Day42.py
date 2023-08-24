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

main()

