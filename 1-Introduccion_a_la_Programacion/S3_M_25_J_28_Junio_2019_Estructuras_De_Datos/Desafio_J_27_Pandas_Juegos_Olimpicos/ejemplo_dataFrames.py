import pandas as pd 
df = pd.read_csv("nations.csv")

#####################################
#
#	print(df)	# Devuelve el dataFrame completo
#
#      Unnamed: 0              country   region  ...   literacy        co2       gini
# 0             1              Algeria   Africa  ...  72.599998  15.000000        NaN
# 1             2                Benin   Africa  ...  41.700001   1.200000        NaN
# ...
# 192         193               Tuvalu  Oceania  ...        NaN        NaN        NaN
# 193         194              Vanuatu  Oceania  ...  82.000000   1.500000        NaN

# [194 rows x 14 columns]

#####################################
#
# 	print(df.head())	# imprimer los primeros 5 registros( tambien sirve: df.head(2)  )
#
#    Unnamed: 0       country  region  ...   literacy   co2       gini
# 0           1       Algeria  Africa  ...  72.599998  15.0        NaN
# 1           2         Benin  Africa  ...  41.700001   1.2        NaN
# 2           3      Botswana  Africa  ...  84.099998   9.2        NaN
# 3           4  Burkina Faso  Africa  ...  23.600000   0.2        NaN
# 4           5       Burundi  Africa  ...  66.599998   0.1  33.299999

# [5 rows x 14 columns]


#####################################
#
#	print(df.max())		# muestra los valores maximos de cada columna
#
# Unnamed: 0           194
# country         Zimbabwe
# region           Oceania
# gdp                74906
# school              12.7
# adfert             207.1
# chldmort             209
# life             82.7667
# pop           1324696064
# urban                100
# femlab            1.0344
# literacy             100
# co2               210.65
# gini                58.5
# dtype: object


#####################################
#
# print(df["region"].value_counts())	imprime cuantos valores tiene la columna en total, es como uniq -c
#
# Africa      52
# Asia        49
# Europe      43
# Americas    35
# Oceania     15
# Name: region, dtype: int64


# print(type(df["region"].value_counts()))	# <class 'pandas.core.series.Series'>
# print(type(df["region"].value_counts().mean()))	# <class 'numpy.float64'>
# print(df["region"].value_counts().mean())	# 38.8


###########################
#
# print(df[df["region"] == "Americas"])
#     Unnamed: 0                country  ...        co2       gini
# 52          53    Antigua and Barbuda  ...  18.299999        NaN
# 53          54              Argentina  ...  15.650000  45.799999
# 54          55                Bahamas  ...  23.950001        NaN
# 55          56               Barbados  ...  16.650000        NaN

# df_americas_gini_nan = df[df["region"] == "Americas"]["gini"].isnull()==True
# print(df_americas_gini_nan.head())


#############################
#
#df_nan = df[df["gdp"].isnull() == True]["region"]
#print(df_nan)
#
# 42       Africa
# 51       Africa
# 54     Americas 	imprimir despues
# 63     Americas 	imprimir despues
# 114        Asia
# 116        Asia
# 119        Asia
# 137      Europe
# 156      Europe
# 162      Europe
# 170      Europe
# 183     Oceania
# 185     Oceania
# 187     Oceania
# 192     Oceania
# Name: region, dtype: object




################################ filtrar la serie anterior por Americas DESPLIEGA WARNING
#
# df_nan = df[df["gdp"].isnull() == True][df["region"]== "Americas"]
# print(df_nan)
#
# ejemplo_iteritems.py:112: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
#   df_nan = df[df["gdp"].isnull() == True][df["region"]== "Americas"]
#     Unnamed: 0  country    region  gdp  ...  femlab   literacy        co2  gini
# 54          55  Bahamas  Americas  NaN  ...  0.8656        NaN  23.950001   NaN
# 63          64     Cuba  Americas  NaN  ...  0.6018  99.800003   8.850000   NaN

# [2 rows x 14 columns]


################################  EJEMPLO CON MULTIPLE FILTRADO DESPLIEGA WARNING
#
# df_nan = df[df["gdp"].isnull() == True][df["region"]== "Americas"][df["literacy"].isnull() == False]
# print(df_nan)

# ejemplo_iteritems.py:114: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
#   df_nan = df[df["gdp"].isnull() == True][df["region"]== "Americas"][df["literacy"].isnull() == False]
#     Unnamed: 0 country    region  gdp  ...  femlab   literacy   co2  gini
# 63          64    Cuba  Americas  NaN  ...  0.6018  99.800003  8.85   NaN

# [1 rows x 14 columns]


############################## SI IMPRIME TYPE DE LO ANTERIOR, TAMBIEN DESPLIEGA WARNING
#
#print(type(df[df["gdp"].isnull() == True][df["region"]== "Americas"][df["literacy"].isnull() == False]))
#
# ejemplo_iteritems.py:132: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
#   print(type(df[df["gdp"].isnull() == True][df["region"]== "Americas"][df["literacy"].isnull() == False]))
# <class 'pandas.core.frame.DataFrame'>