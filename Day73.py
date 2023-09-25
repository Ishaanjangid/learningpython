# This is my take on the 
# Phone number and email exerector program

import re

# First I need to make a regex to find PHONE number 

text = '''My number is 323-432-4354
My friend number is (342)-342-4322
My friend number is 434-5432'''

phoneRegEx = r'\d{3}|\(\d{3}\)\s|-|\.\d{3}\s|-|\.\d{4}'

matches = re.findall(phoneRegEx,text)

print(matches)

