from Frontera import Frontera
from Visitados import Visitados
from Problema import Problema
from NodosArbol import NodosArbol


class Algoritmo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def run(self, nodoInicio):
        fr = Frontera().lista
        vis = Visitados().visitados
        esSol = False
        n = nodoInicio
        valor = 0
        
        while not esSol and len(fr.lista) > 0:
            n = fr.extraer()
            if Problema.goal_state(n.estado):
                esSol = True
            else:
                if (n.estado.Id not in vis.visitados):
                    vis.add(n.estado.Id)
                    
                    if (n.estrategia == "BFS"):
                        valor = n.profundidad
                    elif (n.estrategia == "DFS"):
                        valor = 1/(n.profundidad + 1)
                    elif (n.estrategia == "UCS"):
                        valor = n.costo
                        
                    for sucesor in Problema.sucesores(n):
                        nN = NodosArbol(n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], 0, valor, n.estrategia)
                        # for nodo in fr.lista:
                        #    if (n.valor != nN.valor):
                            
                            
                        # fr.insertar(nN)   

        if esSol:
            return n.path()
        else:
            return []
