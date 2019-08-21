def imprimir_menu():
	print('Menú: Escoja una acción')
	print('-' * 20)
	print('1) Acción 1')
	print('2) Acción 2')
	print('Escribe "Salir" para terminar el programa')
	print()
opt_menu = 'cualquier valor'

while opt_menu != 'salir' and opt_menu != 'Salir': # Si se cambia por "or" nunca sale e imprime "Saliendo"
	imprimir_menu() # Se llama a la función
	opt_menu = input()
	if opt_menu == '1':
		print('Realizando acción 1')
	elif opt_menu == '2':
		print('Realizando acción 2')
	elif opt_menu == 'salir' or opt_menu == 'Salir': # Se considera tanto salir como Salir
		print('Saliendo')
		# print(opt_menu)
	else:
		print('Opción inválida')
	print()