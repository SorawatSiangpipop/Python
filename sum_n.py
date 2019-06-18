#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:37:32 2019

@author: ssiangpipop
"""

#1+2+3+...10
n=10
sum=0
for i in range(1, n+1):
    sum = sum + i
    #print(i)
    
print("sum=", sum)
print("sun2=", (n*(n+1))/2)

# 1+10=11
# 2+9=11
# 3+8=11
# 4+7=11
# 5+6=11

# (n*(n+1))/2
# (10*11)/2