# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:43:39 2022

@author: 26902
"""

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    product_name = item.split(",")[0]
    product_number = item.split(",")[1]
    product_price = item.split(",")[2]
    print("The store has{} {}, each for{} USD.".format(product_number, product_name, product_price))
