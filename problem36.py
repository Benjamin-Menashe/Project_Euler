# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

Sammy = 0

for i in range(1000000):
    if str(i) == str(i)[::-1]:
        if str(bin(i))[2:] == str(bin(i)[::-1])[:-2]:
            Sammy += i

Answer = Sammy
print(Answer)