# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:16:30 2021

@author: Benjamin
"""

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# %% create big dictionary of all numbers and their strings using the small dictionary

diksh = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten' \
         ,11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen' \
         ,18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy' \
         ,80:'eighty',90:'ninety'}

big_diksh = {}

for i in range(1,1000):
    estr = []
    j = i % 100
    if j == 0:
        estr = diksh[i/100] + 'hundred'
    else:
        if j <= 20:
            estr = diksh[j]
        else:
            k = j % 10
            estr = "".join((diksh[j-k],diksh[k]))
        
        m = (i-j)/100
        if m > 0:
            estr = diksh[m] + 'hundredand' + estr
    
    big_diksh[i] = estr

big_diksh[1000] = 'onethousand'
    
# %% add all string lengths together
zz = "".join((big_diksh.values()))
Answer = len(zz)
print(Answer)
