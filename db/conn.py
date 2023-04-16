"""
Módulo encargado de establecer la conexion a la base de datos
"""
import sqlite3


def conn() -> sqlite3.Connection:
    """Establece la conexion a la base de datos
    """
    try:
        return  sqlite3.connect(database="database.db")
    except sqlite3.Error as err:
        raise err
    