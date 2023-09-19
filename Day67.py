import re 

text = r'ROBOCOP protect the innocent.'

pattern = r'robocop'

match = re.findall(pattern,text,re.I)

print(match)
