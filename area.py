#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:04:39 2019

@author: ssiangpipop
"""

def rectangle(W,H): # Dynamic Typing
    # code block
    area = W * H
    return area

def triangle(W , H):
    #area = 1/2 * W *  H
    return 1/2 * W * H

# main entry point
W = int(input("width = "))  
H = int(input("height = "))  

print(rectangle(W , H))
print(triangle(W , H))