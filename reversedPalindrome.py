# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:29:47 2022

@author: 26902
"""

p_phrase = "was it a car or a cat I saw"
phrase = []
for letter in p_phrase:
    phrase.append(letter)
phrase.reverse()
r_phrase= ''
r_phrase = "".join(phrase)
print(r_phrase)
