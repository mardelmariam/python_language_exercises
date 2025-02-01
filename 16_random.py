# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:50:15 2024

@author: mdelm
"""
"""
# IMPORT-1
import random
# IMPORT-2
from random import choice

numbers = [num for num in range(0,100)]

#CLIENT-CODE-1
random.shuffle(numbers)

#CLIENT-CODE-2
pick = choice(numbers)
"""

#%%

def some_func(iterator):
    
    iterator = iter(iterator)
    
    try:
        first = next(iterator)
    except StopIteration:
        return True
    
    return all(first == x for x in iterator)

mytuple = ("apple", "apple", "apple")

print(some_func(mytuple))


#%%

lista = [i**3 for i in range(0,100)]

filtro = list(filter(lambda item: item%5==0, lista))


#%%

L = [i for i in range(1,10)]

print(list(map(lambda x: x**2, L)))


#%%

def function(text):
    return text == text[::-1]

print(function("ala"))
