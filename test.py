def HCF(a, b):
    """Return the HIGHEST COMMON FACTOR of a and b using
    Euclid's Algorithm."""

    while a != 0:
        a, b = b % a , a

    return b

name = 'IshaanI'

x = name.find('I')
print(x)
