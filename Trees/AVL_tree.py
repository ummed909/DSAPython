from tabnanny import check

from Trees.node import TreeNode
from Trees.Tree import BST

class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def insert_u(self,value):
        flag = [True]
        self.root = self.insert_r(self.root, value, check=flag)


    def update_bf_for_left_node(self, node,check):
        if node.balance_factor == 0:
            node.balance_factor = 1
        elif node.balance_factor == -1:
            node.balance_factor = 0
            check[0] = False
        else:
            p = node.left
            if p.balance_factor == -1:
                node.left = self.left_rotation(node.left)
            node = self.right_rotation(node)
            node.balance_factor = 0
            check[0] = False
        return node

    def update_bf_for_right_node(self, node, check):

        if node.balance_factor == 0:
            node.balance_factor = -1
        elif node.balance_factor == 1:
            node.balance_factor = 0
            check[0] = False
        else:
            p = node.right
            if p.balance_factor == 1:
                node.right = self.right_rotation(node.right)
            node = self.left_rotation(node)
            node.balance_factor = 0
            check[0] = False

        return node

    def right_rotation(self, node):
        temp = node.left
        node.left = temp.right
        node.balance_factor=0
        if temp.right is None and node.right is not None:
            node.balance_factor = -1
        temp.right = node
        return temp

    def left_rotation(self, node):
        temp = node.right
        node.right = temp.left
        node.balance_factor=0
        if temp.left is None and node.left is not None:
            node.balance_factor = 1
        temp.left = node
        return temp

    def insert_r(self, node, value, check):
        if node is None:
            return TreeNode(value)
        if node.data > value:
            node.left = self.insert_r(node.left,value, check)
            if check[0]:
                node = self.update_bf_for_left_node(node,check)
        elif node.data < value:
            node.right = self.insert_r(node.right, value, check)
            if check[0]:
                node = self.update_bf_for_right_node(node, check)
        return node

    # deletion functionality, is not working properly --- need to work on it
    def delete_node(self, value):
        flag = [True]
        self.root = self.delete(self.root,value, check=flag)
    def delete(self, node,x, check):
        if node is None:
            return node
        if node.data == x:
            if node.left is not None and node.right is not None:
                t = node.right
                while t.left is not None:
                    t = t.left
                node.data = t.data
                node.right = self.delete(node.right,t.data, check)
            else:
                temp = node
                if node.left is not None:
                    node = node.left
                elif node.right is not None:
                    node = node.right
                else:
                    node = None
                del temp
        elif node.data < x:
            node.right = self.delete(node.right,x, check)
            if check[0]:
                node = self.update_right_node_for_delete(node,check)
        else:
            node.left = self.delete(node.left,x, check)
            if check[0]:
                node = self.update_left_node_for_delete(node,check)
        return node

    def update_left_node_for_delete(self, node, check):
        if node.balance_factor == 0:
            node.balance_factor = -1
            check[0] = False
        elif node.balance_factor == 1:
            node.balance_factor = 0
        else:
            p = node.right
            if p.balance_factor == 1:
                node.right = self.right_rotation(node.right)
            if node.right.balance_factor == 0:
                node.balance_factor = -1
                check[0] = False
            node = self.left_rotation(node)
            if node.left.balance_factor == -1:
                node.balance_factor = 1
        return node

    def update_right_node_for_delete(self, node, check):
        if node.balance_factor == 0:
            node.balance_factor = 1
            check[0] = False
        elif node.balance_factor == -1:
            node.balance_factor = 0
        else:
            p = node.left
            if p.balance_factor == -1:
                node.left = self.left_rotation(node.left)
            if node.left.balance_factor == 0:
                node.balance_factor = 1
                check[0]=False
            node = self.right_rotation(node)
            if node.right.balance_factor == 1:
                node.balance_factor = -1
        return node




