"""
    El problema estaba en el valor por defecto del parámetro contenido
    en el método __init__ de la clase Canguro.

    Al pasar una lista vacía como valor por defecto, se crea una única
    lista que es compartida por todas las instancias de la clase Canguro.
    Por lo tanto, al agregar elementos a la lista de contenido de una
    instancia, se están agregando a la lista compartida por todas las
    instancias.

    La solución es crear una nueva lista vacía cada vez que se crea una
    nueva instancia de la clase Canguro, como se muestra en el código
    corregido.

"""

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido is None:
            contenido = []
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [self.nombre + ' tiene en su marsupio:']
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


if __name__ == '__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)

    print(madre_canguro)
    print(cangurito)
