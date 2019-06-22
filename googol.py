#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:07:33 2019

@author: ssiangpipop
"""

def demo1():
    # Google (googol) = 1e100
    print("1" +("0" *5))

    # string.format
    print("1{0}".format("0" * 5))
    
    #f-string (Python 3.6+)
    print(f'1{"0" *5}')
    
def demo2():
    print("1", end="")
    for i in range(5):
       print("0", end="")
       
def repeat(ch, times):
    for i in range(times):
       print("0", end="")
      
def repeat2(ch, times):
    s=""
    for i in range(times):
        s +=ch
    return s
      
demo1()     
demo2()
print("\n" +"1", end="")
repeat("0", 5)

print("\n" +"1" +repeat2("0", 5))