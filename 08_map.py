# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:42:20 2023

@author: mmcorrea
"""

numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)
    
numbers_v3 = map(lambda i: i*2, numbers)

print(numbers)
print(numbers_v2)
print(numbers_v3)
print(list(numbers_v3))

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]

result = list(map(lambda x, y: x+y, numbers_1, numbers_2))
print(result)

    