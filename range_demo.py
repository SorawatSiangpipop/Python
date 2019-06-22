#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:51:58 2019

@author: ssiangpipop
"""


"""
r = range(10) # [0, 10] (inclusive, exclusive)
print(r)
print(list(r))
print(len(r))
print(type(r))
"""

"""
r1 = range(5,20)
print(list(r1))
print("-" *40)
r2 = range(5, 20, 2)
print(list(r2))
print("-" *40)
r3 = range(10, 0, -3)
print(list(r3))
print("-" *40)
r4 = range(-1, -10, 1)
print(list(r4))
print("-" *40)
r5 = range(-1, -10, -1)
print(list(r5))
"""

n = range(1, 101, 2)
print(list(n))
print("-" *40)
print(len(n))
print("-" *40)
print(sum(n))