#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:31:25 2019

@author: ssiangpipop
"""

# come 3, pay 2
# come 4, pay 3

# input -> process -> output

# input
#come_x = 4
#pay_y = 3
per_head = 100
pax = 9

# process
#print((pax // come_x) * (pay_y * per_head))
#print((pax % come_x) * per_head)
#total = (pax // come_x) * (pay_y * per_head) + (pax % come_x) * per_head
#print(total)

def come_x_pay_y(pax, per_head, come_x=4, pay_y=3):
    total = (pax // come_x) * (pay_y * per_head) + (pax % come_x) * per_head
    return total
print(come_x_pay_y(pax, per_head))