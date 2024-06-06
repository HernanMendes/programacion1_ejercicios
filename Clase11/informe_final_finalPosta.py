#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

# %% ejercicio 7.7
import fileparse
import lote
import formato_tabla


def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f, select=['nombre', 'cajones', 'precio'], types=[
                                     str, int, float], has_headers=True)
        camion = [lote.Lote(c['nombre'], c['cajones'], c['precio']) for c in camion]
        return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    return precios


def hacer_informe(camion, precios):
    lista = []
    for c in camion:
        cambio = precios[c.nombre] - c.precio
        t = (c.nombre, c.cajones, c.precio, cambio)
        lista.append(t)
    return lista


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt='txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


# %%
def f_principal(*argumentos):
    if len(argumentos) < 2 or len(argumentos) > 3:
        raise ValueError("Se requieren 2 o 3 argumentos: archivo_camion, archivo_precios, [fmt]")

    informe_camion(*argumentos)


if __name__ == '__main__':
    import sys
    f_principal(*sys.argv[1:])
