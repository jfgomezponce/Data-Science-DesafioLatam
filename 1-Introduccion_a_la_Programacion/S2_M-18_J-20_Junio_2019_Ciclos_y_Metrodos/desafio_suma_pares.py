'''
suma_pares.py : El programa debe sumar solo los números pares entre 1 y 100, y mostrar ese
resultado. tip: Utilize % (módulo).

'''

lista_numeros = range(101)
for cada_numero in lista_numeros:
	if cada_numero % 2 == 0: # Verifica si el resto es cero
		print(cada_numero, " -> par")

print(7%2)