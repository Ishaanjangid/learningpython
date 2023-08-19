
message = input("English message: ")

VOWELS = tuple('aeiouy')  # Constant value

piglatin = []  # list to store translated words

for word in message.split():

    prefixConsonants = []
    word = word.lower()
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants.append(word[0])

        word = word[1:]
        print(word)
print(prefixConsonants)