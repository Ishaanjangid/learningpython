# Testing for random sample

import random

def alphabet():
    alphabet = ''

    for i in range(65,91):
        alphabet += chr(i)

    return alphabet
alph = alphabet()
print(alph)
print(random.sample(alph,5))
response = input('> ').upper()
response = response.replace(' ','')
print(response)
