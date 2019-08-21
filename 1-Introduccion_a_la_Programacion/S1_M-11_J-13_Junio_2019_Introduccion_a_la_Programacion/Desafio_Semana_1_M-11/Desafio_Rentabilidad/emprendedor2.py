#!/usr/bin/python

import sys

'''
Un emprendedor quiere crear una aplicación y necesita saber si es rentable, para eso tiene que:
El producto planea venderse en 50 dólares.
Se espera tener 1000 usuarios en el año.
Los gastos del año son 20000 dólares
Las utilidades se calculan como PRECIO_VENTA * USUARIOS - GASTOS
Los impuestos aplicados a las utilidades son el 35% y solo aplican si es positivo.

Crear el programa emprendedor2.py donde el usuario ingrese el precio, el número de
usuarios totales(incluyendo a usuarios premium y gratuitos), el número de usuarios
premium(pagan el doble), el número de usuarios gratuitos(no pagan) y los gastos. El programa
debe calcular las utilidades.

'''

precio = float(sys.argv[1])
numero_usuarios_totales = float(sys.argv[2])
numero_usuarios_premium = float(sys.argv[3])
numero_usuarios_gratuitos = float(sys.argv[4])
gastos = float(sys.argv[5])

utilidades = 0
#suma_usuarios = numero_usuarios_premium + numero_usuarios_gratuitos

##########
## AMBAS FORMULAS DAN EL MISMO VALOR, YA QUE NO SE TOMA EN CUENTA EL PRECIO DE LOS USUARIOS GRATUITOS... 
##########
utilidades = precio * (2 * numero_usuarios_premium + (numero_usuarios_totales - numero_usuarios_premium - numero_usuarios_gratuitos)) - gastos

#utilidades_2 = ((precio * numero_usuarios_premium) * 2) - gastos


if utilidades > 0:
#	print("positivo")
	utilidad_despues_impuesto = utilidades * 0.65
	print("utilidad: {}".format(utilidad_despues_impuesto))
else: 
#	print("negativo")
	print ("utilidad: {}".format(utilidades))
