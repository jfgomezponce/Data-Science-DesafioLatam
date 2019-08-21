import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def desafio_2(dataframe):
    continuas = dataframe.select_dtypes(include=['float64'])
    discreta = dataframe.select_dtypes(include=['object'])
    
#    print(continuas.columns)
    for colname, registro in continuas.iteritems():
        print("\t"+colname)
        print("-"*50)
        print(continuas[colname].describe())
        print("#"*50+"\n")
        
    for colname, registro in discreta.iteritems():
        print("\t"+colname)
        print("-"*50)
        print(discreta[colname].value_counts())
        print("#"*50+"\n")

##############
#    Reporte las estadísticas descriptivas para gle_cgdpc , undp_hdi , imf_pop .
##############
    print("#"*60)
    print("Reporte las estadísticas descriptivas para gle_cgdpc , undp_hdi , imf_pop .")
    print("#"*60+"\n")
    print(dataframe['gle_cgdpc'].describe())
    print("#"*60+"\n")
    print(dataframe['undp_hdi'].describe())
    print("#"*60+"\n")
    print(dataframe['imf_pop'].describe())
    return(continuas)


def obs_perdidas(dataframe,var,print_list=False):
#    La función debe retornar la cantidad de casos perdidos y el porcentaje correspondiente.
##################
#    perdidas = dataframe[var].isna()
#    print(type(perdidas)) # <class 'pandas.core.series.Series'>  (False y Null)  
#    perdidas_true = [name for name, registro in perdidas.iteritems() if registro == True]
#    print(f"Cantidad de perdidas en la columna [{var}]: {len(perdidas_true)} \nporcentaje: {len(perdidas_true)/len(dataframe[var])*100} %")
################## Refactorizar...

    perdidas = dataframe[var].isna()  # array con las filas que contienen NaN
    cantidad = perdidas.sum()
    porcentaje = round(cantidad/len(dataframe[var])*100,2)
#    print(f"cantidad: {cantidad}, porcentaje: {porcentaje}")
    
    if print_list == True:
        print(dataframe[dataframe[var].isna() == True])
    
    return(cantidad,porcentaje)


def grafica_hist(dataframe,var,sample_mean=False,true_mean=False):
    '''
    sample_mean : Booleano. Si es verdadero, debe generar una recta vertical indicando la
        media de la variable en la selección muestral. Por defecto debe ser False .
        
    true_mean : Booleano. Si es verdadero, debe generar una recta vertical indicando la
        media de variable en la base de datos completa.
    
    ======
    Implemente las funciones para las 4 variables seleccionadas según su grupo.
    
        ffp_hf : Human Flight and Brain Drain
        wef_qes : Quality of the educational system
        wdi_expedu : Government expenditure on education, total (% of GDP)
        wdi_ners : School enrollment, secondary (% net)
    '''
    
    col_dropna = dataframe[var].dropna()
    plt.hist(col_dropna, color='lightblue', alpha=.4)
    if sample_mean == True:
        plt.axvline(dataframe[var].mean(), color = 'tomato', linestyle = '--')
    if true_mean == True:
        plt.axvline(df[var].mean(), color = 'green', linestyle = '--')
    #plt.title(f"Histograma para" + r"$\bf{"+{var}+"}$")
    plt.title("histograma de: " + r"$\bf{%s}$" % var)
    plt.show()


def get_z_score(dataframe, cols):
    """
    Esta funcion retorna un sub dataframe de "dataframe" el cual contiene los z-scores de [cols]
    """
    #df_z_scores = pd.DataFrame()
    #for i in cols:
    droped_na = dataframe[cols].dropna()
    mean_drop = droped_na.mean()
    std_drop = droped_na.std()
    z_score = (droped_na - mean_drop) / std_drop
    return z_score

def graficar_dotplot(dataframe, plot_var, plot_by, global_stat=False, statistic='mean'):
    '''
    dataframe : La tabla de datos donde buscar las variables.
    plot_var : La variable a analizar y extraer las medias.
    plot_by : La variable agrupadora.
    global_stat : Booleano. Si es True debe graficar la media global de la variable. Por
        defecto debe ser False .
    statistic: Debe presentar dos opciones. mean para la media y median para la mediana.
        Por defecto debe ser mean .
    '''
    #dataframe.dropna()
    dataframe_agrupado = dataframe.groupby(plot_by)[plot_var]
    var_mean = dataframe[plot_var].mean()

    
    if statistic == 'mean':
        mean_agrupado = round(dataframe_agrupado.mean(),2)
        #print(type(mean_agrupado.index))
        #print(len(mean_agrupado.values))
        
        # SI NO LOS PASO A LISTA, ME DA ERROR "TUPLE OUT OF RANGE"
        x = [i for i in mean_agrupado.values]
        y = [i for i in mean_agrupado.index]
        
        #plt.plot(mean_agrupado.values,mean_agrupado.index,'o') # IndexError: tuple index out of range
        plt.plot(x,y,'o')
        
        
    elif statistic == 'median':
        median_agrupado = round(dataframe_agrupado.median(),2)
        x2 = [i for i in median_agrupado.values]
        y2 = [i for i in median_agrupado.index]
        plt.plot(x2,y2,'go')
        #plt.plot(median_agrupado.values,median_agrupado.index,'o') # IndexError: tuple index out of range

    if statistic == 'zscore':
        z_score_serie = get_z_score(dataframe,plot_var)
        z_score_serie_mean = z_score_serie.mean()
        nombre_var = "%s_zscore" % plot_var
        dataframe[nombre_var] = z_score_serie
        zscore_grouped = dataframe.groupby(plot_by)[nombre_var]
        zscore_grouped_mean = zscore_grouped.mean()
        plt.plot(list(zscore_grouped_mean.values),list(zscore_grouped_mean.index),'o')
        plt.axvline(z_score_serie_mean, color='r', linestyle='--', label=f"Z-score mean({z_score_serie_mean} % )")
        #plt.show()



#        x = list(z_score.values)
 #       y = list(z_score.index)
  #      plt.plot(x,y,'o')

    if global_stat:
        plt.axvline(var_mean, color = 'r',label=f"Mean ({round(var_mean,2)})", linestyle = '--')
        plt.legend(loc='lower left')

    #plt.title(f"Dotplot de: {plot_var} - {statistic}", size='x-large')
    plt.show()