#!/usr/bin/python3

import xml.sax
import xml.sax.handler
import Graph

stack = []
nodes = []
edges = []
matrices = []
listadelistas = []


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.data = ""

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "node":

            nodeId = attrs["id"]
            stack.append("Nodo")
            stack.append(nodeId)

        if tag == "data":
            try:
                if stack.index("Nodo") == 0:
                    key = attrs["key"]
                    stack.append(key)

            except ValueError:
                try:
                    if stack.index("Edge") == 0:
                        # print("Edge...")
                        key = attrs["key"]
                        stack.append(key)
                        # print("\tKey:", key)
                except ValueError:
                    pass
                pass

        if tag == "edge":
            
            source = attrs["source"]
            target = attrs["target"]
            id = attrs["id"]
            stack.append("Edge")
            stack.append(id)
            stack.append(source)
            stack.append(target)
          

    def endElement(self, tag):
        idEdgeActual = ""
        idSourceActual = ""
        idTargetActual = ""
        idActual = ""
        lonActual = ""
        latActual = ""
        osm_idActual = ""
        edgeLengthActual = ""

        if tag == "node":
            idActual = stack[1]
            for i in range(0, len(stack)):

                if stack[i] == "d4":
                    osm_idActual = stack[i+1]
                if stack[i] == "d8":
                    lonActual = stack[i+1]
                if stack[i] == "d9":
                    latActual = stack[i+1]
            nodo = Graph.Node(idActual, osm_idActual, lonActual, latActual)
            nodes.append(nodo)
            stack.clear()
        if tag == "edge":
            idEdgeActual = stack[1]
            idSourceActual = stack[2]
            idTargetActual = stack[3]
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
        if self.CurrentData == "data":
            try:
                if stack.index("Nodo") == 0:
                    self.data = content
                    stack.append(content)
            except ValueError:
                try:
                    if stack.index("Edge") == 0:
                        self.data = content
                        stack.append(content)
                except ValueError:
                    pass
                pass

    def crearMatriz(nodes, edges):
        for i in range(0, len(nodes)):
            Graph.Matrix.crearNodo(nodes[i].id, edges, matrices)
            listadelistas.append(matrices.copy())

    def main():
        parseador = xml.sax.make_parser()
        manejador = XMLHandler()
        parseador.setContentHandler(manejador)
        ruta = "/home/oem/Desktop/Universidad/LabInteligentes/Parte1/CR_Capital.graphML"

        parseador.parse(ruta)
        XMLHandler.crearMatriz(nodes, edges)
        for i in range(0, len(listadelistas)):
            print("Id:", nodes[i].id, "Lista Adyacencia -> ", listadelistas[i])
        grafo = Graph.Graph("Grafo Ciu", nodes, edges, listadelistas)


if (__name__ == "__main__"):
    XMLHandler.main()
