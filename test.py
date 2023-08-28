import random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF""" + \
          """GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def genarateRandomKey():
    """Generate and return a random encrypted key."""

    # while True:
    keyA = random.randint(2,len(SYMBOLS))
    keyB = random.randint(2,len(SYMBOLS))

    return keyA,keyB

a,b = genarateRandomKey()
# print(genarateRandomKey())
print(a)
print(b)
