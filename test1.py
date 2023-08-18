def abAB():
    x = [] 

    for i in range(97,123):
        x.append(chr(i))

    for i in range(65,91):
        x.append(chr(i))

    return x

# Variable
vowel = tuple('aeiou')

# This take user input
sentence = input("Enter: ")

# Convert the sentence in list
words = sentence.split()


# Main program section
sentence_new = []
punc_lst = []

for i in range(len(words)):

    # check if the word start with a vowel
    if words[i].lower().startswith(vowel):
        # check if the word end with puncuation (',','.' so on)
        for i in words:
            if [-1] not in abAB():
                punc_lst.append()

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

