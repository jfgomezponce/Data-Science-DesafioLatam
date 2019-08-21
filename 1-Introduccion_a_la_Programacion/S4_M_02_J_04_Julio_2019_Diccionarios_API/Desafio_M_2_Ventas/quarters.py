'''
Generar programa quarters.py
Se pide generar un diccionario, llamado quarters , con las ventas de cada trimestre. Las claves
tienen que ser "Q1" , "Q2" , "Q3" , "Q4" .
Tips:
Los valores ingresados serán distintos.
El diccionario de resultados debe llamarse quarters , pues este será el que se evalúe.
¿Se necesitan los keys?
¿Necesitamos iterar elementos, o elementos e índices a la vez?
'''
quarters = {}
quarters = {"Q1":0, "Q2":0 , "Q3":0, "Q4":0}

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

# print(len(list(ventas)))
# print(list(ventas))

# for i in range(0,len(ventas),3):
# 	print(i)

quarters = {
"Q1": sum([ventas["Enero"],ventas["Febrero"],ventas["Marzo"]]),
"Q2": sum([ventas["Abril"],ventas["Mayo"],ventas["Junio"]]),
"Q3": sum([ventas["Julio"],ventas["Agosto"],ventas["Septiembre"]]),
"Q4": sum([ventas["Octubre"],ventas["Noviembre"],ventas["Diciembre"]])
}
