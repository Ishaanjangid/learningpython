import re, pyperclip 


# Creating phone regEx
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # seperator
                        (\d{3})                         # First 3 digits
                        (\s|-|\.)                       # seperator
                        (\d{4})                         # last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # separator
                        
                        
)''',re.VERBOSE)

# Creating Email RegEx

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9.%+-]+    # username
                        @                   # @ symbol
                        [a-zA-Z0-9.+-]+     # domain name
                        (\.[a-zA-Z]{2,4})   # dot-something
)''',re.VERBOSE)


# Find matches in the cipboard text.

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])

    if groups[8] != '':
        phoneNum += ' x' + groups[8]

    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy result to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Coipies to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone number or email address found.')

    