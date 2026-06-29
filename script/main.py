from funciones import cargar_csv, mostrar_menu, pedir_opcion, mostrar_paises, agregar_pais, guardar_csv, buscar_pais, modificar_pais, eliminar_pais, mostrar_estadisticas, ordenar_paises, filtrar_paises

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
        elif opcion == 2:
            agregar_pais(paises)
        elif opcion == 3:
            modificar_pais(paises)
        elif opcion == 4:
            eliminar_pais(paises)
        elif opcion == 5:
            buscar_pais(paises)
        elif opcion == 6:
            filtrar_paises(paises)
        elif opcion == 7:
            ordenar_paises(paises)
        elif opcion == 8:
            mostrar_estadisticas(paises)
        elif opcion == 9:
            guardar_csv(paises)
            print("\n¡Gracias por utilizar el sistema! Hasta luego.")
            break

# Ejecuta el programa
main()
