import pandas as pd 
import os
import pickle
def input_catalogo_cuentas() -> dict | str:
    catalogo_cuentas = {}
    try:
        año = input("Ingrese el año: ")
        if año.isnumeric():
            pass
        else:
            return "Error: Por favor, ingrese un valor numérico válido.\n"
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
        return "Error: Por favor, ingrese un valor numérico válido.\n"
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
        utilidad_bruta = estado_resultados["Ventas"] - estado_resultados["Costo de Ventas"]
        estado_resultados["UTILIDAD BRUTA"] = utilidad_bruta
        estado_resultados["Gastos Generales"] = catalogo_cuentas.get("Gastos Generales", 0)
        estado_resultados["Gastos de Ventas"] = catalogo_cuentas.get("Gastos de Ventas", 0)
        estado_resultados["Gastos Administrativos"] = catalogo_cuentas.get("Gastos Administrativos", 0)
        estado_resultados["Gastos de Depreciacion"] = catalogo_cuentas.get("Gastos de Depreciacion", 0)
        total_gastos = estado_resultados["Gastos Generales"] + estado_resultados["Gastos de Ventas"] + estado_resultados["Gastos Administrativos"] + estado_resultados["Gastos de Depreciacion"]
        estado_resultados["TOTAL GASTOS"] = total_gastos
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
        balance_general["Bancos"] = catalogo_cuentas.get("Bancos", 0)
        balance_general["Clientes"] = catalogo_cuentas.get("Clientes", 0)
        balance_general["Inventarios"] = catalogo_cuentas.get("Inventarios", 0)
        balance_general["Papelería y Utiles"] = catalogo_cuentas.get("Papelería y Utiles", 0)
        balance_general["TOTAL ACTIVO CIRCULANTE"] = catalogo_cuentas.get("Bancos", 0) + catalogo_cuentas.get("Clientes", 0) + catalogo_cuentas.get("Inventarios", 0) + catalogo_cuentas.get("Papelería y Utiles", 0)
        balance_general["Terreno y Edificio"] = catalogo_cuentas.get("Terreno y Edificio", 0)
        balance_general["Maquinaria y Equipo"] = catalogo_cuentas.get("Maquinaria y Equipo", 0)
        balance_general["Mobiliario y Accesorios"] = catalogo_cuentas.get("Mobiliario y Accesorios", 0)
        balance_general["Equipo de Transporte"] = catalogo_cuentas.get("Equipo de Transporte", 0)
        balance_general["Equipo de Cómputo"] = catalogo_cuentas.get("Equipo de Cómputo", 0)
        balance_general["Depreciación Acumulada Activos Fijos"] = catalogo_cuentas.get("Depreciación Acumulada Activos Fijos", 0)
        balance_general["Inversiones Permanentes"] = catalogo_cuentas.get("Inversiones Permanentes", 0)
        balance_general["Gastos de Instalacion"] = catalogo_cuentas.get("Gastos de Instalacion", 0)
        balance_general["TOTAL ACTIVO NO CIRCULANTE"] = catalogo_cuentas.get("Maquinaria y Equipo", 0) + catalogo_cuentas.get("Mobiliario y Accesorios", 0) + catalogo_cuentas.get("Terreno y Edificio", 0) + catalogo_cuentas.get("Inversiones Permanentes", 0) + catalogo_cuentas.get("Equipo de Transporte",0) + catalogo_cuentas.get("Equipo de Cómputo", 0) + catalogo_cuentas.get("Depreciación Acumulada Activos Fijos", 0)
        balance_general["TOTAL ACTIVO"] = balance_general["TOTAL ACTIVO CIRCULANTE"] + balance_general["TOTAL ACTIVO NO CIRCULANTE"] + balance_general.get("Gastos de Instalacion", 0)
        balance_general["Proveedores"] = catalogo_cuentas.get("Proveedores", 0)
        balance_general["Acreedores Diversos"] = catalogo_cuentas.get("Acreedores Diversos", 0)
        balance_general["Anticipos a Clientes"] = catalogo_cuentas.get("Anticipos a Clientes", 0)
        balance_general["Gastos por Pagar"] = catalogo_cuentas.get("Gastos por Pagar", 0)
        balance_general["Hipotecas por Pagar (Corto Plazo)"] = catalogo_cuentas.get("Hipotecas por Pagar (Corto Plazo)", 0)
        balance_general["Impuestos por Pagar"] = estado_resultados.get("TOTAL IMPUESTOS", 0)
        balance_general["Préstamos Bancarios (Corto Plazo)"] = catalogo_cuentas.get("Préstamos Bancarios (Corto Plazo)", 0)
        balance_general["TOTAL PASIVO CIRCULANTE"] = catalogo_cuentas.get("Proveedores", 0) + catalogo_cuentas.get("Gastos por Pagar", 0) + catalogo_cuentas.get("Hipotecas por Pagar (Corto Plazo)", 0) + catalogo_cuentas.get("Préstamos Bancarios (Corto Plazo)", 0) + catalogo_cuentas.get("Acreedores Diversos", 0) + catalogo_cuentas.get("Anticipos a Clientes", 0) + estado_resultados.get("TOTAL IMPUESTOS", 0)
        balance_general["Hipotecas por Pagar (Largo Plazo)"] = catalogo_cuentas.get("Hipotecas por Pagar (Largo Plazo)", 0)
        balance_general["Préstamos Bancarios (Largo Plazo)"] = catalogo_cuentas.get("Préstamos Bancarios (Largo Plazo)", 0)
        balance_general["TOTAL PASIVO NO CIRCULANTE"] = catalogo_cuentas.get("Hipotecas por Pagar (Largo Plazo)", 0) + catalogo_cuentas.get("Préstamos Bancarios (Largo Plazo)", 0)
        balance_general["TOTAL PASIVO"] = balance_general["TOTAL PASIVO CIRCULANTE"] + balance_general["TOTAL PASIVO NO CIRCULANTE"]
        balance_general["Capital Social"] = catalogo_cuentas.get("Capital Social", 0)
        balance_general["Utilidades del Ejercicio Anterior"] = catalogo_cuentas.get("Utilidades del Ejercicio Anterior", 0)
        balance_general["Reserva Legal"] = catalogo_cuentas.get("Reserva Legal", 0)
        balance_general["Utilidad del Ejercicio"] = estado_resultados.get("UTILIDAD NETA", 0)
        balance_general["Total Capital Ganado"] = balance_general["Utilidades del Ejercicio Anterior"] + balance_general["Reserva Legal"] + balance_general["Utilidad del Ejercicio"]
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
        razon_actividad["Cuentas por Pagar"] = balance_general.get("Proveedores", 0)
        razon_actividad["ROTACION DE CUENTAS POR PAGAR"] = razon_actividad["Costo de Ventas"] / razon_actividad["Cuentas por Pagar"]
        razon_actividad["TOTAL ACTIVO NO CIRCULANTE"] = balance_general.get("TOTAL ACTIVO NO CIRCULANTE", 0)
        razon_actividad["ROTACION DE ACTIVOS FIJOS"] = razon_actividad["Ventas"] / razon_actividad["TOTAL ACTIVO NO CIRCULANTE"]
        razon_actividad["Activos Totales"] = balance_general.get("TOTAL ACTIVO", 0)
        razon_actividad["Activos Totales"] = balance_general.get("TOTAL ACTIVO", 0)
        razon_actividad["ROTACION DE ACTIVOS TOTALES"] = razon_actividad["Ventas"] / razon_actividad["Activos Totales"]
        razon_actividad["CAPITAL DE TRABAJO"] = capital_trabajo.get("CAPITAL DE TRABAJO", 0)
        razon_actividad["ROTACION DE CAPITAL DE TRABAJO"] = razon_actividad["Ventas"] / razon_actividad["CAPITAL DE TRABAJO"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas o en el estado de resultados.\n"
    except Exception as e:
        return f"Error al calcular la razón de actividad: {e}\n"
    return razon_actividad

def calcular_razon_liquidez(balance_general: dict, catalogo_cuentas: dict) -> dict | str:
    razon_liquidez = {}

    try:
        razon_liquidez["Año"] = balance_general.get("Año", "")
        razon_liquidez["Activo Circulante"] = balance_general.get("TOTAL ACTIVO CIRCULANTE", 0)
        razon_liquidez["Pasivo a Corto Plazo"] = balance_general.get("TOTAL PASIVO CIRCULANTE", 0)
        razon_liquidez["RAZON CIRCULANTE"] = (
            razon_liquidez["Activo Circulante"] /
            razon_liquidez["Pasivo a Corto Plazo"]
            if razon_liquidez["Pasivo a Corto Plazo"] != 0 else 0
        )

        razon_liquidez["Inventario"] = catalogo_cuentas.get("Inventarios", 0)
        razon_liquidez["ACTIVO MENOS INVENTARIO"] = (
            razon_liquidez["Activo Circulante"] -
            razon_liquidez["Inventario"]
        )

        razon_liquidez["PRUEBA ACIDA"] = (
            razon_liquidez["ACTIVO MENOS INVENTARIO"] /
            razon_liquidez["Pasivo a Corto Plazo"]
            if razon_liquidez["Pasivo a Corto Plazo"] != 0 else 0
        )

        razon_liquidez["Efectivo"] = catalogo_cuentas.get("Bancos", 0)

        razon_liquidez["RAZON DE EFECTIVO"] = (
            razon_liquidez["Efectivo"] /
            razon_liquidez["Pasivo a Corto Plazo"]
            if razon_liquidez["Pasivo a Corto Plazo"] != 0 else 0
        )
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el balance general o catálogo de cuentas.\n"
    except Exception as e:
        return f"Error al calcular la razón de liquidez: {e}\n"
    
    return razon_liquidez

def calcular_razon_endeudamiento(
    balance_general: dict,
    estado_resultados: dict,
    catalogo_cuentas: dict
) -> dict | str:

    razon_endeudamiento = {}

    try:

        razon_endeudamiento["Año"] = balance_general.get("Año", "")

        razon_endeudamiento["Pasivos"] = balance_general.get("TOTAL PASIVO", 0)

        razon_endeudamiento["Activos"] = balance_general.get("TOTAL ACTIVO", 0)

        razon_endeudamiento["RAZON DE ENDEUDAMIENTO"] = (
            (razon_endeudamiento["Pasivos"] /
            razon_endeudamiento["Activos"]) * 100
            if razon_endeudamiento["Activos"] != 0 else 0
        )

        razon_endeudamiento["Capital Contable"] = balance_general.get("Capital Contable", 0)

        razon_endeudamiento["RAZON DE CAPITAL"] = (
            (razon_endeudamiento["Capital Contable"] /
            razon_endeudamiento["Activos"]) * 100
            if razon_endeudamiento["Activos"] != 0 else 0
        )

        razon_endeudamiento["Pasivo LP"] = balance_general.get(
            "TOTAL PASIVO NO CIRCULANTE",
            0
        )

        razon_endeudamiento["Capital Social"] = catalogo_cuentas.get(
            "Capital Social",
            0
        )

        razon_endeudamiento["APALANCAMIENTO FINANCIERO"] = (
            razon_endeudamiento["Pasivo LP"] /
            razon_endeudamiento["Capital Social"]
            if razon_endeudamiento["Capital Social"] != 0 else 0
        )

        razon_endeudamiento["UAI"] = estado_resultados.get(
            "UTILIDAD ANTES DE IMPUESTOS",
            0
        )

        razon_endeudamiento["GF"] = catalogo_cuentas.get(
            "Gastos Financieros",
            0
        )

        razon_endeudamiento["UAI+GF"] = (
            razon_endeudamiento["UAI"] +
            razon_endeudamiento["GF"]
        )

        razon_endeudamiento["COBERTURA DE INTERESES"] = (
            razon_endeudamiento["UAI+GF"] /
            razon_endeudamiento["GF"]
            if razon_endeudamiento["GF"] != 0 else 0
        )

    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en los estados financieros.\n"

    except Exception as e:
        return f"Error al calcular la razón de endeudamiento: {e}\n"

    return razon_endeudamiento

def calcular_razon_rentabilidad(estado_resultados: dict, balance_general: dict) -> dict | str:
    razon_rentabilidad = {}
    try:
        razon_rentabilidad["Año"] = estado_resultados.get("Año", "")
        razon_rentabilidad["Utilidad neta"] = estado_resultados.get("UTILIDAD NETA", 0)
        razon_rentabilidad["Ventas"] = estado_resultados.get("Ventas", 0)
        razon_rentabilidad["MARGEN DE UTILIDAD"] = (razon_rentabilidad["Utilidad neta"] / razon_rentabilidad["Ventas"]) * 100 if razon_rentabilidad["Ventas"] != 0 else 0
        razon_rentabilidad["Utilidad bruta"] = estado_resultados.get("UTILIDAD BRUTA", 0)
        razon_rentabilidad["MARGEN DE UTILIDAD BRUTA"] = (razon_rentabilidad["Utilidad bruta"] / razon_rentabilidad["Ventas"]) * 100 if razon_rentabilidad["Ventas"] != 0 else 0
        razon_rentabilidad["Utilidad de operacion"] = estado_resultados.get("UTILIDAD DE OPERACION", 0)
        razon_rentabilidad["MARGEN DE UTILIDAD OPERATIVA"] = (razon_rentabilidad["Utilidad de operacion"] / razon_rentabilidad["Ventas"]) * 100 if razon_rentabilidad["Ventas"] != 0 else 0
        razon_rentabilidad["Total activos"] = balance_general.get("TOTAL ACTIVO", 0)
        razon_rentabilidad["RENDIMIENTO SOBRE LOS ACTIVOS TOTALES"] = (razon_rentabilidad["Utilidad neta"] / razon_rentabilidad["Total activos"]) * 100 if razon_rentabilidad["Total activos"] != 0 else 0
        razon_rentabilidad["Capital contable"] = balance_general.get("Capital Contable", 0)
        razon_rentabilidad["RENDIMIENTO SOBRE EL PATRIMONIO"] = (razon_rentabilidad["Utilidad neta"] / razon_rentabilidad["Capital contable"]) * 100 if razon_rentabilidad["Capital contable"] != 0 else 0
        razon_rentabilidad["Capital social"] =balance_general.get("Capital Social", 0)
        razon_rentabilidad["RENDIMIENTO SOBRE EL CAPITAL COMUN"] = (razon_rentabilidad["Utilidad neta"] / razon_rentabilidad["Capital social"]) * 100 if razon_rentabilidad["Capital social"] != 0 else 0
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas o en el estado de resultados.\n"
    except Exception as e:
        return f"Error al calcular la razón de actividad: {e}\n"
    return razon_rentabilidad  


def calcular_bursatilidad(estado_resultados: dict, balance_general: dict) -> dict | str:
    bursatilidad = {}

    try:
        Numero_de_acciones = float(input("Ingrese el numero de acciones: "))
        valor_en_mercado = float(input("Ingrese el valor de mercado: "))
    except ValueError:
        return "Error: Por favor, ingrese un valor numérico válido.\n"

    try:
        bursatilidad ["Año"]= balance_general.get("Año")
        bursatilidad ["Capital social"] = balance_general.get("Capital Social", 0)
        bursatilidad ["Numero de acciones"] = Numero_de_acciones
        bursatilidad ["R_V_N"] = bursatilidad["Capital social"] / bursatilidad["Numero de acciones"]
        bursatilidad ["Capital contable"] = balance_general.get("TOTAL PASIVO Y CAPITAL CONTABLE", 0)
        bursatilidad["Numero de acciones"] = Numero_de_acciones
        bursatilidad["R_V_L"] = bursatilidad ["Capital contable"] / bursatilidad["Numero de acciones"]
        bursatilidad["Valor en mercado"] = valor_en_mercado
        bursatilidad["Valor en libros"] = bursatilidad["R_V_L"] 
        bursatilidad["R_V_ML"] = bursatilidad ["Valor en mercado"] / bursatilidad["Valor en libros"]
        bursatilidad["Utilidad del ejercicio"] = estado_resultados.get("UTILIDAD NETA", 0) 
        bursatilidad["Numero de acciones"] = Numero_de_acciones
        bursatilidad["Valor por accion"] = bursatilidad["Utilidad del ejercicio"] /bursatilidad["Numero de acciones"]
        bursatilidad["Valor en mercado"] = valor_en_mercado
        bursatilidad["Utilidad x accion"] = bursatilidad["Valor por accion"] 
        bursatilidad["R_P_U"] = bursatilidad["Valor en mercado"] / bursatilidad["Utilidad x accion"]
        bursatilidad["Utilidad por accion"] = bursatilidad["Utilidad x accion"]
        bursatilidad["Valor en libros"] = bursatilidad["R_V_L"] 
        bursatilidad["R_R_A"] =bursatilidad["Utilidad por accion"] / bursatilidad["Valor en libros"]
        bursatilidad["Utilidad x accion"] = bursatilidad["Utilidad por accion"] 
        bursatilidad["Valor nominal"] = bursatilidad["R_V_N"] 
        bursatilidad["R_U_V"] = bursatilidad["Utilidad x accion"] * bursatilidad["Valor nominal"]
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas o en el estado de resultados.\n"
    except Exception as e:
        return f"Error al calcular la razón: {e}\n"
    return bursatilidad

def calcular_analisis_DuPont(estado_resultados: dict, balance_general: dict) -> dict | str:
    analisis_dupont = {}
    try:
        analisis_dupont["Año"] = estado_resultados.get("Año", "")
        analisis_dupont["Utilidad neta"] = estado_resultados.get("UTILIDAD NETA", 0)
        analisis_dupont["Ventas"] = estado_resultados.get("Ventas", 0)
        analisis_dupont["Total de activos"] = balance_general.get("TOTAL ACTIVO", 0)
        analisis_dupont["Capital Contable"] = balance_general.get("Capital Contable", 0)
        analisis_dupont["Margen de utilidad neta"] = (analisis_dupont["Utilidad neta"] / analisis_dupont["Ventas"] if analisis_dupont["Ventas"] != 0 else 0)
        analisis_dupont["Rotacion de activos totales"] = (analisis_dupont["Ventas"] / analisis_dupont["Total de activos"] if analisis_dupont["Total de activos"] != 0 else 0)
        analisis_dupont["Rendimiento sobre activos (ROA)"] = (analisis_dupont["Margen de utilidad neta"] * analisis_dupont["Rotacion de activos totales"])
        analisis_dupont["Razon de endeudamiento sobre patrimonio"] = (analisis_dupont["Total de activos"] / analisis_dupont["Capital Contable"]if analisis_dupont["Capital Contable"] != 0 else 0)
        analisis_dupont["Rendimiento sobre capital (ROE)"] = (analisis_dupont["Rendimiento sobre activos (ROA)"] * analisis_dupont["Razon de endeudamiento sobre patrimonio"]) * 100
    except KeyError as e:
        return f"Error: La cuenta '{e.args[0]}' no se encuentra en el catálogo de cuentas o en el estado de resultados.\n"
    except Exception as e:
        return f"Error al calcular el analisis DuPont: {e}\n"
    return analisis_dupont
    
# Funciones para mostrar los estados financieros de forma legible utilizando pandas

def mostrar_catalogo_cuentas(catalogo_cuentas: dict) -> str:
    try:
        df=pd.DataFrame(catalogo_cuentas.items(), columns=["Cuenta", "Saldo"])
        print("\nCatálogo de Cuentas Cargado:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al cargar el catálogo de cuentas: {e}"

def mostrar_estado_resultados(estado_resultados: dict) -> str:
    try:
        #df=pd.DataFrame(estado_resultados.items(), columns=["Concepto", "Valor"])
        df=pd.DataFrame({
            "Valor":[
                estado_resultados.get("Año", 0), estado_resultados.get("Ventas", 0), estado_resultados.get("Costo de Ventas", 0), "", estado_resultados.get("Gastos Generales", 0),
                estado_resultados.get("Gastos de Ventas", 0), estado_resultados.get("Gastos Administrativos", 0), estado_resultados.get("Gastos de Depreciacion", 0), estado_resultados.get("TOTAL GASTOS", 0),
                "", estado_resultados.get("Gastos Financieros", 0), estado_resultados.get("Productos Financieros", 0), estado_resultados.get("RESULTADO INTEGRAL DE FINANCIAMIENTO", 0), estado_resultados.get("Otros Gastos", 0),
                estado_resultados.get("Otros Productos", 0), estado_resultados.get("TOTAL PERTIDAS DISCONTINUAS", 0), estado_resultados.get("TOTAL OTROS GASTOS Y PRODUCTOS", 0), "", estado_resultados.get("Porcentaje ISR", 0),
                estado_resultados.get("Porcentaje PTU", 0), estado_resultados.get("Valor ISR", 0), estado_resultados.get("Valor PTU", 0), estado_resultados.get("TOTAL IMPUESTOS", 0), ""
            ],
            "Utilidad":[
                "", "", "", estado_resultados.get("UTILIDAD BRUTA", 0), "",
                "", "", "", "",
                estado_resultados.get("UTILIDAD DE OPERACION", 0), "", "", "", "",
                "", "", "", estado_resultados.get("UTILIDAD ANTES DE IMPUESTOS", 0), "",
                "", "", "", "", estado_resultados.get("UTILIDAD NETA", 0)
            ]
        })

        df.index = [
            "Año", "Ventas", "Costo de Ventas", "UTILIDAD BRUTA", "Gastos Generales",
            "Gastos de Ventas", "Gastos Administrativos", "Gastos de Depreciacion", "TOTAL GASTOS",
            "UTILIDAD DE OPERACION", "Gastos Financieros", "Productos Financieros", "RESULTADO INTEGRAL DE FINANCIAMIENTO", "Otros Gastos",
            "Otros Productos", "TOTAL PERTIDAS DISCONTINUAS", "TOTAL OTROS GASTOS Y PRODUCTOS", "UTILIDAD ANTES DE IMPUESTOS", "Porcentaje ISR",
            "Porcentaje PTU", "Valor ISR", "Valor PTU", "TOTAL IMPUESTOS", "UTILIDAD NETA"
        ]
        print("\nEstado de Resultados:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar el estado de resultados: {e}"
    
def mostrar_balance_general(balance_general: dict) -> str:
    try:
        df=pd.DataFrame({
            "Valor":[
                balance_general.get("Año", 0), "", balance_general.get("Bancos", 0), balance_general.get("Clientes", 0), balance_general.get("Inventarios", 0), balance_general.get("Papelería y Utiles", 0), "",
                "", balance_general.get("Terreno y Edificio", 0), balance_general.get("Maquinaria y Equipo", 0), balance_general.get("Mobiliario y Accesorios", 0), balance_general.get("Equipo de Transporte", 0), balance_general.get("Equipo de Cómputo", 0), balance_general.get("Depreciación Acumulada Activos Fijos", 0), 
                balance_general.get("Inversiones Permanentes", 0), "", balance_general.get("Gastos de Instalacion", 0), "", "", "", balance_general.get("Proveedores", 0), 
                balance_general.get("Acreedores Diversos", 0), balance_general.get("Anticipos a Clientes", 0), balance_general.get("Gastos por Pagar", 0), balance_general.get("Hipotecas por Pagar (Corto Plazo)", 0), balance_general.get("Impuestos por Pagar", 0), balance_general.get("Préstamos Bancarios (Corto Plazo)", 0), "",
                "", balance_general.get("Hipotecas por Pagar (Largo Plazo)", 0),balance_general.get("Préstamos Bancarios (Largo Plazo)", 0), "", "", "", balance_general.get("Capital Social", 0), 
                "", balance_general.get("Utilidades del Ejercicio Anterior", 0), balance_general.get("Reserva Legal", 0), balance_general.get("Utilidad del Ejercicio", 0), "", "", ""
            ], 
            "Suma Activo/Pasivo":[
                "", "", "", "", "", "", balance_general.get("TOTAL ACTIVO CIRCULANTE", 0),
                "", "", "", "", "", "", "", 
                "", "", "", balance_general.get("TOTAL ACTIVO NO CIRCULANTE", 0), "","", "",
                "", "", "", "", "", "", balance_general.get("TOTAL PASIVO CIRCULANTE", 0),
                "", "", "", balance_general.get("TOTAL PASIVO NO CIRCULANTE", 0), "", "", balance_general.get("Capital Social", 0),
                "", "", "", "", balance_general.get("Total Capital Ganado", 0), balance_general.get("Capital Contable", 0), ""
            ], 
            "Total Activo/Pasivo":[
                "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", 
                "", "", "", "", balance_general.get("TOTAL ACTIVO", 0), "", "", 
                "", "", "", "", "", "", "", 
                "","", "", "", balance_general.get("TOTAL PASIVO", 0), "", "", 
                "", "", "", "", "", "", balance_general.get("TOTAL PASIVO Y CAPITAL CONTABLE", 0)
            ]
        })

        df.index = [
            "Año", "ACTIVO CIRCULANTE", "Bancos", "Clientes", "Inventarios", "Papelería y Utiles", "TOTAL ACTIVO CIRCULANTE",
            "ACTIVO NO CIRCULANTE", "Terreno y Edificio", "Maquinaria y Equipo", "Mobiliario y Accesorios", "Equipo de Transporte", "Equipo de Cómputo", "Depreciación Acumulada Activos Fijos", 
            "Inversiones Permanentes", "OTROS ACTIVOS", "Gastos de Instalacion", "TOTAL ACTIVO NO CIRCULANTE", "TOTAL ACTIVO", "PASIVO A CORTO PLAZO", "Proveedores", 
            "Acreedores Diversos", "Anticipos a Clientes", "Gastos por Pagar", "Hipotecas por Pagar (Corto Plazo)", "Impuestos por Pagar", "Préstamos Bancarios (Corto Plazo)", "TOTAL PASIVO CIRCULANTE",
            "PASIVO A LARGO PLAZO", "Hipotecas por Pagar (Largo Plazo)", "Préstamos Bancarios (Largo Plazo)", "TOTAL PASIVO NO CIRCULANTE", "TOTAL PASIVO", "CAPITAL CONTRIBUIDO", "Capital Social", 
            "CAPITAL GANADO", "Utilidades del Ejercicio Anterior", "Reserva Legal", "Utilidad del Ejercicio", "Total Capital Ganado", "Capital Contable", "TOTAL PASIVO Y CAPITAL CONTABLE"
        ]
        print("\nBalance General:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar el balance general: {e}"
    
def mostrar_capital_trabajo(capital_trabajo: dict) -> str:
    try:
        df=pd.DataFrame(capital_trabajo.items(), columns=["Concepto", "Valor"])
        print("\nCapital de Trabajo:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar el capital de trabajo: {e}"

def mostrar_razon_actividad(razon_actividad: dict) -> str:
    try:
        df=pd.DataFrame({
            "Valor":[
                razon_actividad.get("Año"), razon_actividad.get("Costo de Ventas"), razon_actividad.get("Inventario"), "",
                razon_actividad.get("Ventas"), razon_actividad.get("Cuentas por Cobrar"), "", razon_actividad.get("Costo de Ventas"),
                razon_actividad.get("Cuentas por Pagar"), "", razon_actividad.get("Ventas"), razon_actividad.get("TOTAL ACTIVO NO CIRCULANTE"),
                "", razon_actividad.get("Activos Totales"), razon_actividad.get("Ventas"), "",
                razon_actividad.get("Ventas"), razon_actividad.get("CAPITAL DE TRABAJO"), ""
            ],
            "Rotacion":[
                "", "", "", razon_actividad.get("ROTACION DE INVENTARIOS"),
                "", "", razon_actividad.get("ROTACION CUENTAS POR COBRAR"), "",
                "", razon_actividad.get("ROTACION DE CUENTAS POR PAGAR"), "", "",
                razon_actividad.get("ROTACION DE ACTIVOS FIJOS"), "", "", razon_actividad.get("ROTACION DE ACTIVOS TOTALES"),
                "", "", razon_actividad.get("ROTACION DE CAPITAL DE TRABAJO")
            ]
        })
        df.index = [
            "Año", "Costo de Ventas", "Inventario", "ROTACION DE INVENTARIOS",
            "Ventas", "Cuentas por Cobrar", "ROTACION CUENTAS POR COBRAR", "Costo de Ventas", 
            "Cuentas por Pagar", "ROTACION DE CUENTAS POR PAGAR", "Ventas", "TOTAL ACTIVO NO CIRCULANTE", 
            "ROTACION DE ACTIVOS FIJOS", "Activos Totales", "Ventas", "ROTACION DE ACTIVOS TOTALES",
            "Ventas", "CAPITAL DE TRABAJO", "ROTACION DE CAPITAL DE TRABAJO"
        ]
        print("\nRazón de Actividad:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar la razón de actividad: {e}\n"
    
def mostrar_razon_liquidez(razon_liquidez: dict, capital_trabajo: dict) -> str:

    try:
        print("\nRAZONES DE LIQUIDEZ\n")

        df_capital_trabajo = pd.DataFrame({
            "Valor": [
                capital_trabajo.get("Año", ""),
                capital_trabajo.get("TOTAL ACTIVO CIRCULANTE", 0),
                capital_trabajo.get("TOTAL PASIVO CIRCULANTE", 0),
                capital_trabajo.get("CAPITAL DE TRABAJO", 0)
            ]
        })

        df_capital_trabajo.index = [
            "Año",
            "Activo Circulante",
            "Pasivo a Corto Plazo",
            "Capital de Trabajo"
        ]

        print("\n--- CAPITAL DE TRABAJO ---")
        print(df_capital_trabajo.to_string())

        df_razon_circulante = pd.DataFrame({
            "Valor": [
                razon_liquidez.get("Año", ""),
                f"{razon_liquidez.get('Activo Circulante', 0):,.2f}",
                f"{razon_liquidez.get('Pasivo a Corto Plazo', 0):,.2f}",
                f"{razon_liquidez.get('RAZON CIRCULANTE', 0):.4f}"
            ]
        })

        df_razon_circulante.index = [
            "Año",
            "Activo Circulante",
            "Pasivo a Corto Plazo",
            "Razon Circulante"
        ]

        print("\n--- RAZON CIRCULANTE ---")
        print(df_razon_circulante.to_string())

        df_prueba_acida = pd.DataFrame({
            "Valor": [
                razon_liquidez.get("Año", ""),
                f"{razon_liquidez.get('ACTIVO MENOS INVENTARIO', 0):,.2f}",
                f"{razon_liquidez.get('Pasivo a Corto Plazo', 0):,.2f}",
                f"{razon_liquidez.get('PRUEBA ACIDA', 0):.4f}"
            ]
        })

        df_prueba_acida.index = [
            "Año",
            "ACT-INV",
            "Pasivo a Corto Plazo",
            "Prueba Acida"
        ]

        print("\n--- PRUEBA ACIDA ---")
        print(df_prueba_acida.to_string())

        df_razon_efectivo = pd.DataFrame({
            "Valor": [
                razon_liquidez.get("Año", ""),
                f"{razon_liquidez.get('Efectivo', 0):,.2f}",
                f"{razon_liquidez.get('Pasivo a Corto Plazo', 0):,.2f}",
                f"{razon_liquidez.get('RAZON DE EFECTIVO', 0):.4f}"
            ]
        })

        df_razon_efectivo.index = [
            "Año",
            "Efectivo",
            "Pasivo a Corto Plazo",
            "Razon de Efectivo"
        ]

        print("\n--- RAZON DE EFECTIVO ---")
        print(df_razon_efectivo.to_string())

        return "\nRazones de liquidez mostradas correctamente.\n"
    except Exception as e:
        return f"Error al mostrar la razón de liquidez: {e}\n"
    
def mostrar_razon_endeudamiento(
    razon_endeudamiento: dict
) -> str:

    try:

        df = pd.DataFrame({

            "Valor":[

                razon_endeudamiento.get("Año", ""),

                f"{razon_endeudamiento.get('Pasivos', 0):,.2f}",
                f"{razon_endeudamiento.get('Activos', 0):,.2f}",
                "",

                f"{razon_endeudamiento.get('Capital Contable', 0):,.2f}",
                f"{razon_endeudamiento.get('Activos', 0):,.2f}",
                "",

                f"{razon_endeudamiento.get('Pasivo LP', 0):,.2f}",
                f"{razon_endeudamiento.get('Capital Social', 0):,.2f}",
                "",

                f"{razon_endeudamiento.get('UAI+GF', 0):,.2f}",
                f"{razon_endeudamiento.get('GF', 0):,.2f}",
                ""

            ],

            "Porcentaje":[

                "",

                "",
                "",
                f"{razon_endeudamiento.get('RAZON DE ENDEUDAMIENTO', 0):.2f}%",

                "",
                "",
                f"{razon_endeudamiento.get('RAZON DE CAPITAL', 0):.2f}%",

                "",
                "",
                f"{razon_endeudamiento.get('APALANCAMIENTO FINANCIERO', 0):.2f}",

                "",
                "",
                f"{razon_endeudamiento.get('COBERTURA DE INTERESES', 0):.2f}"

            ]

        })

        df.index = [

            "Año",

            "Pasivos",
            "Activos",
            "Razon de endeudamiento %",

            "Capital contable",
            "Activos",
            "Razon de capital %",

            "Pasivo LP",
            "Capital social",
            "Apalancamiento financiero",

            "UAI+GF",
            "GF",
            "Cobertura de intereses"

        ]

        print("\nRazón de Endeudamiento:")

        pd.options.display.float_format = '{:,.2f}'.format

        return f"{df}\n"

    except Exception as e:
        return f"Error al mostrar la razón de endeudamiento: {e}\n"

def mostrar_razon_rentabilidad(razon_rentabilidad: dict) -> str:
    try:
        df=pd.DataFrame({    
            "Valor":[
                razon_rentabilidad.get("Año"), razon_rentabilidad.get("Utilidad neta"), razon_rentabilidad.get("Ventas"), "",  
                razon_rentabilidad.get("Utilidad bruta"), "", razon_rentabilidad.get("Utilidad de operacion"), "", 
                razon_rentabilidad.get("Total activos"), "", razon_rentabilidad.get("Capital contable"), "", razon_rentabilidad.get("Capital social"),""
            ],    
            "Porcentaje":[
                "", "", "", razon_rentabilidad.get("MARGEN DE UTILIDAD"), "", razon_rentabilidad.get("MARGEN DE UTILIDAD BRUTA"), "", 
                razon_rentabilidad.get("MARGEN DE UTILIDAD OPERATIVA"), "", razon_rentabilidad.get("RENDIMIENTO SOBRE LOS ACTIVOS TOTALES"), "", 
                razon_rentabilidad.get("RENDIMIENTO SOBRE EL PATRIMONIO"), "", razon_rentabilidad.get("RENDIMIENTO SOBRE EL CAPITAL COMUN")
            ]
        }) 
        df.index = [
            "Año", "Utilidad neta", "Ventas", "MARGEN DE UTILIDAD", 
            "Utilidad bruta", "MARGEN DE UTILIDAD BRUTA", "Utilidad de operacion", "MARGEN DE UTILIDAD OPERATIVA", 
            "Total activos", "RENDIMIENTO SOBRE LOS ACTIVOS TOTALES", "Capital contable", "RENDIMIENTO SOBRE EL PATRIMONIO", 
            "Capital social", "RENDIMIENTO SOBRE EL CAPITAL COMUN"
        ]
        print("\nRazón de Rentabilidad:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar la razón de rentabilidad: {e}\n"
    
def mostrar_bursatilidad(bursatilidad: dict) -> str:
    try:
        df = pd.DataFrame({
            "Valor": [
                bursatilidad.get("Año",0), bursatilidad.get("Capital social", 0), bursatilidad.get("Numero de acciones", 0), bursatilidad.get("R_V_N", 0),
                " ", bursatilidad.get("Capital contable", 0), bursatilidad.get("Numero de acciones", 0), bursatilidad.get("R_V_L", 0),
                " ", bursatilidad.get("Valor en mercado", 0), bursatilidad.get("Valor en libros", 0), bursatilidad.get("R_V_ML", 0),
                " ", bursatilidad.get("Utilidad del ejercicio", 0), bursatilidad.get("Numero de acciones", 0), bursatilidad.get("Valor por accion", 0),
                " ", bursatilidad.get("Valor en mercado", 0), bursatilidad.get("Utilidad x accion", 0), bursatilidad.get("R_P_U", 0),
                " ", bursatilidad.get("Utilidad por accion", 0), bursatilidad.get("Valor en libros", 0), bursatilidad.get("R_R_A", 0),
                " ", bursatilidad.get("Utilidad x accion", 0), bursatilidad.get("Valor nominal", 0), bursatilidad.get("R_U_V", 0)
            ]
        }, index=[
            "Año", "Capital social", "No. acciones", "Valor Nominal",
            "VALOR EN LIBROS", "Capital contable", "No. acciones", "Valor en Libros",
            "VALOR MERCADO / VALOR LIBROS", " alor en mercado", "Valor en libros", "Valor M/L",
            "UTILIDAD POR ACCIÓN", "Utilidad del ejercicio", "No. acciones", "Utilidad por Acción",
            "RAZÓN PRECIO / U", "Valor mercado", "Utilidad x acción", "Razón",
            "RENTABILIDAD POR ACCIÓN", "Utilidad x acción", "Valor en libros", "Rentabilidad",
            "UTILIDAD / VALOR NOMINAL", "Utilidad x acción", "Valor nominal", "Utilidad"
        ])

        pd.options.display.float_format = '{:,.2f}'.format
        print("\nBursatilidad:\n")
        print(df.to_string(justify="right"))
        return "\nTabla de bursatilidad mostrada correctamente.\n"
    except Exception as e:
        return f"Error al mostrar bursatilidad: {e}\n"

def mostrar_analisis_dupont(analisis_dupont: dict) -> str:
    try:
        df = pd.DataFrame({
            "Valor":[
                analisis_dupont.get("Año"), analisis_dupont.get("Utilidad neta"), analisis_dupont.get("Ventas"),"",
                analisis_dupont.get("Total de activos"),"", analisis_dupont.get("Capital Contable"),"", ""
            ],
            "Resultado": ["","","",analisis_dupont.get("Margen de utilidad neta"),
                "",analisis_dupont.get("Rotacion de activos totales"),"",
                analisis_dupont.get("Razon de endeudamiento sobre patrimonio"),
                analisis_dupont.get("Rendimiento sobre capital (ROE)")
            ]
        })
        df.index = [
            "Año",
            "Utilidad neta",
            "Ventas",
            "Margen de utilidad neta",
            "Total de activos",
            "Rotacion de activos totales",
            "Capital Contable",
            "Razon de endeudamiento sobre patrimonio",
            "Rendimiento sobre capital (ROE)"
        ]
        print("\nAnalisis DuPont:")
        pd.options.display.float_format = '{:,.2f}'.format
        return f"{df}\n"
    except Exception as e:
        return f"Error al mostrar el analisis DuPont: {e}\n"

# Funciones para la persistencia de datos utilizando pickle
def cargar_datos_catalogo(nombre_archivo) -> dict | str:
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
        return f"No se encontró el archivo '{archivo_datos}'. Iniciando con datos vacíos.\n"

def guardar_datos(datos, nombre_archivo):
    """Guarda el estado actual (diccionarios y variables) en un archivo .pkl."""
    archivo_datos = nombre_archivo
    try:
        with open(archivo_datos, "wb") as f:
            pickle.dump(datos, f)
        return "--- Datos guardados exitosamente ---\n"
    except Exception as e:
        return f"Error al guardar datos: {e}\n"

