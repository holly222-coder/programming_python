# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:12:46 2022

@author: 26902
"""


import turtle
wn = turtle.Screen()
june = turtle.Turtle()

for _ in range(5):
    june.color("green", "yellow")
    june.forward(50)
    june.speed(1)
    june.right(72)
wn.exitonclick()