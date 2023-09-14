import re

# # Regular expression

# print("Enter Number: ")
# text = input('> ')


# def isNumber(text):
#     if len(text) != 12:
#         return False
    
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
    
#     if text[3] != '-':
#         return False
    
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
    
#     if text[7] != '-':
#         return False
    
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
    
#     return True
    
# print(isNumber(text))



pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

phoneNumRegex = re.compile(pattern)

mo = phoneNumRegex.search('My Number is 456-456-6536')

print('Phone Number Found',mo.group())