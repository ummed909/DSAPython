from abstract_classes import ABC_Graph
from Nodes import Node

class Graph(ABC_Graph):
    def __init__(self, size=50):
        self.size = size
        self.vertices = 0
        self.edges = 0
        self.vertices_list = []
        self.adjecency_matrix = [[0]*self.size for i in range(self.size)]
        self.path_matrix = [[0]*self.size for i in range(self.size)]

    def get_vertex_index(self, value):
        for i in range(self.vertices):
            if self.vertices_list[i].value == value:
                return i
        return False

    def add_vertex(self,value):
        if not self.get_vertex(value):
            print("Node is already present in network")
            return False
        self.vertices_list[self.vertices] = Node(value)
        self.vertices+=1

    def remove_vertices(self, value):
        x = self.get_vertex_index(value)
        if x is False:
            return x
        return self.vertices_list.pop(x)

    def add_edge(self, value_1, value_2, w=1):
        x1 = self.get_vertex_index(value_1)
        x2 = self.get_vertex_index(value_2)
        if not x1 or not x2:
            print("One of vertices is not found")
            return False
        self.adjecency_matrix[x1][x2] = w
        self.edges += 1
        return True

    def remove_edge(self, value_1, value_2):
        x1 = self.get_vertex_index(value_1)
        x2 = self.get_vertex_index(value_2)
        if not x1 or not x2:
            print("One of vertices os not found")
            return False
        self.adjecency_matrix[x1][x2]=0
        self.edges -=1
        return True

