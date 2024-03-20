# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:35:57 2024

@author: mdelm
"""


"""
# Búsqueda lineal - O(n)

import random

def busqueda_lineal(lista, objetivo):
    match = False
    
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    
    return match


if __name__ == '__main__':
    tamano = int(input('Tamaño de la lista? '))
    objetivo = int(input('Qué número quieres encontrar? '))
    
    lista = [random.randint(0, 100) for i in range(tamano)]
    
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
    

#%% Búsqueda binaria - O(log(n))

import random

def busqueda_binaria(lista, comienzo, final, objetivo): # O(log(n))
    
    if comienzo>final:
        return False
    
    medio = (comienzo +  final) // 2  # División de enteros
    
    if lista[medio]==objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)
    

if __name__ == '__main__':
    tamano = int(input('Tamaño de la lista? '))
    objetivo = int(input('Qué número quieres encontrar? '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamano)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
        

#%% Ordenamiento de burbuja - O(n*n) -> O(n^2)

import random

def ordenamiento_de_burbuja(lista):
    
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista
    

if __name__ == '__main__':
    tamano = int(input('Tamaño de la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano)]
    print(lista)
    
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
 
    
#%% Ordenamiento por inserción - O(n*n) -> O(n^2)

import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            
        lista[posicion_actual] = valor_actual
   
    return lista


if __name__ == '__main__':
    tamano = int(input('Tamaño de la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano)]
    print(lista)
    
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)
    
 

#%% Merge sort - ordenamiento por mezcla

import random

def ordenamiento_por_mezcla(lista):
    if len(lista)>1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        
        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        
        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
    return lista
        

if __name__ == '__main__':
    tamano = int(input('Tamaño de la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano)]
    print(lista)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
    
"""  
    
#%% El problema del morral - Algoritmo incompleto. Funciona limitadamente
# Lo suficientemente bueno para salir de apuros

def morral(tamano_morral, pesos, valores, n):
    
    if n==0 or tamano_morral==0:
        return 0
    
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)
    
    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1), \
               morral(tamano_morral, pesos, valores, n-1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)


#%% Search in rotated arrays

def busqueda_binaria(lista, comienzo, final, objetivo): # O(log(n))
    
    if comienzo>final:
        return -1
    
    medio = (comienzo +  final) // 2  # División de enteros
    
    if lista[medio]==objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)
    

def busqueda_lista_rotada(lista, objetivo):
    
    lista_min = min(lista)
    lista_max = max(lista)
    n = len(lista)
    
    offset = 0
    
    for i in range(n):
        if lista[i] == lista_min:
            offset = i
            break

    lista_ord = sorted(lista)
    
    pos = busqueda_binaria(lista_ord, 0, n, objetivo)
    
    pos_r = pos + offset
    if pos_r >= n:
        print(pos_r-n)
    else:
        print(pos_r)          
    
busqueda_lista_rotada([2,4,8,10,12,14,0], 0)
    

#%% Algoritmo para búsqueda en matrices


def busqueda_binaria(lista, comienzo, final, objetivo): # O(log(n))
    
    if comienzo>final:
        return -1
    
    medio = (comienzo +  final) // 2  # División de enteros
    
    if lista[medio]==objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)


def busqueda_matriz(arr, objetivo):
    
    n = len(arr)
    p = len(arr[0])
    
    arr_flat = [item for row in arr for item in row]
    
    pos = busqueda_binaria(arr_flat, 0, p, objetivo)
    
    return (pos//p, pos%p)


#

arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

print(busqueda_matriz(arr, 5))


