#!/usr/bin/python3

import Estado
import xml.sax
import xml.sax.handler
from Frontera import FronteraOrdenada
import Graph
import NodosArbol
import Algoritmo
from Problema import Problema


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
                if stack[i] == "d5":
                    lonActual = stack[i+1]
                if stack[i] == "d6":
                    latActual = stack[i+1]
            nodo = Graph.Node(idActual, osm_idActual, lonActual, latActual)
            nodes.append(nodo)

            stack.clear()
        if tag == "edge":

            edgeLengthActual = ""
            idEdgeActual = stack[1]
            idSourceActual = stack[2]
            idTargetActual = stack[3]

            # if idSourceAnterior == idSourceActual and idTargetAnterior == idTargetActual:
            #     pass

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

            adjacencyList.append((matrixes.copy()))

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

        lista = [nodes[248], nodes[528], nodes[896], nodes[1097]]
        idInicial = nodes[37]
        print("Id inicial: ", idInicial.id, idInicial.osm_id, idInicial.lon)
        lista.sort(key=lambda x: int(x.id))
        estado = Estado.Estado(idInicial.id, lista, grafo)
        # estado2 = Estado.Estado(50, lista, grafo)
        bool = estado.check_nodes(estado.id_node, estado.nodes_to_visit, grafo)

        # if bool:
        #     string = estado.crear_string(estado.id_node, estado.nodes_to_visit)
        #     print(string)
        #     id = estado.convert_to_md5(string)
        #     print(id)
        # else:
        #     print("No se puede crear el estado, nodos incorrectos.")

        
        # print("Sucesores: ", sucesores)
        # md5 = estado.convert_to_md5(string)
        # print(md5)
        # print(estado.__str__())

        # for i in range(0,len(grafo.nodes)):
        #print(grafo.nodes[i].id + " " + str(grafo.nodes[i].osm_id) + " " + grafo.nodes[i].lon + " " + grafo.nodes[i].lat)

        # for i in range(0,len(edges)):
        #     print(edges[i].id + " " + edges[i].source + " " + edges[i].target + " " )

        # nodo1 = NodosArbol.NodosArbol(None, estado, 0, 0, None, 0, 0, "BFS")
        # nodo = NodosArbol.NodosArbol(None, estado, 0, 0, None, 0, None, "BFS")
        # nodo3 = NodosArbol.NodosArbol(nodo, estado, 0, 0, None, 0, 7, "BFS")

        # front = FronteraOrdenada()

        # front.insertar(nodo1, 10)
        # front.insertar(nodo, 10)
        # front.insertar(nodo3, 10)

        # ola = []
        nodo = None
        for i in range(0, len(nodes)):
            if estado.id_node == nodes[i].id:
                nodo = nodes[i]
                break
            
        nodoArbol = NodosArbol.NodosArbol(None, estado, 0, 0, None, 0, 0, "UCS")
        # print(nodo.id, nodo.osm_id, nodo.lon, nodo.lat)
        # estado.nodes_to_visit.sort(key=lambda x: int(x.id))
        # print(estado.id_node.id, end=" ")
        # for i in range(0, len(estado.nodes_to_visit)):
        #     print(estado.nodes_to_visit[i].id, end=" ")
        # print()

        # print(estado.id_node.id,estado.nodes_to_visit)
        # ola = front.mostrar()

        # for i in range(0, front.lista._qsize()):
        #     print(front.lista.get(i).estado.id_node)

        # camino = nodo.path()
        # for i in range(0, len(camino)-1):
        #     print(camino[i].id, end=" -> ")
        # print(camino[len(camino)-1].id)

        # print()

        # sucesores = estado.f_sucesor(estado.id_node.id, estado.nodes_to_visit)

        pro = Problema("Soy un problema", estado, grafo)

        algo = Algoritmo.Algoritmo("Algoritmo BFS", pro, "UCS",grafo)
        path = algo.run()
        
        for i in range(0, len(path)-1):
            print(path[i].id, end=" -> ")
        print(path[len(path)-1].id)
        # camino = algo.run(estado)
        # if len(camino) == 0:
        #     print("No hay solución.")
        # else:
        #     for i in range(0, len(camino)-1):
        #         print(camino[i].id, end=" -> ")
        #     print(camino[len(camino)-1].id)


if (__name__ == "__main__"):
    XMLHandler.main()
