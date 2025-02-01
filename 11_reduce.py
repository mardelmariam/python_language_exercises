# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:32:56 2024

@author: mdelm
"""

import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)