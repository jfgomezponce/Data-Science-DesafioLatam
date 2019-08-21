lista = [1,2,6,7,2,5,8,9,1,3,6,7]
print("lista:", lista)
diccionario = {}

for i in lista:
	if i in diccionario:
		diccionario[i] += 1 # Si ya se creó la instancia, se aumenta 1 el valor
	else:
		diccionario[i] = 1  # Si no está, crea la instancia inicializando el valor, asi se puede sumar en caso de estar despues
print("diccionario 1:",diccionario)

####################################
print("\nUsando GROUPBY...\n")
####################################

from itertools import groupby
lista.sort()  # LOS ELEMENTOS SIEMPRE DEBEN ORDENARSE PARA GROUPBY
diccionario2 = {k: len(list(v)) for k, v in groupby(lista)}
print("diccionario 2:",diccionario2)
