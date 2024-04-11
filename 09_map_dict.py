# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:48:56 2023

@author: mmcorrea
"""

items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
    new_item = item.copy()  # Para no modificar la lista inicial de items
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)
