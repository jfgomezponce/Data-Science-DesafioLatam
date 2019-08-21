from itertools import groupby
# Cuenta las ocurrencias del string y lo retorna
# como valor de un diccionario

animales = ["perro","gato","erizo"]
animales.sort() # ['erizo', 'gato', 'perro']

dic = {key: len(list(value)) for key, value in groupby(animales)} 

print(dic)# {'erizo': 1, 'gato': 1, 'perro': 1}