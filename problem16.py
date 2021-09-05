# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:05:26 2021

@author: Benjamin
"""

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

numr = 2**1000

estr = str(numr)

lizt = []

[lizt.append(int(i)) for i in estr]

Answer = sum(lizt)
print(Answer)