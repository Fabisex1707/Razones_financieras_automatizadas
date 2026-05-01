import pandas as pd
import pickle
from funciones.funciones_razones_financieras import input_catalogo_cuentas, cargar_datos_catalogo, guardar_datos,mostrar_catalogo_cuentas, calcular_estado_resultados, mostrar_estado_resultados, calcular_balance_general, mostrar_balance_general

def main():
    print(f"{'-'*20} Bienvenido al programa de Razones Financieras {'-'*20}")
    print(f"***Esete programa le permitirá calcular diversas razones financieras utilizando los datos de su catálogo de cuentas.***\n")
    estado_catalogo= cargar_datos_catalogo("catalogo_cuentas.pkl")
    if estado_catalogo is None:
        print(f"No se encontraron datos precargados. Por favor, ingrese los datos del catálogo de cuentas.\n")
    else:
        print("Datos del catalogo de cuentas encontrados y cargados exitosamente.")

    estado_resultados = None  # Variable para almacenar el estado de resultados calculado
    balance_general = None  # Variable para almacenar el balance general calculado
    while True:
        print("Menu de opciones:")
        print("1. Ingresar o actualizar datos del catálogo de cuentas")
        print("2. Mostrar catálogo de cuentas")
        print("3. Calcular estado de resultados")
        print("4. Calcular balance general")
        print("5. Calcular razones financieras")
        print("6. Salir")
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
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                if isinstance(estado_resultados, dict):
                    balance_general = calcular_balance_general(catalogo_cuentas, estado_resultados)
                    if isinstance(balance_general, dict):
                        mostrar_balance_general(balance_general)
                    else:
                        print(balance_general)  # Muestra el mensaje de error si no se pudo calcular el balance general
                else:
                    print("Error: No calculo primero el estado de resultados! \n")  # Muestra el mensaje de error si no se pudo calcular el estado de resultados
            else:
                print("Error: No hay datos del catálogo de cuentas cargados.\n")  # Muestra el mensaje de error si no se pudo cargar el catálogo
        elif opcion == 5:
            if isinstance(estado_resultados, dict) and isinstance(balance_general, dict):
                while True:
                    print("\nMenu de razones financieras:")
                    print("1. Calcular razon de actividad")
                    print("2. Calcular razon de liquidez")
                    print("3. Calcular razon de endeudamiento")
                    print("4. Calcular razon de rentabilidad")
                    print("5. Calcular razon de bursatilidad")
                    print("6. Calcular la razon DuPont")
                    print("7. Salir")
                    try:
                        opcion = int(input("Seleccione una opción: "))
                    except ValueError:
                        print("Error: Por favor, ingrese un número válido.")
                        continue
                    if opcion == 7:
                        print("Gracias por usar el programa de Razones Financieras. ¡Hasta luego!\n")
                        break
                    elif opcion == 1:
                        print("Opción para calcular razón de actividad seleccionada. (Funcionalidad en desarrollo)")
                    elif opcion == 2:
                        print("Opción para calcular razón de liquidez seleccionada. (Funcionalidad en desarrollo)")   
                    elif opcion == 3:
                        print("Opción para calcular razón de endeudamiento seleccionada. (Funcionalidad en desarrollo)")
                    elif opcion == 4:
                        print("Opción para calcular razón de rentabilidad seleccionada. (Funcionalidad en desarrollo)")
                    elif opcion == 5:
                        print("Opción para calcular razón de bursatilidad seleccionada. (Funcionalidad en desarrollo)")
                    elif opcion == 6:
                        print("Opción para calcular la razón DuPont seleccionada. (Funcionalidad en desarrollo)") 
                    else:
                        print("Opción no válida. Por favor, seleccione una opción del menú.")
            else:
                print("Error: Para calcular las razones financieras, primero debe calcular el estado de resultados y el balance general.\n")
        elif opcion == 6:
                    print("Gracias por usar el programa de Razones Financieras. ¡Hasta luego!\n")
                    break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.\n")






if __name__ == "__main__":
    main()