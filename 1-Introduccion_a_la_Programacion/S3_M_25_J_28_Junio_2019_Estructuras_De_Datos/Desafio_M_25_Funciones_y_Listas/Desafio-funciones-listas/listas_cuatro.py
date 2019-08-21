'''
4. Utilizar los valores booleanos de cada lista (penúltimo campo) para mostrar en pantalla el nombre del
auto correspondiente, en caso de que este valor sea True.
La solución debe estar dentro del programa listas_cuatro.py
'''

from velocidad import promedio


auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

lista_autos = [auto1,auto2,auto3,auto4,auto5,auto6]

for autos in lista_autos:
	if autos[-2] is True:
		print(autos[0])

