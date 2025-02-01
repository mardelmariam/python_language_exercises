# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:00:31 2023

@author: mmcorrea
"""

numbers = []

for element in range(1,11):
    numbers.append(element)

print(numbers)

numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)

numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

# [element for element in iterable]
# iterable puede ser un rango o una lista

numbers3 = [i*2 for i in range(1,101) if i%2==0]
print(numbers3)



numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [num for num in numbers if num%2==0]

print('v2 =>', even_numbers_v2)



