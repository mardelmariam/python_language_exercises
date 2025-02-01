# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:29:36 2023

@author: mmcorrea
"""

def increment(x):
    return x+1

print(increment(10))

increment_v2 = lambda x : x+1
print(increment_v2(10))

full_name = lambda name, last_name: f'Full name is {name} {last_name}'

print(full_name('A', 'B'))


def multiply_numbers(numbers):
    x2 = lambda x : x*2
    res = [x2(x) for x in numbers]
    return res

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
