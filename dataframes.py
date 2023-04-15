"""
módulo encargado de definir las tablas de los grupos de
alimentos en la base de datos
"""
from enum import Enum


import pandas as pd
from sqlite3 import Connection



class GruposAlimentos(Enum):
    """Define los diferentes grupos de alimentos disponibles asi mismo representan 
    los nombres de las hojas de excel de cada grupo de alimento
    """
    FRUTAS = "frutas"
    VERDURAS = "verduras"
    LEGUMINOSAS = "leguminosas"
    CEREALES_SIN_GRASA = "cereales sin grasa"
    CEREALES_CON_GRASA = "cereales con grasa"
    ALIMENTOS_ORIGEN_ANIMAL_MUY_BAJOS_EN_GRASA = "a.o.a muy bajos en grasa"
    ALIMENTOS_ORIGEN_ANIMAL_BAJO_EN_GRASA = "a.o.a.bajo en grasa"
    ALIMENTOS_ORIGEN_ANIMAL_MODERADOS_EN_GRASA = "a.o.a.moderados en grasa"
    ALIMENTOS_ORIGEN_ANIMAL_ALTO_EN_GRASA = "a.o.a.alto en grasa"
    LECHE_DESCREMADA = "leche descremada"
    LECHE_SEMIDESCREMADA = "leche semidescremada"
    LECHE_ENTERA = "leche entera"
    LECHE_CON_AZUCAR = "leche con azucar"
    ACEITES_Y_GRASAS = "aceites y grasas"
    ACEITES_Y_GRASAS_CON_PROTEINAS = "aceites y grasas con proteinas"
    AZUCARES_SIN_GRASA = "azucares sin grasa"
    AZUCARES_CON_GRASA = "azucares con grasa"
    ALIMENTOS_LIBRES_EN_ENERGIA = "alimentos libres en energia"



def obtener_archivo_excel(ruta_archivo: str) -> pd.ExcelFile:
    """Devuelve el archivo de excel a utilizar
    """
    try:
        return pd.ExcelFile(ruta_archivo)
    except FileNotFoundError:
        raise ValueError("La ruta del archivo no es correcta")    

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

print(len(obtener_nombres_tabla()))


def dataframes_a_sql(dataframes: list[pd.DataFrame], nombres_tabla: list[str], conn: Connection) -> None:
    """Genera la consulta sql mediante pandas para convertir los dataframes en tablas de base de datos"""
    for indice, dataframe in enumerate(dataframes):
        dataframe: pd.DataFrame = dataframe.replace("ND", 0.0, inplace=False)
        dataframe.to_sql(name=nombres_tabla[indice], con=conn, if_exists="replace", index=False, chunksize=100)

    conn.close()



