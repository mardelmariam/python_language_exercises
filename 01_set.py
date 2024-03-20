# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:44:57 2023

@author: mmcorrea
"""

# Los set se pueden modificar
# No tienen un orden
# No pueden tener elementos duplicados

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))


set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_from_string = set('Hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
unique_numbers = set(numbers)
print(list(unique_numbers))


