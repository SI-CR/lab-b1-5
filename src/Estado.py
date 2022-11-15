import hashlib


class Estado():

    def __init__(self, id_node, nodes_to_visit, grafo):
        self.grafo = grafo
        self.id_node = id_node
        nodes_to_visit.sort()
        self.nodes_to_visit = nodes_to_visit

    def convert_to_md5(self, string):
        id = hashlib.md5(string.encode()).hexdigest()
        return id

    def crear_string(self, id_node, nodes_to_visit):
        string_nodos = ""
        for i in range(0, len(nodes_to_visit)-1):
            string_nodos += str(nodes_to_visit[i]) + ","
        string_nodos += str(nodes_to_visit[len(nodes_to_visit)-1])
        string = ("("+id_node+",["+string_nodos+"])").strip()
        return string

    def check_nodes(self, id_node, nodes_to_visit, graph):
        boolean = True
        if int(id_node) > len(graph.nodes)-1:
            boolean = False

        for i in range(0, len(nodes_to_visit)):
            if int(nodes_to_visit[i]) > len(graph.nodes) - 1:
                boolean = False
        return boolean

    def f_sucesor(self, id, nodes_to_visit):
        lista = []
        list_ad = self.grafo.matrix
        nodos_nuevo_sucesor = []
        for i in range(0, len(list_ad)):
            if id == str(i):
                nodos_nuevo_sucesor = list_ad[i]
                break
        # (2->3, (3,[11,40,50,300]),costo(2,3))

        string_nodos = ""
        lista_por_si_acaso = []
        
        for i in range(0, len(nodos_nuevo_sucesor)):
            if nodos_nuevo_sucesor[i] in nodes_to_visit:
                lista_por_si_acaso = nodes_to_visit.copy()
                lista_por_si_acaso.remove(nodos_nuevo_sucesor[i])
                string_nodos = Estado.crear_string(self, str(nodos_nuevo_sucesor[i]), lista_por_si_acaso)
                sucesor = "("+id+"->"+str(nodos_nuevo_sucesor[i])+"," + string_nodos + ",costo("+id+","+str(nodos_nuevo_sucesor[i])+"))"
                lista.append(sucesor)
                lista_por_si_acaso.clear()
            else:
                string_nodos = Estado.crear_string(self, str(nodos_nuevo_sucesor[i]), nodes_to_visit)
                sucesor = "("+id+"->"+str(nodos_nuevo_sucesor[i])+"," + string_nodos +",costo("+id+","+str(nodos_nuevo_sucesor[i])+"))"
                lista.append(sucesor)

        return lista

     
    def __str__(self):
        return self.id_node + " " + str(self.nodes_to_visit)
