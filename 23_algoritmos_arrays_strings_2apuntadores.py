# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:01:45 2024

@author: mdelm
"""

"""

El "patrón de dos apuntadores" es un diseño o técnica de programación en el 
cual se utilizan dos punteros para recorrer y manipular una estructura de datos 
en forma conjunta. Esta estructura de datos puede ser, por ejemplo, una lista 
enlazada, un árbol binario o una matriz bidimensional.

En este patrón, los dos punteros se utilizan para rastrear diferentes posiciones 
dentro de la estructura de datos y realizar operaciones relacionadas. 
Por lo general, uno de los punteros se mueve a una velocidad más rápida 
que el otro, lo que crea una distancia fija o una relación predefinida entre ellos.

El patrón de dos apuntadores es especialmente útil en situaciones en las que 
necesitas realizar operaciones que involucren comparaciones o interacciones 
entre elementos adyacentes de una estructura de datos. Por ejemplo, puede ser 
utilizado para buscar un par de elementos que cumplan cierta condición, 
encontrar el punto medio de una lista o realizar operaciones de fusión o 
intersección en conjuntos ordenados.

Este enfoque puede mejorar la eficiencia y reducir la complejidad de los 
algoritmos, ya que evita la necesidad de realizar múltiples recorridos o 
búsquedas completas de la estructura de datos. Sin embargo, su uso 
requiere un cuidadoso manejo de los punteros para evitar errores y 
asegurar que los límites de la estructura de datos sean respetados.

"""

#%% Verifying alien dictionary

# Problema 1: Verifying alien dictionary

"""

En una lengua alienígena, sorprendentemente, también utilizan las letras
del español, pero posiblemente en un orden diferente, una permutación de
nuestro alfabeto.

Dada una secuencia de palabras escritas en el idioma extranjero, y el orden
del alfabeto, devuelve verdadero si y solo si las palabras están ordenadas
lexicográficamente en este idioma extranjero.

lexicográficamente: ordenar palabras de la misma manera en como un diccionario
ordena las palabras

"""

import string

orden_alfabetico = string.ascii_lowercase
orden_alfabeto_alien = 'hlabcdefgikmnopqrstuvqxyz'

def revisar_orden(palabras, alfabeto):
    
    # Una especie de hash table con un dictionary comprehension
    alfabeto_nums = {(alfabeto[i]): i for i in range(len(alfabeto))}
    
    # Máximo número de letras esperado
    k = max([len(palabras[i]) for i in range(len(palabras))])

    for n in range(len(palabras)-1): # Todas las palabras, de 2 en 2

        for idx in range(k): # Recorrido de cada caracter
            
            letra_1 = ''
            letra_2 = ''
            
            try:
                letra_1 = palabras[n][idx]
            except:
                pass
            
            try:
                letra_2 = palabras[n+1][idx]
            except:
                pass
        
            #peso_1 = alfabeto.find(letra_1) if letra_1!='' else -1
            #peso_2 = alfabeto.find(letra_2) if letra_2!='' else -1
            peso_1 = -1
            peso_2 = -1
            
            try:
                peso_1 = alfabeto_nums[letra_1]
            except:
                pass
            
            try:
                peso_2 = alfabeto_nums[letra_2]
            except:
                pass
            
            if peso_1 > peso_2:
                return False
            elif peso_1 < peso_2:
                break
            else:
                continue
        
    return True


palabras = ['conocer', 'cono']
print(revisar_orden(palabras, orden_alfabetico))
print(revisar_orden(palabras, orden_alfabeto_alien))
print('\n')

palabras = ['habito', 'hacer', 'lectura', 'sonreir']
print(revisar_orden(palabras, orden_alfabetico))
print(revisar_orden(palabras, orden_alfabeto_alien))
print('\n')

palabras = ['habito', 'hacer', 'sonreir', 'lectura']
print(revisar_orden(palabras, orden_alfabetico))
print(revisar_orden(palabras, orden_alfabeto_alien))
print('\n')

palabras = ["aguila","cocoa","coco","cocodrilo","rana"]
print(revisar_orden(palabras, orden_alfabetico))
print(revisar_orden(palabras, orden_alfabeto_alien))
print('\n')


#%% Merge two sorted lists - Mio - Encuentra dónde inserta # y desplaza - 
# Complejidad lograda - nlog(n)

"""

Dadas dos listas de números enteros nums1 y nums2, cada una ordenada en 
orden ascendente, y dos enteros m y n, que representan la cantidad de
elementos en nums1 y nums2 respectivamente.

Combinar nums1 y nums2 en un único array ordenado de forma ascendente.

Para ello, nums1 tiene una longitud de m+n, donde los primeros m elementos
denotan los elementos que deben ser combinados, y los últimos n elementos
son 0 y deben ser ignorados.


"""

import random
import time

def ordenamiento_de_listas(nums1, nums2, verbose):
    
    m = len(nums1)
    n = len(nums2)
    
    for i in range(n):
        nums1.append(0)
        
    idx2 = m # Apuntador hacia las ubicaciones a llenar
    idx1 = 0 # Apuntador a la posición donde hay que cambiar el número
    # El desplazamiento de los números ocurre entre idx1 e idx2
    
    
    for j in range(n):
        
        num = nums2[j]
        
        # Hallar idx1
        for i in range(idx2):
            
            a = nums1[i]
            b = nums1[i+1]
            
            if num<=a and num<b:  # n<=a<b
                idx1 = i
                if verbose==1:
                    print(f"Caso 1: num={num} - a={a} - b={b} - idx1={idx1} - idx2={idx2}")
                break
            elif num>a and num<=b:  # a<n<=b
                idx1 = i+1
                if verbose==1:
                    print(f"Caso 2: num={num} - a={a} - b={b} - idx1={idx1} - idx2={idx2}")
                break
            else:  # a<b<n
                if verbose==1:
                    print(f"Caso 3: num={num} - a={a} - b={b} - idx1={idx1} - idx2={idx2}")
                

        # Desplazamientos y asignación de valor a posición  
        if num<=b:
            idx2 += 1
            if verbose==1:
                print(f"Desplazando elementos... {idx1} {idx2}")
            
            if idx2 < n+m:
                i = 0
                if verbose==1:
                    print(f"Desplazamiento ini: {nums1}") 
                while i<(idx2-idx1):
                    nums1[idx2-i] = nums1[idx2-1-i]
                    i += 1
                    if verbose==1:
                        print(f"Desplazamiento: {nums1}") 
            else:
                i = 0
                if verbose==1:
                    print(f"Desplazamiento ini: {nums1}") 
                while i<(idx2-idx1):
                    nums1[idx2-1-i] = nums1[idx2-2-i]
                    i += 1
                    if verbose==1:
                        print(f"Desplazamiento: {nums1}")
                    
            nums1[idx1] = num
            idx1 += 1
            if verbose==1:
                print(f"Final: {nums1}")  
            
        else:
            nums1[idx2] = num
            idx2 += 1
            idx1 += 1
            if verbose==1:
                print(f"Final F: {nums1}") 
                
    print(nums1)
    print('\n')
    

if __name__ == '__main__':
    
    #"""
    tamano = int(input('Tamaño de la lista? '))
    
    for _ in range(3):
    
        nums1 = [random.randint(0, tamano) for i in range(tamano)]
        nums1 = sorted(nums1)
        print(nums1)
        
        nums2 = [random.randint(0, tamano) for i in range(tamano)]
        nums2 = sorted(nums2)
        print(nums2)
        
        ordenamiento_de_listas(nums1, nums2, 0)
        time.sleep(5)
        print('\n')
        
        
#%% Solución de la profe - Ordenar de mayor a menor - Complejidad: O (n+m)
# Funcionalidad limitada

def merge_lists(nums1, n, nums2, m):
    
    p1 = n-1
    p2 = m-1
    p = len(nums1)-1
    print(f"p1={p1} p2={p2} p={p}")
    
    while 0 <= p1 and 0 <= p2:
        print(f"p1={p1} p2={p2} p={p}")
        # nums2 nos sirve
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -=1
        # nums1 nos sirve
        else:
            nums1[p] = nums1[p1]
            p1 -=1
        # mover apuntador p
        print(f"p1={p1} p2={p2} p={p}")
        print(f"{nums1}")
        p -=1
        print('\n')
    
    if n!=m:
        nums1[:p2+1] = nums2[:p2+1]
        
    print(nums1)
    

merge_lists([1, 1, 1, 1, 3, 4, 5, 0, 0, 0, 0, 0, 0], 14, [0, 0, 1, 2, 2, 6, 7], 7)

#%% Container with most water

def container_with_most_water(nums):
    
    max_area = 0
    left = 0
    right = len(nums)-1
    
    while left<right:
        area = (right - left) * min([nums[left], nums[right]]) # Base x altura
        max_area = max([area, max_area])
        print(f"{area} {max_area}:  {left} {nums[left]} {right} {nums[right]}")
        if nums[left] < nums[right]:
            left +=1
        else:
            right -=1
            
    return max_area

container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])


#%% Trapping rain water

"""
Data una lista de números que representan un grupo de líneas de diferentes
alturas, calcula cuánta agua puede atrapar después de llover.

"""

def trapped_rain_water(nums):
    
    # Se agregan tantos ceros al final o al principio como se necesiten
    # para ampliar la búsqueda de máximos locales
    # Luego se deben aplicar correcciones a las posiciones encontradas
    #nums.append(0)
    
    max_idx = []
    
    m = len(nums)
    # Hallar máximos locales
    for i in range(1,m-1):
        if nums[i]>nums[i+1] and nums[i]>nums[i-1]: #and \
            #nums[i]>nums[i+2] and nums[i]>nums[i-2]:
            max_idx.append(i)
    print(max_idx)
    
    # Lo se se agregó de ceros debe retirarse
    #nums.pop(-1)
    
    alturas = []
    alturas_ref = [0 for i in range(m)]
    
    # Hallar alturas mínimas entre máximos para hacer los cálculos
    p = len(max_idx)
    for i in range(p-1):
        a = max_idx[i]
        b = max_idx[i+1]
        h1 = nums[a]
        h2 = nums[b]
        alturas.append(min([h1, h2]))
        print(f"{a} {b} {h1} {h2} {min([h1, h2])}")
    min_u = min(alturas[-1],nums[max_idx[-1]]) # última altura a agregar
    alturas.append(min_u)
    print(alturas)
        
    # Describir las alturas de referencia para cada tramo de máximo local
    aux = 0
    alturas_ref[0] = alturas[aux]
    print(f"{aux} {max_idx[aux]} {alturas_ref}")
    
    for i in range(1,len(nums)):
        print(f"i={i} aux={aux} max={max_idx[aux]}")
        alturas_ref[i] = alturas[aux]
        if i>max_idx[aux]:
            aux +=1
        print(alturas_ref)
        
    # Hallar los valores por debajo de las alturas de refencia y sumarlos al área
    area = 0
    for i in range(max_idx[0], max_idx[-1]): # Desde primer máximo hasta último máximo
        ref = alturas_ref[i]
        val = nums[i]
        if val<=ref and (ref-val)>0:
            area += (ref-val) # Suma lo que haya a igual nivel o por debajo
        print(f"{ref} {val} {area}")
        

def trappingRainWater(alturas): # Solución de otro estudiante
    izq = 0
    der = len(alturas)-1 
    maxIzq = maxDer = 0
    aguaRecolectada = 0

    while(izq <= der):
        print(f'{izq} {der} {alturas[izq]} {alturas[der]} {maxIzq} {maxDer} {aguaRecolectada}')
        if(alturas[izq]<=alturas[der]): 
            if(alturas[izq]>=maxIzq): maxIzq = alturas[izq]
            else: aguaRecolectada += maxIzq - alturas[izq]
            izq += 1
        else:
            if(alturas[der]>=maxDer): maxDer = alturas[der]
            else: aguaRecolectada += maxDer - alturas[der]
            der -= 1
    return aguaRecolectada

        
#trapped_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

print(trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

#print(trappingRainWater([0, 1, 4, 3, 2, 0, 4, 0, 2, 3, 4, 0, 1, 0, 1, 0, 1, 0, 4, 0]))

#trapped_rain_water([0, 2, 3, 1, 1, 0, 1, 1, 2, 3, 4, 1])

#trapped_rain_water([0, 1, 4, 3, 2, 0, 4, 0, 2, 3, 4, 0, 1, 0, 1, 0, 1, 0, 4, 0])


#%% Mover ceros al final, sin ordenar los números, dejándolos como están

def mover_ceros_al_final(nums):
    
    zeroes = 0
    pos = []
    
    n = len(nums)
    
    for i in range(n):
        if nums[i]==0:
            zeroes +=1
        else:
            pos.append(i)
    
    for i in range(len(pos)):
        nums[i] = nums[pos[i]]
    
    for i in range(len(pos), len(pos)+zeroes):
        nums[i] = 0
        
    print(nums)
    #for j in range(zeroes):
        #if 

mover_ceros_al_final([0,1,0,3,12])

mover_ceros_al_final([1,3,0,8,0,9,0,0,0,1,5,2,6,3,0,0,3,0,1,5,9,1,2,0,0,0,3,4,5,6,7,0,1])


#%% Invertir string

def invertir_string(palabra):
    
    idx = len(palabra)-1
    
    out = ''
    
    while idx>=0:
        out += palabra[idx]
        idx -= 1
        
    return out

    # Pythonic: ''.join(list(reversed('Hello')))

print(invertir_string('hello'))

#%% Intersección de un intervalo

def interseccion_intervalos(arr1, arr2):
    
    for i in range(len(arr1)):
        
        int1 = arr1[i]
        int2 = arr2[i]

        a = int1[0]
        b = int1[1]
        c = int2[0]
        d = int2[1]
        
        if a<b and b<c and c<d:
            return []
    
        elif c<d and d<a and a<b:
            return []
        
        else:
            #Hay traslape en algún valor
            ini = 0
            fin = 0
            
            if a>c:
                ini = a
            else:
                ini = c
            
            if b<d:
                fin = b
            else:
                fin = d
            
            print(f"{ini} {fin}")
    
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
        
interseccion_intervalos(firstList, secondList)        
    

