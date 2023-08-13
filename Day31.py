### String method's
import pyperclip


name = "This Is NOT Title Case"
# print(name.isalpha())
# print(name.isalnum())
# print(name.isdecimal())
# print(name.isspace())
# print(name.istitle())

### startwith() ans endswith()

# while True:
#     spam = input("Enter [yes,no]: ")

#     if spam.lower().endswith('o'):
#         print("ERROR!!!")
#         continue

#     if spam.lower().startswith('y'):
#         break
    
#     else:
#         print("ERROR!!!")

# print("Done:-)")

### join()

def designLine(indent,spaces,char):
    lst = [''*indent]*spaces


    value = char.join(lst)
    print(value)


### split()

# value = """This is your,
# friend Ishaan.
# I am in class XII"""

# # print(value.split('\n'))

# ### partition()

# print(value.partition('\n'))


### rjust(), ljust(), center()

# x = 'Hello'
# print(x.center(20,'='))

classDict = {"Class IX":32,'Class X': 43,"Class XI":45,'ClassXII':54}

def printClass(itemDict,leftWidth,rightWidth):
    print("Class Student Number".center(leftWidth+rightWidth,'-'))

    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))


### pyperclip module

print(pyperclip.paste())