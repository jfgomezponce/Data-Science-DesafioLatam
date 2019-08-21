####################################
# Convertir un diccionario en lista
####################################
# Utilizando la funcion list() con items())

dic = {"k1": 5, "k2": 7}
lista_from_dic = list(dic.items())
print("dic_2_list:", lista_from_dic)

print("dic_2_list:",list({"k1": 5, "k2": 7}.items()))


####################################
# Convertir una lista en diccionario
####################################
# Se debe entregar una lista de tuplas

lista_tuplas = [("k1",5),("k2",7)]
dic_de_lista = dict(lista_tuplas)
print(dic_de_lista)

print(dict([("k1",5),("k2",7)]))


####################################
# Crear diccionario de dos listas
####################################

nombres = ["Alumno1", "Alumno2", "Alumno3"]
notas = [10, 3, 8]

# PRIMERA FORMA
notas_por_alumno = {}

for i in range(len(nombres)):
	nombre = nombres[i]
	nota = notas[i]
	notas_por_alumno[nombre] = nota

print(notas_por_alumno)

# SEGUNDA FORMA, MAS OPTIMA, usando dict() y zip() en conjunto

print(dict(zip(nombres, notas)))