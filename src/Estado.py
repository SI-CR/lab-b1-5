import hashlib

class Estado():

    def __init__(self, id_node, nodes_to_visit):
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
        string = ("("+id_node + ",[" + string_nodos+"])").strip()
        return string

    def check_nodes(self,id_node, nodes_to_visit, graph):
        boolean = True
        if int(id_node) > len(graph.nodes)-1 :
            boolean = False

        for i in range(0, len(nodes_to_visit)):
            if int(nodes_to_visit[i]) > len(graph.nodes) -1 :
                boolean = False
        return boolean




