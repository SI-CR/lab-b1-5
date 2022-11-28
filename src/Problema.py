import Graph
import Estado

class Problema:
    
    def __init__(self, name, ini_state, graph):
        self.name = name
        self.ini_state = ini_state
        self.graph = graph
    
    def goal_state(estado):
        return True if len(estado.nodes_to_visit) == 0 else False