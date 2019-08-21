




def mostrar_menu(saldo = 0):
	print("Bienvenido al portal del Banco Amigo. Escoja una opción:\n\
		1. Consultar saldo\n\
		2. Hacer depósito\n\
		3. Realizar giro\n\
		4. Salir\n")


def depositar(saldo, cantidad):
	saldo2 = saldo + cantidad
	return saldo2


def girar(saldo, cantidad):
	if cantidad < saldo:
		saldo2 = saldo - cantidad
		return saldo2
	else: return False



mostrar_menu()
opcion = int(input())
saldo = 0

while opcion > 4 or opcion < 1: 
	print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.\n")
	mostrar_menu()
	opcion = int(input())

while opcion < 4 and opcion > 0:
	if opcion == 1:
		print("Su saldo es de",saldo)
		mostrar_menu()
		opcion = int(input())

	elif opcion == 2:
		cantidad = int(input("ingresar cantidad a depositar: "))
		saldo = depositar(saldo,cantidad)
		print("Su nuevo saldo es de",saldo)
		mostrar_menu()
		opcion = int(input())

	elif opcion == 3:
		if saldo > 0:
			cantidad = int(input("ingresar cantidad a girar: "))
			saldo = girar(saldo,cantidad)
			if saldo is False: print("No puede realizar giros. Su saldo es de",saldo)
			else: print("Su nuevo saldo es de",saldo)
		else: print("No puede realizar giros. Su saldo es 0")
		mostrar_menu()
		opcion = int(input())

	#elif opcion == 4:
	#	break






