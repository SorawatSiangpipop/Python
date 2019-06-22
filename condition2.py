#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:44:36 2019

@author: ssiangpipop
"""

def ticket(age):
    if age <= 5:
        return 0
    else:
        return 100

def ticket2(age):
    if age <= 5 or age>=60:
        return 0
    else:
        return 100

def ticket3(age, is_local):
    if (age <= 5 or age>=60) and is_local:
        return 0
    else:
        return 100
    
def ticket2a(age):
    return 0 if age <= 5 or age>=60 else 100 #ternary

def demo(a):
    if a >= 10 and a<= 20:
        print("ok")
    else:
        print("not ok")
        
def demo2(a):
    if 10 <= a <= 20:
        print("ok")
    else:
        print("not ok")

demo2(15)
print(ticket(4))
print(ticket2(70))
print(ticket2(35))
print(ticket2(3))
print(ticket3(3, False))
print(ticket2a(3))