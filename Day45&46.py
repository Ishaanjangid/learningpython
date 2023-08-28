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

cryptic_txt = []


for i in text.split():
    word = ''
    for j in i:
        
        letter_index = alph.index(j.upper())
        keyA,keyB=int(keyA),int(keyB)

        new_index = ((keyA * letter_index) + keyB) % 26

        word += alph[new_index]

    cryptic_txt.append(word)

print(' '.join(cryptic_txt))        