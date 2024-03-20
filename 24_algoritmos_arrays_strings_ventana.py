# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:08:35 2024

@author: mdelm
"""


# Longest substring without repeating characters

"""
Dada una cadena s, encontrar la longitud de la subcadena más larga sin repetir
caracteres
"""




def duplicated_letters(string):
    
    for letter in string:
        if string.count(letter)>1:
            return True
        
    return False


def longest_substring(string):
    
    n = len(string)
    
    max_long = 0
    
    idx1 = 0
    idx2 = 1
 
    while idx1<idx2 and idx1<n-2:
        if idx2 == n-1:
            idx1 +=1
            idx2 = idx1+1
        substring = string[idx1:idx2]
        if not duplicated_letters(substring):
            long = idx2-idx1
            if long > max_long:
                max_long = long
            idx2 +=1
        else:
            idx1 +=1
            idx2 = idx1+1
    
    print(max_long)



def lengthOfLongestSubstring(self, s: str) -> int:
    inicio = 0
    caracteresAposicion = {}
    mayorLongitud = 0
    for fin in range(len(s)):
        if s[fin] in caracteresAposicion and inicio <= caracteresAposicion[s[fin]]:
            inicio = s[fin] + 1
        caracteresAposicion[s[fin]] = fin
        mayorLongitud = max(mayorLongitud, fin - inicio + 1)
    return mayorLongitud      
        
            
s = 'abcabcbb' # 3
longest_substring(s)
s = 'jdkafnlcdsalkxcmpoiuytfccv' # 15      
longest_substring(s)

