import re

text = 'Ishaan'
pattern = r'I.....n'

match = re.findall(pattern,text)

print(match)