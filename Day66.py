# Learning regular expression 

import re

text = "Hello,World"
text1 = 'World,Hello'
text2 = 'HiHello'

pattern = r"Hello$"

match = re.findall(pattern,text)
match1 = re.findall(pattern,text1)
match2 = re.findall(pattern,text2)

print(match)
print(match1)
print(match2)
