from math import sqrt
from Estado import Estado
from Frontera import FronteraOrdenada
from Visitados import Visitados
from Problema import Problema
from NodosArbol import NodosArbol


class Algoritmo:
    def __init__(self, nombre, problema, estrategia, grafo, heur,profMax):
        self.nombre = nombre
        self.estrategia = estrategia
        self.problema = problema
        self.grafo = grafo
        self.profMax = profMax
        self.heur = heur

    def __str__(self):
        return self.nombre


    def min_long(g):
        mini = float(100000000)
        for i in range(len(g.matrix)):
            for j in range(len(g.matrix[i])):  
                if float(g.matrix[i][j][1]) < mini:
                    mini = float(g.matrix[i][j][1])
        return mini
    
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
    
    def sec_heur(estado,grafo):
        
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
        else:
            return 0
    

    def run(self):
        fr = FronteraOrdenada()
        vis = Visitados()
        esSol = False
        valor = 0
        A1 = Algoritmo.min_long(self.grafo)
        if self.estrategia == "A*" and self.heur == "Arco":
            valor = A1 * len(self.problema.ini_state.nodes_to_visit)
        elif self.estrategia == "A*" and self.heur == "Euclidea":
            valor = min(Algoritmo.min_heur(self.problema.ini_state),Algoritmo.sec_heur(self.problema.ini_state,self.grafo)) * len(self.problema.ini_state.nodes_to_visit)
        elif self.estrategia == "Voraz" and self.heur == "Arco":
            valor = A1 * len(self.problema.ini_state.nodes_to_visit)
        elif self.estrategia == "Voraz" and self.heur == "Euclidea":
            valor = min(Algoritmo.min_heur(self.problema.ini_state),Algoritmo.sec_heur(self.problema.ini_state,self.grafo)) * len(self.problema.ini_state.nodes_to_visit)
            
        
            
        n = NodosArbol(None, self.problema.ini_state, 0, 0, None, round(valor,2), round(valor,2), self.estrategia)
        
        if self.heur == "Euclidea":
            D1 = Algoritmo.min_heur(self.problema.ini_state)

        fr.insertar(valor, n)

        while not esSol and not fr.esVacia():
            n = fr.extraer()
            # heu = A1 * len(n.estado.nodes_to_visit)
            
            if Problema.goal_state(n.estado):
                
                esSol = True
            else:
                if (n.estado.id not in vis.visitados) and (n.profundidad < self.profMax):
                    if n.estado.id[-6:] == "9b8480":
                        print(round(n.costo,2)) 
                        
                    vis.add(n.estado.id)
                    
                    sucesores = Estado.f_sucesor(
                        n.estado.id_node, n.estado.nodes_to_visit, self.grafo)
                    valor = 0  
                    
                    for sucesor in sucesores:
                           
                        D2 = Algoritmo.sec_heur(sucesor[1],self.grafo)
                           
                        if (self.estrategia == "BFS"):
                            valor = n.profundidad+1
                        elif (self.estrategia == "DFS"):
                            valor = 1/(n.profundidad + 1)
                        elif (self.estrategia == "UCS"):
                            valor = n.costo + sucesor[2]
                        elif (self.estrategia == "A*"):
                            if self.heur == "Arco":
                                valor = (n.costo + sucesor[2]) + A1 * len(sucesor[1].nodes_to_visit)
                            else:
                                valor = (n.costo + sucesor[2]) + (min(D1,D2) * len(sucesor[1].nodes_to_visit))

                        elif (self.estrategia == "Voraz"):
                            if self.heur == "Arco":
                                valor = A1 * len(sucesor[1].nodes_to_visit)
                            else:
                                valor = min(D1,Algoritmo.sec_heur(sucesor[1],self.grafo)) * len(sucesor[1].nodes_to_visit)
                         
                        if self.heur == "Arco":
                            nN = NodosArbol(n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], round(A1*len(sucesor[1].nodes_to_visit),2), round(valor,2), self.estrategia) 
                        else: 
                            nN = NodosArbol(n, sucesor[1], n.costo + sucesor[2], n.profundidad + 1, sucesor[0], round(min(D1,D2) * len(sucesor[1].nodes_to_visit),2), round(valor,2), self.estrategia) 
                        fr.insertar(nN.valor, nN)

        if esSol:
            return n.path()
        else:
            return []
