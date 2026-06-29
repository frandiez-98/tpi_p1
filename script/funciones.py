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

# Muestra el menú principal
def mostrar_menu():
    mostrar_titulo("GESTIÓN DE PAÍSES")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Modificar país")
    print("4. Eliminar país")
    print("5. Buscar país")
    print("6. Filtrar países")
    print("7. Ordenar países")
    print("8. Estadísticas")
    print("9. Salir")

# Solicita una opción válida del menú
def pedir_opcion():
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: ").strip())
            if 1 <= opcion <= 9:
                return opcion
            else:
                print("Error: Debe ingresar una opción entre 1 y 9.")
        except ValueError:
            print("Error: debe ingresar un número")

# Busca un país por su nombre y devuelve su posición en la lista
def buscar_indice_pais(paises, nombre):
    for i, pais in enumerate(paises):
        if pais["nombre"].lower() == nombre.lower():
            return i
    return -1

# 1: muestra una tabla con la informacíon de los países
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
    print()

# 2: agrega un país nuevo a lista
def agregar_pais(paises):
    mostrar_titulo("AGREGAR PAÍS")
    # Nombre
    while True:
        nombre = input("Nombre: ").strip().title()
        # Controla nombres vacíos
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue
        # Controla nombres repetidos
        existe = False
        for pais in paises:
            if pais["nombre"] == nombre:
                existe = True
                break
        if existe:
            print("Error: el país ya se encuentra en la lista.")
            continue
        break
    # Población
    while True:
        try:
            poblacion = int(input("Población: ").strip())
            # Controla la carga de números <= 0
            if poblacion <= 0:
                print("Error: la población debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")
    # Superficie
    while True:
        try:
            superficie = int(input("Superficie: ").strip())
            # Controla la carga de números <= 0
            if superficie <= 0:
                print("Error: la superficie debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")
    # Continente
    while True:
        print("\nContinente:")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")
        try:
            opcion = opcion = int(input("\nSeleccione un continente: ").strip())
            if opcion == 1:
                continente = "América"
                break
            elif opcion == 2:
                continente = "Europa"
                break
            elif opcion == 3:
                continente = "Asia"
                break
            elif opcion == 4:
                continente = "África"
                break
            elif opcion == 5:
                continente = "Oceanía"
                break
            else:
                print("ERROR: Debe seleccionar una opción entre 1 y 5.")
        except ValueError:
            print("Error: debe ingresar un número.")
    # Crea un diccionario con los datos del nuevo país
    nuevo_pais = {"nombre": nombre,
        "población": poblacion,
        "superficie": superficie,
        "continente": continente}
    # Agrega el nuevo país a la lista
    paises.append(nuevo_pais)
    print(f"\n¡El país {nombre} se ha cargado correctamente!")
    print()
    
# 5: busca un país por su nombre y muestra su información
def buscar_pais(paises):
    mostrar_titulo("BUSCAR PAÍS")
    nombre = input("Ingrese el nombre del país: ").strip().title()
    indice = buscar_indice_pais(paises, nombre)
    # Controla país no existente en la lista
    if indice == -1:
        print("\nERROR: El país no existe.")
        return
    mostrar_paises([paises[indice]])

# 9: guarda la lista de países en el archivo
def guardar_csv(paises):
    with open(RUTA_CSV, "w", encoding = "utf-8", newline = "") as archivo: # Se usa w porque lo utilizo al salir del programa
        # Escribe el encabezado
        campos = ["nombre", "población", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames = campos)
        escritor.writeheader()
        # Escribe los diccionarios
        escritor.writerows(paises)