'''This part of code check that, How to make a Function 
that have the capability to take the HCF of two(2) numbers'''

def calculate_hcf(a,b):
    '''Function that calculate hcf'''

    factors_a = []
    factors_b = []

    # Calulate the prime factor of 'a'

    i = 2
    while i <= a:
        if a % i == 0:
            factors_a.append(i)
            a //= i

        else:
            i += 1

    # Calculate the prime factor of 'b'

    i = 2
    while i <= b:
        if b % i == 0:
            factors_b.append(i)
            b //= i
        else:
            i += 1

    
    # Finding the common part 

    common_factor = set(factors_a) & set(factors_b)

    hcf = 1

    for factor in common_factor:
        hcf *= factor

    
    return hcf

