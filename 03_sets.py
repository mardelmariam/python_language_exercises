# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:44:11 2023

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

#%%

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

# Para más detalles, ver https://realpython.com/python-sets/

#%%

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

#%%

def distinct_country_stamps(countries):
    countries_set = set(countries)
    print(len(countries_set))


if __name__ == '__main__':
    n = int(input())
    countries = []
    for i in range(n):
        countries.append(input())
    distinct_country_stamps(countries )
    
    
"""
7
UK
China
USA
France
New Zealand
UK
France
"""

#%% Differences between pop(), remove() and discard()

n = int(input())
s = set(map(int, input().split()))

def alter_set(n, numbers, m):
    
    numbers_set = set(numbers)
    
    for i in range(m):
        instruction = input()
        if instruction.find('pop')!=-1:
            numbers_set.pop()
        elif instruction.find('remove')!=-1:
            args = instruction.split()
            try:
                numbers_set.remove(int(args[1]))
            except:
                pass
        elif instruction.find('discard')!=-1:
            args = instruction.split()
            
            numbers_set.discard(int(args[1]))
        
    
    print(sum(list(numbers_set)))
        

m = int(input())
alter_set(n, s, m)

"""
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
"""


#%% Lexicographic combinations of words

from itertools import combinations

def list_combinations(word, k):
    for letters in range(1, k+1):
        combs = list(combinations(word, letters))
        
        for i in range(len(combs)):
            combs[i] = sorted(combs[i])
        
        combs = sorted(combs)
        
        for comb in combs:
            print(''.join(comb))

if __name__ == '__main__':
    args = input().split()
    list_combinations(args[0], int(args[1]))
    
    
#%% Data groups

from itertools import groupby


def number_groups(data):
    groups = []
    uniquekeys = []
    data = [data[i] for i in range(len(data))]
    
    for k, g in groupby(data):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)
    
    groups = list(groups)
    
    for i in range(len(groups)):
        print(f"({len(groups[i])}, {groups[i][0]}) ", end='')


if __name__ == '__main__':
    string = input()
    number_groups(string)
    
