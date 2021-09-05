# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:27:10 2021

@author: Benjamin
"""
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


#%% Create list of palindromes
palis = []

for i in range(9,-1,-1):
    for j in range(9,-1,-1):
        for k in range(9,-1,-1):
            palis.append(int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i)))
            
#%% Check which one is multiple of 2 3-digiters
cand = 0

for aa in range(999,99,-1):
    for bb in range(aa,99,-1):
        if aa*bb > cand:
                if aa*bb in palis:
                    cand = aa*bb     

Answer = cand
print(Answer)