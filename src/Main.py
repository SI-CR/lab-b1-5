#!/usr/bin/python3

import Estado
import xml.sax
import xml.sax.handler
import Graph
import NodosArbol


# Definimos una serie de listas vacías.
stack = []
nodes = []
edges = []
matrixes = []
adjacencyList = []


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.data = ""

    def startElement(self, tag, attrs):
        """Resumen : Metodo que se ejecuta cuando se encuentra un elemento

        Args:
            tag (String): Nos dice si es un nodo, edge o data
            attrs (String): Atributos que contiene el elemento
        """
        self.CurrentData = tag
        if tag == "node":

            stack.clear()
            nodeId = attrs["id"]
            stack.append("Nodo")
            stack.append(nodeId)

        if tag == "edge":

            stack.clear()
            source = attrs["source"]
            target = attrs["target"]
            id = attrs["id"]
            stack.append("Edge")
            stack.append(id)
            stack.append(source)
            stack.append(target)

        if tag == "data":

            key = attrs["key"]
            stack.append(key)

    def endElement(self, tag):
        """Lee la etiqueta de cierre y elimina los elementos de la pila si se ha creado ya el objeto.

        Args:
            tag (String): Identifica si es el cierre de un nodo, edge o data
        """

        # Definición de variables.

        if tag == "node":

            lonActual = ""
            latActual = ""
            osm_idActual = ""
            idActual = stack[1]
            for i in range(0, len(stack)):

                if stack[i] == "d4":
                    cadena = stack[i + 1]
                    if cadena[0] == "[":

                        cadenaFinal = cadena[1:len(cadena) - 1]
                        cadenaFinal = cadenaFinal.split(", ")
                        cadena = cadenaFinal
                    osm_idActual = cadena
                if stack[i] == "d8":
                    lonActual = stack[i+1]
                if stack[i] == "d9":
                    latActual = stack[i+1]
            nodo = Graph.Node(idActual, osm_idActual, lonActual, latActual)
            nodes.append(nodo)

            stack.clear()
        if tag == "edge":

            edgeLengthActual = ""
            idEdgeActual = stack[1]
            idSourceActual = stack[2]
            idTargetActual = stack[3]

            if idEdgeActual != "1":

                for i in range(0, len(stack)):

                    if stack[i] == "d17":
                        edgeLengthActual = stack[i+1]
                        break
                edge = Graph.Edge(idEdgeActual, idSourceActual,
                                  idTargetActual, edgeLengthActual)
                edges.append(edge)
                stack.clear()

            self.CurrentData = ""

    def characters(self, content):
        """Lee el contenido que va dentro de las etiquetas

        Args:
            content (Datos(Lee Strings y luego lo convertiremos al tipo que toca)): Datos que tiene cada clave.
        """
        if self.CurrentData == "data":

            self.data = content
            stack.append(content)

    def crearMatriz(nodes, edges):
        """Crea la lista de adyacencia

        Args:
            nodes (Node -> List): Una lista de nodos
            edges (Edge -> List): Una lista de edges
        """
        for i in range(0, len(nodes)):
            Graph.Matrix.crearNodo(nodes[i].id, edges, matrixes)

            adjacencyList.append(matrixes.copy())

    def main():
        """Función que ejecuta el método principal main()
        """
        parseador = xml.sax.make_parser()
        manejador = XMLHandler()
        parseador.setContentHandler(manejador)
        ruta = "/home/oem/Desktop/Universidad/LabInteligentes/LabGitHub/lab-b1-5/Grafos/CR_Capital.graphML"

        parseador.parse(ruta)
        XMLHandler.crearMatriz(nodes, edges)

        # grafo = Graph.Graph(nodes, edges, matrixes, adjacencyList)

        # for i in range(0, len(adjacencyList)):
        #     print("Id:", nodes[i].id, nodes[i].osm_id, nodes[i].lon,
        #           nodes[i].lat, "Lista Adyacencia -> ", adjacencyList[i])
        grafo = Graph.Graph("Grafo Ciu", nodes, edges, adjacencyList)
        
        lista = [40, 11, 50, 1194]
        idInicial = "123"
        estado = Estado.Estado(idInicial, lista, grafo)
        bool = estado.check_nodes(estado.id_node, estado.nodes_to_visit, grafo)

        if bool:
            string = estado.crear_string(estado.id_node, estado.nodes_to_visit)
            id = estado.convert_to_md5(string)
            print("Correcto.")
        else:
            print("No se puede crear el estado, nodos incorrectos.")

        estado.f_sucesor(idInicial, lista)
        md5 = estado.convert_to_md5(string)
        print(md5)
        print(estado.__str__())

        # for i in range(0,len(grafo.nodes)):
        #     print(grafo.nodes[i].id + " " + str(grafo.nodes[i].osm_id) + " " + grafo.nodes[i].lon + " " + grafo.nodes[i].lat)

        
        nodo = NodosArbol.NodosArbol(0,"pais",estado,0,0, "su papi muñaño", 0, 0)
        nodo.path()
            
    

if (__name__ == "__main__"):
    XMLHandler.main()
