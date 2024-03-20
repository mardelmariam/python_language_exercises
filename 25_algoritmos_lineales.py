# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:09:05 2024

@author: mdelm
"""

# Lista enlazada

# Estructura de datos en la que los valores no están guardados de forma
# contigua en memoria

 # Desventaja: toca recorrer toda la lista para acceder a cierto elemento O(n)
 
 # Ventaja: Insertar un nuevo elemento no signfifica que hay que correr todos
 # los elementos que van después. Complejidad de insertar: O(1)
 # Algo similar sucede cuando se quiere remover un valor
 
 
class Node:

    def __init__(self, item, _next=None):
        self.item = item
        self.next = _next

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, item):
        self.item = item
    
    def setNext(self, _next):
        self.next = next
        

class LinkedList:
    
    class __Node:
        
        # Esta clase es de uso interno para LinkedList. Es invisible fuera
        # de la clase.
        
        def __init__(self, item, _next=None):
            self.item = item
            self.next = _next
            
        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item
       
        def setNext(self, _next):
            self.next = next
           
           
    def __init__(self, contents=[]):
        
        # Se genera un nodo dummy, que es el primero y el último inicialmente
       
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0      
        
        for e in contents:
            self.append(e)
            

    def __getitem__(self, index):
        if index>=0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor.getItem()()
        
        raise IndexError("LinkedList index out of range")
        
    
    def __setitem__(self, index, val):
        if index>=0 and index < self.numItems:
            cursor = self.first.getNext():
            for i in range(index):
                cursor = cursor.getNext()
            cursor.setItem(val)
            return
        
        raise IndexError("LinkedList assignment index out of range")
        
    
                    