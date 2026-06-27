from funciones import cargar_csv

paises = cargar_csv()
print(f"Cantidad de países: {len(paises)}")
for pais in paises:
    print(pais)