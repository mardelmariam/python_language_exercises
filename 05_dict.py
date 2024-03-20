# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 07:08:03 2023

@author: mmcorrea
"""

dict_v2 = {i: i*2 for i in range(1,5)}
print(dict_v2)

import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
    
print(population)

population_v2 = {country: random.randint(1,100) for country in countries}

print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population>10}

print(result)


names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]


print(list(zip(names, ages)))

# Mejor generando el diccionario

new_dict = {name: age for (name,age) in zip(names,ages)}

print(new_dict)


text = "Hola, soy Nicolas"
unique = {c: c.upper() for c in text if c in 'aeiou'}








