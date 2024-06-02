import informe_funciones


def costo_camion(nombre_archivo):
    costo_total = 0
    camion = informe_funciones.leer_camion(nombre_archivo)
    for lote in camion:
        cant_cajones = lote['cajones']
        precio_cajon = lote['precio']
        costo_total += cant_cajones * precio_cajon
    return costo_total
