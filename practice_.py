# This file I will practice IF & ELSE


### Question 1

# while True:

#     input_percent = float(input("Enter percentage: "))

#     if input_percent > 100:
#         print("Enter Valid Input")
#         continue

#     else:
#         if input_percent > 90:
#             print("Grade : A")
#             break

#         elif input_percent > 80 and input_percent <= 90 :
#             print("Grade : B")
#             break
#         elif input_percent >= 60 and input_percent <= 80:
#             print("Grade : C")
#             break
#         elif input_percent < 60:
#             print("Grade : D")
#             break

### Question 2

# cost_price = float(input("Enter Cost Price: "))

# if cost_price > 100000:
#     print("Tax 15% - ",end= "")

#     print(f"{cost_price*(15/100)}")


# elif cost_price > 50000 and cost_price <= 100000:
#     print("Tax 10% - ",end = "")
#     print(f"{cost_price*(10/100)}")

# elif cost_price <= 50000:
#     print("Tax 5% - ",end="")
#     print(f"{cost_price*(5/100)}")

### Question 3

# year = int(input("Enter Year: "))

# if year % 4 == 0:
#     print(f"{year} is Leep Year")

# else:
#     print(f"{year} is not a Leep Year")

### Queestion 4

# spam = 1

# while spam < 11:
#     print(spam)

#     spam += 1

### Question 5

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end = "")
#     print()

### Question 6

# sum = 0
# input_num = int(input("Enter Number: "))

# for i in range(1,input_num+1):
#     sum += i

# print(f"Sum: {sum}")


### Question 7

# lst = []
# num = 2
# for i in range(1,11):
#     lst.append(num*i)

# print(lst)


### Question 8

# import random

# lst = []

# for i in range(1,11):
#     lst.append(random.randint(100,600))

# print(lst)

# # lst = [12, 75, 150, 180, 145, 525, 50]



# for i in lst:

#     if i >500:
#         break

#     if i >150 :
#         continue

#     if i % 5 == 0:
#         print(i)

### Question  9 


# lst = [10,20,30,40,50]

# size = len(lst) - 1 

# for i in range(size,-1,-1):
#     print(lst[i])

### Question 10

for i in range(-10,0,1):
    print(i)    