# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:09:05 2024

@author: mdelm
"""

# Lista enlazada - Linked list

# Estructura de datos en la que los valores no están guardados de forma
# contigua en memoria

 
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
        
        # This class is used internally by the LinkedList class. It is
        # invisible from outside this class due to the two underscores that
        # precede the class name.
        
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
            self.next = _next
           
           
    def __init__(self, contents=[]):
        
        # Creating a linked list object has exactly the same complexity 
        # as constructing a <list> object. O(1)
        # At first, the head and the tail of the linked list point
        # to a dummy node
       
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0      
        
        for e in contents:
            self.append(e)
            
            
    # SET and GET methods of a linked list. 
    # If random access to a list is desired, then the <list> class should be used.
    # Linked lists are not randomly accesible. They require linear search 
    # through the datatype to access a particular location in the list.
    # Each of these operations is O(n) where n is the value of the index
    
    def __getitem__(self, index):
        if index>=0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor.getItem()
        
        raise IndexError("LinkedList index out of range")
        
    
    def __setitem__(self, index, val):
        if index>=0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            cursor.setItem(val)
            return
        
        raise IndexError("LinkedList assignment index out of range")
        
    
    # CONCATENATE method for a linked list. O(n) complexity
    
    def concat(self, other):
        if type(self) != type(other):
            raise TypeError(f"Concatenate undefined for {str(type(self))} \
                            and {str(type(other))}")
        
        result = LinkedList()
        
        cursor = self.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        
        return result
    
    
    # APPEND method. O(1) complexity
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
        
        
    # INSERT method. O(n) complexity
    # Inserting into a list is a O(n) operation where n is the number of elements
    # that are in the list after the insertion point since they must all be moved
    # down to make room for the new item. When working with a LinkedList the
    # n is the number of elements that appear before the insertion point because
    # we must search for the correct insertion point.
    
    def insert(self, index, item):
        cursor = self.first

        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
            
            
    # DELETE methold. O(n) complexity
    
    def delete(self, index):
        cursor = self.first

        if index < self.numItems - 1:
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor_del = cursor
            cursor_del = cursor_del.getNext()
            cursor.setNext(cursor_del.getNext())
            
            del(cursor_del)
            del(cursor)

        elif index == self.numItems - 1:
            
            for i in range(index):
                cursor = cursor.getNext()
                
            del(cursor)
            
            cursor = self.first
            
            for i in range(index):
                cursor = cursor.getNext()
            
            cursor.setNext(None)
            self.last = cursor
        
        else:
            
            cursor = self.first
            cursor_next = cursor.getNext()
            
            del(cursor)
            
            self.first = cursor_next
            
            
        self.numItems -= 1
        
        
    def reverse(self):
        
        result = LinkedList()
        
        index = self.numItems-1
        
        for i in range(self.numItems):
            value = self.__getitem__(index)
            print('\t' + value)
            result.append(value)
            index -= 1
        
        return result
    
    
    def reverse(self):
        
        result = LinkedList()
        
        index = self.numItems-1
        
        for i in range(self.numItems):
            value = self.__getitem__(index)
            result.append(value)
            index -= 1
        
        return result
    
    
    def OddEvenOrder(self):
        
        result = LinkedList()
        
        for i in range(self.numItems):
            value = self.__getitem__(i)
            if value%2==1:
                result.append(value)
            else:
                continue
                
        for i in range(self.numItems):
            value = self.__getitem__(i)
            if value%2==0:
                result.append(value)
            else:
                continue
        
        return result
            
      
          
ListaEnlazada = LinkedList(['a', 'b', 'c', 'd'])
"""
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')
"""

ListaReversa = ListaEnlazada.reverse()
del ListaEnlazada
for i in range(ListaReversa.numItems):
    print(ListaReversa.__getitem__(i))
print('\n')

ListaEnlazada = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
Lista_Orden = ListaEnlazada.OddEvenOrder()
del ListaEnlazada
for i in range(Lista_Orden.numItems):
    print(Lista_Orden.__getitem__(i))
print('\n')


ListaEnlazada = LinkedList(['a', 'b', 'c', 'd'])

ListaEnlazada.append('f')
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')

ListaEnlazada.insert(4, 'e')
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')

ListaEnlazada.delete(0)
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')


ListaEnlazada_Otra = LinkedList(['g', 'h', 'i', 'j'])

ListaEnlazada_Concat = ListaEnlazada.__add__(ListaEnlazada_Otra)
for i in range(ListaEnlazada_Concat.numItems):
    print(ListaEnlazada_Concat.__getitem__(i))
print('\n')


ListaEnlazada.append('f')
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')


ListaEnlazada.delete(2)
for i in range(ListaEnlazada.numItems):
    print(ListaEnlazada.__getitem__(i))
print('\n')


ListaEnlazada_Otra = LinkedList(['g', 'h', 'i', 'j'])

ListaEnlazada_Concat = ListaEnlazada.concat(ListaEnlazada_Otra)
for i in range(ListaEnlazada_Concat.numItems):
    print(ListaEnlazada_Concat.__getitem__(i))
print('\n')



#%% Otra implementación de lista enlazada

class Node:
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    
    def __init__(self, first_node):
        self.head = first_node  
        self.tail = first_node
        
    def insert_node_at_end(self, new_node):
        self.tail.next = new_node
        self.tail = self.tail.next
    
    def delete_node(self, node):
        node.next = None
        
    def search_node(self, value_to_search):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value_to_search:
                return current_node
            current_node = current_node.next
        return None
    
    
    def delete_node_by_value(self, value):
        if self.head and self.head.value==value:
            self.head = self.head.next
            return
        
        previous_node = None
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == value:
                break
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return
        
        previous_node.next = current_node.next
        
        if current_node == self.tail:
            self.tail = previous_node
            
            
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            
lista = LinkedList(Node(1))
lista.insert_node_at_end(Node(2)) 
lista.insert_node_at_end(Node(3)) 
lista.delete_node_by_value(2)
lista.print_list() 


#%% Detecting and deleting loops on a linked list

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=' —> ')
        curr = curr.next
    print('None')
 
 
def removeCycle(head):
    prev = None        
    curr = head        
    s = set()
    while curr:
        if curr in s:
            prev.next = None
            return

        s.add(curr)
        prev = curr
        curr = curr.next
 
if __name__ == '__main__':
 
    head = None
    head = Node(1, head)
    head = Node(0, head)
    head = Node(3, head)
    head = Node(0, head)
    head = Node(1, head)
 
    head.next.next.next.next.next = head.next
 
    removeCycle(head)
    printList(head)

#%% Double linked list

class Node:
     
     def __init__(self, value=None, prev= None, next=None):
         self.value = value
         self.prev = prev
         self.next = next

class DoubleLinkedList:
    
    def __init__(self, first_node):
        self.head = first_node  
        self.tail = first_node
        self.numNodes = 1
        
    def insert_node_at_end(self, new_node):
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next
        self.numNodes += 1
        
    def search_node(self, value_to_search):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value_to_search:
                return current_node
            current_node = current_node.next
        return None
    
    def get_node(self, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value
    
    def get_reverse_node(self, index):
        current_node = self.tail
        for _ in range(index):
            current_node = current_node.prev
        return current_node.value
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            
    def change_order(self):
        # L0, Ln, L1, Ln-1, L2, Ln-2...
        
        result = DoubleLinkedList(Node(self.head.value))
        result.insert_node_at_end(Node(self.tail.value))
        
        left_node = self.head.next
        right_node = self.tail.prev
        
        if self.numNodes%2==0:
            for _ in range(self.numNodes//2-1):
                result.insert_node_at_end(Node(left_node.value))
                result.insert_node_at_end(Node(right_node.value))
                left_node = left_node.next
                right_node = right_node.prev
        else:
            for _ in range(self.numNodes//2-1):
                result.insert_node_at_end(Node(left_node.value))
                result.insert_node_at_end(Node(right_node.value))
                left_node = left_node.next
                right_node = right_node.prev   
            result.insert_node_at_end(Node(left_node.value))
       
        return result
                
    
lista = DoubleLinkedList(Node('a'))
lista.insert_node_at_end(Node('b')) 
lista.insert_node_at_end(Node('c')) 
lista.insert_node_at_end(Node('d')) 
lista.insert_node_at_end(Node('e')) 
lista.insert_node_at_end(Node('f'))
lista.insert_node_at_end(Node('g'))  
lista.insert_node_at_end(Node('h')) 
lista.insert_node_at_end(Node('i')) 
#lista.insert_node_at_end(Node('j')) 
lista.print_list() 


# Detecting palindromes
idx = 0
palindromo = True
while idx < lista.numNodes//2:
    item_left = lista.get_node(idx)
    item_right = lista.get_node(lista.numNodes-1-idx)
    if item_left != item_right:
        palindromo = False
        break
    idx += 1

print('No es palíndromo') if not palindromo else print('Es palíndromo')
print('\n')

# Reordering double linked list
lista_orden = lista.change_order()
lista_orden.print_list() 
print('\n')

#%% Pilas - Stacks

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    def is_empty(self):
        return self.top is None
    

# Checking parenthesis consistency

def isValid(s):
    stack = Stack()
    
    for char in s:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

isValid('(())')    
isValid(')(')

#%% Another implementation of stacks in Python

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
    

#%%

def calculator(string) -> int:
    string = string.replace(' ', '')
    stack = []
    current_number = 0 
    operator = '+'
    string += '+'

    for char in string:
        if char.isdigit():
            current_number = current_number*10 + int(char)
        else:
            if operator == '+':
                stack.append(current_number)
            elif operator == '-':
                stack.append(-current_number)
            elif operator == '*':
                stack[-1] *= current_number
            elif operator == '/':
                stack[-1] = int(float(stack[-1]/current_number))
            current_number = 0
            operator = char 
            
    return sum(stack)


print(calculator('3+2*2'))
print(calculator('3/2'))
print(calculator('3+5 / 2'))


#%% Colas de prioridad - Priority queues with the Python heapq library

import heapq
import random


def generate_random_points(a,b,num):
    arr = []
    
    for i in range(num):
        x = random.randint(a, b)
        y = random.randint(a, b)
        arr.append([x,y])
    
    return arr
    

def KClosest(points, k):
    
    def square_distance(point):
        return point[0]**2 + point[1]**2
    
    dists = []
    
    for point in points:
        distance = square_distance(point)
        heapq.heappush(dists, (-distance, point))
        
        if len(dists)>k:
            heapq.heappop(dists)

    k_points = [point for _, point in dists]
    
    return k_points


points = generate_random_points(-100, 100, 10)
print(points)
print(KClosest(points, 3))

#%%

import heapq
from collections import defaultdict

    
def reorganize_string(s: str):
    occurences = defaultdict(int)
    for char in s:
        occurences[char] += 1
        if occurences[char] > (len(s) + 1)/2:
            return ''
    
    priority_queue = [] 
    for char in occurences:
        priority_queue.append((-occurences[char], char))
    heapq.heapify(priority_queue)
    
    string_ordered = []
    
    while 2 <= len(priority_queue):
        occur1, char1 = heapq.heappop(priority_queue)
        occur2, char2 = heapq.heappop(priority_queue)
        string_ordered.append(char1)
        string_ordered.append(char2)
        if occur1 + 1: 
            heapq.heappush(priority_queue, (occur1 + 1, char1))
        if occur2 + 1: 
            heapq.heappush(priority_queue, (occur2 + 1, char2))
     
    if priority_queue:
        return "".join(string_ordered) + priority_queue[0][1]
    
    return ''.join(string_ordered)
        
    
print(reorganize_string('aaacb'))
   

#%%

