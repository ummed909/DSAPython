class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    # get position of x
    def get_position(self,x):
        r = 0
        temp = self.head
        while temp is not None:
            r+= 1
            if temp.data == x:
                return r
            temp = temp.next
        if temp is None:
            return -1

    # search for en element
    def search(self,x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        return False

    def get_number_of_nodes(self):
        n=0
        temp = self.head
        while temp:
            n+=1
            temp = temp.next
        return n

    def is_empty(self):
        return self.head is None

    # display the hole list
    def display(self):
        if self.is_empty():
            print("Lists is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    # display only first n=5 elements
    def get_head(self, n=5):
        if self.is_empty():
            print("Lists is empty")
            return
        temp = self.head
        while temp and n>0:
            n -= 1
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    # add the node at end of the list
    def append(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
        return data

    # add the node at the begning of list
    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        return data

    # add node ater x
    def add_after_x(self, data, x):
        if self.is_empty():
            print("Lists is empty")
        else:
            temp = self.head
            while temp and temp.data != x:
                temp = temp.next
            if(temp):
                node = Node(data)
                node.next = temp.next
                temp.next = node
            else:
                print("No x is found")
        return

    # add node before x
    def add_before_x(self, data, x):
        if self.is_empty():
            print("Lists is empty")
        else:
            temp = self.head
            prv = None
            while temp and temp.data != x:
                prv = temp
                temp = temp.next
            if temp:
                if prv:
                    node = Node(data)
                    node.next = prv.next
                    prv.next = node
                else:
                    self.add(data)
            else:
                print("No x is found")
        return

    # delete first node
    def delete_first(self):
        if self.is_empty():
            print("Lists is empty")
            return None
        temp = self.head
        x = self.head.data
        self.head = self.head.next
        del temp
        return x

    # delete node x
    def delete_x(self, x):
        if self.is_empty():
            print("Lists is empty")
            return None
        if self.head.data == x:
            self.delete_first()
            return x
        temp = self.head
        prev = self.head
        while temp and temp.data != x:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
            del temp
            return x
        else:
            print("No x is found")
            return None

    # delete last node
    def delete_last(self):
        if self.is_empty():
            print("Lists is empty")
            return None
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        if prev is None:
            return self.delete_first()
        else:
            r = temp.data
            prev.next = temp.next
            del temp
            return r


