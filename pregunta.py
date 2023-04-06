"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    df = pd.read_fwf('clusters_report.txt', colspecs=[(3,5),(9,14),(25,29),(40,119)], header = None)
    df.head(10)
    
    df.drop(df.index[:3], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    df_f= pd.DataFrame
    df_f['cluster'] =df[0]
    df_f['cantidad_de_palabras_clave'] = df[1]
    df_f['porcentaje_de_palabras_clave'] =df[2].str.replace(',','.')
    df_f.dropna(inplace=True)
    
    df_f.reset_index(drop=True,inplace=True)
    df_f['cluster'] = df_f['cluster'].str.strip().astype(int)
    df_f['cantidad_de_palabras_clave'] = df_f['cantidad_de_palabras_clave'].str.strip().astype(int)
    df_f['porcentaje_de_palabras_clave'] = df_f['porcentaje_de_palabras_clave'].str.strip().astype(float)
               
    words =[]
    [words.append(i) for i in df[3]]
    key_word = ' '.join(words).replace('control multi', 'control.multi')
    Words_1 = []
    [Words_1.append(i.strip()) for i in key_word[:-1].split('.')]
    
    df_f['principales_palabras_clave'] = pd.concat([pd.Series(i) for i in Words_1]).reset_index(drop=True)
    df_f['principales_palabras_clave'] = df_f['principales_palabras_clave'].str.replace(' ,', ',').replace(',',', ').str.replace('   ',' ').str.replace('  ',' ').str.strip('\n').str.replace('  ', ' ')

    return df_f