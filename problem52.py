# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:12:43 2021

@author: Benjamin
"""

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

### UNSOLVED BECAUSE NOT SURE IF MUST BE UNIQUE DIGITS

def cmp_dig(n: int) -> bool():
    chief = set(str(n))
    if digs == chief:
        return True
    return False


x = False
while x != True:
    for i in range(100000,130000):
        digs = set(str(i))
        mult2 = i*2
        x = cmp_dig(mult2)
        
Answer = i
print(Answer)