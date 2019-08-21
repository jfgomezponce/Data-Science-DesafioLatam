'''

Generar programa agrupados.py
Se solicita generar un diccionario con "n" claves, una para cada posible valor de venta dentro del
diccionario.
Para cada clave generada, se debe indicar cuántas veces estuvo presente ese valor.

'''
from itertools import groupby

ventas = {
	"Enero": 15000,
	"Febrero": 22000,
	"Marzo": 12000,
	"Abril": 17000,
	"Mayo": 81000,
	"Junio": 13000,
	"Julio": 21000,
	"Agosto": 41200,
	"Septiembre": 25000,
	"Octubre": 21500,
	"Noviembre": 91000,
	"Diciembre": 21000,
}

#dicc_inv = { v:k for k,v in ventas.items()}
valores = list(ventas.values())

valores.sort()
#print(len(valores))
dic2 = {k: len(list(v)) for k, v in groupby(valores)}
print(dic2)