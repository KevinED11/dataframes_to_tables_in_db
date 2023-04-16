"""Almacena la clase que define los grupos de alimentos
"""
from enum import Enum


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
