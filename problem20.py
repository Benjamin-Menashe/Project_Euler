# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:00:52 2021

@author: Benjamin
"""

# Find the sum of the digits in the number 100!

import math

a = math.factorial(100)
sammy = sum([int(i) for i in str(a)])

Answer = sammy
print(Answer)
