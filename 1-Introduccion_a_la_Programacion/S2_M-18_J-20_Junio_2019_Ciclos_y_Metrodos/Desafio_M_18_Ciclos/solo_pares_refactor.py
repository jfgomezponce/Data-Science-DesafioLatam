'''
1. Crear un programa llamado solo_pares.py , que muestre todos los números pares hasta "n"
(incluyendo "n", si éste es par), donde "n" es un valor ingresado por el usuario.
uso: python solo_pares.py

2. Crear una variante del programa anterior llamado solo_pares_refactor.py . En este caso, el cero no
debe ser considerado (el cero no es par).

'''

numero = int(input("numero:\n"))
for i in range(1,numero+1):
	if i%2==0: print(i)