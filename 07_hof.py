# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:35:16 2023

@author: mmcorrea
"""

def increment(x):
    return x+1

increment_v2 = lambda x : x+1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)   
print(result) 

high_order_function_v2 = lambda x, func: x + func(x)

print(high_order_function_v2(2, increment_v2))

