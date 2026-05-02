import pandas as pd 
import os
import pickle
def input_catalogo_cuentas() -> dict | None:
    catalogo_cuentas = {}
    try:
        año = input("Ingrese el año: ")
        acreedores_diversos = float(input("Ingrese el saldo de Acreedores Diversos: "))
        anticipos_clientes = float(input("Ingrese el saldo de Anticipos a Clientes: "))
        bancos = float(input("Ingrese el saldo de Bancos: "))
        capital_social = float(input("Ingrese el saldo de Capital Social: "))
        clientes = float(input("Ingrese el saldo de Clientes: "))
        costo_ventas = float(input("Ingrese el saldo de Costo de Ventas: "))
        depreciacion_acumulada_activos_fijos = float(input("Ingrese el saldo de Depreciación Acumulada Activos Fijos: "))
        equipo_computo = float(input("Ingrese el saldo de Equipo de Cómputo: "))
        equipo_transporte = float(input("Ingrese el saldo de Equipo de Transporte: "))
        gastos_administrativos = float(input("Ingrese el saldo de Gastos Administrativos: "))
        gastos_instalacion = float(input("Ingrese el saldo de Gastos de Instalación: "))
        gastos_ventas = float(input("Ingrese el saldo de Gastos de Ventas: "))
        gastos_financieros = float(input("Ingrese el saldo de Gastos Financieros: "))
        gastos_depreciacion = float(input("Ingrese el saldo de Gastos de Depreciación: "))
        gastos_x_pagar = float(input("Ingrese el saldo de Gastos por Pagar: "))
        hipotecas_x_pagar_cp = float(input("Ingrese el saldo de Hipotecas por Pagar (Corto Plazo): "))
        hipotecas_x_pagar_lp = float(input("Ingrese el saldo de Hipotecas por Pagar (Largo Plazo): "))
        inventarios = float(input("Ingrese el saldo de Inventarios: "))
        inversiones_permanentes = float(input("Ingrese el saldo de Inversiones Permanentes: "))
        maquinaria_equipo = float(input("Ingrese el saldo de Maquinaria y Equipo: "))
        mobiliario_accesorios = float(input("Ingrese el saldo de Mobiliario y Accesorios: "))
        otros_gastos = float(input("Ingrese el saldo de Otros Gastos: "))
        otros_productos = float(input("Ingrese el saldo de Otros Productos: "))
        papeleria_utiles = float(input("Ingrese el saldo de Papelería y Útiles: "))
        prestamos_bancarios_cp = float(input("Ingrese el saldo de Préstamos Bancarios (Corto Plazo): "))
        prestamos_bancarios_lp = float(input("Ingrese el saldo de Préstamos Bancarios (Largo Plazo): "))
        productos_financieros = float(input("Ingrese el saldo de Productos Financieros: "))
        proveedores = float(input("Ingrese el saldo de Proveedores: "))
        reserva_legal = float(input("Ingrese el saldo de Reserva Legal: "))
        terreno_edificio = float(input("Ingrese el saldo de Terreno y Edificio: "))
        utilidades_ejercicio_anterior = float(input("Ingrese el saldo de Utilidades del Ejercicio Anterior: "))
        ventas = float(input("Ingrese el saldo de Ventas: "))
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.\n")
        return None
    else:
        catalogo_cuentas = {
            "Año": año,
            "Acreedores Diversos": acreedores_diversos,
            "Anticipos a Clientes": anticipos_clientes,
            "Bancos": bancos,
            "Capital Social": capital_social,
            "Clientes": clientes,
            "Costo de Ventas": costo_ventas,
            "Depreciación Acumulada Activos Fijos": depreciacion_acumulada_activos_fijos,
            "Equipo de Cómputo": equipo_computo,
            "Equipo de Transporte": equipo_transporte,
            "Gastos Administrativos": gastos_administrativos,
            "Gastos de Instalacion": gastos_instalacion,
            "Gastos de Ventas": gastos_ventas,
            "Gastos Financieros": gastos_financieros,
            "Gastos de Depreciacion": gastos_depreciacion,
            "Gastos por Pagar": gastos_x_pagar,
            "Hipotecas por Pagar (Corto Plazo)": hipotecas_x_pagar_cp,
            "Hipotecas por Pagar (Largo Plazo)": hipotecas_x_pagar_lp,
            "Inventarios": inventarios,
            "Inversiones Permanentes": inversiones_permanentes,
            "Maquinaria y Equipo": maquinaria_equipo,
            "Mobiliario y Accesorios": mobiliario_accesorios,
            "Otros Gastos": otros_gastos,
            "Otros Productos": otros_productos,
            "Papelería y Utiles": papeleria_utiles,
            "Préstamos Bancarios (Corto Plazo)": prestamos_bancarios_cp,
            "Préstamos Bancarios (Largo Plazo)": prestamos_bancarios_lp,
            "Productos Financieros": productos_financieros,
            "Proveedores": proveedores,
            "Reserva Legal": reserva_legal,
            "Terreno y Edificio": terreno_edificio,
            "Utilidades del Ejercicio Anterior": utilidades_ejercicio_anterior,
            "Ventas": ventas
        }
        return catalogo_cuentas
    
# Funciones para calcular los estados financieros
    
def calcular_estado_resultados(catalogo_cuentas: dict) -> dict | str:
    estado_resultados = {}
    try:
        isr=float(input("Ingrese la tasa del Impuesto Sobre la Renta (en porcentaje, por ejemplo, 30 para 30%): "))
        ptu=float(input("Ingrese la tasa de Participación de los Trabajadores en las Utilidades (en porcentaje, por ejemplo, 10 para 10%): "))
    except ValueError:
        return "Error: Por favor, ingrese un valor numérico válido para las tasas.\n"
    try:
        # Asignar los valores del catálogo de cuentas a las variables correspondientes
        estado_resultados["Año"] = catalogo_cuentas.get("Año", "")
        estado_resultados["Ventas"] = catalogo_cuentas.get("Ventas", 0)
        estado_resultados["Costo de Ventas"] = catalogo_cuentas.get("Costo de Ventas", 0)
        estado_resultados["UTILIDAD BRUTA"] = estado_resultados["Ventas"] - estado_resultados["Costo de Ventas"]
        estado_resultados["Gastos Generales"] = catalogo_cuentas.get("Gastos Generales", 0)
        estado_resultados["Gastos de Ventas"] = catalogo_cuentas.get("Gastos de Ventas", 0)
        estado_resultados["Gastos Administrativos"] = catalogo_cuentas.get("Gastos Administrativos", 0)
        estado_resultados["Gastos de Depreciacion"] = catalogo_cuentas.get("Gastos de Depreciacion", 0)
        estado_resultados["TOTAL GASTOS"] = estado_resultados["Gastos Generales"] + estado_resultados["Gastos de Ventas"] + estado_resultados["Gastos Administrativos"] + estado_resultados["Gastos de Depreciacion"]
        estado_resultados["UTILIDAD DE OPERACION"] = estado_resultados["UTILIDAD BRUTA"] - estado_resultados["TOTAL GASTOS"]
        estado_resultados["Gastos Financieros"] = catalogo_cuentas.get("Gastos Financieros", 0)
        estado_resultados["Productos Financieros"] = catalogo_cuentas.get("Productos Financieros", 0)
        estado_resultados["RESULTADO INTEGRAL DE FINANCIAMIENTO"]=estado_resultados["Gastos Financieros"]-estado_resultados["Productos Financieros"]
        estado_resultados["Otros Gastos"] = catalogo_cuentas.get("Otros Gastos", 0)
        estado_resultados["Otros Productos"] = catalogo_cuentas.get("Otros Productos", 0)
        estado_resultados["TOTAL PERTIDAS DISCONTINUAS"]=estado_resultados["Otros Gastos"]-estado_resultados["Otros Productos"]
        estado_resultados["TOTAL OTROS GASTOS Y PRODUCTOS"]=estado_resultados["RESULTADO INTEGRAL DE FINANCIAMIENTO"]+estado_resultados["TOTAL PERTIDAS DISCONTINUAS"]
        estado_resultados["UTILIDAD ANTES DE IMPUESTOS"]=estado_resultados["UTILIDAD DE OPERACION"]-estado_resultados["TOTAL OTROS GASTOS Y PRODUCTOS"]
        estado_resultados["Porcentaje ISR"]=isr/100
        estado_resultados["Porcentaje PTU"]=ptu/100
        estado_resultados["Valor ISR"]=estado_resultados["UTILIDAD ANTES DE IMPUESTOS"]*estado_resultados["Porcentaje ISR"]
        estado_resultados["Valor PTU"]=estado_resultados["UTILIDAD ANTES DE IMPUESTOS"]*estado_resultados["Porcentaje PTU"]
        estado_resultados["TOTAL IMPUESTOS"]=estado_resultados["Valor ISR"]+estado_resultados["Valor PTU"]
        estado_resultados["UTILIDAD NETA"]=estado_resultados["UTILIDAD ANTES DE IMPUESTOS"]-estado_resultados["TOTAL IMPUESTOS"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas.\n"
    return estado_resultados

def calcular_balance_general(catalogo_cuentas: dict, estado_resultados: dict) -> dict | str:
    balance_general = {}
    try:
        # Asignar los valores del catálogo de cuentas a las variables correspondientes
        balance_general["Año"] = catalogo_cuentas.get("Año", "")
        balance_general["ACTIVO CIRCULANTE"] = ""
        balance_general["Bancos"] = catalogo_cuentas.get("Bancos", 0)
        balance_general["Clientes"] = catalogo_cuentas.get("Clientes", 0)
        balance_general["Inventarios"] = catalogo_cuentas.get("Inventarios", 0)
        balance_general["Papelería y Utiles"] = catalogo_cuentas.get("Papelería y Utiles", 0)
        balance_general["TOTAL ACTIVO CIRCULANTE"] = catalogo_cuentas.get("Bancos", 0) + catalogo_cuentas.get("Clientes", 0) + catalogo_cuentas.get("Inventarios", 0) + catalogo_cuentas.get("Papelería y Utiles", 0)
        balance_general["ACTIVO NO CIRCULANTE"] = ""
        balance_general["Terreno y Edificio"] = catalogo_cuentas.get("Terreno y Edificio", 0)
        balance_general["Maquinaria y Equipo"] = catalogo_cuentas.get("Maquinaria y Equipo", 0)
        balance_general["Mobiliario y Accesorios"] = catalogo_cuentas.get("Mobiliario y Accesorios", 0)
        balance_general["Equipo de Transporte"] = catalogo_cuentas.get("Equipo de Transporte", 0)
        balance_general["Equipo de Cómputo"] = catalogo_cuentas.get("Equipo de Cómputo", 0)
        balance_general["Depreciación Acumulada Activos Fijos"] = catalogo_cuentas.get("Depreciación Acumulada Activos Fijos", 0)
        balance_general["Inversiones Permanentes"] = catalogo_cuentas.get("Inversiones Permanentes", 0)
        balance_general["OTROS ACTIVOS"] = ""
        balance_general["Gastos de Instalacion"] = catalogo_cuentas.get("Gastos de Instalacion", 0)
        balance_general["TOTAL ACTIVO NO CIRCULANTE"] = catalogo_cuentas.get("Maquinaria y Equipo", 0) + catalogo_cuentas.get("Mobiliario y Accesorios", 0) + catalogo_cuentas.get("Terreno y Edificio", 0) + catalogo_cuentas.get("Inversiones Permanentes", 0) + catalogo_cuentas.get("Equipo de Transporte",0) + catalogo_cuentas.get("Equipo de Cómputo", 0) + catalogo_cuentas.get("Depreciación Acumulada Activos Fijos", 0)
        balance_general["TOTAL ACTIVO"] = balance_general["TOTAL ACTIVO CIRCULANTE"] + balance_general["TOTAL ACTIVO NO CIRCULANTE"] + balance_general.get("Gastos de Instalacion", 0)
        balance_general["PASIVO A CORTO PLAZO"] = ""
        balance_general["Proveedores"] = catalogo_cuentas.get("Proveedores", 0)
        balance_general["Acreedores Diversos"] = catalogo_cuentas.get("Acreedores Diversos", 0)
        balance_general["Anticipos a Clientes"] = catalogo_cuentas.get("Anticipos a Clientes", 0)
        balance_general["Gastos por Pagar"] = catalogo_cuentas.get("Gastos por Pagar", 0)
        balance_general["Hipotecas por Pagar (Corto Plazo)"] = catalogo_cuentas.get("Hipotecas por Pagar (Corto Plazo)", 0)
        balance_general["Impuestos por Pagar"] = estado_resultados.get("TOTAL IMPUESTOS", 0)
        balance_general["Préstamos Bancarios (Corto Plazo)"] = catalogo_cuentas.get("Préstamos Bancarios (Corto Plazo)", 0)
        balance_general["TOTAL PASIVO CIRCULANTE"] = catalogo_cuentas.get("Proveedores", 0) + catalogo_cuentas.get("Gastos por Pagar", 0) + catalogo_cuentas.get("Hipotecas por Pagar (Corto Plazo)", 0) + catalogo_cuentas.get("Préstamos Bancarios (Corto Plazo)", 0) + catalogo_cuentas.get("Acreedores Diversos", 0) + catalogo_cuentas.get("Anticipos a Clientes", 0) + estado_resultados.get("TOTAL IMPUESTOS", 0)
        balance_general["PASIVO A LARGO PLAZO"] = ""
        balance_general["Hipotecas por Pagar (Largo Plazo)"] = catalogo_cuentas.get("Hipotecas por Pagar (Largo Plazo)", 0)
        balance_general["Préstamos Bancarios (Largo Plazo)"] = catalogo_cuentas.get("Préstamos Bancarios (Largo Plazo)", 0)
        balance_general["TOTAL PASIVO NO CIRCULANTE"] = catalogo_cuentas.get("Hipotecas por Pagar (Largo Plazo)", 0) + catalogo_cuentas.get("Préstamos Bancarios (Largo Plazo)", 0)
        balance_general["TOTAL PASIVO"] = balance_general["TOTAL PASIVO CIRCULANTE"] + balance_general["TOTAL PASIVO NO CIRCULANTE"]
        balance_general["CAPITAL CONTRIBUIDO"] = ""
        balance_general["Capital Social"] = catalogo_cuentas.get("Capital Social", 0)
        balance_general["CAPITAL GANADO"] = ""
        balance_general["Utilidades del Ejercicio Anterior"] = catalogo_cuentas.get("Utilidades del Ejercicio Anterior", 0)
        balance_general["Reserva Legal"] = catalogo_cuentas.get("Reserva Legal", 0)
        balance_general["Uitilidad del Ejercicio"] = estado_resultados.get("UTILIDAD NETA", 0)
        balance_general["Capital Contable"] = catalogo_cuentas.get("Capital Social", 0) + catalogo_cuentas.get("Reserva Legal", 0) + catalogo_cuentas.get("Utilidades del Ejercicio Anterior", 0) + estado_resultados.get("UTILIDAD NETA", 0)
        balance_general["TOTAL PASIVO Y CAPITAL CONTABLE"] = balance_general["TOTAL PASIVO"] + balance_general["Capital Contable"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas.\n"
    return balance_general

def calcular_capital_trabajo(balance_general: dict) -> dict | str:
    capital_trabajo = {}
    try:
        capital_trabajo["Año"] = balance_general.get("Año", "")
        capital_trabajo["TOTAL ACTIVO CIRCULANTE"] = balance_general.get("TOTAL ACTIVO CIRCULANTE", 0)
        capital_trabajo["TOTAL PASIVO CIRCULANTE"] = balance_general.get("TOTAL PASIVO CIRCULANTE", 0)
        capital_trabajo["CAPITAL DE TRABAJO"] = balance_general.get("TOTAL ACTIVO CIRCULANTE", 0) - balance_general.get("TOTAL PASIVO CIRCULANTE", 0)
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el balance general.\n"
    except Exception as e:
        return f"Error al calcular el capital de trabajo: {e}\n"
    return capital_trabajo

# Funciones para calcular las razones financieras

def calcular_razon_actividad(estado_resultados: dict, balance_general: dict, capital_trabajo: dict) -> dict | str:
    razon_actividad = {}
    try:
        razon_actividad["Año"] = estado_resultados.get("Año", "")
        razon_actividad["Costo de Ventas"] = estado_resultados.get("Costo de Ventas", 0)
        razon_actividad["Inventario"]= balance_general.get("Inventarios", 0)
        razon_actividad["ROTACION DE INVENTARIOS"] = razon_actividad["Costo de Ventas"] / razon_actividad["Inventario"]
        razon_actividad["Ventas"] = estado_resultados.get("Ventas", 0)
        razon_actividad["Cuentas por Cobrar"] = balance_general.get("Clientes", 0)
        razon_actividad["ROTACION CUENTAS POR COBRAR"] = razon_actividad["Ventas"] / razon_actividad["Cuentas por Cobrar"]
        razon_actividad["Costo de Ventas 2"] = razon_actividad["Costo de Ventas"]
        razon_actividad["Cuentas por Pagar"] = balance_general.get("Proveedores", 0)
        razon_actividad["ROTACION DE CUENTAS POR PAGAR"] = razon_actividad["Costo de Ventas 2"] / razon_actividad["Cuentas por Pagar"]
        razon_actividad["Ventas 2"] = razon_actividad["Ventas"]
        razon_actividad["TOTAL ACTIVO NO CIRCULANTE"] = balance_general.get("TOTAL ACTIVO NO CIRCULANTE", 0)
        razon_actividad["ROTACION DE ACTIVOS FIJOS"] = razon_actividad["Ventas 2"] / razon_actividad["TOTAL ACTIVO NO CIRCULANTE"]
        razon_actividad["Activos Totales"] = balance_general.get("TOTAL ACTIVO", 0)
        razon_actividad["Ventas 3"] = razon_actividad["Ventas"]
        razon_actividad["Activos Totales"] = balance_general.get("TOTAL ACTIVO", 0)
        razon_actividad["ROTACION DE ACTIVOS TOTALES"] = razon_actividad["Ventas 3"] / razon_actividad["Activos Totales"]
        razon_actividad["Ventas 2"] = razon_actividad["Ventas"]
        razon_actividad["CAPITAL DE TRABAJO"] = capital_trabajo.get("CAPITAL DE TRABAJO", 0)
        razon_actividad["ROTACION DE CAPITAL DE TRABAJO"] = razon_actividad["Ventas 2"] / razon_actividad["CAPITAL DE TRABAJO"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas o en el estado de resultados.\n"
    except Exception as e:
        return f"Error al calcular la razón de actividad: {e}\n"
    return razon_actividad

# Funciones para mostrar los estados financieros de forma legible utilizando pandas

def mostrar_catalogo_cuentas(catalogo_cuentas: dict) -> None:
    try:
        df=pd.DataFrame(catalogo_cuentas.items(), columns=["Cuenta", "Saldo"])
        print("\nCatálogo de Cuentas Cargado:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(f"{df}\n")
    except Exception as e:
        print(f"Error al cargar el catálogo de cuentas: {e}")

def mostrar_estado_resultados(estado_resultados: dict) -> str:
    try:
        df=pd.DataFrame(estado_resultados.items(), columns=["Concepto", "Valor"])
        print("\nEstado de Resultados:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(f"{df}\n")
    except Exception as e:
        return f"Error al mostrar el estado de resultados: {e}"
    
def mostrar_balance_general(balance_general: dict) -> str:
    try:
        df=pd.DataFrame(balance_general.items(), columns=["Concepto", "Valor"])
        print("\nBalance General:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(f"{df}\n")
    except Exception as e:
        return f"Error al mostrar el balance general: {e}"
    
def mostrar_capital_trabajo(capital_trabajo: dict) -> str:
    try:
        df=pd.DataFrame(capital_trabajo.items(), columns=["Concepto", "Valor"])
        print("\nCapital de Trabajo:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(f"{df}\n")
    except Exception as e:
        return f"Error al mostrar el capital de trabajo: {e}"

def mostrar_razon_actividad(razon_actividad: dict) -> str:
    try:
        df=pd.DataFrame(razon_actividad.items(), columns=["Concepto", "Valor"])
        print("\nRazón de Actividad:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(f"{df}\n")
    except Exception as e:
        return f"Error al mostrar la razón de actividad: {e}"
    

# Funciones para la persistencia de datos utilizando pickle
def cargar_datos_catalogo(nombre_archivo):
    """Intenta cargar el estado guardado (diccionarios y variables) desde un archivo."""
    archivo_datos = nombre_archivo
    if os.path.exists(archivo_datos):
        try:
            with open(archivo_datos, "rb") as f:
                datos_catalogo = pickle.load(f)
                return datos_catalogo
        except Exception as e:
            return f"Error al cargar datos: {e}. Iniciando con datos vacíos.\n"
    else:
        # Si no hay archivo retorna none
        return None

def guardar_datos(datos, nombre_archivo):
    """Guarda el estado actual (diccionarios y variables) en un archivo .pkl."""
    archivo_datos = nombre_archivo
    try:
        with open(archivo_datos, "wb") as f:
            pickle.dump(datos, f)
        print("--- Datos guardados exitosamente ---")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

