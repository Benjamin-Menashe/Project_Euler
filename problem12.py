# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:40:49 2021

@author: Benjamin
"""
# What is the value of the first triangle number to have over five hundred divisors?

def tau(n):
        sqroot,t = int(n**0.5),0
        for factor in range(1,sqroot+1):
                if n % factor == 0:
                        t += 2 # both factor and N/factor
        if sqroot*sqroot == n: t = t - 1 # if sqroot is a factor then we counted it twice, so subtract 1
        return t
    
n = 1
z = 1
while z < 500:
    n += 1
    z = tau((n*(n+1))/2)
    
    
Answer = int((n*(n+1))/2)
print(Answer)