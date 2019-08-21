
# Desafio 1

import numpy as np
array_1_50 = np.linspace(1,50)
#array_50_150 = np.linspace(50,150,101) 
# Se agrega el tercer argumento para generar un array de 101 elementos. 
# Por default el tercer argumento es 50, por lo que genera un array de 50 elementos entre 50 y 150
# Si se deja como (50,150), no generara numeros enteros, o sea:
# len(array_50_150) imprime 50
#
# Pero luego:
# array_50_150 = np.linspace(50,150,101)
# len(array_50_150) imprime 101

# Por convencion, se dejó como:
array_50_150 = np.linspace(50,150,dtype=int)
# De esta forma sólo se crearan 50 numeros enteros solamente


# Desafio 2

#for i in array_1_50:
#	if i % 2 == 0: print(i,"es par")
#	else: print(i,"es impar")



# Desafio 3
'''

div_2_o_3 = 0
div_2_y_3 = 0
div_3_no_2 = 0
no_div_3_ni_2 = 0

for i in array_50_150:
	if (i % 2==0) or (i % 3==0):	div_2_o_3 +=1
	elif (i % 2==0) and (i % 3==0):	div_2_y_3 +=1
	elif (i % 3 == 0) and (i % 2 != 0): div_3_no_2 +=1
	elif (i % 2 != 0) and (i % 3 != 0): no_div_3_ni_2 +=1
print("números divisibles por 2 o 3: {}\n\
números divisibles por 2 y 3: {}\n\
números divisibles por 3 pero no por 2: {}\n\
números no divisibles por 2 ni 3: {}".format(div_2_o_3,div_2_y_3,div_3_no_2,no_div_3_ni_2))



# Desafio 4

for i in range(100):
    print(i**2) # I debe ser reemplazado por i para acceder al elemento



# Desafio 5

import pandas as pd


df = pd.read_csv('flights.csv')

df['underperforming'] = 0

media = df['passengers'].mean()

for ids,fila in df.iterrows():
	if fila['passengers'] < media:
		df.set_value(ids,'underperforming',1)

print(df.head())
'''

# DESAFIO 6

import pandas as pd
df = pd.read_csv('flights.csv')

media = df['passengers'].mean()
desv_std = df['passengers'].std()

df['outlier'] = 0

for ids, fila in df.iterrows():
	if fila['passengers'] < (media - desv_std):
		df.set_value(ids,'outlier',1)
	if fila['passengers'] > (media + desv_std):
		df.set_value(ids,'outlier',1)

print(df['outlier'].value_counts())


