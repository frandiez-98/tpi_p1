from funciones import cargar_csv, mostrar_menu

# Función principal
def main():
    # Carga los países desde el archivo
    paises = cargar_csv()
    # Muestra el menú
    mostrar_menu()

# Ejecuta el programa
main()


