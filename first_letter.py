# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:03:38 2022

@author: 26902
"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""

for word in org.lower().split(" "):
    if word not in stopwords:
        
        acro += word[0].upper()
print(acro)