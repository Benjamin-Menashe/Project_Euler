# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:24:19 2021

@author: Benjamin
"""

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

counts = 0
i = 1

nmin2 = 1
nmin1 = 1

dmin2 = 0
dmin1 = 1

while i <= 1000:
    numer = 2*nmin1 + nmin2
    a = len(str(numer))
    nmin2 = nmin1
    nmin1 = numer
    
    denom = 2*dmin1 + dmin2
    b = len(str(denom))
    dmin2 = dmin1
    dmin1 = denom
    
    if a > b:
        counts += 1
    
    i += 1

Answer = counts
print(Answer)