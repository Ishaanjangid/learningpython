lst = []

message = input("Enter message: ")

for word in message.split():
    # Seprate the non-letters zt the start of this word:

    prefixNonLetters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    
    if len(word) == 0 :
        lst.append(prefixNonLetters)
        continue


print(lst)
print(prefixNonLetters)

