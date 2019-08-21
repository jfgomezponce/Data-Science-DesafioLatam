#!/usr/bin/python

import sys

'''
Un emprendedor quiere crear una aplicación y necesita saber si es rentable, para eso tiene que:
El producto planea venderse en 50 dólares.
Se espera tener 1000 usuarios en el año.
Los gastos del año son 20000 dólares
Las utilidades se calculan como PRECIO_VENTA * USUARIOS - GASTOS
Los impuestos aplicados a las utilidades son el 35% y solo aplican si es positivo.

Crear el progama emprendedor1.py donde el usuario ingrese el precio, el número de
usuarios, los gastos y el programa calcula las utilidades.

'''

precio_venta = float(sys.argv[1])
usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

utilidades = precio_venta * usuarios - gastos

if utilidades > 0:
#	print("positivo")
	utilidad_despues_impuesto = utilidades * 0.65
	print("utilidad: {}".format(utilidad_despues_impuesto))
else: 
#	print("negativo")
	print ("utilidad: {}".format(utilidades))