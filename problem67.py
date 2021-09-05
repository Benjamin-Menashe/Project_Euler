# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:09:00 2021

@author: Benjamin
"""

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# %% Manually open p067_triangle.txt from the folder and replace ' 0' with ' '.

# %% load as list

triangle = open('p067_triangle.txt', "r")
pyr = triangle.readlines()

for i in range(100):
    pyr[i] = list(map(int,pyr[i].split(' ')))


# %% continue to prune paths

pyr2 = [0 for x in range(100)]
for i in range(100):
    pyr2[i] = list(filter(lambda i: type(i)==int,pyr[i]))

rep = [0 for x in range(100)]
for j in range(100):    
    rep[j] = ((99,j),pyr2[99][j])
dik = dict(rep)

for i in range(98,-1,-1):
    for j in range(len(pyr2[i])):
        best = max(dik[(i+1,j)], dik[(i+1,j+1)])
        dik[(i,j)] = pyr2[i][j] + best
        
Answer = dik[(0,0)]
print(Answer)