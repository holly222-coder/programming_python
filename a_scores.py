#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:41:12 2022

@author: 26902
"""

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0

for score in scores.split(" "):
    if int(score) >= 90:
        a_scores +=1
print(a_scores)
