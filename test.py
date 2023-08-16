x = 'This is Ishaan Jangid'.split()

vowel = tuple('aeiou')

# for i in x:
#     # print(i.startswith(not vowel,0,1))
#     for j in i:
#         print(j)
#         if j[0].lower() not in vowel :
#             print('Yes')
#         else:
#             print('no')
#     print()

new_lst = []

for i in x:

    print(i)
    if i[0].lower() not in vowel and i[1].lower() not in vowel:        
        
        new_lst.append(i[2:]+i[0:2]+'ay')


    else:
        if i[0].lower() not in vowel:
            
            new_lst.append(i[1:]+i[0]+'ay')

print(new_lst)