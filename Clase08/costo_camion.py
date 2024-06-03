import informe_final


def costo_camion(nombre_archivo):
    costo_total = 0
    camion = informe_final.leer_camion(nombre_archivo)
    for lote in camion:
        cant_cajones = lote['cajones']
        precio_cajon = lote['precio']
        costo_total += cant_cajones * precio_cajon
    return costo_total


def main(parametros):
    costo_camion(parametros[1])


if __name__ == '__main__':
    import sys
    main(sys.argv)
