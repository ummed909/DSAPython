from Lists.simple_list import SimpleLinkedList
from Lists.doubly_list import DoublyLinkedList
from Lists.circular_list import CircularList
from Lists.header_linked_list import HeaderNodeList
from Trees.Tree import BST
from Trees.AVL_tree import AVLTree

tree = AVLTree()

tree.insert_u(10)
tree.insert_u(20)
tree.insert_u(30)
tree.insert_u(40)
tree.insert_u(25)
tree.insert_u(22)
tree.insert_u(23)
tree.insert_u(24)
tree.insert_u(21)
# tree.delete_node(24)
tree.delete_node(40)
# tree.delete_node(25)
# tree.delete_node(30)
# tree.delete_node(23)
# tree.delete_node(24)
# tree.delete_node(22)
tree.level_order_traversal()


