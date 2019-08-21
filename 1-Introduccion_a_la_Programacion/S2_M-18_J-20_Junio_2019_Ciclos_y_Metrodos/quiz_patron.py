import sys

pat1 = "(>'-')>"
pat2 = "(^_^)"
patron = ""

limite = int(sys.argv[1])

for i in range(limite):
	if i%3 == 0:
		patron += pat1
	else:
		patron += pat2
print(patron)
