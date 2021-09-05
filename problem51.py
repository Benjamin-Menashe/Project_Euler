# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:11:24 2021

@author: Benjamin
"""

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# %% function to make Primes
def sieve(n: int) -> list:
    """
    Sieve away and only primes are left.
    """
    primes = 2*[False] + (n-1)*[True]
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]

# %% function to replace all instance of a with b in number
def rep_dig(a: int, b: int, num: int) -> int:
    stringy = str(num)
    new = str.replace(stringy, str(a), str(b))
    return int(new)

# %% function to check all replacements or numbers
def prime_buddies8(n: int) -> bool:
    strike = 0
    if '0' in str(n):
        for j in range(1,10):
            new = rep_dig(0,j,n)
            if new not in prms:
                strike += 1
            if strike == 3:
                return False
        return True
    elif '1' in str(n):
        strike = 1
        for j in range(2,10):
            new = rep_dig(1,j,n)
            if new not in prms:
                strike += 1
            if strike == 3:
                return False
        return True
    elif '2' in str(n):
        strike = 2
        for j in range(3,10):
            new = rep_dig(2,j,n)
            if new not in prms:
                strike += 1
            if strike == 3:
                return False
        return True
    else:
        return False

# %%
prms = sieve(1000000)
x = False
win = 'no such numbah here'
i = 5683 # index of smallest with 7 buddies

while x == False:
    x = prime_buddies8(prms[i])
    if x == True:
        win = prms[i]
    i += 1
    if i == len(prms): # out of while loop
        x = 10
    
Answer = win
print(Answer)
    
