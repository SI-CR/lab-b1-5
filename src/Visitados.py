class Visitados:
    def __init__(self):
        self.visitados = set()

    def add(self, nodo):
        self.visitados.add(nodo)

    def contains(self, nodo):
        return nodo in self.visitados

    def __str__(self):
        return str(self.visitados)