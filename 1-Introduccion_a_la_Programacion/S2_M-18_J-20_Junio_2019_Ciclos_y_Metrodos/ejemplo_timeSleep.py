'''
import time

time.sleep(5)
print("Boom")

def maquina_escribir(array_input):
	for each_char in array_input:
		time.sleep(1)
		print(each_char)

frase = input("Nombre: ")
maquina_escribir(frase)

'''
from time import sleep

print('LOADING...')
sleep(4) # Si se importa from time, no es necesario escribir "time.sleep(), solo sleep()"

loading = input("Ingresa un string: ")
for i in range(len(loading)):
	print(loading[i].upper(), sep=' ', end=' ', flush=True); sleep(0.1)

	# Imprime un string, letra por letra. 
	# Si flush se cambia a False, se imprime todo el string de una, no respeta el tiempo de sleep(0.1)
print("\n")