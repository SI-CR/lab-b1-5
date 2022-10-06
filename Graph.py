#!/usr/bin/python3

class Graph:
    def __init__(self, name, nodes, edges, matrix):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        self.matrix = matrix


class Node:
    def __init__(self, id,data):
        self.id = id
        self.data = data


class Edge:
    def __init__(self, id, source, target):
        self.id = id
        self.source = source
        self.target = target


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
