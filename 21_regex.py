# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:35:35 2024

@author: mdelm
"""

import re

# \d - dígito
# \w - letra
# \s - espacio
# [0-9] - dígito específico. Se puede acotar [6-9] por ej
# [0-9a-zA-Z] - caracter alfanumérico. Se puede acotar rango
# \D - caracter que no sea dígito
# [a-zA-Z] - letra. Se puede acotar rango
# \W - caracter no alfanumérico
# \ - Permite otros caracteres o caracteres especiales \@, @\., @\, .
# {} - Cantidad a encontrar
# \t - tabulador
# * - Contador: cero o muchos
# + - Contador: uno o muchos
# ? - Contador: cero o uno
# ^ y $ - inicio y fin de string, o de línea
# .* - Comodín

# Más detalles en:
    
# https://developers.google.com/edu/python/regular-expressions?hl=es-419
# https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular

"""

Ejemplos:
    
'\d{4}' 4 dígitos consecutivos

"""


fptr = open('liners.txt', 'r')
content = fptr.read()

lines = content.split('\n')

#pattern = '^\-?\d{1-3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6}$'

pattern = "[LOG.*ENTRY].*"

"""

Patrones de ejemplo

Palabra intermedia: [\w.\-]{1,30}
Sólo dígitos: '^\d{1,20}$'

URL: 'https?:\/\/[\w.\-]+\.[a-z]{2,5}\/?'
Correo: '[\w.\-]{1,30}@[\w.\-]+\.[a-z]{2,5}
Coordenadas: '\d{1,3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6}'


'^\[LOG.*\[WARN\].*$'
"LOG.*ENTRY.*"

'https?[\w.\-]{1,30}'

\+?\d+[#pe]?\d*$ - Quiero una línea que puede empezar o no con símbolo de +,
       seguida por 1 o más dígitos, y seguida por #pe, y pueden seguir 
       números hasta acabar $


"""

for i in range(len(lines)-1):
    # re.match(pattern, lines[i]) - con match.group
    match = re.findall(pattern, lines[i])
    if match:
        print(f'{lines[i]}: Encontrado {match}')
        