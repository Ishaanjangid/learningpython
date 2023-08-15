#! python 3

import sys
import pyperclip


# TEXT = {'agree': """Yes, I agree. That sound fine to me.""",
#         'busy': """"Sorry, can we do this later this week or next week?""",
#         'upsell': """Would you  consider this a monthly donation?"""}

# user = input("Type: ")


# if user.lower() in TEXT:
#     print("Yes")
#     pyperclip.copy(TEXT[user])
#     print(f"This message is copied for {user}")

# else:
#     if user.lower() == "show":
#         for i in TEXT:
#             print(i)
#         # print("it's SHOW")
        
#####################################################################################################################################

### program to copy a list and 
### a bullit point and space on it 


text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
