'''
Se pide crear el programa velocidad.py que dada la información de velocidad promedio de distintos
vehículos se pueda entregar cierta información.

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

Se pide:
Crear una función llamada promedio que devuelva la velocidad promedio de los vehículos en la lista.

tips:_
La corrección del ejercicio funciona llamando a la función promedio , por lo que la función debe existir
y el valor ser el promedio de cualquier arreglo ingresado
Puede probar el programa llamando a la función y mostrando el resultado pero no es necesario que el
programa entregue resultado alguno. La revisión se hace llamando a la función.

'''

# import statistics
# def promedio(lista):
# 	return statistics.mean(lista)



# HACERLO A MANO

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


#print(promedio(velocidad))









