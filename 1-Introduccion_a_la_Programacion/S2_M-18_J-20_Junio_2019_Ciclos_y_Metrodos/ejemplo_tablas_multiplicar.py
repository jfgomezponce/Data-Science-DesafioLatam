
'''
Supongamos que queremos mostrar una tabla de multiplicar. Por ejemplo la tabla del 5. Esto se puede
escribir como:

for i in range(10):
	print("5 * {} = {}".format(i, (5 * i)))

5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45


¿Cómo podríamos hacer para mostrar todas las tablas de multiplicar del 1 al 10?
Fácil, envolviendo el código anterior en otro ciclo que itere de 1 a 10.

'''


for k in range(1,11):   # Ciclo que recorre del 1 al 10
	for i in range(10):
		print("{} * {} = {}".format(k,i, (k * i)))
	print("\n")