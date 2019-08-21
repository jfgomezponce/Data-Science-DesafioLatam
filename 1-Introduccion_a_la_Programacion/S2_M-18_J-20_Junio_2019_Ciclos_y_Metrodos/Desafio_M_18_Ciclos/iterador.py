'''

Reemplazar la instrucción while por for dentro del programa llamado iterador.py .
La impresión debe ser la misma:

i = 0
while i < 50:
	print("Iteración {}".format(i + 1))
	i +=1

'''

for i in range(50):
	print("Iteración {}".format(i+1))