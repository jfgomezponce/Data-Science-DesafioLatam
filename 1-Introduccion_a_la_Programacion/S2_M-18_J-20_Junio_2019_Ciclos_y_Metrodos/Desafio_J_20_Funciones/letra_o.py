'''
1. La función letra_o(n) , la cual al ser llamada, dibujará una letra "o" según el ejemplo
letra_o(n)

*****
*   *
*   *
*   *
*****

'''

def letra_o(n):
	ancho = n
	asterisco = ''
	for i in range(ancho):
		if i == 0: # primera linea
			asterisco += '*' * ancho + '\n'
		elif i == ancho-1: # ultima linea
			asterisco += '*' * ancho + '\n'
		else:
			asterisco += '*' + ' '*(ancho-2)  + '*'+ '\n'

	#print(asterisco)
	return asterisco[:-1] # Se debe eliminar el salto de linea final porque el GRADER no lo pesca...
#letra_o(int(input()))
string_asteriscos = letra_o(int(input()))
#string_asteriscos = letra_o()
#print(string_asteriscos[:-1])