import pandas as pd

df = pd.read_csv("nations.csv")


###########################
#
# print(df.head())
#
#    Unnamed: 0       country  region  ...   literacy   co2       gini
# 0           1       Algeria  Africa  ...  72.599998  15.0        NaN
# 1           2         Benin  Africa  ...  41.700001   1.2        NaN
# 2           3      Botswana  Africa  ...  84.099998   9.2        NaN
# 3           4  Burkina Faso  Africa  ...  23.600000   0.2        NaN
# 4           5       Burundi  Africa  ...  66.599998   0.1  33.299999
#
# [5 rows x 14 columns]


dff = df.drop(columns="Unnamed: 0")
###########################
#
# print(dff.head())
#
#         country  region           gdp  ...   literacy   co2       gini
# 0       Algeria  Africa   7300.399902  ...  72.599998  15.0        NaN
# 1         Benin  Africa   1338.800049  ...  41.700001   1.2        NaN
# 2      Botswana  Africa  12307.400391  ...  84.099998   9.2        NaN
# 3  Burkina Faso  Africa   1063.400024  ...  23.600000   0.2        NaN
# 4       Burundi  Africa    349.200012  ...  66.599998   0.1  33.299999

# [5 rows x 13 columns]


###########################
#for i in df:
#	print(i)
############# Es lo mismo que ##############
#
# for colname,serie in dff.iteritems():
# 	print(colname)

# country
# region
# gdp
# school
# adfert
# chldmort
# life
# pop
# urban
# femlab
# literacy
# co2
# gini

############################
# iteritems() itera por columnas, de izquierda a derecha, entonces serie correspondera a los valores de cada columna
# for colname,serie in dff.iteritems():
#  	print(serie)
#
# 0                  Algeria
# 1                    Benin
# 193                Vanuatu
# Name: country, Length: 194, dtype: object
#
# 0       Africa
# 1       Africa
# 193    Oceania
# Name: region, Length: 194, dtype: object
#
# 193     3809.800049
# Name: gdp, Length: 194, dtype: float64	



############################# IMPRIME EL NOMBRE DE LA COLUMNA Y SUS VALORES
#
# for colname,serie in dff.iteritems():
# 	print(colname)
# 	print(serie)
# 	break

# country
# 0                  Algeria
# 1                    Benin
# 192                 Tuvalu
# 193                Vanuatu
# Name: country, Length: 194, dtype: object


