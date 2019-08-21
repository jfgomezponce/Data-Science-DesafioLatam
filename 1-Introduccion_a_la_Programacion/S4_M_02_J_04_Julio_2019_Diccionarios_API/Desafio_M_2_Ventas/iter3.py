
'''
Se pide crear un programa llamado iter3.py , que contenga un método llamado filter y que
reciba 2 argumentos, un diccionario y un valor a filtrar, este método tiene que devolver un diccionario
nuevo con los valores superiores al valor ingresado al momento de llamar al programa.
Tips:
Respetar el nombre del programa.
El diccionario utilizado para evaluar puede ser distinto y tener mas o menos meses
Respetar el nombre del método.
Se evaluará el llamado al método .

'''


def filter(diccionario, valor):
	dicc_filtrado = {}
	return {k:v for k,v in diccionario.items() if v > valor}


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

#print(filter(ventas,45000))