'''
Crear el programa iter1.py .
Se solicita iterar el diccionario ventas y mostrar en pantalla todas los ventas superiores a
45000 (sólo el valor de la venta)
Uso:
python iter1.py
81000
91000
Se evaluará el output en pantalla.
El diccionario utilizado para evaluar puede ser distinto y tener más o menos meses.

'''

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

dicc_filtrados = []
for k,v in ventas.items():
	if v > 45000:
		print(v)


