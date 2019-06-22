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
print("1, rectangle คำนวนพื้นที่สี่เหลี่ยม")
print("2, triangle คำนวนพื้นที่สามเหลี่ยม")
n = input("please select option: ")

W = int(input("width = "))  
H = int(input("height = "))  

if n == "1":
    print("rectangle area = ", rectangle(W , H))
    #print(rectangle(W , H))
else:
    print("triangle area = ", triangle(W , H))
    #print(triangle(W , H))