import re

text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarters i.e. FY2020 Q4 it was $3 billion.
fy2020 Q3'''

pattern = r'FY\d{4} Q[1-4] | \$[\d.]+'

match = re.findall(pattern,text,flags=re.I)

print(match)

# Question 1
# https:\/\/twitter\.com\/|[0-9]|_[a-z]+

# Question 2
# Concentration of Risk:([^\n]+)