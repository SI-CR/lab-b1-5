#!/usr/bin/python3

class Graph:
    def __init__(self, name, nodes, edges, matrix):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        self.matrix = matrix


class Node:
    def __init__(self, id,osm_id,lon,lat):
        self.id = id
        self.osm_id = osm_id
        self.lon = lon
        self.lat = lat


class Edge:
    def __init__(self, id, source, target,long):
        self.id = id
        self.source = source
        self.target = target
        self.long = long
        


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
       
        
    def crearNodo(idNodo, edge,lista):
        
        lista.clear()
        for i in range(0, len(edge)):
            if edge[i].source == idNodo:
                lista.append(int(edge[i].target))
        lista.sort()
            
        
            
                
               
        
        
