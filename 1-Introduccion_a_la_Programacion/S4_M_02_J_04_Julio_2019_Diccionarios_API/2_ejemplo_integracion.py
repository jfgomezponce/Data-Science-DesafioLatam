diccionario_productos = {"celular":140000, "notebook":489990, "tablet":120000, "cargador":12400}

diccionario_caros = {}
diccionario_productos_2 = {}

for key, value in diccionario_productos.items():
	if value < 120000:
		diccionario_productos[key] = int(value * 0.9) # HAce un 10% de descuento si es que el valor es menor a 120000 y modifica el valor original
		#diccionario_productos_2[key] = int(value * 0.9) # HAce un 10% de descuento y lo agrega al diccionario nuevo
	else:
		diccionario_caros[key] = value # Si el valor es mayor a 120000, asigna el producto a un nuevo diccionario_caros

print(diccionario_productos)
#print(diccionario_productos_2) # Si se descomenta, se debe descomentar la linea del "if"
print(diccionario_caros)