import fileparse


def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo, 'rt') as file:
        camion = fileparse.parse_csv(file, types=[str, int, float])
        return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        precios = fileparse.parse_csv(file, has_headers=False, types=[str, float])
        precios = {prod: precio for prod, precio in precios}
        return precios


def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista


def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


def main(parametros):
    informe_camion(parametros[1], parametros[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
