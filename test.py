'''This part of code check's the KEY part in 
the github code by AL SWEIGERT'''


# import random

# SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF""" + \
#           """GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

# def HCF(a,b):
#     factor_a = []
#     factor_b = []

#     # Calculating factor of 'a'

#     i = 2
#     while i <= a:

#         if a % i == 0:
#             factor_a.append(i)
#             a //= i
#         else:
#             i += 1


#     # Calculating factor of 'b'
    
#     i = 2

#     while i <= b:
#         if b % i == 0:
#             factor_b.append(i)
#             b //= i
#         else:
#             i += 1

#     # Collecting the common factors

#     common_factor = set(factor_a) & set(factor_b)

#     hcf = 1

#     for factor in common_factor:
#         hcf *= factor

    
#     return hcf

# def genarateRandomKey():

#     """Generate and return a random encrypted key."""

#     while True:
#         keyA = random.randint(2,len(SYMBOLS))
#         keyB = random.randint(2,len(SYMBOLS))

#         if HCF(keyA,len(SYMBOLS)) == 1:
#             # print(f"KeyA: {keyA}")
#             # print(f"len(SYMOBOL): {len(SYMBOLS)}")
#             # print(HCF(keyA,len(SYMBOLS)))
#             return keyA * len(SYMBOLS) + keyB

# def getKeyPartsFromKey(key):
#     """Get the two key Parts form the KEY."""
#     keyA = key // len(SYMBOLS)
#     keyB = key // len(SYMBOLS)

#     return (keyA,keyB)


# # a,b = genarateRandomKey()
# key = genarateRandomKey()
# print(key)
# print(getKeyPartsFromKey(key))
# # print(a)
# # print(b)


### Function to check if the key's are valid or not...

def checkKey(keyA, keyB,mode):
    '''Check If the key's are valid or not'''

    if mode == 'encrypt' and keyA == 1 and keyB == 0:
        print("This key effectively does not do any encryption on the")
        print("message. Choose a different key.")

        return False
    
    elif keyA < 0 or keyB < 0 or 