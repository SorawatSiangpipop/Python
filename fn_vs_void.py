#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:39:01 2019

@author: ssiangpipop
"""

def celsius_to_fah(celsius): #fn
    return (celsius *9 /5) +32

def temperature_table(): #void fn
    for c in range(0, 101, 5):
        f = celsius_to_fah(c)
        print("{}C = {}F".format(c, f))
    #in Python return None
    
def menu(): #void fn
    print("1, convert C to F")
    print("2 , display temp. table")
    n = input("enter choice: ")
    if n == "1":
        celsius = float(input("enter degree in C: "))
        print("{}C = {}F".format(celsius, celsius_to_fah(celsius)))
    elif n == "2":
        temperature_table()
        
#f = celsius_to_fah(100)
#print(f)
#a = temperature_table()
#print(a)
menu()