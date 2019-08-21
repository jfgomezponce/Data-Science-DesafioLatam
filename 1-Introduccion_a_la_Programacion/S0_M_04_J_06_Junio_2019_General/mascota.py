masc="gato"
#if masc = "gato": print("qwe")
#if masc == "perro": print("lkj")

valor1 = int(input("Ingrese valor 1"))
valor2 = int(input("Ingrese valor 2"))
if valor1 > valor2:
	print("valor1 {} es mayor".format(valor1))
else:
	if valor1 == valor2:
		print("Ambos valores son iguales")
	else:
		print("valor2 {} es mayor".format(valor2))
