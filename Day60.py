import re

# This is the Day-2 of learning regEX

text = '''Ishaan
Jangid
'''

pattern = r'\n'

match = re.search(pattern,text)

print(match)