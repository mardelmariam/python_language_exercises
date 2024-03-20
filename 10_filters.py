# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:45:13 2023

@author: mmcorrea
"""

numbers = [1,2,3,4,5]
new_numbers = filter(lambda x: x%2==0, numbers)
print(list(new_numbers))

#%%


matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))


#%%


def filter_by_length(words):
   resu = list(filter(lambda item: len(item)>3, words))
   return resu

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)


