import random

spam = ['cat','bat','rat','elephent']

# print(spam)

# for i in range(-1,-5,-1):
#     print(spam[i])

# print(spam[1:3])

# print(spam[:-1])
# print(spam[1:])
# print(spam[:])

# print(spam)
# del spam[2]
# print(spam)

# del spam[0]

# print(spam)

# del spam
# print(spam)

# cat_name = []


# while True:
#     name = input("Enter cat name: ")

#     if name == 'q':
#         break

#     cat_name.append(name)

    


# print(cat_name)


# option = ["YES","NO"]

# ans = input("Enter: ")

# if ans.upper() not in option:
#     print("NO it is not present")

# else:
#     print("Present")


# for i in range(len(spam)):
#     print(f"Item:{i}, Value:{spam[i]}")

# for index,item in enumerate(spam):
#     print(f"Index: {index}, Value:{item}")



### Random module in list



# while True:
    
#     if spam == random.shuffle(spam):
#         print("Done")
#         break
#     else:
#         continue
# print("Congrulation!!!")

### Method in list

# print(spam)
# spam.insert(2,"Ishaan")
# print(spam)
# spam.insert(1,"Kartik")
# print(spam)

# spam.remove("Kartik")
# print(spam)
# spam.remove("Ishaan")
# print(spam)

# print(spam) 
# spam.sort(reverse=True)   ### This method do not create a new list they just do the change in the original list
# print(spam)

# lst = ['a','v','r','j','t']


# lst_new = ['A','V','R','J','T']


# new_lst = lst + lst_new

# new_lst = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# print(new_lst)
# new_lst.sort(key=str.lower)
# print(new_lst)



### Slicing a list 


lst = [1,2,3,4,5,6,7,8,9,0]


# new_lst = lst[lst[3:5]]

# print(new_lst)


lst = [54,6,53,"Ishaan",'spam',32,0]


# print(lst.index(53))
# print(lst.index("spam"))

new_lst = [65,45,64]


lst.extend(new_lst)

print(lst)
