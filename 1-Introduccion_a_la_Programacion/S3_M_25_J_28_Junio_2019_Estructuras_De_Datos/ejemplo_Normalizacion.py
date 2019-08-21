import math

def modulo(lista):
	suma = 0
	for i in lista:
		suma = suma + i**2
	return math.sqrt(suma)

def normalizar(lista):
	m = modulo(lista)
	normalized = []
	for i in lista:
		normalized.append(i/m)
	return normalized

output = normalizar([185,22,36])
print(output)

suma = 0
for i in output:
	suma += i**2
print(suma)