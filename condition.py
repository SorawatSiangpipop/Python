#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:57:59 2019

@author: ssiangpipop
"""

# ==, <>, !-, <, >, <=, >=, not, and, or
"""
score = 65
if score > 70:
    print("good")
else:
    print("try harder")
"""

def greeting(lang):
    if lang == "th":
        print("sawadee")
    else:
        print("hello")
        
def greeting2(lang):
    if lang == "th":
        print("sawadee")
    elif lang == "jp":
        print("konichiwa")
    elif lang == "kr":
        print("ann-yeong")
    else:
        print("hello")
        
def meet_re(eng, interview):
    if eng > 70 and interview > 80:
        return True
    else:
        return False
        
greeting("aa")
greeting2("kr")
print(meet_re(80, 90))