"""
módulo encargado de definir las tablas de los grupos de
alimentos en la base de datos
"""


import pandas as pd
from sqlite3 import Connection


from grupos_alimentos import GruposAlimentos




def obtener_archivo_excel(ruta_archivo: str) -> pd.ExcelFile:
    """Devuelve el archivo de excel a utilizar
    """
    try:
        return pd.ExcelFile(ruta_archivo)
    except FileNotFoundError as err:
        raise err    

def obtener_nombres_hojas_excel() -> list[str]:
    """Retorna los nombres de las hojas que se usaran para crear los dataframe 
    del archivo excel mediante la clase NombreTabla, el nombre de la 
    tabla y la hoja son los mismos"""
    return [hoja.value.upper() for hoja in GruposAlimentos]


def obtener_dataframes(archivo_excel: pd.ExcelFile, hojas_a_usar: list[str]) -> list[pd.DataFrame]:
    """Se generan los dataframes o tablas de datos a partir del archivo y las hojas de excel
    """
    dataframes: list[pd.DataFrame] = [pd.read_excel(archivo_excel, sheet_name=hoja, header=2).dropna() for hoja in hojas_a_usar] 
    return dataframes



def obtener_nombres_tabla() -> list[str]:
    """Obtiene los nombres que se le pondran a las tablas en la base de datos"""
    return [grupo.value for grupo in GruposAlimentos]



def dataframes_a_sql(dataframes: list[pd.DataFrame], nombres_tabla: list[str], conn: Connection) -> None:
    """Genera la consulta sql mediante pandas para convertir los dataframes en tablas de base de datos"""
    for indice, dataframe in enumerate(dataframes):
        dataframe_sin_nd: pd.DataFrame = dataframe.replace("ND", 0.0, inplace=False)
        dataframe_sin_nd.to_sql(name=nombres_tabla[indice], con=conn, if_exists="replace", index=False, chunksize=100)

    conn.close()



