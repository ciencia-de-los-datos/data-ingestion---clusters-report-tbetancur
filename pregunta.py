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

    df = pd.read_csv('clusters_report.txt', widths=[9,16,16,80], header=None)
    
    list_column = df[:2].fillna('').apply(lambda x:' '+x). sum().tolist()
    list_column=[colum.strip().lower().replace(' ','_')for colum in list_column]
    
    df =df[3:]
    df.columns = list_column
    
    df= df.fillna(method= 'ffill')
    df.principales_palabras_claves = df.principales_palabras_claves.apply(
        lambda words: ' ' + words
    )
    
    df= df.groupby([
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave'        
    ], as_index =False)
    [['principales_palabras_claves']].sum()
    
    df.principales_palabras_claves =df.principales_palabras_claves.str.replace(".","",regex=True)
    df.principales_palabras_claves =df.principales_palabras_claves.str.replace ("  "," ")
    df.principales_palabras_claves =df.principales_palabras_claves.str.replace (" "," ")
    df.principales_palabras_claves =df.principales_palabras_claves.str.replace (" "," ")
    df.principales_palabras_claves =df.principales_palabras_claves.str.strip()
    
    
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.str.replace('%', '')
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.str.replace(',', '.')
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.map(float)

    df.cantidad_de_palabras_clave = df.cantidad_de_palabras_clave.map(int)
    df.cluster = df.cluster.map(int)
    df = df.sort_values('cluster')
    df = df.reset_index(drop=True)
    
    return df