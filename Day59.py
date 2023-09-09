# From now I am starting regular expression :->

import re

pattern = 'i'

text = '''In the vast world of AI and programming, every line of code we write is a step closer to
        mastering the craft. As a dedicated student pursuing engineering in Artificial Intelligence,
        your journey is filled with opportunities to learn, create, and innovate. Keep your passion for
        coding burning bright, for it is the path to becoming the best programmer you aspire to be.'''

# Simple way
# dic = {}
# for i,v in enumerate(text):
#     dic.

# RE way

match = re.search(pattern,text)
# print(match)

dic = dict('1;2')
print(dic)