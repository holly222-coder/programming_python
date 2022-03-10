# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:42:42 2022

@author: 26902
"""

s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)