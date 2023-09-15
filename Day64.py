import re

# Compiling the regular expression

pattern = r'Bat(wo)?man'

text = '''The Advanture of Batman.
        The Advanture of Batwman.
        The Advanture of Batwoman.'''

search = re.search(pattern,text)

print(search.group())