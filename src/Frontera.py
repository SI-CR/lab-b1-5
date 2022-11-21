class Frontera():
    def __init__(self):
        self.lista = []

    def insertar(self, nodo):
        self.lista.append(nodo)

    def extraer(self):
        self.lista.pop(0)
