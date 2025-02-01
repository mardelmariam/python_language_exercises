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
    
    
#%% DEC to BIN, OCT and HEX

def print_formatted(number):
    
    #number = 17
    
    padding = len("{0:b}".format(number))+1
    
    for idx in range(1, number+1):

        binary_num = "{0:b}".format(idx)
        nums = len(binary_num)

        expanded_binary = binary_num[::-1]
        while nums%3!=0:
            expanded_binary += '0'
            nums = len(expanded_binary)
        expanded_binary = expanded_binary[::-1]
            
        # To OCTAL
        octal_num = ''
        for i in range(nums//3):
            a = 3*i
            b = 3*(i+1)
            subnum = expanded_binary[a:b]
            
            if subnum == '000': octal_num += '0'
            elif subnum == '001': octal_num += '1'
            elif subnum == '010': octal_num += '2'
            elif subnum == '011': octal_num += '3'
            elif subnum == '100': octal_num += '4'
            elif subnum == '101': octal_num += '5'
            elif subnum == '110': octal_num += '6'
            else: octal_num += '7'
            
        octal_num = octal_num[1:] if octal_num[0]=='0' else octal_num
        
        # To HEX
        
        expanded_binary = binary_num[::-1]
        while nums%4!=0:
            expanded_binary += '0'
            nums = len(expanded_binary)
        expanded_binary = expanded_binary[::-1]
            
        hex_num = ''
        for i in range(nums//4):
            a = 4*i
            b = 4*(i+1)
            subnum = expanded_binary[a:b]
            
            if subnum == '0000': hex_num += '0'
            elif subnum == '0001': hex_num += '1'
            elif subnum == '0010': hex_num += '2'
            elif subnum == '0011': hex_num += '3'
            elif subnum == '0100': hex_num += '4'
            elif subnum == '0101': hex_num += '5'
            elif subnum == '0110': hex_num += '6'
            elif subnum == '0111': hex_num += '7'
            elif subnum == '1000': hex_num += '8'
            elif subnum == '1001': hex_num += '9'
            elif subnum == '1010': hex_num += 'A'
            elif subnum == '1011': hex_num += 'B'
            elif subnum == '1100': hex_num += 'C'
            elif subnum == '1101': hex_num += 'D'
            elif subnum == '1110': hex_num += 'E'
            else: hex_num += 'F'
        
        hex_num = hex_num[1:] if hex_num[0]=='0' else hex_num
        
        # Print results
        if padding-1-len(str(idx))>0:
            for j in range(padding-1-len(str(idx))):
                print(' ', end='')
        else:
            for j in range(padding-len(str(idx))):
                print(' ', end='')
        print(idx, end='')
        for j in range(padding-len(octal_num)):
            print(' ', end='')
        print(octal_num, end='')
        for j in range(padding-len(hex_num)):
            print(' ', end='')
        print(hex_num, end='')
        for j in range(padding-len(binary_num)):
            print(' ', end='')
        print(binary_num)

    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#%% Using the string library

import string

def print_rangoli(size):
    
    # variables
    length = 4 * size - 3
    lower = list(string.ascii_lowercase)
    strlist = []
    
    # top
    newstr = ''
    for i in range(size - 1,-1,-1):
        if i == size - 1:
            newstr = lower[i]
        else:
            newstr = newstr[0: int(len(newstr)/2) + 1]+ '-' + lower[i] + '-' + newstr[int(len(newstr)/2):]
            
        strlist.append(newstr)
        print(newstr.center(length, '-'))
    
    # bottom
    for i in range(len(strlist) - 2, -1, -1):
        print(strlist[i].center(length, '-'))
        
print_rangoli(5)