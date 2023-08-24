def gcd(a, b):
    """Return the greatest common Divisor of a and b using
    Euclid's Algorithm."""

    while a != 0:
        a, b = b % a , a

    return b


print(gcd(6,12))