# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:42:08 2024

@author: mdelm
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# Funciona ^_^
# input 7 debe dar 7
# input 8 debe dar 4

def superDigit(n, k):
    import functools
    if len(n)<4000:
        if int(n)<10:
            return n
        else:
            suma = functools.reduce(lambda a,b: int(a)+int(b), n)
            suma *= k
            return superDigit(str(suma), 1)
    else:
        suma = 0 
        veces = 0
        res = len(n)%4000
        veces = len(n)//4000
        for i in range(veces):
            part = n[4000*i:4000*(i+1)]    
            aux = functools.reduce(lambda a,b: int(a)+int(b), part)
            suma +=aux
        if res!=0:
            part = n[4000*veces:4000*veces+res]    
            aux = functools.reduce(lambda a,b: int(a)+int(b), part)
            suma +=aux
        if k%10!=0:
            suma *= k
        return superDigit(str(suma), 1)


if __name__ == '__main__':
    fptr = open('input07a.txt', 'r')
    content = fptr.read()
    
    first_multiple_input = content.split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)

    fptr.close()
