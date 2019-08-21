
diccionario_productos = {140000: "celular", 489990: "notebook", 120000: "tablet", 12400: "cargador"}
diccionario_invertido = {}

print("Diccionario Original: ",diccionario_productos)

for key,value in diccionario_productos.items():
	diccionario_invertido[value] = key

print("Diccionario invertido: ",diccionario_invertido)

diccionario_invertido_comprehension = { v:k for k,v in diccionario_productos.items()}
print("Comprehension inverted dicc: ",diccionario_invertido_comprehension)