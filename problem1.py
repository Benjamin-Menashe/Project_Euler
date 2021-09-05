# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:09:34 2021

@author: Benjamin
"""

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np

fives = np.array(range(0,1000,5))
threes = np.array(range(0,1000,3))
fifteens = np.array(range(0,1000,15))

Answer = sum(fives) + sum(threes) - sum(fifteens)
print(Answer)