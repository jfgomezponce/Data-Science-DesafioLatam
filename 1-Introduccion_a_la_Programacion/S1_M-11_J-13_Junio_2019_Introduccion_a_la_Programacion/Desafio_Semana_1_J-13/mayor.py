'''

Se pide crear el programa mayor.py este script debe tomar los 3 argumentos y determinar cual es el
mayor.
Uso:
python mayor.py 10 5 3
10
python mayor.py 10 15 7
15
python mayor.py -21 9 39
39
python mayor.py 3 2 3
3

'''

import sys

Lista_numeros = [int(i) for i in sys.argv[1:]]
print(max(Lista_numeros))