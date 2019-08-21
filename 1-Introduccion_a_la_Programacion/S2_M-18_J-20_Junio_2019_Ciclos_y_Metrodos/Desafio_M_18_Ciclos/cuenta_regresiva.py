

'''
Reemplaza la instrucción for por while dentro del programa llamado cuenta_regresiva.py .
La impresión debe ser la misma:

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
for i in range(cuenta_regresiva):
	tmp = cuenta_regresiva
	print("Iteración {}".format(tmp - i))

4 
(Donde i = [0,1,2,3] por eso se resta "tmp - 1" )
Iteración 4
Iteración 3
Iteración 2
Iteración 1

'''

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i = 0
while i < cuenta_regresiva:
	print("Iteración {}".format(cuenta_regresiva - i))
	i+=1