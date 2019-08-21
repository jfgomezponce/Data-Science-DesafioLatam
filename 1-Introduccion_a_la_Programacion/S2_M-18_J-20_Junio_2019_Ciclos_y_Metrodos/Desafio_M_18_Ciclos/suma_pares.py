'''
Crear un programa llamado suma_pares.py que sume todos los números pares hasta "n" (incluyendo "n"
si éste es par), donde "n" es ingresado por el usuario.
Tip: El cero no es par; no afecta en la suma, pero se debe tener cuidado con los bordes del ciclo.
uso: python suma_pares.py
	2 + 4 + 6 + 8 + 10 # iteraciones
	30 # salida
'''
iteraciones = ''
suma = 0
numero = int(input("numero:\n"))
for i in range(1,numero+1):
	if i % 2 == 0:
		suma += i
#		iteraciones += '{} + '.format(i)
#print("{}".format(iteraciones[:-2]))
print(suma)