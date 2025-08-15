from math import sqrt
from math import isqrt

def is_prime(n):

    if n ==1:
        return False

    for i in range(2, isqrt(n)+ 1):
        if n%i == 0:
            return False
        
    return True


print(isqrt(16))