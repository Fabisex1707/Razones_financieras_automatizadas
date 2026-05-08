import pandas as pd
import pickle
from funciones.funciones_razones_financieras import input_catalogo_cuentas, cargar_datos_catalogo, guardar_datos,mostrar_catalogo_cuentas, calcular_estado_resultados, mostrar_estado_resultados, calcular_balance_general, mostrar_balance_general, calcular_capital_trabajo, calcular_razon_actividad, mostrar_razon_actividad, calcular_razon_rentabilidad, mostrar_razon_rentabilidad, calcular_bursatilidad, mostrar_bursatilidad, calcular_analisis_DuPont, mostrar_analisis_dupont

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
                                print("\t\t---Interpretación de resultados---")
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

                                print("\t--Rotacion de cuentas por cobrar--")
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
                        razon_rentabilidad = calcular_razon_rentabilidad(estado_resultados, balance_general)
                        if isinstance(razon_rentabilidad, dict):
                            print(mostrar_razon_rentabilidad(razon_rentabilidad))

                            try:
                                margen_utilidad = razon_rentabilidad.get("MARGEN DE UTILIDAD",0)
                                margen_utilidad_bruta = razon_rentabilidad.get("MARGEN DE UTILIDAD BRUTA",0)
                                margen_utilidad_operativa = razon_rentabilidad.get("MARGEN DE UTILIDAD OPERATIVA",0)
                                rendimiento_activos = razon_rentabilidad.get("RENDIMIENTO SOBRE LOS ACTIVOS TOTALES",0)
                                rendimiento_patrimonio = razon_rentabilidad.get("RENDIMIENTO SOBRE EL PATRIMONIO",0)
                                rendimiento_capital = razon_rentabilidad.get("RENDIMIENTO SOBRE EL CAPITAL COMUN",0)
                            except Exception as e:
                                print(f"Error al extraer las razones de rentabilidad: {e}")
                                continue

                            print(f"\n{'*'*80}")
                            print("\t\t---Interpretación de resultados---")
                            print(f"{'*'*80}\n")


                            print("\t--Margen de utilidad--")
                            if margen_utilidad < 5:
                                print("El margen de utilidad es bajo.")
                                print(f"La empresa obtiene {margen_utilidad:.2f}% de utilidad neta por cada venta realizada.")
                                print("Lo que puede indicar altos costos, gastos excesivos o poca eficiencia para generar ganancias.\n")
                            elif margen_utilidad > 15:
                                print("El margen de utilidad es alto.")
                                print(f"La empresa obtiene {margen_utilidad:.2f}% de utilidad neta por cada venta realizada.")
                                print("Lo que puede indicar una excelente administración de costos y buena rentabilidad.\n")
                            else:
                                print("El margen de utilidad es regular.")
                                print(f"La empresa obtiene {margen_utilidad:.2f}% de utilidad neta por cada venta realizada.")
                                print("Lo que puede indicar una rentabilidad estable, aunque todavía puede mejorar.\n")


                            print("\t--Margen de utilidad bruta--")
                            if margen_utilidad_bruta < 20:
                                print("El margen de utilidad bruta es bajo.")
                                print(f"La empresa conserva {margen_utilidad_bruta:.2f}% después de cubrir el costo de ventas.")
                                print("Lo que puede indicar costos de producción elevados o poca eficiencia operativa.\n")
                            elif margen_utilidad_bruta > 50:
                                print("El margen de utilidad bruta es alto.")
                                print(f"La empresa conserva {margen_utilidad_bruta:.2f}% después de cubrir el costo de ventas.")
                                print("Lo que puede indicar un excelente control de costos y alta capacidad para generar ganancias.\n")
                            else:
                                print("El margen de utilidad bruta es regular.")
                                print(f"La empresa conserva {margen_utilidad_bruta:.2f}% después de cubrir el costo de ventas.")
                                print("Lo que puede indicar un manejo aceptable de costos de producción.\n")


                            print("\t--Margen de utilidad operativa--")
                            if margen_utilidad_operativa < 10:
                                print("El margen de utilidad operativa es bajo.")
                                print(f"La empresa genera {margen_utilidad_operativa:.2f}% de utilidad operativa sobre sus ventas.")
                                print("Lo que puede indicar altos gastos administrativos o de operación.\n")
                            elif margen_utilidad_operativa > 25:
                                print("El margen de utilidad operativa es alto.")
                                print(f"La empresa genera {margen_utilidad_operativa:.2f}% de utilidad operativa sobre sus ventas.")
                                print("Lo que puede indicar una operación eficiente y bien administrada.\n")
                            else:
                                print("El margen de utilidad operativa es regular.")
                                print(f"La empresa genera {margen_utilidad_operativa:.2f}% de utilidad operativa sobre sus ventas.")
                                print("Lo que puede indicar una eficiencia operativa aceptable.\n")


                            print("\t--Rendimiento sobre los activos totales--")
                            if rendimiento_activos < 5:
                                print("El rendimiento sobre activos es bajo.")
                                print(f"La empresa genera {rendimiento_activos:.2f}% de utilidad por cada peso invertido en activos.")
                                print("Lo que puede indicar que los activos no están siendo aprovechados eficientemente.\n")
                            elif rendimiento_activos > 15:
                                print("El rendimiento sobre activos es alto.")
                                print(f"La empresa genera {rendimiento_activos:.2f}% de utilidad por cada peso invertido en activos.")
                                print("Lo que puede indicar un excelente aprovechamiento de los recursos de la empresa.\n")
                            else:
                                print("El rendimiento sobre activos es regular.")
                                print(f"La empresa genera {rendimiento_activos:.2f}% de utilidad por cada peso invertido en activos.")
                                print("Lo que puede indicar un uso aceptable de los activos.\n")

                            
                            print("\t--Rendimiento sobre el patrimonio--")
                            if rendimiento_patrimonio < 10:
                                print("El rendimiento sobre el patrimonio es bajo.")
                                print(f"La empresa genera {rendimiento_patrimonio:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar una baja rentabilidad para los propietarios.\n")
                            elif rendimiento_patrimonio > 20:
                                print("El rendimiento sobre el patrimonio es alto.")
                                print(f"La empresa genera {rendimiento_patrimonio:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar una excelente generación de ganancias para los inversionistas.\n")
                            else:
                                print("El rendimiento sobre el patrimonio es regular.")
                                print(f"La empresa genera {rendimiento_patrimonio:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar una rentabilidad estable para los propietarios.\n")

                        
                            print("\t--Rendimiento sobre el capital común--")
                            if rendimiento_capital < 10:
                                print("El rendimiento sobre el capital común es bajo.")
                                print(f"La empresa obtiene {rendimiento_capital:.2f}% sobre el capital invertido.")
                                print("Lo que puede indicar poca eficiencia para generar utilidades con el capital social.\n")
                            elif rendimiento_capital > 20:
                                print("El rendimiento sobre el capital común es alto.")
                                print(f"La empresa obtiene {rendimiento_capital:.2f}% sobre el capital invertido.")
                                print("Lo que puede indicar una excelente capacidad para generar ganancias a partir del capital.\n")
                            else:
                                print("El rendimiento sobre el capital común es regular.")
                                print(f"La empresa obtiene {rendimiento_capital:.2f}% sobre el capital invertido.")
                                print("Lo que puede indicar un rendimiento aceptable para los inversionistas.\n")
                        else:
                            print(razon_rentabilidad)
                    elif opcion == 5:
                        try:
                            bursatilidad = calcular_bursatilidad(estado_resultados, balance_general)
                            if isinstance(bursatilidad, dict):
                                mostrar_bursatilidad(bursatilidad)
                                valor_nominal = bursatilidad.get("R_V_N")
                                valor_libros = bursatilidad.get("R_V_L")
                                razon_ml = bursatilidad.get("R_V_ML")
                                utilidad_accion = bursatilidad.get("Valor por accion")
                                razon_pu = bursatilidad.get("R_P_U")
                                rentabilidad_accion = bursatilidad.get("R_R_A")
                                utilidad_valor_nominal = bursatilidad.get("R_U_V")

                                print("\n" + "="*65)
                                print("Interpretación de resultados de bursatilidad")
                                print("="*65 + "\n")

                                print("\t--Valor nominal--")
                                if valor_nominal < 1:
                                    print(f"Valor nominal: {valor_nominal:.2f} Muy bajo, cada acción representa poco capital social.\n")
                                elif 1 <= valor_nominal < 5:
                                    print(f"Valor nominal: {valor_nominal:.2f} Adecuado, respaldo moderado por acción.\n")
                                else:
                                    print(f"Valor nominal: {valor_nominal:.2f} Alto, cada acción concentra más capital y refleja solidez.\n")

                                print("\t--Valor en libros--")
                                if valor_libros < 1:
                                    print(f"Valor en libros: {valor_libros:.2f} Respaldo contable débil por acción.\n")
                                elif 1 <= valor_libros < 3:
                                    print(f"Valor en libros: {valor_libros:.2f} Respaldo aceptable, cada acción tiene un valor razonable.\n")
                                else:
                                    print(f"Valor en libros: {valor_libros:.2f} Respaldo fuerte, cada acción refleja buen nivel de capital contable.\n")
                                
                                print("\t--Razon ml--")
                                if razon_ml < 1:
                                    print(f"Razón V/L: {razon_ml:.2f} El valor calculado es menor al respaldo contable, indica debilidad.\n")
                                elif 1 <= razon_ml < 2:
                                    print(f"Razón V/L: {razon_ml:.2f} El valor calculado supera al respaldo contable, muestra fortaleza.\n")
                                else:
                                    print(f"Razón V/L: {razon_ml:.2f} El valor calculado es muy superior, refleja posición destacada frente al respaldo.\n")

                                print("\t--Utilidad por accion--")
                                if utilidad_accion <= 0:
                                    print(f"Utilidad por acción: {utilidad_accion:.2f} Pérdida neta por acción, situación crítica.\n")
                                elif 0 < utilidad_accion < 1:
                                    print(f"Utilidad por acción: {utilidad_accion:.2f} Baja utilidad, cada acción aporta poco beneficio.\n")
                                elif 1 <= utilidad_accion < 3:
                                    print(f"Utilidad por acción: {utilidad_accion:.2f} Utilidad aceptable, cada acción genera beneficio razonable.\n")
                                else:
                                    print(f"Utilidad por acción: {utilidad_accion:.2f} Alta utilidad, cada acción aporta beneficio considerable.\n")

                                print("\t--Razon precio U--")
                                if razon_pu < 10:
                                    print(f"Razón P/U: {razon_pu:.2f} Relación baja, utilidades relativamente fuertes frente al valor.\n")
                                elif 10 <= razon_pu <= 20:
                                    print(f"Razón P/U: {razon_pu:.2f} Relación moderada, equilibrio entre valor y utilidad.\n")
                                elif 20 < razon_pu <= 30:
                                    print(f"Razón P/U: {razon_pu:.2f} Relación alta, utilidades pequeñas frente al valor.\n")
                                else:
                                    print(f"Razón P/U: {razon_pu:.2f} Relación muy elevada, utilidades limitadas frente al valor asignado.\n")

                                print("\t--Rentabilidad por accion--")
                                if rentabilidad_accion < 0.1:
                                    print(f"Rentabilidad por acción: {rentabilidad_accion:.2f} Muy baja, poca capacidad de convertir respaldo en utilidad.\n")
                                elif 0.1 <= rentabilidad_accion < 0.5:
                                    print(f"Rentabilidad por acción: {rentabilidad_accion:.2f} Aceptable, aunque con margen de mejora.\n")
                                elif 0.5 <= rentabilidad_accion < 1:
                                    print(f"Rentabilidad por acción: {rentabilidad_accion:.2f} Buena, convierte eficientemente respaldo contable en utilidad.\n")
                                else:
                                    print(f"Rentabilidad por acción: {rentabilidad_accion:.2f} Excelente, utilidades muy altas respecto al respaldo contable.\n")

                                print("\t--Utilidad valor nominal--")
                                if utilidad_valor_nominal < 1:
                                    print(f"Utilidad/Valor nominal: {utilidad_valor_nominal:.2f} Utilidad limitada respecto al valor nominal.\n")
                                elif 1 <= utilidad_valor_nominal < 2:
                                    print(f"Utilidad/Valor nominal: {utilidad_valor_nominal:.2f} Buen desempeño, utilidad superior al valor nominal.\n")
                                else:
                                    print(f"Utilidad/Valor nominal: {utilidad_valor_nominal:.2f} Excelente desempeño, utilidad muy superior al valor nominal.\n")
                            else:
                                print(bursatilidad)
                        except Exception as e:
                            print(f"Error al interpretar bursatilidad: {e}")
                    elif opcion == 6:
                        analisis_dupont = calcular_analisis_DuPont(estado_resultados, balance_general)
                        if isinstance(analisis_dupont, dict):
                            print(mostrar_analisis_dupont(analisis_dupont))
                            try:
                                margen_utilidad_neta = analisis_dupont.get("Margen de utilidad neta", 0)
                                rotacion_activos = analisis_dupont.get("Rotacion de activos totales", 0)
                                razon_endeudamiento = analisis_dupont.get("Razon de endeudamiento sobre patrimonio", 0)
                                roe = analisis_dupont.get("Rendimiento sobre capital (ROE)", 0)
                            except Exception as e:
                                print(f"Error al extraer las razones DuPont: {e}")
                                continue
                            print(f"\n{'*'*80}")
                            print("\t\t---Interpretación de resultados DuPont---")
                            print(f"{'*'*80}\n")

                            print("\t--Margen de utilidad neta--")
                            if margen_utilidad_neta < 5:
                                print("El margen de utilidad neta es bajo.")
                                print(f"La empresa obtiene {margen_utilidad_neta:.2f}% de utilidad por sus ventas.")
                                print("Lo que puede indicar altos costos o poca eficiencia operativa.\n")
                            elif margen_utilidad_neta > 15:
                                print("El margen de utilidad neta es alto.")
                                print(f"La empresa obtiene {margen_utilidad_neta:.2f}% de utilidad por sus ventas.")
                                print("Lo que puede indicar una excelente administración de costos y gastos.\n")
                            else:
                                print("El margen de utilidad neta es regular.")
                                print(f"La empresa obtiene {margen_utilidad_neta:.2f}% de utilidad por sus ventas.")
                                print("Lo que puede indicar una rentabilidad estable.\n")
                            
                            print("\t--Rotacion de activos totales--")
                            if rotacion_activos < 1:
                                print("La rotación de activos totales es baja.")
                                print(f"La empresa genera ${rotacion_activos:.2f} pesos por cada $1.00 invertido en activos.")
                                print("Lo que puede indicar poco aprovechamiento de los activos.\n")
                            elif rotacion_activos > 2:
                                print("La rotación de activos totales es alta.")
                                print(f"La empresa genera ${rotacion_activos:.2f} pesos por cada $1.00 invertido en activos.")
                                print("Lo que puede indicar un excelente uso de los activos.\n")
                            else:
                                print("La rotación de activos totales es regular.")
                                print(f"La empresa genera ${rotacion_activos:.2f} pesos por cada $1.00 invertido en activos.")
                                print("Lo que puede indicar un uso aceptable de los activos.\n")

                            print("\t--Razon de endeudamiento sobre patrimonio--")
                            if razon_endeudamiento < 1:
                                print("La razón de endeudamiento es baja.")
                                print(f"La empresa utiliza {razon_endeudamiento:.2f} veces deuda respecto a su patrimonio.")
                                print("Lo que puede indicar bajo riesgo financiero.\n")
                            elif razon_endeudamiento > 2:
                                print("La razón de endeudamiento es alta.")
                                print(f"La empresa utiliza {razon_endeudamiento:.2f} veces deuda respecto a su patrimonio.")
                                print("Lo que puede indicar un mayor riesgo financiero por exceso de deuda.\n")
                            else:
                                 print("La razón de endeudamiento es regular.")
                            print(f"La empresa utiliza {razon_endeudamiento:.2f} veces deuda respecto a su patrimonio.")
                            print("Lo que puede indicar un equilibrio financiero aceptable.\n")
                            print("\t--Rendimiento sobre capital (ROE)--")
                            if roe < 10:
                                print("El rendimiento sobre capital es bajo.")
                                print(f"La empresa genera {roe:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar baja rentabilidad para los inversionistas.\n")
                            elif roe > 20:
                                print("El rendimiento sobre capital es alto.")
                                print(f"La empresa genera {roe:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar una excelente generación de utilidades.\n")
                            else:
                                print("El rendimiento sobre capital es regular.")
                                print(f"La empresa genera {roe:.2f}% de rendimiento para los accionistas.")
                                print("Lo que puede indicar una rentabilidad estable para los inversionistas.\n")
                        else:
                            print(analisis_dupont)
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