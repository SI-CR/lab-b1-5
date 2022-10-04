#!/usr/bin/python3

import xml.sax
import xml.sax.handler


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.data = ""

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == "node":
            print("---NODE---")
            id = attrs["id"]
            print("Id:", id)
        elif tag == "edge":
            print("--EDGE--")
            source = attrs["source"]
            target = attrs["target"]
            id = attrs["id"]
            print("Source:", source, "Target:", target, "Id:", id)

    def endElement(self, tag):
        if self.CurrentData == "data":
            print("Data:", self.data)

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
