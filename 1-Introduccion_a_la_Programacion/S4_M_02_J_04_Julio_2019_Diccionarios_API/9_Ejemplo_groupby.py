# pip3 install more-itertools

from itertools import groupby

'''
arreglo_groupby = [(k, list(g)) for k, g in groupby('AAAABBBCCDAABBB')]
print(arreglo_groupby)

[('A', ['A', 'A', 'A', 'A']),
('B', ['B', 'B', 'B']),
('C', ['C', 'C']),
('D', ['D']),
('A', ['A', 'A']),
('B', ['B', 'B', 'B'])]

k va iterando dentro del string AAAABBBCCDAABBB
Dada la funcion list(g) en la posición de los valores, se crea:
una lista que contiene tuplas, y cada tupla contiene un string y una lista con la cantidad de ocurrencias de ese string


# Podemos ocupar este output para generar un diccionario
## Para crear un diccionario se debe cambiar los [] por {}

dic_groupby = {k: len(list(g)) for k, g in groupby('AAAABBBCCD')}

print(dic_groupby)
{'A': 4, 'B': 3, 'C': 2, 'D': 1}

Crea un diccionario donde las claves equivalen al string
y los valores del diccionario equivalen a la cantidad de ocurrencias del string
'''



words = ["hola", "a", "todos", "y", "cada", "uno"]

# Los valores siempre deben estar ordenados !!
# Se ordena la lista en base al largo de las palabras, 
# en orden ascendente (sort recibe key= como parametro, por defecto equivale al valor de la lista, por eso ordena por valor de letras)
words.sort(key=lambda x: len(x))
print("lista orden ascente:",words)
# ['a', 'y', 'uno', 'hola', 'cada', 'todos']

dic = {k: list(v) for k, v in groupby(words, key=len)}
dic2 = {k: list(v) for k, v in groupby(words)}

print("groupby key:",dic) 		# {1: ['a', 'y'], 3: ['uno'], 4: ['hola', 'cada'], 5: ['todos']}

# El siguiente dic2 no es correcto porque crea una lista en base al valor de words
print("groupby no-key:",dic2)	# {'a': ['a'], 'y': ['y'], 'uno': ['uno'], 'hola': ['hola'], 'cada': ['cada'], 'todos': ['todos']}


# Esto NO CAMBIA la forma en que se imprime el diccionario
# TypeError: 'int' object is not iterable
dic3 = {v: list(k) for k, v in groupby(words, key=len)}
print("groupby key:",dic3)	# TypeError: 'int' object is not iterable

