#!/usr/bin/python

import sys

'''
Un emprendedor quiere crear una aplicación y necesita saber si es rentable, para eso tiene que:
El producto planea venderse en 50 dólares.
Se espera tener 1000 usuarios en el año.
Los gastos del año son 20000 dólares
Las utilidades se calculan como PRECIO_VENTA * USUARIOS - GASTOS
Los impuestos aplicados a las utilidades son el 35% y solo aplican si es positivo.

Crear el programa emprendedor3.py donde el usuario ingrese:
1 - el precio
2 - el número de usuarios
3 - Los gastos
4 - las utilidades del año anterior, este último parámetro será optativo, si el
usuario no lo ingresa se asumirá 1000 como base.

Debes sumar las utilidades del año anterior al resultado final de las utilidades

'''

if len(sys.argv) == 5:
	Lista_Argumentos = [float(i) for i in sys.argv[1:5]]
	utilidades = (Lista_Argumentos[0] * Lista_Argumentos[1]) - Lista_Argumentos[2]
elif len(sys.argv) == 4:
	Lista_Argumentos = [float(i) for i in sys.argv[1:4]]
	Lista_Argumentos.append(1000)
	utilidades = (Lista_Argumentos[0] * Lista_Argumentos[1]) - Lista_Argumentos[2]
else:
	pass

#SUMO A UTILIDADES PERO DESPUES DE IMPUESTOS

if utilidades > 0:
#	print("positivo")
	utilidad_despues_impuesto = utilidades * 0.65
	utilidad_despues_impuesto = utilidad_despues_impuesto + Lista_Argumentos[3]
	print("utilidad: {}".format(utilidad_despues_impuesto))
else: 
#	print("negativo")
	utilidades = utilidades + Lista_Argumentos[3]
	print ("utilidad: {}".format(utilidades))