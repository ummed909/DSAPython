from fcntl import FASYNC


class Node:
    def __init__(self, value):
        self.value=value
        self.is_visited = False
        self.is_waiting = False
