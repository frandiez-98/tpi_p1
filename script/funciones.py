# Importar módulos necesarios
import csv
from pathlib import Path # Permite trabajar con rutas de archivos

# Ruta del archivo csv
RUTA_CSV = Path(__file__).resolve().parent.parent / "data" /"paises.csv"

# Lee el archivo y devuelve una lista de diccionarios
def cargar_csv():
    paises = []
    try:
        with open(RUTA_CSV, "r", encoding = "utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {"nombre": fila["nombre"],
                        "población": int(fila["población"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]}
                paises.append(pais)
    except FileNotFoundError:
        print("Error: no se encontró el archivo de países")
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
            opcion = int(input("\nSeleccione un continente: ").strip())
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
                print("Error: debe seleccionar una opción entre 1 y 5.")
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

# 3: modifica los datos de un país
def modificar_pais(paises):
    mostrar_titulo("MODIFICAR PAÍS")
    nombre = input("Ingrese el país a modificar: ").strip().title()
    indice = buscar_indice_pais(paises, nombre)
    # Controla país no existente en la lista
    if indice == -1:
        print("\nError: el país no existe.")
        return
    print("\nIngrese los nuevos datos.\n")
    # Cambiar población
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
    # Cambiar superficie
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
    # Cambiar continente
    while True:
        print("\nContinente:")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")
        try:
            opcion = int(input("\nSeleccione un continente: ").strip())
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
                print("Error: debe seleccionar una opción entre 1 y 5.")
        except ValueError:
            print("Error: debe ingresar un número.")
    # Carga de cambio
    paises[indice]["población"] = poblacion
    paises[indice]["superficie"] = superficie
    paises[indice]["continente"] = continente
    print(f"\n¡El país {nombre} se modificado correctamente!")

# 4: elimina un país
def eliminar_pais(paises):
    mostrar_titulo("ELIMINAR PAÍS")
    nombre = input("Ingrese el país a eliminar: ").strip().title()
    indice = buscar_indice_pais(paises, nombre)
    # Controla país no existente en la lista
    if indice == -1:
        print("\nError: el país no existe.")
        return
    del paises[indice]
    print(f"\n¡El país {nombre} se ha eliminado correctamente!")

# 5: busca un país por su nombre y muestra su información
def buscar_pais(paises):
    mostrar_titulo("BUSCAR PAÍS")
    nombre = input("Ingrese el nombre del país: ").strip().title()
    print()
    resultados = []
    # Busca coincidenacias completas o parciales
    for pais in paises:
        if nombre.lower() in pais["nombre"].lower():
            resultados.append(pais)
    # Controla país no existente en la lista
    if not resultados:
        print("\nError: no se encontraron coincidencias.")
        return
    mostrar_paises(resultados)

# 6: filtra países según el criterio seleccionado
def filtrar_paises(paises):
    mostrar_titulo("FILTRAR PAÍSES")
    # Menú interno
    print("1. Filtrar por continente")
    print("2. Filtrar por rango de población")
    print("3. Filtrar por rango de superficie")
    print("4. Volver")
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: ").strip())
            if opcion not in [1, 2, 3, 4]:
                print("Error: debe ingresar una opción válida.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número.")
    # Filtro por continente
    if opcion == 1:
        print("\nContinentes disponibles:")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")
        while True:
            try:
                opcion_continente = int(input("\nSeleccione un continente: ").strip())
                if opcion_continente == 1:
                    continente = "América"
                elif opcion_continente == 2:
                    continente = "Europa"
                elif opcion_continente == 3:
                    continente = "Asia"
                elif opcion_continente == 4:
                    continente = "África"
                elif opcion_continente == 5:
                    continente = "Oceanía"
                else:
                    print("Error: debe ingresar una opción entre 1 y 5.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número entero.")
        filtrados = []
        for pais in paises:
            if pais["continente"] == continente:
                filtrados.append(pais)
    # Filtro por población
    elif opcion == 2:
        while True:
            try:
                minimo = int(input("\nIngrese la población mínima: ").strip())
                maximo = int(input("Ingrese la población máxima: ").strip())
                # Controla coherencia en los rangos
                if minimo > maximo:
                    print("Error: la población mínima no puede ser mayor que la máxima.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número entero.")
        filtrados = []
        for pais in paises:
            if minimo <= pais["población"] <= maximo:
                filtrados.append(pais)
    # Filtro por superficie
    elif opcion == 3:
        while True:
            try:
                minimo = int(input("\nIngrese la superficie mínima: ").strip())
                maximo = int(input("Ingrese la superficie máxima: ").strip())
                # Controla coherencia en los rangos
                if minimo > maximo:
                    print("Error: la superficie mínima no puede ser mayor que la máxima.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número entero.")
        filtrados = []
        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                filtrados.append(pais)            
    if opcion == 4:
        return
    if not filtrados:
        print("\nError: no se encontraron países que cumplan el criterio.")
        return
    mostrar_paises(filtrados)

# 7: ordena los países según el criterio seleccionado
def ordenar_paises(paises):
    mostrar_titulo("ORDENAR PAÍSES")
    # Menú interno
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: ").strip())
            if opcion < 1 or opcion > 3:
                print("Error: debe ingresar una opción entre 1 y 3.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número.")
    # Ordenar por nombre
    if opcion == 1:
        ordenados = sorted(paises, key=lambda pais: pais["nombre"])
    # Ordenar por población
    elif opcion == 2:
        ordenados = sorted(paises, key=lambda pais: pais["población"])
    # Ordenar por superficie
    else:
        while True:
            # Menú interno
            print("\n1. Ascendente")
            print("2. Descendente")
            try:
                orden = int(input("\nSeleccione el orden: ").strip())
                if orden == 1:
                    ordenados = sorted(paises, key=lambda pais: pais["superficie"])
                    break
                elif orden == 2:
                    ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=True)
                    break
                else:
                    print("Error: debe ingresar 1 o 2.")
            except ValueError:
                print("Error: debe ingresar un número.")
    mostrar_paises(ordenados)

# 8: muestra estadísticas generales de los países
def mostrar_estadisticas(paises):
    mostrar_titulo("ESTADÍSTICAS")
    # Mayor poblacíon
    mayor = max(paises, key=lambda pais: pais["población"])
    print(f"País con mayor población: {mayor['nombre']}")
    print(f"Población: {mayor['población']:,}".replace(",", "."))
    print()
    # Menor población
    menor = min(paises, key=lambda pais: pais["población"])
    print(f"País con menor población: {menor['nombre']}")
    print(f"Población: {menor['población']:,}".replace(",", "."))
    print()
    # Calcula el promedio de población
    total_poblacion = sum(pais["población"] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)
    print(f"Promedio de población: {promedio_poblacion:,.0f}".replace(",", "."))
    print()
    # Calcula el promedio de superficie
    total_superficie = sum(pais["superficie"] for pais in paises)
    promedio_superficie = total_superficie / len(paises)
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²".replace(",", "."))
    print()
    # Cuenta la cantidad de países por continente
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    print("Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")

# 9: guarda la lista de países en el archivo
def guardar_csv(paises):
    with open(RUTA_CSV, "w", encoding = "utf-8", newline = "") as archivo: # Se usa w porque lo utilizo al salir del programa
        # Escribe el encabezado
        campos = ["nombre", "población", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames = campos)
        escritor.writeheader()
        # Escribe los diccionarios
        escritor.writerows(paises)