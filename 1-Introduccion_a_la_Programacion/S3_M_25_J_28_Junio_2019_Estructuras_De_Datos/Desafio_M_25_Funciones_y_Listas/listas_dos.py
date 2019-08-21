'''
2. Utilizar la función construída en el Desafío - Velocidad para obtener la media entre los 6 autos para
cada uno de los campos numéricos. Puede hacer uso de un loop.
La solución debe estar dentro del programa listas_dos.py .

'''

from velocidad import promedio # importacion de la funcion "promedio" del script "valocidad.py"

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

lista_autos = [auto1,auto2,auto3,auto4,auto5,auto6]

# listas columnas = [1, 2 ,4]
lista_campo1 = []
lista_campo2 = []
lista_campo4 = []

for auto in lista_autos:

	lista_campo1.append(auto[1])
	lista_campo2.append(auto[2])
	lista_campo4.append(auto[4])

# lista_Promedio_campo1 = promedio(lista_campo1)
# lista_Promedio_campo2 = promedio(lista_campo2)
# lista_Promedio_campo4 = promedio(lista_campo4)

# lista_final = [lista_Promedio_campo1, lista_Promedio_campo2, lista_Promedio_campo4]
# print(lista_final)

print(promedio(lista_campo1))
print(promedio(lista_campo2))
print(promedio(lista_campo4))


