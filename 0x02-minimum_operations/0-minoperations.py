#!/usr/bin/python3
""" 0-minoperations """
from typing import List


def is_prime(n: int) -> bool:
    """ return true if @n is prime else false """
    if n <= 1:
        # 1 and negative numbers are not prime
        return False
    elif n <= 3:
        # 2 and 3 are prime
        return True
    elif n % 2 == 0 or n % 3 == 0:
        # Numbers divisible by 2 or 3 are not prime
        return False
    else:
        # Check for factors of the form 6k ± 1 up to the square root of n
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


def prime_factors(n: int) -> List[int]:
    """ returns the prime factors of @n """
    factors = []
    # Check for factors of 2 first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for factors of odd numbers up to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is greater than 2 and not yet included in the factors list,
    # it must be prime
    if n > 2:
        factors.append(n)
    return factors


def minOperations(n: int) -> int:
    """ returns the minimum operations if possible or 0 o.w. """
    if is_prime(n) or n < 1:
        return 0
    else:
        return sum(prime_factors(n))
