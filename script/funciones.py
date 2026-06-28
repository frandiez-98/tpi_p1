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

# Crea los títulos centrados entre líneas 
def mostrar_titulo(titulo):
    ANCHO = 75
    print("=" * ANCHO)
    print(titulo.center(ANCHO))
    print("=" * ANCHO)

# Muestra una tabla con la informacíon de los países
def mostrar_paises(paises):
    ANCHO = 75
    mostrar_titulo("LISTADO DE PAÍSES")
    # Verifica si la lista está vacía
    if not paises:
        print("No hay países para mostrar.")
        return
    # Imprime la tabla
    print(f"{'NOMBRE':<20}{'POBLACIÓN':>10}{'SUPERFICIE (km²)':>25}{'CONTINENTE':>20}")
    print("-" * ANCHO)
    for pais in paises:
        poblacion = f"{pais['población']:,}".replace(",",".")
        superficie = f"{pais['superficie']:,}".replace(",",".")
        print(f"{pais['nombre']:<20}{poblacion:<20}{superficie:<25}{pais['continente']:<20}")
    print("-" * ANCHO)
    print(f"Total de países: {len(paises)}")