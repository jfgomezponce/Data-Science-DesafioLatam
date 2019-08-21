'''
Ahora necesitamos asociar cada registro de velocidad con la distancia recorrida. Para ello, se debe
implementar la función zip . Ésta debe permitir asociar elementos entre dos listas (una de velocidades, y
otra de distancias).
La solución debe estar dentro del programa asociar.py .


EJEMPLO: 

lista_1 = [1, 2, 3]
lista_2 = ['A', 'B', 'C']

for i in zip(lista_1, lista_2):
	print(i)

# Retorno
# (1, 'A')
# (2, 'B')
# (3, 'C')

Con esta función, se le solicita que cuente todas las observaciones que cumplan por lo menos con una de
las siguientes condiciones:

1- Velocidad bajo el promedio
2- Velocidad bajo el promedio y distancia sobre el promedio.
3- Velocidad sobre el promedio
4- Velocidad sobre el promedio y distancia bajo el promedio.
tip: Puede contar las ocurrencias declarando contadores fuera del loop.

'''

#from velocidad import promedio

def promedio(lista):
	suma = 0
	div = len(lista)
	for i in lista:
		suma += int(i)
	promedioFinal = suma/div

	return(promedioFinal)


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

promedio_velocidad = promedio(velocidad)
promedio_distancia = promedio(distancia)

observacion_1 = 0 # Velocida bajo el promedio
observacion_2 = 0 # Velocidad bajo el promedio y distancia sobre el promedio.
observacion_3 = 0 # Velocidad sobre el promedio
observacion_4 = 0 # Velocidad sobre el promedio y distancia bajo el promedio.

for tuplas_zipeadas in zip(velocidad, distancia):

	if tuplas_zipeadas[0] < promedio_velocidad:
		observacion_1 += 1
	if tuplas_zipeadas[0] < promedio_velocidad and tuplas_zipeadas[1] > promedio_distancia:
	 	observacion_2 += 1
	if tuplas_zipeadas[0] > promedio_velocidad:
	 	observacion_3 += 1
	if tuplas_zipeadas[0] > promedio_velocidad and tuplas_zipeadas[1] < promedio_distancia:
	 	observacion_4 += 1

print(observacion_1)
print(observacion_2)
print(observacion_3)
print(observacion_4)	




