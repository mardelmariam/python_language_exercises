# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:08:06 2024

@author: mdelm
"""

import time

#import sys
#sys.setrecursionlimit(1000000)


def factorial(n):
    respuesta = 1
    
    while n>1:
        respuesta *=n
        n -= 1
        
    return respuesta


def factorial_r(n):
    if n==1:
        return 1
    
    return n * factorial(n-1)


if __name__ == '__main__':
    n = 200000 # El crecimiento del retardo NO es lineal
    
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)
    
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
    
    # 19.850406885147095 y 20.357691287994385 en laptop
    # Cuánto daría en el PC?
    
    