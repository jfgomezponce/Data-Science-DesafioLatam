#!/usr/bin/python
from os import system

#password = ()
system("clear")
password = str(input("Ingrese una contrasenha: "))
system("clear")
if len(password)<6: print("AVISO, password muy corta!!\n")
elif password == "12345": print("password incorrecto\n")
else: print("password {} ingresado satisfactoriamente".format(password))
