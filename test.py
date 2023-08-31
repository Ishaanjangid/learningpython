keyA = 3
def alphabet():
    alphabet = []

    for i in range(65,91):
        alphabet.append(chr(i))

    return alphabet

alph = alphabet()

print('Key A ({}) and symbol set'.format(keyA))
print('size ({}) are not relatively prime.'.format(len(alph)))
