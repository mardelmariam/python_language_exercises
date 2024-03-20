# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:25:58 2023

@author: mmcorrea
"""

set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# Adicionar
set_countries.add('pe')

# Update

set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# Eliminación
"""
discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
"""
set_countries.remove('col')
print(set_countries)
print(sorted(set_countries))

# Limpiar
print(set_countries.clear())

# Operaciones entre conjuntos...




