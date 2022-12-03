from queue import PriorityQueue

class Frontera():
    def __init__(self):
        self.lista = PriorityQueue()

    def insertar(self, valor,nodo):
        pass

    def extraer(self):
        pass

    def esVacia(self):
        pass
    
    
        
    
class FronteraOrdenada(Frontera):
    def __init__(self):
        super().__init__()

    
    def insertar(self,valor,nodo):
        self.lista.put((valor,nodo))

    
    def extraer(self):
        return self.lista.get()[1]

    def esVacia(self):
        return self.lista.empty()
    
