
ingredientes = ["masa tradicional", "salsa de tomate", "queso"]

opcion = 1

while opcion < 6:
	print("¡ Gracias por ordenar con nosotros, ¿Que desea realizar?")
	print("1. Consultar ingredientes de la pizza")
	print("2. Cambiar el tipo de masa")
	print("3. Cambiar el tipo de salsa")
	print("4. Agregar ingredientes")
	print("5. Eliminar ingredientes")
	print("6. Ordenar")

	opcion = int(input())

	if opcion == 1:
		print("Ingredientes seleccionados:", ingredientes)
		print()

	elif opcion == 2:
		# 1. Consultar si entre los ingredientes está la masa tradicional
		if "masa tradicional" in ingredientes:
		# 1.1 Si está, consultar si la desea cambiar por masa delgada
			print("¿Cambiar masa tradicional por masa delgada?")
			print("Escriba 'S' para cambiar, o 'N' para conservar masa tradicional")
			cambiar = input.upper()
		# 1.1.1 Si la quiere cambiar, eliminar de la lista la masa tradicional y agregar la masa delgada
			if cambiar == "S":
				ingredientes.remove("masa tradicional")
				ingredientes.insert(0, "masa delgada")
		# 1.1.2 Si no la quiere cambiar, volver a mostrar el menu

		# 1.2 Si no esta, consultar si la lista tiene la masa delgada
		elif "masa delgada" in ingredientes:
		# 1.2.1 Si está, consultar si la desea cambiar por masa tradicional
			print("¿Cambiar masa delgada por masa tradicional?")
			print("Escriba 'S' para cambiar o 'N' para conservar masa delgada")
			cambiar = input().upper()
		# 1.2.1.1 Si dice que si, eliminar de la lista la masa delgada y agregar masa tradicional
			if cambiar == 'S':
				ingredientes.remove("masa delgada")
				ingredientes.insert(0, "masa tradicional")
		# 1.2.1.2 Si dice que no, volver al menu

		# 1.3 No tiene ningun tipo de masa (else)
		else:
			print("¡Su pizza no tiene masa")
		# 1.3.1 Consultar con un nuevo submenu qué masa desea
			print("Escriba 1 si desea masa tradicional, o 2 si desea masa delgada")
			masa = input()

			if masa == "1":
				ingredientes.insert(0, "masa tradicional")
			elif masa == "2":
				ingredientes.insert(0, "masa tradicional")

	if opcion == 3:
		print()

	if opcion == 4:
		print("¿Que ingredientes desea agregar? (Escriba una de las siguientes opciones)")
		print("Tomate")
		print("Aceituna")
		print("Queso")
		print("Peperoni")
		print("Pollo")
		nuevo = input().lower()

		while nuevo != "tomate" and nuevo != "aceitunas" and nuevo != "queso" and nuevo != "pollo":
			print("Ingrese un ingrediente válido:")
			print("Tomate")
			print("Aceituna")
			print("Queso")
			print("Peperoni")
			print("Pollo")
			nuevo = input().lower()			

		ingredientes.append(nuevo)

	if opcion == 5:
		print("Ingredientes actuales:", ingredientes)
		print("Escriba el ingrediente que se desea eliminar")
		eliminar = input().lower()

		while eliminar not in ingredientes:
			print("Ingredientes actuales:", ingredientes)
			print("Escriba el ingrediente que se desea eliminar")
			eliminar = input().lower()			

		ingredientes.remove(eliminar)




