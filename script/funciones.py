# Importar módulos necesarios
import csv
from pathlib import Path # Permite trabajar con rutas de archivos

# Ruta del archivo csv
RUTA_CSV = Path(__file__).resolve().parent.parent / "data" /"paises.csv"

# Lee el archivo y devuelve una lista de diccionarios
def cargar_csv():
    paises = []
    with open(RUTA_CSV, "r", encoding = "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            pais = {"nombre": fila["nombre"],
                    "población": int(fila["población"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]}
            paises.append(pais)
    return paises