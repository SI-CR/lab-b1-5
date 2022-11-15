import Estado

class NodosArbol():
    def __init__(self, id, padre, estado, costo, profundidad, accion, heuristica, valor):
        self.id = id
        self.padre = padre
        self.estado = estado
        self.costo = costo
        self.profundidad = profundidad
        self.accion = accion
        self.heuristica = heuristica
        self.valor = valor
        
    
    def path(self, lista):
        camino = []
        camino.append(self)
        while self.padre != 0:
            if self.padre in lista.id:
                self = lista[lista.id.index(self.padre)]
                camino.append(self)
                
        return camino
        #     camino.append(self.id)
       
    def toString(self):
        md5 = Estado.convert_to_md5(self.id)
        return "["+str(self.id)+"]"+"["+str(self.costo)+","+str(md5[-6:])+","+str(self.padre)+","+str(self.accion)+","+str(self.profundidad)+","+str(self.heuristica)+","+str(self.valor)+"]" 
        
            
    def __str__(self):
        return "id: "+str(self.id)+" padre: "+str(self.padre)+" estado: "+str(self.estado)+" costo: "+str(self.costo)+" profundidad: "+str(self.profundidad)+" accion: "+str(self.accion)+" heuristica: "+str(self.heuristica)+" valor: "+str(self.valor)