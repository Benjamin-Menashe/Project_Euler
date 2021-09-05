# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:47:02 2021

@author: Benjamin
"""

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

## easy to see that we must use 20 "downs" and 20 "right", just in different order each time.
## so we know that there will be 40 steps, 20 of them "rights", and the other 20 "downs".
## if we first select the 20 "rights" the other places must be "downs", and so we can compute:
## 40Choose20 for the number of lattice routes.

import math

Answer = math.factorial(40) / (math.factorial(20)**2)
print(int(Answer))