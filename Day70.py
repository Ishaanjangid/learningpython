import re

text = '''Ishaan: 453-543-5321,
Kartik: 453-543-6433,
Rajvir: 564-564-6544'''

pattern = r'''[A-Za-z]+:'''

match = re.findall(pattern,text,re.VERBOSE)
print(match)