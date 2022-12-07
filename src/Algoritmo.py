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


    def min_long(g):
        mini = float(100000000)
        for i in range(len(g.matrix)):
            for j in range(len(g.matrix[i])):  
                if float(g.matrix[i][j][1]) < mini:
                    mini = float(g.matrix[i][j][1])
        return mini
    

    def run(self):
        fr = FronteraOrdenada()
        vis = Visitados()
        esSol = False
        A1 = Algoritmo.min_long(self.grafo)
        if self.estrategia == "A*" or self.estrategia == "Voraz":
            valor = A1 * len(self.problema.ini_state.nodes_to_visit)
        else:
            valor = 0
        n = NodosArbol(None, self.problema.ini_state, 0, 0, None, round(A1*len(self.problema.ini_state.nodes_to_visit),2), round(valor,2), self.estrategia)

        fr.insertar(valor, n)

        while not esSol and not fr.esVacia():
            n = fr.extraer()
            # heu = A1 * len(n.estado.nodes_to_visit)
            
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
                        elif (self.estrategia == "A*"):
                            valor = (n.costo + sucesor[2]) + A1 * len(sucesor[1].nodes_to_visit)
                        elif (self.estrategia == "Voraz"):
                            valor = A1 * len(sucesor[1].nodes_to_visit)
                         
                        
                        nN = NodosArbol(n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], round(A1*len(sucesor[1].nodes_to_visit),2), round(valor,2), self.estrategia) 
                        fr.insertar(nN.valor, nN)

        if esSol:
            return n.path()
        else:
            return []
