#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:48:14 2019

@author: ssiangpipop
"""
"""
point = 1, 7
print(point[0])
print(point[1])

pointB = (1,7)
print(pointB[1])

th = "Thailand", 5, 10, 15
print(th[1] + th[2] + th[3])

monster = ("pikachu", "bulbasaur", "eevee")
"""

def distance(pointA, pointB):
    return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) **.5 
#def distance(x1, y1, x2, y2):
#   return((x1 - x2) **2 + (y1 - y2) **2) **.5

pointA = (1, 7)
pointB = 1, 10

d = distance(pointA, pointB)
print(d)

# immutable tuple : cannot be edited