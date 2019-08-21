'''
Crear un programa llamado busqueda.py que pueda buscar a cuál mes pertenece una o mas cifras
específicas. En caso de no encontrarlo mostrar el mensaje "no encontrado"
Uso:
python busqueda.py 15000 31000 27000
Enero
no encontrado
no encontrado
Se asumirá que en ningún mes la venta se repite.
Tips:
Se evalúa la salida en pantalla por lo que se debe respetar el formato de los mensajes.
Se evaluará con un diccionario distinto al mostrado.

'''
import sys

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

aux = 0
#print(sys.argv[1:])
for i in sys.argv[1:]:
	for k , v in ventas.items():
		if v == int(i):
			print(k)
			aux = True
			break
		else:
			aux = False
	if aux == False:
		print("no encontrado")