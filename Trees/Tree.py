from Queues.QueueArray import Queue
from Stacks.StackArray import Stack

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # def insert(self, value):
    #     temp = self.root
    #     prev = None
    #     while temp:
    #         prev = temp
    #         if temp.data > value:
    #             temp = temp.left
    #         elif temp.data < value:
    #             temp = temp.right
    #         else:
    #             print("Tree have already node with value :", value)
    #             return
    #     if prev is None:
    #         self.root = TreeNode(value)
    #     elif prev.data > value:
    #         prev.left = TreeNode(value)
    #     else:
    #         prev.right = TreeNode(value)

    def insert(self, value):
        self.root  = self.insert_r(self.root,value)
    def insert_r(self, node, value):
        if node is None:
            return TreeNode(value)
        if node.data > value:
            node.left = self.insert_r(node.left,value)
        elif node.data < value:
            node.right = self.insert_r(node.right, value)
        return node

    def find(self, value):
        node = self.root
        while node:
            if node.data == value:
                return node
            elif node.data > value:
                node = node.left
            else:
                node = node.right
        return None

    def get_height(self):
        return self.height(self.root)

    def max(self,x,y):
        return x if x > y else y

    def height(self, node):
        if node is None:
            return 0
        else:
            return 1+ self.max(self.height(node.left), self.height(node.right))



    #_______________________pre_order_travarsal___________________
    def pre_order_traversal(self):
        if self.is_empty():
            print("Tree is empty")
        else:
            self.pre_order_t(self.root)

    def pre_order_t(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order_t(node.left)
        self.pre_order_t(node.right)

    def pre_order_travarsal_itrative(self):
        if self.is_empty():
            print("Tree is empty")
        else:
            stk = Stack()
            stk.push(self.root)
            while not stk.is_empty():
                node = stk.pop()
                print(node.data, end=" ")
                if node.right:
                    stk.push(node.right)
                if node.left:
                    stk.push(node.left)

    # ______________________in_order_travarsal_____________________
    def in_order_traversal_itrative(self):
        if self.is_empty():
            print("Tree is empty")
        else:
            stk = Stack()
            stk.push(self.root)
            node = self.root.left
            while not stk.is_empty():
                while node is not None:
                    stk.push(node)
                    node = node.left
                temp = stk.pop()
                print(temp.data, end=" ")
                if temp.right:
                    node = temp.right
                    stk.push(node)
                    node = node.left
    def in_order_travarsal(self):
        if self.is_empty():
            print("Tree is empty")
        else:
            self.in_order_t(self.root)
    def in_order_t(self, node):
        if node is None:
            return
        self.in_order_t(node.left)
        print(node.data, end=" ")
        self.in_order_t(node.right)

    #_______________________ level_order_travrsal__________________
    def level_order_traversal(self):
        if self.is_empty():
            print("Tree is empty")
            return
        que  = Queue()
        que.enqueue(self.root)
        while not que.is_empty():
            node = que.dequeue()
            print(node.data, ":", node.balance_factor, " | " , end="")
            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)

    # ______________________ post order travarsal__________________
    def post_order_travaesal(self):
        if self.is_empty():
            print("Tree is empty")
        else:
            self.post_order_t(self.root)
    def post_order_t(self, node):
        if node is None:
            return
        self.post_order_t(node.left)
        self.post_order_t(node.right)
        print(node.data, end=" ")


    # delete node
    def delete_node(self, value):
        node = self.root
        prev = None
        while node and node.data != value:
            prev = node
            if node.data > value:
                node = node.left
            else:
                node = node.right
        if node is None:
            return
        if node.right is not None and node.left is not None:
            temp = node.right
            prev = node
            while temp.left is not None:
                prev = temp
                temp = temp.left
            node.data = temp.data
            node =temp
        if node.left is not None:
            if prev is None:
                self.root = node.left
            elif prev.left == node:
                prev.left = node.left
            else:
                prev.right = node.left
        elif node.right is not None:
            if prev is None:
                self.root = node.right
            elif prev.left == node:
                prev.left = node.right
            else:
                prev.right = node.right
        else:
            if prev is None:
                self.root = None
            elif prev.left == node:
                prev.left = None
            else:
                prev.right = None
        del node











