#!/usr/bin/python
from os import system
system("clear")
password = str(input("pass:"))

while len(password) < 6:
	print("Pass debe ser > 7 letras")
	if password == "12345": print("incorrecto\n")
	password = str(input("ingrese pass again:"))
print("perfect")
