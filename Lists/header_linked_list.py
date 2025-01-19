from Lists.simple_list import Node

class HeaderNode:
    def __init__(self, name):
        self.name=name
        self.count=0
        self.next = None

class HeaderNodeList:
    def __init__(self, name):
        self.head = HeaderNode(name)

    def is_empty(self):
        return self.head.next is None

    def display(self):
        print("Name : ", self.head.name )
        print("count : ", self.head.count)
        node = self.head.next
        while node:
            print(node.data, end=" ")
            node = node.next
        print("")
        return

    def get_node_count(self):
        return self.head.count

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head.next = node
        else:
            temp = self.head.next
            while temp.next:
                temp = temp.next
            temp.next = node
        self.head.count += 1

    def add_at_start(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.head.count += 1

    def add_after_x(self, data,x):
        temp = self.head.next
        while temp.next and temp.data != x:
            temp = temp.next
        if temp.data == x:
            node = Node(data)
            node.next = temp.next
            temp.next = node
            self.head.count += 1
        else:
            print("No x is found")
        return

    def add_before_x(self, data,x):
        temp = self.head.next
        prev = None
        while temp.next and temp.data != x:
            prev = temp
            temp = temp.next
        if temp.data == x:
            if prev is None:
                self.add_at_start(data)
            else:
                node = Node(data)
                node.next = prev.next
                prev.next = node
                self.head.count += 1
        else:
            print("No x is found")

    def delete_last(self):
        if self.is_empty():
            print("The list is empty")
        else:
            node = self.head.next
            prev = self.head
            while node.next:
                prev = node
                node = node.next
            prev.next = None
            self.head.count -= 1
            del node

    def delete_at_start(self):
        if self.is_empty():
            print("The list is empty")
        else:
            node = self.head.next
            self.head.next = node.next
            self.head.count -= 1
            del node

    def delete_node_x(self,x):
        if self.is_empty():
            print("The list is empty")
        else:
            node = self.head.next
            prev = self.head
            while node.next and node.data != x:
                prev = node
                node = node.next
            if node.data == x:
                prev.next = node.next
                self.head.count -= 1
                del node






