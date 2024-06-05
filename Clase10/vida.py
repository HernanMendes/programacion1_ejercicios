import datetime


def vida_en_segundos(fecha_nac):
    fecha_nac = datetime.datetime.strptime(fecha_nac, '%d-%m-%Y')
    fecha_hoy = datetime.datetime.now()
    vida = fecha_hoy - fecha_nac
    return vida.total_seconds()


if __name__ == '__main__':
    fecha_nac = '01-08-1998'
    print(vida_en_segundos(fecha_nac))
