#!/usr/bin/python3

import xml.sax
import xml.sax.handler
import Graph

stack = []
nodes = []
edges = []

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.data = ""

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "node":
            print("---NODE---")
            id = attrs["id"]
            stack.append("Nodo")
            print("Id:", id)
        if tag == "data":
            try:
                if stack.index("Nodo") == 0:
                    print("Node...")
                    key = attrs["key"]
                    print("\tKey:", key)
                
            except ValueError:
                try:
                    if stack.index("Edge") == 0:
                        print("Edge...")
                        key = attrs["key"]
                        print("\tKey:", key)
                except ValueError:
                    pass
                pass

        if tag == "edge":
            print("---EDGE---")
            source = attrs["source"]
            target = attrs["target"]
            id = attrs["id"]
            stack.append("Edge")
            print("Source:", source, "Target:", target, "Id:", id)

    def endElement(self, tag):
        if tag == "node" or tag == "edge":
            stack.clear()
        if self.CurrentData == "data":
            print("\t\tData:", self.data)

        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "data":
            self.data = content


if (__name__ == "__main__"):
    parseador = xml.sax.make_parser()
    manejador = XMLHandler()
    parseador.setContentHandler(manejador)
    ruta = "/home/oem/Desktop/Universidad/LabInteligentes/Parte1/CR_Capital.graphML"

    parseador.parse(ruta)
