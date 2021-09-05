# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:11:54 2021

@author: Benjamin
"""

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

SqOsum = (101*100/2)**2

pyramid100 = 100*(100+1)*(2*100+1)/6

Answer = SqOsum - pyramid100
print(Answer)