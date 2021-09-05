# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:24:56 2021

@author: Benjamin
"""

# Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
# How many Lychrel numbers are there below ten-thousand?

def is_pali(n: int) -> bool:
    if str(n) == str(n)[::-1]:
        return True
    return False


def proccessize(n: int) -> int:
    return n + int(str(n)[::-1])


not_lychs = 0

for i in range(10000):
    j = 1
    pali = False
    x = i
    while j <= 50 and pali == False:
        x = proccessize(x)
        if is_pali(x):
            pali = True
            not_lychs += 1
        j += 1
        
Answer = 10000 - not_lychs
print(Answer)