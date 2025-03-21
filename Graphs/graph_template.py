from abstract_classes import ABC_Graph
from Nodes import Node
import copy
from Queues.QueueArray import Queue
from Stacks.StackArray import Stack

class Graph(ABC_Graph):
    def __init__(self, size=50):
        self.size = size
        self.vertices = 0
        self.edges = 0
        self.vertices_list = []
        self.adjecency_matrix = [[0]*self.size for i in range(self.size)]
        self.path_matrix = None

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

    def get_adjecency_matrix(self):
        temp_adjecency_matrix = [[0]*self.vertices for i in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                temp_adjecency_matrix[i][j] = self.adjecency_matrix[i][j]
        return temp_adjecency_matrix

    def get_vertices(self):
        return copy.deepcopy(self.vertices)

    def is_edge_exist(self, value_1, value_2):
        x1 = self.get_vertex_index(value_1)
        x2 = self.get_vertex_index(value_2)
        if not x1 or not x2:
            print("One of index is not found")
            return False
        if self.adjecency_matrix[x1][x2] == 0:
            return False
        return True

    def is_vertex_exist(self, value):
        for i in self.vertices_list:
            if i.value == value:
                return True
        return False

    def get_path_matrix(self):
        self.calculate_path_matrix()
        return copy.deepcopy(self.path_matrix)

    def calculate_path_matrix(self):
        self.path_matrix = self.get_adjecency_matrix()
        for i in range(self.vertices):
            for j in range(self.vertices):
                for k in range(self.vertices):
                    if self.path_matrix[j][k]==0:
                        if self.path_matrix[j][i]!=0 and self.path_matrix[i][k]!=0:
                            self.path_matrix[j][k] = 1

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.path_matrix[i][j] != 0:
                    self.path_matrix[i][j] = 1

    def refresh_nodes(self):
        for i in self.vertices_list:
            i.is_visited = False
            i.is_waiting = False

    def BFS(self, start=None):
        if start is None:
            start = 0
        else:
            start = self.get_vertex_index(start)
            if not start:
                print("start vertex is not found")
                return False
        return self.breath_first_search([],start)

    def breath_first_search(self,result_index, start=0):
        if start != 0:
            start = self.get_vertex_index(start)
            if not start:
                print("start vertex is not found")
                return
        self.refresh_nodes()
        que = Queue()
        que.enqueue(start)
        while not que.is_empty():
            x = que.dequeue()
            self.vertices_list[x].is_visited = True
            result_index.append(x)
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if self.adjecency_matrix[i][j] != 0:
                        if not self.vertices_list[j].is_visited or not self.vertices_list[j].is_waiting:
                            que.enqueue(j)
                            self.vertices_list[j].is_waiting = True

        for i in range(self.vertices):
            if not self.vertices_list[i].is_visited:
                result_index = self.breath_first_search(result_index,start=i)

        return result_index

    def DFS(self):
        













