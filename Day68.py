import re

text = '''Ishaan: $100,
Aaradhya: €50,
Rajvir: ¥2000'''
pattern = r'[$€¥]\d+'

match = re.sub(pattern,'AMOUNT',text,re.VERBOSE)

print(match)
