### This program find the given value and tell the index
### This works for 2 iteration

lst = list([1,2,3,4,1,2,3,1])


# value = int(input("Enter Value: "))
# counter = 0 
# for i in range(len(lst)):
#     if value in lst:
#         counter += lst.index(value)
#         # print(lst.index(value))
#         print(counter)
        
#         lst.remove(value)
#         counter + 1
#     else:
#         break
# print("Done")



# counter = 0

# while True:
#     if value in lst:
#         counter += lst.index(value)
#         # print(lst.index(value))
#         print(counter)
#         lst.remove(value)
#         counter + 1

#     else:
#         break


### This program will remove every occerence 
### Of the "Value" from the list.

# while True:
#     if value in lst:
#         lst.remove(value)

#     else:
#         break

# print(lst)


### Question 1

# my_lst = [1,2,3,4]
# value = eval(input("Enter: "))

# if type(value) == type([]):
#     my_lst.append(value)

# elif type(value) == type(1):
#     my_lst.extend(my_lst)

# else:
#     print("Enter a valid INPUT!")


### Question 2
lst = [43,4,3,5432,43,4235,54,3,434,534,543,543,5,435,45,435,]

# print("1. Delete using values")
# print("2. Delete using index")
# print("3. Delete a subset")

# option = int(input("Enter: "))

# if option == 1:
#     value = int(input("Enter the value: "))
#     lst.remove(value)
#     print(lst)
    
# elif option == 2:
#     index = int(input("Enter the index: "))
#     del lst[index]
#     print(lst)

# elif option == 3:
#     start = int(input("Enter start value: "))
#     stop = int(input("Enter stop value: "))

#     del lst[start:stop]
#     print(lst)


# else:
#     print("INVALID INPUT !!!")

### Question 3

enter_lst = eval(input("Enter list: "))

# print(f"Original List",enter_lst)
# double_lst = enter_lst*2

# print("Replicated list",double_lst)

# double_lst.sort()

# print(double_lst)

### Question 4

# min_ele = enter_lst[0]
# min_inx = 0

# for index,item in enumerate(enter_lst):
#     if enter_lst[index] < min_ele:
#         min_ele = enter_lst[index]
#         min_inx = index

# print(f"Element: {min_ele}")
# print(f"Index: {min_inx}")


### Question 5

# sum = 0 

# for index,item in enumerate(enter_lst):
#     sum += item

# print(f"Mean: {sum/len(enter_lst)}")

### Question 6

# length  = len(enter_lst)

# max = max(enter_lst)
# max_inx = enter_lst.index(max)

# if max_inx <= (length/2):
#     print("It lie in the first half")
# else:
#     print("It lie in the second half")

print("Enter list",enter_lst)
print("Reverse",enter_lst[::-1])