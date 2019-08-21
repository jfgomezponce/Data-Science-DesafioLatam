'''
Ejemplo para unir 2 diccionarios
Descomentar las partes comentadas para ver la diferencia,
NOTAR LA CLAVE =ALTURA= QUE ESTÁ PRESENTE EN AMBOS
'''

dicc1 = {"altura": 175, "edad": 20, "sexo": 'M'}
dicc2 = {"nombre": "juan", "apellido": "perez", "altura": 1.701}

# En este caso, altura conservará la posicion del dicc1 pero con el valor de dicc2
#dicc1.update(dicc2)
#print(dicc1)

# En este caso, altura conservará la posición del dicc2, pero con el valor de dicc1
#dicc2.update(dicc1)
#print(dicc2)

# El diccionario actualizado con update siempre guarda la posicion original de una llave repetida
# sin embargo, guarda el valor del diccionario que se le agrega
