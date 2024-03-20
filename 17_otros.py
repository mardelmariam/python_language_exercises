# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:11:01 2024

@author: mdelm
"""

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)
    
    
#%%

## Calcule permutaciones de coordenadas, y que estas sumen diferente a un número n

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    perms = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]
    
    print(perms)
    
#%%

matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

n = len(matrix)
s = 0


# MATRIX GROUPS
# A, B, B, A
# C, D, D, C
# C, D, D, C
# A, B, B, A
# max value = max(A) + max(B) +  max(C) + max(D)

for i in range(n//2):
    for j in range(n//2):
        s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    
print(s)

#%% Reto: Find a string - Pasó ^_^

def count_substring(string, sub_string):
    
    n = 0
    m = len(sub_string)
    
    for i in range(len(string)-m+1):
        if sub_string == string[i:i+m]:
            n += 1
            
    return n

        

if __name__ == '__main__':
    string = 'AAABAAAABAAA'
    sub_string = 'AAA'
    
    count = count_substring(string, sub_string)
    print(count)