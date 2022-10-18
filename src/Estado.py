import hashlib


class Estado():
    def __init__(self, id_node, nodes_to_visit):
        self.id_node = id_node
        self.nodes_to_visit = nodes_to_visit
        
    def convert_to_md5(self,string):
        id = hashlib.md5(string.encode()).hexdigest()
        return id
    
    def crear_string(self,id_node,nodes_to_visit):
        string_nodos = ""
        for i in range(0,len(nodes_to_visit)-1):
            string_nodos += str(nodes_to_visit[i]) + ", "
        string_nodos += str(nodes_to_visit[len(nodes_to_visit)-1])
        string = ("("+id_node + "," + str(nodes_to_visit)+")").strip()
        return string

lista = ["60", "30", "40"]
lista.sort()
estado = Estado("10", lista)
string = estado.crear_string(estado.id_node, estado.nodes_to_visit)
id = estado.convert_to_md5(string)


