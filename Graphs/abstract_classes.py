from abc import ABC, abstractmethod

class ABC_Graph(ABC):
    @abstractmethod
    def add_vertex(self, value):
        pass
    @abstractmethod
    def delete_vertex(self,value):
        pass
    @abstractmethod
    def add_edge(self, value_1, value_2):
        pass
    @abstractmethod
    def delete_edge(self, value_1, value_2):
        pass
    @abstractmethod
    def get_path_matrix(self):
        pass
    @abstractmethod
    def get_adjecency_matrix(self):
        pass
    @abstractmethod
    def get_vertices(self):
        pass
    @abstractmethod
    def get_edges(self):
        pass
    @abstractmethod
    def get_shortest_path(self, value):
        pass
    @abstractmethod
    def is_vertex_exist(self, value):
        pass
    @abstractmethod
    def is_edge_exist(self, value_1, value_2):
        pass
    @abstractmethod
    def breath_first_search(self, start):
        pass
    @abstractmethod
    def depth_first_search(self, start):
        pass



