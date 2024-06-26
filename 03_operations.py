# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:44:11 2023

@author: mmcorrea
"""

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión
## mediante método
set_c = set_a.union(set_b)
print(set_c)
## mediante operador
print(set_a | set_b)

# Intersección
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Diferencia
# A-B
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Diferencia simétrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)


# Reto
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
new_set = countries.union(northAm, centralAm, southAm)

print(new_set)



