class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, n_cajones):
        self.cajones -= n_cajones

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'


if __name__ == '__main__':
    a = Lote('Pera', 100, 490.1)
    print(a.nombre)
    print(a.cajones)
    print(a.precio)
