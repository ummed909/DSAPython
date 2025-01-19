from Lists.simple_list import Node


class CircularList:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.tail is None

    def display(self):
        if self.is_empty():
            print("The list is empty")
            return
        temp = self.tail.next
        while temp!=self.tail:
            print(temp.data, end=" ")
            temp = temp.next
        print(self.tail.data)

    def add_node_in_empty_list(self, value):
        self.tail = Node(value)
        self.tail.next = self.tail

    def append(self, value):
        if self.is_empty():
            self.add_node_in_empty_list(value)
        else:
            node = Node(value)
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

    def add_node_at_first(self,value):
        if self.is_empty():
            self.add_node_in_empty_list(value)
        else:
            node = Node(value)
            node.next = self.tail.next
            self.tail.next = node

    def add_after_x(self,value,x):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.tail.next
            while temp!=self.tail and temp.data !=x:
                temp = temp.next
            if temp.data == x:
                if(temp == self.tail):
                    self.append(value)
                else:
                    node = Node(value)
                    node.next = temp.next
                    temp.next = node
            else:
                print("no x is found")

    def add_before_x(self,value,x):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.tail.next
            prev = None
            while temp!=self.tail and temp.data !=x:
                prev = temp
                temp = temp.next
            if temp.data == x:
                if temp == self.tail.next:
                    self.add_node_at_first(value)
                else:
                    node = Node(value)
                    node.next = temp
                    prev.next = node
            else:
                print("no x is found")

    def delete_last_node(self):
        if self.is_empty():
            print("List is empty")
        else:
            node = self.tail
            if self.tail.next == self.tail:
                self.tail = None
            else:
                temp = self.tail.next
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = self.tail.next
                self.tail = temp
            del node

    def delete_first_node(self):
        if self.is_empty():
            print("List is empty")
        else:
            node = self.tail.next
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
            del node

    def delete_node_x(self,x):
        if self.is_empty():
            print("List is empty")
        else:
            node = self.tail.next
            prev = self.tail
            while node != self.tail and node.data != x:
                prev = node
                node = node.next
            if node.data == x:
                if node == self.tail:
                    self.tail = prev
                prev.next = node.next
                del node
            else:
                print("no x is found")

    def get_number_of_nodes(self):
        if self.is_empty():
            return 0
        count = 1
        temp = self.tail.next
        while temp != self.tail:
            temp = temp.next
            count += 1
        return count







