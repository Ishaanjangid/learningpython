# Modular Inverse

# def modular_inverse(a, m):
#     try:
#         inverse = pow(a , -1 , m)
#     except:
#         raise ValueError("Inverse does not exist for this pair of numbers.")


def HCF(a,b):
    '''To find the HCF of given two(2) number's'''

    factor_a = []
    factor_b = []

    # Calculating factor of 'a'

    i = 2
    while i <= a:

        if a % i == 0:
            factor_a.append(i)
            a //= i
        else:
            i += 1


    # Calculating factor of 'b'

    i = 2

    while i <= b:
        if b % i == 0:
            factor_b.append(i)
            b //= i
        else:
            i += 1

    # Collecting the common factors

    common_factor = set(factor_a) & set(factor_b)

    hcf = 1
    for factor in common_factor:
        hcf *= factor

    return hcf

def findModInverse(a, m):
    """Return the modular inverse of a % m, which is the number x such
    that a*x % m = 1"""

    if HCF(a, m) != 1:
        # No mod inverse exists if a & m aren't relatively prime:
        return None

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = ((u1 - q * v1),
                                  (u2 - q * v2),
                                  (u3 - q * v3),
                                  v1, v2, v3)
    return u1 % m

inverse = findModInverse(3, 11)

if inverse is not None:
    print(f"The modular inverse of {3} mod {11} is {inverse}")

else:
    print("Does not exist")