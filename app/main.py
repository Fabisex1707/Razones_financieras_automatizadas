import pandas as pd
import pickle
from funciones.funciones_razones_financieras import input_catalogo_cuentas, cargar_datos_catalogo, guardar_datos,mostrar_catalogo_cuentas, calcular_estado_resultados, mostrar_estado_resultados, calcular_balance_general, mostrar_balance_general, calcular_capital_trabajo, calcular_razon_actividad, mostrar_razon_actividad

def main():
    print(f"{'-'*20} Bienvenido al programa de Razones Financieras {'-'*20}")
    print(f"***Esete programa le permitirá calcular diversas razones financieras utilizando los datos de su catálogo de cuentas.***\n")
    estado_catalogo= cargar_datos_catalogo("catalogo_cuentas.pkl")
    if isinstance(estado_catalogo, dict):
        print("Datos del catalogo de cuentas encontrados y cargados exitosamente.")
    else:
        print(f"No se encontraron datos precargados. Por favor, ingrese los datos del catálogo de cuentas.\n")

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
            if isinstance(catalogo_cuentas, dict):
                resultado_catalogo = guardar_datos(catalogo_cuentas, "catalogo_cuentas.pkl")
                print(resultado_catalogo)
            else:
                print(catalogo_cuentas)  # Muestra el mensaje de error si no se pudo ingresar el catálogo
        elif opcion == 2:
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                print(mostrar_catalogo_cuentas(catalogo_cuentas))
            else:
                print(catalogo_cuentas)  # Muestra el mensaje de error si no se pudo cargar el catálogo
        elif opcion == 3:
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                estado_resultados = calcular_estado_resultados(catalogo_cuentas)
                if isinstance(estado_resultados, dict):
                    print(mostrar_estado_resultados(estado_resultados))
                else:
                    print(estado_resultados)  # Muestra el mensaje de error si no se pudo calcular el estado de resultados
            else:
                print(catalogo_cuentas)  # Muestra el mensaje de error si no se pudo cargar el catálogo
        elif opcion == 4:
            catalogo_cuentas = cargar_datos_catalogo("catalogo_cuentas.pkl")
            if isinstance(catalogo_cuentas, dict):
                if isinstance(estado_resultados, dict):
                    balance_general = calcular_balance_general(catalogo_cuentas, estado_resultados)
                    if isinstance(balance_general, dict):
                        print(mostrar_balance_general(balance_general))
                    else:
                        print(balance_general)  # Muestra el mensaje de error si no se pudo calcular el balance general
                else:
                    print("Error: No se pudo calcular el balance general, sin antes calcular el estado de resultados.\n")  # Muestra el mensaje de error si no se pudo calcular el estado de resultados
            else:
                print(catalogo_cuentas)  # Muestra el mensaje de error si no se pudo cargar el catálogo
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
                        capital_trabajo = calcular_capital_trabajo(balance_general)
                        if isinstance(capital_trabajo, dict):
                            razon_actividad = calcular_razon_actividad(estado_resultados, balance_general, capital_trabajo)
                            if isinstance(razon_actividad, dict):
                                print(mostrar_razon_actividad(razon_actividad))
                                try:
                                    rotacion_inventarios = razon_actividad.get("ROTACION DE INVENTARIOS")
                                    rotacion_cuentas_cobrar = razon_actividad.get("ROTACION CUENTAS POR COBRAR")
                                    rotacion_cuentas_pagar = razon_actividad.get("ROTACION DE CUENTAS POR PAGAR")
                                    rotacion_activos_fijos = razon_actividad.get("ROTACION DE ACTIVOS FIJOS")
                                    rotacion_activos_totales = razon_actividad.get("ROTACION DE ACTIVOS TOTALES")
                                    rotacion_capital_trabajo = razon_actividad.get("ROTACION DE CAPITAL DE TRABAJO")
                                except Exception as e:
                                    print(f"Error al extraer las razones de actividad: {e}")
                                    continue
                                print(f"\n{'*'*80}")
                                print("\t---Interpretación de resultados---")
                                print(f"{'*'*80}\n")

                                print("\t--Rotacion de inventarios---")
                                periodo_promedio_inventario = 365/rotacion_inventarios
                                if rotacion_inventarios < 2:
                                    print("La rotación de inventarios es baja.")
                                    print(f"El numero de días promedio que tardas en convertir el inventario en efectivo es de {int(periodo_promedio_inventario)} días.")
                                    print(f"Lo que puede indicar problemas de obsolescencia o exceso de inventario, pero eso dependera de la temporada y el sector en el que estes.\n")
                                elif rotacion_inventarios > 5:
                                    print("La rotación de inventarios es alta.")
                                    print(f"El numero de días promedio que tardas en convertir el inventario en efectivo es de {int(periodo_promedio_inventario)} días.")
                                    print(f"Lo que puede indicar una buena administración del inventario o alta demanda, pero eso dependera de la temporada y el sector en el que estes.\n")
                                else:
                                    print("La rotación de inventarios es regular.")
                                    print(f"El numero de días promedio que tardas en convertir el inventario en efectivo es de {int(periodo_promedio_inventario)} días.")
                                    print(f"Lo que puede indicar una administración del inventario regular o alta moderada, pero eso dependera de la temporada y el sector en el que estes.\n")

                                print("\t\t--Rotacion de cuentas por cobrar--")
                                periodo_promedio_cuentas_por_cobrar=365/rotacion_cuentas_cobrar
                                if rotacion_cuentas_cobrar < 2:
                                    print("La rotación de cuentas por cobrar es baja.")
                                    print(f"El numero de días promedio que tardas en cobrar el credito de tus clientes es de: {int(periodo_promedio_cuentas_por_cobrar)} días.")
                                    print(f"Lo que puede indicar un sistema ineficiente para la gestion y cobro de créditos.\n")
                                elif rotacion_cuentas_cobrar > 5:
                                    print("La rotación de cuentas por cobrar es alta.")
                                    print(f"El numero de días promedio que tardas en cobrar el credito de tus clientes es de: {int(periodo_promedio_cuentas_por_cobrar)} días.")
                                    print(f"Lo que puede indicar un sistema eficiente para la gestion y cobro de créditos, pero debes tener cuidado con no ser tan inflexible \ncon los dias ya que puedes ahuyentar a posibles clientes.\n")
                                else:
                                    print("La rotación de cuentas por cobrar es regular.")
                                    print(f"El numero de días promedio que tardas en cobrar el credito de tus clientes es de: {int(periodo_promedio_cuentas_por_cobrar)} días.")
                                    print(f"Lo que puede indicar un sistema eficiente para la gestion y cobro de créditos.\n")

                                print("\t--Rotacion de cuentas por pagar--")
                                periodo_promedio_cuentas_por_pagar=365/rotacion_cuentas_pagar
                                if rotacion_cuentas_pagar < 2:
                                    print("La rotación de cuentas por pagar es baja.")
                                    print(f"El numero de días promedio que tardas en pagar tus pasivos a corto plazo es de: {int(periodo_promedio_cuentas_por_pagar)} días.")
                                    print(f"Lo que puede indicar un problema para cumplir con las responsabilidades de la empresa y problemas para generar liquidez.\n")
                                elif rotacion_cuentas_pagar > 5:
                                    print("La rotación de cuentas por pagar es alta.")
                                    print(f"El numero de días promedio que tardas en pagar tus pasivos a corto plazo es de: {int(periodo_promedio_cuentas_por_pagar)} días.")
                                    print(f"Lo que puede indicar un buen manejo de flujo de efectivo y una alta creedibilidad a sus proveedores para cumplir con sus deudas.\n")
                                else:
                                    print("La rotación de cuentas por cobrar es regular.")
                                    print(f"El numero de días promedio que tardas en cobrar el credito de tus clientes es de: {int(periodo_promedio_cuentas_por_pagar)} días.")
                                    print(f"Lo que puede indicar una estrategia eficiente de financiamiento a corto plazo, permitiendo a la empresa generar más liquidez.\n")
                                
                                print("\t--Rotacion de activos fijos--")
                                if rotacion_activos_fijos < 0.8:
                                    print("La rotación de activos fijos es baja.")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo fijo.")
                                    print("Lo que puede indicar que no se esta aprovechando del todo todos los activos a largo plazo con los que cuenta la empresa.\n")
                                elif rotacion_activos_fijos > 1.5:
                                    print("La rotación de activos fijos es alta")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo fijo.")
                                    print("Lo que puede indicar que se esta aprovechando de manera excelente todos los activos a largo plazo con los que cuenta la empresa.\n")
                                else:
                                    print("La rotación de activos fijos es regular.")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo fijo.")
                                    print("Lo que puede indicar que se esta aprovechando de manera eficiente todos los activos a largo plazo con los que cuenta la empresa pero que podría mejorar.\n")

                                print("\t--Rotacion de activos totales--")
                                if rotacion_activos_totales < 0.8:
                                    print("La rotación de activos totales es baja.")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo.")
                                    print("Lo que puede indicar que no se esta aprovechando del todo todos los activos con los que cuenta la empresa.\n")
                                elif rotacion_activos_totales > 1.5:
                                    print("La rotación de activos totales es alta")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo.")
                                    print("Lo que puede indicar que se esta aprovechando de manera excelente todos los activos con los que cuenta la empresa.\n")
                                else:
                                    print("La rotación de activos totales es regular.")
                                    print(f"La empresa genera ${rotacion_activos_fijos:.2f} pesos por cada $1.00 de activo.")
                                    print("Lo que puede indicar que se esta aprovechando de manera eficiente todos los activos con los que cuenta la empresa pero que podría mejorar.\n")
                                
                                print("\t--Rotacion de capital de trabajo--")
                                print(f"Rotacion de capital de trabajo: {rotacion_capital_trabajo:.2f}")
                                if rotacion_capital_trabajo < 0:
                                    print("La rotación de capital de trabajo es muy baja.")
                                    print("Lo que puede indicar que la empresa está utilizando demasiado capital de trabajo para generar ventas, lo que representa una ineficiencia en el manejo de sus recursos.\n")
                                else:
                                    print("La rotación de capital de trabajo es aceptable.")
                                    print("Lo que puede indicar una eficiente rotación de inventarios y cobro de cuentas.\n")
                            else: 
                                print(razon_actividad)  # Muestra el mensaje de error si no se pudo calcular la razón de actividad
                        else:
                            print(capital_trabajo)
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