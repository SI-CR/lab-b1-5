from math import sqrt
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

    def __lt__(self, other):
        
               
        return self.id < other.id

    def path(self):

        camino = []
        n = self

        while n != None:
            camino.insert(0,n)
            n = n.padre

        return camino
    
    
    
        
        
        
    def print_path(path):
        for i in range(0, len(path)-1):
                if path[i].padre != None and path[i].accion != None:
                    print("["+str(path[i].id)+"]" + "["+str("{:.2f}").format(path[i].costo)+",[(" + str(path[i].estado.id_node)+",["+str(path[i].estado.show_nodes_to_visit(
                    )) + "])|" + str(path[i].estado.id[-6:])+"],"+str(path[i].padre.id)+","+str(path[i].accion)+","+str(path[i].profundidad)+","+str(path[i].heuristica)+","+str("{:.2f}").format(path[i].valor)+"]")

                else:
                    print("["+str(path[i].id)+"]" + "["+str("{:.2f}").format(path[i].costo)+",[(" + str(path[i].estado.id_node)+",["+str(
                        path[i].estado.show_nodes_to_visit()) + "])|" + str(path[i].estado.id[-6:])+"], None, None, 0,"+str(path[i].heuristica)+str(",{:.2f}").format(path[i].valor)+"]")
        print("["+str(path[len(path)-1].id)+"]" + "["+str("{:.2f}").format(path[len(path)-1].costo)+",[(" + str(path[len(path)-1].estado.id_node)+",["+str(path[len(path)-1].estado.nodes_to_visit) + "])|" + str(path[len(path)-1].estado.id[-6:])+"],"+str(path[len(path)-1].padre.id)+","+str(path[len(path)-1].accion)+","+str(path[len(path)-1].profundidad)+","+str(path[len(path)-1].heuristica)+","+str("{:.2f}").format(path[len(path)-1].valor)+"]")
        
