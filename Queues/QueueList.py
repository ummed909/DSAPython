from Lists.double_ended_list import DoubleEndedList

class QueueList:
    def __init__(self):
        self.list = DoubleEndedList()

    def is_empty(self):
        return self.list.is_empty()

    def display(self):
        return self.list.display()

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        r = self.list.delete_at_front()
        if r is None:
            return None
        return r.data

    def get_size(self):
        return self.list.length

    def get_front(self):
        return self.list.get_front()

    def get_rear(self):
        return self.list.get_tail()