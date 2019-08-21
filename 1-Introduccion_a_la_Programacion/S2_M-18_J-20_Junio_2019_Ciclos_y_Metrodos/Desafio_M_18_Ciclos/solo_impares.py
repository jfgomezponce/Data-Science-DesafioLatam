'''
Crear un programa llamado solo_impares.py , que muestre todos los números impares hasta "n"
(incluyendo "n", si éste es impar), donde "n" es un valor ingresado por el usuario.
Tip: el número siguiente a un par siempre es un impar :)

'''
numero = int(input("numero:\n"))
#for i in range(numero+1):
#	if i%2==0: print(i+1)

for i in range(numero+1):
	if i%2 != 0: print(i)

