import sys

limite = int(input("ingrese limite N a sumar: "))

i = 0
suma = 0

while i < limite:
	i += 1
	suma += i
print("Sumatoria de 1 a {} es: {}".format(limite,suma))
