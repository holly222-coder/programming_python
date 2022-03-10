# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:40:47 2022

@author: 26902
"""

phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)