
# Function to print aA-zZ

def abAB():
    x = [] 

    for i in range(97,123):
        x.append(chr(i))

    for i in range(65,91):
        x.append(chr(i))

    return x



lst = "In my AI engineering studies, I delve into complex data structures.".split()
punc_lst = []


for i in lst:    
    if i[-1] not in abAB():
        punc_lst.append(i)

print(punc_lst)
print(punc_lst[0][:-1])


