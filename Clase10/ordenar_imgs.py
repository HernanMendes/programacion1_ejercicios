import os
import datetime


def crear_directorio(nombre_directorio):
    """Crea un directorio si no existe
    :param nombre_directorio: str, nombre del directorio a crear
    """
    if not os.path.exists(nombre_directorio):
        os.makedirs(nombre_directorio)
    else:
        print('El directorio ya existe')


def recorrer_directorio(nombre_directorio):
    """Recorre un directorio y retorna una lista con los nombres de los archivos
    :param nombre_directorio: str, nombre del directorio a recorrer
    :return: list, lista con los nombres de los archivos
    """
    files_names = []
    for root, dirs, files in os.walk(nombre_directorio):
        for name in files:
            print(os.path.join(root, name))
            files_names.append(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    return files_names


def buscar_png(files):
    """Busca los archivos con extensión .png en una lista de archivos
    :param files: list, lista con los nombres de los archivos
    :return: list, lista con los nombres de los archivos .png
    """
    files_pngs = []
    for file in files:
        if file.endswith('.png'):
            files_pngs.append(file)
    return files_pngs


def procesar_names(fname):
    """Procesa el nombre de un archivo para obtener la fecha y el nombre corregido
    :param fname: str, nombre del archivo
    :return: str, str, fecha y nombre corregido
    """
    pre_fecha = fname.split('_')[-1]
    fecha = pre_fecha.split('.')[0]
    fname_corregido = fname.replace('_'+fecha, '')
    fname_corregido = 'Data/imgs_procesadas/'+fname_corregido.split('/')[-1]
    return fecha, fname_corregido


def procesar(fname):
    """Procesa un archivo, cambia su nombre y modifica la fecha de última modificación
    :param fname: str, nombre del archivo
    """
    fecha, fname_corregido = procesar_names(fname)
    print(fecha, fname_corregido)
    os.rename(fname, fname_corregido)
    fecha = datetime.datetime.strptime(fecha, '%Y%m%d')
    ts_fecha = fecha.timestamp()
    os.utime(fname_corregido, (ts_fecha, ts_fecha))


def procesar_pngs(files_png):
    """Procesa una lista de archivos .png
    :param files_png: list, lista con los nombres de los archivos .png
    """
    for file in files_png:
        procesar(file)


def borrar_carpetas_vacias(directorio):
    """Borra las carpetas vacías de un directorio
    :param directorio: str, nombre del directorio a revisar
    """
    for root, dirs, files in os.walk(directorio):
        for name in dirs:
            if not os.listdir(os.path.join(root, name)):
                os.rmdir(os.path.join(root, name))


def main(parametros):
    """Función principal
    :param parametros: list, lista con los parámetros de entrada
    """
    directorio_leer = parametros[0]
    directorio_destino = parametros[1]

    crear_directorio(directorio_destino)
    files = recorrer_directorio(directorio_leer)
    files_png = buscar_png(files)
    procesar_pngs(files_png)
    borrar_carpetas_vacias(directorio_leer)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
