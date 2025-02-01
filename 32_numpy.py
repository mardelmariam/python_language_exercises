#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:07:16 2025

@author: maryam
"""

import numpy as np

print(np.__version__)

#%%

print(np.show_config())

#%%

# Ayuda de comandos
np.info(np.add)

#%%

Z = np.zeros((10,))
Z[4] = 1
print(Z)

#%%

Z = np.arange(10,52,2)
Z = Z[::-1]

#%%

Z = np.arange(1,10).reshape(3,3)
print(Z)

#%%

Z = np.nonzero([1,2,0,0,4,0,5,0,3,3])
print(Z)

#%%

Z = np.eye(3)
print(Z)

#%%

Z = np.random.random((10,10))
print(Z)

#%%

Z = np.random.randint(1, 1001, 10)
print(Z)

#%%

print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan == np.nan)
print(0 * np.nan)

#%%

Z = np.zeros((8,8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

#%%

Z = np.diag(1+np.arange(4))
print(Z)
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

#%%

Z = np.tile( np.array([[1,0],[0,1]]), (4,4) )
print(Z)

#%%

Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

#%%

Z = np.dot([ [1,6,11],[2,7,12],[3,8,13],[4,9,14],[5,10,15] ], [[1,4],[2,5],[3,6]])
print(Z)

#%%

M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])

dot_result = np.dot(M1, M2)      # Producto matricial estándar
multiply_result = np.multiply(M1, M2)  # Producto elemento a elemento

#%%

Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1

#%%

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


#%%

Z = np.array([1, 3, 2, 5, 4, 7, 6, 9, 8])
print(Z*Z) # producto punto
print(np.dot(Z,Z))
print(np.multiply(Z,Z))
print(2 << Z >> 2) # Desplazamientos en bits 
print(Z < -Z)
print(1j *  Z)

#%%

Z = np.random.uniform(-10,+10,10)
print (np.trunc(Z + np.copysign(0.5, Z)))

#%%

Z = np.random.uniform(0,10,10)
print(Z - Z%1)
print(np.floor(Z))
print(np.ceil(Z)-1)
print(np.round(Z))
print(Z.astype(int))
print(np.trunc(Z))

#%%

def generate():
    for x in range(10):
        yield x
        
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)

#%%

Z = np.linspace(0,1,12)[1:-1]
print(Z)
Z = np.linspace(0,1,12,endpoint=False)
print(Z)

#%%

Z = np.random.random(10)
Z.sort()
print(Z)

#%%

Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1

#%%

Z = np.random.random(10)
print(Z)
Z[Z.argmax()] = 0
print(Z)

#%%

for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
    
#%%

for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)
    
#%%

np.set_printoptions(threshold=np.nan)
Z = np.zeros((25,25))
print(Z)

#%% Point by point distances

Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)

# Much faster with scipy
import scipy
import scipy.spatial

Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)

#%%

Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)

#%% Subtract the mean of each row in a matrix

X = np.random.rand(5, 10)
# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

#%% Sorting an array by the n-th column

Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])

#%% Bin counting, useful for histograms

Z = np.ones(10)
print(Z)
I = np.random.randint(0,len(Z),20)
print(I)
Z += np.bincount(I, minlength=len(Z))
print(Z)

#%%

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print(F)

#%% Moving averages

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

Z = np.random.randint((20,))
print(Z)
print(moving_average(Z, n=3))

#%% Printing floating numbers

# Concentración de huecos entre Ev y Ev-kT en el silicio, a 300 K

def format_number(number, places):
    return ('{0:0.' + str(places) + '}').format(number)

mo = 9.1e-31
kT = 1.38 * 1e-23  * 400
h = 6.626e-34
kT_eV = kT/(1.6e-19)

Nc = 2 * np.power(2 * np.pi * 1.08 * mo * kT / np.power(h,2), 3/2) 
Nc = Nc * 1e-6
print(str(Nc) + " estados/cm^3")

no = Nc * np.exp(-0.25/kT_eV)
print(str(format_number(no, 3)) + " concentración de electrones (cm^-3)")
print(f"{no:.3f} concentración de electrones (cm^-3)")

#%%

