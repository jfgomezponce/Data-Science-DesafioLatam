#!/usr/bin/python

import sys
import math

g = float(sys.argv[1])
r = float(sys.argv[2])

#v_escape = 0
#r_metros = 0
#if g == 9.8 and r == 6371: # Datos de la tierra
r_metros = r*1000
v_escape = math.sqrt(2*g*r_metros)

print ("velocidad: {}".format(v_escape))
