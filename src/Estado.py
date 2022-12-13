import hashlib


class Estado():
    id = ""
    
#Meter aquí el grafo como variable de clase y actualizarlo
    def __init__(self, id_node,nodes_to_visit, grafo):
        self.grafo = grafo
        self.id = Estado.convert_to_md5(self, Estado.crear_string(self, id_node, nodes_to_visit),id_node)
        self.nodes_to_visit = nodes_to_visit
        self.id_node = id_node        
       

    def convert_to_md5(self, string,id_node):
        id = hashlib.md5(string.encode()).hexdigest()
        if id[-6:] == "486eff":
            print("ID: "+id+ "\n")
        return id

    def crear_string(self, id_node, nodes_to_visit):
        string_nodos = ""
        if len(nodes_to_visit) > 0:
            for i in range(0, len(nodes_to_visit)-1):
                string_nodos += str(nodes_to_visit[i].id) + ","
            string_nodos += str(nodes_to_visit[len(nodes_to_visit)-1].id)
        string = ("("+str(id_node)+",["+string_nodos+"])").strip()
        return string
    
    def f_sucesor(id, nodes_to_visit,grafo):

        list_ad = grafo.matrix
        nodos_nuevo_sucesor = []
        lista_id = []
        for i in range(0, len(nodes_to_visit)):
            lista_id.append(int(nodes_to_visit[i].id))
        
        for i in range(0, len(list_ad)):
            if str(id) == str(i):
                nodos_nuevo_sucesor = list_ad[i]
                break
        # (2->3, (3,[11,40,50,300]),costo(2,3))

        lista_por_si_acaso = []
        
        acciones = []
        accion = ""
        nuevo_estado = None
        estados_nuevos = []
        costo = 0
        
        lista_sucesores = []
        
        
        for i in range(0, len(nodos_nuevo_sucesor)):
            accion = str(id) + "->" + str(nodos_nuevo_sucesor[i][0])
            acciones.append(accion)
            nuevo_estado = Estado(nodos_nuevo_sucesor[i][0], nodes_to_visit, grafo)
            if nodos_nuevo_sucesor[i][0] in lista_id:
                lista_por_si_acaso = nodes_to_visit.copy()
                lista_por_si_acaso.remove(nuevo_estado.nodes_to_visit[lista_id.index(nodos_nuevo_sucesor[i][0])]) 
                nuevo_estado = Estado(nodos_nuevo_sucesor[i][0], lista_por_si_acaso, grafo)
            estados_nuevos.append(nuevo_estado)
            costo = grafo.matrix[int(id)][i][1]
            lista_sucesores.append((accion, nuevo_estado, costo))

        return lista_sucesores


    def show_nodes_to_visit(self):
        string = ""
        for i in range(0, len(self.nodes_to_visit)-1):
            string += str(self.nodes_to_visit[i].id) + ","
        string += str(self.nodes_to_visit[len(self.nodes_to_visit)-1].id)
        return string
     
    def __str__(self):
        return str(self.id_node) + " " + str(self.nodes_to_visit)
