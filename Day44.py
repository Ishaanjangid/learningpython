def alphabet():
    alphabet = []

    for i in range(65,91):
        alphabet.append(chr(i))

    return alphabet

alph = alphabet()


print("Enter Text...")
text = input("> ")

print("Enter keys:")
keys = input('> ')
keyA, keyB = keys.split()

cryptic_text = ''
for i in text:
    letter_index = alph.index(i.upper())
    keyA,keyB=int(keyA),int(keyB)

    new_index = ((keyA * letter_index) + keyB) % 26

    cryptic_text += alph[new_index]

print(cryptic_text)