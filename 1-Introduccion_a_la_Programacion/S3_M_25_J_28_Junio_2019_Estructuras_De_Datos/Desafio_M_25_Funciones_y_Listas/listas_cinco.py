'''
5. Generar una lista con los valores flotantes (segundo campo) que sean mayores que el promedio,
utilizando una operación funcional para filtrar estos datos.
La solución debe estar dentro del programa listas_cinco.py .

'''

from velocidad import promedio


auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

lista_autos = [auto1,auto2,auto3,auto4,auto5,auto6]

lista_campo1 = []

for auto in lista_autos:
	lista_campo1.append(auto[1])

promedio_campo1 = promedio(lista_campo1)

filtrada = filter(lambda x: x > promedio_campo1, lista_campo1)
print(list(filtrada))




