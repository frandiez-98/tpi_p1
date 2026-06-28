from funciones import cargar_csv, mostrar_menu, pedir_opcion, mostrar_paises

# Función principal
def main():
    # Carga los países desde el archivo
    paises = cargar_csv()

    # Muestra el menú
    while True:
        mostrar_menu()
        # Seleccionar opción
        opcion = pedir_opcion()
        if opcion == 1:
            mostrar_paises(paises)
        elif opcion == 9:
            print("\n¡Gracias por utilizar el sistema! Hasta luego")
            break

# Ejecuta el programa
main()
