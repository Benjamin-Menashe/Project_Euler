# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 11:05:42 2021

@author: Benjamin
"""

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


import numpy as np

def lpf_odd(num):
    i = 3
    while i <= np.sqrt(num):
        if num % i == 0:
            return i
        else:
            i=i+2
    if i > np.sqrt(num):
        return num
       
x = 600851475143
cands = []

while x != 1:
    d = lpf_odd(x)
    cands.append(d)
    x = x/d

cands = np.array(cands)    
Answer = int(cands.max())
print(Answer)
