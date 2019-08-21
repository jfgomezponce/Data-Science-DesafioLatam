'''
Se busca crear un programa fuerza_bruta.py que revise cuántos intentos se requieren para hackear un
password por fuerza bruta.

Uso: python fuerza_bruta.py
	Ingresa contraseña
	gato
	43 intentos

Para ello, el programa debe intentar todas las combinaciones de letras posibles, en orden alfabético, hasta
que la combinación de letras sea igual a la de la contraseña indicada. Deberá hacer este proceso letra por
letra, de izquierda a derecha.
Es decir:
	- Primero probará con a, luego b, luego c ... hasta z, o hasta que encuentre una letra igual a la primera
		letra de la contraseña.
	- Suponiendo que la primera letra correspondía a "d", después empezará a comparar la segunda letra
		de la forma da, db, dc, dd... hasta encontrar la coincidencia de la segunda letra.
	- Suponiendo que la segunda letra era "e", continuará luego comparando la tercera letra de la forma
		dea, deb, dec ...etc.
	- Y así sucesivamente hasta completar la comparación con cada letra de la contraseña.

password <- gato
## recorrer password = g a t o
recorrer password = g
	correr el abcdario por cada letra: 
		obtener la letra (cada intento suma 1)
			obtiene letra: 
				guarda la letra en una variable.
recorrer password = a



'''
import string
lista_abc = string.ascii_letters[:26]
#print(lista_abc) #abcdefghijklmnopqrstuvwxyz

password = str(input("Ingresa contraseña\n"))
intentos = 0
string_pass = ''

for i in password:
	intento = 0
	for k in lista_abc:
		intento += 1
		if i == k:
			string_pass += k
			intentos += intento
			#print("{} encontrada con {} - intentos {}".format(i,k,intento))
			continue
		else:
			continue
#print(string_pass)
print(intentos,"intentos")
	
