import re

text = 'RoboCop eats baby food. BABY FOOD.'

pattern = r'[^aeiouAEIOU]+'

match = re.findall(pattern,text)

print(match)