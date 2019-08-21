'''

promedio.py : El usuario debe ingresar número. El programa debe sumar todos los números desde 1
hasta el número ingresado. Luego, debe mostrar el resultado de la suma divido por la cantidad de
iteraciones.

'''


import sys

numero_limite = int(input("ingrese N para sumar de 1 a N: "))
i = 0
suma = 0
promedio = 0
while i < numero_limite:
	i+=1
	suma += i

promedio = suma/i
print(promedio)
