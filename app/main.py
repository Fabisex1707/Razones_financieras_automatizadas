import pandas as pd
import pickle
from funciones.funciones_razones_financieras import input_catalogo_cuentas, cargar_datos_catalogo, guardar_datos,mostrar_catalogo_cuentas, calcular_estado_resultados, mostrar_estado_resultados

def main():
    print(f"{'-'*20} Bienvenido al programa de Razones Financieras {'-'*20}")
    print(f"***Esete programa le permitirá calcular diversas razones financieras utilizando los datos de su catálogo de cuentas.***\n")
    estado_catalogo= cargar_datos_catalogo("catalogo_cuentas.pkl")
    if estado_catalogo is None:
        print(f"No se encontraron datos precargados. Por favor, ingrese los datos del catálogo de cuentas.\n")
    else:
        print("Datos del catalogo de cuentas encontrados y cargados exitosamente.")
    while True:
        print("Menu de opciones:")
        print("1. Ingresar o actualizar datos del catálogo de cuentas")
        print("2. Mostrar catálogo de cuentas")
        print("3. Calcular estado de resultados")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            catalogo_cuentas = input_catalogo_cuentas()
            if catalogo_cuentas is None:
                pass
            else:
                guardar_datos(catalogo_cuentas, "catalogo_cuentas.pkl")
        elif opcion == 2:
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                mostrar_catalogo_cuentas(catalogo_cuentas)
            else:
                print("Error: No hay datos del catálogo de cuentas cargados.\n")
        elif opcion == 3:
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                estado_resultados = calcular_estado_resultados(catalogo_cuentas)
                if isinstance(estado_resultados, dict):
                    mostrar_estado_resultados(estado_resultados)
                else:
                    print(estado_resultados)  # Muestra el mensaje de error si no se pudo calcular el estado de resultados
            else:
                print("Error: No hay datos del catálogo de cuentas cargados.\n")  # Muestra el mensaje de error si no se pudo cargar el catálogo
        elif opcion == 4:
            print("Gracias por usar el programa de Razones Financieras. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.\n")






if __name__ == "__main__":
    main()