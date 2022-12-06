#!/usr/bin/python3

import signal
from time import sleep
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

def handler(signum, frame):
    print("\n[!] Se ha pulsado Ctrl+C\nSaliendo del programa...")
    sleep(1)
    exit(1)

signal.signal(signal.SIGINT, handler)

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

            yActual = ""
            xActual = ""
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
                    yActual = stack[i+1]
                if stack[i] == "d6":
                    xActual = stack[i+1]
            nodo = Graph.Node(idActual, osm_idActual, yActual, xActual)
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

            adjacencyList.append((matrixes.copy()))

    def menu():
        opcion = int(
            input("¿Qué algoritmo quieres usar? (1)BFS (2)DFS (3)UCS (4)A* (5)Voraz: "))
        while opcion < 1 or opcion > 5:
            opcion = int(
                input("Opción no válida. Introduce una opción válida: "))

        if opcion == 1:
            estrategia = "BFS"
        elif opcion == 2:
            estrategia = "DFS"
        elif opcion == 3:
            estrategia = "UCS"
        elif opcion == 4:
            estrategia = "A*"
        elif opcion == 5:
            estrategia = "Voraz"
        return estrategia
    
    def mostrar_inicio(idInicial, lista):
        string = ""
        for i in range(0, len(lista)):
            string += lista[i].id + " "
        print("Id inicial:", idInicial.id, "\nIds finales:", string)

    def pedir_inicio():
        
        print("BIENVENIDO AL PROGRAMA DE ESTRATEGIAS DE BÚSQUEDA")
        sleep(1)
        lista = []
        nLista = int(input("¿Cuántos nodos a visitar quiere? "))
        id_inicial = int(input("Introduce el id del nodo inicial: "))
        try:
            id_inicial = nodes[id_inicial]
        except IndexError:
            print("El nodo no existe")
            exit(1)
        for i in range(0, nLista):
            node_id = int(input("Introduce el id del nodo a visitar: "))
            try:
                lista.append(nodes[node_id])
            except IndexError:
                print("El nodo no existe")
                exit(1)
        
        
        return id_inicial, lista

    def run(estado, grafo):
        pro = Problema("Algoritmo de búsqueda", estado, grafo)

        estrategia = XMLHandler.menu()

        algo = Algoritmo.Algoritmo(("Algoritmo "+estrategia), pro, estrategia, grafo, 1000)

        print(pro.name+": "+algo.nombre)

        path = algo.run()

        if path != []:
            NodosArbol.NodosArbol.print_path(path)
        else:
            print("No se encontró solución")

    def generar_grafo():
        parseador = xml.sax.make_parser()
        manejador = XMLHandler()
        parseador.setContentHandler(manejador)
        ruta = "/home/oem/Desktop/Universidad/LabInteligentes/LabGitHub/lab-b1-5/Grafos/CR_Capital.graphML"

        parseador.parse(ruta)
        XMLHandler.crearMatriz(nodes, edges)

        grafo = Graph.Graph("Grafo Ciu", nodes, edges, adjacencyList)
        return grafo

    def main():
        """Función que ejecuta el método principal main()
        """
        grafo = XMLHandler.generar_grafo()

        idInicial, lista = XMLHandler.pedir_inicio()
        
        XMLHandler.mostrar_inicio(idInicial, lista)
        
        lista.sort(key=lambda x: int(x.id))
        estado = Estado.Estado(idInicial.id, lista, grafo)

        XMLHandler.run(estado, grafo)



if (__name__ == "__main__"):
    XMLHandler.main()
