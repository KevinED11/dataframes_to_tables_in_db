import pandas as pd


from sqlite3 import Connection


from db.conn import conn
from dataframes import obtener_archivo_excel, obtener_nombres_hojas_excel, obtener_nombres_tabla, obtener_dataframes, dataframes_a_sql


def main():
    connection: Connection = conn

    archivo: pd.ExcelFile = obtener_archivo_excel(
        ruta_archivo="SMAE/SMAE-2014-EN-EXCEL.xlsx")
    
    hojas: list[str] = obtener_nombres_hojas_excel()

    nombres_de_tablas: list[str] = obtener_nombres_tabla()

    dataframes: list[pd.DataFrame] = obtener_dataframes(archivo_excel=archivo, hojas_a_usar=hojas)

    dataframes_a_sql(dataframes=dataframes, nombres_tabla=nombres_de_tablas, conn=connection)



if __name__ == "__main__":
    main()