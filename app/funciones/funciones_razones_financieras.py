import pandas as pd 
import os
import pickle
def input_catalogo_cuentas() -> dict | None:
    catalogo_cuentas = {}
    try:
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
    
def calcular_estado_resultados(catalogo_cuentas: dict) -> dict | str:
    estado_resultados = {}
    try:
        isr=float(input("Ingrese la tasa del Impuesto Sobre la Renta (en porcentaje, por ejemplo, 30 para 30%): "))
        ptu=float(input("Ingrese la tasa de Participación de los Trabajadores en las Utilidades (en porcentaje, por ejemplo, 10 para 10%): "))
    except ValueError:
        return "Error: Por favor, ingrese un valor numérico válido para las tasas.\n"
    try:
        # Asignar los valores del catálogo de cuentas a las variables correspondientes
        estado_resultados["Ventas"] = catalogo_cuentas.get("Ventas", 0)
        estado_resultados["Costo de Ventas"] = catalogo_cuentas.get("Costo de Ventas", 0)
        estado_resultados["Utilidad Bruta"] = estado_resultados["Ventas"] - estado_resultados["Costo de Ventas"]
        estado_resultados["Gastos Generales"] = catalogo_cuentas.get("Gastos Generales", 0)
        estado_resultados["Gastos de Ventas"] = catalogo_cuentas.get("Gastos de Ventas", 0)
        estado_resultados["Gastos Administrativos"] = catalogo_cuentas.get("Gastos Administrativos", 0)
        estado_resultados["Gastos de Depreciacion"] = catalogo_cuentas.get("Gastos de Depreciacion", 0)
        estado_resultados["Total Gastos"] = estado_resultados["Gastos Generales"] + estado_resultados["Gastos de Ventas"] + estado_resultados["Gastos Administrativos"] + estado_resultados["Gastos de Depreciacion"]
        estado_resultados["Utilidad de Operacion"] = estado_resultados["Utilidad Bruta"] - estado_resultados["Total Gastos"]
        estado_resultados["Gastos Financieros"] = catalogo_cuentas.get("Gastos Financieros", 0)
        estado_resultados["Productos Financieros"] = catalogo_cuentas.get("Productos Financieros", 0)
        estado_resultados["Resultado Integral de Financiamiento"]=estado_resultados["Gastos Financieros"]-estado_resultados["Productos Financieros"]
        estado_resultados["Otros Gastos"] = catalogo_cuentas.get("Otros Gastos", 0)
        estado_resultados["Otros Productos"] = catalogo_cuentas.get("Otros Productos", 0)
        estado_resultados["Total Partidas Discontinuas"]=estado_resultados["Otros Gastos"]-estado_resultados["Otros Productos"]
        estado_resultados["Total Otros Gastos y Productos"]=estado_resultados["Resultado Integral de Financiamiento"]+estado_resultados["Total Partidas Discontinuas"]
        estado_resultados["Utilidad Antes de Impuestos"]=estado_resultados["Utilidad de Operacion"]-estado_resultados["Total Otros Gastos y Productos"]
        estado_resultados["Porcentaje ISR"]=isr/100
        estado_resultados["Porcentaje PTU"]=ptu/100
        estado_resultados["Valor ISR"]=estado_resultados["Utilidad Antes de Impuestos"]*estado_resultados["Porcentaje ISR"]
        estado_resultados["Valor PTU"]=estado_resultados["Utilidad Antes de Impuestos"]*estado_resultados["Porcentaje PTU"]
        estado_resultados["Total Impuestos"]=estado_resultados["Valor ISR"]+estado_resultados["Valor PTU"]
        estado_resultados["Utilidad Neta"]=estado_resultados["Utilidad Antes de Impuestos"]-estado_resultados["Total Impuestos"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas.\n"
    return estado_resultados

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
# Funciones que muestan los datos tabulados en la consola

def mostrar_catalogo_cuentas(catalogo_cuentas: dict) -> None:
    try:
        df=pd.DataFrame(catalogo_cuentas.items(), columns=["Cuenta", "Saldo"])
        print("\nCatálogo de Cuentas Cargado:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(df)
    except Exception as e:
        print(f"Error al cargar el catálogo de cuentas: {e}")

def mostrar_estado_resultados(estado_resultados: dict) -> str:
    try:
        df=pd.DataFrame(estado_resultados.items(), columns=["Concepto", "Valor"])
        print("\nEstado de Resultados:")
        pd.options.display.float_format = '{:,.2f}'.format
        print(df)
    except Exception as e:
        return f"Error al mostrar el estado de resultados: {e}"

