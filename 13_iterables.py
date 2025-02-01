# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:43:30 2024

@author: mdelm
"""

from itertools import product

def cartesian_product(x, y):
    args = [x, y]
    args_list = list(product(*args))
    
    str_args = str(tuple(args_list[0]))
    for i in range(1, len(args_list)):
        str_args += f" {str(args_list[i])}"
    
    print(str_args)
        
    
if __name__ == '__main__':
    
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    cartesian_product(a, b)

#%%

from itertools import permutations

def word_variations(word, num):
    
    letters = [word[i] for i in range(len(word))]
    
    args_list = list(permutations(letters, int(num)))
    args_list = sorted(args_list)
    
    for i in range(len(args_list)):
        print(''.join(args_list[i]))
        
    
if __name__ == '__main__':
    
    a = list(map(str, input().rstrip().split()))
    
    word_variations(a[0], a[1])

