from Lists.simple_list import Node

class DoubleEndedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_front(self):
        if self.is_empty():
            return None
        return self.head.data

    def get_tail(self):
        if self.is_empty():
            return None
        return self.tail.data

    def search(self, value):
        if self.is_empty():
            return False
        temp = self.head
        while temp.value != value:
            temp = temp.next
        if temp is None:
            return False
        else:
            return True

    def is_empty(self):
        return self.head is None

    def append(self, item):
        n = Node(item)
        if self.is_empty():
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        self.tail = n
        self.length += 1

    def add_at_front(self, item):
        n = Node(item)
        if self.is_empty():
            self.tail = n
        n.next = self.head
        self.head = n
        self.length += 1

    def delete_at_tail(self):
        if self.is_empty():
            print("The list is empty")
            return
        self.length -= 1
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        r  = temp
        if prev:
            self.tail  = prev
            prev.next = None
        else:
            self.tail = None
            self.head = None
        return r

    def delete_at_front(self):
        if self.is_empty():
            print("The list is empty")
            return
        self.length -= 1
        r = self.head
        self.head = self.head.next
        return r

    def display(self):
        if self.is_empty():
            print("The list is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next



