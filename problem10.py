# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:16:17 2021

@author: Benjamin
"""

# Find the sum of all the primes below two million.

def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]


Answer = sum(sieve(2000000))
print(Answer)