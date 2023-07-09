import random

rand_values = random.randint(1,10)


for i in range(1,11):
    if i == rand_values:
        print("~",end = " ")
        continue
    print(i,end=" ")
print()
print()
## In 2d

lst = [[1,2,3],
       [4,5,6],
       [7,8,9]] 

for i in lst:
    for j in i:
        if j == rand_values:
            print("~",end="   ")
            continue
        print(j,end = "   ")

    print()
    print()