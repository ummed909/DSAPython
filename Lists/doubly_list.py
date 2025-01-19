
class DoublyLinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    def add_node_in_empty_list(self, value):
        node  = DoublyLinkNode(value)
        self.head = node
        self.tail = node


    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.value, end=" ")
                current = current.next
        print("")
        return

    # display list in reverse
    def display_reverse(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.tail
            while current:
                print(current.value, end=" ")
                current = current.prev
        print("")
        return

   # add node at the end
    def append(self, value):
        node = DoublyLinkNode(value)
        if self.is_empty():
            self.add_node_in_empty_list(value)
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return

    # add node at the begning
    def add_at_start(self, value):
        node = DoublyLinkNode(value)
        if not self.is_empty():
            temp = self.head
            temp.prev = node
            node.next = temp
        else:
            self.tail = node
        self.head = node


    # add node after_x
    def add_after_x(self, value, x):
        temp = self.head
        while temp and temp.value != x:
            temp = temp.next
        if temp and temp.next is None:
            self.append(value)
        elif temp:
            node = DoublyLinkNode(value)
            node.next = temp.next
            node.next.prev = node
            node.prev = temp
            temp.next = node
        else:
            print("No x is found")

    def add_before_x(self, value,x):
        if self.is_empty():
            self.add_node_in_empty_list(value)
            return
        temp = self.head
        while temp and temp.value != x:
            temp = temp.next
        if temp == self.head:
            self.add_at_start(value)
        elif temp:
            node = DoublyLinkNode(value)
            node.prev = temp.prev
            temp.prev.next = node
            node.next = temp
            temp.prev = node

    # get the number of nodes
    def get_number_of_nodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete_start_node(self):
        if self.is_empty():
            print("List is empty")
        else:
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
               self.head = node.next
               self.head.prev= None
            del node

    def delete_end_node(self):
        if self.is_empty():
            print("List is empty")
        else:
            node = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = node.prev
                self.tail.next = None
            del node

    def delete_x_node(self,x):
        node = self.head
        while node and node.value != x:
            node = node.next
        if node:
            if node == self.tail:
                self.delete_end_node()
            elif node == self.head:
                self.delete_start_node()
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                del node
        else:
            print("No x is found")
        return







