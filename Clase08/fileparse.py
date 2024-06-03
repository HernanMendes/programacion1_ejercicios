# fileparse.py
import csv


def parse_csv(iterable, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    filas = csv.reader(iterable)

    # Lee los encabezados del archivo
    indices = []
    if has_headers:
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select

    registros = []
    for i, fila in enumerate(filas):
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]

        if types:
            try:
                fila = [func(val) for func, val in zip(types, fila)]
            except ValueError as error:
                if not silence_errors:
                    print(f"Fila {i+1}: No pude convertir {fila}")
                    print(f"Fila {i+1}: Motivo: {error}")
                continue

        # Armar el diccionario
        if has_headers:
            registro = dict(zip(encabezados, fila))
        else:
            registro = tuple(fila)
        registros.append(registro)

    return registros
