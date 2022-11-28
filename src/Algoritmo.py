from Estado import Estado
from Frontera import FronteraOrdenada
from Visitados import Visitados
from Problema import Problema
from NodosArbol import NodosArbol


class Algoritmo:
    def __init__(self, nombre, problema,estrategia):
        self.nombre = nombre
        self.estrategia = estrategia
        self.problema = problema

    def __str__(self):
        return self.nombre

    def run(self):
        fr = FronteraOrdenada()
        vis = Visitados()
        esSol = False
        n = NodosArbol(None, self.problema.ini_state, 0, 0, None, 0, 0, self.estrategia)
        valor = 0
        fr.insertar(valor,n)
        
        while not esSol and not fr.esVacia():
            n = fr.extraer()
            if Problema.goal_state(n.estado):
                esSol = True
            else:
                if (n.estado.id_node not in vis.visitados):
                    vis.add(n.estado.id_node)
                    
                    if (n.estrategia == "BFS"):
                        valor = n.profundidad+1
                    elif (n.estrategia == "DFS"):
                        valor = 1/(n.profundidad + 1)
                    elif (n.estrategia == "UCS"):
                        valor+= n.costo
                        
                    sucesores = Estado.f_sucesor(n.id,n.estado.nodes_to_visit)
                    for sucesor in sucesores:
                        nN = NodosArbol(n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], 0, valor, self.estrategia)                      
                        fr.insertar(nN.valor,nN)

        if esSol:
            return n.path()
        else:
            return []
