import copy

### List

spam = [1,2,3,[4,5],6]

cheese = copy.copy(spam)

print("The original element before deep copying")

for index,item in enumerate(spam):
    print(f"Index:{index},Item:{item}")

print("\r")

cheese[3][0] = "x"

print("The new list after deep copying")
for index,item in enumerate(cheese):
    print(f"Index:{index},Item:{item}")

print("\r")

print("The original element after deep copying")
for index,item in enumerate(spam):
    print(f"Index:{index},Item:{item}")




# ### Integer

# spam = 10

# cheese = spam

# spam = 9
# print(spam,id(spam))
# print(cheese,id(cheese))

# ### String

# spam = "Hello"

# cheese = spam

# spam = "World"
# print(spam,id(spam))
# print(cheese,id(cheese))

# spam = "Ishaan"

# print(id(spam))



