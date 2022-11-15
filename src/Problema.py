import Graph
import Estado

def __init__(self, name, ini_state, goal_state, graph):
    self.name = name
    self.ini_state = ini_state
    self.goal_state = goal_state
    self.graph = graph
    
def goal_state(self, estado):
        return True if len(estado.lista) == 0 else False