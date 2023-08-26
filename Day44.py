
alphabet = []

for i in range(65,91):
    alphabet.append(chr(i))

print("Enter Text...")
text = input("> ")

print("Enter keys:")
keys = input('> ')
keyA, keyB = keys.split()

cryptic_text = ''
for i in text:
    letter_index = alphabet.index(i.upper())
    keyA,keyB=int(keyA),int(keyB)

    new_index = ((keyA * letter_index) + keyB) % 26

    cryptic_text += alphabet[new_index]

print(cryptic_text)