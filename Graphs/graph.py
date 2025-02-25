from Queues.QueueArray import Queue
from Stacks.StackArray import Stack
from utils.constants import *

class Node:
    def __init__(self, name):
        self.name = name
        self.is_visited = False
        self.is_waiting = False
        self.distance = INFINITY
        self.predecessor = None
        self.status = 0

class Graph:
    def __init__(self, size=20):
        self.adjMatrix = [[0] * size for i in range(size)]
        self.path_matrix = [[0] * size for i in range(size)]
        self.edges_count = -1
        self.vertex_count=-1
        self.vertices = []
        self.is_changed=True
        self.directed=False

    def is_vertex_present(self, name):
        for i in self.vertices:
            if i.name == name:
                return True
        return False

    def get_index(self, name):
        for i in range(self.vertex_count+1):
            if self.vertices[i].name == name:
                return i
        return -1


    def display(self):
        print("Name of Vertices: ")
        for i in range(self.vertex_count+1):
            print(self.vertices[i].name, end=" ")
        print("Adjecency Matrix is")
        for i in range(self.vertex_count+1):
            for j in range(self.vertex_count+1):
                print(self.adjMatrix[i][j], end=" ")
            print("")

        print("Edges are :")
        for i in range(self.vertex_count+1):
            for j in range(self.vertex_count+1):
                if self.adjMatrix[i][j] != 0:
                    print(self.vertices[i].name," -> ", self.vertices[j].name)

    def add_vertex(self, name):
        if self.is_vertex_present(name):
            return
        self.is_changed = True
        self.vertex_count+=1
        vertex = Node(name)
        self.vertices.append(vertex)


    def add_edge(self, v1, v2, w=1):
        if not (self.is_vertex_present(v1) and self.is_vertex_present(v2)):
            print("both or one of Vertices is not  present in graph")
            return
        self.is_changed = True
        v1 = self.get_index(v1)
        v2 = self.get_index(v2)

        self.adjMatrix[v1][v2] = w

    def calculate_path_matrix(self):
        x = [[0]* (self.vertex_count+1) for i in range(self.vertex_count+1)]
        for i in range(self.vertex_count+1):
            for j in range(self.vertex_count+1):
                self.path_matrix[i][j] = self.adjMatrix[i][j]

        for n in range(self.vertex_count+1):
            for i in range(self.vertex_count + 1):
                for j in range(self.vertex_count + 1):
                    for k in range(self.vertex_count + 1):
                        x[i][j] += (self.path_matrix[i][k] * self.adjMatrix[k][j])

            for i in range(self.vertex_count + 1):
                for j in range(self.vertex_count + 1):
                    self.path_matrix[i][j] += x[i][j]

    def get_path_matrix(self):
        if self.is_changed:
            self.calculate_path_matrix()
            self.is_changed = False
        for i in range(self.vertex_count+1):
            for j in range(self.vertex_count+1):
                if self.path_matrix[i][j] !=0:
                    self.path_matrix[i][j] = 1
                print(self.path_matrix[i][j], end=" ")
            print("")

    def get_unvisited_node(self):
        for i in self.vertices:
            if not i.is_visited and not i.is_waiting:
                return self.get_index(i.name)
        return -1

    def breath_first_search(self, start = None):
        queue = Queue()
        if start is None:
            vertex = self.get_unvisited_node()
        else:
            vertex = self.get_index(start)
        queue.enqueue(vertex)
        self.vertices[vertex].is_waiting = True
        while not queue.is_empty():
            vertex = queue.dequeue()
            self.vertices[vertex].visited = True
            print(self.vertices[vertex].name, end=" -> ")
            for i in range(self.vertex_count+1):
                if self.adjMatrix[vertex][i] != 0:
                    if not self.vertices[i].is_waiting and not self.vertices[i].is_visited:
                        queue.enqueue(i)
                        self.vertices[i].is_waiting = True
        vertex = self.get_unvisited_node()
        if vertex == -1:
            return
        else:
            self.breath_first_search()

    def calculte_sortest_path_undirected_graph(self, start):
        queue = Queue()
        v = self.get_index(start)
        if v == -1:
            print("start vertex is not present in graph")
            return False
        self.vertices[v].distance = 0
        self.vertices[v].is_waiting = True
        queue.enqueue(v)
        while not queue.is_empty():
            vertex = queue.dequeue()
            self.vertices[vertex].visited = True
            for i in range(self.vertex_count+1):
                if self.adjMatrix[vertex][i] != 0:
                    if not self.vertices[i].is_waiting and not self.vertices[i].is_visited:
                        queue.enqueue(i)
                        self.vertices[i].is_waiting = True
                        self.vertices[i].predecessor = vertex
                        self.vertices[i].distance = self.vertices[vertex].distance + 1
        return True

    def display_shortest_path(self, start):
        v = self.get_index(start)
        if v == -1:
            return
        for i in range(self.vertex_count+1):
            if self.vertices[i].distance == INFINITY:
                print(self.vertices[i].name, "Is not Reachable")
                continue
            print(self.vertices[i].name ," Distance is :", self.vertices[i].distance, end="| Path is :")
            print(self.vertices[i].name, end="")
            predecessor = self.vertices[i].predecessor
            while predecessor is not None:
                print(' <-',self.vertices[predecessor].name, end="")
                predecessor = self.vertices[predecessor].predecessor
            print("")


    def get_sorted_path_undirected_graph(self, start):
        if not self.calculte_sortest_path_undirected_graph(start):
            return
        self.display_shortest_path(start)

    def depth_first_search(self, start = None):
        vertex = self.get_index(start)
        if start is None:
            vertex = self.get_unvisited_node()
        if vertex == -1:
            return
        stack = Stack()
        stack.push(vertex)
        while not stack.is_empty():
            vertex = stack.pop()
            if not self.vertices[vertex].is_visited:
                print(self.vertices[vertex].name, end=" -> ")
                self.vertices[vertex].is_visited = True
                for i in range(self.vertex_count+1,0, -1):
                    if self.adjMatrix[vertex][i] != 0:
                        stack.push(i)

        for i in range(self.vertex_count+1):
            if not self.vertices[i].is_visited:
                self.depth_first_search(self.vertices[i].name)
        return

    def dfs_recusive(self, start = None):
        node = self.get_index(start)
        if node == -1:
            return
        self.dfs_r(node)
        for i in range(self.vertex_count+1):
            if not self.vertices[i].is_visited:
                self.dfs_recusive(self.vertices[i].name)

    def dfs_r(self, node):
        print(self.vertices[node].name, end="->")
        self.vertices[node].is_visited = True
        for i in range(self.vertex_count+1):
            if self.adjMatrix[node][i] != 0 and not self.vertices[i].is_visited:
                self.dfs_r(i)

    def get_min_distance(self):
        min_dis = INFINITY
        index = -1
        for i in range(self.vertex_count+1):
            if self.vertices[i].status==0:
                if self.vertices[i].distance < min_dis:
                    min_dis = self.vertices[i].distance
                    index = i
        if min_dis == INFINITY:
            return -1
        else:
            return index

    def dijkstra_algorithm(self, start = None):
        vertex = self.get_index(start)
        if vertex == -1:
            return
        self.vertices[vertex].distance = 0
        while True:
            node = self.get_min_distance()
            if node == -1:
                break
            self.vertices[node].status=1
            for i in range(self.vertex_count+1):
                if self.adjMatrix[node][i]!=0:
                    if self.vertices[i].distance > self.adjMatrix[node][i]+self.vertices[node].distance:
                        self.vertices[i].distance = self.vertices[node].distance + self.adjMatrix[node][i]
                        self.vertices[i].predecessor = node
        self.display_shortest_path(start)

    def prism_algorithm(self, start = None):
        vertex = self.get_index(start)
        if self.directed or vertex == -1:
            print("Only work on the undirected graph Or no start vertex found")
            return
        self.vertices[vertex].distance = 0
        while True:
            node = self.get_min_distance()
            if node == -1:
                break
            self.vertices[node].status=1
            for i in range(self.vertex_count+1):
                if self.adjMatrix[node][i]!=0:
                    if self.vertices[i].distance > self.adjMatrix[node][i]+self.vertices[node].distance:
                        self.vertices[i].distance = self.vertices[node].distance + self.adjMatrix[node][i]
                        self.vertices[i].predecessor = node

        for i in range(self.vertex_count+1):
            if self.vertices[i].status==0:
                print("No spanning tree is possible, graph is not connected")
            else:
                















    














