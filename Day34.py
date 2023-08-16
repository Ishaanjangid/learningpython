
# Day34.py - This is a ENGLISH-PIG_LATIN converter


### Rules of pig-latin
# 1. If a word start with vowals (a,e,i,o,u) then add 'way' at the end.
# 2. if a word start with consonant or consonant cluster then
# put the world ant the end and add 'ay'.


sentence = input("Enter: ")
words = sentence.split()

vowel = tuple('aeiou')

for word in words:
    if word.lower().startswith(vowel):
        print(f"Start with Vowels: {word}")
    else:
        print(f"Don't start with vowels: {word}")