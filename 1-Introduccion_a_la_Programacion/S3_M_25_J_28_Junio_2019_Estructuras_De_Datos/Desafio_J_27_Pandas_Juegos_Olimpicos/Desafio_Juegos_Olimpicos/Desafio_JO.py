'''
DESAFIO JUEGOS OLIMPICOS

Por parte de la organización de los Juegos Olímpicos, se nos ha solicitado realizar un análisis de
todos los competidores a lo largo de las olimpiadas. Para lograr este análisis, se requiere:

1. Importar la base de datos athlete_events.csv , y reportar la cantidad de registros (filas) y
de campos (columnas). El resultado debe guardarse en una variable llamada ejercicio_1 .
tip: Puede hacer uso de .shape para esto.

2. Reportar cuántas competencias se han realizado a lo largo del tiempo. El resultado debe ser
un número entero y debe guardarse en una variable llamada ejercicio_2 .

3. Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los juegos
olímpicos de Verano como en los de Invierno. El resultado debe guardarse en una variable
llamada ejercicio_3 .

4. Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El resultado debe
guardarse en una variable llamada ejercicio_4 .
tip: Investige sobre las funciones min() y unique() de una Serie de pandas.

5. Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El resultado
debe guardarse en una variable llamada ejercicio_5 .

6. Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo de los
juegos. El resultado debe guardarse en una variable llamada ejercicio_6 .

7. Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe
guardarse en una variable llamada ejercicio_7 .

8. Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. El
resultado debe guardarse en una variable llamada ejercicio_8

'''

# Recomendación, las variables deben contenter solo los resultados, no concatenes strings en ellas
# Recomendación, para cargar el archivo athlete_events.csv, usa rutas relativas.

import pandas as pd 

df = pd.read_csv('athlete_events.csv')

###################################
# 1. Importar la base de datos athlete_events.csv , y reportar la cantidad de registros (filas) y
# de campos (columnas). El resultado debe guardarse en una variable llamada ejercicio_1 .
# tip: Puede hacer uso de .shape para esto.
ejercicio_1 = df.shape
###################################

###################################
# 2. Reportar cuántas competencias se han realizado a lo largo del tiempo. El resultado debe ser
# un número entero y debe guardarse en una variable llamada ejercicio_2 .
#ejercicio_2 = df["ID"].max() # debes contener el total de competencias realizadas
#ejercicio_2 = len(df["Event"].unique()) # # debes contener el total de competencias realizadas
ejercicio_2 = len(df["Games"].unique())

############# OTRA FORMA  #########
#ejercicio_2 = df["Games"].nunique()
###################################

###################################
# 3. Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los juegos
# olímpicos de Verano como en los de Invierno. El resultado debe guardarse en una variable
# llamada ejercicio_3 .
#ejercicio_3 = [df["Season"].value_counts()["Summer"] / df["Season"].value_counts().sum() , df["Season"].value_counts()["Winter"] / df["Season"].value_counts().sum()] #  debe ser de tipo panda series para poder evaluarla
ejercicio_3 = df["Season"].value_counts('%')
###################################

###################################
# 4. Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El resultado debe
# guardarse en una variable llamada ejercicio_4 .
# tip: Investige sobre las funciones min() y unique() de una Serie de pandas.

#NO ejercicio_4 = df[df["Season"] == "Summer"]["Year"].unique()
#NO ejercicio_4 = df[df["Season"] == "Summer"].min()["Year"] # debes contener donde fue la primera celebracion de los juegos olimpicos de verano
#NO subset1 = df.loc[:,["Year","Season","City"]]
#NO ejercicio_4 = df_subset_1[df_subset_1["Year"] == df_subset_1["Year"].min()].head(1)["Team"]
#NO ejercicio_4 = subset1[subset1["Season"] == "Summer"].min()["City"]


############# OTRA FORMA  #########

#summer = df['Season'] == 'Summer'
#summer_athletes = df[summer]
#first_year_summer = summer_athletes['Year'].min()
#ejercicio_4 = summer_athletes[summer_athletes['Year'] == first_year_summer]['City'].unique()

verano = df[df["Season"]=='Summer']
ejercicio_4 = verano[verano["Year"] == verano["Year"].min()]["City"].unique()
###################################

###################################
# 5. Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El resultado
# debe guardarse en una variable llamada ejercicio_5 .
#ejercicio_5 = df[df["Season"] == "Winter"]["Year"].unique().min() # debes contener donde fue la primera celebracion de los juegos olimpicos de invierno

#df_subset_2 = df.loc[:,["Year","Season","Team"]]
#ejercicio_5 = df_subset_2[df_subset_2["Season"] == "Winter"].min()["Team"]
#subset2 = df.loc[:,["Year","Season","City"]]
#ejercicio_5 = subset2[subset2["Season"] == "Winter"].min()["City"]
invierno = df[df["Season"] == "Winter"]
ejercicio_5 = invierno[invierno["Year"] == invierno["Year"].min()]["City"].unique()
###################################

###################################
# 6. Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo de los
# juegos. El resultado debe guardarse en una variable llamada ejercicio_6 .
ejercicio_6 = df["Team"].value_counts().head(10)
###################################

###################################
# 7. Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe
# guardarse en una variable llamada ejercicio_7 .
#ejercicio_7 = [df["Medal"].value_counts()["Gold"]/df["Medal"].value_counts().sum(), df["Medal"].value_counts()["Bronze"]/df["Medal"].value_counts().sum(), df["Medal"].value_counts()["Silver"]/df["Medal"].value_counts().sum()] # debe ser de tipo panda series para poder evaluarla
ejercicio_7 = df["Medal"].value_counts('%')
###################################

###################################
# 8. Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. El
# resultado debe guardarse en una variable llamada ejercicio_8
#ejercicio_8 = df[df["Season"]== "Summer"]["Team"].head(4) # debes contener cuales fueron los paises participantes en las primeras olimpiadas de verano
#ejercicio_8 = df[df["Season"]== "Summer"]["Team"].head()
#ejercicio_8 = df["NOC"].head()
primeros = df[df["Season"] == "Summer"]
ejercicio_8 = primeros[primeros["Year"] == primeros["Year"].min()]["NOC"].unique()

