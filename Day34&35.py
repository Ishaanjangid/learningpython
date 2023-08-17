
# Day34.py - This is a ENGLISH-PIG_LATIN converter


### Rules of pig-latin
# 1. If a word start with vowals (a,e,i,o,u) then add 'way' at the end.
# 2. if a word start with consonant or consonant cluster then
# put the world ant the end and add 'ay'.


# Variable
vowel = tuple('aeiou')

# This take user input
sentence = input("Enter: ")

# Convert the sentence in list
words = sentence.split()


# Main program section
sentence_new = []

for i in range(len(words)):

    # check if the word start with a vowel
    if words[i].lower().startswith(vowel):
        words[-1] = 'yay'
        sentence_new.append(words[i] + words[-1])
    
    # check if the word start with consonent / consonent cluster
    else:

        # check if the word have a consonent cluster
        if words[i][0].lower() not in vowel and words[i][1].lower() not in vowel:

        
            sentence_new.append(words[i][2:]+words[i][0:2]+'ay')

        # Check if there is only on consonent
        else:
            if words[i][0].lower() not in vowel:
                
                sentence_new.append(words[i][1:]+words[i][0]+'ay')
        

# Join the list in a sentence
sentence = ' '.join(sentence_new)
print(sentence)
