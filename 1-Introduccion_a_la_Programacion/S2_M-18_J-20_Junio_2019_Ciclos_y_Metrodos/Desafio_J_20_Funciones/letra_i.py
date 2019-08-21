'''
2. La función letra_i(n), la cual al ser llamada, dibujará una letra "i" según el ejemplo
letra_i(5)

*****
  *
  *
  *
*****

'''

def letra_i(n):
	ancho = n
	asteriscos = ''
	for i in range(ancho):
		if i == 0 or i == ancho-1:
			asteriscos += '*' * ancho + '\n'
		else:
			asteriscos += ' '* int((ancho-1)/2) + '*' + ' '* int((ancho-1)/2) + '\n'
	#print (asteriscos)
	return asteriscos
string_asteriscos = letra_i(int(input()))
#print(string_asteriscos)