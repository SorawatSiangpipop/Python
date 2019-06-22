#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:29:53 2019

@author: ssiangpipop
"""

"""
def price_with_vat(amount):
    vat = amount *7 /107 # 107 *7 /107
    price = amount - vat
    #t = price, vat # tuple
    return (price, vat)
    #return t

print(price_with_vat(107))

a = price_with_vat(200)
print(type(a))
print(a)
print('price =', a[0])
print('vat = ', a[1])

p, v = price_with_vat(200)
print("p = ", p)
print("v = ", v)
"""


def thai_area(sqwa):
    rai = sqwa // 400 # 1 rai = 400 aqwa
    ngan = (sqwa - (rai * 400)) // 100
    wa = sqwa %100
    return rai, ngan, wa

a = 956
print(thai_area(a))
r, n, w = thai_area(a)
print(r, n, w, sep="-")
