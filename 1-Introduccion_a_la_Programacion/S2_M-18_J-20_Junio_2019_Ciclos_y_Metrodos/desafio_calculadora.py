'''
calculadora.py : Crear un programa que permita ingresar de 4 opciones, identificadas con un
número (1: sumar, 2: restar, 3: multiplicar, 4: dividir). Luego el usuario debe ingresar 2 números, sobre
los cuales se realice la operación escogida. El programa debe mostrar el resultado.
'''
from os import system
from time import sleep

system("clear")
print("Qué hacer?:\n1: sumar\n2: restar\n3: multiplicar\n4: dividir\n5: Salir")
opcion = int(input())
while opcion > 5 or opcion < 1:
	print("\n{} No es una opcion valida!!\n".format(opcion))
	print("Qué hacer?:\n1: sumar\n2: restar\n3: multiplicar\n4: dividir\n5: Salir")
	opcion = int(input())

while opcion < 5 and opcion > 0:
	
	if opcion == 1:
		system("clear")	
		print("ingresar 2 valores para sumar: ")
		valor1 = int(input("Ingresar primer valor: "))
		valor2 = int(input("Ingresar segundo valor: "))

		valor3 = valor1+valor2
		print(valor3)
		sleep(1)

	elif opcion == 2:
		system("clear")
		print("ingresar 2 valores para restar: ")
		valor1 = int(input("Ingresar primer valor: "))
		valor2 = int(input("Ingresar segundo valor: "))

		valor3 = valor1-valor2
		print(valor3)
		sleep(1)

	elif opcion == 3:
		system("clear")
		print("ingresar 2 valores para multiplicar: ")
		valor1 = int(input("Ingresar primer valor: "))
		valor2 = int(input("Ingresar segundo valor: "))

		valor3 = valor1*valor2
		print(valor3)
		sleep(1)

	elif opcion == 4:
		system("clear")
		print("ingresar 2 valores para dividir: ")
		valor1 = int(input("Ingresar primer valor: "))
		valor2 = int(input("Ingresar segundo valor: "))

		valor3 = valor1/valor2
		print(valor3)
		sleep(1)

	print("\n")
	print("Qué hacer ahora?:\n1: sumar\n2: restar\n3: multiplicar\n4: dividir\n5: Salir")
	opcion = int(input())
	while opcion > 5 or opcion < 1:
		print("\n{} No es una opcion valida!!\n".format(opcion))
		print("Qué hacer?:\n1: sumar\n2: restar\n3: multiplicar\n4: dividir\n5: Salir")
		opcion = int(input())

if opcion == 5:
	system("clear")
	salir = 'saliendo...'
	for each in range(len(salir)):
		print(salir[each].upper(), sep=' ', end=' ', flush=True)
		sleep(0.2) #flush= False caga todo
	print("\n")


