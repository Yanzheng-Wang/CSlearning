def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k

from math import sqrt
def if_(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
    
def real_sqrt(n):
    """Return the real square root of positive integer n.
       If n is not a perfect square, give an approximate value.

    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(9)
    3.0
    >>> real_sqrt(8)
    2.8284271247461903
    >>> real_sqrt(10)
    3.1622776601683795"""
    return if_(n>=0,sqrt(n),0)