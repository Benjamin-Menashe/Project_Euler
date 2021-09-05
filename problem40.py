# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 09:53:36 2021

@author: Benjamin
"""

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

estr = ''

for i in range(300000):
    estr += str(i)

Andy = [10**x for x in range(7)]

Prod = 1
for j in range(len(Andy)):
    Prod = Prod*int(estr[Andy[j]])
    
Answer = Prod
print(Answer)
