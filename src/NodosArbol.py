import Estado
# para hacer Nodo.nnodos


class NodosArbol():
    nNodos = 0

    def __init__(self, padre, estado, costo, profundidad, accion, heuristica, valor,estrategia):

        self.id = NodosArbol.nNodos
        NodosArbol.nNodos += 1
        self.padre = padre
        self.estado = estado
        self.costo = costo
        self.profundidad = profundidad
        self.accion = accion
        self.heuristica = heuristica
        self.valor = valor
        self.estrategia = estrategia

    def path(self):

        camino = []
        n = self

        while n != None:
            camino.insert(0,n)
            n = n.padre

        return camino
        

    def toString(self):
        md5 = Estado.convert_to_md5(self.id)
        return "["+str(self.id)+"]"+"["+str(self.costo)+","+str(md5[-6:])+","+str(self.padre)+","+str(self.accion)+","+str(self.profundidad)+","+str(self.heuristica)+","+str(self.valor)+"]"

    def __str__(self):
        return "id: "+str(self.id)+" padre: "+str(self.padre)+" estado: "+str(self.estado)+" costo: "+str(self.costo)+" profundidad: "+str(self.profundidad)+" accion: "+str(self.accion)+" heuristica: "+str(self.heuristica)+" valor: "+str(self.valor)
