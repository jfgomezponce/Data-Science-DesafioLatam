
'''
Se pide crear el programa juego.py , el usuario pasará como argumento piedra, papel o tijera, el programa
escogerá una opción al azar jugará con número al azar.

Para que el computador pueda jugar escoger un número al azar entre 1 y 3, si es 1 entonces en piedra, si es
2 entonces papel y 3 tijera.

### python juego.py piedra
### Computador juega tijera
### Ganaste

En caso que el argumento sea distinto a piedra papel o tijera el programa debe mostrar las opciones que se
pueden jugar.
python juego.py papelon
Argumento inválido: Debe ser piedra, papel o tijera.

tijera < piedra
tijera > papel
papel > piedra

Segun abc: 
piedra = 2
papel = 1
tijera = 3


'''
import sys
from random import randint

jugador = 0
lista_opciones = ['piedra','papel','tijera']
if sys.argv[1] not in lista_opciones: print("Argumento inválido: Debe ser piedra, papel o tijera.")
else: 
	#jugador = lista_opciones.index(sys.argv[1])

	#print(jugador) # tijera = 2
	#jugador_versus = jugador + 1 # Para que sea de: 0 a 2 -> 1 a 3

	jugador_versus = sys.argv[1]

	Computador = randint(0,2)
	print("tu jugaste:     ", jugador_versus)
	print("Computador juega",lista_opciones[Computador])
	Computador_versus = lista_opciones[Computador]

	if jugador_versus == 'tijera' and Computador_versus == 'papel': print("Ganaste")
	elif jugador_versus == 'papel' and Computador_versus == 'piedra': print("Ganaste")
	elif jugador_versus == 'piedra' and Computador_versus == 'tijera': print("Ganaste")
	elif jugador_versus == Computador_versus: print("Empataste")
	else: print("Perdiste")

#if lista_opciones[Computador-1] == True:
#else:
#	print("Argumento inválido: Debe ser piedra, papel o tijera.")


