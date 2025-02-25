from Lists.double_ended_list import DoubleEndedList

class StackList:
    def __init__(self):
        self.top = None
        self.list = DoubleEndedList()

    def is_empty(self):
        return self.top is None

    def get_top(self):
        return self.list.get_front()

    def search(self, x):
        return self.list.search(x)

    def get_size(self):
        return self.list.length

    def display(self):
        self.list.display()

    def push(self, x):
        self.list.add_at_front(x)

    def pop(self):
        node= self.list.delete_at_front()
        if node is None:
            return None
        return node.data

