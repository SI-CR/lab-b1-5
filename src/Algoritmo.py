from math import sqrt
from Estado import Estado
from Frontera import FronteraOrdenada
from Visitados import Visitados
from Problema import Problema
from NodosArbol import NodosArbol


class Algoritmo:
    def __init__(self, nombre, problema, estrategia, grafo, profMax):
        self.nombre = nombre
        self.estrategia = estrategia
        self.problema = problema
        self.grafo = grafo
        self.profMax = profMax

    def __str__(self):
        return self.nombre

    def min_heur(estado):

        D1 = []

        for i in range(0, len(estado.nodes_to_visit)):
            valorActualx = float(estado.nodes_to_visit[i].x)
            valorActualy = float(estado.nodes_to_visit[i].y)
            if i+1 < len(estado.nodes_to_visit):
                for j in range(i+1, len(estado.nodes_to_visit)):
                    D1.append(sqrt((valorActualx-float(estado.nodes_to_visit[j].x))**2+(
                        valorActualy-float(estado.nodes_to_visit[j].y))**2))
            else:
                break

        return min(D1)


    def sec_heur(nodo,grafo):
        estado = nodo.estado
        nodo = None
        D2 = []
        for i in range(0, len(grafo.nodes)):
            if str(estado.id_node) == str(grafo.nodes[i].id):
                nodo = grafo.nodes[i]
                break
        
        valorX = float(nodo.x)
        valorY = float(nodo.y)
        
        for i in range(0, len(estado.nodes_to_visit)):
            D2.append(sqrt((valorX-float(estado.nodes_to_visit[i].x))**2+(
                valorY-float(estado.nodes_to_visit[i].y))**2))
        if len(D2) > 0:
            return min(D2)
        
        

    def run(self):
        fr = FronteraOrdenada()
        vis = Visitados()
        esSol = False
        n = NodosArbol(None, self.problema.ini_state, 0, 0, None, 0, 0, self.estrategia)
        D1 = Algoritmo.min_heur(n.estado)
        
        
        valor = 0

        fr.insertar(valor, n)

        while not esSol and not fr.esVacia():
            n = fr.extraer()
            D2 = Algoritmo.sec_heur(n,self.grafo)
            if D2 != None:
                heur = min(D1,D2)*len(n.estado.nodes_to_visit)
            else:
                heur = 0
            if Problema.goal_state(n.estado):
                esSol = True
            else:
                if (n.estado.id not in vis.visitados) and (n.profundidad < self.profMax):
                    vis.add(n.estado.id)

                    sucesores = Estado.f_sucesor(
                        n.estado.id_node, n.estado.nodes_to_visit, self.grafo)
                    valor = 0

                    for sucesor in sucesores:

                        if (self.estrategia == "BFS"):
                            valor = n.profundidad+1
                        elif (self.estrategia == "DFS"):
                            valor = 1/(n.profundidad + 1)
                        elif (self.estrategia == "UCS"):
                            valor = n.costo + sucesor[2]

                        nN = NodosArbol(
                            n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], heur, valor, self.estrategia)
                        fr.insertar(nN.valor, nN)

        if esSol:
            return n.path()
        else:
            return []
