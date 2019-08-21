
# VERSION DE LOS VIDEOS
n = 5
contain = ""

for i in range(n+1):
	contain += "*" * i + "\n"
print(contain)

n = 5
contain = ""

for i in range(n): #range(5) ==  0 a 4 
	for j in range(n - i): # El contador j lo ignora, se crea pero no se utiliza
		# (Adiciona un * por cada iteracion)
		# print(i,j, range(n - i))
	#    n    i j 
		#5	# 0 0 range(0, 5) == 0 1 2 3 4 
		#5	# 0 1 range(0, 5)
		#5	# 0 2 range(0, 5)
		#5	# 0 3 range(0, 5)
		#5	# 0 4 range(0, 5)
		#5	# 1 0 range(0, 4) == 0 1 2 3
		#5	# 1 1 range(0, 4)
		#5	# 1 2 range(0, 4)
		#5	# 1 3 range(0, 4)
		#5	# 2 0 range(0, 3) == 0 1 2
		#5	# 2 1 range(0, 3)
		#5	# 3 1 range(0, 3)
		#5	# 2 2 range(0, 2) == 0 1
		#5	# 3 0 range(0, 2)
		#5	# 4 0 range(0, 1) == 0

		contain += "*"
	contain += "\n"
print(contain)



'''

Version mia, mejorada y más óptima:
EN CASO DE PREGUNTA, HACERLO DE ESTA FORMA, ASI QUEDA PERFECTO EL TRIANGULO
Y ADEMAS NO SE CREAN VARIABLES INNECESARIAMENTE.

n = 5
contain = ""

for i in range(n+1):
	contain += "*" * i + "\n"
print(contain[:-1])

contain = ""
for i in range(5,0,-1):
	contain += "*" * i + "\n"
print(contain)



'''