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
                    print("    ---DATA---")
                    key = attrs["key"]
                    print("    Key:",key)
            except ValueError:
                pass 
                
        elif tag == "edge":
            print("---EDGE---")
            source = attrs["source"]
            target = attrs["target"]
            id = attrs["id"]
            print("Source:", source, "Target:", target, "Id:", id)

    def endElement(self, tag):
        if tag == "node":
            print("Data:", self.data)
            
            self.data = ""
        # if self.CurrentData == "data":
        #     print("Data:", self.data)

        # self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "data":
            self.data = content


if (__name__ == "__main__"):
    parseador = xml.sax.make_parser()
    manejador = XMLHandler()
    parseador.setContentHandler(manejador)
    ruta = "/home/oem/Desktop/Universidad/LabInteligentes/Parte1/CR_Capital.graphML"

    parseador.parse(ruta)
