# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:21:29 2021

@author: Benjamin
"""

# How many, not necessarily distinct, values of nCHOOSEr for 1 <= n <= 100 are greater than one-million?
import scipy.special

def least_r_over_mil(n: int) -> int:
    for i in range(3, int((n+1)/2)):
        combs = scipy.special.comb(n,i)
        if combs > 1000000:
            return i
    return 0

bigs = 0
for n in range(23,101):
    r = least_r_over_mil(n)
    if r > 0:
        b = 2*((n/2)-r)+1
        bigs += b

Answer = bigs
print(Answer)