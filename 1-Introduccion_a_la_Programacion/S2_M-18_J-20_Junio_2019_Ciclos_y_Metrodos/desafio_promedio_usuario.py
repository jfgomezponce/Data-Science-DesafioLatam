'''
promedio_usuario.py : El usuario debe ingresar un número, el cual indica al programa la cantidad de
datos que se van a ingresar. Luego, debe ingresar la cantidad de datos indicada. El programa debe
mostrar el promedio de los datos ingresados a continuación del primer argumento.

'''

import sys

numero_limite = int(sys.argv[1])
i = 0
suma = 0
promedio = 0

while i < numero_limite:
	i += 1
	dato = int(input("ingresar dato {}: ".format(i)))
	suma += dato
#	dato += dato # Si se hace esto, se duplica el primer numero, ya que dato no comenzaria en cero, sino en el primer valor que le da el usuario

promedio = suma/i
print("argumento 1: {}\nPromedio de los {} datos: {}".format(sys.argv[1], i, promedio))


